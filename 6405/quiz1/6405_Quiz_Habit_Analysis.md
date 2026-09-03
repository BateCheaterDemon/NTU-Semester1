# EE6405 Quiz 出题习惯分析 + 复习指南（Dr. S. Supraja）

> 基于 Week 1–5 全部 MCQ（`Week1MCQ.md`~`Week5MCQ.md`）+ tasks + notebooks + 课件，逆向推导老师出题偏好，做成专项复习指南。
> 适用：Coding Quiz（15 分钟，5 题单选，负分制）+ IRA/TRA Theory Quiz（20 分钟，多选多答，错答扣分）。

---

## 一、考核机制速记（先记住规则）

| 类型 | 占比 | 周次 | 形式 | 扣分规则 |
|---|---|---|---|---|
| **Coding Quiz** | 20%（4 次） | W3,5,7,9 | 15 分钟，5 题单选 | near-miss=0 分；完全错答**扣分**，总分可为负 |
| **Theory IRA/TRA** | 20% | W4,6,10,11 | 20 分钟，**多选多答** | 错答**扣分**（最低 0） |
| Mid-term | 35% | W8 周五 9 Oct | 监考，覆盖 W1–6 | — |

- **Coding quiz 缩放公式**：`(((score*2)+20)/120)*100`（使最低分=0）。
  - 0/50→16.67；20/50→50；38/50→80。
- **闭卷 + Respondus lockdown browser**，现场 attendance，access code 课上给。
- **覆盖规则**：一般考当周+前一周；但 Coding quiz #3(W7) 只考前一周(W6)；#4(W9) 只考 W7；IRA/TRA #3/#4 只考当周。

> ⚠️ 扣分制意味着**瞎猜非常危险**——没把握的选项宁可不选（Theory 多选题）或选 near-miss（Coding 题至少不倒扣）。

---

## 二、⭐ 出题习惯总结（5 周 MCQ 逆向归纳）

### 习惯 1：题型高度固定——"给代码，问输出/问改写"

5 周共 25 题，**全部是代码题**，无纯概念默写。两类：

| 题型 | 出现周次 | 占比 | 形式 |
|---|---|---|---|
| **"What is the output"**（读代码算结果） | W1(Q1,Q3,Q4,Q5), W2(Q1,Q3,Q4) | ~40% | 给代码，问运行输出 |
| **"Missing code / Spot the error / 改参数"** | W2(Q5), W3(全部), W4(全部), W5(全部) | ~60% | 给代码，问哪行出错/该填什么/改哪个参数 |

> **结论**：复习必须**动手跑代码**，不能只看概念。每个 API 的**精确方法名/参数名**要记牢。

### 习惯 2：选项设计——5 个高度相似选项 + 1 个正确

- 每题 5 个选项，**正确项与干扰项只在细节上差一点**：
  - W1Q1：`s3` vs `s4` vs `s5` 三条 `re.sub` 链，选项混用不同中间结果。
  - W3Q3：`argsort()[-5:]` vs `argsort()[-5:]`(重复) vs `range()` vs 无 `[]` vs `.sorted()`。
  - W4Q2：`C=0.5` vs `degree=2` vs `gamma='auto'` vs `coef0=1.0` vs `probability=True`。
- **干扰项来源**：用**相邻概念/相邻参数**混淆：
  - `gamma`（RBF 宽度）vs `C`（正则强度）——都属 SVM 但作用不同。
  - `n_clusters` vs `n_init` vs `max_iter`——KMeans 三个以 n 开头的参数。
  - `length_scale` vs `length_scale_bounds`——前者是值，后者是优化边界。

> **应试**：记参数时**连"它属于哪个对象的构造器"一起记**（见下表）。

### 习惯 3：考点随周递进——紧跟 notebook 的 sklearn/nltk/spacy 调用

