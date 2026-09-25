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

---

## Week 4 — Traditional ML Methods and NLP Applications（传统机器学习方法与 NLP 应用）

> **权威来源说明**：本周**无录播转写**（`week4/` 内无 txt）。基于官方材料整理：
> - `EE6405_W4_Traditional ML and NLP Applications_For Students.pdf`（Week 4 主课件，Dr. S. Supraja，48 页）
> - `Week 4.ipynb`（六大分类/聚类模型实战 notebook，含 sklearn 调用与输出）
> - `Week4MCQ.md`（5 题 MCQ，全部为 sklearn 代码改写题——本周考点信号）
> - `Week 4 tasks.pdf`（课堂任务）
>
> 本周对应公告 Lesson plan：**Week 4 — Classification and Clustering, Evaluation Metrics, Word Embeddings + IRA/TRA #1**。课件实际聚焦传统 ML 分类器与聚类算法，Evaluation Metrics 与 Word Embeddings 预计在课堂短讲/下周展开。无转写故不含老师口述补充。

### 1. 本周主线

Week 1–2 完成 preprocessing 与 linguistic feature extraction 后，本周回答"**如何用传统 ML 做文本分类与聚类**"。主线：
1. 把文本转成数值向量（**TF-IDF vectorization**）→ 2. 套用传统 ML 分类器（Naïve Bayes / SVM / ELM / Gaussian Process / Linear Regression）→ 3. 无监督聚类（K-Means / Hierarchical / Fuzzy）。

> ⭐ **本周 IRA/TRA #1（Theory Quiz，20%，闭卷 lockdown browser）**考当周(Week 4)+前一周(Week 3)内容 + 课上短讲。Week4MCQ 的 5 道代码题是本周考点核心信号。

### 2. Text Classification（文本分类）概述

- **Text classification**：给文档 $d$ 分配预定义类别 $c \in C = \{c_1, c_2, \dots, c_j\}$。
- **应用**（四类）：
  - **Topic Modelling**：按内容分主题。
  - **Sentiment Analysis**：分析对公司/人/产品的情感（市场研究、声誉管理）。
  - **Language Identification**：识别语言（搜索引擎查询处理）。
  - **Authorship Attribution**：作者识别（取证、网络安全）。
- **两类方法**：
  - **Rule-based classifiers**：基于人工规则。
  - **ML models**：Naïve-Bayes、SVM、ELM、Gaussian Processes、Linear Regression。

### 3. ⭐ Naïve Bayes（朴素贝叶斯）— BOW + Bayes Theorem

#### 3.1 推导（课件重点）

对文档 $d$ 与类别 $c$，由 **Bayes Theorem**：

$$P(c|d)=\frac{P(d|c)P(c)}{P(d)}$$

- 最可能类别：$\hat{c}=\arg\max P(c|d)=\arg\max P(d|c)P(c)$（**去掉分母** $P(d)$，因对所有类别相同）。
- 把文档表示为特征 $x_1,\dots,x_n$（BOW 词频）：$\hat{c}=\arg\max P(x_1,x_2,\dots,x_n|c)P(c)$。
- **"Naïve" assumption（朴素假设）**：词之间条件独立 → $P(x_1,\dots,x_n|c)=\prod_j P(x_j|c)$。
- 最终：$\hat{c}=\arg\max \prod_j P(x_j|c)P(c)$。

#### 3.2 训练（MLE）

- **Class Prior**：$P(c)=\frac{\text{count}(documents\in class\ c)}{\text{count}(total\ documents)}$。
- **Conditional Probability**：$P(w_i|c)=\frac{\text{count}(word\ w_i\in class\ c)}{\text{count}(documents\in class\ c)}$。

#### 3.3 ⭐ Zero Probability Problem + Laplace Smoothing

- **问题**：若测试词在训练集某类中未出现（如 "excellent" 仅出现在 review1 的 positive 类），则 $P(w_i|c)=0$ → 整个乘积为 0，无法分类（"zero probabilities cannot be conditioned away no matter the evidence"）。
- **解决 — Laplace (Add-One) Smoothing**：

$$P(w_i|c)=\frac{\text{count}(w_i,c)+1}{\sum_{w\in V}\text{count}(w,c)+|V|}$$

其中 $V$ = vocabulary size（词表大小）。

#### 3.4 ⭐ Worked Example（课件手算，必考）

