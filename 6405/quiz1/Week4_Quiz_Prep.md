# EE6405 Week 4 Quiz 预测与复习

> **Quiz 形式**：Week 4 是 **IRA/TRA #1（Theory Quiz）**——20 分钟，**多选多答**，错答**扣分**（最低 0），闭卷 + Respondus lockdown browser。老师声明覆盖 **Week 3 + Week 4**，但实测带**更早知识点**（见 §三）。
> 本文档由 `quiz-predict-6405` skill 生成：从 Week 1–3 quiz 截图（15 题）归纳出题逻辑，结合 Week 4 PPT + notebook 预测考点。

---

## 一、过往知识精简回顾（Week 1–2，quiz 会滚动复现）

> 每周 quiz 会带 1–2 道"再之前"的知识点。Week 4 quiz 会复现这些——精简列出，重在辨析。

### Week 1 精简（Preprocessing）

| 考点 | 一句话 | 易错 |
|---|---|---|
| **Stemming**（PorterStemmer） | 截词尾得 stem（可能无意义，如 `easili`） | `easily`→`easili` 不是 `easily` |
| **Lemmatization**（WordNetLemmatizer） | 归约到字典 lemma，需 `pos='v'` 才正确还原动词 | 不传 pos 默认当名词 |
| **reg.sub / regex** | `[^\w\s]` 去标点（`\w`=词字符、`\s`=空白）；`\W+` 会连空格一起去 | `[^\w\s]` vs `\W+` 是 W1 quiz 真题陷阱 |
| **Stop word removal** | `stopwords.words('english')` + `word_tokenize` 后过滤 | — |
| **N-gram** | 连续 n 个 token；bigram 用 Markov assumption | bigram 全列（W1 quiz 答案是 8 个全列的选项） |

### Week 2 精简（Linguistic Features，spaCy）

| 考点 | 一句话 | 易错 |
|---|---|---|
| **NER** | `doc.ents`，`entity.text`/`entity.label_` | `doc.entities`（错）vs `doc.ents`（对） |
| **POS tagging** | `token.pos_`（粗粒度）/ `token.tag_`（细粒度） | 带下划线 `pos_`/`tag_`，不带的是错 |
| **Dependency parsing** | `token.dep_`/`token.head.text`/`token.children` | `dep_` 带下划线；`children` 是生成器要 `list()` |
| **WSD** | `from nltk.wsd import lesk`——Lesk algorithm | W2 quiz 真题考算法名 `lesk` |
| **Semantic role labeling** | nsubj→ARG0(Agent)、dobj→ARG1(Patient)、prep→ARGM-LOC | Agent=who、Patient=what、Predicate=do what |

> W3 quiz 已复现 W1（lemmatization+POS 嵌入 `tagged_lemma`）和 W2（semantic role labeling）。W4 会继续带，且与新知识结合考。

---

## 二、前一周稍微丰富（Week 3，Term Weighting / Topic Modeling / Dim Reduction）

> Week 3 是 Week 4 quiz 声明覆盖的"上周"——稍详细，因为必考。

### 2.1 TF-IDF（Term Frequency-Inverse Document Frequency）

- **TF**：词在某文档出现频率；**IDF**：词在整个 corpus 的稀有度。TF-IDF = TF × IDF。
- 词越重要 TF-IDF 越高；越不重要越接近 0。
- **sklearn**：`TfidfVectorizer().fit_transform(corpus)` → 稀疏矩阵。
- ⭐ **W3 quiz Q2 真题**：`TfidfVectorizer(stop_words='english')` 去 stop word 后，`get_feature_names_out()` 返回**字母序**列表：
  ```python
  corpus = ["The cat sat on the mat", "The dog sat on the rug"]
  # 去掉 the/on → ['cat', 'dog', 'mat', 'rug', 'sat']（字母序）
  ```
  - 干扰项：非字母序的选项（如 `['cat','sat','mat','dog','rug']`）。
- ⭐ **W3 quiz Q5 真题**：`len(vectorizer.get_feature_names_out())`——`["apple banana apple", "banana orange"]` → 词表 `{apple, banana, orange}` → **3**。

### 2.2 BM25

- 另一种 term weighting scheme，比 TF-IDF 更注重文档长度归一化。
- `BM25Okapi(tokenized_corpus).get_scores(tokenized_query)`——注意 `get_scores`（**复数**）。

### 2.3 Topic Modeling — LDA（Latent Dirichlet Allocation）

- **LDA 用 `CountVectorizer`（整数词频），不用 TF-IDF**（LDA 要计数）。
  ```python
  vectorizer = CountVectorizer()
  input = vectorizer.fit_transform(corpus)  # 变量名要叫 input
  lda = LatentDirichletAllocation(n_components=2, random_state=42)
  lda.fit(input)
  ```
