# EE6407 Quiz 2 Review — Slides 6–10

**Genetic Algorithms and Machine Learning · Mao Kezhi 部分**

> **Quiz 2**: 2026-11-10（周二）9:30–10:30；**40 minutes**；考场见 `6407/quiz2/Quiz2Venue.pdf`。
> **Coverage**: **Classification Tree / Classifier Performance Evaluation / Regression / Feature Selection / K-means Clustering**（Slides 6–10）。
> **Language**: 英文考试；本资料用中文讲解，但所有**专业术语保留英文**，并给出英文答题句式。
> **Sources**: `6407/week10/ML-Slides6.pdf`、`week11/ML-Slides7.pdf`、`week11/ML-Slides8.pdf`、`week12/ML-Slides9.pdf`、`week12/ML-Slides10.pdf`、`week12/week12.txt`、`6407/Learning_note.md`（Week 10–12）。

---

## 0. 40 分钟考试策略

| 项目 | 建议 |
|---|---|
| 题量 | 5 个 topic，预计 4–6 题（含 1–2 道计算） |
| 时间 | 每题约 7–8 分钟；计算题先写公式再代数字 |
| 语言 | 用英文答题；关键术语不要翻译成中文 |
| 计算器 | 按课程通知；简单计算尽量手算 |
| 检查 | 单位、符号（Gini vs entropy 不可比）、分母（precision vs recall） |

**英文答题常用句式**：

- "The Gini impurity of the node is ..."
- "The impurity drop is ...; therefore the best split is ..."
- "Accuracy = (TP+TN)/N = ..."
- "Precision = TP/(TP+FP) = ...; Recall = TP/(TP+FN) = ..."
- "The OLS estimate is θ = (FᵀF)⁻¹Fᵀy."
- "K-means minimizes the within-cluster sum of squares (WCSS)."

---

## 1. Classification Tree（分类树）— Slide 6

### 1.1 Key terms（必背英文）

| English term | 中文 | 一句话 |
|---|---|---|
| **root node** | 根节点 | 第一个问题 |
| **internal node** | 内部节点 | 中间问题 |
| **leaf node** | 叶节点 | 输出 class label |
| **branch** | 分支 | 问题的答案 |
| **split** | 分裂 | 用 feature + threshold 分数据 |
| **impurity** | 不纯度 | 节点混合程度；越小越纯 |
| **entropy impurity** | 熵不纯度 | `-Σ p log2 p` |
| **Gini impurity** | Gini 不纯度 | `1 - Σ p²`（或 `1/2[...]`） |
| **misclassification impurity** | 误分类不纯度 | `1 - max p` |
| **variance impurity** | 方差不纯度 | `p1 p2`（二分类） |
| **impurity drop** | 不纯度下降 | 选 split 的准则 |
| **gain ratio** | 增益率 | multi-split 的修正 |
| **continuous feature** | 连续特征 | 排序 + 中点作为候选 split |
| **stopping criterion** | 停止准则 | 何时停止长树 |
| **pruning** | 剪枝 | 合并相邻 leaf，防过拟合 |
| **leaf label** | 叶节点标签 | 多数类 |
| **random forest** | 随机森林 | bagging + random feature subset |

### 1.2 Why classification tree?

- **Nonmetric method**：不依赖 Euclidean distance，能处理 **nominal / categorical / mixed data**；
- **Interpretable**：树 = if-then rules；
- **Handles nonlinearity and feature interactions**；
- 缺点：单棵深树 **high variance**，容易 overfit → 需要 stopping/pruning，或 random forest。

### 1.3 Impurity measures（公式 + 原理）

设节点 N 中第 j 类比例为 `p_j`。

**Entropy impurity**：

```
i_E(N) = - Σ_j p_j log2(p_j)
```

- 纯节点（只有一类）→ 0；
- 二分类 50/50 → 1；
- 熵越大 → 越混合。

**Gini impurity**：