| Doc | Words | Class |
|---|---|---|
| 1 | Hive, Arc, Hive | NTU |
| 2 | Hive, Hive, Spine | NTU |
| 3 | Hive, Tamarind | NTU |
| 4 | Eusoff, Temasek, Hive | NUS |
| 5 | Hive, Hive, Hive, Eusoff, Temasek | ? (test) |

- **Class Prior**：$P(NTU)=3/4$，$P(NUS)=1/4$。
- 词表 $V=\{$Hive, Arc, Spine, Tamarind, Eusoff, Temasek$\}$，$|V|=6$。
- 用 Laplace smoothing 算 test doc（Hive×3, Eusoff, Temasek）对各类的条件概率：
  - $P(NTU|d) \approx \frac{3}{4}\cdot\left(\frac{5+1}{8+6}\right)^3\cdot\frac{0+1}{8+6}\cdot\frac{0+1}{8+6} \approx 0.0005$（据课件数值）
  - $P(NUS|d) \approx \frac{1}{4}\cdot\left(\frac{1+1}{3+6}\right)^3\cdot\frac{1+1}{3+6}\cdot\frac{1+1}{3+6} \approx 0.0014$
- ⇒ 判 **NUS**（因 NTU 类中 Eusoff/Temasek 计数为 0，被 Laplace 拉平后 NUS 更高）。

> 课件最终数值：$P(NTU|d)\approx0.0053$，$P(NUS|d)\approx0.0056$（精确分数见 PDF 第 10 页），NUS 略高 ⇒ 判 NUS。

#### 3.5 notebook 实现

```python
from sklearn.naive_bayes import MultinomialNB, GaussianNB, CategoricalNB
nb = MultinomialNB()
nb.fit(X_train, y_train)
predictions = nb.predict(X_test)  # 本例输出 [1 1 1]，标签 [0 0 1]
```

- **MultinomialNB**：适合词频/TF-IDF（离散计数）。
- **GaussianNB**：假设特征连续高斯，适合实值特征。
- **CategoricalNB**：类别特征。

### 4. ⭐ Support Vector Machines (SVM)

#### 4.1 原理

- **目标**：在高维空间找 **hyperplane**（超平面）最好地分隔不同类别的数据点。
- **Hyperplane 方程**：$w\cdot x + b = 0$。
- **点到超平面距离**：$\frac{w\cdot x+b}{\|w\|_2}$。
- **SVM 最大化 margin**（超平面到最近数据点的距离）⇔ **最小化 $\|w\|_2$**（primal problem）。

#### 4.2 Hinge Loss + Regularization

$$c(x,y,f(x))=\begin{cases}0,& y\cdot f(x)\ge 1\\1-y\cdot f(x),&\text{otherwise}\end{cases}$$

- 预测值与真实值同号且 margin 足够 ⇒ loss = 0；否则算 loss。
- 加正则项 $C\cdot\|w\|_2$ 防止 **overfitting**。**C 越大正则越弱**（对训练数据拟合越紧）。

#### 4.3 ⭐ Kernel Trick（核技巧）

- **问题**：文本数据常**线性不可分**（linearly inseparable）。
- **Kernel trick**：把数据映射到更高维 feature space 使其线性可分；**不显式计算高维坐标**，只计算高维空间中的点积。
- **常用核**：

| 核 | 公式 | 说明 |
|---|---|---|
| **RBF / Radial Basis Function** | $K(x_1,x_2)=\exp\left(-\frac{\|x_1-x_2\|^2}{2\sigma^2}\right)$ | $\sigma$ 为核宽度 |
| **Linear** | $K(x_1,x_2)=x_1^T x_2$ | 两类学习 |
| **Polynomial** | $K(x_1,x_2)=(x_1^T x_2+1)^\rho$ | $\rho$ 为多项式阶数 |
| **Sigmoid** | $K(x_1,x_2)=\tanh(\beta_0 x_1^T x_2+\beta_1)$ | 仅特定 $\beta_0,\beta_1$ 为 Mercer 核 |

#### 4.4 notebook 实现

```python
from sklearn import svm
svm = svm.SVC(kernel='linear')
svm.fit(X_train, y_train)  # 输出 [1 1 1]，标签 [0 0 1]
```

### 5. Extreme Learning Machines (ELM)

- **浅层前馈神经网络**，**单隐藏层**，**无 backpropagation**。
- **输入→隐藏层权重随机初始化且训练中不更新**；只训练隐藏层→输出层的 $\beta$ 矩阵。
- 输出：$f_L(x)=\sum_{i=1}^L \beta_i g_i(x)=\sum_{i=1}^L \beta_i g(w_i\cdot x_j+b_i)$。
- 训练 = 解线性方程组 $H\beta=y$；因 $H$ 通常非方阵，用 **Moore-Penrose Pseudoinverse**（伪逆，可用 SVD 算）：$\beta=H^+ y$。
- notebook 用 `hpelm.ELM`，10 个 sigmoid 神经元，输出 `[0 1 1]`，标签 `[0 0 1]`。

