# EE6497 Quiz 1 复习笔记

> **Quiz 1 信息**（权威，取自 Week 5/6 课件公告 + Week 1 考核表）
> - **时间**：Week 7 周一，lecture theater 现场完成（需带 laptop/tablet + photo ID）
> - **时长**：60 分钟
> - **范围**：**Week 1–4**（Week 5–6 不考，留期末）
> - **题型**：填空题（fill-in-the-blank）为主，概念 + 推导 + 计算
> - **可带**：1 张 A4 reference sheet（双面可写任意公式）
> - **形式**：lockdown browser（通过 NTULearn 完成）；无有效 LOA/MC 缺考记 0
> - **难度**：比每周 practice problems 稍难，与 review session 的 review questions 相当
>
> **来源**：本复习笔记整合 Week 1–4 的 `Learning_note.md` 内容 + Week 6 的 Quiz 1 review session（`quiz1/review.txt`，老师讲的 4 道复习题）。转写噪声已按课件修正。

---

## ⭐ 老师在 review session 明确强调的应试要点

1. **MLE 不要只会"求导令零"**：先看 likelihood / log-likelihood 函数形态。函数单调（linear in θ）时取**可行域边界**值，不必求导；凹函数才用求导令零。**最终的 maximizer 必须落在参数可行域内**（如 θ∈[0,1]），落在域外的解不是答案。
2. **likelihood / log-likelihood 要写对**：常见粗心错误——IID 乘积里 λ^n 的 **power n 别漏**（Exponential MLE）；log 后乘积变求和别漏项。
3. **EM 算法要会写具体名字**：HMM 的参数学习用 **Baum-Welch**（只写 "EM algorithm" 虽技术正确但不显示你知道 HMM 的专门算法，会被扣分或不得分）。推断最可能隐状态**序列**用 **Viterbi**（不是 forward-backward，forward 只做 filtering）。
4. **EM 只保证收敛到 local maximum**，不保证 global；多随机初值取最优。
5. **EM 的 E step**：是 $E[\log p(Y|\theta) \mid X, \theta^{(old)}]$ 的**条件期望**，条件在观测 $X$ 与上一轮估计 $\theta^{(old)}$ 上。
6. **MLE 依赖你实际观察到什么**：观察整个序列 vs 只观察末端，likelihood 不同，MLE 可能完全不同（review Q D vs E）。

---

## 一、Week 1：概率论复习 + 共轭先验

### 1.1 必记分布的 likelihood

| 分布 | 参数 | likelihood $p(D|\theta)$ | MLE |
|---|---|---|---|
| **Bernoulli** | θ∈[0,1] | $\theta^{N_1}(1-\theta)^{N_0}$，$N_k=\sum\mathbf{1}\{x_i=k\}$ | $\hat\theta=N_1/n$ |
| **Exponential** | λ>0 | $\lambda^n\exp(-\lambda\sum x_i)$ | $\hat\lambda=n/\sum x_i$ |
| **Gaussian**（σ² 已知） | μ | $(2\pi\sigma^2)^{-n/2}\exp[-\sum(x_i-\mu)^2/(2\sigma^2)]$ | $\hat\mu=\bar x$ |
| **Gaussian**（μ 已知） | σ² | 同上 | $\hat\sigma^2=\frac1n\sum(x_i-\mu)^2$ |

> ⚠️ Exponential：log-likelihood $=n\log\lambda-\lambda\sum x_i$，求导 $n/\lambda-\sum x_i=0$。**别漏 $\lambda^n$ 的 n**。

### 1.2 核心概率公式