```
i_Gini(N) = Σ_{j≠k} p_j p_k = (1/2)[1 - Σ_j p_j²]
```

- 纯节点 → 0；
- 二分类 50/50 → 0.5；
- 二分类可写 `2p(1-p)`。

**Variance impurity**（二分类）：

```
i_Var(N) = p1 * p2
```

**Misclassification impurity**：

```
i_MC(N) = 1 - max_j p_j
```

⭐ **四种 measure 的数值不能直接比较**；同一棵树/同一题只用一种 measure。

### 1.4 Split selection（impurity drop）

```
Δi(N) = i(N) - P_L i(N_L) - P_R i(N_R)
```

- `P_L = n_L/n`，`P_R = n_R/n`；
- **maximize Δi** ⇔ **minimize weighted child impurity**；
- multi-split：`Δi = i(N) - Σ_k P_k i(N_k)`；
- multi-split 偏爱大 B → 用 **gain ratio**：

```
Δi'(N) = Δi(N) / ( - Σ_k P_k log2 P_k )
```

### 1.5 Worked example 1：Gini vs Entropy（10 个样本）

父节点：10 个样本，正负各 5。

```
G_parent = 1 - 0.5² - 0.5² = 0.5
H_parent = -0.5 log2 0.5 - 0.5 log2 0.5 = 1 bit
```

分裂后：

- 左：5 个，4 正 1 负；
- 右：5 个，1 正 4 负。

```
G_L = 1 - 0.8² - 0.2² = 0.32
G_R = 0.32
G_after = 0.5*0.32 + 0.5*0.32 = 0.32
ΔG = 0.5 - 0.32 = 0.18
```

```
H_L = -0.8 log2 0.8 - 0.2 log2 0.2 ≈ 0.7219
H_R ≈ 0.7219
H_after ≈ 0.7219
ΔH = 1 - 0.7219 = 0.2781 bit
```

⭐ 两个指标都说明 split 变纯，但 **0.18 和 0.2781 不能直接比大小**。

### 1.6 Worked example 2：Heart disease（连续 + 离散）

303 个样本；Class 1 = 139（with heart attack），Class 2 = 164（without）。

**Candidate `sex`（Sex=0?）**：

- 左：25 / 72（97 个）；
- 右：114 / 92（206 个）。

```
G_left = 0.1913
G_right = 0.2471
G_sex = (97/303)*0.1913 + (206/303)*0.2471 ≈ 0.2276
```

（按公式精确复算约 0.2293；课件写 0.2276，以方法为准。）

**Candidate `fbs`（fbs=0?）**：

- 左：117 / 141（258）；
- 右：22 / 23（45）。

```
G_left = 0.2478
G_right = 0.2499
G_fbs = (258/303)*0.2478 + (45/303)*0.2499 ≈ 0.2481
```

**Candidate `age`（continuous）**：

1. 排序：29, 34, 35, 37, ...
2. 相邻中点：31.5, 34.5, 36, ...
3. 逐个试，选 impurity 最小的 split point。

以 `age > 31.5` 为例：

- 左：139 / 163（302）；
- 右：0 / 1（1）。

```
G_left = 0.2484
G_right = 0
G_31.5 = (302/303)*0.2484 + (1/303)*0 ≈ 0.2476
```

`age` 的最低 Gini 是 **0.228 @ 54.5**。

⭐ 比较所有 feature：假设 `sex` 最低 → root node = `Sex = 0?`；左分支继续用 `exang`（0.1493）而不是 `fbs`（0.1831）。

### 1.7 Stopping / Pruning / Leaf label

**Stopping criteria**：

- maximum depth；
- minimum samples to split；
- minimum samples per leaf；
- minimum impurity decrease；
- cross-validation / validation error；
- trade-off `J = α*size + Σ_leaf i(N)`。

**Pruning**：

- 合并相邻 leaf pair（same parent）；
- 若 impurity 上升可接受 → merge，parent becomes leaf；
- pruning = inverse of splitting。

