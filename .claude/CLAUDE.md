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

- 语言：中文讲解 + **英文术语保留原词**。课程为英文授课、英文考试，术语必须保留英文以与考题对应。
  - 做法：首次出现写成 `English term（中文释义）`，之后直接用英文 term；不要让中文译名"喧宾夺主"。
  - 必须保留英文的包括：算法名/模型名（GA、EM、MCMC、HMM、Baum-Welch）、概率概念（prior、posterior、likelihood、conjugate prior、expectation、variance、covariance、PDF/PMF、IID）、问题类型（optimization、modeling、simulation、CSP/COP/FOP、search problem、NP-hard/complete）、GA 算子（fitness、selection、crossover、mutation、recombination、genotype、phenotype、chromosome）、平台名（Wooclap、NTULearn）等。
  - 中文仅用于组织句意、连接、补充释义，不替代核心术语。
- 结构：每周一个二级标题（`## Week N — 标题`），全部周汇总在同一 `Learning_note.md`。
- 开课周优先突出考核与行政信息，用表格列明占比与关键日期。
- **权威来源优先**：转写文本（`weekN.txt`）由语音识别生成，噪声多且术语常被错拼（如 "Tang" 实为 Tay Wee Peng、"Depo" 实为 Wang Lipo、"CLAP" 实为 Wooclap、"pyro" 实为 prior、"livelihood" 实为 likelihood、"gaucin" 实为 Gaussian、"data" 常指参数 θ 等）。整理时需对照同周文件夹内的官方课件 PDF 修正，以 PDF 为准；不要照抄转写错字。
- 正确术语示例：Bayes、Bernoulli、Gaussian、prior/posterior/likelihood、EM、MCMC、Wooclap、NTULearn。

## 可用 skill

- **`coursework-notes`**（`.claude/skills/coursework-notes/SKILL.md`）：把某课程每周的录播转写 `weekN.txt` + 官方课件 PDF 整理成 `Learning_note.md` 的详细教学版中文笔记（英文术语保留原词），含 ASR 转写噪声按 PDF 修正、Week 1 优先行政/考核信息、公式推导、Wooclap 例题、下一周预告等完整流程与检查清单。处理"按之前方式总结 / 完成 XXXX 课程 / 第 N 周内容"类请求时使用。
- **`quiz-predict-6405`**（`.claude/skills/quiz-predict-6405/SKILL.md`）：专门针对 EE6405（Dr. S. Supraja）的 quiz 复习与预测。基于已归档的每周 quiz 截图（`weekN/quiz/1.png..5.png`）+ MCQ.md + notebook + 课件，逆向归纳老师出题逻辑（题型分布、干扰项设计、跨周知识滚动），为下一周 quiz 生成"考点预测 + 复习清单"md 文档放到 `6405/quiz1/Week{N}_Quiz_Prep.md`。处理"6405 第 N 周 quiz 预测 / 下周 6405 quiz 复习 / 总结 6405 出题习惯"类请求时使用。与 `coursework-notes` 互补：前者整理知识点，本 skill 专注 quiz 出题逻辑。

## .gitignore

不要忽略 `.claude/`（项目级约定与 memory 随仓库管理）。转写原文 `*.txt` 可按需保留或忽略，默认保留。
