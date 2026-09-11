# EE6497 Homework 1 — 题目精讲与解答整理

> 课程：IE4497/EE6497 Pattern Recognition and Deep Learning
> 来源：`HW1.pdf`（题目）+ `HW1_Solutions.pdf`（官方解答）
> 提交截止：**11 Sep 2026, 23:59**，单个 PDF，**不允许迟交（no late submission）**，占 **5%**（Homework ×2 共 10%）。
> 覆盖范围：Week 1–4 的概率建模 / Mixture Model / HMM / MLE——与 Week 4 的 HMM 内容直接对应。

---

## 题 1（10 分）— 简答三则

### (a) 由 log p(x) 反推分布

**题**：设 $\log p(x) = ax + b$（$x \ge 0$，$a < 0$）。这是什么著名的 pdf？

**解**：

$$p(x) = \exp(ax + b) = e^b e^{ax}, \quad a < 0$$

由归一化条件 $\int_0^\infty p(x)\,dx = 1$：

$$\int_0^\infty e^b e^{ax}\,dx = e^b \left(-\frac{1}{a}\right) = 1 \;\Rightarrow\; e^b = -a$$

令 $\lambda = -a > 0$，则 $b = \log \lambda$，故

$$\boxed{p(x) = \lambda e^{-\lambda x}, \quad x \ge 0}$$

即 **Exponential distribution（指数分布）**，rate $\lambda = -a$。

> 关键：$a < 0$ 保证可归一化；$e^b = -a$ 由 ∫=1 定出常数。

---

### (b) Cat 隐变量选 Exponential 分量 → mixture model

**题**：$z \sim \text{Cat}(\cdot | 0.5, 0.4, 0.1)$，条件分布 $x|z \sim \text{Exp}(x | \lambda_z)$，$\lambda_1=7.8,\ \lambda_2=0.6,\ \lambda_3=4.5$。$p(x)$ 是 mixture model 吗？写出 pdf。

**解**：**是 finite mixture model**。Categorical latent variable $z$ 选中三个 exponential 分量之一，marginalizing out $z$：

$$p(x) = 0.5\,\text{Exp}(x|7.8) + 0.4\,\text{Exp}(x|0.6) + 0.1\,\text{Exp}(x|4.5)$$

即对 $x \ge 0$：

$$\boxed{p(x) = 0.5(7.8)e^{-7.8x} + 0.4(0.6)e^{-0.6x} + 0.1(4.5)e^{-4.5x}}$$

> 这正是 Week 3 mixture model 的标准形式：$p(x) = \sum_k \pi_k p_k(x)$，这里 $p_k$ 是 Exponential 而非 Gaussian。

---

### (c) R² 能否为负？

**题**：$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$。$R^2 < 0$ 可能吗？解释。

**解**：**可能**。记 $\text{SSE} = \sum (y_i - \hat{y}_i)^2$，$\text{SST} = \sum (y_i - \bar{y})^2$，则

$$R^2 = 1 - \text{SSE}/\text{SST}, \qquad R^2 < 0 \iff \text{SSE} > \text{SST}$$

含义：模型的平方误差**比常数基线 $\hat{y}_i = \bar{y}$ 还差**。可能发生于：
- 模型拟合很差（poorly fitted）；
- 拟合时未含 intercept（截距项）；
- 在**与训练数据不同的数据上评估**（evaluation on data different from fitting）。

> 注：普通最小二乘（OLS）在**训练数据上**且含 intercept 时，$R^2$ 不会为负。

---

## 题 2（25 分）— HMM：Joint / Likelihood / MLE / Baum-Welch

设定：state space $\mathcal{Z} = \{s_1, s_2\}$，emission symbols $\{o_1, o_2\}$。

- 初始概率 $\pi(s_1) = \pi(s_2) = 1/2$。
- 转移矩阵 $T = \begin{pmatrix} a & 1-a \\ 1-b & b \end{pmatrix}$（行 $s_1, s_2$，列 $s_1, s_2$）。
- emission：$p(o_1|s_1)=p,\ p(o_2|s_1)=1-p;\ p(o_1|s_2)=q,\ p(o_2|s_2)=1-q$。

> 区分两种模型：**HMM**（只观察 emission $x$，state $z$ 隐）vs **标准 Markov model with emissions**（$z, x$ 都观察）。

### (a)(i) 标准模型下 $L=2$、$x=(o_2, o_1)$ 的联合概率

HMM 因子分解：

$$p(z[1], z[2], x[1], x[2]) = \pi(z[1])\,p(x[1]|z[1])\,T_{z[1],z[2]}\,p(x[2]|z[2])$$

对 $x[1]=o_2, x[2]=o_1$，四条 state path 的联合概率：

