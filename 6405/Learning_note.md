# EE6405 — Natural Language Processing（自然语言处理）

> 课程学习笔记总览。每周一节，按周总结重点内容。
> 第一周（开课周）特别关注考核要求、任课教师、课程结构。
>
> **权威来源说明**：6405 本周**无录播转写**（`week1/` 内无 txt）。本笔记基于官方材料整理：
> - `EE6405_W1_Introduction to NLP_For Students_final ver.pdf`（Week 1 主课件，Liu Runlin 编写，41 页）
> - `Week 1 class slides and announcements.pdf`（课堂公告与教学计划，Dr. S. Supraja，4 页，含考核细节）
> - `Week 1.ipynb` / `Week 1 (1).ipynb`（preprocessing 实战 notebook）
> - `Week1MCQ.md`（练习题，用于确认重点）
>
> 因无转写，本笔记不含老师口述补充，仅据课件与代码整理。待有录播后可补充。

---

## Week 1 — 开课周：NLP 导论 + Preprocessing Techniques（预处理技术）

### 1. 课程基本信息

- **课程名称**：EE6405 **Natural Language Processing**（NLP，自然语言处理）。
- **任课教师**（据公告与课件作者）：
  - **Dr. S. Supraja**（NTU EEE）：主讲前半学期——Traditional Machine Learning 与 Deep Learning 部分（Week 1–7、9–11、13）。
  - **Dr. Simon**：主讲后半学期的 Business perspective 与 New Topics（Week 7、10–13），并负责 midterm invigilation 与 industry sharing。
  - Week 1 课件由 **Liu Runlin** 编写（PDF author 字段），Supraja 授课。
- **课程结构**（三段，取自课件 Content 图）：
  - **Traditional Machine Learning**（Dr. Supraja）
  - **Deep Learning**（Dr. Supraja）
  - **New NLP Trends / Business perspective**（Dr. Simon）

### 2. ⭐ 考核要求（重要，取自课堂公告）

| 成分 | 占比 | 时间 | 说明 |
|---|---|---|---|
| **Theory Quiz (IRA + TRA)** | **20%** | Week 4, 6, 10, 11 | IRA=Individual Readiness Assessment (15%)，TRA=Team Readiness Assessment (5%)；共 4 次 |
| **Mid-term Test** | **35%** | **Week 8，周五 9 October** | 覆盖 Week 1–6，**invigilated 现场监考**（Dr. Simon + TAs） |
| **Coding Quiz** | **20%** | Week 3, 5, 7, 9 | 共 4 次，application-based |
| **Final Capstone Group Project** | **25%** | Week 13 due | Individual 70% + Team 30% |
| **Peer Evaluation** | 0%（但未做扣 5%） | Week 13 | via Peerceptive/NTULearn |
| **合计** | 100% | | |

#### ⭐ Quiz 形式细节（务必注意）

- **闭卷**（closed-book），用 **Respondus lockdown browser** 经 NTULearn 完成，**现场 attendance**。Access code 课上提供。
- **IRA/TRA（Theory）**：
  - 20 分钟，测当周+前一周内容 + 课上 new short lecture；**无需死记，理解概念即可**（基于 lecture video + slides，不需课外资料）。
  - **每题多选多答**（multiple correct answers）。
  - **错答有扣分**（subtraction of marks，最低 0）。
  - 流程：先个人做（题序/选项随机）→ 团队讨论同一题后提交团队答案。
  - Practice IRA access code: `549608`（5 题 10 分钟）。
- **Coding Quiz**：
  - 15 分钟，测当周+前一周+课上短讲，应用题。
  - **每题单选**（single correct answer），5 题。
  - **near-miss 答案 0 分；完全错答扣分，总分可为负**。
  - 最终分数按公式缩放使最低为 0：`(((score*2)+20)/120)*100`。
    - 例：0/50 → 16.67/100；20/50 → 50/100；38/50 → 80/100。
  - Practice coding access code: `316882`。
- **Make-up quizzes**：Week 12。
- 考试覆盖规则（公告脚注）：
  - Coding quiz #3 (Week 7) 只考前一周(Week 6)；Coding quiz #4 (Week 9) 只考 Week 7。
  - IRA/TRA #3 (Week 10)、#4 (Week 11) 只考当周。
  - 其余 quiz 考当周+前一周。

#### 周历与教学节奏（取自公告 Lesson plan）

