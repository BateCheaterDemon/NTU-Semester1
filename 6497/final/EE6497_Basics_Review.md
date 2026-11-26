# EE6497 Pattern Recognition and Deep Learning — 基础知识复习

> **定位**：这份资料只讲 **Week 1–13 的基础概念、公式与直觉**，不押题、不练真题；适合在刷往年卷之前先把框架搭起来。配合 `EE6497_Final_Review.pdf`（真题题型版）使用。
>
> **课程两条主线**：
>
> - **Part 1（Week 1–7，Tay Wee Peng）**：概率 → MLE/MAP → EM → HMM → Sampling → MCMC——**从数据推断参数/隐变量**；
> - **Part 2（Week 8–13，Wang Lipo）**：神经元 → MLP/forward → 训练/正则化 → CNN——**从数据学习函数**。

---

## 目录

**Part A — 概率、推断与采样（Week 1–7）**

1. 概率论基础
2. 常见概率分布
3. Maximum Likelihood Estimation（MLE）
4. Bayesian Inference 与 MAP
5. Mixture Models 与 EM
6. Markov Chains 与 HMM
7. Sampling（采样）
8. MCMC（马尔可夫链蒙特卡洛）

**Part B — 神经网络与深度学习（Week 8–13）**

9. 从生物神经元到人工神经元
10. 感知机与线性可分性
11. MLP 与前向传播
12. Loss 函数与 Softmax
13. Backpropagation（反向传播）
14. 优化与训练技巧
15. 正则化
16. Convolutional Neural Networks（CNN）
17. ReLU 网络的性质
18. 公式表
19. 基础自测 20 题＋答案

---

# Part A — 概率、推断与采样

# 1. 概率论基础

## 1.1 随机变量与分布

| 概念 | 离散（PMF） | 连续（PDF） |
|---|---|---|
| 概率 | $P(X=x)=p(x)$ | $P(a\le X\le b)=\int_a^b p(x)\,dx$ |
| 归一化 | $\sum_x p(x)=1$ | $\int p(x)\,dx=1$ |
| 期望 | $\mathbb E[X]=\sum_x x\,p(x)$ | $\mathbb E[X]=\int x\,p(x)\,dx$ |
| 方差 | $\mathrm{Var}(X)=\mathbb E[(X-\mathbb E X)^2]$ | 同左 |

**方差展开**：

$$
\mathrm{Var}(X)=\mathbb E[X^2]-(\mathbb E[X])^2
$$

**协方差**：

$$
\mathrm{Cov}(X,Y)=\mathbb E[(X-\mathbb E X)(Y-\mathbb E Y)]
=\mathbb E[XY]-\mathbb E X\,\mathbb E Y
$$

- $X,Y$ 独立 ⇒ $\mathrm{Cov}(X,Y)=0$（反之不成立）；
- $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$；
- $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y)$。

## 1.2 条件概率与 Bayes 公式

$$
P(A\mid B)=\frac{P(A,B)}{P(B)}
$$

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
$$

**全概率公式**：

$$
P(B)=\sum_i P(B\mid A_i)P(A_i)
$$

**独立**：

$$
P(A,B)=P(A)P(B)
\quad\Longleftrightarrow\quad
P(A\mid B)=P(A)
$$

## 1.3 从联合到边缘与条件

$$
p(x)=\int p(x,y)\,dy
\qquad\text{(marginal)}
$$

$$
p(y\mid x)=\frac{p(x,y)}{p(x)}
\qquad\text{(conditional)}
$$

**链式法则**：

$$
p(x_1,\dots,x_n)=p(x_1)p(x_2\mid x_1)\cdots p(x_n\mid x_1,\dots,x_{n-1})
$$

## 1.4 期望的线性性与条件期望

$$
\mathbb E[aX+bY]=a\mathbb E[X]+b\mathbb E[Y]
$$

**全期望公式**：

$$
\mathbb E[X]=\mathbb E\big[\mathbb E[X\mid Y]\big]
$$

**全方差公式**：

$$
\mathrm{Var}(X)=\mathbb E[\mathrm{Var}(X\mid Y)]+\mathrm{Var}(\mathbb E[X\mid Y])
$$

⭐ 这两个式子是 EM、HMM、贝叶斯推断的底层工具。

---

# 2. 常见概率分布

