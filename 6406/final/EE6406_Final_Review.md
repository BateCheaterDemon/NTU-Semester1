# EE6406 Analytic and Ensemble Learning — Final Exam Review（期末复习）

> **考试**：**3 小时**，**closed-book**，**4 道题、每题等分（25 分）、全部必答**；Final 占总评 **60%**。
>
> **命题结构（课程公告）**：**约 2.5 题来自 Part 1（Lecture 1–8，Analytic Learning，约 62 分）**，**约 1.5 题来自 Part 2（Lecture 9–13，Ensemble Learning，约 38 分）**。
>
> **两套新真题（2024-25 S2、2025-26 S2）完全印证了这个结构**：Q1–Q3 的**大部分**是 Part 1，Q3 的 (c)(d) 与 Q4 是 Part 2。
>
> **本资料用法**：按 **六个"关卡"** 组织——每个关卡 = 考点公式 + 真题手算 + 答题模板。考前按关卡顺序过一遍，配合第 8 节的 3 小时模拟卷。

---

## 目录

1. 两套真题的命题地图（先看这个）
2. 第一关 — 核矩阵与 Kernel Ridge Regression（20–25 分）
3. 第二关 — 多项式设计矩阵与最小二乘 / XOR（15–25 分）
4. 第三关 — LSE vs TER 决策边界 + $\ell_p$ 范数（12 分）
5. 第四关 — 数据类型与机器学习任务匹配（15–20 分）
6. 第五关 — Bagging、Random Forest 与 OOB（13 分）
7. 第六关 — Boosting / GBDT / XGBoost / LightGBM（25 分）
8. 公式速查表
9. 模拟卷（4 题）＋ 答案要点
10. 考前 2 天计划

---

# 1. 两套真题的命题地图

| 题 | 2025-26 S2（25 分/题） | 2024-25 S2（25 分/题） | 所属 |
|---|---|---|---|
| Q1 | (a) 数据类型 5 选 1（20 分）；(b) 构造 polynomial matrix $P$（5 分） | (a) 5 个项目匹配 ML 任务（15 分）；(b) 核矩阵 $K$ 与测试核矩阵 $K_t$（10 分） | Part 1 |
| Q2 | (a) $K$ vs $K_t$ 概念单选（5 分）；(b) KRR 全流程手算（20 分） | (a)–(d) 多项式模型、SSE、正规方程、XOR（25 分） | Part 1 |
| Q3 | (a) LSE / TER × Linear / Poly 边界（6 分）；(b) $\ell_p$ 范数截面图（6 分）；(c) RF 两大随机性（6 分）；(d) OOB 推导（7 分） | (a) 1D 分类器准确率（6 分）；(b) 收缩 vs 稀疏填表（6 分）；(c) Bagging 对方差/偏差（6 分）；(d) 集成方差推导（7 分） | 前 12 分 Part 1，后 13 分 Part 2 |
| Q4 | XGBoost 目标 + 叶子权重推导（13）；叶子权重手算（4）；GOSS / EFB（8） | Boosting vs Bagging（8）；Gradient Boosting 与残差（8）；XGBoost 正则/剪枝/权重（9） | Part 2 |

**三条结论**：

1. **Part 1 的分数几乎全在 Q1–Q3 的前半**，题型固定为 **概念匹配 + 矩阵手算 + 图像判读**；**Part 2 固定 13 分（Q3 后半）+ 25 分（Q4）= 38 分**。
2. **Q2 一定是"手算大题的 C 位"**：要么 KRR 全流程，要么多项式矩阵 + XOR + 正规方程推导——**必须会写矩阵、会求逆、会推导**。
3. **Q4 一定是 XGBoost 的推导 + 手算 + LightGBM 概念**；把二阶 Taylor 推导背到能默写，25 分基本到手。

---

# 2. 第一关 — 核矩阵与 Kernel Ridge Regression

> **真题**：2025-26 S2 Q2（25 分）、2024-25 S2 Q1(b)（10 分）。
> **必会**：设计矩阵 $P$ → Gram 矩阵 $K=PP^{T}$ → 对偶/核化 → $\alpha=(K+\lambda I)^{-1}y$ → $K_t$ → $\hat{y}_t=K_t\alpha$。

## 2.1 从线性模型到设计矩阵

线性参数模型：

$$
g(x) = p(x)^{T}w = w_0 + w_1x_1 + \cdots + w_Dx_D
$$

- $p(x)\in\mathbb{R}^{D+1}$：把输入 $x$ 映射成**基函数向量**（含常数项 1）；
- $w\in\mathbb{R}^{D+1}$：待学习参数。

把 $m$ 个训练样本按行排成**设计矩阵（design matrix）**：

$$
P =
\begin{bmatrix}
p(x_1)^{T}\\
p(x_2)^{T}\\
\vdots\\
p(x_m)^{T}
\end{bmatrix}
\in\mathbb{R}^{m\times(D+1)},
\qquad
y =
\begin{bmatrix}
y_1\\ \vdots\\ y_m
\end{bmatrix}
$$

于是所有训练输出：

$$
\hat{y} = Pw
$$

> 记号提醒：课程里 $P$ 有时写作 $\Phi$，含义相同；**行 = 样本，列 = 基函数**。

## 2.2 最小二乘与正规方程

**Sum of Squared Errors（SSE）**：

$$
\mathrm{SSE}(w) = \|y-Pw\|^{2} = (y-Pw)^{T}(y-Pw)
$$

展开：

$$
\mathrm{SSE}(w) = y^{T}y - 2w^{T}P^{T}y + w^{T}P^{T}Pw
$$

对 $w$ 求导并令零：

$$
\frac{\partial\,\mathrm{SSE}}{\partial w} = -2P^{T}y + 2P^{T}Pw = 0
$$

$$
\boxed{\;P^{T}P\,w = P^{T}y
\quad\Longrightarrow\quad
\hat{w} = (P^{T}P)^{-1}P^{T}y\;}
$$

> **前提**：$P^{T}P$ 可逆（列满秩，样本数 ≥ 参数数且特征不共线）。若不可逆或过拟合，就加正则。

## 2.3 岭回归（Ridge）与对偶

**Primal ridge regression**：

$$
J(w) = \|y-Pw\|^{2} + \lambda\|w\|^{2}
$$

$$
\boxed{\;\hat{w} = (P^{T}P+\lambda I)^{-1}P^{T}y\;}
$$

- $\lambda>0$ 保证矩阵可逆、抑制过拟合；$\lambda\to0$ 退化为最小二乘。

**对偶（dual）形式**：当**样本数 $m$ 远小于特征维 $D+1$** 时，在 $m$ 维空间求逆更便宜。令

$$
w = P^{T}\alpha
$$

则

$$
(P^{T}P+\lambda I)P^{T}\alpha = P^{T}y
$$

左乘 $(P^{T}P+\lambda I)^{-1}$ 后整理可得

$$
(PP^{T}+\lambda I)\alpha = y
\quad\Longrightarrow\quad
\boxed{\;\hat{\alpha} = (K+\lambda I)^{-1}y\;}
$$

其中

$$
K = PP^{T}\in\mathbb{R}^{m\times m},
\qquad
K_{ij} = p(x_i)^{T}p(x_j)
$$