| $z[1]$ | $z[2]$ | $p(z[1],z[2],o_2,o_1)$ |
|---|---|---|
| $s_1$ | $s_1$ | $\frac{1}{2}(1-p)\,a\,p$ |
| $s_1$ | $s_2$ | $\frac{1}{2}(1-p)(1-a)\,q$ |
| $s_2$ | $s_1$ | $\frac{1}{2}(1-q)(1-b)\,p$ |
| $s_2$ | $s_2$ | $\frac{1}{2}(1-q)\,b\,q$ |

> $o_2$ ⇒ 用 $1-p$（$s_1$）或 $1-q$（$s_2$）；$o_1$ ⇒ 用 $p$ 或 $q$。

---

### (a)(ii) HMM 下 emission sequence 的 likelihood

只有 emission 可见时，对所有 state path 求和（marginalize $z$）：

$$p(o_2, o_1) = \sum_{z[1],z[2]} p(z[1], z[2], o_2, o_1)$$

$$\boxed{p(o_2, o_1) = \frac{1}{2}\Big[(1-p)\{ap + (1-a)q\} + (1-q)\{(1-b)p + bq\}\Big]}$$

> 这正是 forward algorithm 的 $L=2$ 手算版：$\alpha_2(o_1) = \sum_{z[2]} \big(\sum_{z[1]} \alpha_1(z[1]) T_{z[1],z[2]}\big) p(o_1|z[2])$。

---

### (b)(i) 标准模型（states 已观察）下 $a, b$ 的 MLE

四条独立序列的 transition counts：

$$N_{11}=1,\quad N_{12}=1,\quad N_{21}=0,\quad N_{22}=2$$

（$N_{ij}$ = $s_i \to s_j$ 的次数。）已知的 emission 概率 $p, q$ 与固定初始概率不参与 $a, b$ 的优化，故

$$L(a,b) \propto a^{N_{11}} (1-a)^{N_{12}} (1-b)^{N_{21}} b^{N_{22}} = a(1-a)b^2$$

每个 transition probability 由观察到的相对频率估计：

$$\boxed{\hat{a}_{\text{MLE}} = \frac{N_{11}}{N_{11}+N_{12}} = \frac{1}{2}, \qquad \hat{b}_{\text{MLE}} = \frac{N_{22}}{N_{21}+N_{22}} = 1}$$

> states 可见 ⇒ MLE 就是计数比（complete data 的闭式 MLE）。

---

### (b)(ii) HMM（states 隐）下单条 emission 序列的 MLE

记 $\Delta = p - q \ne 0$。由 (a)(ii)：

$$L(a,b) = \frac{1}{2}\Big[(1-p)(q + a\Delta) + (1-q)(p - b\Delta)\Big]$$

这是 $a, b$ 的**仿射函数（affine）**，故最大值在边界 $a, b \in [0,1]$ 取得：

- **若 $p > q$**（$\Delta > 0$）：$a$ 的系数为正、$b$ 的系数为负 ⇒
  $$\boxed{\hat{a}_{\text{MLE}} = 1,\quad \hat{b}_{\text{MLE}} = 0}$$
- **若 $p < q$**（$\Delta < 0$）：$a$ 的系数为负、$b$ 的系数为正 ⇒
  $$\boxed{\hat{a}_{\text{MLE}} = 0,\quad \hat{b}_{\text{MLE}} = 1}$$

> 在 $0 < p, q < 1$ 非退化条件下唯一。若 $p=1$（$>q$）则 likelihood 与 $a$ 无关（$a$ 不可识别）；若 $q=1$（$>p$）则与 $b$ 无关。
> 直觉：HMM 把不确定性 marginalize 掉后，likelihood 对转移参数变仿射 ⇒ 极值在边界，与 complete-data 的内部解完全不同。

---

### (c) 5 条长度 $L=20$ 的 emission 序列 ⇒ 用 Baum-Welch

**算法**：**Baum–Welch algorithm**（HMM 专用 EM）。

理由：latent state paths 未观察，枚举每条序列的 $2^{20}$ 条 path 不必要。每次 EM 迭代：

1. **E-step**：对每条序列跑 **forward–backward algorithm**，计算后验期望转移计数 $\mathbb{E}[N_{11}], \mathbb{E}[N_{12}], \mathbb{E}[N_{21}], \mathbb{E}[N_{22}]$，并在 5 条序列上求和。
2. **M-step**：归一化期望计数：
   $$a_{\text{new}} = \frac{\mathbb{E}[N_{11}]}{\mathbb{E}[N_{11}]+\mathbb{E}[N_{12}]}, \qquad b_{\text{new}} = \frac{\mathbb{E}[N_{22}]}{\mathbb{E}[N_{21}]+\mathbb{E}[N_{22}]}$$
3. 重复至 data log-likelihood 收敛。