| 分布 | 参数 | PMF/PDF | 用途 |
|---|---|---|---|
| **Bernoulli** | $\theta$ | $p(x)=\theta^x(1-\theta)^{1-x},\ x\in\{0,1\}$ | 二分类、抛硬币 |
| **Binomial** | $n,\theta$ | $p(x)=\binom nx\theta^x(1-\theta)^{n-x}$ | $n$ 次试验成功数 |
| **Categorical** | $\theta_1,\dots,\theta_K$ | $p(x=k)=\theta_k$ | 多分类 |
| **Multinomial** | $n,\theta$ | $\frac{n!}{x_1!\cdots x_K!}\prod_k\theta_k^{x_k}$ | 词频、计数 |
| **Gaussian** | $\mu,\sigma^2$ | $\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | 连续噪声、特征 |
| **Multivariate Gaussian** | $\mu,\Sigma$ | $\frac{1}{(2\pi)^{d/2}\lvert\Sigma\rvert^{1/2}}e^{-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)}$ | 多维特征 |
| **Beta** | $a,b$ | $\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\theta^{a-1}(1-\theta)^{b-1}$ | **Bernoulli 的共轭先验** |
| **Dirichlet** | $\alpha$ | $\frac{\Gamma(\sum\alpha_k)}{\prod\Gamma(\alpha_k)}\prod_k\theta_k^{\alpha_k-1}$ | **Categorical 的共轭先验** |
| **Uniform** | $a,b$ | $\frac{1}{b-a}$ | 无信息先验、proposal |
| **Exponential** | $\lambda$ | $\lambda e^{-\lambda x},\ x\ge0$ | 等待时间、非负误差 |

**Gaussian 的性质**：

$$
X\sim\mathcal N(\mu,\sigma^2)
\Longrightarrow
aX+b\sim\mathcal N(a\mu+b,a^2\sigma^2)
$$

独立高斯之和仍是高斯。

**Beta 的形状**：

- $a=b=1$ ⇒ Uniform；
- $a,b>1$ ⇒ 单峰；
- $a<1$ 或 $b<1$ ⇒ 在 0/1 附近发散。

⭐ **为什么 Beta 是 Bernoulli 的共轭先验**：Beta prior × Bernoulli likelihood ⇒ 后验仍是 Beta，只是参数变成 $a+r,\ b+n-r$。

---

# 3. Maximum Likelihood Estimation（MLE）

## 3.1 定义

给定 i.i.d. 数据 $x_1,\dots,x_n$ 和参数化分布 $p(x\mid\theta)$：

$$
L(\theta)=\prod_{i=1}^{n}p(x_i\mid\theta)
$$

$$
\ell(\theta)=\ln L(\theta)=\sum_{i=1}^{n}\ln p(x_i\mid\theta)
$$

$$
\boxed{\;\hat\theta_{\mathrm{MLE}}=\arg\max_\theta \ell(\theta)\;}
$$

⭐ 取 log 的理由：乘积变求和、数值更稳、单调变换不改变 argmax。

## 3.2 三个基本例子

### 3.2.1 Bernoulli

$$
\ell(\theta)=r\ln\theta+(n-r)\ln(1-\theta),
\qquad r=\sum_i x_i
$$

$$
\frac{d\ell}{d\theta}=\frac r\theta-\frac{n-r}{1-\theta}=0
\Longrightarrow
\hat\theta=\frac rn
$$

### 3.2.2 Gaussian

$$
\ell(\mu,\sigma^2)=-\frac n2\ln(2\pi\sigma^2)-\frac{1}{2\sigma^2}\sum_i(x_i-\mu)^2
$$

$$
\hat\mu=\bar x,
\qquad
\hat\sigma^2=\frac1n\sum_i(x_i-\bar x)^2
$$

（注意：MLE 的方差是**有偏**的，除以 $n$；无偏估计除以 $n-1$。）

### 3.2.3 Exponential

$$
\ell(\lambda)=n\ln\lambda-\lambda\sum_i x_i
\Longrightarrow
\hat\lambda=\frac{n}{\sum_i x_i}=\frac1{\bar x}
$$

## 3.3 MLE 的性质

| 性质 | 说明 |
|---|---|
| **一致性** | $n\to\infty$ 时收敛到真值 |
| **渐近正态** | $\hat\theta\approx\mathcal N(\theta,I^{-1}(\theta))$，$I$ 为 Fisher information |
| **渐近有效** | 达到 Cramér–Rao 下界 |
| **不一定无偏** | 有限样本可能有偏（如 $\hat\sigma^2$） |
| **参数变换不变** | 若 $\hat\theta$ 是 MLE，则 $g(\hat\theta)$ 是 $g(\theta)$ 的 MLE |

## 3.4 什么时候 MLE 会失效

- 模型不可识别（不同参数给同一分布）；
- 参数在边界（如 $\theta=0$）；
- 样本太少 / 完全分离（logistic regression 的 MLE 不存在）；
- 隐变量导致 likelihood 不可解（→ EM）。