| Week | 内容 | 评估 | 节奏 |
|---|---|---|---|
| 1 | Introduction to AI and NLP, Pre-processing | Practice quizzes（不计分） | 2h |
| 2 | Linguistic Feature Extraction (POS, NER, DP) | Practice quizzes | 2h |
| 3 | Term Weighting, Topic Modeling, Dimensionality Reduction | **Coding quiz #1** | 2h |
| 4 | Classification and Clustering, Evaluation Metrics, Word Embeddings | **IRA/TRA #1** | 2h |
| 5 | Neural models (RNN, LSTM, GRU) and Hyperparameter Tuning | **Coding quiz #2** | 2h |
| 6 | Transformers and Transformer-based LLMs | **IRA/TRA #2** | 2h |
| 7 | NLP Applications in Industry | **Coding quiz #3** | — |
| — | RECESS（无课） | — | — |
| 8 | **Mid-term test（Week 1–6）周五 9 Oct** | 监考 | 2h |
| 9 | Project briefing + midterm 复习 | **Coding quiz #4** | 2h |
| 10 | Recent emerging trends (Part 1) | **IRA/TRA #3** | 3h |
| 11 | Recent emerging trends (Part 2) | **IRA/TRA #4** | 3h |
| 12 | Project feedback/consultations | Make-up quizzes | 3h |
| 13 | Industry sharing（受邀讲者） | **Group project due** | 3h |

> **教学方式**：短讲(15–20min) → quiz(15–30min) → team-based guiding questions(30–40min) → class sharing(20–30min)。强调 team-based learning。**本学年新增**：课堂活跃团队获 bonus participation 分（计入 team assessment）。
> **课前预告**：Week 1 作业 = 看 Week 2 lecture videos + 做 Jupyter notebook 练习，下周课上再做 practice quiz。

### 3. 课程目标（Course Objectives）

学完应能：
- 判断不同场景下 NLP preprocessing 技术的适用性。
- 解释传统 NLP 方法的数学推导（term weighting、feature extraction、topic modeling）。
- 在小规模问题上执行 classification/clustering 并评估性能。
- 用 Python 实现 NLP 算法。
- 区分传统与深度神经网络 NLP 技术的理论差异。
- 构建词嵌入与基于 RNN/Seq2Seq/Attention/Transformer 的模型训练。
- 描述预训练语言模型工作原理。
- 团队设计 NLP 项目解决真实应用（含 fine-tuning）。

### 4. NLP 是什么（知识内容开始）

- **NLP**：AI 的一个分支，聚焦于**理解、分析、生成**人类自然语言（口语与书面），是**人机之间的桥梁**。
- 四大用途：
  - **Language Understanding**：让计算机理解语言的意义与上下文。
  - **Sentiment Analysis**：分析文本/语音背后的情感。
  - **Machine Translation**：自动翻译。
  - **Language Generation**：生成类人文本/语音。
- **简史**：
  - 1906 Ferdinand de Saussure：语言作为科学，意义源于语言内部关系与对比。
  - 1916 《普通语言学教程》出版，结构主义语言学。
  - 1957 Chomsky：计算机要理解语言，需改变句子结构。
  - 1980s：从 rule-based（symbolic）转向统计模型（stochastic），做软的概率决策。
  - 1997 RNN 引入，2007 用于 NLP。
  - 2003 Yoshua Bengio：首个 neural language model（feed-forward NN），神经 NLP 诞生。
  - 2011 Apple Siri：首批成功的 NLP/AI 助手。
- **三种 NLP 方法（Approaches）**：
  | 方法 | 特点 | 例子 |
  |---|---|---|
  | **Symbolic** | rule-based，基于 lexica 与语义 | — |
  | **Stochastic** | 概率语言模型 | N-grams、Bayes Theorem、K-Means |
  | **Neural Model** | 神经网络方法 | BERT、LSTM、GCN 等 |

### 5. ⭐ Preprocessing Techniques（预处理技术）— Week 1 核心内容

#### 5.1 为什么需要预处理

| 技术 | 作用 |
|---|---|
| **Noise Reduction** | 移除特殊字符、标点、无关信息，清理数据 |
| **Tokenization** | 把文本切成更小单元（word/subword）便于分析 |
| **Normalization** | 标准化（lowercase、stemming、lemmatization），减小词表 |
| **Stop Word Removal** | 移除语义价值低的常见词，降噪 |
| **Handling OOV Words** | 用 unknown token 或 subword tokenization 处理 out-of-vocabulary 词 |
| **Sentence Segmentation** | 切句，逐句分析 |
| **Feature Engineering** | 提取 linguistic features（n-grams、POS tags） |