- **Bayes' Rule**：$p(\theta|x)=\frac{p(x|\theta)p(\theta)}{p(x)}$，分母不依赖 θ 时可忽略（∝）。
- **posterior ∝ likelihood × prior**。
- **IID**：联合 = 各点之积；log 后变求和（log 单调，不改变 argmax）。
- **Expectation 线性性**：$E[x+y]=E[x]+E[y]$，$E[cx]=cE[x]$；独立 ⇒ $E[xy]=E[x]E[y]$。
- **Variance**：$\text{Var}(x)=E[x^2]-(E[x])^2$；$\text{Var}(x+y)=\text{Var}(x)+\text{Var}(y)+2\text{Cov}(x,y)$。
- **Covariance**：$\text{Cov}(x,y)=E[xy]-E[x]E[y]$；独立 ⇒ Cov=0，但 **Cov=0 ⇏ 独立**。
- **Covariance matrix**：$\Sigma_x=E[(x-\mu)(x-\mu)^T]$，对角为方差、其余为协方差。

### 1.3 共轭先验（Conjugate Prior）

| likelihood | conjugate prior | posterior |
|---|---|---|
| Bernoulli / Binomial | **Beta(a,b)** | Beta($N_1$+a, $N_0$+b) |
| Categorical | **Dirichlet** | Dirichlet(更新计数) |
| Gaussian（对均值 μ） | **Gaussian** | Gaussian |

- 选 conjugate prior 的好处：posterior 与 prior 同族，闭式可算。
- 缺点：特殊情形才成立；不满足 → Week 6 用 **MCMC**。

---

## 二、Week 2：MLE / MAP / Linear Regression

### 2.1 MLE 通用流程

$$\theta_{ML}=\arg\max_\theta p(D|\theta)\;\Leftrightarrow\;\arg\max_\theta \log p(D|\theta)$$

1. 写 likelihood（IID → 乘积）。
2. 取 log（乘积变求和）。
3. 对 θ 求导令零，解方程（依赖 concavity 保证是 max）。
4. **不可导时**：直接分析目标函数极值（如含绝对值 |θ−y| → θ=y 取最小）。

### 2.2 ⭐ MLE 各分布速记（review session Q1/Q3 原题）

**Gaussian variance MLE（μ 已知，review Q1）**：

$$\log p(D|\sigma^2)=-\frac n2\log(2\pi\sigma^2)-\frac{1}{2\sigma^2}\sum(x_i-\mu)^2$$

不含 $\sigma^2$ 的项归常数。对 $\sigma^2$ 求偏导（把 $\sigma^2$ 当单一变量）：

$$\frac{\partial}{\partial\sigma^2}=-\frac{n}{2\sigma^2}+\frac{1}{2(\sigma^2)^2}\sum(x_i-\mu)^2=0$$

$$\boxed{\hat\sigma^2_{ML}=\frac1n\sum_{i=1}^n(x_i-\mu)^2}$$

**Exponential MLE（review Q3）**：$D=\{x_1,\dots,x_n\}$ IID $\sim\text{Exp}(\lambda)$，$p(x|\lambda)=\lambda e^{-\lambda x}$。

$$p(D|\lambda)=\prod_i\lambda e^{-\lambda x_i}=\lambda^n e^{-\lambda\sum x_i}\;\Rightarrow\;\log p=n\log\lambda-\lambda\sum x_i$$

求导令零：$n/\lambda-\sum x_i=0$ ⇒ $\hat\lambda=n/\sum x_i$。

> ⚠️ **review 老师强调**：$\lambda$ 在乘积里每项都有，所以有 $\lambda^n$，**power n 别漏**。

### 2.3 ⭐ Boundary MLE（函数不可导或单调时，review session 重点）

老师画图说明的核心点：

- likelihood 函数若在可行域内**单调递增**（如 linear 且系数为正）→ maximizer 取**上界**。
- 若**单调递减** → 取**下界**。
- 若有**内部峰值但峰值在可行域外** → 取最接近峰值的**边界**值。
- **总结**：别默认求导=0。先判断函数在可行域内是增是减，单调就直接取边界。θ 是概率时域为 [0,1]。

**review Q E 的例子**（只观测 $x_2$，求 θ 的 MLE）：likelihood $=(0.36+0.1\theta)^2$，对 θ 单调递增，θ∈[0,1] → $\hat\theta_{ML}=1$（取上界）。对比 Q D 观测整个序列时 $\hat\theta_{ML}=0.5$——**观察到什么决定 MLE**。