- ⭐ W3 MCQ Q1 真题干扰项：用 `TfidfVectorizer` 给 LDA 是错的。
- 可视化：`pyLDAvis.lda_model.prepare(lda, dt_matrix, vectorizer)`（注意拼写 `lda_model` 不是 `lda_mdel`）。

### 2.4 LSA（Latent Semantic Analysis）

- `TruncatedSVD(n_components=2).fit_transform(dt_matrix)`；`components_` 是主题×词矩阵。
- 取 top5 词：`topic.argsort()[-5:]` + `vectorizer.get_feature_names_out()[i]`。
- 易错：`argsort()` 不是 `sorted()`；`get_feature_names_out()` 带 `s`。

### 2.5 ⭐ PCA 降维（W3 quiz Q3 真题，高频陷阱）

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)
pca.fit(X)
```

- ⭐ **`n_components=0.95` 表示保留 95% 的 variance（方差），不是 95% 的 features**。
- W3 quiz feedback 原文："Near misses: it's a common misunderstanding to take the float value as a direct count of components."
- 若 `n_components` 是**整数** = 保留多少个主成分；是 **float 0–1** = 保留方差比例。
- ⚠️ PCA 要**密集矩阵**，TF-IDF 是稀疏矩阵须先 `.toarray()`（W3 MCQ Q5）。

### 2.6 Preprocessing for ML（Week 3 PPT 第 11 页，承上启下）

课件明确 ML 前的预处理四步：① RegEx 去标点+小写 → ② POS tagging + lemmatize → ③ 去 stop words → ④ **TF-IDF vectorisation**。这条 pipeline 是 Week 3→4 的桥梁，W4 quiz 会考。

---

## 三、本周知识详尽讲解（Week 4，Traditional ML Methods and NLP Applications）

> 基于 `EE6405_W4_Traditional ML and NLP Applications.pdf`（48 页）+ `Week 4.ipynb` 详尽整理。本周是 IRA/TRA #1 的核心。

### 3. Text Classification（文本分类）概述

**Text classification**：给文档 $d$ 分配预定义类别 $c \in C = \{c_1, c_2, \dots, c_j\}$。

**四大应用**：
| 应用 | 说明 |
|---|---|
| **Topic Modelling** | 按内容分主题 |
| **Sentiment Analysis** | 分析对公司/人/产品的情感（market research、reputation management） |
| **Language Identification** | 识别语言（搜索引擎查询处理） |
| **Authorship Attribution** | 作者识别（forensics、cybersecurity） |

**两类方法**：
- **Rule-based classifiers**：人工规则。
- **ML models**：Naïve-Bayes、SVM、ELM、Gaussian Processes、Linear Regression。

**Text Classifiers 的一般结构**：
- **Input**：一个文档 $d$ + 预定义类别集 $\{c_1, c_2, \dots, c_j\}$
- **Output**：预测类别 $c \in C$

> 传统 ML classifier 用 labelled training set 学习每个 label 的特征，再给新数据分配 label。

---

### 4. ⭐ Naïve Bayes（朴素贝叶斯）

Naïve Bayes 用 **BOW（bag-of-words）** approach 做文本分类。

#### 4.1 推导（Bayes Theorem）

对文档 $d$ 和类别 $c$：

$$P(c|d) = \frac{P(d|c)P(c)}{P(d)}$$

- 最可能类别：$\hat{c} = \arg\max P(c|d) = \arg\max P(d|c)P(c)$（**去掉分母** $P(d)$，因对所有类别相同）。
- 文档表示为特征 $x_1, \dots, x_n$（BOW 词频）：$\hat{c} = \arg\max P(x_1, x_2, \dots, x_n | c) P(c)$。
- ⭐ **"Naïve" assumption（朴素假设）**：词之间**条件独立** given class →
$$\hat{c} = \arg\max \prod_j P(x_j | c) P(c)$$

> 朴素假设是 Naïve Bayes 的核心——"word probabilities are independent of each other"。

#### 4.2 训练（MLE）

用 training corpus 的 maximum likelihood estimators：

- **Class Prior Probability**：
$$P(c) = \frac{\text{count}(documents\ labelled\ c)}{\text{count}(total\ documents)}$$

- **Conditional Probability**：
$$P(w_i | c) = \frac{\text{count}(documents\ containing\ word\ w_i\ labelled\ c)}{\text{count}(documents\ labelled\ c)}$$

#### 4.3 ⭐ Zero Probability Problem + Laplace Smoothing

**问题场景**：分类 reviews 成 positive/negative，词 "excellent" 只出现在 review1 的 positive 类，其他 positive review 没有。
- $P(\text{positive}|\text{review1}) = 0$，因为 $P(\text{"excellent"}|\text{positive}) = 0$。
- "These zero probabilities cannot be conditioned away no matter the evidence."——一旦某词概率为 0，整个乘积为 0，无法分类。

**解决 — Laplace (Add-One) Smoothing**：

$$P(w_i | c) = \frac{\text{count}(w_i, c) + 1}{\sum_{w \in V} \text{count}(w, c) + |V|}$$

其中 $V$ = vocabulary size（词表大小）。分子加 1、分母加 $|V|$，保证不为 0。

#### 4.4 ⭐ Worked Example（课件第 10 页手算，必考概念）

| Doc | Words | Class |
|---|---|---|
| 1 | Hive, Arc, Hive | NTU |
| 2 | Hive, Hive, Spine | NTU |
| 3 | Hive, Tamarind | NTU |
| 4 | Eusoff, Temasek, Hive | NUS |
| 5 | Hive, Hive, Hive, Eusoff, Temasek | ? (test) |

- **Class Prior**：$P(NTU) = 3/4$，$P(NUS) = 1/4$。
- 词表 $V = \{$Hive, Arc, Spine, Tamarind, Eusoff, Temasek$\}$，$|V|=6$。
- NTU 类总词数 = 3+3+2 = 8；NUS 类总词数 = 3。
- 用 Laplace smoothing 算 test doc（Hive×3, Eusoff, Temasek）：
  - $P(\text{Hive}|NTU) = \frac{5+1}{8+6} = \frac{6}{14} = \frac{3}{7}$
  - $P(\text{Eusoff}|NTU) = \frac{0+1}{8+6} = \frac{1}{14}$
  - $P(\text{Temasek}|NTU) = \frac{0+1}{8+6} = \frac{1}{14}$
  - $P(NTU|d) = \frac{3}{4} \cdot (\frac{3}{7})^3 \cdot \frac{1}{14} \cdot \frac{1}{14} \approx 0.0005$
  - $P(\text{Hive}|NUS) = \frac{1+1}{3+6} = \frac{2}{9}$
  - $P(\text{Eusoff}|NUS) = \frac{1+1}{3+6} = \frac{2}{9}$
  - $P(\text{Temasek}|NUS) = \frac{1+1}{3+6} = \frac{2}{9}$
  - $P(NUS|d) = \frac{1}{4} \cdot (\frac{2}{9})^3 \cdot \frac{2}{9} \cdot \frac{2}{9} \approx 0.0014$
- ⇒ 判 **NUS**（因 NTU 类中 Eusoff/Temasek 计数为 0，被 Laplace 拉平后 NUS 反而更高）。

> IRA/TRA 极可能考概念："为什么需要 Laplace smoothing？"——答：解决 zero probability problem，避免某词在训练集某类未出现导致整个概率为 0。

#### 4.5 notebook 实现（cell 3）

```python
from sklearn.naive_bayes import MultinomialNB, GaussianNB, CategoricalNB
nb = MultinomialNB()
nb.fit(X_train, y_train)
predictions = nb.predict(X_test)  # 输出 [1 1 1]，标签 [0 0 1]
```

- **MultinomialNB**：适合词频/TF-IDF 的**离散计数**特征。
- **GaussianNB**：假设特征连续高斯，适合实值特征。
- **CategoricalNB**：类别特征。
- ⭐ **Week4MCQ Q1 真题**：换 `MultinomialNB`→`GaussianNB` 只需改 **Line 1（import）+ Line 2（实例化）**，`.fit/.predict` 接口通用。

---

### 5. ⭐ Support Vector Machines (SVM)

#### 5.1 原理（graphical approach）

- SVM 在 high-dimensional space 找 **hyperplane**（超平面）最好地分隔不同类数据点。
- 选**离最近数据点最远**的 hyperplane → 最大化 **margin**（hyperplane 到最近点的距离）。
- **Hyperplane 方程**：$w \cdot x + b = 0$。
- **点到 hyperplane 距离**：$\frac{w \cdot x + b}{\|w\|_2}$。
- ⭐ SVM 最大化 margin ⇔ **最小化 $\|w\|_2$**——这是 **primal problem**。

#### 5.2 Hinge Loss + Regularization

$$c(x, y, f(x)) = \begin{cases} 0, & y \cdot f(x) \ge 1 \\ 1 - y \cdot f(x), & \text{otherwise} \end{cases}$$

- 预测值与真实值**同号且 margin 足够** ⇒ loss = 0；否则算 loss。
- 加正则项 $C \cdot \|w\|_2$ 防 **overfitting**。
- ⭐ **$C$ 越大正则越弱**（对训练数据拟合越紧，易 overfit）；$C$ 越小正则越强。

#### 5.3 ⭐ Kernel Trick（核技巧）

**问题**：文本数据常 **linearly inseparable**（线性不可分），SVM 找不到 hyperplane 切分。

**Kernel trick**：把数据映射到更高维 **feature space** 使其线性可分；**不显式计算高维坐标**，只计算高维空间中的点积（dot products）。

**四种常用核**（课件表格）：

| Kernel | 公式 | 说明 |
|---|---|---|
| **RBF（Radial Basis Function）** | $K(x_1, x_2) = \exp\left(-\frac{\|x_1 - x_2\|^2}{2\sigma^2}\right)$ | One class learning，$\sigma$ 为核宽度 |
| **Linear** | $K(x_1, x_2) = x_1^T x_2$ | Two class learning |
| **Polynomial** | $K(x_1, x_2) = (x_1^T x_2 + 1)^\rho$ | $\rho$ 为多项式阶数 |
| **Sigmoid** | $K(x_1, x_2) = \tanh(\beta_0 x_1^T x_2 + \beta_1)$ | 仅特定 $\beta_0, \beta_1$ 为 Mercer kernel |

> ⚠️ IRA 高频考点：kernel trick 的**动机**（解线性不可分）+ **做法**（不显式计算高维坐标，只算点积）。

#### 5.4 notebook 实现（cell 5）

```python
from sklearn import svm
svm = svm.SVC(kernel='linear')
svm.fit(X_train, y_train)
predictions = svm.predict(X_test)  # 输出 [1 1 1]，标签 [0 0 1]
```

⭐ **Week4MCQ Q2 真题**：调 SVM 正则强度用 **`C=0.5`**（`degree` 属 poly、`gamma` 属 RBF、`coef0` 属 poly/sigmoid、`probability` 仅开关概率输出）。

---

### 6. Extreme Learning Machines (ELM)

**ELM** 是 shallow feedforward neural network，**单隐藏层（single hidden layer）**。

#### 6.1 结构与公式

输出：
$$f_L(x) = \sum_{i=1}^L \beta_i g_i(x) = \sum_{i=1}^L \beta_i g(w_i \cdot x_j + b_i), \quad j=1,\dots,N$$

- $w$ = input→hidden 权重（随机初始化，**训练中不更新**）。
- $\beta$ = hidden→output 权重（训练目标）。

#### 6.2 ⭐ 三个关键特性

1. **无 backpropagation**（不像传统 NN）。
2. **输入→隐藏层权重随机初始化且不更新**。
3. 只训练 hidden→output 的 $\beta$ 矩阵。

#### 6.3 训练 = 解线性方程组

目标：找 $\beta$ 使 $H\beta = y$（$H$ = hidden layer output matrix，$y$ = target）。
- $H$ 通常非方阵，无精确逆 → 用 **Moore-Penrose Pseudoinverse（伪逆）**：
$$\beta = H^+ y$$
- $H^+$ 可用 **SVD** 计算。

#### 6.4 notebook 实现（cell 7）

```python
from hpelm import ELM
elm = ELM(X_train.shape[1], 1)
elm.add_neurons(10, 'sigm')  # 10 个 sigmoid 神经元
elm.train(X_train, y_train)
predictions = elm.predict(X_test).round().flatten()  # 输出 [0. 1. 1.]，标签 [0 0 1]
```

> IRA 高频考点：ELM 与传统 NN 区别 = **无 backprop** + 输入权重随机不更新 + 训练 $\beta$ 用伪逆。

---

### 7. Gaussian Processes (GP)

**Gaussian Process** 是 probabilistic model，定义**函数上的分布**（distribution over functions）——不把数据点当固定参数，而是把整个函数当随机变量。

#### 7.1 两个组成部分

- **Mean function**：$E[f(x_i)] = \mu(x_i)$
- **Covariance function (kernel function)**：$Cov(f(x_i), f(x_j)) = k(x_i, x_j)$

#### 7.2 Gram Matrix

- $K_x$ = kernel matrix，元素 $k(x_i, x_j)$，又叫 **gram matrix**。
- ⭐ $K_x$ 必须 **positive semidefinite（正半定）**。
- 由 Kolmogorov Extension Theorem 扩展为函数上的分布 = Gaussian Process。

#### 7.3 ⭐ RBF Kernel + Length Scale

$$K_{RBF}(x_i, x_j) = \sigma^2 \exp\left(-\frac{\|x_i - x_j\|^2}{2l^2}\right)$$

- $l^2$ = **length scale**（核宽度）：
  - **小 $l$ → 函数 wiggly（波动大）**
  - **大 $l$ → 函数 smooth（平滑）**
- RBF 生成 smooth、infinitely differentiable functions。

#### 7.4 notebook 实现（cell 9）

```python
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
gpc = GaussianProcessClassifier(kernel=RBF())
gpc.fit(X_train, y_train)
predictions = gpc.predict(X_test)  # 输出 [1 0 1]，标签 [0 0 1]
```

⭐ **Week4MCQ Q3 真题**：调 RBF 的 length scale 用 **`RBF(length_scale=1.5)`**——`length_scale` 传给 **`RBF()` 构造器**，不是 `GaussianProcessClassifier`；`length_scale_bounds` 是优化边界，不是值本身。

---

### 8. Linear Regression

**Linear Regression**：假设 input 与 output 线性关系 $y = mx + c$。

#### 8.1 Loss / Cost

- **Loss（squared error）**：$L(y, t) = \frac{1}{2}(y - t)^2$
- **Cost（MSE）**：
$$J(w, b) = \frac{1}{2N} \sum_{i=1}^N (wx_i + b - t_i)^2$$

#### 8.2 ⭐ Gradient Descent 优化

- 若 $\frac{\partial J}{\partial w_j} > 0$ ⇒ 增 $w_j$ 会增 $J$；$<0$ ⇒ 增 $w_j$ 减 $J$。
- **更新规则**：
$$w_j \leftarrow w_j - \alpha \frac{\partial J}{\partial w_j}$$
- $\alpha$ = **learning rate**。

#### 8.3 notebook 实现（cell 11）

```python
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
predictions = lr.predict(X_test)  # 输出 [0.667, 0.524, 0.667]，标签 [0 0 1]
```

⭐ **Week4MCQ Q4 真题**：训练用 **`.fit(X_train, y_train)`**（`.score` 返回 R²、`.predict` 是推理、`.compile` 是 Keras 接口、`.transform` 属预处理）。

---

### 9. Clustering（聚类，无监督）

**Clustering**：unsupervised ML，用 **distance/similarity metric** 分组，发现 hidden structures，无需预标注。

#### 9.1 K-Means

- 假设 k 个 cluster，每点属于最近 cluster center（均值）。
- **算法**：
  1. **Initialisation**：随机初始化 k 个 centroid。
  2. 迭代交替：
     - **Assignment**：每点分配到最近 cluster。
     - **Refitting**：centroid 移到新 cluster 中心。
- notebook（cell 13）：
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=2, random_state=42)
  kmeans.fit(X)
  print(kmeans.labels_)  # [0 1 0 0 1 1]
  ```