### 6. Gaussian Processes (GP)

- **概率模型**，定义**函数上的分布**（distribution over functions），而非固定参数。
- 由 **mean function** $\mu(x)$ 与 **covariance function (kernel)** $k(x_i,x_j)$ 刻画。
- **Gram matrix** $K_x$：$K_x$ 必须正半定（positive semidefinite）。
- **RBF kernel**：$K_{RBF}(x_i,x_j)=\sigma^2\exp\left(-\frac{\|x_i-x_j\|^2}{2l^2}\right)$。
  - **$l^2$ = length scale**（核宽度）：小 → 函数波动大（wiggly）；大 → 函数更平滑。
- notebook：`GaussianProcessClassifier(kernel=RBF())`，输出 `[1 0 1]`，标签 `[0 0 1]`。

### 7. Linear Regression（线性回归）

- 假设输入与输出线性关系：$y=mx+c$。
- **Loss**（squared error）：$L(y,t)=\frac{1}{2}(y-t)^2$。
- **Cost**（均方误差）：$J(w,b)=\frac{1}{2N}\sum_{i=1}^N(wx_i+b-t_i)^2$。
- **优化 — Gradient Descent**：
  - $\frac{\partial J}{\partial w_j}>0$ ⇒ 增 $w_j$ 会增 $J$；$<0$ ⇒ 增 $w_j$ 减 $J$。
  - 更新：$w_j \leftarrow w_j - \alpha\frac{\partial J}{\partial w_j}$，$\alpha$ = **learning rate**。
- notebook：`LinearRegression().fit(X_train,y_train)`，输出连续值 `[0.667, 0.524, 0.667]`（回归任务，与分类标签 `[0 0 1]` 不同维度）。

### 8. Clustering（聚类，无监督）

- **无监督** ML，用 **distance/similarity metric** 把数据分组，发现隐藏结构，无需预先标注。

#### 8.1 K-Means

- 假设 k 个 cluster，每点属于最近的 cluster center（均值）。
- **算法**：
  1. **Initialization**：随机初始化 k 个 centroid。
  2. 迭代交替：
     - **Assignment**：每点分配到最近 cluster。
     - **Refitting**：centroid 移到新 cluster 的中心。
- notebook：`KMeans(n_clusters=2, random_state=42)`。

#### 8.2 Hierarchical Clustering（层次聚类）

- 用 **dendrogram**（树状图）表示，**无需预设 cluster 数**，在适当高度切割即可。
- **两种方法**：
  - **Agglomerative**（自底向上）：每点自成一簇，逐步合并。
  - **Divisive**（自顶向下）：全部成一簇，逐步分裂。
- **Linkage 方法**（衡量簇间距离）：
  - **Min Linkage**（单链）：最近点距离。
  - **Max Linkage**（全链）：最远点距离。
  - **Centroid Linkage**：簇中心距离。
  - **Average Linkage**：平均距离。
  - **Ward Linkage**：算簇间**方差**而非直接距离；**对噪声和 outlier 更鲁棒**。

#### 8.3 Fuzzy Clustering（模糊聚类）

- 与 K-Means 唯一关键区别：每点**不唯一属于一个 cluster**，而是对每个 cluster 有一个**归属系数**（degree of belonging）。
- centroid = 所有点按归属度加权的均值。

### 9. NLP Applications 小结（课件末页）

- 传统 ML 算法需要**结构化数值输入** → 文本须经 **TF-IDF vectorization** 等转为数值。
- **分类**应用：sentiment analysis、intent classification、authorship attribution。
- **聚类**应用：document clustering、spam detection。

### 10. ⭐ Week4MCQ 考点信号（5 道代码改写题）

本周 MCQ **全部为 sklearn 代码改写**——预示 IRA/TRA #1 会考**代码层面的模型选择与参数调优**。逐题分析：