称为 **Gram matrix（格拉姆矩阵）**。

## 2.4 核技巧（Kernel Trick）

若把内积 $p(x_i)^{T}p(x_j)$ 直接替换成**核函数** $k(x_i,x_j)$，就得到 **Kernel Ridge Regression（KRR）**，无需显式构造高维 $p(x)$：

$$
K_{ij} = k(x_i,x_j)
$$

常见核：

| 核 | 表达式 | 说明 |
|---|---|---|
| Linear | $k(x,x') = x^{T}x'$ | 等价于线性回归 |
| Polynomial | $k(x,x') = (1+x^{T}x')^{p}$ | $p=2$ 对应二阶多项式（含交叉项） |
| RBF / Gaussian | $k(x,x') = \exp\!\left(-\dfrac{\|x-x'\|^{2}}{2\sigma^{2}}\right)$ | 无限维特征空间 |
| Sigmoid | $k(x,x') = \tanh(\beta x^{T}x' + c)$ | 类似神经网络 |

**训练**：

$$
\boxed{\;\hat{\alpha} = (K+\lambda I)^{-1}y\;}
$$

**测试**：对新样本 $x_{t1},\dots,x_{tn}$，构造**测试核矩阵**

$$
(K_t)_{ij} = k(x_{ti},\,x_j),
\qquad
K_t\in\mathbb{R}^{n\times m}
$$

$$
\boxed{\;\hat{y}_t = K_t\,\hat{\alpha}\;}
$$

## 2.5 ⭐ 概念题：$K$ 与 $K_t$ 的区别（2025-26 S2 Q2a，5 分）

正确答案：

> The training kernel matrix $K$ represents **pairwise similarities among training samples**, while the test kernel matrix $K_t$ represents **similarities between test samples and training samples**.

- $K$：$m\times m$，**训练点 × 训练点**；
- $K_t$：$n\times m$，**测试点（行）× 训练点（列）**，每一行是"这个测试点与所有训练点的相似度"。

## 2.6 真题手算 A：2024-25 S2 Q1(b)

数据：

$$
x_1=(2,4),\quad x_2=(4,8),\quad x_3=(4,2),\quad x_4=(8,8)
$$

核：

$$
k(x_i,x_j) = 1 + e^{-0.01\,x_i^{T}x_j}
$$

**Step 1：先算内积 $x_i^{T}x_j$**

| $x_i^{T}x_j$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | 20 | 40 | 16 | 48 |
| 2 | 40 | 80 | 32 | 96 |
| 3 | 16 | 32 | 20 | 48 |
| 4 | 48 | 96 | 48 | 128 |

**Step 2：代核函数（保留 2 位小数）**

$$
K =
\begin{bmatrix}
1.82 & 1.67 & 1.85 & 1.62\\
1.67 & 1.45 & 1.73 & 1.38\\
1.85 & 1.73 & 1.82 & 1.62\\
1.62 & 1.38 & 1.62 & 1.28
\end{bmatrix}
$$

（例：$k_{11}=1+e^{-0.2}=1.8187\to1.82$；$k_{12}=1+e^{-0.4}=1.6703\to1.67$。）

**Step 3：测试样本 $(4,6),(6,4)$ 的 $K_t$**（$2\times4$，行 = 测试点，列 = 训练点）

$$
K_t =
\begin{bmatrix}
1.73 & 1.53 & 1.76 & 1.45\\
1.76 & 1.57 & 1.73 & 1.45
\end{bmatrix}
$$

（例：$k((4,6),(2,4))=1+e^{-0.01(8+24)}=1+e^{-0.32}=1.726\to1.73$。）

> **陷阱**：$K$ 一定**对称**；$K_t$ **不对称**（行列含义不同）。题目要求 2 位小数时，**每个元素都要写全**。

## 2.7 真题手算 B：2025-26 S2 Q2(b)（KRR 全流程，20 分）

数据：

$$
x_1=(1,2),\quad x_2=(3,0),
\qquad
y_1=2,\quad y_2=-1
$$

二阶多项式核（unit bias）：

$$
k(x_i,x_j) = (1+x_i^{T}x_j)^{2},
\qquad
\lambda = 0.1
$$

### (i) 训练核矩阵 $K$

$$
x_1^{T}x_1 = 1+4 = 5,\quad
x_1^{T}x_2 = 3,\quad
x_2^{T}x_2 = 9
$$

$$
K =
\begin{bmatrix}
(1+5)^2 & (1+3)^2\\
(1+3)^2 & (1+9)^2
\end{bmatrix}
=
\begin{bmatrix}
36 & 16\\
16 & 100
\end{bmatrix}
$$

### (ii) 对偶系数 $\alpha$

$$
K+\lambda I =
\begin{bmatrix}
36.1 & 16\\
16 & 100.1
\end{bmatrix}
$$

行列式：

$$
\det = 36.1\times100.1 - 16^2 = 3613.61-256 = 3357.61
$$

$2\times2$ 求逆口诀：**主对角互换、副对角变号、除以行列式**：

$$
(K+\lambda I)^{-1}
= \frac{1}{3357.61}
\begin{bmatrix}
100.1 & -16\\
-16 & 36.1
\end{bmatrix}
$$

$$
\alpha = (K+\lambda I)^{-1}y
= \frac{1}{3357.61}
\begin{bmatrix}
100.1 & -16\\
-16 & 36.1
\end{bmatrix}
\begin{bmatrix}
2\\-1
\end{bmatrix}
=
\begin{bmatrix}
0.0644\\-0.0203
\end{bmatrix}
$$

（手算：$100.1\times2 + (-16)(-1)=216.2$；$(-16)\times2 + 36.1\times(-1)=-68.1$。）

$$
\boxed{\;\alpha \approx [0.064,\ -0.020]^{T}\;}
$$

### (iii) 测试核矩阵 $K_t$

测试点：

$$
x_{t1}=(0,1),\qquad x_{t2}=(2,2)
$$

$$
x_{t1}^{T}x_1 = 2,\quad x_{t1}^{T}x_2 = 0,
\qquad
x_{t2}^{T}x_1 = 6,\quad x_{t2}^{T}x_2 = 6
$$

$$
K_t =
\begin{bmatrix}
(1+2)^2 & (1+0)^2\\
(1+6)^2 & (1+6)^2
\end{bmatrix}
=
\begin{bmatrix}
9 & 1\\
49 & 49
\end{bmatrix}
$$

### (iv) 预测输出

$$
\hat{y}_t = K_t\alpha
=
\begin{bmatrix}
9 & 1\\
49 & 49
\end{bmatrix}
\begin{bmatrix}
0.0644\\-0.0203
\end{bmatrix}
=
\begin{bmatrix}
0.559\\
2.161
\end{bmatrix}
$$

> **答题模板**：每一步都写"矩阵 + 数值"，并注明维度：$K\in\mathbb{R}^{2\times2}$、$\alpha\in\mathbb{R}^{2}$、$K_t\in\mathbb{R}^{2\times2}$、$\hat{y}_t\in\mathbb{R}^{2}$。

## 2.8 常见陷阱