---

# 4. Bayesian Inference 与 MAP

## 4.1 贝叶斯视角

把参数 $\theta$ 也看成随机变量：

```
prior p(θ)  +  likelihood p(D|θ)  →  posterior p(θ|D)
```

$$
p(\theta\mid D)=\frac{p(D\mid\theta)p(\theta)}{p(D)}
\propto p(D\mid\theta)p(\theta)
$$

- **prior**：看数据前的信念；
- **posterior**：看完数据后的信念；
- **evidence** $p(D)$：归一化常数。

## 4.2 MAP 估计

$$
\boxed{\;\hat\theta_{\mathrm{MAP}}
=\arg\max_\theta\big[\ln p(D\mid\theta)+\ln p(\theta)\big]\;}
$$

⭐ **MAP = MLE + 先验正则**；uniform prior 时 MAP = MLE。

## 4.3 共轭先验

| Likelihood | Prior | Posterior | MAP |
|---|---|---|---|
| Bernoulli | Beta$(a,b)$ | Beta$(a+r,b+n-r)$ | $\frac{r+a-1}{n+a+b-2}$ |
| Categorical | Dirichlet$(\alpha)$ | Dirichlet$(\alpha+n)$ | $\frac{n_k+\alpha_k-1}{N+\sum\alpha-2}$ |
| Gaussian（已知 $\sigma^2$） | Gaussian | Gaussian | 先验均值与数据均值的加权 |
| Exponential | Gamma$(\alpha,\beta)$ | Gamma | $\frac{n+\alpha-1}{\sum x_i+\beta}$ |

**Beta-Bernoulli 推导**：

$$
p(\theta\mid D)\propto\theta^{r}(1-\theta)^{n-r}\cdot\theta^{a-1}(1-\theta)^{b-1}
=\theta^{r+a-1}(1-\theta)^{n-r+b-1}
$$

⇒ Beta$(r+a,\ n-r+b)$。

## 4.4 MLE vs MAP

| 维度 | MLE | MAP |
|---|---|---|
| 先验 | 无 | 有 |
| 目标 | likelihood | posterior |
| 小样本 | 容易过拟合 | 先验起正则作用 |
| 大样本 | 两者趋同 | 先验影响消失 |
| 例子 | $\hat\theta=r/n$ | $\frac{r+a-1}{n+a+b-2}$ |

## 4.5 贝叶斯预测

对新样本 $x_{\mathrm{new}}$：

$$
p(x_{\mathrm{new}}\mid D)=\int p(x_{\mathrm{new}}\mid\theta)p(\theta\mid D)\,d\theta
$$

- 这是**对参数不确定性的积分**；
- 与 MAP 的"点估计代入"不同。

---

# 5. Mixture Models 与 EM

## 5.1 混合模型

$$
p(x\mid\theta)=\sum_{k=1}^{K}\pi_k\,p_k(x\mid\theta_k),
\qquad
\sum_k\pi_k=1
$$

- $K$ 个 component；
- $\pi_k$：mixing coefficient；
- 隐变量 $z\in\{1,\dots,K\}$ 表示"来自哪个 component"。

**GMM**：

$$
p(x)=\sum_k\pi_k\,\mathcal N(x\mid\mu_k,\Sigma_k)
$$

## 5.2 为什么不能直接 MLE

$$
\ell(\theta)=\sum_i\ln\left(\sum_k\pi_k p_k(x_i\mid\theta_k)\right)
$$

**log 里套 sum** ⇒ 求导后仍然耦合，一般没有闭式解。

## 5.3 EM 算法

**核心思想**：引入隐变量 $z$，先"猜" $z$ 的分布（E），再更新参数（M），交替直到收敛。

**E-step**：

$$
Q(\theta\mid\theta^{(t)})
=\mathbb E_{z\mid x,\theta^{(t)}}\big[\ln p(x,z\mid\theta)\big]
$$

**M-step**：

$$
\theta^{(t+1)}=\arg\max_\theta Q(\theta\mid\theta^{(t)})
$$

**性质**：每轮 log-likelihood **单调不降**：

$$
\ell(\theta^{(t+1)})\ge\ell(\theta^{(t)})
$$

## 5.4 GMM 的 EM（闭式）

**E-step**：

$$
r_{ik}=\frac{\pi_k\mathcal N(x_i\mid\mu_k,\Sigma_k)}
{\sum_j\pi_j\mathcal N(x_i\mid\mu_j,\Sigma_j)}
$$

**M-step**：

$$
\pi_k=\frac{1}{n}\sum_i r_{ik},
\qquad
\mu_k=\frac{\sum_i r_{ik}x_i}{\sum_i r_{ik}}
$$

