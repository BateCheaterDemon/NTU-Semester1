# EE6405 Week 5 Quiz 预测与复习

> **Quiz 形式**：Week 5 是 **Coding Quiz #2**——15 分钟，5 题单选，**负分制**（near-miss=0 分，完全错答扣分），闭卷 + Respondus lockdown browser。
> 老师声明覆盖 **Week 4 + Week 5**，但实测会带**更早知识点**（见 §一、§二）。
> 本文档由 `quiz-predict-6405` skill 生成：从 Week 1–4 quiz 截图/MCQ 归纳出题逻辑，结合 Week 5 notebook（`week4/Week 5.ipynb`）+ Week 4/5 课件预测考点。
> ⚠️ **本周 notebook 文件名是 `Week 5.ipynb`，放在 `week4/` 文件夹里**——对应教学 Week 5 内容（Evaluation Metrics + Word Embeddings）。`Week5MCQ.md` 也在 `week4/` 下。

---

## 一、过往知识精简回顾（Week 1–3，quiz 会滚动复现）

> 每周 quiz 会带 1–2 道"再之前"的知识点。Week 5 quiz 会复现这些——精简列出，重在辨析。

### Week 1 精简（Preprocessing）

| 考点 | 一句话 | 易错 |
|---|---|---|
| **Stemming**（PorterStemmer） | 截词尾得 stem（可能无意义，如 `easili`） | `easily`→`easili` 不是 `easily` |
| **Lemmatization**（WordNetLemmatizer） | 归约到字典 lemma，需 `pos='v'` 才正确还原动词 | 不传 pos 默认当名词 |
| **reg.sub / regex** | `[^\w\s]` 去标点（`\w`=词字符、`\s`=空白）；`\W+` 会连空格一起去 | `[^\w\s]` vs `\W+` 是 W1 quiz 真题陷阱 |
| **N-gram** | 连续 n 个 token；bigram 用 Markov assumption | bigram 全列（W1 quiz 答案是 8 个全列的选项） |

### Week 2 精简（Linguistic Features，spaCy）

| 考点 | 一句话 | 易错 |
|---|---|---|
| **NER** | `doc.ents`，`entity.text`/`entity.label_` | `doc.entities`（错）vs `doc.ents`（对） |
| **POS tagging** | `token.pos_`（粗粒度）/ `token.tag_`（细粒度） | 带下划线 `pos_`/`tag_`，不带的是错 |
| **Dependency parsing** | `token.dep_`/`token.head.text`/`token.children` | `dep_` 带下划线；`children` 是生成器要 `list()` |

### Week 3 精简（Term Weighting / Topic Modeling / Dim Reduction）

| 考点 | 一句话 | 易错 |
|---|---|---|
| **CountVectorizer vs TfidfVectorizer** | LDA 用 CountVectorizer（整数词频），不用 TF-IDF | LDA 要计数，TF-IDF 是浮点 |
| **BM25** | `BM25Okapi(tokenized_corpus).get_scores(tokenized_query)` | `get_scores`（**复数**），`get_score` 错 |
| **TruncatedSVD / PCA** | LSA 用 TruncatedSVD（稀疏矩阵可接），PCA 要 `.toarray()` | `n_components=3` 才是降到 3 维 |

> Week 5 的 preprocessing 仍会复现 W1 的 `re.sub` 链、lemmatization（本周 notebook cell 4–6 就在用），务必认得 `[^\w\s]`、`(<.*?>)`、`pos_tagger` 这些。

---

## 二、前一周稍微丰富（Week 4，Traditional ML & NLP Applications）

> Week 4 是 Week 5 quiz 声明覆盖的"上周"——稍详细，因为必考。Week 4 的 MCQ **全部为 sklearn 代码改写**，预示 Coding Quiz #2 也会考**代码层面的模型选择与参数调优**。

### 2.1 Naïve Bayes

- **Bayes + 朴素条件独立 + BOW**；**Laplace smoothing（Add-One）** 解 zero probability。
- sklearn：`MultinomialNB`（词频离散）/ `GaussianNB`（连续特征）/ `CategoricalNB`。
- ⭐ **W4 MCQ Q1 真题**：改 `MultinomialNB`→`GaussianNB` 需改 **Line 1 and 2**（`from sklearn.naive_bayes import GaussianNB` + `nb = GaussianNB()`）。
  - `.fit/.predict` 接口通用，不用改。

### 2.2 SVM