### 2.4 MAP

$$\theta_{MAP}=\arg\max_\theta[\log p(D|\theta)+\log p(\theta)]$$

- MLE = prior 均匀时的 MAP 特例。
- **Bernoulli + Beta(a,b)**：$\hat\theta_{MAP}=\frac{N_1+a-1}{n+a+b-2}$（MLE 分子 $N_1$ 变 $N_1$+a−1，分母 $n$ 变 $n$+a+b−2）。
- **Gaussian（σ² 已知）+ Gaussian prior $\mu\sim N(\mu_0,\tau^2)$**：

$$\hat\mu_{MAP}=\frac{\frac1{\sigma^2}\sum_i x_i+\frac{\mu_0}{\tau^2}}{\frac n{\sigma^2}+\frac1{\tau^2}}$$

n 大 ⇒ MAP≈MLE（prior 被稀释）；n 小 ⇒ prior 拉动估计。

### 2.5 Linear Regression = MLE

$y=w^T x+\epsilon$，$\epsilon\sim N(0,\sigma^2)$ ⇒ MLE ⇔ 最小二乘：

$$w_{ML}=(\Phi^T\Phi)^{-1}\Phi^T y$$

- 要求 $\Phi^T\Phi$ 可逆 ⇔ $\Phi$ 列满秩 ⇔ n ≥ M。
- 判 linear regression：只看 **w 是否线性**（x 上可任意非线性变换）。

### 2.6 Classification = cross-entropy loss

分类用 MLE 估 θ ⇔ 最小化 **cross-entropy loss** $-\sum_i\sum_k\mathbf{1}\{y_i=k\}\log q(k|x_i,\theta)$。

### 2.7 Overfitting

- train error 随复杂度↓，test error 在某点后反弹。
- degree=20 拟合训练近乎完美但 test R²=−5167 → 经典 overfitting。
- 比较 train/test R² 判断是否过拟合。

---

## 三、Week 3：Mixture Models + EM Algorithm

### 3.1 Mixture Model 与 latent variable

$$p(x|\theta)=\sum_{k=1}^K\pi(k)\,p(x|\eta_k),\quad \theta=(\pi,\{\eta_k\})$$

- $z\sim\text{Cat}(\pi)$ 指示来自哪个分量，**未被观测 → latent variable**。
- **GMM**：各分量为 Gaussian $N(x|\mu_k,\Sigma_k)$。

### 3.2 ⭐ MLE 的三大困难

| 困难 | 说明 |
|---|---|
| **Singularity** | 某分量 $\mu_k=x_i,\sigma_k\to0$ 时 likelihood → ∞（可无限放大），MLE 无意义。EM 也无法解决 → 用 MAP 加 prior 抑制。 |
| **Unidentifiability** | 置换分量标号 k 得到相同 pdf → 无唯一全局最优（找 good likelihood 即可）。 |
| **Optimization** | $\log\sum_k(\cdot)$ 中 log 与 sum **不可交换**，目标非凹，无闭式解 → **EM 的动机**。 |

### 3.3 ⭐ EM 算法（review session Q B 重点）

**核心思想**：complete data $y=(x,z)$ 易优化，但 $z$ 未知 → 用对 $y$ 的**期望**替代。

**E step**：计算 Q 函数（条件期望，条件在 $X$ 与 $\theta^{(old)}$ 上）：

$$Q(\theta|\theta^{(m)})=E_{p(y|x,\theta^{(m)})}[\log p(y|\theta)]=\int\log p(y|\theta)\,p(y|x,\theta^{(m)})\,dy$$

> ⭐ **review Q B 判 True**：E step 求 $E[\log p(Y|\theta)\mid X,\theta^{(old)}]$，期望**条件在观测 $X$ 与上一轮估计 $\theta^{(old)}$**，用的 PDF 是 $p(y|x,\theta^{(m)})$（上一轮参数构造）。

**M step**：

$$\theta^{(m+1)}=\arg\max_\theta Q(\theta|\theta^{(m)})$$