**Leaf label**：

- 纯 leaf → that class；
- 不纯 → **majority class**（most samples）。

### 1.8 Random Forest（Slide 6 末尾）

- **Bagging**：bootstrap sampling（with replacement）+ train one tree per sample；
- **Random feature subset**：每次 split 只从 `m` 个随机 feature 中选（classification 常用 `√p`，regression 常用 `p/3`）；
- **Prediction**：classification majority vote；regression average；
- **Why**：降低树间 correlation → 平均后 variance 更低；
- **OOB**：约 36.8% 样本未进入某 bootstrap，可做 out-of-bag estimate。

### 1.9 Exam traps

| Trap | Correct |
|---|---|
| Gini 和 entropy 数值可直接比 | ❌ 刻度不同 |
| Gini 的 `1/2` 必须保留 | ❌ 缩放因子，不影响 split 排序 |
| 树越深越好 | ❌ 深树 high variance，overfit |
| 连续 feature 不能用于树 | ❌ 排序 + 中点做候选 split |
| RF 只随机选样本 | ❌ 还随机选 feature |
| Leaf label 用平均 | ❌ classification 用 majority |

---

## 2. Classifier Performance Evaluation（分类器性能评估）— Slide 7

### 2.1 Key terms

| English term | 中文 |
|---|---|
| **holdout method** | 留出法 |
| **repeated holdout** | 重复留出 |
| **k-fold cross-validation** | K 折交叉验证 |
| **leave-one-out (LOOCV)** | 留一法 |
| **repeated k-fold** | 重复 K 折 |
| **stratified sampling** | 分层采样 |
| **confusion matrix** | 混淆矩阵 |
| **TP / FP / TN / FN** | 真阳/假阳/真阴/假阴 |
| **accuracy / error rate** | 准确率/错误率 |
| **sensitivity / specificity** | 敏感度/特异度 |
| **precision / recall** | 精确率/召回率 |
| **F1 score** | F1 分数 |
| **ROC curve / AUC** | ROC 曲线/曲线下面积 |
| **threshold** | 阈值 |

### 2.2 Evaluation procedures（步骤）

| Method | Procedure | Notes |
|---|---|---|
| **Holdout** | random split: 70–80% train, 20–30% test | simple; one random split |
| **Repeated holdout** | repeat holdout many times; average performance | reduces randomness |
| **K-fold CV** | split into K folds; each fold used once as test; average K results | K=5/10 common |
| **LOOCV** | K=N; one sample as test each time | expensive; small data |
| **Repeated K-fold** | repeat K-fold multiple times with reshuffling | reduces variance |
| **Stratified sampling** | sample each class separately to preserve class ratio | for class imbalance |

⭐ **Validation vs Test**：validation 用来调 hyperparameter / early stopping；test 只在最后用一次。

### 2.3 Confusion matrix + metrics（worked example）

Example（N=100）：

| | Actual Positive | Actual Negative |
|---|---|---|
| **Predicted Positive** | TP = 85 | FP = 4 |
| **Predicted Negative** | FN = 2 | TN = 9 |

**Accuracy**：

```
Accuracy = (TP + TN) / N = (85 + 9) / 100 = 94%
```

**Error rate**：

```
Error rate = (FP + FN) / N = (4 + 2) / 100 = 6%
```

**Sensitivity / Recall**：

```
Sensitivity = TP / (TP + FN) = 85 / 87 ≈ 97.7%
```

**Specificity**：

```
Specificity = TN / (TN + FP) = 9 / 13 ≈ 69.2%
```

**Precision**：

```
Precision = TP / (TP + FP) = 85 / 89 ≈ 95.5%
```

**F1**：

```
F1 = 2 * Precision * Recall / (Precision + Recall)
   = 2 * 0.955 * 0.977 / (0.955 + 0.977)
   ≈ 0.966
```