$$
\Sigma_k=\frac{\sum_i r_{ik}(x_i-\mu_k)(x_i-\mu_k)^T}{\sum_i r_{ik}}
$$

⭐ $r_{ik}$ 可理解为"样本 $i$ 属于第 $k$ 个高斯的分担比例"。

## 5.5 K-means = 硬 EM

| 方法 | K-means | GMM-EM |
|---|---|---|
| 隐变量 | 硬分配（0/1） | 软分配（$r_{ik}\in[0,1]$） |
| 协方差 | 球形、相同 | 各自 $\Sigma_k$ |
| M-step | 取均值 | 加权均值 + 协方差 |
| 目标 | 最小化 WCSS | 最大化 likelihood |

## 5.6 EM 的局限

- 只保证**局部最优**（依赖初始化）；
- 收敛速度可能慢；
- GMM 的 likelihood 有无界问题（某 component 塌缩到一个点）⇒ 可用 MAP/正则。

---

# 6. Markov Chains 与 HMM

## 6.1 Markov Chain

**Markov property**：

$$
p(z_t\mid z_1,\dots,z_{t-1})=p(z_t\mid z_{t-1})
$$

**转移矩阵** $T(i,j)=p(z_{t+1}=s_j\mid z_t=s_i)$，每行和为 1。

**联合分布**：

$$
p(z_1,\dots,z_L)=\pi(z_1)\prod_{t=2}^{L}T(z_{t-1},z_t)
$$

**平稳分布**：

$$
\pi=T^T\pi
$$

## 6.2 HMM

- 状态 $z_t$ 不可见；
- 观测 $x_t$ 由 $z_t$ 通过 emission 生成；
- 联合：

$$
p(z_{1:L},x_{1:L})
=\pi(z_1)p(x_1\mid z_1)
\prod_{t=2}^{L}T(z_{t-1},z_t)p(x_t\mid z_t)
$$

## 6.3 HMM 三大问题

| 问题 | 算法 |
|---|---|
| **Evaluation**：$p(x_{1:L})$ | Forward algorithm |
| **Decoding**：最可能状态序列 | Viterbi |
| **Learning**：估参数 | Baum-Welch（EM） |

## 6.4 Forward / Backward

**Forward**：

$$
\alpha_t(j)=p(x_{1:t},z_t=s_j)
=p(x_t\mid s_j)\sum_i\alpha_{t-1}(i)T(i,j)
$$

**Backward**：

$$
\beta_t(i)=p(x_{t+1:L}\mid z_t=s_i)
=\sum_jT(i,j)p(x_{t+1}\mid s_j)\beta_{t+1}(j)
$$

$$
p(x_{1:L})=\sum_i\alpha_L(i)
$$

## 6.5 Baum-Welch

$$
\gamma_t(i)=p(z_t=s_i\mid x)
=\frac{\alpha_t(i)\beta_t(i)}{\sum_j\alpha_t(j)\beta_t(j)}
$$

$$
\xi_t(i,j)=p(z_t=s_i,z_{t+1}=s_j\mid x)
\propto\alpha_t(i)T(i,j)p(x_{t+1}\mid s_j)\beta_{t+1}(j)
$$

**更新**：

$$
\pi_i=\gamma_1(i),
\qquad
T_{ij}=\frac{\sum_{t=1}^{L-1}\xi_t(i,j)}{\sum_{t=1}^{L-1}\gamma_t(i)}
$$

$$
b_i(o)=\frac{\sum_{t:x_t=o}\gamma_t(i)}{\sum_{t=1}^{L}\gamma_t(i)}
$$

## 6.6 Viterbi

$$
\delta_1(i)=\pi_i p(x_1\mid s_i)
$$

$$
\delta_t(j)=\max_i\big[\delta_{t-1}(i)T(i,j)\big]p(x_t\mid s_j)
$$

回溯得到最优路径。

---

# 7. Sampling（采样）

## 7.1 为什么需要采样

- 求期望/积分：$\mathbb E_p[f]=\int f(x)p(x)dx$；
- 高维时数值积分不可行；
- 从 $p$ 采样后用样本平均近似。

**大数定律**：

$$
\frac1n\sum_i f(x_i)\to\mathbb E_p[f]
$$

## 7.2 逆 CDF 法

若 $U\sim\mathrm{Unif}(0,1)$，$x=F^{-1}(u)$，则 $x\sim F$。

- 需要 $F$ 可解析求逆；
- 例：Exponential $F(x)=1-e^{-\lambda x}$ ⇒ $x=-\frac1\lambda\ln(1-u)$。