- **Monotonicity**：每次迭代 log-likelihood **只增不减**（用 Jensen 不等式证明，Q 是 ELBO 下界），但只收敛到 **local maximum**，不保证 global → 多随机初值取最优。
- **EM for MAP**：E step 同 MLE；M step 多加 $\log p(\theta)$：$\theta^{(m+1)}=\arg\max[Q+\log p(\theta)]$。

### 3.4 ⭐ EM for GMM（必记闭式解）

**E step — responsibility**（软分配，$\sum_k r_{ik}=1$）：

$$r_{ik}^{(m)}=\frac{\pi^{(m)}(k)\,N(x_i|\mu_k^{(m)},\Sigma_k^{(m)})}{\sum_{k'}\pi^{(m)}(k')\,N(x_i|\mu_{k'}^{(m)},\Sigma_{k'}^{(m)})}$$

记 $n_k^{(m)}=\sum_i r_{ik}^{(m)}$。

**M step — 闭式更新**：

$$\pi^{(m+1)}(k)=\frac{n_k^{(m)}}{n},\quad \mu_k^{(m+1)}=\frac{1}{n_k^{(m)}}\sum_i r_{ik}^{(m)}x_i,\quad \Sigma_k^{(m+1)}=\frac{1}{n_k^{(m)}}\sum_i r_{ik}^{(m)}(x_i-\mu_k^{(m+1)})(x_i-\mu_k^{(m+1)})^T$$

### 3.5 K-Means = hard EM 的 GMM 特例

- GMM 令 $\Sigma_k=\sigma^2 I$（共享、固定）、$\pi(k)=1/K$（固定），只推 $\mu_k$。
- E step 退化为 **hard assignment**（one-hot）：$r_{ik}=1$ 当 $k=\arg\min_k\|x_i-\mu_k\|^2$。
- M step：$\mu_k=\frac{1}{N_k}\sum_{i:k_i=k}x_i$（簇内均值）。
- 选 K：loss vs K 曲线找 **elbow**。

---

## 四、Week 4：Markov Models + HMM

### 4.1 Markov Chain 基础

- **Markov property**：$p(x[t]\mid x[1],\dots,x[t-1])=p(x[t]\mid x[t-1])$。
- **Transition matrix** $T(i,j)=P(x[t]=j\mid x[t-1]=i)$，行和=1（row stochastic）。
- **状态分布演化**：$p_t=p_{t-1}T=p_0T^t$。

### 4.2 ⭐ Markov Chain 的 MLE（review session Q C/D 原题）

完整观测序列，参数 $\theta=(\pi,T)$：

$$\log p(D|\pi,T)=\sum_x N_x\log\pi(x)+\sum_x\sum_y N_{xy}\log T(x,y)$$

- $N_x$ = 状态 x 作为**起始**的次数；$N_{xy}$ = 从 x 转到 y 的次数。
- **MLE 闭式解**：

$$\hat\pi(x)=\frac{N_x}{n},\quad \hat T(x,y)=\frac{N_{xy}}{\sum_z N_{xz}}$$

**review Q C 原题**：2 状态 MC，$T=\begin{bmatrix}0.3&0.7\\0.4&0.6\end{bmatrix}$，初始 $\pi_0(1)=\theta,\pi_0(2)=1-\theta$。

- $p_1=p_0T$：$\pi_1(1)=0.3\theta+0.4(1-\theta)=0.4-0.1\theta$，$\pi_1(2)=0.6+0.1\theta$。
- $p_2=p_0T^2$：$T^2=\begin{bmatrix}0.37&0.63\\0.36&0.64\end{bmatrix}$，$\pi_2(1)=0.36+0.01\theta$，$\pi_2(2)=0.64-0.01\theta$。