⭐ 记忆：
- **Precision 分母 = predicted positive（TP+FP）**；
- **Recall 分母 = actual positive（TP+FN）**；
- **Recall = Sensitivity**；
- F1 = precision 和 recall 的 harmonic mean。

### 2.4 ROC curve and AUC

- 默认 threshold = 0.5；改变 threshold 会改变 TP/FP/TN/FN；
- **TPR = TP/(TP+FN) = Sensitivity = Recall**；
- **FPR = FP/(FP+TN) = 1 - Specificity**；
- ROC：横轴 FPR，纵轴 TPR；每个 threshold 一个点；
- **AUC**：ROC 下面积；
  - 1 = perfect；
  - 0.5 = random；
  - 0 = completely reversed；
  - higher is better。

⭐ AUC 是 **threshold-independent** 的总体区分能力。

### 2.5 Exam traps

| Trap | Correct |
|---|---|
| Accuracy 高就一定好 | ❌ class imbalance 时 misleading |
| Precision = Recall | ❌ 分母不同 |
| Sensitivity = Specificity | ❌ positive vs negative class |
| ROC 的横轴是 TPR | ❌ 横轴 FPR，纵轴 TPR |
| AUC=0.5 最好 | ❌ 0.5 是 random |
| Test set 可以用来调参 | ❌ 会泄漏，变成 validation |

---

## 3. Regression（回归）— Slide 8

### 3.1 Key terms

| English term | 中文 |
|---|---|
| **simple linear regression** | 简单线性回归 |
| **multiple linear regression** | 多元线性回归 |
| **predictor / independent variable** | 自变量 |
| **target / dependent variable** | 因变量 |
| **residual / error** | 残差/误差 |
| **ordinary least squares (OLS)** | 普通最小二乘 |
| **design matrix F** | 设计矩阵 |
| **normal equation** | 正规方程 |
| **ridge regression** | 岭回归（L2） |
| **lasso regression** | Lasso（L1） |
| **MSE / RMSE / MAE** | 均方误差/均方根/平均绝对误差 |
| **R² / adjusted R²** | 决定系数/调整决定系数 |

### 3.2 Model

**Simple linear regression**：

```
y = θ0 + θ1 x + ε
```

- θ0：intercept（截距）；
- θ1：slope（斜率）；
- ε：residual / noise。

**Multiple linear regression**：

```
y = θ0 + θ1 x1 + θ2 x2 + ... + θm xm + ε
```

Vector form（with `x0 = 1`）：

```
y = θᵀ x + ε
```

### 3.3 OLS（normal equation）

Given N samples, design matrix `F`（each row = `[1, x1, ..., xm]`），target vector `y`：

```
y = F θ + ε
```

Loss（sum of squared residuals）：

```
J(θ) = (y - Fθ)ᵀ (y - Fθ)
```

Derivative：

```
∂J/∂θ = -2 Fᵀ(y - Fθ) = 0
```

Normal equation：

```
θ_hat = (Fᵀ F)⁻¹ Fᵀ y
```

⭐ 这是 **closed-form analytical solution**；不需要迭代。

### 3.4 Worked example：simple linear regression

数据：`(1,2), (2,4), (3,5)`。

```
mean x = 2
mean y = 11/3 ≈ 3.667
Sxx = Σ(x - mean x)² = 1 + 0 + 1 = 2
Sxy = Σ(x - mean x)(y - mean y)
    = (-1)(-1.667) + 0 + (1)(1.333)
    = 3.0
slope θ1 = Sxy / Sxx = 3/2 = 1.5
intercept θ0 = mean y - θ1 * mean x
             = 3.667 - 1.5*2 = 0.667
```

So：

```
y_hat = 0.667 + 1.5 x
```

Predictions：`[2.167, 3.667, 5.167]`；residuals `[-0.167, 0.333, -0.167]`。

### 3.5 Ridge and Lasso

**Ridge（L2）**：

```
J(θ) = ||y - Fθ||² + λ ||θ||²
θ_hat = (FᵀF + λI)⁻¹ Fᵀy
```