- 最大化 margin ⇔ 最小化 $\|w\|$；hinge loss + 正则参数 **C**；**kernel trick** 解线性不可分。
- 四种 kernel：**RBF / Linear / Poly / Sigmoid**。
- ⭐ **W4 MCQ Q2 真题**：调 SVM 正则强度 → **`C=0.5`**。
  - 干扰项：`degree`（属 polynomial 核）、`gamma`（属 RBF 宽度）、`coef0`（属 poly/sigmoid）、`probability`（仅开关概率输出）——都是**非正则参数**。
- ⭐ **W4 MCQ Q3 真题**：调 RBF 核 length scale → **`RBF(length_scale=1.5)`**。
  - `length_scale` 必须传入 `RBF()` **构造器内部**，不能传 `GaussianProcessClassifier(..., length_scale=1.5)`（参数归属层错）。
  - `length_scale_bounds` 仅用于优化边界，不是 length scale 本身。

### 2.3 ELM / Gaussian Process / Linear Regression / Clustering

| 模型 | 关键参数/概念 | 易错（W4 MCQ 已考） |
|---|---|---|
| **ELM** | 随机输入权重 + 训练 $\beta$ via Moore-Penrose pseudoinverse；无 backprop | — |
| **Gaussian Process** | `kernel=RBF(length_scale=...)`；length scale 小→wiggly，大→smooth | length_scale 归属 `RBF()` 构造器 |
| **Linear Regression** | squared error loss；`.fit(X, y)` 训练 | `.score` 返回 R²；`.transform` 属预处理；`.compile` 是 Keras 接口 |
| **K-Means** | `n_clusters`（簇数）；`n_init`（初始化次数）；`max_iter` | ⭐ W4 MCQ Q5：改 cluster 数 → `n_clusters=2`（不是 `n_init`/`max_iter`） |
| **Hierarchical** | Agglomerative vs Divisive；5 种 linkage；**Ward** 对噪声鲁棒 | — |
| **Fuzzy** | 每点对每簇有归属系数（degree of belonging） | — |

> **W4 出题规律**：给一段 sklearn 代码 + 5 个改写选项，选**正确修改某参数/模型**的那行。复习时记每个模型的**关键参数名**与**构造器 vs 分类器层参数的归属**。Week 5 quiz 会延续这一风格，但转向 **evaluation metrics + word embeddings** 的 API。

---

## 三、本周知识详尽讲解（Week 5，Evaluation Metrics + Word Embeddings）

> 按 `Week 5.ipynb`（`week4/` 文件夹）+ 课件顺序详尽整理，保留英文术语原词。代码直接摘自 notebook（含 cell 编号）。这是文档主体。

本周 notebook 分三大块：**(1) Predictive 评估指标**（confusion matrix / F1 / AUC-ROC）、**(2) Generative 评估指标**（BLEU / ROUGE / METEOR）、**(3) Word Embeddings**（Word2Vec / GloVe）。前置是 IMDB sentiment analysis 的 preprocessing + SVM/LinearRegression 训练。

### 3.0 Preprocessing + Sentiment Analysis（cell 2–11，复现 W1/W3）

- IMDB Dataset：`pd.read_csv("IMDB Dataset.csv")`，取正负各 `n_samples=200`。
- **re.sub 链**（cell 4）——W1 知识滚动复现：
  - `re.sub('(<.*?>)', ' ', x)` 去 HTML markup
  - `re.sub('[,\.!?:()"]', '', x)` 去标点
  - `re.sub('[^a-zA-Z"]',' ',x)` 去非字母
  - `.lower()`
- **Lemmatization**（cell 5）——W1 知识滚动：`WordNetLemmatizer` + `pos_tagger`（J→ADJ, V→VERB, N→NOUN, R→ADV），`tagged_lemma` 函数。
- **Vectorization**（cell 8）：`TfidfVectorizer(stop_words='english')` → `.fit_transform` / `.transform` → `.todense()`。
- **SVM**（cell 10）：`svm.SVC(kernel='rbf').fit(...)` → `svm_pred = clf.predict(...)`。
- **LinearRegression**（cell 11）：`lr.predict(...)` → `lr_pred`（连续概率值，非 0/1）。

> 这部分复现 W1（re.sub/lemmatization）和 W3（TF-IDF），Week 5 quiz 可能出"preprocessing 顺序"或"TF-IDF 参数"的滚动题。

### 3.1 Predictive 评估指标（cell 13–16）

#### Confusion Matrix + Accuracy/Precision/Recall（cell 13–14）

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