**review Q D（观测完整序列的 MLE）**：两条序列，$\hat\theta_{ML}=0.5$。
- 序列 1 (1→2→1)：likelihood $=\theta\times0.7\times0.4$。
- 序列 2 (2→1→1)：likelihood $=(1-\theta)\times0.4\times0.3$。
- 只有初始 $\pi_0$ 依赖 θ，转移概率都是常数 → log-likelihood 只含 $\log\theta+\log(1-\theta)$ → 求导得 θ=0.5。

> ⭐ **关键洞察（老师强调）**：转移概率 $T$ 不依赖 θ，只有初始分布 $\pi_0$ 依赖 θ。所以 MLE 只由 $\pi_0$ 部分决定，转移部分是冗余信息。

**review Q E（只观测 $x_2$ 的 MLE）**：只看到 $\pi_2$，不观测 $x_0,x_1$。
- 两次观测都 $x_2=1$ → likelihood $=\pi_2(1)^2=(0.36+0.01\theta)^2$。
- 对 θ 单调递增，θ∈[0,1] → $\hat\theta_{ML}=1$（取上界）。
- 对比 Q D 的 0.5：**观察到什么决定 MLE**。

### 4.3 HMM 结构

- 隐状态 $z[t]$（latent）走 Markov chain，每个 $z[t]$ 独立发射观测 $x[t]$。
- **观测 $x[t]$ 不满足 Markov 性**，长程依赖通过 $z[t]$ 捕捉。
- 参数：初始 $\pi$、转移 $T$、emission $p(x[t]\mid z[t])=p(x[t]\mid\phi_{z[t]})$。

### 4.4 ⭐ HMM 三大问题与算法（review session Q4 重点）

| 问题 | 公式 | 算法 |
|---|---|---|
| **Evaluation** | $p(x[0:T]\mid\theta)$ | Forward algorithm |
| **Decoding** | $z^*[0:T]=\arg\max_z p(z[0:T]\mid x[0:T])$ | **Viterbi algorithm** |
| **Learning** | $\hat\theta=\arg\max_\theta\log p(D\mid\theta)$ | **Baum-Welch**（EM for HMM） |

- **Filtering**（online，$p(z[t]\mid x[0:t])$）：Forward。
- **Smoothing**（offline，$p(z[t]\mid x[0:T])$）：Forward-Backward。
- **MAP sequence**（整个隐状态序列）：**Viterbi**。

### 4.5 ⭐ review Q4 原题：中文语音转写 HMM

**(a) 描述 HMM**：
- $z[t]$ = 实际说的中文字符（latent，未观测）；$x[t]$ = 语音特征（观测）。
- **transition model** $p(z[t]\mid z[t-1])$ ↔ **language model**（语言模型，前字给后字概率），$T$ 是 $n\times n$（n=字典字符数）。
- **emission model** $p(x[t]\mid z[t])$ ↔ **acoustic model**（声学模型，取决于环境/录音）。

**(b) 学参数用什么算法**：**Baum-Welch**（别只写 EM）。

**(c) 给观测序列推断所有字符用什么算法**：**Viterbi**（不是 forward-backward——forward 只做 filtering，forward-backward 是为 Baum-Welch 求 $\gamma,\xi$ 服务的）。

### 4.6 Baum-Welch（EM for HMM）

- E step 用 **forward-backward** 算两个后验：
  - $\gamma_{i,t}(z)=p(z^i[t]=z\mid x^i[0:t_i],\theta^{(m)})$（单时刻 marginal posterior）
  - $\xi_{i,t}(z,z')=p(z^i[t-1]=z,z^i[t]=z'\mid x^i[0:t_i],\theta^{(m)})$（相邻时刻 joint posterior）
- M step 把完整观测 MLE 的**硬计数** $\mathbf{1}\{\cdot\}$ 换成**软后验** $\gamma,\xi$：

$$\hat\pi(z)=\frac{\sum_i\gamma_{i,0}(z)}{n},\quad \hat T(z,z')=\frac{\sum_{i,t}\xi_{i,t}(z,z')}{\sum_{i,t,u}\xi_{i,t}(z,u)}$$