- λ > 0：shrink weights，处理 `m ≥ N` / singular `FᵀF`；
- λ too large → underfit。

**Lasso（L1）**：

```
J(θ) = ||y - Fθ||² + λ Σ|θ_k|
```

- 倾向把不重要系数压到 **exactly 0** → feature selection；
- 无 closed-form，需数值优化。

⭐ Ridge vs Lasso：Ridge 缩小权重；Lasso 稀疏化（部分权重为 0）。

### 3.6 Regression metrics

| Metric | Formula | Meaning |
|---|---|---|
| **MSE** | `(1/N) Σ (y - y_hat)²` | 均方误差 |
| **RMSE** | `sqrt(MSE)` | 与 y 同量纲 |
| **MAE** | `(1/N) Σ abs(y - y_hat)` | 平均绝对误差 |
| **R²** | `1 - RSS/TSS` | 拟合优度；越接近 1 越好 |
| **Adjusted R²** | `1 - (1-R²)(N-1)/(N-p-1)` | 惩罚 feature 数 |

- `RSS = Σ(y - y_hat)²`；
- `TSS = Σ(y - mean y)²`。

### 3.7 Exam traps

| Trap | Correct |
|---|---|
| OLS 需要迭代 | ❌ 有 closed-form normal equation |
| Ridge 会把系数压到 0 | ❌ Lasso 才会；Ridge 只是 shrink |
| R² 越大一定越好 | ❌ 加 feature 会虚高；用 adjusted R² |
| Regression target 是类别 | ❌ regression 是 continuous target |
| `L=(y-F)²` 的残差就是 y-F | ❌ 是 2(y-F)；1/2 版本才是 y-F |

---

## 4. Feature Selection（特征选择）— Slide 9

### 4.1 Key terms

| English term | 中文 |
|---|---|
| **curse of dimensionality** | 维数灾难 |
| **data sparsity** | 数据稀疏 |
| **distance concentration** | 距离集中 |
| **feature selection** | 特征选择（选子集） |
| **feature extraction** | 特征提取（造新 feature） |
| **peaking phenomenon** | 峰值现象 |
| **Fisher's ratio** | Fisher 比率 |
| **mutual information** | 互信息 |
| **exhaustive search** | 穷举搜索 |
| **sequential forward selection** | 顺序前向选择 |
| **sequential backward elimination** | 顺序后向消除 |
| **filter method** | 过滤法 |
| **wrapper method** | 包装法 |
| **embedded method** | 嵌入式 |
| **Mahalanobis distance** | 马氏距离 |
| **scatter matrix** | 散布矩阵 |
| **relevance / redundancy** | 相关性/冗余 |

### 4.2 Curse of dimensionality

Two main aspects：

1. **Data sparsity**：高维空间中样本太少，覆盖不了空间；
2. **Distance concentration**：高维空间中 pairwise distances 趋于相同，"同类近、异类远"失效。

Why reduce features：

- **Computational complexity**：more features → more parameters；
- **Generalization**：`n_samples / n_parameters` 越高越好；features 多 → 参数多 → overfit。

### 4.3 Peaking phenomenon

- 横轴 feature 数，纵轴 error；
- 先增加 feature → error 下降；
- 超过 critical value `L` → error 上升；
- **更多 training samples → 更大的 L 和更好的 peak performance**。

⭐ 结论：小数据用少 feature；大数据可用更多 feature。

### 4.4 Feature selection vs extraction

| | Feature selection | Feature extraction |
|---|---|---|
| 做法 | 选 subset | 变换生成新 feature |
| 保留原 feature | ✅ | ❌ |
| 例子 | 选 x1, x3 | **PCA** |
| 优点 | 可解释 | 压缩效率高 |

### 4.5 Fisher's ratio

For a binary problem, continuous feature：

```
Fisher = (m1 - m2)² / (s1² + s2²)
```