| 陷阱 | 正确做法 |
|---|---|
| 把 $K_t$ 当成对称矩阵 | $K_t$ 是 $n\times m$，**行是测试点** |
| 忘记 $\lambda I$ | 加在**对角线**上；$\lambda$ 乘单位阵 |
| $P$ 的行列搞反 | 行 = 样本，列 = 基函数 |
| 核函数里的内积算错 | 先列内积表，再代指数/平方 |
| 求逆算错 | 用 $2\times2$ 口诀，最后代回验证 $A\alpha\approx y$ |

---

# 3. 第二关 — 多项式设计矩阵与最小二乘 / XOR

> **真题**：2025-26 S2 Q1(b)（5 分，构造 $P$）、2024-25 S2 Q2（25 分，内积形式 + 矩阵形式 + 推导 + XOR）。
> **必会**：把任意多项式模型写成 $g(x)=p(x)^{T}w$，排成 $P$，写 SSE，推导正规方程，并解释 XOR 为什么能被 $x_1^{3}x_2^{3}$ 解决。

## 3.1 基函数与设计矩阵

给定模型

$$
g(x,w) = w_0 + w_1x_1 + w_1x_1x_2 + w_2x_2^{2}
$$

把每一项的"系数"提出来，定义基函数向量：

$$
p(x) = \begin{bmatrix}1\\ x_1\\ x_1x_2\\ x_2^{2}\end{bmatrix},
\qquad
w = \begin{bmatrix}w_0\\ w_1\\ w_1\\ w_2\end{bmatrix}
$$

则 $g(x,w)=p(x)^{T}w$。设计矩阵的**每一行**就是把一个样本代入 $p(x)$。

## 3.2 真题手算 C：2025-26 S2 Q1(b)

模型：

$$
g(x,w) = 1 + x_1 + x_1x_2 + x_2^{2}
$$

（注意：**常数项 1 是模型的一部分，不是参数**；等价于 $p(x)=[1,x_1,x_1x_2,x_2^2]^{T}$。）

样本：

$$
(2,1),\ (3,3),\ (5,8),\ (6,6)
$$

逐行代入：

$$
P =
\begin{bmatrix}
1 & 2 & 2\cdot1 & 1^{2}\\
1 & 3 & 3\cdot3 & 3^{2}\\
1 & 5 & 5\cdot8 & 8^{2}\\
1 & 6 & 6\cdot6 & 6^{2}
\end{bmatrix}
=
\begin{bmatrix}
1 & 2 & 2 & 1\\
1 & 3 & 9 & 9\\
1 & 5 & 40 & 64\\
1 & 6 & 36 & 36
\end{bmatrix}
$$

> **易错**：第三列是 $x_1x_2$（交叉项），不是 $x_2$；第四列是 $x_2^{2}$。

## 3.3 真题手算 D：2024-25 S2 Q2（XOR，25 分）

模型：

$$
g(x) = w_0 + w_1x_1^{3}x_2^{3}
$$

### (a) 内积形式（4 分）

$$
g(x) = p(x)^{T}w,
\qquad
p(x) = \begin{bmatrix}1\\ x_1^{3}x_2^{3}\end{bmatrix},
\qquad
w = \begin{bmatrix}w_0\\ w_1\end{bmatrix}
$$

### (b) 矩阵形式与 SSE（4 分）

$N$ 个样本排成

$$
X =
\begin{bmatrix}
1 & x_{1,1}^{3}x_{1,2}^{3}\\
\vdots & \vdots\\
1 & x_{N,1}^{3}x_{N,2}^{3}
\end{bmatrix}
\in\mathbb{R}^{N\times2},
\qquad
y = [y_1,\dots,y_N]^{T}
$$

$$
\mathrm{SSE}(w) = (y-Xw)^{T}(y-Xw)
$$

### (c) 推导最小二乘解（4 分）

$$
\frac{\partial\,\mathrm{SSE}}{\partial w}
= -2X^{T}y + 2X^{T}Xw = 0
$$

$$
\boxed{\;\hat{w} = (X^{T}X)^{-1}X^{T}y\;}
$$

（要求 $X^{T}X$ 可逆；这里恰好是 $4I$。）

### (d) XOR 手算（13 分）

XOR 数据：

$$
x_1=\begin{bmatrix}-1\\-1\end{bmatrix},
x_2=\begin{bmatrix}-1\\+1\end{bmatrix},
x_3=\begin{bmatrix}+1\\-1\end{bmatrix},
x_4=\begin{bmatrix}+1\\+1\end{bmatrix},
\qquad
y=\begin{bmatrix}-1\\+1\\+1\\-1\end{bmatrix}
$$

**Step 1：算特征 $x_1^{3}x_2^{3}$**

| 样本 | $x_1$ | $x_2$ | $x_1^{3}x_2^{3}$ | $y$ |
|---|---|---|---|---|
| 1 | −1 | −1 | $(-1)(-1)=+1$ | −1 |
| 2 | −1 | +1 | $(-1)(+1)=-1$ | +1 |
| 3 | +1 | −1 | $(+1)(-1)=-1$ | +1 |
| 4 | +1 | +1 | $(+1)(+1)=+1$ | −1 |

$$
X =
\begin{bmatrix}
1 & 1\\
1 & -1\\
1 & -1\\
1 & 1
\end{bmatrix}
$$

**Step 2：$X^{T}X$ 与 $X^{T}y$**

$$
X^{T}X =
\begin{bmatrix}
4 & 1+(-1)+(-1)+1\\
1+(-1)+(-1)+1 & 1+1+1+1
\end{bmatrix}
=
\begin{bmatrix}
4 & 0\\
0 & 4
\end{bmatrix}
=4I
$$

$$
X^{T}y =
\begin{bmatrix}
-1+1+1-1\\
(-1)(1)+(1)(-1)+(1)(-1)+(-1)(1)
\end{bmatrix}
=
\begin{bmatrix}
0\\
-4
\end{bmatrix}
$$

**Step 3：解**

$$
\hat{w} = (4I)^{-1}
\begin{bmatrix}0\\-4\end{bmatrix}
=
\begin{bmatrix}0\\-1\end{bmatrix}
$$

$$
\hat{y} = X\hat{w} =
\begin{bmatrix}
1 & 1\\1 & -1\\1 & -1\\1 & 1
\end{bmatrix}
\begin{bmatrix}0\\-1\end{bmatrix}
=
\begin{bmatrix}-1\\+1\\+1\\-1\end{bmatrix}
= y
$$

**Step 4：结论（为什么能解 XOR）**

> $x_1^{3}x_2^{3}$ 在**同号象限**（$++$ 或 $--$）取 $+1$，在**异号象限**（$+-$ 或 $-+$）取 $-1$。XOR 的标签恰好就是这个符号：同号 → $-1$，异号 → $+1$。因此取 $w_0=0,\ w_1=-1$ 即可**完美分类**，$\mathrm{SSE}=0$。

$$(w_0,w_1)=(0,-1) \text{ 等价于把 } x_1^3x_2^3 \text{ 的符号翻转。}$$

⭐ 一般化答案：**非线性交互项把 XOR 映射到一维空间，使其线性可分**——The nonlinear interaction term maps same-sign quadrants to $+1$ and opposite-sign quadrants to $-1$, making the XOR data linearly separable in the transformed feature space.

## 3.4 答题模板