- ⭐ **Week4MCQ Q5 真题**：改簇数用 **`n_clusters=2`**（`n_init`=初始化次数、`max_iter`=迭代上限，三者不同）。

#### 9.2 Hierarchical Clustering

用 **dendrogram**（树状图）表示，**无需预设 cluster 数**，在适当高度切割即可。

**两种方法**（⚠️ 方向易错）：
| 方法 | 过程 | 方向 |
|---|---|---|
| **Agglomerative** | 每点自成一簇，逐步合并 | **bottom-up（自底向上）** |
| **Divisive** | 全部成一簇，逐步分裂 | **top-down（自顶向下）** |

**五种 Linkage 方法**（衡量簇间距离）：
| Linkage | 定义 |
|---|---|
| **Min Linkage**（单链） | 最近点距离 |
| **Max Linkage**（全链） | 最远点距离 |
| **Centroid Linkage** | 簇中心距离 |
| **Average Linkage** | 平均距离 |
| **Ward Linkage** | 算簇间**方差**而非直接距离；**对噪声和 outlier 更鲁棒**（less susceptible to noise and outliers） |

- notebook（cell 14）：
  ```python
  from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
  linkage_matrix = linkage(X, method='ward')
  clusters = fcluster(linkage_matrix, t=2, criterion='maxclust')  # [1 1 0 0 1 1]
  ```