$$\hat\mu_z=\frac{\sum_{i,t}\gamma_{i,t}(z)x^i[t]}{\sum_{i,t}\gamma_{i,t}(z)},\quad \hat\Sigma_z=\frac{\sum_{i,t}\gamma_{i,t}(z)(x^i[t]-\hat\mu_z)(\cdot)^T}{\sum_{i,t}\gamma_{i,t}(z)}$$

### 4.7 Viterbi（动态规划求 MAP 路径）

$$\delta_t(z)=\max_{z'}\{\delta_{t-1}(z')+\log T(z',z)\}+\log p(x[t]\mid z[t]=z)$$

$$a_t(z)=\arg\max_{z'}\{\delta_{t-1}(z')+\log T(z',z)\}$$

- 初始化 $\delta_0(z)=\log\pi(z)+\log p(x[0]\mid z)$。
- 终止 $z^*[T]=\arg\max_z\delta_T(z)$，回溯 $z^*[t]=a_{t+1}(z^*[t+1])$。

---

## 五、review session 4 道复习题完整解

### Review Q1：Gaussian variance MLE（μ 已知）

$$\log p(D|\sigma^2)=-\frac n2\log\sigma^2-\frac{1}{2\sigma^2}\sum(x_i-\mu)^2+\text{const}$$

对 $\sigma^2$ 求偏导令零 → $\hat\sigma^2_{ML}=\frac1n\sum(x_i-\mu)^2$。

### Review Q2：Bernoulli MLE + EM 判断 + Exponential MLE

- **(A)** Bernoulli $p(x|\theta)=\theta^x(1-\theta)^{1-x}$，$\log p=\sum[x_i\log\theta+(1-x_i)\log(1-\theta)]$，求导 → $\hat\theta=\bar x$。
- **(B)** EM E step 判 **True**（见 §3.3）。
- **(C)** Exponential MLE $\hat\lambda=n/\sum x_i$（见 §2.2，别漏 $\lambda^n$）。

### Review Q3（review 标 4）：Markov chain MLE

- **(C)** 写 transition matrix、算 $\pi_1,\pi_2$（见 §4.2）。
- **(D)** 观测完整序列 → $\hat\theta=0.5$（只有 $\pi_0$ 依赖 θ）。
- **(E)** 只观测 $x_2$ → likelihood 单调递增 → $\hat\theta=1$（取上界）。

### Review Q4：HMM 应用题

- 中文语音转写：$z$=字符(latent)、$x$=语音(obs)；transition↔language model、emission↔acoustic model；学参数用 **Baum-Welch**；推断序列用 **Viterbi**（见 §4.5）。

---

## 六、⭐ 考点速查表（Week 1–4 全覆盖）

| # | 考点 | 关键公式/答案 | 易错点 |
|---|---|---|---|
| 1 | Bernoulli MLE | $\hat\theta=N_1/n$ | — |
| 2 | Exponential MLE | $\hat\lambda=n/\sum x_i$ | **λ^n 的 n 别漏** |
| 3 | Gaussian μ MLE（σ²已知） | $\hat\mu=\bar x$ | — |
| 4 | Gaussian σ² MLE（μ已知） | $\hat\sigma^2=\frac1n\sum(x_i-\mu)^2$ | 对 $\sigma^2$ 求导，别对 σ |
| 5 | Boundary MLE | 单调→取边界 | 别默认求导=0，先看函数形态 |
| 6 | MAP = MLE + log prior | $\arg\max[\log L+\log p(\theta)]$ | prior 均匀→退化为 MLE |
| 7 | Bernoulli+Beta MAP | $(N_1+a-1)/(n+a+b-2)$ | 分子 a−1、分母 a+b−2 |
| 8 | Linear regression MLE | $(\Phi^T\Phi)^{-1}\Phi^T y$ | 要求列满秩 n≥M |
| 9 | Classification MLE | = cross-entropy loss | indicator 分组 |
| 10 | Conjugate prior | Beta/Dirichlet/Gaussian | 对应关系别记混 |
| 11 | Mixture model | $p(x)=\sum_k\pi(k)p(x\mid\eta_k)$ | z 是 latent，marginalize 消去 |
| 12 | EM 三大困难 | singularity/unidentifiability/optimization | log 与 sum 不可交换 |
| 13 | EM E step | $Q=E_{p(y\mid x,\theta^{(m)})}[\log p(y\mid\theta)]$ | 条件在 $X$ 与 $\theta^{(old)}$ |
| 14 | EM monotonicity | log-likelihood 只增不减 | 只到 local max，多初值 |
| 15 | GMM responsibility | $r_{ik}=\pi(k)N(x_i\mid\mu_k,\Sigma_k)/\sum_{k'}$ | $\sum_k r_{ik}=1$ |
| 16 | GMM M step | $\pi=n_k/n,\mu=\sum r_{ik}x_i/n_k$ | $\Sigma$ 含 $(x_i-\mu^{(new)})$ |
| 17 | K-Means | = hard EM 的 GMM（$\Sigma=\sigma^2I$ 共享） | hard assignment one-hot |
| 18 | Markov MLE | $\hat\pi(x)=N_x/n,\hat T(x,y)=N_{xy}/\sum_z N_{xz}$ | 行和=1 |
| 19 | MC 状态演化 | $p_t=p_0T^t$ | 行向量左乘 T |
| 20 | HMM 三问题 | Forward/Viterbi/Baum-Welch | **推断序列=Viterbi 非 forward** |
| 21 | HMM 学参数 | **Baum-Welch**（别只写 EM） | 名字要具体 |
| 22 | Baum-Welch M step | 硬计数→软后验 $\gamma,\xi$ | $\gamma$ 单时刻、$\xi$ 相邻 |
| 23 | HMM 应用映射 | transition↔language, emission↔acoustic | speech recognition 场景 |

---

## 七、A4 reference sheet 建议内容

reference sheet 双面可写，建议按以下优先级排版（小字、双栏）：

**正面**：
1. 三大分布 likelihood + MLE 表（§1.1）
2. Bayes rule、IID log、expectation/variance/covariance 公式
3. MAP 公式 + Bernoulli+Beta MAP + Gaussian+Gaussian MAP
4. Linear regression MLE 闭式解 + cross-entropy loss
5. Conjugate prior 对应表

**反面**：
6. Mixture model 形式 + 三大困难
7. EM 的 Q 函数 + E/M step 一般形式 + monotonicity
8. **GMM responsibility + M step 三公式**（最重要，必抄）
9. K-Means = hard EM 条件
10. Markov MLE（$\hat\pi,\hat T$）+ $p_t=p_0T^t$
11. HMM 三问题算法表 + Baum-Welch M step（γ,ξ 形式）
12. Viterbi 递推 + 回溯

> 不必抄概念描述（reference sheet 是公式速查，概念靠理解）。多留空间给 **GMM EM 闭式解** 和 **Baum-Welch 更新**，这两块计算量最大。

---

## 八、应试策略

1. **MLE 题**：先写 likelihood → 取 log → 判断可不可导。可导就求导令零；**不可导或单调就直接分析函数取边界**。检查答案在可行域内。
2. **EM 题**：E step 写 Q 函数与条件期望（标明条件在 $X,\theta^{(old)}$）；M step 写更新公式。GMM 直接套闭式解。
3. **HMM 题**：学参数写 **Baum-Welch**（别只写 EM）；推断序列写 **Viterbi**；evaluation 写 Forward。区分 filtering（Forward）/smoothing（Forward-Backward）/MAP sequence（Viterbi）。
4. **Markov MLE**：数 $N_x$（起点）、$N_{xy}$（转移），套公式。注意**只有依赖参数的部分才影响 MLE**（如初始 $\pi_0$ 依赖 θ 时转移概率是冗余）。
5. **描述题**（如 HMM 应用）：说清 latent/observation 变量、transition/emission model 对应什么实际模型、用什么算法。
6. **不会的别空着**：likelihood 写对就有过程分；MLE 题即使求导卡住，写出 likelihood 与 log-likelihood 也能拿分。
