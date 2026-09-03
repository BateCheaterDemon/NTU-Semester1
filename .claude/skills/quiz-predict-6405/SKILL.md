---
name: quiz-predict-6405
description: |
  专门针对 EE6405（Dr. S. Supraja）的 quiz 复习与预测。基于已归档的每周 quiz 截图
  （weekN/quiz/1.png..5.png）+ MCQ.md + notebook + 课件，逆向归纳老师出题逻辑，
  为下一周 quiz 生成"考点预测 + 复习清单"md 文档放到对应周目录。
  适用场景：用户说"6405 第 N 周 quiz 预测"、"下周 6405 quiz 复习"、
  "总结 6405 出题习惯"等。
---

# quiz-predict-6405 — EE6405 Quiz 出题逻辑归纳 + 周预测

本 skill 专门服务 EE6405（Natural Language Processing，Dr. S. Supraja）。它与通用 `coursework-notes` skill 互补：后者整理每周**知识点笔记**，本 skill 专注**quiz 出题逻辑**——从已归档的历年/本周 quiz 截图逆向归纳老师出题习惯，并为下一周 quiz 生成考点预测文档。

## 何时使用

用户在 6405 仓库中提出以下请求时启用：

- "6405 第 N 周 quiz 预测" / "下周 6405 quiz 怎么复习"
- "总结 6405 出题习惯/出题逻辑"
- "结合本周和上周知识点预测 quiz"
- "6405 quiz 复习"

判断信号：6405 目录下 `weekN/quiz/*.png` 截图存在，或用户提到 6405 quiz/测试。

## 仓库结构（6405 专属）

```
6405/
├── weeek1/quiz1/1.png..5.png     # Week 1 quiz 截图（注意拼写 weeek1）
├── week2/quiz/1.png..5.png       # Week 2 quiz 截图
├── week3/quiz/1.png..5.png       # Week 3 quiz 截图
├── weekN/
│   ├── Week{N}MCQ.md             # 该周 MCQ 文本（practice）
│   ├── Week N.ipynb              # 该周 notebook（quiz 代码来源）
│   └── EE6405_W{N}_*.pdf         # 该周课件
├── quiz1/                        # 已归档的分析文档
│   ├── 6405_Quiz_Habit_Analysis.md   # 跨周出题习惯总结
│   └── Week4_Quiz_Prep.md            # ← 本 skill 产出的预测文档示例
└── Learning_note.md              # 知识点笔记（coursework-notes 维护）
```

## 核心工作流

### 1. 摸清已有 quiz 材料

```bash
# 列出该课程已归档的 quiz 截图与 MCQ
ls 6405/week*/quiz/*.png 6405/weeek*/quiz*/*.png 2>/dev/null
ls 6405/week*/Week*MCQ.md 2>/dev/null
```

确定：
- 已有几周的 quiz 截图（`weekN/quiz/1.png..5.png`，每周 5 题）。
- 该周 MCQ 文本（`Week{N}MCQ.md`，practice 题）。
- 该周 notebook + 课件（quiz 代码与考点的来源）。

### 2. 读取 quiz 截图（视觉提取题面）

用 Read 工具逐张读取 `weekN/quiz/*.png`——图片会经视觉分析返回题面、代码块、选项、正确/错误标记、feedback。每周 5 张。

**截图信息丰富**，比 MCQ.md 文本多：
- 老师设置的**干扰项**（错答选项，红色高亮）。
- **正确答案**（绿色 "Correct answer 100%"）。
- **得分与扣分**（如 `-2/10`、`0/10`、`10/10`）——体现负分制。
- **feedback 框**（老师解释为什么对/错，常含 "near miss" 提示）。
- 标注 **INCORRECT/CORRECT**——反映学生实际答题情况。

提取每题：题面、代码块、5 个选项、正确答案、错误选项特征、feedback、得分。

### 3. 归纳出题逻辑（跨周）

把已归档的各周 quiz 逐题分析，归纳：

- **题型分布**：读代码问输出 / missing code / spot error / 改参数 / 概念辨析。
- **考点来源**：每周 quiz 的代码几乎**逐字摘自该周 notebook** → 复习必须跑 notebook。
- **干扰项设计**：用相邻 API/参数/拼写/下划线/单复数制造相似选项。
- **跨周知识滚动**：老师称"考本周+上周"，但实测会带**更早的知识点**（如 W3 quiz 仍考 stemming/lemmatization/reg.sub，属 W1）。归纳"滚动复现"的考点。
- **负分制陷阱**：瞎猜会倒扣（`-2/10` 常见）；near-miss 不扣分但 0 分。feedback 里 "Near misses" 是高频陷阱信号。

### 4. 预测下一周 quiz

结合：
- **下一周课件** PDF 主题与代码。
- **下一周 notebook** 的 sklearn/nltk/spaCy 调用。
- **本周 + 上周**知识点（老师声明的范围）。
- **滚动复现**的跨周考点（体感上的"再之前知识点"）。

产出：
- **预测的 5 道题题型 + 考点**（基于 notebook 代码摘录点）。
- 每题给出**可能的题面、代码、5 个选项设计思路、正确答案、干扰项陷阱**。
- **复习清单**：必跑的 notebook cell、必背的 API/参数名、易错点。

### 5. 写成 md 文档放到对应周目录

文件名：`Week{N}_Quiz_Prep.md`，放到 `6405/quiz1/`（归档所有 quiz 复习文档的集中目录，避免散落）。

文档结构（⭐ 风格规范，严格遵守）：