| 题 | 考点 | 答案 | 为什么 |
|---|---|---|---|
| **Q1** 改 `MultinomialNB`→`GaussianNB` | NB 模型切换需改 import + 实例化 | **Line 1 and 2** | `from sklearn.naive_bayes import GaussianNB`（Line1）+ `nb = GaussianNB()`（Line2）；`.fit/.predict` 接口通用 |
| **Q2** 调 SVM 正则强度 | SVM 的正则参数 = **C** | **`C=0.5`** | `degree` 属 polynomial 核；`gamma` 属 RBF；`coef0` 属 poly/sigmoid；`probability` 仅开关概率输出 |
| **Q3** 调 RBF 核 length scale | `length_scale` 是 **RBF() 构造器参数** | **`RBF(length_scale=1.5)`** | length_scale 必须传入 `RBF()` 内部，而非 classifier 层；`length_scale_bounds` 仅用于优化边界 |
| **Q4** LinearRegression 拟合方法 | sklearn 通用训练接口 = **`.fit()`** | **`lr.fit(X_train, y_train)`** | `.score` 返回 R²；`.transform` 属预处理；`.predict` 是推理；`.compile` 是 Keras 接口 |
| **Q5** 改 KMeans cluster 数 | cluster 数参数 = **`n_clusters`** | **`n_clusters=2`** | `n_init` 是初始化次数；`max_iter` 是迭代上限 |

> **出题规律**：给一段 sklearn 代码 + 5 个改写选项，要求选出**正确修改某参数/模型**的那行。复习时要熟悉每个模型的**关键参数名**与**构造器 vs 分类器层参数的归属**。

### 11. 考点速查表

| 模型 | 关键参数/概念 | sklearn 接口 |
|---|---|---|
| **Naïve Bayes** | MultinomialNB（词频）/ GaussianNB（连续）/ CategoricalNB；Laplace smoothing `alpha` | `naive_bayes.MultinomialNB()` |
| **SVM** | `kernel`（linear/rbf/poly/sigmoid）；正则参数 `C`（越大正则越弱）；`gamma`（RBF 宽度） | `svm.SVC(kernel='linear', C=...)` |
| **ELM** | 随机输入权重 + 训练 $\beta$ via Moore-Penrose pseudoinverse | `hpelm.ELM` |
| **Gaussian Process** | `kernel=RBF(length_scale=...)`；length scale 小→wiggly，大→smooth | `GaussianProcessClassifier(kernel=RBF())` |
| **Linear Regression** | squared error loss；gradient descent；learning rate $\alpha$ | `LinearRegression().fit(X,y)` |
| **K-Means** | `n_clusters`（簇数）；`n_init`（初始化次数）；`max_iter` | `KMeans(n_clusters=2)` |
| **Hierarchical** | Agglomerative vs Divisive；Ward 对噪声鲁棒 | — |
| **Fuzzy** | 每点对每簇有归属系数 | — |

### 12. 本周要点小结

- **Text Classification** = 文档 $d$ → 类别 $c$；四大应用（topic/sentiment/language/authorship）。
- **Naïve Bayes**：Bayes + 朴素条件独立 + BOW；**Laplace smoothing** 解 zero probability；手算 prior/conditional + add-one。
- **SVM**：最大化 margin ⇔ 最小化 $\|w\|$；hinge loss + 正则 **C**；**kernel trick** 解线性不可分（RBF/Linear/Poly/Sigmoid）。
- **ELM**：单隐藏层、随机输入权重、无 backprop、训练 $\beta$ 用伪逆。
- **Gaussian Process**：函数上的分布；mean + covariance(kernel)；RBF 的 **length scale** 控平滑度。
- **Linear Regression**：squared error + gradient descent；learning rate $\alpha$。
- **Clustering**：K-Means（assignment+refitting）、Hierarchical（agglomerative/divisive，5 种 linkage，Ward 鲁棒）、Fuzzy（归属系数）。
- **NLP 应用**：文本须先 TF-IDF vectorization 再套 ML；分类用于 sentiment/intent/authorship，聚类用于 document grouping/spam detection。
- **MCQ 出题规律**：sklearn 代码改写——选正确参数名与归属层（构造器 vs 分类器）。

---

> **下周（Week 5）预告**：进入 **Neural models (RNN, LSTM, GRU) and Hyperparameter Tuning**，并有 **Coding quiz #2**（15 分钟，5 题单选，负分制）。本周传统 ML 收尾，下周转入深度学习序列模型。具体以课件为准。
>
> **笔记约定补充**：本周新增保留英文术语（text classification, sentiment analysis, topic modelling, language identification, authorship attribution, Naïve Bayes, Bayes Theorem, class prior, conditional probability, Laplace smoothing / Add-One, zero probability problem, BOW, SVM, hyperplane, margin, hinge loss, regularization, kernel trick, RBF, length scale, ELM, Moore-Penrose pseudoinverse, SVD, Gaussian Process, mean/covariance function, gram matrix, positive semidefinite, Linear Regression, squared error, gradient descent, learning rate, K-Means, centroid, assignment, refitting, hierarchical clustering, dendrogram, agglomerative, divisive, linkage, ward, fuzzy clustering, TF-IDF vectorization, MultinomialNB, GaussianNB, CategoricalNB, n_clusters, n_init 等）。中文用于组织句意与补充释义。
>
> **说明**：本周无录播转写，以上为基于课件/notebook/MCQ 整理。若后续补录播，可补充老师口述要点。