#### 9.3 Fuzzy Clustering

与 K-Means **唯一关键区别**：每点**不唯一属于一个 cluster**，而是对每个 cluster 有一个 **coefficient（归属系数 / degree of belonging）**。
- centroid = 所有点按归属度加权的均值。
- notebook（cell 16）：
  ```python
  from fuzzycmeans import FCM
  fcm = FCM(n_clusters=2, max_iter=5)
  fcm.fit(X_train, y_train)
  predictions = fcm.predict(X_test)  # 输出 membership probabilities
  ```

---

### 10. NLP Applications 小结（课件末页）

- 传统 ML 算法需**结构化数值输入** → 文本须经 **TF-IDF vectorisation** 转数值。
- **分类应用**：sentiment analysis、intent classification、authorship attribution。
- **聚类应用**：document clustering、spam detection。

---

## 四、⭐ 预测题目（5 道，紧密结合 notebook 代码）

> IRA/TRA 是**多选多答**（multiple correct answers），每题可能有 2+ 个正确选项。以下题目代码**直接取自 Week 4 notebook**，按出题逻辑（§一）设计干扰项。

### Q1（预测）：Naïve Bayes 模型切换 + 概念（多选）

**题面**：关于以下代码，下列说法**正确**的有？

```python
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train, y_train)
predictions = nb.predict(X_test)  # 输出 [1 1 1]，标签 [0 0 1]
```