| 周 | 核心 API/库 | 典型考法 |
|---|---|---|
| W1 | `re.sub`, `PorterStemmer`, `WordNetLemmatizer`, `word_tokenize`, n-gram 生成函数 | 问 stemming/lemmatization 输出；n-gram 列表 |
| W2 | `spacy.load`, `doc.ents`, `token.pos_/tag_`, `token.dep_`, `spacy.explain` | 问 NER 实体列表；POS tag 元组；dependency 格式串 |
| W3 | `CountVectorizer`, `TfidfVectorizer`, `LatentDirichletAllocation`, `BM25Okapi`, `TruncatedSVD`, `PCA`, `pyLDAvis` | 问 missing code；选正确 vectorizer；调参 |
| W4 | `MultinomialNB/GaussianNB`, `SVC`, `GaussianProcessClassifier(RBF)`, `LinearRegression`, `KMeans` | 问改模型需改哪几行；问调某参数用哪个 key |
| W5 | `f1_score`, `roc_auc_score`, `sentence_bleu`, `Word2Vec`, `glove_model.most_similar` | 问 spot the error line；问正确调用方法名 |

> **结论**：每周 MCQ **就是该周 notebook 的代码摘录 + 改写**。复习时把该周 notebook **每段代码都跑一遍**，记住输出。

### 习惯 4：两类常见陷阱

**陷阱 A：方法名拼写/大小写**
- W5Q1：`f1_Score`（错，大写 S）vs `f1_score`（对，全小写）——Python 区分大小写。
- W3Q4：`pyLDAvis.lda_mdel`（错，拼写）vs `pyLDAvis.lda_model.prepare`（对，但本题答案其实是选项 5 的 matplotlib 法——注意 pyLDAvis API 拼写陷阱仍考）。
- W3Q2：`bm25.get_score`（错，单数）vs `bm25.get_scores`（对，复数）。

**陷阱 B：参数归属层**
- W4Q3：`length_scale` 必须传给 `RBF()` 构造器，**不能**传给 `GaussianProcessClassifier(..., length_scale=1.5)`。
- W3Q5：`PCA` 对**密集矩阵**用，TF-IDF 是稀疏矩阵要先 `.toarray()`；`n_components=3` 才是降 to 3 维（选项里混了 `n_components=2`）。

> **应试**：遇到"改 X 参数"题，先问"X 是谁的参数"——构造器参数 vs 分类器参数 vs 方法参数。

### 习惯 5：Theory Quiz（IRA/TRA）与 Coding Quiz 的区别

- **Coding Quiz**：5 题单选，全代码题（如上）。
- **IRA/TRA Theory**：多选多答，考概念理解。题目会基于 lecture video + slides，**不需课外资料**。错答扣分 ⇒ **不确定的选项不选**。
- IRA 流程：先个人做→团队讨论同一题→提交团队答案。团队讨论时**可以改答案**，TRA 占 5%。

> IRA/TRA 的多选多答意味着选项之间**独立判分**——每个勾选的选项都对加分、错扣分。部分正确的"near-miss"在这里也危险。

---

## 三、⭐ 各周考点清单 + 必背 API

### Week 1 — Preprocessing

| 考点 | 必背 | 易错 |
|---|---|---|
| `re.sub(pattern, repl, string)` | `\w`=词字符，`\s`=空白，`\d`=数字，`[^\w\s]`=去标点 | `re.sub` 链式调用时记清每步作用的对象 |
| `PorterStemmer().stem(word)` | 输出 stem（可能无意义，如 `easili`） | `easily`→`easili`（不是 `easily`） |
| `WordNetLemmatizer().lemmatize(word, pos='v')` | pos='v' 才正确还原动词 | 不传 pos 默认当名词 |
| `word_tokenize` vs `sent_tokenize` | 分词 vs 分句 | `text.split()` 不分标点 |
| n-gram 生成 | `zip(*[words[i:] for i in range(n)])` + `' '.join` | bigram 选项会漏一个（W1Q5 答案是选项 5，8 个 bigram 全列） |

