# EE6406 Analytic and Ensemble Learning — 基础知识复习

> **定位**：这份资料**不讲真题技巧**，只把 **Lecture 1–11 的基础概念、公式、推导**从头串一遍。适合在刷往年卷之前先建立完整框架；配合 `EE6406_Final_Review.pdf`（真题手算版）使用。
>
> **考试结构回顾**：Final **60%**，**3 小时、closed-book、4 题 × 25 分**；约 **2.5 题来自 Part 1（L1–L8，约 62 分）**，**1.5 题来自 Part 2（L9–L13，约 38 分）**。
>
> **术语约定**：英文术语保留原词（考试用英文），中文只做解释。

---

## 目录

0. 机器学习框架（Lecture 1）
1. 数据与预处理（Lecture 2）
2. 线性模型与最小二乘（Lecture 3）
3. 正则化与惩罚学习（Lecture 5、7）
4. 核方法与 Kernel Ridge Regression（Lecture 5）
5. 分类与评分函数（Lecture 4）
6. 高级解析分类：TER / AUC（Lecture 6）
7. 性能评估与统计推断（Lecture 8）
8. 集成学习基础（Lecture 9）
9. 决策树（Lecture 9）
10. Bagging 与 Random Forest（Lecture 9–10）
11. Boosting 与 GBDT（Lecture 9–11）
12. XGBoost（Lecture 11）
13. LightGBM（Lecture 11）
14. 集成方法总对比
15. 概念速答 30 题
16. 公式表
17. 基础自测 15 题＋答案

---

# 0. 机器学习框架（Lecture 1）

## 0.1 什么是机器学习

**Tom Mitchell (1997) 的定义**：

> A computer program is said to **learn** from experience **E** with respect to some task **T** and performance measure **P**, if its performance at tasks in T, as measured by P, improves with experience E.

三个要素：

| 要素 | 含义 | 例子 |
|---|---|---|
| **Task T** | 要解决的问题 | 分类、回归、聚类 |
| **Experience E** | 用来学习的数据/交互 | 带标签的训练集 |
| **Performance P** | 衡量好坏的标准 | accuracy、error rate、F1 |

## 0.2 学习范式

| 范式 | 数据 | 目标 | 典型任务 |
|---|---|---|---|
| **Supervised** | 有标签 $(x,y)$ | 学 $x\to y$ 的映射 | classification、regression |
| **Unsupervised** | 无标签 | 发现数据结构 | clustering、dimensionality reduction |
| **Semi-supervised** | 少量标签 + 大量无标签 | 结合两者 | 半监督分类 |
| **Reinforcement** | 与环境交互的 reward | 最大化累积回报 | 游戏、机器人 |

## 0.3 Analytic Learning vs Iterative Learning

| 维度 | **Analytic Learning** | **Iterative Optimization** |
|---|---|---|
| 解的形式 | **closed-form（解析解）** | 迭代逼近（GD/SGD/Adam） |
| 典型方法 | 最小二乘、ridge、KRR、TER/AUC learning | 神经网络、深度学习 |
| 优点 | 确定、可解释、超参少、无学习率 | 灵活、能处理高度非线性 |
| 缺点 | 需矩阵求逆、扩展性受限 | 依赖超参、可能局部最优 |

⭐ 本课 Part 1 的主线就是 **analytic learning**：把学习问题写成目标函数，直接求出闭式解。

## 0.4 学习的三个组件

```
Learning model（模型）  →  Learning loss（目标函数）  →  Optimization（求解）
   g(x,w)                     L(w)                      closed-form / GD
```

- **Model**：$g(x,w)$，如线性模型、多项式、核模型；
- **Loss**：SSE、cross-entropy、hinge、exponential 等；
- **Optimization**：求 $\hat{w}=\arg\min_w L(w)$。

## 0.5 Generalization（泛化）

- 学习的目标不是"记住训练集"，而是**在未见数据上表现好**；
- 训练误差低 ≠ 测试误差低；差距过大就是 **overfitting**；
- 评估必须用 **unseen data**（hold-out / cross-validation）。

---

# 1. 数据与预处理（Lecture 2）

## 1.1 数据类型（Data Types）

| 类型 | 有无顺序 | 间距可测 | 有无绝对零点 | 例子 |
|---|---|---|---|---|
| **Nominal**（categorical） | 无 | 否 | 否 | 颜色、血型、商品类别 |
| **Ordinal** | 有 | 否（只可排序） | 否 | 满意度 Poor/Fair/Good/Excellent |
| **Interval** | 有 | 是 | **否** | 摄氏温度（0°C ≠ 无温度） |
| **Ratio** | 有 | 是 | **是** | 身高、体重、开尔文温度 |

补充：

- **Binary**：只有两个取值（0/1、Pass/Fail）；
- **Discrete**：可数（人数、交易次数）；
- **Continuous**：可取任意精度（身高、温度）。

⭐ 数据类型决定了**能做什么运算**：nominal 不能比大小，ordinal 能排序但不能做加减，interval 能加减但不能做比值。

## 1.2 数据质量

| 问题 | 说明 | 常见处理 |
|---|---|---|
| **Missing values** | 缺失 | 删除、均值/中位数填补、模型填补、作为特殊值 |
| **Outliers** | 离群点 | 检测（z-score、IQR、MAD）、删除或鲁棒方法 |
| **Noise** | 随机误差 | 平滑、滤波、鲁棒损失 |
| **Duplicates** | 重复样本 | 去重 |
| **Imbalance** | 类别不平衡 | 重采样、重加权、调整阈值、F1/AUC 评估 |

## 1.3 Normalization（归一化）

### 1.3.1 Min-Max Scaling

