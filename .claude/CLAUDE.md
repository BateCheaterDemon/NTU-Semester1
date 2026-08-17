# CLAUDE.md — NTU 课程学习仓库

本仓库用于归档每个学期各课程的录播转写文本与讲义，并据此生成学习笔记。

## 仓库结构约定

```
Semester1/
├── 6497/                       # 课程编号（如 EE6497）
│   ├── week1/                  # 每周一个文件夹
│   │   ├── week1.txt           # 该周录播转写
│   │   ├── 1_Introduction.pdf  # 官方课件 / 讲义 PDF
│   │   └── Week 1.pdf          # 标注讲义版（含手写批注）
│   ├── week2/
│   └── Learning_note.md        # 该课程的学习笔记（每周总结，单文件汇总所有周）
└── .claude/
    ├── CLAUDE.md               # 本文件：仓库使用规范
    └── memory/                 # 项目级 memory（课程/学习相关事实）
```

## 工作流程

1. 每个课程一个子目录，目录名即课程编号（如 `6497`）。
2. 每周内容放在 `<课程编号>/weekN/` 文件夹内，至少包含转写 `weekN.txt`，以及讲义 PDF（如有）。
3. 每个课程目录下维护一个 `Learning_note.md`（单文件，按周用二级标题累积），逐周总结重点内容。
4. **第一周（开课周）特别重要**：重点提炼考核要求（考勤、quiz、期末、作业占比、提交规则、reference sheet 规则等），用于避免上课时间冗余、靠录播完成学习。

## 笔记撰写规范

- 语言：**中文为主**，专有名词/术语保留英文。
- 结构：每周一个二级标题（`## Week N — 标题`），全部周汇总在同一 `Learning_note.md`。
- 开课周优先突出考核与行政信息，用表格列明占比与关键日期。
- **权威来源优先**：转写文本（`weekN.txt`）由语音识别生成，噪声多且术语常被错拼（如 "Tang" 实为 Tay Wee Peng、"Depo" 实为 Wang Lipo、"CLAP" 实为 Wooclap、"pyro" 实为 prior、"livelihood" 实为 likelihood、"gaucin" 实为 Gaussian、"data" 常指参数 θ 等）。整理时需对照同周文件夹内的官方课件 PDF 修正，以 PDF 为准；不要照抄转写错字。
- 正确术语示例：Bayes、Bernoulli、Gaussian、prior/posterior/likelihood、EM、MCMC、Wooclap、NTULearn。

## .gitignore

不要忽略 `.claude/`（项目级约定与 memory 随仓库管理）。转写原文 `*.txt` 可按需保留或忽略，默认保留。