---

## Week 5 — Neural Language Models + Hyperparameter Tuning（神经语言模型与超参数调优）

> **权威来源说明**：本周**无录播转写**（`week5/` 内无 txt）。基于官方材料整理：
> - `EE6405_W4_NM_For Students.pdf`（Neural Language Models 课件，Dr. Simon Liu）— RNN/LSTM/GRU/BiRNN
> - `EE6405_W5_HPT_For Students.pdf`（HyperParameter Tuning 课件，Dr. S. Supraja）
> - `Week 6.ipynb`（RNNModel/LSTMModel/GRUModel/BiRNNModel + 训练循环）
> - `Week 8(1).ipynb`（GridSearchCV + KFold + LSTMClassifier + gradient clipping）
> - `Week6MCQ.md` / `Week8MCQ.md`（各 5 题代码题——本周考点信号）
>
> ⚠️ 文件命名：`week5/` 内 notebook 叫 `Week 6.ipynb`/`Week 8(1).ipynb`，但对应 Week 5 两堂课；`Week 5.ipynb`（Evaluation Metrics + Word Embeddings）在 `week4/` 文件夹，属 Week 4 延续。完整 Week 5 知识点见 `week5/Week5_Notes.md`。

### 1. 本周主线

Week 4 传统 ML 收尾后，本周转入**深度学习序列模型**：让神经网络处理有顺序的文本。主线：Sequential data 局限 → RNN → LSTM（解 vanishing gradient）→ GRU（简化）→ Bi-RNN（双向）→ Hyperparameter Tuning 调优。

> ⭐ **本周有 Coding Quiz #2**（15 分钟，5 题单选，负分制，覆盖 Week 4 + Week 5）。

### 2. Sequential Data 与传统模型三大局限

- **Sequential data**：按顺序组织的数据，顺序对意义至关重要；文本是典型。
- 传统 feedforward 网络三大局限：**Lack of Memory**（无记忆）、**Order Insensitivity**（对顺序不敏感）、**Variable-Length Limitation**（变长限制）。
- → 需 RNN / LSTM / GRU / Bi-RNN / Transformer。

### 3. RNN（Recurrent Neural Network）

- **核心**：hidden state $h_t = g(x_t, h_{t-1})$ 记忆历史；参数跨时间步**共享**（tied parameters）→ 处理变长序列。
- **Vanilla RNN**：$h_t = \tanh(Ux_t + Wh_{t-1} + b)$，$y_t = \mathrm{softmax}(Vh_t)$。
- **三种架构**：Sequence-to-One（sentiment）、One-to-Sequence（image caption）、Sequence-to-Sequence（POS/NER）。
- **Activation**：Sigmoid（gate/分类输出）、Tanh（hidden state，零中心、收敛快）。
- **局限**：**Vanishing Gradient**（长序列梯度太小）、**Exploding Gradient**（梯度太大不稳定）→ LSTM 解之。

### 4. LSTM（Long Short-Term Memory）

- **Cell state** = long-term memory，由三道 gate 调控：
  - **Forget gate** $f_t = \sigma(W_f h_{t-1} + x_t + b_f)$：保留多少旧信息。
  - **Input gate** $i_t = \sigma(...)$ + 候选 $\tilde{c}_t = \tanh(...)$：加什么新信息。
  - **Cell update** $c_t = f_t c_{t-1} + i_t \tilde{c}_t$。
  - **Output gate** $o_t = \sigma(...)$，$h_t = o_t \tanh(c_t)$。
- 解 vanishing gradient，捕捉 long-term dependency。

### 5. GRU（Gated Recurrent Unit）

- LSTM 简化版（2014）：**无 cell state**，合并 hidden + cell。
- 两道 gate：**Reset gate** $r_t$（忘多少旧）、**Update gate** $z_t$（保留多少 + 加多少新）。
- 参数更少、更省算力，效果常接近 LSTM。