```
1. 写 p(x) 与 w，说明维度
2. 逐行代入，写出 P（不要跳行）
3. 写 SSE = (y − Pw)^T (y − Pw)
4. 求导 → 正规方程 → w_hat = (P^T P)^{-1} P^T y
5. 代入数字，算 w_hat 与 y_hat，最后解释（SSE=0 / 可分）
```

---

# 4. 第三关 — LSE vs TER 决策边界 + $\ell_p$ 范数

> **真题**：两套卷的 Q3(a)(b)，共 12 分。**这是"看图 + 概念"题，不能空。**

## 4.1 LSE 与 TER 的定义

**Least Squares Error（LSE）**：最小化平方误差

$$
\min_w \sum_{i=1}^{m}\big(y_i - g(x_i,w)\big)^{2}
$$

**Total Error Rate（TER）**：直接最小化分类错误率

$$
\mathrm{TER} = \mathrm{FPR} + \mathrm{FNR}
$$

$$
\mathrm{TER} =
\frac{1}{m^{-}}\sum_{j=1}^{m^{-}}\mathrm{cls}\big(g(x_j^{-},w)>\tau\big)
+
\frac{1}{m^{+}}\sum_{i=1}^{m^{+}}\mathrm{cls}\big(g(x_i^{+},w)<\tau\big)
$$

- $\mathrm{cls}(\cdot)\in\{0,1\}$ 是指示函数；$\tau$ 是阈值；
- TER **按类归一化**：正负类**各自平均**，所以**不受类别数量不平衡影响**；
- LSE 是**平方误差**，样本多的类对目标函数贡献大 ⇒ **边界被"拉向"样本多的那一侧**。

## 4.2 判读决策边界（2025-26 S2 Q3a，6 分）

题目给四条边界（A、B、C、D），要求写出：

```
Classifier X = Y + Z      （Y ∈ {LSE, TER}，Z ∈ {Linear, Poly}）
```

**判读方法**：

| 维度 | 观察 | 结论 |
|---|---|---|
| **模型类型** | 边界是**直线** ⇒ Linear；**弯曲**（曲线/闭合曲线）⇒ Poly | 先分 Linear / Poly |
| **目标函数** | 两类样本**密度差异大**时：**LSE 边界偏向稀疏类**（因为密集类样本多、平方误差权重大，模型优先把密集类分对）；**TER 边界居中**（两类错误等权） | 再分 LSE / TER |

真题答案（2025-26 S2）：**A = LSE + Linear，B = TER + Linear，C = LSE + Poly，D = TER + Poly**。

> 逻辑：A、C 是实线且**明显偏向稀疏的负类**（把密集正类全部包住）⇒ LSE；B、D 是虚线、**位于两类中间** ⇒ TER；A/B 直 ⇒ Linear，C/D 弯 ⇒ Poly。

## 4.3 1D 曲线算准确率（2024-25 S2 Q3a，6 分）

题目给三条分类器曲线 $g_A(x),g_B(x),g_C(x)$，以及 1D 数据点（4 个方块 $+1$、6 个圆圈 $-1$，共 10 个）。

**做法**：

1. 找到每条曲线的**判零阈值**（$g(x)=0$ 的交点）；
2. 数**被分错的点数**（正类落在 $g<0$ 一侧、负类落在 $g>0$ 一侧）；
3. 准确率 = $\dfrac{\text{正确数}}{10}\times100\%$。

真题答案：**A = 70%，B = 90%，C = 100%**。

> **得分点**：写出"错几个 / 共 10 个"的算式，而不是只写百分数。

## 4.4 $\ell_p$ 范数的几何（2025-26 S2 Q3b，6 分）

$$
\|w\|_p = \left(|w_1|^{p}+|w_2|^{p}\right)^{1/p}
$$

| $p$ | 等值线形状 | 凸性 | 稀疏性 |
|---|---|---|---|
| $0<p<1$ | **内凹星形**（尖刺伸向坐标轴） | **非凸** | 强稀疏 |
| $p=1$ | **菱形**（顶点在坐标轴上） | 凸 | **稀疏**（Lasso） |
| $1<p<2$ | 略内凹的圆角 | 凸 | 弱稀疏 |
| $p=2$ | **圆/椭圆** | 凸 | 不稀疏（Ridge） |
| $p\to\infty$ | **正方形**（Chebyshev） | 凸 | 不稀疏 |

真题映射（2025-26 S2）：**$p=8\to(a)$，$p=0.5\to(b)$，$p=1.1\to(c)$，$p=2\to(d)$**。

- (a) 平底"锅"、接近方形 ⇒ $p=8$；
- (b) 四角内凹、尖刺 ⇒ $p=0.5$；
- (c) V 字折角但圆滑 ⇒ $p=1.1$；
- (d) 抛物线圆底 ⇒ $p=2$。

## 4.5 收缩（Shrinkage）与稀疏（Sparse）填表（2024-25 S2 Q3b，6 分）

| $q$ | 常见名称 | Coefficient shrinkage | Sparse |
|---|---|---|---|
| 0 | Variable subset selection | **No** | **Yes** |
| 0.5 | — | Yes | Yes |
| 1 | Lasso | **Yes** | **Yes** |
| 2 | Ridge | Yes | No |
| 4 | — | **Yes** | **No** |

**为什么要背**：

- **Shrinkage**：系数被"压小"（所有 $q>0$ 都有）；
- **Sparse**：部分系数**恰好为 0**（只有 $q\le1$ 才有；$q=0$ 是直接选子集，也稀疏，但不"收缩"）。

**几何解释**：$\ell_1$ 球的**顶点在坐标轴上**，平方误差的椭圆最先碰到顶点 ⇒ 某个系数为 0；$\ell_2$ 球是圆的，接触点一般不在轴上 ⇒ 只缩小不为 0。

## 4.6 答题模板

```
1. 先判断"直线/曲线" → Linear / Poly
2. 再判断"边界偏向哪边" → LSE（偏向稀疏类）/ TER（居中）
3. 图表题：写清楚"错几个点 / 共几个点"
4. ℓp 题：按 p 从小到大写形状与稀疏性，直接对应图号
```

---

# 5. 第四关 — 数据类型与机器学习任务匹配

> **真题**：2025-26 S2 Q1(a)（20 分，数据类型 5 选 1）、2024-25 S2 Q1(a)（15 分，项目匹配 ML 任务）。
> **这是"送分题"，但不能丢**：四个数据类型、五个 ML 任务的定义要分清。

## 5.1 数据类型（Data Types）

| 类型 | 定义 | 判据 | 例子 |
|---|---|---|---|
| **Categorical Nominal** | 类别，**无顺序** | 只是标签 | 商品类别（Electronics/Clothing/Toys）、性别、血型 |
| **Ordinal** | 类别，**有顺序**，但**间距不可测** | 能排序，不能做加减 | 满意度（Poor/Fair/Good/Excellent）、病情等级、学历 |
| **Binary** | 只有**两个取值** | 0/1、是/否 | 贷款批准（1/0）、性别（若只有两值）、是否患病 |
| **Continuous Numerical** | 连续数值 | 可取任意精度、可加减 | 身高（cm）、温度（°C）、体重 |
| Discrete Numerical | 离散计数 | 整数、可数 | 人数、交易次数 |
| Interval / Ratio | 连续数值的细分 | 有无绝对零点 | 摄氏（interval）vs 开尔文（ratio） |