**选项**（多选）：
- A. Naïve Bayes 的"naïve"假设是：词之间**条件独立** given class
- B. `MultinomialNB` 适合 TF-IDF 或词频的**离散计数**特征
- C. 若要改成 `GaussianNB`，只需修改 import 和实例化两行，`.fit/.predict` 接口通用
- D. `GaussianNB` 假设特征连续高斯分布，比 `MultinomialNB` 更适合词频向量
- E. Laplace smoothing 用于解决 **zero probability problem**

**预测答案**：**A, B, C, E**
- A ✓ 朴素假设核心。
- B ✓ MultinomialNB 处理计数。
- C ✓ Week4MCQ Q1 结论：换模型只改 import + 实例化。
- D ✗ GaussianNB 假设连续高斯，但词频是**离散计数**，不适合——陷阱。
- E ✓ Laplace smoothing 目的（§4.3）。

**干扰项陷阱**：D 用"Gaussian 听起来更高级"诱导，但词频是离散的，应用 MultinomialNB。

---

### Q2（预测）：SVM kernel + 参数（多选）

**题面**：关于以下代码，下列说法**正确**的有？

```python
from sklearn import svm
svm = svm.SVC(kernel='linear')
svm.fit(X_train, y_train)
predictions = svm.predict(X_test)  # 输出 [1 1 1]
```

