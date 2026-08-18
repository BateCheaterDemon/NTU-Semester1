---
name: coursework-notes
description: |
  把某门 NTU 课程的每周录播转写（weekN.txt）+ 官方课件 PDF + 标注讲义 PDF
  整理成一份中文学习笔记 Learning_note.md（英文术语保留原词），并按周累积。
  适用场景：用户说"按之前的方式处理 XXXX 课程"、"完成第 N 周内容"、
  "总结这门课"等。该课程目录下通常有 weekN/weekN.txt 与若干 PDF。
---

# coursework-notes — 课程录播转写 + 课件 → 中文学习笔记

本 skill 把一门课的**录播转写文本**和**官方课件 PDF**整合成一份按周累积的中文学习笔记 `Learning_note.md`。核心难点与价值在于：转写是 ASR 语音识别输出、噪声极大且术语常被错拼，必须以官方 PDF 为权威来源修正，并保留英文术语以对应英文考题。

## 何时使用

用户在一个课程仓库（结构见下）中提出以下任意请求时启用：

- "按之前的方式处理 / 总结 / 完成 6XXX 课程"
- "完成了第 N 周内容，请继续" / "帮我总结第 N 周"
- "新加了 XXXX，同样操作"

判断信号：某课程编号目录（如 `6497/`）下存在 `weekN/weekN.txt` 或官方 PDF，且仓库根有 `.claude/CLAUDE.md` 约定了本工作流。

## 仓库结构（约定，来自仓库根 CLAUDE.md）

```
<semester>/
├── <课程编号>/                  # 如 6497
│   ├── week1/
│   │   ├── week1.txt            # 录播转写（ASR 噪声大）
│   │   ├── 1_Introduction.pdf   # 官方课件（权威）
│   │   └── Week 1.pdf           # 标注讲义（含手写批注，辅助）
│   ├── week2/
│   └── Learning_note.md         # 单文件，按周累积所有笔记
└── .claude/
    ├── CLAUDE.md                # 仓库规范
    └── skills/coursework-notes/ # 本 skill
```

## 核心工作流

### 0. 先读仓库根 CLAUDE.md

它定义了目录约定、笔记语言规范、ASR 噪声修正原则。本 skill 是对它的执行化，若与 CLAUDE.md 冲突，**以 CLAUDE.md 为准**。

### 1. 摸清该课程已有材料

```bash
# 列出课程目录结构、已有 week 文件夹、是否已有 Learning_note.md
ls -R <课程编号>/
```

确定：
- 已有第几周的 `weekN.txt`（转写）与 PDF。
- 是否已存在 `Learning_note.md`（→ 追加新周；不存在 → 新建）。
- 是否有 `Week N.pdf`（标注讲义）、notebook、MCQ 等辅助材料。

### 2. 读取并核对材料（PDF 为权威）

**逐周处理**。对第 N 周：

1. **读转写** `weekN/weekN.txt`（可能很长，分次读完；转写是 ASR 输出，噪声大，术语常错拼）。
2. **读官方课件 PDF**：
   - 用 `pdftotext` 提取（`pdftotext <pdf> /tmp/<out>.txt`）。若报 "xref not found" 警告但仍有输出，**忽略警告，照用输出**。
   - 官方 PDF 是**权威来源**，用于修正转写错字、补全公式与结构。
3. **标注讲义** `Week N.pdf`（如有）含手写批注，辅助理解但非权威，可跳过或只取关键批注。
4. **辅助材料**：notebook（看代码做了什么、输出图结论）、MCQ（确认重点考点），但不照抄。

### 3. ASR 转写噪声修正（关键）

转写常见错误模式（以 6497 为例，其他课同理需自行识别）：
- 人名错拼："Tang"→Tay Wee Peng、"Depo"→Wang Lipo、"Ji Shi Dong"→Jiang Xudong。
- 平台名："CLAP"→Wooclap。
- 术语错拼：
  - "pyro/pr"→prior、"livelihood/lilihood/hod/Lightho"→likelihood、"gaucin/galsiu/g"→Gaussian、"Bn/Berny/Bernov/nudi"→Bernoulli、"n one/n zero"→N₁/N₀、"data"→参数 θ、"ads/as"→特征 x、"five"→设计矩阵 Φ、"Psych learn"→scikit-learn。
- 正确术语：Bayes、Bernoulli、Gaussian、prior/posterior/likelihood、EM、MCMC、Wooclap、NTULearn。

**做法**：以 PDF 公式/结构为准，转写只用于取"老师口述补充"（直觉、比喻、考场提示）。不要照抄转写错字。在每周笔记开头用一段"权威来源说明"列出本周修正过的典型错拼，供日后查阅。

### 4. 撰写笔记（中文 + 英文术语保留）

#### 笔记文件结构

每课程一个 `Learning_note.md`，**单文件累积所有周**：