$$
x' = \frac{x-\min(X)}{\max(X)-\min(X)}
$$

- 映射到 $[0,1]$；
- 对 **min/max 敏感**（有 outlier 时被压缩）。

### 1.3.2 Standardization（Z-score）

$$
x' = \frac{x-\mu}{\sigma}
$$

- 变成 **零均值、单位方差**；
- 适合**近似正态**的数据，或 min/max 不可知时。

### 1.3.3 Median Absolute Deviation（MAD）

$$
\mathrm{MAD} = \operatorname{median}\big(|x_i-\operatorname{median}(X)|\big),
\qquad
x_i' = \frac{x_i-\operatorname{median}(X)}{\mathrm{MAD}}
$$

- 用 **median** 替代 mean ⇒ **对 outlier 鲁棒**；
- 有离群点时优先用 MAD。

### 1.3.4 什么时候必须归一化

- **距离型方法**：KNN、K-means、SVM、KRR、LDA；
- **梯度型方法**：神经网络、GD；
- **不正则化时**：不同量纲会让数值大的特征主导。

## 1.4 编码（Encoding）

| 类型 | 编码 |
|---|---|
| Nominal | **One-hot encoding**（避免引入虚假顺序） |
| Ordinal | **Rank encoding**（按顺序映射到 1…R，再归一化到 [0,1]） |
| Binary | 0/1 |
| 连续 | 归一化/标准化 |

## 1.5 距离度量（Distance Metrics）

$$
d_{\text{Euclidean}}(x,x') = \sqrt{\sum_i (x_i-x_i')^{2}}
$$

