#!/usr/bin/env python3
"""Build the EE6222 Assignment 2 PDF with a compact academic layout."""
import html
import importlib.util
import os
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MD2PDF = "/home/qwx/NTU/coursework/Semester1/.claude/tools/md2pdf.py"

spec = importlib.util.spec_from_file_location("md2pdf", MD2PDF)
md2pdf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(md2pdf)

CSS = """
@page { size: A4; margin: 13mm 12mm 13mm 12mm; }
* { box-sizing: border-box; }
body {
  font-family: "Liberation Serif", "DejaVu Serif", "Noto Serif CJK SC", serif;
  font-size: 9.55pt; line-height: 1.30; color: #111; margin: 0;
  text-align: justify; hyphens: auto;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
h1 {
  font-family: "Liberation Sans", "DejaVu Sans", sans-serif;
  font-size: 16pt; color: #0b3d67; border-bottom: 2px solid #0b3d67;
  padding-bottom: 4px; margin: 0 0 7px; line-height: 1.15;
}
h2 {
  font-family: "Liberation Sans", "DejaVu Sans", sans-serif;
  font-size: 12.2pt; color: #0b3d67; border-bottom: 1px solid #b9cfe2;
  padding-bottom: 2px; margin: 11px 0 4px; page-break-after: avoid;
}
h3 {
  font-family: "Liberation Sans", "DejaVu Sans", sans-serif;
  font-size: 10.1pt; color: #14618f; margin: 8px 0 2px;
  page-break-after: avoid;
}
p { margin: 2.6px 0; }
ul, ol { margin: 2.6px 0; padding-left: 17px; }
li { margin: 1.2px 0; }
table {
  border-collapse: collapse; width: 100%; margin: 4px 0;
  font-family: "Liberation Sans", "DejaVu Sans", sans-serif;
  font-size: 7.95pt; line-height: 1.20; page-break-inside: avoid;
}
th { background: #0b3d67; color: #fff; padding: 2.8px 3.5px; text-align: left;
     border: 1px solid #0b3d67; font-weight: 600; }
td { padding: 2.2px 3.5px; border: 1px solid #ccd8e3; vertical-align: top; }
tr:nth-child(even) td { background: #f6f9fc; }
blockquote {
  border-left: 3px solid #f0a500; background: #fffbf0;
  margin: 5px 0; padding: 4px 8px; font-size: 8.9pt;
  page-break-inside: avoid;
}
blockquote p { margin: 2px 0; }
strong { color: #0b3d67; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.3pt;
       background: #f0f3f6; padding: 0 2px; border-radius: 2px; color: #b03060; }
a { color: #14618f; text-decoration: none; }
hr { border: none; border-top: 1px solid #ccd8e3; margin: 8px 0; }
"""


def main():
    with open(os.path.join(HERE, "Report.md"), encoding="utf-8") as f:
        md = f.read()

    body = md2pdf.convert(md)
    title = "EE6222 Assignment 2 — Video Generation Proposal"
    page = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f"<title>{html.escape(title)}</title><style>{CSS}</style></head>"
        f"<body>{body}</body></html>"
    )

    out = os.path.join(HERE, "EE6222_Assignment2_Report.pdf")
    with tempfile.TemporaryDirectory() as td:
        hp = os.path.join(td, "report.html")
        with open(hp, "w", encoding="utf-8") as f:
            f.write(page)
        cmd = [
            "google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
            "--no-pdf-header-footer", f"--print-to-pdf={out}", f"file://{hp}",
        ]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if not os.path.exists(out):
            raise SystemExit("PDF generation failed: " + r.stderr[-1200:])
    print(f"wrote {out} ({os.path.getsize(out)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