⭐ **易错点**：

- **满意度**虽然有"好坏"，但**等级之间的差距不能量化** ⇒ **Ordinal**，不是 continuous；
- **贷款批准 1/0** 虽然用数字表示，本质是**二值类别** ⇒ **Binary**，不是 numerical；
- **温度 °C** 是 interval（0°C 不是"没有温度"），但在题目只给 "Continuous Numerical" 时选它；
- **商品类别**没有顺序 ⇒ **Categorical Nominal**。

## 5.2 真题答案（2025-26 S2 Q1a，20 分）

| 小问 | 描述 | 答案 |
|---|---|---|
| (i) | 满意度 Poor/Fair/Good/Excellent，有顺序但差距不可量化 | **Ordinal** |
| (ii) | 商品类别 Electronics/Clothing/Toys，无顺序 | **Categorical Nominal** |
| (iii) | 身高（cm/m），可任意精度 | **Continuous Numerical** |
| (iv) | 贷款批准 1/0 | **Binary** |
| (v) | 每日温度（°C），连续 | **Continuous Numerical** |

> 题目提供的四个选项：Continuous Numerical、Categorical Nominal、Ordinal、Binary——**必须从这四个里选**，不要自创 interval/ratio。

## 5.3 机器学习任务（ML Tasks）

| 任务 | 定义 | 关键判据 | 例子 |
|---|---|---|---|
| **Regression** | 预测**连续值** | 输出是数值 | 销售额、房价、温度 |
| **Classification** | 预测**离散类别** | 输出是类别（有 label） | 情感三分类、垃圾邮件 |
| **Clustering** | **无监督**分组 | 没有 label | 客户分群、图像分割 |
| **Identity Verification** | **1:1** 比对：这个人是"他声称的那个人"吗？ | 有 ID + 待验证样本 | 登录核验、指纹解锁 |
| **Identity Recognition** | **1:N** 搜索：这个人是库里哪一位？ | 在数据库中找人 | 人脸库检索、嫌疑人识别 |

⭐ **Verification vs Recognition 的区别（必考）**：

- **Verification = 1:1**：先声称身份，再验证真假（yes/no）；
- **Recognition = 1:N**：不声称身份，在 N 个候选里找出是谁（open-set 还可能是"不在库里"）。

## 5.4 真题答案（2024-25 S2 Q1a，15 分）

| 项目 | 描述 | 答案 |
|---|---|---|
| A | 用历史销量、营销投入、季节趋势预测未来销量 | **Regression** |
| B | 把客户评论分为 positive / neutral / negative | **Classification** |
| C | 按购买行为与人口统计把客户分组 | **Clustering** |
| D | 用户登录时用密码与存储数据比对，确认是本人 | **Identity Verification** |
| E | 在照片中用人脸特征与已知人脸库比对，识别是谁 | **Identity Recognition** |

## 5.5 答题模板

```
数据类型：先问"有没有顺序？" → 无 = Nominal；有但差距不可测 = Ordinal；
          只有两个值 = Binary；可取任意精度 = Continuous Numerical
ML 任务：先问"有没有 label？" → 无 = Clustering；
          有 → 输出连续 = Regression；输出类别 = Classification；
          比对身份 → 1:1 = Verification；1:N = Recognition
```

---

# 6. 第五关 — Bagging、Random Forest 与 OOB

> **真题**：两套卷的 Q3(c)(d)，共 13 分。**推导题固定**：集成方差公式 + OOB 概率。

## 6.1 Bagging 的基本思想

**Bootstrap AGGregating（Bagging）**：

1. 从训练集**有放回**抽 $N$ 个样本，得到 $M$ 个 bootstrap 子集；
2. 每个子集训练一个基学习器 $f_m$；
3. **聚合**：回归取平均，分类取多数投票。

$$
\bar{f}(x) = \frac{1}{M}\sum_{m=1}^{M} f_m(x)
$$

## 6.2 ⭐ 集成方差推导（2024-25 S2 Q3d，7 分）

设 $M$ 个学习器**方差相同** $\mathrm{Var}(f_m)=\sigma^{2}$，**两两相关系数**为 $\rho$。

$$
\mathrm{Var}\big(\bar{f}\big)
= \mathrm{Var}\!\left(\frac{1}{M}\sum_{m=1}^{M}f_m\right)
= \frac{1}{M^{2}}\left[\sum_{m=1}^{M}\mathrm{Var}(f_m)
+ \sum_{i\ne j}\mathrm{Cov}(f_i,f_j)\right]
$$

代入 $\mathrm{Var}(f_m)=\sigma^{2}$、$\mathrm{Cov}(f_i,f_j)=\rho\sigma^{2}$：

$$
\mathrm{Var}(\bar{f})
= \frac{1}{M^{2}}\Big[M\sigma^{2} + M(M-1)\rho\sigma^{2}\Big]
$$

$$
\boxed{\;\mathrm{Var}(\bar{f})
= \rho\sigma^{2} + \frac{1-\rho}{M}\sigma^{2}\;}
$$

**讨论**：

- $M\to\infty$ 时，第二项 $\to0$，方差趋于 $\rho\sigma^{2}$；
- **只有 $\rho<1$（学习器不完全相关）时，bagging 才有效**；
- $\rho=1$ 时方差不变（平均没有意义）；
- **增加 $M$ 只能消除"独立的部分"，不能消除相关性带来的下界**——这正是 Random Forest 要**随机选特征**来降低 $\rho$ 的原因。

## 6.3 Bagging 对偏差的影响（2024-25 S2 Q3c，6 分）

- Bagging 主要**降低方差**（variance），对**偏差（bias）基本不变**；
- 因为每个基学习器仍在同一分布上训练，平均**不改变期望**：$\mathbb{E}[\bar{f}] = \mathbb{E}[f_m]$；
- 因此 bagging 对**高方差、低偏差**的模型（如深决策树）最有效；对高偏差模型（如线性回归）帮助有限。

## 6.4 ⭐ Bootstrap OOB 概率（2025-26 S2 Q3d，7 分）

**一次抽样**中，某个特定样本**不被选中**的概率：

$$
1-\frac{1}{N}
$$

**$N$ 次有放回抽样**（构成一个大小为 $N$ 的 bootstrap 集）中，它**从未被选中**的概率：

$$
\boxed{\;\left(1-\frac{1}{N}\right)^{N}
\;\xrightarrow[N\to\infty]{}\; e^{-1}\approx0.368\;}
$$

- 即约 **36.8%** 的样本不会出现在某个 bootstrap 集中；
- 若森林有 $M$ 棵树，该样本**是 OOB 的树数期望**：