$$
d_{\text{Manhattan}}(x,x') = \sum_i |x_i-x_i'|
$$

$$
d_{\text{Minkowski}}(x,x') = \left(\sum_i |x_i-x_i'|^{q}\right)^{1/q}
$$

$$
d_{\text{Chebyshev}}(x,x') = \max_i |x_i-x_i'|
$$

$$
d_{\text{Hamming}}(x,x') = \#\{i: x_i\ne x_i'\}
$$

$$
\cos(x,x') = \frac{x^{T}x'}{\|x\|\,\|x'\|}
$$

- Minkowski：$q=1$ → Manhattan，$q=2$ → Euclidean，$q\to\infty$ → Chebyshev；
- Hamming 用于离散/二值序列；
- 余弦相似度只看**方向**，不看长度。

## 1.6 ⭐ Data Leakage（数据泄漏）

- **错误做法**：在切分 train/test **之前**，用**全部数据**算 mean/variance/min/max 做归一化；
- **后果**：测试集信息泄漏进训练过程，评估结果**虚高**；
- **正确做法**：归一化参数**只在 training set 上计算**，再应用到 validation/test。

## 1.7 数据切分

| 方法 | 做法 | 特点 |
|---|---|---|
| **Hold-out** | 一部分训练、一部分测试 | 简单，但浪费数据 |
| **N-fold CV** | 分 N 折，轮流做测试 | 充分利用数据 |
| **LOOCV** | 每次留 1 个样本 | N 次训练，方差低但慢 |
| **Bootstrap** | 有放回抽样 | 可估计不确定性 |

---

# 2. 线性模型与最小二乘（Lecture 3）

## 2.1 线性参数模型

$$
g(x,w) = w_0 + w_1x_1 + \cdots + w_Dx_D = p(x)^{T}w
$$

- $x\in\mathbb{R}^{D}$：输入特征；
- $p(x)\in\mathbb{R}^{D+1}$：**基函数向量**（含常数项 1）；
- $w\in\mathbb{R}^{D+1}$：待学习参数。

⭐ **"线性"指对参数 $w$ 线性**，不是对输入 $x$ 线性——所以多项式、核方法都算线性参数模型。

## 2.2 基函数（Basis Functions）

| 模型 | $p(x)$ |
|---|---|
| 线性 | $[1, x_1, \dots, x_D]^{T}$ |
| 二次多项式 | $[1, x_1, x_2, x_1^{2}, x_1x_2, x_2^{2}]^{T}$ |
| 自定义 | $[1, x_1, x_1x_2, x_2^{2}]^{T}$ |

⭐ 基函数的作用：把**非线性**问题映射到高维空间，使其**对 $w$ 线性**，从而能用最小二乘求解。

## 2.3 设计矩阵（Design Matrix）

$m$ 个训练样本：

$$
P =
\begin{bmatrix}
p(x_1)^{T}\\
\vdots\\
p(x_m)^{T}
\end{bmatrix}
\in\mathbb{R}^{m\times(D+1)},
\qquad
y=\begin{bmatrix}y_1\\ \vdots\\ y_m\end{bmatrix}
$$

$$
\hat{y} = Pw
$$

## 2.4 最小二乘（Least Squares / LSE）

$$
\mathrm{SSE}(w) = \|y-Pw\|^{2} = (y-Pw)^{T}(y-Pw)
$$

展开：

$$
\mathrm{SSE}(w) = y^{T}y - 2w^{T}P^{T}y + w^{T}P^{T}Pw
$$

求导：

$$
\frac{\partial\,\mathrm{SSE}}{\partial w} = -2P^{T}y + 2P^{T}Pw = 0
$$

**Normal equation（正规方程）**：

$$
P^{T}P\,w = P^{T}y
\quad\Longrightarrow\quad
\boxed{\;\hat{w}=(P^{T}P)^{-1}P^{T}y\;}
$$

## 2.5 几何解释

- $Pw$ 是 $P$ 的**列空间**中的向量；
- 最小二乘 = 在列空间中找**离 $y$ 最近**的点；
- 残差 $y-P\hat{w}$ **垂直于列空间**：

$$
P^{T}(y-P\hat{w})=0
$$

这正是正规方程。

## 2.6 Over-determined vs Under-determined

| 情形 | 条件 | 解 |
|---|---|---|
| **Over-determined** | 样本数 > 参数数（$m>D+1$） | 一般无精确解，最小二乘 |
| **Under-determined** | 样本数 < 参数数（$m<D+1$） | 无穷多解；取**最小范数解**（伪逆） |

- 伪逆（pseudo-inverse）：$\hat{w}=P^{+}y$；
- 实际中加 **regularization**（ridge）更稳。

## 2.7 多项式模型示例

模型：

$$
g(x)=w_0+w_1x+w_2x^{2}
$$

样本 $(x_i,y_i)$ 的设计矩阵：

$$
P=
\begin{bmatrix}
1 & x_1 & x_1^{2}\\
1 & x_2 & x_2^{2}\\
\vdots & \vdots & \vdots\\
1 & x_m & x_m^{2}
\end{bmatrix}
$$

> 阶数越高，模型越灵活，但越容易 **overfitting**；用 regularization 或 CV 选阶数。

---

# 3. 正则化与惩罚学习（Lecture 5、7）

## 3.1 为什么需要正则化

- $P^{T}P$ 可能**不可逆**（共线、样本少）；
- 模型太复杂会 **overfitting**；
- 正则化 = 在损失中加**参数惩罚**，限制模型复杂度。

## 3.2 Ridge Regression（L2）

$$
J(w)=\|y-Pw\|^{2}+\lambda\|w\|^{2}
$$

$$
\boxed{\;\hat{w}=(P^{T}P+\lambda I)^{-1}P^{T}y\;}
$$

- $\lambda>0$ 保证矩阵可逆；
- **shrinkage**：系数被压小，但**一般不为 0**；
- $\lambda\to0$ 退化为最小二乘；$\lambda\to\infty$ 系数趋于 0。

**概率解释**：等价于高斯先验下的 MAP 估计（weight decay）。

## 3.3 Lasso（L1）

$$
J(w)=\|y-Pw\|^{2}+\lambda\|w\|_{1},
\qquad
\|w\|_{1}=\sum_j|w_j|
$$

- **sparse**：部分系数**恰好为 0** ⇒ 自带 **variable selection**；
- 无闭式解（需坐标下降/近端梯度）。

## 3.4 Bridge Regression（$L_p$）

$$
J(w)=\|y-Pw\|^{2}+\lambda\sum_j|w_j|^{p},
\qquad p\ge0
$$

| $p$ | 名称 | 形状 | Shrinkage | Sparse |
|---|---|---|---|---|
| 0 | subset selection | — | 否 | 是 |
| 0.5 | — | 内凹星形 | 是 | 是 |
| 1 | Lasso | 菱形 | 是 | 是 |
| 2 | Ridge | 圆 | 是 | 否 |
| 4 | — | 接近方形 | 是 | 否 |

## 3.5 为什么 L1 稀疏、L2 不稀疏（几何）

- 约束形式：$\|w\|_p\le t$；
- 损失等高线（椭圆）与约束区域**第一次相切**的点就是解；
- **L1 菱形**的顶点在坐标轴上 ⇒ 容易切在顶点 ⇒ 某个系数为 0；
- **L2 圆**没有尖角 ⇒ 切点一般不在轴上 ⇒ 只缩小、不为 0。

## 3.6 正则化的偏差-方差视角

- $\lambda\uparrow$ ⇒ 模型更简单 ⇒ **bias 上升、variance 下降**；
- 通过 **cross-validation** 选 $\lambda$，在 bias-variance 间取平衡。

---

# 4. 核方法与 Kernel Ridge Regression（Lecture 5）

## 4.1 从特征映射到核

若把 $x$ 映射到高维 $p(x)$，内积 $p(x)^{T}p(x')$ 可能很贵。**核函数**直接给出内积：

$$
k(x,x') = p(x)^{T}p(x')
$$

⭐ **Kernel trick**：不需要显式算 $p(x)$，只要算 $k(x,x')$。

## 4.2 Gram Matrix

$$
K=PP^{T}\in\mathbb{R}^{m\times m},
\qquad
K_{ij}=p(x_i)^{T}p(x_j)=k(x_i,x_j)
$$

性质：

- **对称**：$K=K^{T}$；
- **半正定**（PSD）：对任意 $a$，$a^{T}Ka\ge0$；
- 对角元 $K_{ii}=k(x_i,x_i)$。

## 4.3 对偶 Ridge 与 KRR

**Primal**：

$$
\hat{w}=(P^{T}P+\lambda I)^{-1}P^{T}y
$$

**Dual**：令 $w=P^{T}\alpha$，可得

$$
(PP^{T}+\lambda I)\alpha=y
\quad\Longrightarrow\quad
\boxed{\;\hat{\alpha}=(K+\lambda I)^{-1}y\;}
$$

**训练预测**：

$$
\hat{y}=P\hat{w}=PP^{T}\alpha=K\alpha
$$

**测试**：对新样本构造

$$
(K_t)_{ij}=k(x_{ti},x_j),
\qquad
\boxed{\;\hat{y}_t=K_t\hat{\alpha}\;}
$$

⭐ 复杂度：primal 求逆 $O((D+1)^3)$，dual 求逆 $O(m^3)$——**样本少用 dual，特征少用 primal**。

## 4.4 常见核

| 核 | 表达式 | 说明 |
|---|---|---|
| Linear | $x^{T}x'$ | 等价线性回归 |
| Polynomial | $(1+x^{T}x')^{p}$ | $p$ 阶多项式（含交叉项） |
| RBF / Gaussian | $\exp\!\left(-\dfrac{\|x-x'\|^{2}}{2\sigma^{2}}\right)$ | 无限维；$\sigma$ 控制平滑度 |
| Sigmoid | $\tanh(\beta x^{T}x'+c)$ | 类似神经网络 |

## 4.5 核矩阵的意义

- $K$：**训练样本两两相似度**；
- $K_t$：**测试样本与训练样本的相似度**；
- KRR 的预测 = 用相似度做**加权平均**：$\hat{y}_t=\sum_j k(x_t,x_j)\alpha_j$。

---

# 5. 分类与评分函数（Lecture 4）

## 5.1 从回归到分类：阈值

回归输出 $g(x,w)$，选阈值 $\tau$：

$$
\hat{y} =
\begin{cases}
+1, & g(x,w)>\tau\\
-1, & g(x,w)\le\tau
\end{cases}
$$

- $\tau$ 的选择影响 **FPR/FNR** 的平衡；
- 常用 $\tau=0$（若标签为 $\pm1$ 且模型对称）。

## 5.2 Confusion Matrix（混淆矩阵）

| | 预测 Positive | 预测 Negative |
|---|---|---|
| **真实 Positive** | TP | FN（type II error） |
| **真实 Negative** | FP（type I error） | TN |

## 5.3 基本指标

$$
\mathrm{Accuracy}=\frac{TP+TN}{TP+TN+FP+FN}
$$

$$
\mathrm{Sensitivity}=\mathrm{Recall}=\mathrm{TPR}=\frac{TP}{TP+FN}=\frac{TP}{n^{+}}
$$

$$
\mathrm{Specificity}=\mathrm{TNR}=\frac{TN}{FP+TN}=\frac{TN}{n^{-}}
$$

$$
\mathrm{Precision}=\mathrm{PPV}=\frac{TP}{TP+FP}
$$

$$
F_1 = \frac{2\cdot\mathrm{Precision}\cdot\mathrm{Recall}}{\mathrm{Precision}+\mathrm{Recall}}
$$

关系：

$$
TPR+FNR=1,
\qquad
TNR+FPR=1
$$

## 5.4 Skewing Factor 与类别不平衡

$$
s=\frac{n^{-}}{n^{+}}
$$

$$
\mathrm{Accuracy}=\frac{TPR+s\cdot TNR}{1+s}
$$

$$
\mathrm{Precision}=\frac{TPR}{TPR+s\cdot FPR}
$$

$$
F\text{-measure}=\frac{2\,TPR}{TPR+s\cdot FPR+1}
$$

⭐ 类别不平衡时，**accuracy 会误导**（全判多数类也很高）；应看 **F1、AUC、TER**。

## 5.5 ROC 与 AUC

- **ROC**：横轴 FPR，纵轴 TPR；每个点对应一个阈值；
- 对角线 = 随机分类器（AUC = 0.5）；
- **AUC** = ROC 曲线下面积：

$$
\mathrm{AUC}=\frac{1}{m^{+}m^{-}}\sum_{i=1}^{m^{+}}\sum_{j=1}^{m^{-}}
u\big(g(x_i^{+})-g(x_j^{-})\big)
$$

其中 $u(\cdot)$ 是单位阶跃函数。

⭐ **AUC 的等价含义**：随机取一个正样本和一个负样本，**正样本得分更高**的概率。

- AUC 只看**排序**，与阈值无关；
- **Gini = 2·AUC − 1**。

## 5.6 EER（Equal Error Rate）

- 阈值 $\tau$ 变化时，FPR 与 FNR 反向变化；
- 两者相等处：$\mathrm{FPR}=\mathrm{FNR}$ ⇒ **EER**；
- EER 越小越好，常用于生物识别。

## 5.7 TER 与 HTER

$$
\mathrm{TER}=\mathrm{FPR}+\mathrm{FNR}
$$

$$
\mathrm{HTER}=\frac{\mathrm{FPR}+\mathrm{FNR}}{2}
$$

- TER 直接累计**归一化的分类错误**；
- HTER 是 TER 的一半，范围 $[0,1]$。

## 5.8 Loss Functions（Margin 视角）

定义 margin：

$$
\mu = y\,g(x),
\qquad y\in\{-1,+1\}
$$

- $\mu>0$ ⇒ 分类正确；$\mu<0$ ⇒ 错误。

| Loss | 形式 | 用途 |
|---|---|---|
| **0-1 loss** | $\mathbf{1}[\mu\le0]$ | 理想但不可微 |
| **Squared loss** | $(y-g(x))^{2}$ | 回归 |
| **Hinge loss** | $\max(0,1-\mu)$ | SVM |
| **Logistic loss** | $\log(1+e^{-\mu})$ | logistic regression |
| **Exponential loss** | $e^{-\mu}$ | AdaBoost |

⭐ 0-1 loss 不可微，训练时用**光滑代理损失**（hinge/logistic/exponential）。

## 5.9 四种目标函数对比

| 目标 | 类型 | 是否阈值相关 | 优化 |
|---|---|---|---|
| **LSE** | 平方误差 | 否（回归） | 闭式 |
| **MCE** | 误分类数 | 是 | 不可微 |
| **TER** | FPR+FNR | 是 | 闭式（近似） |
| **AUC** | 排序 | **否** | 闭式（成对） |

---

# 6. 高级解析分类：TER / AUC（Lecture 6）

## 6.1 动机

- 分类指标（错误数、TER、AUC）是**计数型/排序型**，不可微；
- 传统上只能迭代优化；
- 本讲通过**变量替换 + sigmoid 近似/二次近似**，把分类目标转成**可微凸问题**，从而得到**闭式解**。

## 6.2 TER Learning

TER：

$$
\mathrm{TER}=\frac{1}{m^{-}}\sum_{j=1}^{m^{-}}
\mathrm{cls}\big(g(x_j^{-})>\tau\big)
+\frac{1}{m^{+}}\sum_{i=1}^{m^{+}}
\mathrm{cls}\big(g(x_i^{+})<\tau\big)
$$

- 用 **sigmoid** 近似 step 函数，使目标可微；
- 解的结构类似 **weighted least squares**（按类归一化）；
- 优点：**直接优化分类错误**，且仍是闭式解。

## 6.3 AUC Learning 与 TAUC

- AUC 可写成**成对（pairwise）**形式；
- 通过 data transformation，把 AUC 最大化转成类似最小二乘的问题；
- **TAUC（Transformed AUC）**：带类别权重 $\beta,\gamma$ 的推广形式，$\beta=\gamma=1$ 时退化为 AUC；
- TAUC 与 **TER、FLD（Fisher LDA）** 都有联系。

## 6.4 与 LSE 的关系

| 解 | 与 LSE 的关系 |
|---|---|
| TER | 加权最小二乘（类内归一化） |
| AUC | 成对加权最小二乘 |
| TAUC | 广义加权形式 |

⭐ 这说明：**分类目标也能像回归一样解析求解**，只是需要对数据做变换。

---

# 7. 性能评估与统计推断（Lecture 8）

## 7.1 评估方法

| 方法 | 做法 | 优缺点 |
|---|---|---|
| **Hold-out** | 训练/测试切分 | 简单；结果依赖切分 |
| **Repeated hold-out** | 多次随机切分取平均 | 降低切分方差 |
| **N-fold CV** | N 折轮流测试 | 数据利用充分 |
| **Repeated N-fold** | 多次 N-fold | 更稳，计算量大 |
| **LOOCV** | 每次留 1 个 | 几乎无偏，但 N 次训练 |
| **Bootstrap** | 有放回重采样 | 可估计置信区间 |

## 7.2 统计检验

| 检验 | 用途 | 说明 |
|---|---|---|
| **McNemar's test** | 比较**两个**分类器在同一测试集上的表现 | 基于 2×2 列联表；统计量近似 $\chi^2$ |
| **Wilcoxon signed-rank** | 比较**两个**算法在**多个数据集**上的配对差异 | 非参数；不假设正态 |
| **Friedman test** | 比较**多个**算法在多个数据集上的排名 | 非参数 ANOVA |
| **Nemenyi post-hoc** | Friedman 显著后，两两比较 | 用 critical difference（CD） |

**McNemar 统计量**（2×2 表：两分类器对/错）：

$$
\chi^{2}=\frac{(|b-c|-1)^{2}}{b+c}
$$

其中 $b,c$ 是"一个对一个错"的两种不一致计数。

**Wilcoxon**：对配对差值取绝对值排名，按正负号求和得 $W$，查表判断显著性。

**Friedman**：每个数据集上给算法排名，算平均秩，构造 $\chi_F^{2}$；显著后用 **Nemenyi** 比较平均秩差与 **critical difference**。

## 7.3 NHST vs Bayesian Analysis

| 维度 | NHST | Bayesian Analysis |
|---|---|---|
| 核心 | $p$-value、显著性 | posterior、可信区间 |
| 结论 | "拒绝/不拒绝 $H_0$" | "参数落在某区间的概率" |
| 常用 | t-test、Wilcoxon、Friedman | Bayes factor、ROPE |
| 争议 | $p$-value 易被误用；不告诉你效应大小 | 需要先验；计算更复杂 |

- **ROPE（region of practical equivalence）**：定义一个"实际等价"的区间，看 posterior 是否落在其中。

## 7.4 评估陷阱

- **Data leakage**：预处理参数不能在测试集上算；
- **Multiple comparisons**：多次检验需校正（Bonferroni 等）；
- **Class imbalance**：accuracy 会误导；
- **Cherry-picking**：只报告最好的结果。

---

# 8. 集成学习基础（Lecture 9）

## 8.1 为什么用集成

- 单个模型可能**高方差**（如深树）或**高偏差**（如线性模型）；
- 组合多个模型可以：
  - **降低方差**（bagging）；
  - **降低偏差**（boosting）；
  - 提高**鲁棒性**和**泛化**。

⭐ 关键前提：基学习器之间要有**多样性（diversity）**——完全相同的模型组合没有意义。

## 8.2 Bias-Variance 分解

$$
\mathbb{E}\big[(\hat{f}(x)-f(x))^{2}\big]
= \mathrm{Bias}^{2}+\mathrm{Var}+\sigma^{2}
$$

| 项 | 含义 | 降低方法 |
|---|---|---|
| **Bias** | 模型假设与真实关系的偏离 | 更复杂模型、boosting |
| **Variance** | 对训练集扰动的敏感度 | 更多数据、正则化、bagging |
| **$\sigma^{2}$** | 不可约噪声 | 无法消除 |

## 8.3 集成的组合方式

| 方式 | 做法 | 典型 |
|---|---|---|
| **Averaging** | 回归取平均 | bagging |
| **Voting** | 分类多数投票 | random forest |
| **Weighted voting** | 按性能加权 | AdaBoost |
| **Stacking** | 用 meta-learner 组合 | 异质模型 |

## 8.4 多样性的来源

- 不同的**训练子集**（bootstrap）；
- 不同的**特征子集**；
- 不同的**模型族**；
- 不同的**超参数/初始化**。

---

# 9. 决策树（Lecture 9）

## 9.1 结构

- **根节点** → 内部节点（测试一个特征）→ 分支 → **叶节点**（预测）；
- 分类树：叶节点输出类别；回归树：叶节点输出均值。

## 9.2 划分准则（Impurity）

**Entropy**：

$$
H=-\sum_{k}p_k\log_2 p_k
$$

**Gini impurity**：

$$
\mathrm{Gini}=1-\sum_k p_k^{2}=\sum_{j\ne k}p_jp_k
$$

**Variance（回归）**：

$$
\mathrm{Var}=\frac{1}{n}\sum_i (y_i-\bar{y})^{2}
$$

## 9.3 信息增益

$$
\Delta I = I(\text{parent})-\sum_{\text{children}}\frac{n_c}{n}I(\text{child})
$$

- 选择使 $\Delta I$ 最大的特征/阈值；
- 连续特征：排序后取相邻值中点作为候选阈值。

## 9.4 生长与剪枝

| 步骤 | 方法 |
|---|---|
| **停止条件** | 最大深度、最小样本数、 impurity 下降阈值 |
| **Pre-pruning** | 提前停止（早停） |
| **Post-pruning** | 先长满再剪枝（代价复杂度剪枝） |

## 9.5 优缺点

| 优点 | 缺点 |
|---|---|
| 可解释、无需归一化 | **高方差**（对数据扰动敏感） |
| 能处理非线性、交互 | 容易 overfitting |
| 训练快 | 对不平衡敏感 |

⭐ 决策树是 **bagging/RF 的基学习器**，因为其高方差正好被平均降低。

---

# 10. Bagging 与 Random Forest（Lecture 9–10）

## 10.1 Bootstrap

- 从 $N$ 个样本中**有放回**抽取 $N$ 个，形成 bootstrap 样本；
- 约 **63.2%** 的原样本会出现（至少一次），**36.8%** 不会出现（OOB）。

## 10.2 Bagging 算法

1. 生成 $M$ 个 bootstrap 样本；
2. 每个样本训练一个基学习器；
3. 聚合：回归取平均，分类多数投票。

## 10.3 方差降低（推导）

设每个学习器方差 $\sigma^{2}$、两两相关 $\rho$：

$$
\mathrm{Var}\left(\frac{1}{M}\sum_{m=1}^{M}f_m\right)
=\rho\sigma^{2}+\frac{1-\rho}{M}\sigma^{2}
$$

- $M\to\infty$ 时趋于 $\rho\sigma^{2}$；
- **只有 $\rho<1$ 时 bagging 才有效**；
- bagging **不改变 bias**（平均不改变期望）。

## 10.4 OOB（Out-of-Bag）

- 每个样本约有 **36.8%** 的树没有见过它；
- 用这些树预测该样本 → **OOB prediction**；
- OOB error ≈ 交叉验证误差，**无需额外验证集**。

## 10.5 Random Forest

在 bagging 基础上再加**随机特征子集**：

- 每次**节点分裂**只从 $m_{try}$ 个随机特征中选最优；
- 分类常用 $m_{try}\approx\sqrt{D}$，回归 $m_{try}\approx D/3$；
- 目的：**降低树间相关性 $\rho$** ⇒ 进一步降方差。

## 10.6 特征重要性

| 方法 | 说明 |
|---|---|
| **Impurity-based（MDI）** | 特征带来的 impurity 下降总和；对高基数特征有偏 |
| **Permutation importance** | 打乱该特征后性能下降 |

## 10.7 优缺点

| 优点 | 缺点 |
|---|---|
| 方差低、精度高 | 可解释性差于单树 |
| 对噪声/outlier 较鲁棒 | 模型大、预测慢 |
| 可并行、有 OOB | 高维稀疏数据不如 boosting |

---

# 11. Boosting 与 GBDT（Lecture 9–11）

## 11.1 基本思想

- **串行**训练弱学习器；
- 每个新学习器**关注前面犯的错误**；
- 最终**加权组合**。

## 11.2 AdaBoost

**Step 1** 初始化权重 $w_i=1/N$。

**Step 2** 训练弱分类器 $f_m$，加权错误率：

$$
\varepsilon_m=\frac{\sum_i w_i\,\mathbf{1}[f_m(x_i)\ne y_i]}{\sum_i w_i}
$$

**Step 3** 学习器权重：

$$
\alpha_m=\frac{1}{2}\ln\frac{1-\varepsilon_m}{\varepsilon_m}
$$

**Step 4** 更新权重：

$$
w_i\leftarrow w_i\exp\!\big(-\alpha_m y_i f_m(x_i)\big)
$$

**Step 5** 最终：

$$
F_M(x)=\operatorname{sign}\!\left(\sum_{m=1}^{M}\alpha_m f_m(x)\right)
$$

⭐ AdaBoost = 在**指数损失** $e^{-yF(x)}$ 上的前向分步加法模型。

## 11.3 Gradient Boosting

把 boosting 看成**函数空间的梯度下降**：

$$
r_{im}=-\left[\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}\right]_{F=F_{m-1}}
$$

用弱学习器拟合 $r_{im}$，再加到模型：

$$
F_m(x)=F_{m-1}(x)+\nu f_m(x)
$$

- $\nu$：learning rate / shrinkage；
- 平方损失下，$r_i=y_i-F_{m-1}(x_i)$ 就是**残差**。

## 11.4 GBDT

- 基学习器 = **回归树**；
- 每轮拟合**负梯度**；
- 叶子值可用 line search 或直接取均值；
- 正则化：shrinkage、subsampling、树深限制。

## 11.5 Boosting vs Bagging

| 维度 | Bagging | Boosting |
|---|---|---|
| 训练 | 并行 | 串行 |
| 主要作用 | 降方差 | 降偏差 |
| 基学习器 | 强（深树） | 弱（浅树） |
| 过拟合 | 较低 | 需正则/早停 |

---

# 12. XGBoost（Lecture 11）

## 12.1 正则化目标

$$
\mathcal{L}^{(m)}=\sum_{i=1}^{n}L\big(y_i,F_{m-1}(x_i)+f_m(x_i)\big)
+\gamma T+\frac{1}{2}\lambda\sum_{j=1}^{T}w_j^{2}
$$

- $T$：叶子数；$w_j$：叶子权重；
- $\gamma$：叶子数惩罚（剪枝）；
- $\lambda$：叶子权重的 L2 正则。

## 12.2 二阶 Taylor 展开

$$
L(y_i,F_{m-1}+f_m(x_i))
\approx L(y_i,F_{m-1})+g_i f_m(x_i)+\frac{1}{2}h_i f_m^{2}(x_i)
$$

$$
g_i=\frac{\partial L}{\partial F}\bigg|_{F_{m-1}},
\qquad
h_i=\frac{\partial^{2}L}{\partial F^{2}}\bigg|_{F_{m-1}}
$$

## 12.3 按叶子重组

$$
\tilde{\mathcal{L}}^{(m)}
=\sum_{j=1}^{T}\left[G_jw_j+\frac{1}{2}(H_j+\lambda)w_j^{2}\right]+\gamma T
$$

$$
G_j=\sum_{i\in I_j}g_i,
\qquad
H_j=\sum_{i\in I_j}h_i
$$

## 12.4 最优叶子权重

$$
\boxed{\;w_j^{*}=-\frac{G_j}{H_j+\lambda}\;}
$$

## 12.5 分裂增益

$$
\mathrm{Gain}=\frac{1}{2}\left[
\frac{G_L^{2}}{H_L+\lambda}
+\frac{G_R^{2}}{H_R+\lambda}
-\frac{(G_L+G_R)^{2}}{H_L+H_R+\lambda}
\right]-\gamma
$$

- Gain < 0 ⇒ 不分裂（$\gamma$ 剪枝）。

## 12.6 缺失值处理

- XGBoost 为每个分裂学习**默认方向**（缺失值走左还是右）；
- 训练时用**无缺失**样本枚举方向，选增益大的。

## 12.7 与 GBDT 的区别

| 维度 | GBDT | XGBoost |
|---|---|---|
| 导数 | 一阶 | **二阶** |
| 正则 | 无显式 | $\gamma T+\frac12\lambda\|w\|^2$ |
| 缺失值 | 需预处理 | **自动学习方向** |
| 并行 | 否 | 特征分裂并行 |
| 剪枝 | 后剪枝 | 内置 $\gamma$ |

---

# 13. LightGBM（Lecture 11）

## 13.1 直方图算法

- 把连续特征**分桶**（如 255 个 bin）；
- 分裂时只需遍历桶边界；
- 优点：内存小、速度快；缺点：损失一些精度。

## 13.2 Leaf-wise 生长

- XGBoost：**level-wise**（逐层生长）；
- LightGBM：**leaf-wise**（每次分裂增益最大的叶子）；
- 优点：收敛快；缺点：容易长深 ⇒ 需 `num_leaves`/`max_depth` 限制。

## 13.3 GOSS（Gradient-based One-Side Sampling）

1. 保留梯度**最大**的 $a\times100\%$ 样本；
2. 从其余样本中**随机抽** $b\times100\%$；
3. 对抽中的小梯度样本乘 $\dfrac{1-a}{b}$ 放大。

⭐ 目的：用更少样本估计梯度，保持分布近似无偏。

## 13.4 EFB（Exclusive Feature Bundling）

- 高维稀疏数据中很多特征**互斥**（不同时非零）；
- 用**图着色**把互斥特征分到同一 bundle；
- 用**偏移量**把多个特征合并成一个，减少特征数。

## 13.5 类别特征

- LightGBM **原生支持 categorical**（不需 one-hot）；
- 按类别统计梯度/直方图找最优分裂。

## 13.6 优缺点

| 优点 | 缺点 |
|---|---|
| 快、内存省 | leaf-wise 易过拟合 |
| 原生类别/缺失值 | 小数据上不如精确贪心 |
| 支持大规模数据 | 参数较多 |

---

# 14. 集成方法总对比

| 方法 | 训练 | 主要作用 | 基学习器 | 关键参数 | 代表 |
|---|---|---|---|---|---|
| Bagging | 并行 | 降方差 | 深树 | $M$、$m_{try}$ | Random Forest |
| AdaBoost | 串行 | 降偏差 | stump | $M$、学习率 | AdaBoost |
| Gradient Boosting | 串行 | 降偏差 | 浅树 | 树数、$\nu$、深度 | GBDT |
| XGBoost | 串行 | 降偏差 + 正则 | 树 | $\gamma,\lambda$、$\eta$ | XGBoost |
| LightGBM | 串行 | 快 + 省内存 | 树 | `num_leaves`、GOSS/EFB | LightGBM |

---

# 15. 概念速答 30 题

1. **Supervised vs unsupervised？** 有/无标签。
2. **Classification vs regression？** 输出离散/连续。
3. **Analytic learning 的优点？** 闭式解、确定、超参少。
4. **为什么需要正则化？** 防止过拟合、保证矩阵可逆。
5. **Ridge vs Lasso？** L2 收缩不稀疏；L1 稀疏可选特征。
6. **为什么 L1 稀疏？** 菱形顶点在坐标轴上。
7. **Normal equation？** $\hat{w}=(P^{T}P)^{-1}P^{T}y$。
8. **Over-determined 怎么办？** 最小二乘。
9. **Under-determined 怎么办？** 最小范数解/正则化。
10. **Kernel trick 是什么？** 用 $k(x,x')$ 替代高维内积。
11. **$K$ 与 $K_t$ 区别？** 训练-训练 vs 测试-训练相似度。
12. **KRR 的解？** $\alpha=(K+\lambda I)^{-1}y$。
13. **Sensitivity？** $TP/(TP+FN)$。
14. **Precision？** $TP/(TP+FP)$。
15. **F1？** 调和平均。
16. **AUC 的含义？** 正样本得分高于负样本的概率。
17. **EER？** FPR=FNR 的点。
18. **TER？** FPR+FNR。
19. **为什么 0-1 loss 不直接用？** 不可微。
20. **Hinge/logistic/exponential 用在哪？** SVM/logistic/AdaBoost。
21. **Bias-variance 分解？** 误差 = bias² + variance + noise。
22. **Bagging 为什么降方差？** 平均 + 多样性。
23. **Bagging 对 bias？** 基本不变。
24. **OOB 比例？** $1/e\approx36.8\%$。
25. **RF 的两个随机性？** bootstrap + 随机特征。
26. **AdaBoost 的 $\alpha$？** $\frac12\ln\frac{1-\varepsilon}{\varepsilon}$。
27. **Gradient boosting 拟合什么？** 负梯度/伪残差。
28. **XGBoost 叶子权重？** $-G/(H+\lambda)$。
29. **$\gamma$ 与 $\lambda$？** 叶子数惩罚 / 权重 L2。
30. **GOSS/EFB？** 梯度采样 / 互斥特征打包。

---

# 16. 公式表

## 16.1 回归

$$
\hat{w}=(P^{T}P)^{-1}P^{T}y
$$

$$
\hat{w}=(P^{T}P+\lambda I)^{-1}P^{T}y
$$

$$
K=PP^{T},\quad
\hat{\alpha}=(K+\lambda I)^{-1}y,\quad
\hat{y}_t=K_t\hat{\alpha}
$$

## 16.2 分类指标

$$
\mathrm{TPR}=\frac{TP}{n^{+}},\quad
\mathrm{TNR}=\frac{TN}{n^{-}},\quad
\mathrm{FPR}=\frac{FP}{n^{-}},\quad
\mathrm{FNR}=\frac{FN}{n^{+}}
$$

$$
\mathrm{TER}=\mathrm{FPR}+\mathrm{FNR},\qquad
\mathrm{HTER}=\frac{\mathrm{TER}}{2}
$$

$$
\mathrm{AUC}=P\big(g(x^{+})>g(x^{-})\big),\qquad
\mathrm{Gini}=2\mathrm{AUC}-1
$$

## 16.3 集成

$$
\mathrm{Var}(\bar{f})=\rho\sigma^{2}+\frac{1-\rho}{M}\sigma^{2}
$$

$$
\left(1-\frac1N\right)^{N}\to e^{-1}\approx0.368
$$

$$
\alpha_m=\frac12\ln\frac{1-\varepsilon_m}{\varepsilon_m}
$$

$$
w_j^{*}=-\frac{G_j}{H_j+\lambda}
$$

$$
\mathrm{Gain}=\frac12\left[
\frac{G_L^{2}}{H_L+\lambda}
+\frac{G_R^{2}}{H_R+\lambda}
-\frac{(G_L+G_R)^{2}}{H_L+H_R+\lambda}
\right]-\gamma
$$

---

# 17. 基础自测 15 题＋答案

**1.** 机器学习的三要素是什么？
**答**：Task T、Experience E、Performance P。

**2.** 说出四种数据类型并各举一例。
**答**：Nominal（血型）、Ordinal（满意度）、Interval（摄氏温度）、Ratio（身高）。

**3.** 有 outlier 时用哪种归一化？
**答**：MAD（或鲁棒方法），不用 z-score。

**4.** 为什么归一化参数只能在训练集上算？
**答**：否则造成 data leakage，测试信息泄漏。

**5.** 写出最小二乘的正规方程。
**答**：$P^{T}Pw=P^{T}y$。

**6.** Ridge 的解是什么？$\lambda$ 的作用？
**答**：$(P^{T}P+\lambda I)^{-1}P^{T}y$；$\lambda$ 控制正则强度。

**7.** 为什么 Lasso 能做特征选择？
**答**：L1 约束的菱形顶点在坐标轴上，部分系数恰为 0。

**8.** KRR 中 $K$ 和 $K_t$ 的维度与含义？
**答**：$K$ 是 $m\times m$（训练-训练），$K_t$ 是 $n\times m$（测试-训练）。

**9.** 写出 sensitivity、specificity、precision。
**答**：$TP/(TP+FN)$、$TN/(TN+FP)$、$TP/(TP+FP)$。

**10.** AUC 为什么与阈值无关？
**答**：它衡量的是所有正负样本对的排序，不依赖某个阈值。

**11.** Bagging 为什么能降方差？公式？
**答**：平均降低方差；$\rho\sigma^2+(1-\rho)\sigma^2/M$。

**12.** OOB 的 36.8% 怎么来的？
**答**：$(1-1/N)^N\to e^{-1}$。

**13.** Random Forest 的两个随机性？
**答**：bootstrap 采样 + 节点随机特征子集。

**14.** AdaBoost 中错误率越低，$\alpha$ 越大还是越小？
**答**：越大。

**15.** XGBoost 相比 GBDT 的三个改进？
**答**：二阶导数、显式正则（$\gamma,\lambda$）、缺失值自动方向。

---

> **复习建议**：先用这份资料建立框架（概念 → 公式 → 直觉），再用 `EE6406_Final_Review.pdf` 做真题手算；两部分配合，Part 1 的 62 分和 Part 2 的 38 分都能覆盖。