## 7.3 变量变换法

若 $y=g(x)$ 单调，则

$$
p_Y(y)=p_X(x)\left|\frac{dx}{dy}\right|
$$

## 7.4 Rejection Sampling

目标 $p(x)=\tilde p(x)/Z$，proposal $q$，常数 $M$ 满足 $\tilde p(x)\le Mq(x)$。

```
repeat:
  x ~ q(x)
  u ~ Unif(0,1)
  if u <= p̃(x)/(M q(x)): accept x
```

**接受概率**：

$$
P(\text{accept})=\int \frac{\tilde p(x)}{Mq(x)}q(x)dx=\frac1M
$$

- $M$ 越小效率越高；
- proposal 的 support 必须覆盖 target。

## 7.5 Importance Sampling

$$
\mathbb E_p[f]=\mathbb E_q\left[\frac{p(x)}{q(x)}f(x)\right]
\approx\frac1n\sum_i\frac{p(x_i)}{q(x_i)}f(x_i)
$$

自归一化版本：

$$
w_i=\frac{\tilde p(x_i)/q(x_i)}{\sum_j\tilde p(x_j)/q(x_j)}
$$

- 用加权平均代替直接平均；
- $q$ 与 $p$ 越接近，方差越小。

## 7.6 SIR（Sampling Importance Resampling）

1. 从 $q$ 采样 $z_1,\dots,z_n$；
2. 算权重 $w_i$；
3. 按权重**有放回重采样**。

⭐ 得到的是**近似来自 $p$ 的样本**（带权重）。

---

# 8. MCMC

## 8.1 动机

高维 posterior 无法直接采样；构造一条**马尔可夫链**，使其 stationary distribution 就是目标 $p$。

## 8.2 Markov Chain 的收敛

- 不可约 + 非周期 + 正常返 ⇒ 收敛到唯一 stationary distribution；
- **detailed balance（细致平衡）**：

$$
\pi(x)T(x,y)=\pi(y)T(y,x)
$$

⇒ $\pi$ 是 stationary distribution。

## 8.3 Metropolis-Hastings

```
初始化 x
for t = 1..T:
  y ~ q(y|x)                  # proposal
  A = min(1, π(y)q(x|y) / (π(x)q(y|x)))
  u ~ Unif(0,1)
  if u < A: x = y
  记录 x
```

- 只需**未归一化**的 $\tilde\pi$；
- 对称 proposal 时 $q$ 项消掉；
- 接受率过低 ⇒ 链移动慢；过高 ⇒ 可能乱跳。

## 8.4 Gibbs Sampling

- 对每个变量，从**全条件** $p(z_i\mid z_{-i},x)$ 采样；
- 总是接受；
- 是 MH 的特例（proposal 取全条件）。

## 8.5 Burn-in 与 Thinning

| 概念 | 作用 |
|---|---|
| **Burn-in** | 丢弃链初期未收敛的样本 |
| **Thinning** | 每隔 $k$ 步取一个，降低自相关 |

## 8.6 应用：Ising 模型图像去噪

- 像素 $z_i\in\{-1,+1\}$；
- 先验鼓励邻居一致：$p(z)\propto\exp(J\sum_{i\sim j}z_iz_j)$；
- 似然：观测 $y_i$ 是 $z_i$ 加噪声；
- 用 Gibbs 逐个像素更新：

$$
p(z_i\mid z_{-i},y)\propto p(y_i\mid z_i)\prod_{j\in N_i}\psi(z_i,z_j)
$$

---

# Part B — 神经网络与深度学习

# 9. 从生物神经元到人工神经元

## 9.1 人工神经元

$$
y=f\left(\sum_i w_ix_i+b\right)=f(w^Tx+b)
$$

- $w$：权重；$b$：bias；$f$：activation；
- 线性部分 $w^Tx+b$ 决定"证据"，$f$ 决定"是否激活"。

## 9.2 常见激活函数

| 激活 | 公式 | 特点 |
|---|---|---|
| **Sigmoid** | $\sigma(z)=\frac{1}{1+e^{-z}}$ | 输出 $(0,1)$；两端饱和、梯度消失 |
| **Tanh** | $\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}$ | 输出 $(-1,1)$；零中心 |
| **ReLU** | $\max(0,z)$ | 计算简单、缓解梯度消失；可能 dead |
| **Leaky ReLU** | $\max(0.01z,z)$ | 负半轴有斜率，缓解 dead |
| **Softmax** | $\frac{e^{z_k}}{\sum_j e^{z_j}}$ | 多分类输出概率 |