**选项**（多选）：
- A. SVM 最大化 margin ⇔ 最小化 $\|w\|_2$（primal problem）
- B. `kernel='linear'` 对应 $K(x_1, x_2) = x_1^T x_2$，适用 two class learning
- C. 要调正则强度，应设 `C=0.5`；**`C` 越大正则越弱**
- D. `degree` 参数属于 **RBF** 核，用于控制核宽度
- E. Kernel trick 把数据映射到更高维 space 使其线性可分，**不显式计算高维坐标**

**预测答案**：**A, B, C, E**
- A ✓ §5.1 核心。
- B ✓ Linear kernel 定义（§5.3 表）。
- C ✓ Week4MCQ Q2：`C` 是正则参数，越大正则越弱。
- D ✗ `degree` 属 **polynomial** 核，不属 RBF——陷阱（`gamma` 才属 RBF）。
- E ✓ kernel trick 定义（§5.3）。

**干扰项陷阱**：D 把 `degree` 错配到 RBF——Week4MCQ Q2 的干扰项复现。

---

### Q3（预测）：Gaussian Process length scale（多选）

**题面**：关于以下代码，下列说法**正确**的有？

```python
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
gpc = GaussianProcessClassifier(kernel=RBF())
gpc.fit(X_train, y_train)  # 输出 [1 0 1]
```

**选项**（多选）：
- A. `length_scale` 是 **`RBF()` 构造器**的参数，不是 `GaussianProcessClassifier` 的参数
- B. length scale **小** → 函数 wiggly；**大** → 函数 smooth
- C. Gaussian Process 定义**函数上的分布**，由 mean function 与 covariance function (kernel) 刻画
- D. Gram matrix $K_x$ 必须 **positive semidefinite**
- E. `length_scale` 和 `length_scale_bounds` 是同一个参数

**预测答案**：**A, B, C, D**
- A ✓ Week4MCQ Q3：参数归属层。
- B §7.3 几何意义。
- C ✓ GP 定义（§7.1）。
- D ✓ Gram matrix 性质（§7.2）。
- E ✗ `length_scale_bounds` 是优化边界，`length_scale` 是值本身——陷阱。

**干扰项陷阱**：E 混淆 `length_scale` 与 `length_scale_bounds`——Week4MCQ Q3 的干扰项。

---

### Q4（预测）：Clustering 方法对比（多选）

**题面**：关于以下三段聚类代码，下列说法**正确**的有？

```python
# K-Means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Hierarchical
from scipy.cluster.hierarchy import linkage
linkage_matrix = linkage(X, method='ward')

# Fuzzy
from fuzzycmeans import FCM
fcm = FCM(n_clusters=2, max_iter=5)
```

**选项**（多选）：
- A. `n_clusters` 控制簇数，`n_init` 控制初始化次数，`max_iter` 控制迭代上限——三者不同
- B. Hierarchical clustering 用 **dendrogram** 表示，**无需预设 cluster 数**
- C. **Ward linkage** 算簇间**方差**，对噪声和 outlier 更鲁棒
- D. Fuzzy clustering 与 K-Means 的关键区别：每点对每 cluster 有**归属系数**，不唯一属于一个 cluster
- E. Agglomerative 是**自顶向下分裂**，Divisive 是**自底向上合并**