### 6. Bi-RNN（Bi-Directional RNN）

- 正向 + 反向两个 RNN，同时看过去和未来上下文。
- 适合 NER / POS tagging（词标签常由前后词决定）。
- 代码两处改动：`bidirectional=True` + `fc = nn.Linear(hidden_dim * 2, output_size)`。

### 7. Hyperparameter Tuning

| 超参 | 要点 |
|---|---|
| **K-Fold CV** | 评估模型设计（非某次训练）；k=10 常用；`GridSearchCV(clf, param_grid, cv=5)` + `cross_val_score` |
| **Optimizer** | Gradient Descent / SGD（batch）/ Adam（自适应 + momentum）/ RMSprop |
| **Loss** | BCE（二分类）/ CCE（多分类，配 softmax）；PyTorch `CrossEntropyLoss` 内含 softmax |
| **Batch size** | 大→快但可能精度低；小→更准但慢 |
| **Learning rate** | 0.1~0.0001；过高 overshoot，过低慢 |
| **Epochs** | 太少 underfit，太多 overfit；**Early stopping** 防过拟合 |
| **Gradient clipping** | 防 exploding gradient；`clip_grad_value_(params, clip_value=0.5)`（clipping by value/norm） |

### 8. 训练循环（PyTorch）

```
model.train() → optimizer.zero_grad() → output=model(x) → loss=criterion(output,target) → loss.backward() → optimizer.step()
```
- `zero_grad()`：清梯度（backward 前必须）。
- `step()`：按 optimizer 规则更新权重。
- `model.train()`/`model.eval()` 切训练/评估模式。

### 9. ⭐ Week 5 MCQ 考点信号

| 题 | 考点 | 答案 |
|---|---|---|
| **W6 Q1** `self.embedding` 作用 | indices → dense vector | To convert input sequences of indices into dense vector representations |
| **W6 Q2** RNN→Bi-RNN | `bidirectional=True` + `fc=hidden_dim*2` | 同时改两处 |
| **W6 Q3** RNN→LSTM | `nn.RNN`→`nn.LSTM` | 只换类名 |
| **W6 Q4** `optimizer.zero_grad()` | 清梯度 | clears gradients before backward |
| **W6 Q5** 调 Adam lr | `lr=1e-2`/`1e-3` | `eps=` 不是 lr |
| **W8 Q1** 不用 5-fold | 看 `cv=5` 显式与否 | GridSearchCV/cross_val_score 的 cv |
| **W8 Q2** KFold missing code | `X[train_index], X[val_index]` | 行列不混搭 |
| **W8 Q3** 维度定义作用 | 初始化 NN 结构 | 不只算 feature 长度 |
| **W8 Q4** tensor+DataLoader | 转 tensor+Loader+初始化 | 不含 normalize/train |
| **W8 Q5** gradient clipping | `clip_grad_value_(model.parameters(), clip_value=0.5)` | clip_value 是 float |

### 10. 本周要点小结

- **RNN** 用 hidden state 记忆历史、参数共享，但 vanishing/exploding gradient 是软肋。
- **LSTM** 用 cell state + forget/input/output 三 gate 解 vanishing gradient；**GRU** 简化为 reset/update 两 gate，更省算力。
- **Bi-RNN** 正反向，`bidirectional=True` + `fc` 输入 `hidden_dim*2`。
- **Hyperparameter Tuning**：K-Fold CV 评模型设计；GridSearchCV 网格搜索；optimizer/loss/batch/lr/epochs/early stopping/gradient clipping 均可调。
- **PyTorch API**：`nn.Embedding/RNN/LSTM/GRU`（接口一致）；`optim.Adam(lr=...)`；`zero_grad()`→`backward()`→`step()`；`clip_grad_value_(params, clip_value)`。

---

> **下周（Week 6）预告**：进入 **Transformer 与 Attention 机制**，从 RNN/LSTM 转向 self-attention 架构；并有 **IRA/TRA #2**（20 分钟，多选多答，扣分制，覆盖 Week 5 + Week 6）。
>
> **笔记约定补充**：本周新增保留英文术语（sequential data, RNN, hidden state, vanilla RNN, parameter sharing, sequence-to-one/one-to-sequence/sequence-to-sequence, sigmoid, tanh, vanishing gradient, exploding gradient, LSTM, cell state, forget gate, input gate, output gate, GRU, reset gate, update gate, Bi-RNN, bidirectional, hyperparameter, K-fold cross-validation, GridSearchCV, cross_val_score, optimizer, Gradient Descent, SGD, Adam, RMSprop, momentum, bias correction, Binary Cross Entropy, Categorical Cross Entropy, softmax, batch size, learning rate, epoch, early stopping, gradient clipping, clipping by value / by norm, nn.Embedding, nn.RNN, nn.LSTM, nn.GRU, optimizer.zero_grad, optimizer.step, model.train/eval 等）。
>
> **说明**：本周无录播转写，基于课件/notebook/MCQ/tasks 整理。Neural Language Models 课件署名 Dr. Simon Liu，HPT 课件署名 Dr. S. Supraja。完整知识点见 `week5/Week5_Notes.md`。