- `m1,m2`：class means；
- `s1²,s2²`：class variances；
- **larger → more discriminative**；
- 要求 continuous feature（不能直接用于 nominal）。

**Example**：m1=2, s1²=1; m2=6, s2²=4：

```
Fisher = (2-6)² / (1+4) = 16/5 = 3.2
```

### 4.6 Mutual information

```
I(X;Y) = H(X) + H(Y) - H(X,Y)
```

- 衡量 feature X 与 class Y 的 dependence；
- **larger → more relevant**；
- 常用于 discrete/categorical；continuous 可先 discretize（bin）。

### 4.7 Feature subset selection

**Why not top-k?** Top-ranked features may be highly correlated/redundant；good subset = **maximum relevance + minimum redundancy**。

**Search algorithms**：

| Method | Procedure | Note |
|---|---|---|
| **Exhaustive** | all subsets | optimal but combinatorial |
| **Sequential forward** | start empty; add best feature each step | bottom-up |
| **Sequential backward** | start full; remove least important each step | top-down |

**Evaluation criteria**：

- **Wrapper**：train a classifier on each subset; use validation accuracy/error；
  - accurate/matched to classifier, but expensive.
- **Filter**：use separability measure, no classifier；
  - **Mahalanobis distance**：`(m1-m2)ᵀ C⁻¹ (m1-m2)`；
  - **Scatter**：`trace(Sw⁻¹ Sb)` or `trace(Sb)/trace(Sw)`；
  - fast, but distribution assumptions.

**Embedded**：

- Model has built-in feature selection；
- **Lasso**：L1 penalty shrinks unimportant coefficients to 0.

### 4.8 Exam traps

| Trap | Correct |
|---|---|
| 选 top-k 就是好 subset | ❌ 可能高度冗余 |
| Fisher 可用于 categorical | ❌ 需要均值和方差，连续特征 |
| Filter 需要训练 classifier | ❌ wrapper 才训练 |
| Lasso 是 filter | ❌ embedded |
| Peaking：feature 越多越好 | ❌ 先降后升 |
| Mutual information 越大越不相关 | ❌ 越大越相关 |

---

## 5. K-means Clustering（K-means 聚类）— Slide 10

### 5.1 Key terms

| English term | 中文 |
|---|---|
| **clustering** | 聚类 |
| **cluster** | 簇 |
| **centroid** | 质心 |
| **within-cluster sum of squares (WCSS)** | 簇内平方和 |
| **assignment step** | 分配步 |
| **update step** | 更新步 |
| **convergence** | 收敛 |
| **elbow method** | 肘部法 |
| **K** | 簇数 |
| **Minkowski distance** | 闵可夫斯基距离 |
| **Euclidean distance** | 欧氏距离 |
| **Manhattan distance** | 曼哈顿距离 |
| **cosine similarity** | 余弦相似度 |

### 5.2 Distance metrics

**Minkowski distance**：

```
d(x, x') = ( Σ_k |x_k - x'_k|^q )^(1/q)
```

- q=2 → **Euclidean**；
- q=1 → **Manhattan / city-block**；
- **Mahalanobis** 考虑 feature correlation；
- **Cosine similarity**：`xᵀx' / (||x|| ||x'||)`，越大越相似。

### 5.3 K-means objective

```
WCSS = Σ_k Σ_{x ∈ C_k} ||x - μ_k||²
```

- `C_k`：第 k 个 cluster；
- `μ_k`：第 k 个 centroid；
- K-means 最小化 WCSS。

### 5.4 Algorithm（two operations per iteration）

1. 选择 K；
2. 初始化 K 个 centroids（random / random samples）；
3. **Assignment step**：每个 sample 分到**最近的 centroid**；
4. **Update step**：每个 cluster 的新 centroid = 该 cluster 所有 sample 的**均值**；
5. 重复 3–4，直到 **centroid 不再变化** / **assignment 不再变化**。

### 5.5 Worked example 1（1D）