**预测答案**：**A, B, C, D**
- A ✓ Week4MCQ Q5 三个 n 参数辨析。
- B ✓ Hierarchical 特性（§9.2）。
- C ✓ Ward 鲁棒性（§9.2）。
- D ✓ Fuzzy 与 K-Means 唯一关键区别（§9.3）。
- E ✗ 反了：Agglomerative = **bottom-up（自底向上合并）**，Divisive = **top-down（自顶向下分裂）**——陷阱。

**干扰项陷阱**：E 把 agglomerative/divisive 方向说反——经典概念陷阱，课件 §9.2 表格原文。

---

### Q5（预测）：滚动复现——TF-IDF + Preprocessing（多选）

**题面**：关于以下代码，下列说法**正确**的有？（滚动复现 Week 1+3 知识点）

```python
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = ["The cat sat on the mat", "The dog sat on the rug"]
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out())
```

**选项**（多选）：
- A. `stop_words='english'` 去掉 "the"、"on" 等 stop words，剩余词按**字母序**输出
- B. 输出为 `['cat', 'dog', 'mat', 'rug', 'sat']`（5 个词，字母序）
- C. `TfidfVectorizer` 输出 TF-IDF **浮点权重**，不是整数词频
- D. 若改用 `CountVectorizer`，输出整数词频向量，更适合给 `LatentDirichletAllocation` 用
- E. TF-IDF 值越高表示词越重要；越不重要越接近 0

**预测答案**：**A, B, C, D, E**（全选，但考场上逐项独立判断）
- A ✓ W3 quiz Q2 原题逻辑。
- B ✓ W3 quiz Q2 正确答案。
- C ✓ TF-IDF vs BOW 区别。
- D ✓ LDA 用 CountVectorizer（W3 MCQ Q1）。
- E §2.1 TF-IDF 语义。

**干扰项陷阱**：B 的词序——`stop_words='english'` 后 `get_feature_names_out()` 返回**字母序**，不是出现顺序。W3 quiz Q2 的错答就是选了非字母序选项。

> ⚠️ IRA/TRA 多选题里"全选"罕见，老师可能让其中一项微妙错误。**不确定的选项不选**（错选扣分，少选不扣）。

---

## 五、复习清单

### 5.1 必跑 notebook cell（Week 4.ipynb）

- [ ] Cell 3：`MultinomialNB` / `GaussianNB` / `CategoricalNB` 切换，记 `.fit/.predict` 通用
- [ ] Cell 5：`SVC(kernel='linear')`，记 `C`/`degree`/`gamma`/`coef0` 各属哪个核
- [ ] Cell 9：`GaussianProcessClassifier(kernel=RBF(length_scale=...))`，记参数归属层
- [ ] Cell 11：`LinearRegression().fit(X, y)`，记训练方法名
- [ ] Cell 13：`KMeans(n_clusters=2)`，记 `n_clusters` vs `n_init` vs `max_iter`
- [ ] Cell 14：`linkage(X, method='ward')`，记 5 种 linkage + Ward 鲁棒
- [ ] Cell 19：`f1_score(average='micro'/'macro')`（W5 前置，但 IRA 可能带）

### 5.2 必背 API/参数名（精确拼写）

| API/参数 | 归属 | 易错 |
|---|---|---|
| `MultinomialNB` / `GaussianNB` / `CategoricalNB` | `sklearn.naive_bayes` | 换模型改 import + 实例化 |
| `SVC(kernel=, C=)` | `sklearn.svm` | `C` = 正则强度；`degree` 属 poly；`gamma` 属 RBF |
| `RBF(length_scale=)` | `sklearn.gaussian_process.kernels` | `length_scale` 传 RBF()，不传 classifier |
| `LinearRegression().fit(X, y)` | `sklearn.linear_model` | 训练 = `.fit`（不是 `.compile`/`.score`） |
| `KMeans(n_clusters=)` | `sklearn.cluster` | `n_clusters` = 簇数；`n_init` = 初始化次数 |
| `linkage(X, method='ward')` | `scipy.cluster.hierarchy` | Ward 对噪声鲁棒 |
| `f1_score(y_true, y_pred, average=)` | `sklearn.metrics` | `f1_score` 全小写；`average='micro'/'macro'` |
| `TfidfVectorizer(stop_words='english')` | `sklearn.feature_extraction.text` | 去停用词后字母序输出 |
| `get_feature_names_out()` | vectorizer 方法 | 带 `s`（不是 `get_feature_names`） |

### 5.3 必背概念辨析（IRA/TRA 多选高频）