---

## Week 7 — Coding Quiz #3 + ML CA Team Project + NLP Applications 预习

> **本周材料**（`week7/`）：`Week 7 tasks.pdf`（ML CA team project 说明）、`EE6405_W10_ A survey of NLP applications across diverse industries_For Students.pdf`（Dr. Simon Liu，NLP 行业应用 survey）、`EE6405_W11_ Deep-dive into NLP_For Students.pdf`（Dr. Simon Liu，NLP 应用深度案例）、`Week 10.ipynb` / `Week 11(1).ipynb`（对应 notebook）、`Week10MCQ.md`（练习题）。本周无录播转写，基于课件与 tasks 整理。

### 1. ⭐ Coding Quiz #3（本周唯一线下考核）

- **形式**：15 分钟，5 题单选，**负分制**（瞎猜倒扣）。
- **范围**：**只考 Week 6 Transformer 代码**（seq2seq / Attention / BahdanauAttention / MultiHeadAttention / PositionalEncoding / Encoder-Decoder / Transformer）。
- **缩放公式**：`(((score*2)+20)/120)*100`。
- **复习材料**：已备 `quiz1/Week6_Quiz_Prep.md`（5 道预测题 + 复习清单 + 应试策略）。必跑 `week6/Week 7.ipynb` 全部 cell，重点背：
  - `MultiHeadAttention`：4 个投影 `W_q/W_k/W_v/W_o: Linear(d_model, d_model)`，scaled dot-product `softmax(QK^T/sqrt(d_k))V`。
  - `BahdanauAttention`：`Wa/Ua: Linear(hidden,hidden)`，`Va: Linear(hidden,1)`。
  - `PositionalEncoding`：`pe[:,0::2]=sin`，`pe[:,1::2]=cos`，`forward: x + self.pe[:, :x.size(1)]`。
  - `AttnDecoderRNN`：`GRU(2*hidden_size, hidden_size, batch_first=True)`，`torch.cat((embedded,context))`。
  - `DecoderRNN`：返回 `None`（for consistency in the training loop）。

### 2. ⭐ ML CA Team Project（`Week 7 tasks.pdf`）

本周发布 **ML CA team project** 任务说明（占 ML CA 30% 的一部分，与 Quiz 2 共 30%）：

- **核心要求**：用 **ChatGPT**（或类似 LLM）构建一个 innovative NLP project。
- **Topic 要求**：除 ChatGPT 外，项目须包含 6 个 NLP topic 中的**至少 2 个**：
  - Language Translation
  - Automated Text Summarization
  - Text Completion
  - Question Answering
  - Content Generation
  - Sentiment Analysis
- **工具建议**：强烈建议结合课程中学过的其他 tools/packages（sklearn、torch、transformers 等）。
- **展示要求**：准备 3–5 分钟 short presentation，分享：
  1. 项目目标（the goal）
  2. ChatGPT 如何帮助达成目标
  3. 代码快速 review + highlight 任何有趣的 key components

### 3. NLP Applications Survey（`EE6405_W10`，Dr. Simon Liu）

课件概览 NLP 在各行业的应用，每行业列出典型用例与所涉 NLP algorithm：

| 行业 | 典型应用 | NLP 算法/技术 |
|---|---|---|
| **Healthcare** | 医疗文本处理 | text parsing、extraction |
| **Finance & Banking** | Financial report automation、fraud detection | ML、language models、text analytics |
| **Retail & Commerce** | Sentiment analysis for product reviews | sentiment analysis、deep learning |
| **Legal** | Contract analysis、key term extraction | text mining、predictive analytics |
| **Automotive** | Speech recognition、language understanding | voice recognition、NLU |
| **Publishing** | Content curation、automated content generation | NLG、transformer models |
| **Education** | Content personalization | text comparison、similarity scoring |
| **Travel & Hospitality** | Booking chatbot、language translation | chatbot、intent recognition、semantic search |
| **Media & Entertainment** | Content recommendation、social media sentiment | recommendation、sentiment analysis |
| **Government / Public sector** | 文本挖掘、预测分析 | text mining |

