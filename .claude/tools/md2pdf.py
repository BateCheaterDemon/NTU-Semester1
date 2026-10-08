#!/usr/bin/env python3
"""md2pdf.py — 把 Markdown 转成排版良好的 PDF（中文友好）。

用法：python3 md2pdf.py input.md output.pdf ["文档标题"]

管线：Markdown → HTML（自带解析） → google-chrome --headless --print-to-pdf
不依赖 pandoc / LaTeX / markdown 库；依赖系统安装的 google-chrome 与 Noto CJK 字体。
"""
import html
import os
import re
import subprocess
import sys
import tempfile

CSS = """
@page { size: A4; margin: 15mm 12mm 15mm 12mm; }
* { box-sizing: border-box; }
body {
  font-family: "Noto Sans CJK SC", "Noto Sans CJK TC", "Noto Sans CJK JP", sans-serif;
  font-size: 10.5pt; line-height: 1.62; color: #1a1a1a; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
h1 { font-size: 20pt; color: #0b3d67; border-bottom: 2.5px solid #0b3d67;
     padding-bottom: 6px; margin: 0 0 14px; }
h2 { font-size: 15pt; color: #0b3d67; border-bottom: 1.2px solid #b9cfe2;
     padding-bottom: 4px; margin: 22px 0 10px; page-break-after: avoid; }
h3 { font-size: 12.5pt; color: #14618f; margin: 16px 0 7px; page-break-after: avoid; }
h4 { font-size: 11pt; color: #14618f; margin: 13px 0 6px; page-break-after: avoid; }
p { margin: 6px 0; }
ul, ol { margin: 6px 0; padding-left: 22px; }
li { margin: 3px 0; }
code { font-family: "DejaVu Sans Mono", "Noto Sans Mono", monospace; font-size: 8.8pt;
       background: #f0f3f6; padding: 1px 4px; border-radius: 3px; color: #b03060; }
pre { background: #1e1e28; color: #e8e8e8; padding: 10px 12px; border-radius: 6px;
      overflow-x: auto; page-break-inside: avoid; margin: 8px 0; }
pre code { background: none; color: #e8e8e8; padding: 0; font-size: 8.6pt;
           line-height: 1.45; white-space: pre-wrap; word-break: break-word; }
table { border-collapse: collapse; width: 100%; margin: 9px 0; font-size: 9.3pt;
        page-break-inside: avoid; }
th { background: #0b3d67; color: #fff; padding: 6px 8px; text-align: left;
     border: 1px solid #0b3d67; font-weight: 600; }
td { padding: 5px 8px; border: 1px solid #ccd8e3; vertical-align: top; }
tr:nth-child(even) td { background: #f6f9fc; }
blockquote { border-left: 4px solid #f0a500; background: #fffbf0;
             margin: 9px 0; padding: 8px 12px; page-break-inside: avoid; }
blockquote p { margin: 4px 0; }
hr { border: none; border-top: 1px solid #ccd8e3; margin: 16px 0; }
.opts { margin: 8px 0 8px 4px; }
.opts .opt { margin: 3px 0; padding-left: 14px; text-indent: -14px; }
a { color: #14618f; text-decoration: none; }
strong { color: #0b3d67; }
"""


def inline(text: str) -> str:
    """行内元素：先把 code 挖出来占位，避免其中内容被后续规则改写。"""
    slots = []

    def stash(m):
        slots.append(f'<code>{html.escape(m.group(1))}</code>')
        return f"\x00{len(slots) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)

    for i, s in enumerate(slots):
        text = text.replace(f"\x00{i}\x00", s)
    return text