**W1 真题答案**：Q1=选项4(s4); Q2=选项2(`word_tokenize`); Q3=选项5(`run,runner,ran,easili,fair,isn't`); Q4=选项1(`run,runner,run,easily,fairness,isn't`); Q5=选项5(8个bigram)。

### Week 2 — Linguistic Features (spaCy)

| 考点 | 必背 | 易错 |
|---|---|---|
| `spacy.load("en_core_web_sm")` | 加载小模型 | 模型名拼写 |
| `doc.ents` | 命名实体列表，`entity.text`/`entity.label_` | `label_` 带下划线，`label` 不行 |
| `token.pos_` / `token.tag_` | 粗粒度 POS / 细粒度 POS | `the`→`(DET, DT)`；`?`→`(., PUNCT)`？实际 W2Q3 答案选项1=`(DET,DT)`和`(.,PUNCT)` |
| `token.text` / `token.orth_` | 两者**相同**（orth_ 是 hash 的文本形式） | W2Q4 答案选项1=`(the,the)`和`(greatest,greatest)` |
| `token.dep_` / `token.head.text` / `token.children` | 依赖关系/父节点/子节点列表 | `dep_` 带下划线；`token.children` 是生成器要 list() |
| `spacy.explain('_SP')` | 返回 `"whitespace"`（注意是 `explain` 不是 `explains`） | `_SP` = space/whitespace |

**W2 真题答案**：Q1=选项1; Q2=选项3(`spacy.explain('_SP')`+"whitespace"); Q3=选项1; Q4=选项1; Q5=选项1(全部带`.text`/`_`)。

### Week 3 — Term Weighting / Topic Modeling / Dim Reduction

| 考点 | 必背 | 易错 |
|---|---|---|
| `CountVectorizer().fit_transform(corpus)` → 稠密可给 LDA | LDA 用 **CountVectorizer**（词频），不是 TF-IDF | W3Q1 答案选项3：`input = vectorizer.fit_transform(corpus)`（变量名要叫 `input`） |
| `TfidfVectorizer` | TF-IDF，**不适合 LDA**（LDA 要整数计数） | 选项1/4 用 TfidfVectorizer 是干扰 |
| `BM25Okapi(tokenized_corpus).get_scores(tokenized_query)` | 方法名 `get_scores`（**复数**） | `get_score`（单数）是错的；query 要 tokenized |
| `TruncatedSVD(n_components=2).fit_transform(dt_matrix)` | LSA；`components_` 是主题×词矩阵 | `get_feature_names_out()`（注意 `s`） |
| `topic.argsort()[-5:]` | 取 top5 词索引，配合 `vectorizer.get_feature_names_out()[i]` | `range()` 包裹是错的；`.sorted()` 是错的；缺 `[]` 是错的 |
| `pyLDAvis.lda_model.prepare(lda, dt_matrix, vectorizer)` | 可视化 LDA（但拼写陷阱多） | W3Q4 实际答案是选项5（matplotlib 手动画）——pyLDAvis 选项都有拼写错 |
| `PCA(n_components=3, svd_solver='full')` + `tfidf_data.toarray()` | PCA 要密集矩阵，TF-IDF 须 `.toarray()` | 不加 `.toarray()` 会报错；`n_components` 要等于目标维度 |

**W3 真题答案**：Q1=选项3; Q2=选项1; Q3=选项2(注意与选项1仅`get_features`vs`get_feature_names`之差，实际选项2才是正确拼写); Q4=选项5; Q5=选项1(降3维应是 n_components=3，但选项1无 n_components——需核对，本题选项5的 n_components=3 但缺 toarray，选项1有 toarray 但无 n_components；正确应是 PCA(n_components=3)+toarray()，最接近的是选项1因为 toarray 是必须的)。