```markdown
# EE6XXX — 课程英文名（中文名）

> 课程学习笔记总览。每周一节，按周总结重点内容。
> 第一周（开课周）特别关注考核要求、任课教师、课程结构。
>
> **权威来源说明**：本笔记先由 weekN.txt 转写整理，再以 <官方 PDF> 核对修正。
> 转写噪声（"X"实为 Y、"Z"实为 W……），以 PDF 为准。

---

## Week N — 标题

### 1. ...
...
---

> **下一周预告**：Week N+1 将进入 <主题>（据 Week 1 进度表 / 课件 outline）。
```

- 新一周内容 **追加**到文件末尾，用 `## Week N — 标题` 二级标题分隔。
- 每周末尾给 **下一周预告**（从 Week 1 进度表或课件 outline 取下一主题）。

#### Week 1（开课周）特别处理

开课周信息量集中在行政/考核，而非知识。**必须用表格列明**：
- 考核占比（Final/Quiz/Homework/Participation/Project 等）。
- 关键时间节点（quiz 在第几周覆盖哪些周、作业 due、recess week）。
- 考勤规则（Wooclap/NTULearn、参与次数要求）。
- 任课教师分段（前 N 周谁、后 N 周谁）。
- 课程进度表（从课件 Course Content 页取，列全 13 周主题 + CA due）。

这一周优先级：行政信息 > 知识内容。目的是让用户"靠录播完成学习、避免上课时间冗余"。

#### 语言规范（来自 CLAUDE.md，严格遵守）

- **中文讲解 + 英文术语保留原词**。课程英文授课、英文考试，术语必须保留以对应考题。
- 首次出现：`English term（中文释义）`，之后直接用英文 term。不要让中文译名"喧宾夺主"。
- **必须保留英文**的包括（非穷尽）：
  - 算法/模型名：GA、EM、MCMC、HMM、Baum-Welch、CNN、Naive Bayes。
  - 概率概念：prior、posterior、likelihood、conjugate prior、expectation、variance、covariance、PDF/PMF、IID。
  - 问题类型：optimization、modeling、simulation、CSP/COP/FOP、search problem、NP-hard/complete。
  - GA 算子：fitness、selection、crossover、mutation、recombination、genotype、phenotype、chromosome。
  - 平台名：Wooclap、NTULearn。
- 中文仅用于组织句意、连接、补充释义，不替代核心术语。

#### 内容深度

- **详细教学版**，含公式与推导（用户曾明确要求"结合 pdf 内容详细讲解"）。
  - 公式用 LaTeX `$$...$$` 块；行内用 `$...$`。
  - 推导关键步骤写全（求导、令零、解方程），而非只给结论。
- 给直觉与"为什么"（如 KL divergence 解释 MLE 合理性、cross-entropy loss 从 MLE 推出的意义）。
- 用表格整理：分布的 likelihood 形式、考核占比、degree 对比、MLE vs MAP 等。
- Wooclap 练习题/课堂例题写进笔记（题干 + 答案 + 为什么），是考点信号。
- 课件末的 Practice Problems（附解答）单独成节整理。

### 5. 特殊情形：无转写文本

若该周 `weekN/` 内**无 txt**（如 6405 Week 1）：
- 在笔记开头明确声明"本周无录播转写，基于官方材料整理"。
- 来源改为 PDF + notebook + MCQ。
- 不含老师口述补充，仅据课件与代码整理。待有录播再补。
- 据课件结构照样写，但标注"无口述补充"。

### 6. 多周顺序处理

若用户一次提供多周或新加课程：
1. 先看是否已有 `Learning_note.md`：有则读其现有风格，**严格对齐**（标题层级、表格风格、公式写法、是否用"⭐"标重点、是否给下一周预告）。
2. 按 Week 顺序逐周处理（Week 1 优先行政信息）。
3. 每周处理完追加到文件末尾，最后统一更新"下一周预告"。

## 执行检查清单

对每周笔记，完成前自检：
- [ ] 读了 `weekN.txt` 转写全文。
- [ ] 提取并读了官方 PDF 文本，用于修正转写噪声。
- [ ] ASR 错拼已按 PDF 修正；开头列出本周典型错拼。
- [ ] 英文术语保留原词，未用中文译名替代核心术语。
- [ ] Week 1：考核占比表、关键日期、考勤、进度表齐全。
- [ ] 非开课周：公式与推导写全，Wooclap 例题/Practice Problems 整理。
- [ ] 末尾有"下一周预告"。
- [ ] 追加而非覆盖已有 `Learning_note.md`；对齐既有风格。

## 注意事项

- 不要忽略 `.claude/`（项目级约定与 memory 随仓库管理）。
- 转写原文 `*.txt` 默认保留（不忽略）。
- 不要照抄转写错字；不要凭空编造内容——拿不准处读 PDF 或标注讲义确认。
- PDF 提取报 xref 警告但有输出时，照用输出，不必中断。