Data：`[1, 2, 3, 10, 11, 12]`，K=2，initial centroids `μ1=1, μ2=12`。

**Iteration 1 — assignment**：

- 1,2,3 → closer to 1 → C1；
- 10,11,12 → closer to 12 → C2。

**Iteration 1 — update**：

```
μ1 = mean(1,2,3) = 2
μ2 = mean(10,11,12) = 11
```

**Iteration 2 — assignment**：same assignment（1,2,3 → 2；10,11,12 → 11）。

**Iteration 2 — update**：μ1=2, μ2=11 → unchanged → **converged**.

### 5.6 Worked example 2（2D）

Data：`A(1,1), B(2,1), C(4,3), D(5,4)`；K=2；initial centroids `μ1=(1,1)`, `μ2=(5,4)`。

**Assignment**：

| Point | Distance to μ1 | Distance to μ2 | Cluster |
|---|---|---|---|
| A(1,1) | 0 | √(16+9)=5 | C1 |
| B(2,1) | 1 | √(9+9)=4.24 | C1 |
| C(4,3) | √(9+4)=3.61 | √(1+1)=1.41 | C2 |
| D(5,4) | 5 | 0 | C2 |

**Update**：

```
μ1 = mean(A,B) = (1.5, 1)
μ2 = mean(C,D) = (4.5, 3.5)
```

Next assignment：A,B stay C1；C,D stay C2 → converged.

### 5.7 Choosing K：Elbow method

- For K=1,2,3,... run K-means；compute WCSS；
- Plot WCSS vs K；
- WCSS always decreases with K（K=N → 0）；
- Find the **elbow** where the decrease becomes slow；
- That K is a reasonable choice。

### 5.8 Limitations

- Assumes **spherical/compact clusters**；
- Sensitive to **initialization**（local minima）；
- Must choose K；
- Sensitive to **feature scaling**；
- Sensitive to **outliers**。

### 5.9 Exam traps

| Trap | Correct |
|---|---|
| K-means 是有监督 | ❌ unsupervised |
| K-means 最大化 WCSS | ❌ minimize |
| 每次迭代只做 assignment | ❌ assignment + update |
| WCSS 随 K 增加而增加 | ❌ 下降 |
| K-means 适合任意形状 cluster | ❌ 球形/紧凑 |
| K-means 对初始化不敏感 | ❌ 敏感，可能 local minimum |

---

## 6. Formula Sheet（考前速记）

```
Entropy:        i_E = -Σ p_j log2 p_j
Gini:           i_Gini = 1 - Σ p_j²  (or (1/2)[1-Σp_j²])
Misclass:       i_MC = 1 - max p_j
Impurity drop:  Δi = i(N) - P_L i(N_L) - P_R i(N_R)
Gain ratio:     Δi' = Δi / (-Σ P_k log2 P_k)

Accuracy:       (TP+TN)/N
Error rate:     (FP+FN)/N
Sensitivity:    TP/(TP+FN) = Recall
Specificity:    TN/(TN+FP)
Precision:      TP/(TP+FP)
F1:             2PR/(P+R)
TPR:            TP/(TP+FN)
FPR:            FP/(FP+TN) = 1 - Specificity

OLS:            θ_hat = (FᵀF)⁻¹Fᵀy
Ridge:          θ_hat = (FᵀF + λI)⁻¹Fᵀy
Lasso:          J = ||y-Fθ||² + λΣ|θ|
MSE:            (1/N)Σ(y-ŷ)²
RMSE:           sqrt(MSE)
MAE:            (1/N)Σ|y-ŷ|
R²:             1 - RSS/TSS

Fisher:         (m1-m2)²/(s1²+s2²)
MI:             H(X)+H(Y)-H(X,Y)
Mahalanobis:    (m1-m2)ᵀ C⁻¹ (m1-m2)
Scatter:        trace(Sw⁻¹Sb) or trace(Sb)/trace(Sw)

K-means WCSS:   Σ_k Σ_{x∈C_k} ||x-μ_k||²
Minkowski:      (Σ|x_k-x'_k|^q)^(1/q)
```