def split_row(line: str):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def convert(md: str) -> str:
    out, i = [], 0
    lines = md.split("\n")

    while i < len(lines):
        line = lines[i]

        # 代码块
        if line.strip().startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(buf))}</code></pre>")
            continue

        # 表格
        if line.strip().startswith("|") and i + 1 < len(lines) and \
           re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            header = split_row(line)
            i += 2
            body = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(split_row(lines[i]))
                i += 1
            t = ["<table><thead><tr>"]
            t += [f"<th>{inline(c)}</th>" for c in header]
            t.append("</tr></thead><tbody>")
            for r in body:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        # 标题
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue

        # 分隔线
        if re.match(r"^\s*(-{3,}|\*{3,})\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # 引用块（支持内嵌 ``` 代码块）
        if line.strip().startswith(">"):
            parts = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                raw = lines[i].strip()[1:]
                if raw.strip().startswith("```"):
                    i += 1
                    code = []
                    while i < len(lines) and lines[i].strip().startswith(">"):
                        inner = lines[i].strip()[1:]
                        if inner.strip().startswith("```"):
                            break
                        code.append(inner[1:] if inner.startswith(" ") else inner)
                        i += 1
                    i += 1  # 跳过收尾围栏
                    parts.append(
                        f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
                    continue
                if raw.strip():
                    parts.append(f"<p>{inline(raw.strip())}</p>")
                i += 1
            out.append("<blockquote>" + "".join(parts) + "</blockquote>")
            continue

        # 列表
        if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
            ordered = bool(re.match(r"^\s*\d+\.", line))
            tag = "ol" if ordered else "ul"
            items, cur = [], None
            while i < len(lines) and re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i]):
                content = re.sub(r"^\s*([-*+]|\d+\.)\s+", "", lines[i])
                # 续行（缩进 2+ 且不是新条目）
                i += 1
                while i < len(lines) and lines[i].strip() and \
                        not re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i]) and \
                        re.match(r"^\s{2,}\S", lines[i]) and \
                        not lines[i].strip().startswith(("|", ">", "#", "```")):
                    content += " " + lines[i].strip()
                    i += 1
                if cur is not None:
                    items.append(cur)
                cur = content
            if cur is not None:
                items.append(cur)
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items)
                       + f"</{tag}>")
            continue

        # 选项组：连续的 "A. …" "B. …" 行 → 各占一行（不合并成段落）
        if re.match(r"^[A-Z]\.\s", line.strip()):
            opts = []
            while i < len(lines) and re.match(r"^[A-Z]\.\s", lines[i].strip()):
                opts.append(lines[i].strip())
                i += 1
            if len(opts) >= 2:
                out.append('<div class="opts">' + "".join(
                    f'<p class="opt">{inline(o)}</p>' for o in opts) + "</div>")
                continue
            i -= len(opts)  # 只有一个，交给段落逻辑处理

        # 空行
        if not line.strip():
            i += 1
            continue

        # 段落
        buf = []
        while i < len(lines) and lines[i].strip() and \
                not re.match(r"^\s*(#{1,6}\s|[-*+]\s|\d+\.\s|>|\||```)", lines[i]) and \
                not re.match(r"^\s*(-{3,}|\*{3,})\s*$", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        if buf:
            out.append(f"<p>{inline(' '.join(buf))}</p>")

    return "\n".join(out)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    src, dst = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(src)

    with open(src, encoding="utf-8") as f:
        md = f.read()

    page = (f'<!doctype html><html lang="zh"><head><meta charset="utf-8">'
            f"<title>{html.escape(title)}</title><style>{CSS}</style></head>"
            f"<body>{convert(md)}</body></html>")

    with tempfile.TemporaryDirectory() as td:
        hp = os.path.join(td, "doc.html")
        with open(hp, "w", encoding="utf-8") as f:
            f.write(page)
        cmd = ["google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
               "--no-pdf-header-footer", f"--print-to-pdf={os.path.abspath(dst)}",
               f"file://{hp}"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if not os.path.exists(dst):
            print("PDF 生成失败：", r.stderr[-800:], file=sys.stderr)
            sys.exit(1)

    print(f"✓ {dst}  ({os.path.getsize(dst) / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