⭐ 非线性激活是**多层网络表达能力**的来源；全是线性 ⇒ 等价单层。

---

# 10. 感知机与线性可分性

## 10.1 单层感知机

$$
y=\begin{cases}1,&w^Tx+b>0\\0,&w^Tx+b\le0\end{cases}
$$

- 决策边界 $w^Tx+b=0$ 是**超平面**；
- $w$ 决定方向，$b$ 决定位置。

## 10.2 线性可分与 XOR

- 单层感知机只能解决**线性可分**问题；
- XOR 不是线性可分 ⇒ 单层做不到；
- 多层（至少一个隐藏层）可以。

**XOR 的经典构造**：两个隐藏神经元做 AND，输出做 OR。

## 10.3 Universal Approximation

含足够多隐藏神经元的一层网络，可以以任意精度逼近**紧集上的连续函数**。

- 但"存在性"不等于"容易训练"；
- 深层网络用更少参数表达复杂函数（层次化特征）。

---

# 11. MLP 与前向传播

## 11.1 结构

```
输入层 → 隐藏层 1 → ... → 隐藏层 L → 输出层
```

每层：

$$
h^{(l)}=f\left(W^{(l)T}h^{(l-1)}+b^{(l)}\right)
$$

## 11.2 参数量

$$
\text{params}=(n_{in}+1)\times n_{out}
$$

**例**：$784\to256\to10$：

$$
(784+1)\times256+(256+1)\times10
=200960+2570=203530
$$

## 11.3 输出层

- 回归：线性输出；
- 二分类：sigmoid + BCE；
- 多分类：softmax + CE。

---

# 12. Loss 函数与 Softmax

## 12.1 MSE

$$
L=\frac1n\sum_i(y_i-\hat y_i)^2
$$

## 12.2 Cross-Entropy

**二分类（BCE）**：

$$
L=-\big[y\ln\hat y+(1-y)\ln(1-\hat y)\big]
$$

**多分类（CE）**：

$$
L=-\sum_k y_k\ln p_k
$$

one-hot 时只剩正确类：$L=-\ln p_{y}$。

## 12.3 Softmax + CE 的梯度

$$
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
$$

$$
\frac{\partial L}{\partial z_k}=p_k-y_k
$$

⭐ 这个简洁的梯度是 softmax + CE 组合被广泛使用的原因。

## 12.4 为什么分类不用 MSE

- MSE 对错误概率的惩罚是"平方"，梯度在饱和区很小；
- CE 的梯度与误差成正比，收敛更快；
- CE 等价于 Bernoulli/Categorical 的 MLE。

---

# 13. Backpropagation

## 13.1 链式法则

$$
\frac{\partial L}{\partial w}=\frac{\partial L}{\partial y}\cdot\frac{\partial y}{\partial z}\cdot\frac{\partial z}{\partial w}
$$

## 13.2 输出层（平方损失 + 线性输出）

$$
z=w^Tx+b,\quad \hat y=z,\quad L=\frac12(y-\hat y)^2
$$

$$
\frac{\partial L}{\partial z}=-(y-\hat y)
$$

$$
\frac{\partial L}{\partial w}=-(y-\hat y)x,
\qquad
\frac{\partial L}{\partial b}=-(y-\hat y)
$$

## 13.3 隐藏层

设 $\delta^{(l)}=\partial L/\partial z^{(l)}$：

$$
\delta^{(l)}=\left(W^{(l+1)}\delta^{(l+1)}\right)\odot f'(z^{(l)})
$$

$$
\frac{\partial L}{\partial W^{(l)}}=\delta^{(l)}h^{(l-1)T},
\qquad
\frac{\partial L}{\partial b^{(l)}}=\delta^{(l)}
$$

## 13.4 梯度消失/爆炸

- 深层网络中，梯度是**连乘**；
- sigmoid/tanh 的导数 $<1$ ⇒ 连乘趋 0（vanishing）；
- 权重过大 ⇒ 连乘爆炸；
- 缓解：ReLU、BatchNorm、残差连接、合适初始化。

---

# 14. 优化与训练技巧

## 14.1 Gradient Descent

$$
\theta\leftarrow\theta-\eta\nabla L(\theta)
$$

| 变体 | 每次用多少数据 |
|---|---|
| Batch GD | 全部 |
| SGD | 1 个 |
| Mini-batch | $B$ 个 |

## 14.2 Momentum

$$
v_t=\beta v_{t-1}+(1-\beta)\nabla L,
\qquad
\theta\leftarrow\theta-\eta v_t
$$

- 加速沿一致方向、抑制震荡。

## 14.3 Adam

$$
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
\qquad
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
$$