def getConfMatrix(pred_data, actual):
    conf_mat = confusion_matrix(actual, pred_data, labels=[0,1])
    accuracy = accuracy_score(actual, pred_data)
    precision = precision_score(actual, pred_data, average='micro')
    recall = recall_score(actual, pred_data, average='micro')
    ...
getConfMatrix(svm_pred, test_sent)            # SVM 直接是 0/1
getConfMatrix((lr_pred > 0.5).astype(int), test_sent)  # LR 需阈值转 0/1
```

- **`confusion_matrix(actual, pred_data, labels=[0,1])`**——注意参数顺序：**真实值在前，预测值在后**；`labels=[0,1]` 指定类标顺序。
- **`accuracy_score(actual, pred)`** = 正确预测比例。
- **`precision_score` / `recall_score`** 的 `average` 参数：
  - `'micro'`：全局算 TP/FP/FN（多类时按整体）。
  - `'macro'`：各类分别算再平均（不加权）。
  - `'weighted'`：各类按样本数加权。
- ⭐ **关键**：LinearRegression 输出是**连续概率**，必须 `(lr_pred > 0.5).astype(int)` 转 binary 才能进 confusion matrix（cell 14 注释明确）。

#### F1-score（cell 15）

```python
from sklearn.metrics import f1_score
def get_f1_score(y_true, y_pred):
    micro = f1_score(y_true, y_pred, average='micro')
    macro = f1_score(y_true, y_pred, average='macro')
    print('F1 Micro: ' + str(micro))
    print('F1 Macro: ' + str(macro))
get_f1_score(test_sent, svm_pred)
get_f1_score(test_sent, (lr_pred > 0.5).astype(int))
```

- **`f1_score(y_true, y_pred, average=...)`**——参数顺序：**真实值在前**。
- `average='micro'` vs `'macro'` vs `'weighted'` vs `None`（返回每类 F1）。
- ⭐ **W5 MCQ Q1 真题**就是这段代码的 **spot the error**：
  ```python
  1: from sklearn.metrics import f1_score        # 对
  2: def get_f1_score(y_true, y_pred):            # 对
  3:    micro = f1_Score(y_true, y_pred, ...)      # 错！大写 S
  4:    macro = f1_Score(y_true,y_pred, ...)       # 错！大写 S
  ...
  8: get_f1_Score(test_sent, svm_pred)            # 错！大写 S + 调用名不匹配
  ```
  - 答案 **3, 4, 8**（`f1_Score` 大写 S 是错的，正确是 `f1_score` 全小写）。
  - 陷阱：Line 1 (`f1_score` import 正确) 不选；Line 2 (`def` 定义正确) 不选。
  - 这是**方法名大小写**陷阱（W5 出题习惯 #4-A）。

#### AUC-ROC（cell 16）

```python
from sklearn import metrics
fpr, tpr, _ = metrics.roc_curve(test_sent, lr_pred)
auc = metrics.roc_auc_score(test_sent, lr_pred)
plt.plot(fpr, tpr, label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
```

- **`metrics.roc_curve(y_true, y_score)`** → 返回 `(fpr, tpr, thresholds)`。`y_score` 用**连续概率**（`lr_pred`），不是 binary。
- **`metrics.roc_auc_score(y_true, y_score)`** → 返回 AUC 值（float）。
- ⭐ **注释原文**："AUCROC only works on **probability predictions**, not binary predictions." → 用 `lr_pred`（连续），**不是** `(lr_pred > 0.5).astype(int)`（binary）。
- ⭐ **W5 MCQ Q2 真题**：计算 AUC-ROC 选哪行？
  - **答案 `metrics.roc_auc_score(test_sent, lr_pred)`**（用 `metrics` 复数 + `lr_pred` 连续概率）。
  - 干扰项：
    - `metric.roc_auc_score(...)`（`metric` 单数，错——模块名是 `metrics`）
    - `metrics.roc_auc_score(test_sent, svm_pred)`（SVM 输出 binary，不适合 AUC）
    - `metrics.roc_auc_score(test_sent, (lr_pred > 0.5).astype(int))`（转成 binary 了，失去概率信息）
    - `metrics.roc_auc_score(test_sent, (svm_pred > 0.5).astype(int))`（SVM 已是 0/1，转阈值无意义）
  - 陷阱：**模块名 `metrics`（复数）vs `metric`（单数）**；**AUC 用连续概率 vs binary**。

### 3.2 Generative 评估指标（cell 18–22）

#### BLEU（cell 18–19）

```python
import nltk
from nltk import word_tokenize
from nltk.translate.bleu_score import SmoothingFunction
ref = 'A fast brown dog jumps over a sleeping fox'
cand = 'A quick brown dog jumps over the fox'
smoothie = SmoothingFunction().method1          # method1（不是 method8）
reference = word_tokenize(ref)
candidate = word_tokenize(cand)

for i in range(2, 6):
    weights = [1/i for _ in range(i)]
    BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], candidate, weights, smoothing_function=smoothie)
    print(f"BLEU score with {i}-grams: {BLEUscore}, input weight: {weights}")