> ⚠️ W3Q5 有争议，需实际跑代码确认。**关键记忆点**：PCA 对稀疏矩阵必须先 `.toarray()`，且 `n_components` 要等于目标维度。

### Week 4 — Traditional ML (sklearn 分类器/聚类)

| 模型 | 关键参数 | 易错 |
|---|---|---|
| `MultinomialNB` → `GaussianNB` | 改 import + 实例化（2 行），`.fit/.predict` 通用 | W4Q1 答案选项1：**Line 1 and 2** |
| `SVC(kernel='linear', C=0.5)` | `C` = 正则强度（**越大正则越弱**） | `degree` 属 poly；`gamma` 属 RBF；`coef0` 属 poly/sigmoid |
| `GaussianProcessClassifier(kernel=RBF(length_scale=1.5))` | `length_scale` 传给 **RBF()** 不是分类器 | `length_scale_bounds` 是优化边界不是值 |
| `LinearRegression().fit(X, y)` | 训练 = `.fit()` | `.score` 返回 R²；`.compile` 是 Keras |
| `KMeans(n_clusters=2, random_state=42)` | `n_clusters` = 簇数 | `n_init`=初始化次数；`max_iter`=迭代上限 |

**W4 真题答案**：Q1=选项1(Line1&2); Q2=选项5(C=0.5); Q3=选项3(RBF(length_scale=1.5)); Q4=选项4(.fit); Q5=选项1(n_clusters=2)。

### Week 5 — Evaluation Metrics + Word Embeddings

| 考点 | 必背 | 易错 |
|---|---|---|
| `f1_score(y_true, y_pred, average='micro'/'macro')` | 函数名全小写 `f1_score`（不是 `f1_Score`） | W5Q1 错在 Line 3,4,8 的大小写 + 调用名 |
| `metrics.roc_auc_score(y_true, y_pred)` | `metrics`（复数），不是 `metric` | 分类用 `svm_pred`，回归用 `lr_pred` 但要 `(lr_pred>0.5).astype(int)` 二值化 |
| `sentence_bleu([reference], candidate, weights, smoothing_function=)` | reference 要 **list 包裹** `[reference]`；weights 是 4-元组 | W5Q3 错在 Line2：`[reference]` vs `reference`，且 weights 要在用之前定义 |
| `Word2Vec(tokenized, vector_size=100, window=5, min_count=1, sg=0)` | `sg=0` 是 CBOW，`sg=1` 是 Skip-gram；`model.wv[word]` 取向量 | W5Q4 错在 Line3：`Word2Vec.load` 会覆盖刚训练的 model（逻辑错） |
| `glove_model.most_similar('word')` | 方法名 `most_similar`（带下划线词），不是 `similar` | `most_similar` vs `similar` |

**W5 真题答案**：Q1=选项3(Line 3,4,8); Q2=选项3/6(`metrics.roc_auc_score`，分类用 svm_pred 选项3，回归用 lr_pred 需二值化选项6); Q3=选项2(reference 未 list 化); Q4=选项3(`Word2Vec.load` 覆盖了训练好的 model); Q5=选项4(`most_similar('word')`)。

> ⚠️ W5Q2 有 6 个选项（唯一一题 6 选项），需注意 `metrics`（复数）+ 分类用 `svm_pred`/回归用 `lr_pred` 且要二值化。

---

## 四、⭐ 高频考点 Top 10（跨周统计）