$$
\hat m_t=\frac{m_t}{1-\beta_1^t},
\qquad
\hat v_t=\frac{v_t}{1-\beta_2^t}
$$

$$
\theta\leftarrow\theta-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
$$

## 14.4 Learning Rate

- 太大 ⇒ 震荡/发散；
- 太小 ⇒ 收敛慢；
- 常用 schedule：step decay、cosine、warmup。

## 14.5 初始化

- 全零 ⇒ 对称性无法打破；
- Xavier：适合 tanh/sigmoid；
- He：适合 ReLU。

---

# 15. 正则化

| 方法 | 做法 | 作用 |
|---|---|---|
| **L2** | 加 $\lambda\|w\|^2$ | 权重变小、平滑 |
| **L1** | 加 $\lambda\|w\|_1$ | 稀疏 |
| **Dropout** | 训练时随机置零 | 防止共适应 |
| **Early stopping** | 验证集变差就停 | 防止过拟合 |
| **BatchNorm** | 每层归一化 | 稳定训练、加速 |
| **Data augmentation** | 旋转/翻转/裁剪 | 增加数据多样性 |

## 15.1 Dropout

训练时：

$$
h_i'=\frac{m_i}{p}h_i,
\qquad
m_i\sim\mathrm{Bernoulli}(p)
$$

测试时不 dropout（或用期望缩放）。

## 15.2 BatchNorm

$$
\hat x=\frac{x-\mu_B}{\sqrt{\sigma_B^2+\epsilon}},
\qquad
y=\gamma\hat x+\beta
$$

- 训练用 batch 统计量；
- 测试用 running平均。

## 15.3 Underfitting vs Overfitting

| 情况 | 训练误差 | 验证误差 | 对策 |
|---|---|---|---|
| Underfitting | 高 | 高 | 更复杂模型、训练更久 |
| Overfitting | 低 | 高 | 正则、更多数据、早停 |
| Good fit | 低 | 低（gap 小） | — |

---

# 16. CNN

## 16.1 为什么 MLP 不适合图像

- 参数量爆炸（$224\times224\times3$ 的图接 FC 就是百万级）；
- 平移后输入完全改变，MLP 不具平移不变性；
- 图像局部结构（边缘、纹理）应被**共享的 filter**捕捉。

## 16.2 卷积

$$
y_{i,j,k}=\sum_{n=1}^{C}\sum_{m}\sum_{l}w_{l,m,n,k}\,x_{i-l,j-m,n}+b_k
$$

- **local receptive field**：每个输出只看局部；
- **parameter sharing**：同一个 filter 滑全图；
- **translation equivariance**：平移输入 ⇒ 平移输出。

## 16.3 输出尺寸

$$
W_{out}=\frac{W_{in}-F+2P}{S}+1
$$

**例**：$32\times32$，$5\times5$，pad 0，stride 1 ⇒ $28\times28$。

## 16.4 参数量

$$
F\cdot F\cdot C\cdot D+D
$$

**例**：$5\times5\times3$、8 个 filter ⇒ $8\times(75+1)=608$。

## 16.5 Pooling

- Max pooling / average pooling；
- 无参数；
- 降低空间尺寸、增加感受野、提供一定平移不变性。

## 16.6 典型结构

```
CONV → ReLU → POOL → ... → Flatten → FC → Softmax
```

- 浅层学边缘/颜色；
- 深层学语义/物体；
- 感受野随深度增大。

## 16.7 ResNet

$$
y=x+\mathcal F(x)
$$

- skip connection 让梯度直接回传；
- 缓解 vanishing gradient，可训练很深。

## 16.8 1×1 卷积

- 通道维度线性组合；
- 用于降维/升维、增加非线性；
- 参数量 $C\cdot D+D$。

---

# 17. ReLU 网络的性质

## 17.1 分段线性

$$
f(x)=\sum_{i=1}^{m}v_i\max(0,w_ix+b_i)+c
$$

- 每个 ReLU 在 $x=-b_i/w_i$ 处斜率改变；
- 所以 $f$ 是**分段线性**，最多 $m$ 个 kink。

## 17.2 构造 $\lvert x\rvert$

$$
|x|=\mathrm{ReLU}(x)+\mathrm{ReLU}(-x)
$$

参数：$w_1=1,b_1=0,v_1=1$；$w_2=-1,b_2=0,v_2=1$；$c=0$。

## 17.3 逼近 $x^2$

- 增加 $m$ ⇒ 更多折线段 ⇒ 折线逼近抛物线；
- 若激活是线性的 ⇒ $f(x)=Ax+B$，无论 $m$ 多大都只是直线。

---

# 18. 公式表

## 18.1 概率