```

- **`nltk.translate.bleu_score.sentence_bleu([reference], candidate, weights, smoothing_function=...)`**
  - `reference` 必须**套列表** `[reference]`（多参考时是 list of list）。
  - `weights` 是 n-gram 权重 tuple/list，如 `(0.5, 0.5)` 表 2-gram 各 0.5。
  - `SmoothingFunction().method1`（method1~method8 共 8 种，notebook 用 method1）。
- **`sentence_bleu` vs `corpus_bleu`**：单句 vs 整个 corpus。
- ⭐ **W5 MCQ Q3 真题**：identify the line with error in BLEU calculation：
  ```python
  1. smoothie = SmoothingFunction().method8       # 本题用 method8（与 notebook 的 method1 不同，但都是合法 method）
  2. BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], candidate, weights, smoothing_function=smoothie)  # 错！weights 在定义前使用
  3. weights = (0.2, 0.3, 0.4, 0.1)                 # 定义在 line 2 之后
  4. reference = word_tokenize(ref)
  5. candidate = word_tokenize(cand)
  ```
  - **答案 Line 2**：`weights` 在 line 3 才定义，line 2 就用了 → **NameError / 顺序错**。
  - 陷阱：reference/candidate tokenize 顺序不影响；smoothing method1 vs method8 都合法。

#### ROUGE（cell 20–21）

```python
import evaluate
rouge = evaluate.load('rouge')
references = ['A fast brown dog jumps over a sleeping fox', 
              'A quick brown dog jumps over the fox']
predictions = ['The quick brown fox jumps over the lazy dog']
results = rouge.compute(predictions=predictions, references=references)
print(results)
```

- 用 **`evaluate` 库**（HuggingFace）：`evaluate.load('rouge')` → `.compute(predictions=..., references=...)`。
- **ROUGE-L**（最长公共子序列）、**ROUGE-N**（n-gram 召回）、**ROUGE-S**（skip-bigram）。
- cell 21 手写 `rouge_s` 用 `nltk.skipgrams(words, 2, 1)`（skip-bigram，窗口 1）。
  - `precision = len(common_bigrams) / len(cand_bigrams)`
  - `recall = len(common_bigrams) / len(ref_bigrams)`
  - `f1 = 2*p*r/(p+r)`
- ROUGE 重**召回**（reference 覆盖多少）；BLEU 重**精确率**（candidate 有多少在 reference 里）。

#### METEOR（cell 22）

```python
from nltk.translate import meteor
from nltk import word_tokenize
score = round(meteor([word_tokenize('A fast brown dog jumps over a sleeping fox')],
                     word_tokenize('The quick brown fox jumps over the lazy dog')), 4)
print('The METEOR score is: ' + str(score))
```

- **`nltk.translate.meteor(references, hypothesis)`**——参数：references 是 **list of tokenized**（`[word_tokenize(ref)]`），hypothesis 是单个 tokenized。
- METEOR 考虑 **precision + recall + fragmentation penalty**，支持同义词匹配（unigram matching + stemming）。

### 3.3 Word Embeddings（cell 24–25）

#### Word2Vec（cell 24，gensim）

```python
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]
model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, sg=0)
model.save("word2vec.model")
# model = Word2Vec.load("word2vec.model")

word = "word"
if word in model.wv:
    embedding = model.wv[word]
    print(f"Embedding for '{word}': {embedding}")
else:
    print(f"'{word}' is not in the vocabulary.")