| 排名 | 考点 | 出现周次 | 类型 |
|---|---|---|---|
| 1 | **sklearn 模型参数名精确记忆**（C/length_scale/n_clusters/n_components） | W3,W4 | Coding |
| 2 | **方法名拼写与下划线**（`f1_score`/`pos_`/`tag_`/`dep_`/`get_scores`/`most_similar`） | W2,W3,W5 | Coding |
| 3 | **stemming vs lemmatization 输出**（PorterStemmer 的 `easili`） | W1 | Coding |
| 4 | **spaCy 属性带不带下划线**（`label_`/`pos_`/`dep_`/`orth_`） | W2 | Coding |
| 5 | **稀疏矩阵→密集**（TF-IDF 给 PCA 要 `.toarray()`） | W3 | Coding |
| 6 | **参数归属层**（RBF 构造器 vs 分类器） | W4 | Coding |
| 7 | **NB 模型切换改哪几行**（import+实例化，fit/predict 通用） | W4 | Coding |
| 8 | **n-gram 生成函数输出**（bigram 全列） | W1 | Coding |
| 9 | **BLEU reference 要 list 包裹** | W5 | Coding |
| 10 | **Word2Vec.load 覆盖训练模型**（逻辑错误） | W5 | Coding |

---

## 五、⭐ 应试策略

### 1. Coding Quiz 策略（15 分钟 5 题，负分制）

- **每题先读代码，在脑中跑一遍**——老师爱考"这段代码输出什么"。
- **遇到"改参数"题**：先定位"该参数属于哪个对象"——构造器参数传构造器，分类器参数传分类器。
- **遇到"spot error"题**：逐行检查 (a) 方法名拼写/大小写 (b) 下划线 (c) 参数名 (d) 变量名 (e) 逻辑顺序。
- **没把握的选项**：选 nearest miss（至少不倒扣）；**完全不会**就选一个看起来最合理的，避免乱猜导致负分。
- **时间**：15 分钟 5 题 = 每题 3 分钟。卡住的题先标记跳过，最后回来。

### 2. IRA/TRA Theory 策略（20 分钟，多选多答，错答扣分）

- **多选多答 ⇒ 不确定的选项宁可不选**（少选不扣分，错选扣分）。
- **先个人做，再团队讨论**——TRA 阶段可以改答案，团队讨论时把有把握的留下。
- 考概念理解，基于 lecture video + slides，**不需课外资料**。
- 常见多选题陷阱：选项里有"always/never/must"的通常**不选**（除非课件明确说绝对）。

### 3. 考前一周复习清单

- [ ] 把该周 + 前一周的 **notebook 每段代码都跑一遍**，记住关键输出。
- [ ] 背本周涉及的 **sklearn/nltk/spaCy API 精确方法名 + 参数名**（带不带下划线、单复数）。
- [ ] 整理"参数归属层"表：每个参数属于构造器还是分类器/方法。
- [ ] 重做本周 MCQ，**计时 15 分钟**，模拟负分制。
- [ ] For IRA/TRA：过一遍 lecture slides 的概念定义，准备多选题。

---

## 六、老师出题"指纹"总结（一句话）

> Dr. Supraja 的 quiz **不是考你会不会概念，而是考你能不能在 5 个长得几乎一样的代码选项里，认出那个拼写正确、参数归属正确、方法名带对下划线的唯一答案。** 复习的唯一捷径就是**把 notebook 代码自己跑一遍**——所有考点都从 notebook 代码摘录而来。

---

## 附：6405 Quiz 时间表（本学期）

| 周 | 评估 | 覆盖 | 形式 |
|---|---|---|---|
| W3 | Coding quiz #1 | W2+W3 | 15min 5题单选 负分 |
| W4 | **IRA/TRA #1** | W3+W4 | 20min 多选多答 扣分 |
| W5 | **Coding quiz #2** | W4+W5 | 15min 5题单选 负分 |
| W6 | IRA/TRA #2 | W5+W6 | 20min 多选多答 扣分 |
| W7 | Coding quiz #3 | **只考 W6** | 15min 5题单选 负分 |
| W8 | **Mid-term** | W1–6 | 监考 |
| W9 | Coding quiz #4 | **只考 W7** | 15min 5题单选 负分 |
| W10 | IRA/TRA #3 | **只考 W10** | 20min 多选多答 扣分 |
| W11 | IRA/TRA #4 | **只考 W11** | 20min 多选多答 扣分 |
| W12 | Make-up quizzes | — | — |