#### 5.2 RegEx（Regular Expressions，正则表达式）

- 用于**匹配、定位、管理**文本模式的字符串。
- **三类构件**：
  - **Metacharacters（元字符）**：有特殊功能的字符。
  - **Special Sequences（特殊序列）**：`\` + 字符，匹配特定集合。
  - **Sets（集合）**：`[ ]` 内的字符集合。

**Metacharacters 速查**：
| 字符 | 含义 | 例 |
|---|---|---|
| `[]` | 字符集 | `[a-m]` |
| `\` | 转义/特殊序列 | `\.` |
| `.` | 任意字符（除换行） | `c.t` |
| `^` | 开头 | `^hello` |
| `$` | 结尾 | `planet$` |
| `*` | 0 次或多次 | `he.*o` |
| `+` | 1 次或多次 | `he.+o` |
| `?` | 0 次或 1 次 | `colou?r` |
| `{}` | 精确次数 | `he.{2}o` |
| ` | ` | 或 |
| `()` | 精确匹配分组 | `(hello)+` |

**Special Sequences**：`\A`(开头)、`\b`(词边界)、`\B`(非词边界)、`\d`(数字)、`\D`(非数字)、`\s`(空白)、`\S`(非空白)、`\w`(单词字符 a-z A-Z 0-9 _)、`\W`(非单词字符)、`\Z`(结尾)。

**Sets**：`[ntu]`（任一）、`[a-d]`（范围）、`[^ntu]`（除此外）、`[0-9]`、`[a-zA-Z]`、`[+]`（字面 +）。

**RegEx 函数**：`findall()`（所有匹配列表）、`search()`（任意位置 match object）、`split()`（按匹配分割）、`sub()`（替换匹配）。

**例**：`[pP]omeranian` 匹配 Pomeranian/pomeranian；`pomeranians?` 匹配单复数；`pomeranian|retriever` 匹配两者之一；`pomeranian+` 匹配 pomeranian, pomeraniannn；`p.meranian` 匹配 pemeranian, p0meranian；`pomeranian$` 匹配行尾。

#### 5.3 NLTK（Natural Language Toolkit）

- NLP 的主要 Python API，含 preprocessing 函数：tokenization、stop word removal、lemmatization/stemming、POS tagging。

#### 5.4 Tokenization（分词）

- 把文本切成更小的 **tokens**，可为 word/character/subword(n-gram)。
- 最常见：以空格为分隔，得单词 token。
- NLTK：`word_tokenize`（分词）、`sent_tokenize`（分句）。

#### 5.5 ⭐ Stemming（词干提取）

- 把词的词形变化归约到 **stem**：Studying / Studies / Study → **Studi**（注意 stem 可能无意义，如 "Studi"）。
- 方法：去掉词尾几个字符得较短形式。
- **优点**：减少独特词数（提升模型性能）；相似词归一组；减小词表降低复杂度。
- **缺点**：
  - **Overstemming**：不相关词被归到同一 stem（university/universal/universe → universi）。
  - **Understemming**：归约不足，同义词得到不同 stem（alumnus/alumni/alumnae 未归一）。
  - **Language challenges**：形态复杂的语言（如法语动词变位多）stemmer 难设计。
- 实现：`PorterStemmer()`。

#### 5.6 ⭐ Lemmatization（词形还原）

- 把词归约到 **lemma**（字典形式）：Studying / Studies / Study → **Study**（有意义）。
- 与 stemming 区别：**只去词形变化词尾，返回字典形式**；考虑 **POS（Part-Of-Speech）** 上下文，更准确。
- **优点**：准确（考虑 POS 与上下文）。
- **缺点**：慢（每个词做形态分析）。
- 实现：`WordNetLemmatizer()`，默认把所有词当名词；需结合 POS tagging 才能正确还原（如动词 pos='v'）。

#### 5.7 Stemming vs Lemmatization 对比（Week1MCQ 重点）

| | Stemming | Lemmatization |
|---|---|---|
| 产物 | stem（可能无意义） | lemma（字典形式，有意义） |
| 方法 | 截词尾 | 形态分析 + POS |
| 速度 | 快 | 慢 |
| 准确 | 低 | 高 |
| 例子 | running→run, easily→easili, fairness→fair | running→run（pos='v'）, easily→easily |

> MCQ 真实输出参考（PorterStemmer）：`["running","runner","ran","easily","fairness","isn't"]` → `['run','runner','run','easili','fair',"isn't"]`。
> WordNetLemmatizer(pos='v')：→ `['run','runner','run','easily','fairness',"isn't"]`（easily/fairness 作动词不变；实际需 POS tag 才准确）。

#### 5.8 ⭐ Bag-of-Words (BOW)

- 用词的出现次数表示文本；**只保留词频，丢弃语法与词序**（故称 "bag"）。
- 把非结构化文本转为**定长向量**的结构化数据。
- **步骤**（课件例）：
  1. Tokenize + lowercase + 去标点 + 去停词。
  2. 建词汇表（vocabulary）。
  3. 对每句按词汇表统计词频 → 定长向量。
- 课件例：
  - S1: "never gonna give you up, never gonna let you down" → `never gon na give never gon na let`
  - S2: "never gonna run around and desert you" → `never gon na run desert`
  - 词表(7词)：never, gon, na, give, let, run, desert
  - S1 向量 `[2,2,2,1,1,0,0]`，S2 向量 `[1,1,1,0,0,1,1]`
  - 可用 **cosine similarity** 比较两句向量。
- 实现：`sklearn.feature_extraction.text.CountVectorizer`。

#### 5.9 ⭐ N-grams

- **n-gram**：从文本/语料中取的连续 n 个 token 序列。
  - Unigram: "I", "am", "the", "one", "who", "knocks"
  - Bigram: "I am", "the one", "who knocks"
  - Trigram: "I am the", "one who knocks"
- **N-gram 是概率模型**，计算句子/词序列概率：
  - `P(W) = P(w1,w2,…,wn)` 或 `P(w5 | w1,w2,w3,w4)`
  - 用 **chain rule**：`P(A,B,C,D) = P(A)·P(B|A)·P(C|A,B)·P(D|A,B,C)`
  - 句子变长时计算困难 → 用 **Markov Assumption** 简化：
    - Unigram: `P(wn|w1,…,wn-1) ≈ P(wn)`
    - Bigram: `P(wn|w1,…,wn-1) ≈ P(wn|wn-1)`
    - k-gram: `≈ P(wn|wn-k,…,wn-1)`
  - 直觉：下一个词可基于前 n 个词的概率预测。
- **Bigram 概率估计**：`P(wi|wi-1) = c(wi-1,wi) / c(wi-1)`（计数比）。
- 课件例：语料 `<s>This is a dog</s>`、`<s>This is a cat</s>`、`<s>I love my cat</s>`：
  - `P(dog|a) = 1/2 = 0.5`、`P(cat|a) = 1/2 = 0.5`、`P(</s>|cat) = 2/2 = 1` 等。

### 6. Week 1 要点小结（取自课件 Summary）

- **RegEx**：匹配/搜索/管理文本模式的字符序列。
- **Stemming**：归约到词根形式，简化分析、改善信息检索。
- **Lemmatization**：归约到字典形式(lemma)，保留语法意义、改善理解。
- **NLTK**：处理人类语言数据的 Python 库。
- **Bag of Words**：把文档转为向量，忽略语法与词序，按词频。
- **N-grams**：连续 n 词序列，用于语言建模与文本分析，捕捉局部上下文与词间关系。

### 7. Week 1 团队讨论题（Padlet，预告下周）

- Task A：如何比较 stemming 与 lemmatization（各适用何种场景）？
- Task B：去/不去 stop word 对 downstream 任务的影响？
- Task C：RegEx 主要用在哪、具体什么场景？
- Task D：最重要的预处理技术是哪个、为什么？

---

> **下周（Week 2）预告**：**Linguistic Feature Extraction**——POS（Part-Of-Speech tagging）、NER（Named Entity Recognition）、DP（Dependency Parsing）。本周 notebook 中已提到 POS tagging 是 lemmatization 的前置，下周深入。
>
> **笔记约定**：本课英文授课、英文考试，核心术语保留英文（NLP, tokenization, stemming, lemmatization, lemma/stem, POS tagging, stop word, OOV, n-gram, unigram/bigram/trigram, Bag-of-Words, RegEx, metacharacter, special sequence, set, cosine similarity, Markov assumption, chain rule, NLTK, CountVectorizer, IRA/TRA, lockdown browser 等）。中文用于组织句意与补充释义。
>
> **说明**：本周无录播转写，以上为基于课件/notebook/MCQ/公告整理。若后续补录播，可补充老师口述要点与课堂补充。