---

## 7. Practice Questions（含答案）

### Q1（Gini）

A node has 10 samples, 5 positive / 5 negative. After a split: left 4 positive + 1 negative; right 1 positive + 4 negative. Compute Gini gain.

**Answer**：

```
G_parent = 1 - 0.5² - 0.5² = 0.5
G_left = 1 - 0.8² - 0.2² = 0.32
G_right = 0.32
G_after = 0.5*0.32 + 0.5*0.32 = 0.32
ΔG = 0.5 - 0.32 = 0.18
```

### Q2（Entropy）

Same split；compute entropy gain.

**Answer**：

```
H_parent = 1
H_left = H_right = -0.8log2 0.8 - 0.2log2 0.2 ≈ 0.7219
H_after ≈ 0.7219
ΔH = 1 - 0.7219 = 0.2781
```

### Q3（Confusion matrix）

TP=85, FP=4, FN=2, TN=9. Compute accuracy, sensitivity, specificity, precision, recall, F1.

**Answer**：

```
Accuracy = (85+9)/100 = 94%
Sensitivity = 85/87 ≈ 97.7%
Specificity = 9/13 ≈ 69.2%
Precision = 85/89 ≈ 95.5%
Recall = 85/87 ≈ 97.7%
F1 = 2*0.955*0.977/(0.955+0.977) ≈ 0.966
```

### Q4（OLS）

Data `(1,2),(2,4),(3,5)`. Find OLS line.

**Answer**：

```
mean x = 2; mean y = 3.667
Sxx = 2; Sxy = 3
slope = 1.5; intercept = 0.667
y_hat = 0.667 + 1.5x
```

### Q5（Ridge）

For `FᵀF = [[2,0],[0,2]]`, `Fᵀy = [4,6]`, λ=2. Find ridge θ.

**Answer**：

```
(FᵀF + λI) = [[4,0],[0,4]]
θ = [[4,0],[0,4]]⁻¹ [4,6] = [1, 1.5]
```

### Q6（Feature selection）

Class 1: mean=2, variance=1; Class 2: mean=6, variance=4. Compute Fisher's ratio.

**Answer**：

```
Fisher = (2-6)² / (1+4) = 16/5 = 3.2
```

### Q7（K-means）

Data `[1,2,3,10,11,12]`, K=2, initial centroids 1 and 12. Do one iteration.

**Answer**：

```
Assignment: {1,2,3}→C1, {10,11,12}→C2
Update: μ1=2, μ2=11
```

### Q8（Elbow）

WCSS for K=1..5: 100, 60, 45, 42, 40. Which K by elbow?

**Answer**：K=3（从 60→45 降幅大，45→42 明显变小）。

---

## 8. Last-minute Checklist

- [ ] Gini / entropy / impurity drop 公式能默写。
- [ ] 连续 feature 的 split 步骤：sort → midpoints → test each。
- [ ] Confusion matrix 四种情况 + 所有指标公式。
- [ ] ROC 横轴 FPR、纵轴 TPR；AUC 含义。
- [ ] OLS normal equation；ridge 加 λI；lasso 稀疏。
- [ ] MSE/RMSE/MAE/R² 公式。
- [ ] Fisher's ratio；mutual information。
- [ ] filter vs wrapper vs embedded。
- [ ] K-means 两步：assignment + update；WCSS 最小化。
- [ ] Elbow method。
- [ ] 英文术语：impurity, split, confusion matrix, precision, recall, OLS, ridge, lasso, Fisher's ratio, mutual information, within-cluster sum of squares。

> **一句话**：Quiz 2 = **Gini/entropy 计算 + confusion matrix 指标 + OLS/ridge + Fisher/MI + K-means 手算**；40 分钟，先做会的，计算题写公式再代数字。