```markdown
# EE6405 Week N Quiz 预测与复习

> 基于 Week 1..N-1 quiz 截图归纳的出题逻辑 + Week N 课件/notebook 预测。
> Quiz 形式：(Coding 15min 5题单选负分 / IRA 20min 多选多答扣分)。

## 一、过往知识精简回顾（Week 1..N-2，quiz 会滚动复现）
...精简列表，每考点一句话 + 易错点。重在辨析，不展开推导...

## 二、前一周稍微丰富（Week N-1，声明覆盖的"上周"）
...稍详细：TF-IDF/BM25/LDA/LSA/PCA 等，含真题原文与干扰项...

## 三、本周知识详尽讲解（Week N，根据 PPT 内容，保留中英文）
...按 PPT 顺序逐节详尽整理，保留英文术语原词：
- Text Classification 四应用
- Naïve Bayes：Bayes 推导 + Laplace smoothing + worked example 手算 + notebook 代码
- SVM：hyperplane/margin/hinge loss/kernel trick 四种核 + notebook 代码
- ELM：无 backprop + 随机权重 + Moore-Penrose pseudoinverse + notebook 代码
- Gaussian Process：mean/covariance + RBF length scale + notebook 代码
- Linear Regression：squared error + gradient descent + notebook 代码
- Clustering：K-Means/Hierarchical 5 linkage/Fuzzy + notebook 代码
公式用 LaTeX $$...$$，代码直接摘自 notebook（含输出）...

## 四、⭐ 预测题目（5 道，紧密结合 notebook 代码）
### Q1..Q5
每题：题面 + 代码（直接取自 notebook）+ 5 选项 + 正确答案 + 干扰项陷阱分析。
IRA/TRA 用多选多答风格；Coding quiz 用单选风格。代码必须与 notebook 一致。

## 五、复习清单
- [ ] 必跑 notebook cell
- [ ] 必背 API/参数（精确拼写表）
- [ ] 必背概念辨析
- [ ] 易错点（干扰项陷阱）

## 六、应试策略（负分制）
...

## 附：Week 1..N-1 quiz 真题归纳表
...出题逻辑依据...
```

### ⭐ 风格规范（严格遵守）

1. **过往知识（Week 1..N-2）精简**：每考点一行表格，一句话 + 易错点。不展开推导。目的是"滚动复现提醒"。
2. **前一周（Week N-1）稍微丰富**：比过往详细，含真题原文、干扰项、易错点。因为这是声明覆盖的"上周"。
3. **本周（Week N）详尽讲解**：按 PPT 顺序逐节整理，**保留英文术语原词**（Naïve Bayes、SVM、kernel trick、length scale、Moore-Penrose pseudoinverse、agglomerative/divisive、Ward linkage 等）。公式用 LaTeX，代码直接摘自 notebook（含输出）。这是文档主体。
4. **预测题目紧密结合代码**：每题的代码块**直接取自该周 notebook**（cell 编号对应），不编造代码。干扰项用真题归纳的 5 类陷阱设计。IRA/TRA 用多选多答，Coding 用单选。
5. **中英文保留**：所有 API/概念保留英文原词，中文仅释义连接。

## 笔记撰写规范（继承 CLAUDE.md）

- **中文讲解 + 英文术语保留原词**。课程英文授课、英文考试，术语必须保留英文以与考题对应。
- 首次出现 `English term（中文释义）`，之后直接用英文 term。
- 必须保留英文的包括：sklearn API（`TfidfVectorizer`、`MultinomialNB`、`SVC`、`KMeans`、`PCA`、`f1_score`）、nltk API（`PorterStemmer`、`WordNetLemmatizer`、`word_tokenize`）、spaCy API（`doc.ents`、`token.pos_`、`token.dep_`）、NLP 概念（stemming、lemmatization、TF-IDF、bag-of-words、n-gram、stop word、POS、NER、WSD、semantic role labeling）等。
- 公式用 LaTeX `$$...$$`；代码用 ``` 代码块。
- 中文仅用于组织句意、连接、补充释义，不替代核心术语。

## 执行检查清单

对每周 quiz 预测文档，完成前自检：
- [ ] 读了该周及之前所有 `week*/quiz/*.png` 截图（视觉提取题面+答案+feedback）。
- [ ] 读了该周 `Week{N}MCQ.md`（practice 题，补充考点信号）。
- [ ] 读了该周课件 PDF 与 notebook（quiz 代码来源）。
- [ ] 归纳了跨周出题逻辑（题型/干扰项/滚动复现）。
- [ ] 预测的 5 道题每题有题面+代码+5选项+答案+陷阱分析。
- [ ] 给出复习清单（必跑 cell + 必背 API + 易错点）。
- [ ] 英文术语保留原词，未用中文译名替代核心 API/概念。
- [ ] 文档放到 `6405/quiz1/Week{N}_Quiz_Prep.md`。

## 注意事项

- 本 skill 专注 **quiz 出题逻辑与预测**，不重复 `coursework-notes` 的知识点整理工作。若用户要知识点笔记，用 `coursework-notes`；要 quiz 预测，用本 skill。两者互补。
- 截图读取依赖视觉分析，若返回 empty，重试单张读取。
- 预测基于归纳，不保证命中——重点是**覆盖可考代码点 + 暴露干扰项陷阱**，让用户考场上能识别。
- 负分制下**不猜比瞎猜安全**：没把握的题选 near-miss（不倒扣），宁可不选 IRA 多选题的不确定选项。