> **要点**：这是一张 survey 表，了解 NLP 应用广度即可，不必逐行业深记。核心 takeaway：NLP 应用横跨 finance、retail、legal、automotive、publishing、travel、media 等行业，所用技术主要是 sentiment analysis、text mining、NLG、chatbot、semantic search、transformer models。

### 4. NLP Applications Deep-dive（`EE6405_W11`，Dr. Simon Liu）

课件深入讲解 4 个真实 NLP 项目（2 个 NLP-based + 2 个 ChatGPT-based）：

#### 4.1 Fraud Detection Model（电商欺诈检测）

- **场景**：e-commerce platform 上的 fraudulent seller，两种 fraud：
  - **Fulfilment Fraud**（履约欺诈）：数据源 = buyer 的 product review。
  - **Off-platform Fraud**（平台外欺诈）：数据源 = seller 发给 buyer 的 messages。
- **Fulfilment Fraud Model pipeline**：
  1. 收集 product review（文本）。
  2. **Sentence Model**：对每条 review 的每句生成 **sentence embedding**（用 Transformer，如某 popular model）。
  3. **Aggregated at seller level**：把同一 seller 的所有 sentence embedding 聚合。
  4. **XGBoost Model**：用聚合后的 embedding 训练 **XGBoost** 分类器，判定该 seller 是否欺诈。
  5. 疑似 fraud seller 送人工审核（human investigator），确认后施加不同等级 punishment。
- **技术栈**：Transformer（sentence embedding）+ XGBoost（分类）。

#### 4.2 Human Trafficking Model（人口贩卖检测）

- **场景**：human trafficking 是年值约 $150M USD 的暗色产业；利用 bank 数据 + AI/ML 检测 sex trafficking 活动。
- **Pipeline**：transactions（交易数据）→ NLP/ML Model → Segmentation（分段）→ Score（评分）。
- 专注于 sex trafficking 的交易模式检测。

#### 4.3 Content Moderation（ChatGPT-based，prompt engineering）

- 用 ChatGPT + prompt engineering 做 content moderation（内容审核）。

#### 4.4 Product Recommendation Chatbot（ChatGPT-based）

- 用 ChatGPT + prompt engineering 构建商品推荐 chatbot。

### 5. Week 10 Notebook + MCQ（`Week 10.ipynb` / `Week10MCQ.md`）

`Week10MCQ.md` 两道练习题，围绕用 HuggingFace `transformers` 调用 chat model（Qwen）：

- **Q1**：`model.generate(**model_inputs, max_new_tokens=0)` —— `max_new_tokens=0` 表示不生成新 token，只返回 prompt 本身（或空），考察对 generation 参数的理解。
- **Q2**：`messages[1]["content"] = ""`（user content 为空字符串）—— 空输入能否运行 / 报什么错（AttributeError / ValueError / IndexError）。

> ⚠️ 这些 MCQ 对应 Week 10 的 notebook 内容（调用 chat model），与 ML CA team project 的 ChatGPT 使用直接相关。

### 6. 本周要点小结

- **Coding Quiz #3**：只考 Week 6 Transformer 代码，15min 5 题单选负分制，已备 `Week6_Quiz_Prep.md`。
- **ML CA Team Project**：用 ChatGPT 做 NLP project，须含 6 topic 中 ≥2 个（translation/summarization/completion/QA/generation/sentiment），3–5min presentation。
- **NLP Applications**（W10 survey）：NLP 横跨 healthcare/finance/retail/legal/automotive/publishing/travel/media/government，核心技术 sentiment analysis、text mining、NLG、chatbot、semantic search、transformer。
- **NLP Deep-dive**（W11）：Fraud Detection（Transformer embedding + XGBoost）、Human Trafficking（交易数据 + ML）、Content Moderation（ChatGPT prompt engineering）、Product Recommendation Chatbot（ChatGPT）。
- **Week 10 notebook**：HuggingFace `transformers` 调用 chat model（`apply_chat_template`、`model.generate`、`tokenizer.batch_decode`）。

---

> **下一周（Week 8）预告**：进入课程后半段——**New NLP Trends / Business perspective**（Dr. Simon Liu 主讲），围绕 NLP 在真实项目中的应用与 ChatGPT-based 应用开发。ML CA team project 持续进行（Assignment 在 Week 7&8 发布、Week 10 提交）。具体以 Week 8 课件为准。