$$
\mathbb{E}[\#\text{OOB trees}] = 0.368\,M
$$

**OOB error 怎么用**：

1. 对每个训练样本 $x_i$，只取**没有见过它**的树（OOB 树）做预测；
2. 平均/投票得到 $\hat{f}_{\mathrm{OOB}}(x_i)$；
3. 与真实标签比较，算误差：

$$
\mathrm{OOB\ Error} = \frac{1}{N}\sum_{i=1}^{N} L\big(y_i,\hat{f}_{\mathrm{OOB}}(x_i)\big)
$$

⭐ OOB error 相当于**内置的交叉验证**，不需要额外划分验证集。

## 6.5 Random Forest 的两大随机性（2025-26 S2 Q3c，6 分）

| 随机性 | 做法 | 作用 |
|---|---|---|
| **1. Bootstrap sampling** | 每棵树用**有放回**抽取的 $N$ 个样本训练 | 让每棵树看到不同的数据子集，**降低树间相关性 $\rho$** |
| **2. Random feature subset** | 每次**节点分裂**时，只从随机选的 $m_{try}$ 个特征中挑最优分裂 | 防止强特征主导所有树，**进一步降低 $\rho$**、增加多样性 |

- 分类常用 $m_{try}\approx\sqrt{D}$，回归常用 $m_{try}\approx D/3$；
- 两者共同作用 ⇒ $\rho$ 下降 ⇒ 由 6.2 的公式，**集成方差下降**。

> 答题金句：**Bootstrap reduces correlation by giving each tree different training data; random feature selection reduces correlation by preventing the same dominant features from being chosen at every split.**

## 6.6 答题模板

```
方差题：写 Var(平均) = 1/M^2 [ΣVar + ΣCov] → 代入 σ², ρσ² → ρσ² + (1−ρ)σ²/M
       → 讨论 M→∞ 与 ρ 的作用
OOB 题：(1−1/N)^N → e^{-1} ≈ 0.368 → 期望 OOB 树数 0.368M → OOB error 用法
RF 题：bootstrap + random feature subset → 降 ρ → 降方差
Bagging 偏差：基本不变（平均不改变期望）
```

---

# 7. 第六关 — Boosting / GBDT / XGBoost / LightGBM

> **真题**：2025-26 S2 Q4（25 分）、2024-25 S2 Q4（25 分）。**这是 Part 2 的整道大题，必须拿满。**
> **必会**：Boosting vs Bagging、加法模型、Gradient Boosting 残差、XGBoost 二阶 Taylor 推导、叶子权重、$\gamma$ 与 $\lambda$、GOSS、EFB。

## 7.1 Boosting vs Bagging

| 维度 | Bagging | Boosting |
|---|---|---|
| 训练方式 | **并行**（各基学习器独立） | **串行**（后一个修正前一个） |
| 样本权重 | 等权（bootstrap） | **自适应**（错分样本权重增大） |
| 主要作用 | **降方差** | **降偏差**（也降方差） |
| 基学习器 | 强学习器（深树） | **弱学习器**（浅树/stump） |
| 过拟合风险 | 低（平均） | 较高（需正则/早停） |

**加法模型（additive model）**：

$$
F_M(x) = \sum_{m=1}^{M}\alpha_m f_m(x)
$$

- $f_m$：第 $m$ 个弱学习器；
- $\alpha_m$：它的权重（AdaBoost 里由错误率决定）；
- $M$：学习器个数。

## 7.2 AdaBoost（自适应 boosting）

**Step 1 — 初始化样本权重**：$w_i=1/N$。

**Step 2 — 训练弱分类器 $f_m$，算加权错误率**：

$$
\varepsilon_m = \frac{\sum_i w_i\,\mathbf{1}[f_m(x_i)\ne y_i]}{\sum_i w_i}
$$

**Step 3 — 学习器权重**：

$$
\alpha_m = \frac{1}{2}\ln\frac{1-\varepsilon_m}{\varepsilon_m}
$$

**Step 4 — 更新样本权重**：

$$
w_i \leftarrow w_i\exp\!\big(-\alpha_m y_i f_m(x_i)\big)
$$

**Step 5 — 最终分类器**：

$$
F_M(x) = \operatorname{sign}\!\left(\sum_{m=1}^{M}\alpha_m f_m(x)\right)
$$

⭐ 直观：**错误率越低，$\alpha_m$ 越大；被分错的样本权重变大，下一个学习器专注它们**。

## 7.3 Gradient Boosting（梯度提升）

**核心思想**：把 boosting 看成**函数空间里的梯度下降**——每个新学习器拟合**损失函数的负梯度（伪残差）**。

$$
r_{im} = -\left[\frac{\partial L(y_i,F(x_i))}{\partial F(x_i)}\right]_{F=F_{m-1}}
$$

**平方损失** $L=\tfrac12(y-F)^2$：

$$
-\frac{\partial L}{\partial F} = y-F
\quad\Longrightarrow\quad
r_i = y_i - F_{m-1}(x_i)
$$

即**残差**。更新：

$$
F_m(x) = F_{m-1}(x) + \nu\, f_m(x)
$$

- $\nu\in(0,1]$：learning rate / shrinkage，防止过拟合。

**真题手算（2024-25 S2 Q4b(iii)）**：

$$
y=[2,3,4,5],\qquad
\hat{y}=[2.2,2.8,3.5,4.7]
$$

$$
r = y-\hat{y} = [-0.2,\ 0.2,\ 0.5,\ 0.3]
$$

**与 AdaBoost 的区别**：

- AdaBoost 用**指数损失**、通过**样本权重**修正；
- Gradient Boosting 用**任意可微损失**、通过**拟合负梯度**修正；
- AdaBoost 可看作 Gradient Boosting 在指数损失下的特例。

## 7.4 ⭐ XGBoost：正则目标与二阶 Taylor（2025-26 S2 Q4a，13 分）

### 7.4.1 正则化目标函数

第 $m$ 轮的目标：

$$
\mathcal{L}^{(m)} = \sum_{i=1}^{n} L\big(y_i,\;F_{m-1}(x_i)+f_m(x_i)\big)
+ \Omega(f_m)
$$

$$
\Omega(f) = \gamma T + \frac{1}{2}\lambda\sum_{j=1}^{T}w_j^{2}
$$

- $T$：叶子数；$w_j$：第 $j$ 个叶子的输出值；
- $\gamma$：**每增加一个叶子要付出的代价**（控制树的复杂度、剪枝）；
- $\lambda$：**叶子权重的 L2 正则**（防止权重过大）。

### 7.4.2 二阶 Taylor 展开

在 $F_{m-1}(x_i)$ 处展开：

$$
L\big(y_i,F_{m-1}+f_m(x_i)\big)
\approx L(y_i,F_{m-1}) + g_i f_m(x_i) + \frac{1}{2}h_i f_m^{2}(x_i)
$$

其中

$$
g_i = \frac{\partial L(y_i,F)}{\partial F}\bigg|_{F_{m-1}},
\qquad
h_i = \frac{\partial^{2} L(y_i,F)}{\partial F^{2}}\bigg|_{F_{m-1}}
$$

丢掉与 $f_m$ 无关的常数：

$$
\tilde{\mathcal{L}}^{(m)}
= \sum_{i=1}^{n}\left[g_i f_m(x_i) + \frac{1}{2}h_i f_m^{2}(x_i)\right]
+ \gamma T + \frac{1}{2}\lambda\sum_{j=1}^{T}w_j^{2}
$$

### 7.4.3 按叶子重组

设叶子 $j$ 的样本集合为 $I_j=\{i\mid q(x_i)=j\}$，则 $f_m(x_i)=w_j$：

$$
\tilde{\mathcal{L}}^{(m)}
= \sum_{j=1}^{T}\left[\Big(\sum_{i\in I_j}g_i\Big)w_j
+ \frac{1}{2}\Big(\sum_{i\in I_j}h_i+\lambda\Big)w_j^{2}\right]
+ \gamma T
$$

记 $G_j=\sum_{i\in I_j}g_i$，$H_j=\sum_{i\in I_j}h_i$：

$$
\tilde{\mathcal{L}}^{(m)}
= \sum_{j=1}^{T}\left[G_j w_j + \frac{1}{2}(H_j+\lambda)w_j^{2}\right] + \gamma T
$$

### 7.4.4 最优叶子权重（必背推导）

对每个 $w_j$ 求导令零：

$$
\frac{\partial \tilde{\mathcal{L}}}{\partial w_j}
= G_j + (H_j+\lambda)w_j = 0
$$

$$
\boxed{\;w_j^{*} = -\frac{G_j}{H_j+\lambda}
= -\frac{\sum_{i\in I_j}g_i}{\sum_{i\in I_j}h_i+\lambda}\;}
$$

代回得最优目标：

$$
\tilde{\mathcal{L}}^{*}
= -\frac{1}{2}\sum_{j=1}^{T}\frac{G_j^{2}}{H_j+\lambda}
+ \gamma T
$$

### 7.4.5 分裂增益（Gain）

$$
\mathrm{Gain} = \frac{1}{2}\left[
\frac{G_L^{2}}{H_L+\lambda}
+ \frac{G_R^{2}}{H_R+\lambda}
- \frac{(G_L+G_R)^{2}}{H_L+H_R+\lambda}
\right] - \gamma
$$

- 第一、二项：左右子节点的"纯度"；
- 第三项：不分裂时的"纯度"；
- $\gamma$：分裂的代价；**Gain < 0 就不分裂**（这就是 $\gamma$ 的剪枝作用）。

## 7.5 真题手算：叶子权重（两套卷）

**2025-26 S2 Q4(b)**：一个叶子有 3 个样本，$g=\{-4,-6,-8\}$，$h=\{2,2,2\}$，$\lambda=2$。

$$
G=\sum g_i = -18,\qquad
H=\sum h_i = 6
$$

$$
w^{*} = -\frac{-18}{6+2} = \frac{18}{8} = \mathbf{2.25}
$$

**2024-25 S2 Q4c(iii)**：$g_1=-2.5,\ g_2=-3.0$，$h_1=1.5,\ h_2=2.0$，$\lambda=1.2$。

$$
G=-5.5,\qquad H=3.5
$$

$$
w^{*} = -\frac{-5.5}{3.5+1.2} = \frac{5.5}{4.7} \approx \mathbf{1.170}
$$

> **易错**：分子是**负的梯度之和**，所以公式里有两个负号；$\lambda$ **只加在分母**；$h$ 是二阶导（Hessian），平方损失下 $h=1$，logistic 下 $h=p(1-p)$。

## 7.6 LightGBM

### 7.6.1 与 XGBoost 的差别

| 维度 | XGBoost | LightGBM |
|---|---|---|
| 树生长 | **level-wise**（逐层） | **leaf-wise**（每次分裂增益最大的叶子） |
| 特征分裂 | 精确贪心（遍历所有取值） | **直方图分桶**（histogram） |
| 大数据 | 较慢 | 快（内存/计算省） |
| 过拟合 | — | leaf-wise 更深，需 `max_depth`/`num_leaves` 限制 |

### 7.6.2 GOSS（Gradient-based One-Side Sampling）

**动机**：梯度小的样本已经拟合得很好，对分裂贡献小；全部保留浪费计算。

**做法**：

1. 按梯度绝对值排序，**保留 top $a\times100\%$** 的大梯度样本；
2. 从剩余小梯度样本中**随机抽 $b\times100\%$**；
3. 对被抽中的小梯度样本**乘放大系数** $\dfrac{1-a}{b}$，保持数据分布无偏。

> 记忆：**大梯度全留，小梯度抽样并放大 $(1-a)/b$**。

### 7.6.3 EFB（Exclusive Feature Bundling）

**动机**：高维稀疏数据中，很多特征**互斥**（几乎不同时非零，如 one-hot 的不同列）。

**做法**：

1. 把**互斥特征**（conflict rate 低）分到同一 bundle；
2. 用**图着色（graph coloring）**把特征分组，使同组内冲突最少；
3. 用**偏移量（offset）**把多个特征"拼接"成一个特征，不丢失信息。

> 记忆：**互斥特征打包 + 图着色 + 偏移量**，把稀疏特征数降下来。

## 7.7 答题模板

```
Q4(a)：写目标函数（损失 + γT + ½λΣw²）→ 解释每一项 → 二阶 Taylor →
      按叶子重组 → 求导 → w* = −G/(H+λ) → 代回最优值 → Gain
Q4(b)：G = Σg，H = Σh，代 w* = −G/(H+λ)，保留 2–3 位小数
Q4(c)：GOSS（top a% + 抽 b% + 放大 (1−a)/b）；EFB（互斥 + 图着色 + offset）
```

---

# 8. 公式速查表

## 8.1 Part 1

$$
g(x)=p(x)^{T}w,
\qquad
\hat{y}=Pw,
\qquad
\mathrm{SSE}=(y-Pw)^{T}(y-Pw)
$$

$$
\hat{w}=(P^{T}P)^{-1}P^{T}y
\qquad\text{(OLS)}
$$

$$
\hat{w}=(P^{T}P+\lambda I)^{-1}P^{T}y
\qquad\text{(primal ridge)}
$$

$$
K=PP^{T},\qquad
\hat{\alpha}=(K+\lambda I)^{-1}y,
\qquad
\hat{y}_t=K_t\hat{\alpha}
$$

$$
K_{ij}=k(x_i,x_j),
\qquad
(K_t)_{ij}=k(x_{ti},x_j)
$$

## 8.2 LSE / TER / $\ell_p$

$$
\mathrm{LSE}=\sum_i (y_i-g(x_i))^{2}
$$

$$
\mathrm{TER}=\mathrm{FPR}+\mathrm{FNR}
$$

$$
\|w\|_p=\left(\sum_j|w_j|^{p}\right)^{1/p}
$$

| $p$ | 形状 | 稀疏 |
|---|---|---|
| $0<p<1$ | 星形/内凹 | 强 |
| $1$ | 菱形 | 是 |
| $2$ | 圆 | 否 |
| $\infty$ | 方形 | 否 |

## 8.3 Part 2

$$
\bar{f}=\frac{1}{M}\sum_m f_m,
\qquad
\mathrm{Var}(\bar{f})=\rho\sigma^{2}+\frac{1-\rho}{M}\sigma^{2}
$$

$$
\left(1-\frac{1}{N}\right)^{N}\to e^{-1}\approx0.368
$$

$$
F_M(x)=\sum_{m=1}^{M}\alpha_m f_m(x),
\qquad
\alpha_m=\frac{1}{2}\ln\frac{1-\varepsilon_m}{\varepsilon_m}
$$

$$
r_i=-\frac{\partial L}{\partial F}\bigg|_{F_{m-1}},
\qquad
F_m=F_{m-1}+\nu f_m
$$

$$
\mathcal{L}^{(m)}=\sum_i L(y_i,F_{m-1}+f_m)+\gamma T+\frac{1}{2}\lambda\sum_j w_j^{2}
$$

$$
\tilde{\mathcal{L}}=\sum_j\left[G_jw_j+\frac{1}{2}(H_j+\lambda)w_j^{2}\right]+\gamma T
$$

$$
w_j^{*}=-\frac{G_j}{H_j+\lambda},
\qquad
\mathrm{Gain}=\frac{1}{2}\left[\frac{G_L^{2}}{H_L+\lambda}+\frac{G_R^{2}}{H_R+\lambda}-\frac{(G_L+G_R)^{2}}{H_L+H_R+\lambda}\right]-\gamma
$$

---

# 9. 模拟卷（4 题）

> 按两套真题的题型自编，建议限时 3 小时闭卷完成。

## Q1（25 分）

(a) 判断下列数据类型（Continuous Numerical / Categorical Nominal / Ordinal / Binary）：（15 分）

1. 电影评分 1–5 星（有顺序，但间距不可量化）
2. 血型 A/B/AB/O
3. 某门课是否通过（Pass/Fail）
4. 空气湿度（%）
5. 衬衫尺码 S/M/L/XL

(b) 模型 $g(x)=1+x_1^2+x_1x_2$，样本 $(1,2),(2,1),(3,3)$，写出设计矩阵 $P$。（10 分）

## Q2（25 分）

给定 $x_1=(1,1),\ x_2=(2,0)$，$y_1=1,\ y_2=2$，核 $k(x_i,x_j)=(1+x_i^{T}x_j)^2$，$\lambda=0.5$。

(a) 求训练核矩阵 $K$。（6 分）
(b) 求对偶系数 $\alpha$。（8 分）
(c) 测试点 $x_{t}=(0,1)$，求 $K_t$ 与预测值。（6 分）
(d) 说明 $K$ 与 $K_t$ 的物理意义。（5 分）

## Q3（25 分）

(a) 用 1D 数据（5 个 $+1$、5 个 $-1$）判断三个分类器的准确率并写出算式。（6 分）
(b) 填表：$q=0,1,2,4$ 的 shrinkage / sparse。（6 分）
(c) 推导 $M$ 个相关系数为 $\rho$ 的学习器平均后的方差，并讨论 $M\to\infty$。（7 分）
(d) 随机森林有 100 棵树，估计某个训练样本是 OOB 的树数期望，并说明 OOB error 的计算。（6 分）

## Q4（25 分）

(a) 写出 XGBoost 的正则目标函数，说明 $\gamma$ 与 $\lambda$ 的作用。（6 分）
(b) 从二阶 Taylor 展开推导 $w_j^{*}=-G_j/(H_j+\lambda)$。（10 分）
(c) 某叶子 $g=\{-1,-3,-5\}$，$h=\{1,1,1\}$，$\lambda=1$，求 $w^{*}$。（4 分）
(d) 简述 GOSS 与 EFB 的动机与做法。（5 分）

## 9.1 答案要点

### Q1

(a) 1. Ordinal；2. Categorical Nominal；3. Binary；4. Continuous Numerical；5. Ordinal。

(b)

$$
P=
\begin{bmatrix}
1 & 1 & 2\\
1 & 4 & 2\\
1 & 9 & 9
\end{bmatrix}
$$

### Q2

(a)

$$
K=
\begin{bmatrix}
9 & 9\\
9 & 25
\end{bmatrix}
$$

（$x_1^{T}x_1=2\Rightarrow k_{11}=(1+2)^2=9$；$x_1^{T}x_2=2\Rightarrow k_{12}=9$；$x_2^{T}x_2=4\Rightarrow k_{22}=(1+4)^2=25$。）

(b)

$$
K+0.5I=
\begin{bmatrix}
9.5 & 9\\
9 & 25.5
\end{bmatrix},
\qquad
\det=9.5\times25.5-81=161.25
$$

$$
\alpha=\frac{1}{161.25}
\begin{bmatrix}
25.5 & -9\\
-9 & 9.5
\end{bmatrix}
\begin{bmatrix}
1\\2
\end{bmatrix}
=
\begin{bmatrix}
0.0465\\0.0620
\end{bmatrix}
$$

(c) $K_t=[\,(1+1)^2,\ (1+0)^2\,]=[4,\ 1]$，

$$
\hat{y}_t = 4(0.0465)+1(0.0620)=0.186+0.062=0.248
$$

(d) $K$：训练样本两两相似度；$K_t$：测试样本与训练样本的相似度。

### Q3

(a) 写出"错 $k$ 个 / 10"的算式；例：A 错 3 个 → 70%，B 错 1 个 → 90%，C 错 0 个 → 100%。

(b) $q=0$：No / Yes；$q=1$：Yes / Yes；$q=2$：Yes / No；$q=4$：Yes / No。

(c) 见 6.2 推导；$M\to\infty$ 时趋于 $\rho\sigma^{2}$。

(d) 每棵树 OOB 概率 $(1-1/N)^N\approx0.368$；期望 $0.368\times100=36.8\approx37$ 棵；OOB error 见 6.4。

### Q4

(a) $\mathcal{L}=\sum_i L(y_i,F_{m-1}+f_m)+\gamma T+\frac12\lambda\sum_j w_j^2$；$\gamma$ 控制叶子数（剪枝），$\lambda$ 控制叶子权重幅度。

(b) 见 7.4.2–7.4.4 的推导步骤。

(c) $G=-9,\ H=3,\ \lambda=1$：

$$
w^{*}=-\frac{-9}{3+1}=2.25
$$

(d) GOSS：保留大梯度 top $a$、抽样小梯度 $b$、放大 $(1-a)/b$；EFB：互斥特征打包、图着色、偏移量。

---

# 10. 考前 2 天计划

| 时间 | 内容 | 目标 |
|---|---|---|
| 第 1 天上午 | 第 2 关 KRR：默写推导 + 重做两道真题 | 不看答案能算 $\alpha$ 与预测 |
| 第 1 天下午 | 第 3 关多项式/XOR：默写正规方程 + XOR 手算 | 10 分钟写完 Q2 |
| 第 1 天晚上 | 第 4 关 LSE/TER + $\ell_p$ + 数据类型 | 图表题不丢分 |
| 第 2 天上午 | 第 5 关 Bagging/OOB：默写方差公式与 $(1-1/N)^N$ | 推导题拿满 |
| 第 2 天下午 | 第 6 关 XGBoost：默写二阶 Taylor 与 $w^{*}$ | 25 分大题拿满 |
| 第 2 天晚上 | 第 9 节模拟卷（限时 3 小时）+ 第 8 节公式表 | 查漏补缺 |

**考场策略**：

1. **Q1 先做**（数据类型/任务匹配，20–25 分最稳）；
2. **Q2 写清矩阵维度与每一步**（过程分多）；
3. **Q3 前半看图题先定性、后半推导写公式**；
4. **Q4 先写 XGBoost 目标函数与推导框架**，再代数字；GOSS/EFB 用"动机 + 做法"两句话答；
5. 时间：每题 **40–45 分钟**，留 10 分钟检查负号与 $\lambda$。

---

> **最后提醒**：6406 的 Final **不考 Lecture 12（RL）、不考 Lecture 13（industry sharing）**；Lecture 1 只提供背景，但 **data types / ML tasks 已连续两年出现在 Q1**，必须背熟。