> forward–backward 以序列长度的线性时间算出所需后验量；每次 EM 迭代不降低 observed-data likelihood。因 EM 可能收敛到 local optimum，可尝试多个 $(a,b)$ 初值取最大 likelihood 的解。
> 这正是 Week 4 HMM 三大问题中的 **Learning 问题** ⇒ Baum-Welch（EM for HMM），把 complete-data MLE 的硬计数 $N_{ij}$ 换成软期望 $\mathbb{E}[N_{ij}]$。

---

## 题 3（15 分，EE6497 必做 / IE4497 bonus）— 设备失效时间的 MLE

设定：失效时间 $x \in \{1, 2, \dots, r, r+1\}$，pmf 为

$$p(x=k|\theta) = \theta^{k-1}(1-\theta),\ k=1,\dots,r; \qquad p(x=r+1|\theta) = \theta^r$$

其中 $0 < \theta \le 1$。$n$ 个独立观测 $x_1,\dots,x_n$，$n_k$ = 取值 $k$ 的个数。

> 这是一种**截断 Geometric**：$x \le r$ 为"第 $k$ 次成功前未失败"的概率，$x=r+1$ 表示"前 $r$ 次都未失效"（存活过 $r$ 期）。

### (a) Log-likelihood

独立性 ⇒

$$L(\theta) = \prod_{k=1}^{r} \big[\theta^{k-1}(1-\theta)\big]^{n_k} \cdot (\theta^r)^{n_{r+1}} = \theta^{\sum_{k=1}^{r}(k-1)n_k + r n_{r+1}} (1-\theta)^{\sum_{k=1}^{r} n_k}$$

故

$$\ell(\theta) = \Big[\sum_{k=1}^{r}(k-1)n_k + r n_{r+1}\Big]\log\theta + \Big[\sum_{k=1}^{r} n_k\Big]\log(1-\theta)$$

利用 $\sum_{k=1}^{r+1} n_k = n$，可紧凑写成

$$\boxed{\ell(\theta) = \Big[\sum_{k=1}^{r+1} k\,n_k - n\Big]\log\theta + (n - n_{r+1})\log(1-\theta)}$$

> 注意 $x=r+1$ 的概率是 $\theta^r$（无 $(1-\theta)$ 因子），与 $k \le r$ 不同——这是本题关键陷阱。

---

### (b) MLE of $\theta$

令 $A = \sum_{k=1}^{r+1} k\,n_k - n$，$B = n - n_{r+1}$。内部解由 $\frac{d\ell}{d\theta} = \frac{A}{\theta} - \frac{B}{1-\theta} = 0$：

$$A(1-\theta) = B\theta \;\Rightarrow\; \theta = \frac{A}{A+B}$$

二阶导 $\frac{d^2\ell}{d\theta^2} = -\frac{A}{\theta^2} - \frac{B}{(1-\theta)^2} < 0$（$A, B > 0$ 时），故为唯一最大值。又

$$A + B = \Big[\sum_{k=1}^{r+1} k\,n_k - n\Big] + (n - n_{r+1}) = \sum_{k=1}^{r+1} k\,n_k - n_{r+1}$$

故

$$\boxed{\hat{\theta}_{\text{MLE}} = \frac{\sum_{k=1}^{r+1} k\,n_k - n}{\sum_{k=1}^{r+1} k\,n_k - n_{r+1}}}$$

**边界情形**：若所有观测都 $= r+1$，公式给 $\hat\theta = 1$；若都 $= 1$，给 $0$（在 $\theta > 0$ 严格条件下是 $\theta \downarrow 0$ 的上确界而非达到的 MLE）。

---

## 与课程内容的对应

| HW1 题 | 对应 Week | 课程知识点 |
|---|---|---|
| 1(a) Exponential 推导 | Week 1–2 | 常见分布、归一化求常数 |
| 1(b) Mixture of Exponentials | Week 3 | Mixture model $p(x)=\sum\pi_k p_k(x)$、latent variable |
| 1(c) R² < 0 | Week 1–2 | 回归评估、SSE vs SST |
| 2(a)(i) HMM joint | Week 4 | HMM 因子分解 $\pi \cdot T \cdot p(x|z)$ |
| 2(a)(ii) HMM likelihood | Week 4 | Forward / marginalize $z$ |
| 2(b)(i) Complete-data MLE | Week 3–4 | 计数比 = complete-data MLE |
| 2(b)(ii) HMM boundary MLE | Week 4 | incomplete data ⇒ likelihood 仿射 ⇒ 边界解 |
| 2(c) Baum-Welch | Week 4 | HMM Learning 问题 = EM（E: forward-backward，M: 归一化期望计数） |
| 3 Geometric MLE | Week 1–3 | MLE 求导、log-likelihood、二阶条件、边界 |

> HW1 是 Week 1–4 的综合练习，核心在 **MLE（complete vs incomplete data）** 与 **HMM（forward/Baum-Welch）**——与 Week 7 Quiz（覆盖 Week 1–4）高度重合，可作为 Quiz 复习的主线练习。