- **Naïve Bayes**：朴素条件独立假设；Laplace smoothing 解 zero probability；MultinomialNB（计数）vs GaussianNB（连续）。
- **SVM**：最大化 margin ⇔ 最小化 $\|w\|$；kernel trick 解线性不可分；C 越大正则越弱。
- **ELM**：单隐藏层、随机输入权重、**无 backprop**、训练 β 用 Moore-Penrose pseudoinverse。
- **Gaussian Process**：函数上的分布；mean + covariance(kernel)；length scale 小→wiggly，大→smooth。
- **Clustering**：K-Means（assignment+refitting）；Hierarchical（agglomerative **自底向上** / divisive **自顶向下**，5 种 linkage，Ward 鲁棒）；Fuzzy（归属系数）。
- **TF-IDF vs BOW**：TF-IDF 浮点权重 vs BOW 整数词频；LDA 用 BOW（CountVectorizer）。
- **PCA n_components**：float 值 = 保留方差比例（0.95 = 95% variance，不是 95% features）。

### 5.4 易错点（干扰项陷阱）

- `doc.ents`（对）vs `doc.entities`（错）
- `token.pos_` / `ent.label_`（带下划线，对）vs `token.pos` / `ent.label`（错）
- `f1_score`（全小写，对）vs `f1_Score`（错）
- `get_feature_names_out()`（带 s，对）vs `get_feature_names()`（旧版/错）
- `n_clusters`（簇数）vs `n_init`（初始化次数）vs `max_iter`（迭代上限）
- `length_scale`（值，传 RBF）vs `length_scale_bounds`（优化边界）
- PCA `n_components=0.95` = 95% **variance**（不是 95% features）
- agglomerative = **自底向上合并**（不是分裂）；divisive = 自顶向下分裂
- SVM `degree` 属 **polynomial**（不是 RBF）；`gamma` 属 RBF
- TF-IDF 去停用词后输出是**字母序**（不是出现顺序）

---

## 六、应试策略（IRA/TRA 多选多答 + 负分制）

1. **多选题逐项独立判断**：每个勾选的选项独立计分——对加分、错扣分。**不确定的选项宁可不选**（少选不扣，错选扣）。
2. **先个人做，再团队讨论**：TRA 阶段可改答案。团队讨论时把**有把握**的留下，**没把握**的删掉。
3. **警惕绝对词**：选项含 "always/never/must/only" 通常错（除非课件明确说绝对）。
4. **概念题用"为什么"复习**：IRA 不考手算大数字，考"为什么需要 X"——准备每算法的一句话动机。
5. **滚动复现准备**：考前快速过 W1（stemming/lemmatization/regex/stopword）+ W2（POS/NER/WSD）+ W3（TF-IDF/PCA/LDA）的概念定义。
6. **时间**：20 分钟多选题，每题 ~4 分钟。卡住的题先标记跳过，团队讨论阶段再攻坚。

---

## 附：Week 1–3 quiz 真题归纳表（出题逻辑依据）

| 周 | 题号 | 题型 | 考点 | 正确答案 | 错答干扰 |
|---|---|---|---|---|---|
| W1 | Q1 | 读代码问目的 | PorterStemmer 作用 | B（convert to root form） | — |
| W1 | Q2 | 读代码问目的 | WordNetLemmatizer(pos='v') | B（base form of verb） | — |
| W1 | Q3 | Missing code | lemmatize + POS tagging 流程 | E | — |
| W1 | Q4 | 读代码问目的 | stop word removal | A | — |
| W1 | Q5 | 改参数 | regex 去标点 `[^\w\s]` | D | A（`\W+` 会去空格） |
| W2 | Q1 | 改参数 | 打印 entity text | C（`[entity.text for entity in doc.ents]`） | `doc.entities`（错） |
| W2 | Q2 | Missing code | 提取含 ORG 的句子 | B（`if "ORG" in [ent.label_ for ent in sent.ents]`） | `sent.ents.label_`（错），**-2/10** |
| W2 | Q3 | Missing code | lemmatize + unique lemmas | E（`set(lemmas)`） | `unique(lemmas)`（错） |
| W2 | Q4 | 改参数 | WSD 算法名 | A（lesk） | tokens（错），**-2/10** |
| W2 | Q5 | 读代码问输出 | `re.sub('.g.*d',...)` | A（Harper is the goodest girl.） | — |
| W3 | Q1 | 概念辨析 | tagged_lemma 在 TF-IDF 前的作用 | B（reduce vocabulary sparsity） | — |
| W3 | Q2 | 读代码问输出 | TfidfVectorizer stop_words 输出 | A（`['cat','dog','mat','rug','sat']`） | 非字母序选项 |
| W3 | Q3 | 概念辨析 | PCA n_components=0.95 | A（95% variance） | B（95% features，near-miss） |
| W3 | Q4 | 读代码问输出 | semantic role labeling (Agent/Patient/Predicate) | D（Students/NLP/learn） | E（NTU 当 Patient，near-miss） |
| W3 | Q5 | 读代码问输出 | `len(get_feature_names_out())` | C（3） | — |