similarity = model.wv.similarity("word", "embedding")
```

- **`Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)`**
  - `vector_size`：embedding 维度（旧版叫 `size`）。
  - `window`：上下文窗口大小。
  - `min_count`：词频下限（低于则忽略）。
  - `sg`：**0 = CBOW**，**1 = Skip-gram**。
- **`model.wv`**（KeyedVectors）访问词向量：`model.wv[word]`、`model.wv.similarity(w1, w2)`、`model.wv.most_similar(word)`。
- ⭐ **W5 MCQ Q4 真题**：identify error in Word2Vec training/usage：
  ```python
  1. tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]  # 对
  2. model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, sg=0)  # 对
  3. model = Word2Vec.load("word2vec.model")   # 错！覆盖了刚训练的 model（且文件可能不存在）
  4. embedding = model.wv["word"]              # 依赖 line 3 的 load，若 load 失败则错
  5. similarity = model.wv.similarity("word", "embedding")
  ```
  - **答案 Line 3**：`Word2Vec.load("word2vec.model")` 会**覆盖**刚训练的 model，且该文件未保存过 → 错。
  - 陷阱：line 4 本身语法对，但依赖 line 3；line 1/2/5 都正确。

#### GloVe（cell 25，gensim.downloader）

```python
import gensim.downloader as api
glove_model = api.load("glove-wiki-gigaword-100")
word = "nero"
embedding = glove_model[word]                    # 直接索引
similar_words = glove_model.most_similar(word)   # 最相似词
```

- **`gensim.downloader.api.load("glove-wiki-gigaword-100")`** 加载预训练 GloVe。
- `glove_model[word]` 直接取 embedding（与 Word2Vec 的 `model.wv[word]` 不同——GloVe 经 api.load 后直接是 KeyedVectors）。
- `glove_model.most_similar(word)` 返回最相似词列表。
- ⭐ **W5 MCQ Q5 真题**：find most similar words to `word` using GloVe：
  - **答案 `glove_model.most_similar('word')`**（`most_similar` + 引号字符串）。
  - 干扰项：
    - `glove_model.similar(word)`（方法名错，没有 `similar`，只有 `most_similar`）
    - `glove_model.similar('word')`（同上，方法名错）
    - `glove_model.most_similar(word)`（`word` 是变量名，题里指字符串 `'word'`——但本题 4 个选项中唯一对的是 `most_similar('word')`）
  - 陷阱：**方法名 `most_similar`**（不是 `similar`）；变量 `word` vs 字符串 `'word'`。

### 3.4 本周考点速查表

| API | 关键参数/方法 | 易错 |
|---|---|---|
| `f1_score` | `f1_score(y_true, y_pred, average='micro'/'macro')` | **全小写** `f1_score`，不是 `f1_Score` |
| `metrics.roc_auc_score` | `(y_true, y_score)`，y_score 用**连续概率** | `metrics`（复数）不是 `metric`；AUC 用概率非 binary |
| `metrics.roc_curve` | 返回 `(fpr, tpr, thresholds)` | — |
| `confusion_matrix` | `(actual, pred, labels=[0,1])`，真实在前 | 参数顺序 |
| `accuracy_score/precision_score/recall_score` | `average='micro'/'macro'/'weighted'` | precision/recall 的 average 参数 |
| `sentence_bleu` | `([reference], candidate, weights, smoothing_function=...)` | reference 套列表；weights 顺序；`SmoothingFunction().method1` |
| `evaluate.load('rouge')` | `.compute(predictions=..., references=...)` | 用 evaluate 库，不是 nltk |
| `nltk.translate.meteor` | `([word_tokenize(ref)], word_tokenize(hyp))` | references 是 list of tokenized |
| `Word2Vec` | `vector_size, window, min_count, sg(0=CBOW,1=Skip-gram)` | `model.wv[word]`/`.similarity`/`.most_similar` |
| `gensim.downloader.api.load` | `glove_model[word]` / `glove_model.most_similar(word)` | `most_similar` 不是 `similar` |

---

## 四、⭐ 预测题目（5 道，紧密结合 notebook 代码）

> Coding Quiz #2 是单选风格（5 选项 1 正确），负分制。以下预测基于 `Week 5.ipynb` 的代码点 + W5 MCQ 的出题逻辑。代码直接取自 notebook cell。

### Q1（spot the error）— F1-score 大小写陷阱（复现 W5MCQ Q1 风格）

**题**：以下代码计算 SVM 预测的 F1 Micro 和 F1 Macro。哪一行有错？假设 `test_sent` 和 `svm_pred` 已定义。

```python
1: from sklearn.metrics import f1_score
2: def get_f1_score(y_true, y_pred):
3:    micro = f1_Score(y_true, y_pred, average='micro')
4:    macro = f1_Score(y_true, y_pred, average='macro')
5:    print('F1 Micro: ' + str(micro))
6:    print('F1 Macro: ' + str(macro))
7: print("SVM:")
8: get_f1_Score(test_sent, svm_pred)
```

选项：
1. Line 1
2. Line 1 and 3
3. Line 3, 4, 8
4. Line 2, 3, 4
5. Line 1, 8

**答案**：**3. Line 3, 4, 8**

**陷阱分析**：
- Line 1 `from sklearn.metrics import f1_score`（全小写）**正确**——干扰项让选 Line 1 的选项（2、5）错。
- Line 2 `def get_f1_score(...)` 定义正确（小写）。
- Line 3/4 `f1_Score`（大写 S）**错**——Python 区分大小写，应为 `f1_score`。
- Line 8 `get_f1_Score(...)`（大写 S）**错**——调用名与定义的 `get_f1_score` 不匹配，会 NameError。
- 这是**方法名大小写**陷阱（出题习惯 #4-A）：`f1_Score` vs `f1_score`。

### Q2（改参数）— AUC-ROC 用哪个预测（复现 W5MCQ Q2 风格）

**题**：你已用 SVM 得到 `svm_pred`、用 LinearRegression 得到 `lr_pred`（同一份测试数据）。以下哪行能正确计算 AUC-ROC？

```python
1. auc = metric.roc_auc_score(test_sent, svm_pred)
2. auc = metric.roc_auc_score(test_sent, lr_pred)
3. auc = metrics.roc_auc_score(test_sent, svm_pred)
4. auc = metrics.roc_auc_score(test_sent, lr_pred)
5. auc = metrics.roc_auc_score(test_sent, (svm_pred > 0.5).astype(int))
```

选项：1 / 2 / 3 / 4 / 5

**答案**：**4. `auc = metrics.roc_auc_score(test_sent, lr_pred)`**

**陷阱分析**：
- `metric`（单数）模块名不存在 → 排除 1、2（**模块名 `metrics` 复数**陷阱）。
- AUC-ROC 需要**连续概率**（probability predictions），不是 binary——notebook cell 16 注释原文。`svm_pred` 是 0/1 binary，不适合 → 排除 3。
- `(svm_pred > 0.5).astype(int)` 对已是 0/1 的 SVM 输出无意义，且变 binary → 排除 5。
- `lr_pred` 是 LinearRegression 的连续输出（概率性）→ 正确。
- **双重陷阱**：模块名 `metrics` vs `metric` + 概率 vs binary。

### Q3（概念 + 代码）— BLEU weights 顺序

**题**：以下代码计算 BLEU score。哪一行有错？

```python
import nltk
from nltk import word_tokenize
from nltk.translate.bleu_score import SmoothingFunction
ref = 'The guard arrived late because it was raining.'
cand = 'The guard arrived late because of the rain.'
1. smoothie = SmoothingFunction().method1
2. BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], candidate, weights, smoothing_function=smoothie)
3. weights = (0.25, 0.25, 0.25, 0.25)
4. reference = word_tokenize(ref)
5. candidate = word_tokenize(cand)
```

选项：
1. Line 1
2. Line 2
3. Line 1, 2
4. Line 2, 3
5. Line 3, 4

**答案**：**2. Line 2**

**陷阱分析**：
- Line 2 使用 `weights`（line 3 才定义）和 `reference`/`candidate`（line 4/5 才定义）→ **变量未定义先使用**，NameError。
- `SmoothingFunction().method1`（line 1）合法——method1~method8 都是合法 smoothing。
- 这题考**代码执行顺序**：Python 从上到下执行，`weights = (0.25, 0.25, 0.25, 0.25)` 必须在 `sentence_bleu` 调用前。
- 干扰项：选 Line 3（weights 定义本身没错，错的是它的位置）、选 Line 1（method1 合法）。

### Q4（missing code / 改写）— Word2Vec 训练后取词向量

**题**：以下用 gensim 训练 Word2Vec 并取词 `'word'` 的 embedding。哪一行有错？

```python
1. tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]
2. model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, sg=0)
3. model = Word2Vec.load("word2vec.model")
4. embedding = model.wv["word"]
5. similarity = model.wv.similarity("word", "embedding")
```

选项：
1. Line 1
2. Line 2
3. Line 3
4. Line 3, 4
5. Line 4, 5

**答案**：**3. Line 3**

**陷阱分析**：
- Line 3 `Word2Vec.load("word2vec.model")` **覆盖**了 line 2 刚训练的 model，且该文件未先 `model.save()` → 会 FileNotFoundError 或丢失训练结果。
- Line 1（tokenize 正确）、Line 2（Word2Vec 参数正确：`vector_size`/`window`/`min_count`/`sg=0`）、Line 4/5（`model.wv["word"]` / `.similarity` 正确，假设 line 3 不存在）。
- 干扰项：选 Line 4/5（`model.wv` 用法本身对，错在 line 3 覆盖了 model）。
- 这是**训练/加载逻辑**陷阱：训练后不要立刻 load 覆盖。

### Q5（改写）— GloVe 找最相似词

**题**：以下哪行代码能正确用 GloVe 找到与单词 `'word'` 最相似的词？假设 `glove_model` 已通过 `gensim.downloader.api.load` 加载。

```python
1. similar_words = glove_model.similar('word')
2. similar_words = glove_model.most_similar(word)
3. similar_words = glove_model.similar(word)
4. similar_words = glove_model.most_similar('word')
5. similar_words = glove_model.most_similarity('word')
```

选项：1 / 2 / 3 / 4 / 5

**答案**：**4. `similar_words = glove_model.most_similar('word')`**

**陷阱分析**：
- gensim KeyedVectors 的方法名是 **`most_similar`**，不是 `similar`（1、3 错）、不是 `most_similarity`（5 错）。
- `word`（变量，未定义）vs `'word'`（字符串字面量）——题里指字符串 `'word'`，选项 2 用裸 `word` 会 NameError。
- 这是**方法名拼写** + **变量 vs 字面量**双重陷阱（出题习惯 #4-A）。

---

## 五、复习清单

### 必跑 notebook cell（`week4/Week 5.ipynb`）

- [ ] **Cell 13–14**：`getConfMatrix`——confusion_matrix 参数顺序、`(lr_pred > 0.5).astype(int)` 转 binary。
- [ ] **Cell 15**：`get_f1_score`——`f1_score` 全小写、average='micro'/'macro'。对照 W5MCQ Q1 的错误版。
- [ ] **Cell 16**：AUC-ROC——`metrics.roc_auc_score(test_sent, lr_pred)` 用连续概率；`metrics` 复数。对照 W5MCQ Q2。
- [ ] **Cell 18–19**：BLEU——`sentence_bleu([reference], candidate, weights, smoothing_function=...)`，weights 顺序。对照 W5MCQ Q3。
- [ ] **Cell 24**：Word2Vec——`Word2Vec(..., vector_size, window, min_count, sg=0)`、`model.wv[word]`/`.similarity`。对照 W5MCQ Q4。
- [ ] **Cell 25**：GloVe——`glove_model.most_similar('word')`。对照 W5MCQ Q5。
- [ ] **Cell 20–22**：ROUGE（`evaluate.load('rouge').compute`）+ METEOR（`nltk.translate.meteor`）——认 API 名。

### 必背 API/参数（精确拼写表）

| API | 精确写法 | 易错点 |
|---|---|---|
| F1 | `f1_score(y_true, y_pred, average='micro')` | **全小写** `f1_score`，大写 S 错 |
| AUC | `metrics.roc_auc_score(y_true, y_score)` | `metrics`（复数）；y_score 用概率 |
| ROC curve | `metrics.roc_curve(y_true, y_score)` → `(fpr, tpr, _)` | 返回三元组 |
| Confusion | `confusion_matrix(actual, pred, labels=[0,1])` | 真实在前 |
| Precision/Recall | `precision_score(actual, pred, average='micro')` | average 参数 |
| BLEU | `nltk.translate.bleu_score.sentence_bleu([ref], cand, weights, smoothing_function=SmoothingFunction().method1)` | ref 套列表；weights 顺序 |
| ROUGE | `evaluate.load('rouge').compute(predictions=..., references=...)` | 用 evaluate 库 |
| METEOR | `nltk.translate.meteor([word_tokenize(ref)], word_tokenize(hyp))` | references 是 list of tokenized |
| Word2Vec | `Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)` | sg=0 CBOW, sg=1 Skip-gram |
| Word2Vec 取向量 | `model.wv[word]` / `model.wv.similarity(w1, w2)` | `.wv` 不能少 |
| GloVe | `glove_model.most_similar('word')` | `most_similar` 不是 `similar`/`most_similarity` |

### 必背概念辨析

- [ ] **Predictive vs Generative 评估**：Predictive 用 confusion matrix/F1/AUC-ROC（有 ground truth 对比）；Generative 用 BLEU/ROUGE/METEOR（文本生成质量）。
- [ ] **AUC-ROC 用连续概率**，不是 binary——cell 16 注释原文 "only works on probability predictions, not binary predictions"。
- [ ] **BLEU 重 precision**（candidate 有多少在 reference 里），**ROUGE 重 recall**（reference 覆盖多少）。
- [ ] **CBOW vs Skip-gram**：`sg=0` 是 CBOW，`sg=1` 是 Skip-gram。
- [ ] **Word2Vec 需 tokenize**：`[word_tokenize(sentence.lower()) for sentence in sentences]`。

### 易错点（干扰项陷阱）

- [ ] `f1_Score`（大写 S）vs `f1_score`（全小写）——Python 大小写敏感。
- [ ] `metric`（单数）vs `metrics`（复数）——sklearn 模块名是 `metrics`。
- [ ] `similar` / `most_similarity` vs `most_similar`——gensim 方法名。
- [ ] 变量 `word` vs 字面量 `'word'`——题里指字符串时必须加引号。
- [ ] `weights` 在 `sentence_bleu` 调用前必须先定义——代码顺序。
- [ ] `Word2Vec.load` 会覆盖刚训练的 model——训练后不要立刻 load。
- [ ] AUC 用 `lr_pred`（连续），不是 `(lr_pred > 0.5).astype(int)`（binary）。

---

## 六、应试策略（负分制）

1. **负分制下不猜比瞎猜安全**：Coding quiz 完全错答**扣分**，near-miss=0 分。没把握的题选最接近的（至少不倒扣）。
2. **先看模块名/方法名拼写**：`metrics` vs `metric`、`f1_score` vs `f1_Score`、`most_similar` vs `similar`——这类陷阱一眼能破。
3. **代码顺序检查**：变量是否在使用前定义（如 BLEU 的 `weights`）。
4. **概率 vs binary**：AUC-ROC 用连续概率，confusion matrix 用 binary（LinearRegression 输出要 `.astype(int)`）。
5. **参数归属层**：`vector_size`/`window`/`min_count`/`sg` 都属 `Word2Vec()` 构造器；`model.wv` 是取向量的接口。
6. **时间管理**：15 分钟 5 题，每题 3 分钟。先做有把握的，难题最后回。

---

## 附：Week 1–5 MCQ 真题归纳表（出题逻辑依据）

| 周 | 题型 | 核心 API | 答案要点 |
|---|---|---|---|
| W1 Q1 | 读代码问输出 | `re.sub` 链 | 选项4(s4) |
| W1 Q2 | missing code | `word_tokenize` | 选项2 |
| W1 Q3 | 读输出 | stemming | 选项5 |
| W1 Q4 | 读输出 | lemmatization | 选项1 |
| W1 Q5 | 读输出 | bigram | 选项5(8个全列) |
| W2 Q1-5 | 读输出 | spaCy `doc.ents`/`pos_`/`dep_` | 全选项1（带下划线 API） |
| W3 Q1-5 | missing code/调参 | CountVectorizer/TfidfVectorizer/BM25/LDA/PCA | `get_scores`复数；LDA用Count |
| W4 Q1 | 改模型 | MultinomialNB→GaussianNB | Line 1 and 2 |
| W4 Q2 | 调参数 | SVM 正则 | `C=0.5` |
| W4 Q3 | 调参数 | RBF length_scale | `RBF(length_scale=1.5)` |
| W4 Q4 | 调方法 | LinearRegression | `.fit(X,y)` |
| W4 Q5 | 调参数 | KMeans | `n_clusters=2` |
| **W5 Q1** | **spot error** | **f1_score** | **Line 3,4,8（大写S）** |
| **W5 Q2** | **选正确行** | **AUC-ROC** | **`metrics.roc_auc_score(test_sent, lr_pred)`** |
| **W5 Q3** | **spot error** | **BLEU** | **Line 2（weights 顺序）** |
| **W5 Q4** | **spot error** | **Word2Vec** | **Line 3（load 覆盖）** |
| **W5 Q5** | **选正确行** | **GloVe** | **`glove_model.most_similar('word')`** |

> **Week 5 出题规律**：全部围绕 `Week 5.ipynb` 的 evaluation metrics + word embeddings 代码，题型为 **spot the error**（找错行）和 **选正确调用**。复习时把 cell 13–25 每段代码跑一遍，记住每个 API 的**精确拼写**和**参数顺序**。