$$
p(x)=\int p(x,y)dy,
\qquad
p(y\mid x)=\frac{p(x,y)}{p(x)}
$$

$$
\mathrm{Var}(X)=\mathbb E[X^2]-(\mathbb E X)^2
$$

## 18.2 估计

$$
\hat\theta_{\mathrm{MLE}}=\arg\max_\theta\sum_i\ln p(x_i\mid\theta)
$$

$$
\hat\theta_{\mathrm{MAP}}=\arg\max_\theta\left[\sum_i\ln p(x_i\mid\theta)+\ln p(\theta)\right]
$$

## 18.3 EM / GMM

$$
Q(\theta\mid\theta^{(t)})=\mathbb E_{z\mid x,\theta^{(t)}}[\ln p(x,z\mid\theta)]
$$

$$
r_{ik}=\frac{\pi_k\mathcal N(x_i\mid\mu_k,\Sigma_k)}{\sum_j\pi_j\mathcal N(x_i\mid\mu_j,\Sigma_j)}
$$

## 18.4 HMM

$$
\alpha_t(j)=p(x_t\mid s_j)\sum_i\alpha_{t-1}(i)T(i,j)
$$

$$
\gamma_t(i)=\frac{\alpha_t(i)\beta_t(i)}{\sum_j\alpha_t(j)\beta_t(j)}
$$

## 18.5 Sampling

$$
P(\text{accept})=\frac1M,
\qquad
A(x,y)=\min\left(1,\frac{\tilde\pi(y)q(y,x)}{\tilde\pi(x)q(x,y)}\right)
$$

## 18.6 NN / CNN

$$
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}},
\qquad
L=-\sum_k y_k\ln p_k
$$

$$
W_{out}=\frac{W_{in}-F+2P}{S}+1,
\qquad
\text{params}=F^2CD+D
$$

---

# 19. 基础自测 20 题＋答案

**1.** 写出 Bayes 公式。
**答**：$p(\theta\mid D)=p(D\mid\theta)p(\theta)/p(D)$。

**2.** 期望的线性性是什么？
**答**：$\mathbb E[aX+bY]=a\mathbb E X+b\mathbb E Y$。

**3.** Bernoulli 的 MLE？
**答**：$\hat\theta=r/n$。

**4.** Gaussian 的 MLE 均值与方差？
**答**：$\hat\mu=\bar x$，$\hat\sigma^2=\frac1n\sum(x_i-\bar x)^2$。

**5.** 为什么 MLE 的方差有偏？
**答**：除以 $n$，低估总体方差；无偏估计除以 $n-1$。

**6.** Beta 分布为什么是 Bernoulli 的共轭先验？
**答**：Beta×Bernoulli 后验仍是 Beta。

**7.** MAP 与 MLE 的关系？
**答**：MAP 加先验；uniform prior 时相同。

**8.** 为什么混合模型要用 EM？
**答**：log 内套 sum，无法直接求导。

**9.** EM 的两步？
**答**：E-step 求 complete-data log-likelihood 的条件期望；M-step 最大化。

**10.** EM 是否保证全局最优？
**答**：只保证局部最优、单调不降。

**11.** HMM 的三个基本问题？
**答**：evaluation（forward）、decoding（Viterbi）、learning（Baum-Welch）。

**12.** Baum-Welch 中 $\gamma$ 与 $\xi$ 的含义？
**答**：$\gamma_t(i)=p(z_t=s_i\mid x)$；$\xi_t(i,j)=p(z_t=s_i,z_{t+1}=s_j\mid x)$。

**13.** Rejection sampling 的接受概率？
**答**：$1/M$。

**14.** Importance sampling 的权重？
**答**：$w_i\propto \tilde p(x_i)/q(x_i)$。

**15.** MH 的接受概率？
**答**：$\min(1,\tilde\pi(y)q(y,x)/(\tilde\pi(x)q(x,y)))$。

**16.** Gibbs 为什么总是接受？
**答**：proposal 就是全条件分布。

**17.** 为什么需要非线性激活？
**答**：否则多层等价于单层线性变换。

**18.** Softmax + CE 的梯度？
**答**：$\partial L/\partial z_k=p_k-y_k$。

**19.** CNN 输出尺寸公式？
**答**：$(W-F+2P)/S+1$。

**20.** ReLU 网络为什么是分段线性？
**答**：有限个 ReLU 之和，每个 ReLU 在零点改变斜率。

---

> **下一步**：把这份资料过一遍后，用 `EE6497_Final_Review.pdf` 按题型做真题；两部分配合，Part 1 的推断题与 Part 2 的网络计算都能覆盖。
