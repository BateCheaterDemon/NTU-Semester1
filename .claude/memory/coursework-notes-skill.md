---
name: coursework-notes-skill
description: 把"课程转写+课件→中文学习笔记"工作流固化为可复用 skill 的位置与用法
metadata:
  type: reference
---

"课程录播转写 + 官方课件 PDF → 中文学习笔记（英文术语保留原词）"的整套工作流已固化为项目级 skill：

- **位置**：`.claude/skills/coursework-notes/SKILL.md`
- **调用**：用户说"按之前方式总结/完成 XXXX 课程""完成第 N 周内容""新加了 XXXX 同样操作"时使用。
- **覆盖**：摸清材料、pdftotext 提取 PDF、ASR 转写噪声按 PDF 修正、Week 1 优先行政/考核信息、公式推导、Wooclap 例题、下一周预告、追加而非覆盖、对齐既有笔记风格等完整流程 + 检查清单。
- 仓库根 CLAUDE.md 已有"可用 skill"小节指向它。

已有笔记（对齐此 skill 产出的风格）：6497（Week1-2）、6222、6405、6406、6407 的 `Learning_note.md`。相关规范见 [[note-language-english-terms]]、[[transcript-quality-noise]]、[[semester1-repo-purpose]]。
