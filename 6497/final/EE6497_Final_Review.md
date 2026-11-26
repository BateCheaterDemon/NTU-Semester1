# EE6497 Pattern Recognition and Deep Learning — Final Exam Review（期末复习）

> **考试**：Final 占总评 **60%**；按往年卷为 **2 小时、4 道题、每题等分（25 分）、全部必答**。
>
> **开卷形式**：**Restricted open book**——只允许**一张双面 A4 reference sheet**（手写或打印，**不能**贴便签/便利贴/胶装附加页）。
>
> **试卷附录**：Appendix A 给常见分布（Bernoulli、Binomial、Categorical、Multinomial、Gaussian、Beta、Dirichlet、Uniform、Exponential 等）；Appendix B 给深度学习常用公式。**这两页不用背，但要知道怎么用**。
>
> **范围**：**Week 1–13 全部内容**（概率/Bayes/MLE/MAP → EM → HMM → Sampling → MCMC → NN/DL/CNN）。Week 13 的 Part 2.4 就是官方复习课。
>
> **重要变化**：Wang Lipo 明确说 **Python 编程不考**（"not in the final exam or in the quiz"）。旧卷里的 PyTorch/NumPy 代码题**可以跳过**，但 **shape、参数量、softmax、卷积手算**仍然要会。

---

## 目录

1. 三套往年卷的命题地图
2. 题型一 — MLE / MAP / EM（约 25 分）
3. 题型二 — HMM 与 Baum-Welch（约 25 分）
4. 题型三 — Sampling 与 MCMC（约 25 分）
5. 题型四 — NN / CNN 计算（约 25 分）
6. 题型五 — ReLU 网络理论（约 25 分）
7. 题型六 — 概念判断与简答（T/F）
8. Week 13 官方复习课例题（Part 2 必看）
9. A4 Reference Sheet 双面模板
10. 公式速查表
11. 模拟卷（4 题）＋ 答案要点
12. 考前 2 天计划

---

# 1. 三套往年卷的命题地图

| 试卷 | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| **2025-26 S2** | (a) T/F 10 分（MLE、K-means、rejection）；(b) censored geometric 的 MLE 15 分 | HMM：2 步 joint / likelihood / 有标注 MLE / 无标注 Baum-Welch（11+11+3） | CNN：shape、参数量、flatten、FC、softmax（6+6+6+7） | ReLU 网络：图形、kink 上界、构造 $\lvert x\rvert$、万能逼近（6+6+6+7） |
| **2024-25 S2** | (a) Bernoulli MLE 8 分；(b) Beta prior MAP 10 分；(c) latent + EM 7 分 | MH acceptance 8 分；HMM + Gibbs 13 分；burn-in / thinning 4 分 | BCE 5 分；SGD 更新 5 分；PyTorch 15 分 | 卷积 shape 5 分；手算卷积 10 分；Python 10 分 |
| **2023-24 S2** | (a) Exponential MLE 10 分；(b) MAP 8 分；(c) EM 7 分 | Rejection sampling 6 分；混合 proposal 12 分；Importance sampling 7 分 | 训练要点 5 分；激活函数判断 5 分；Python debug 15 分 | GAN 数据增强 5 分；CNN bias 5 分；Python 15 分 |

**结论**：

1. **Q1 一定是"参数估计"**：MLE → MAP → EM 三段式，**几乎每年都考**；分布可能是 Bernoulli、Exponential、几何/截断几何、Beta prior。
2. **Q2 一定是"隐变量/采样"**：HMM（joint、likelihood、Baum-Welch）或 MCMC（MH、Gibbs）/ Rejection / Importance。
3. **Q3/Q4 是 Part 2**：CNN 的 shape/参数量/softmax/卷积手算 + 神经网络理论（ReLU、逼近、激活函数、训练）。
4. **旧卷的代码题**（PyTorch/NumPy/debug）在当前课程说明下**不考**；把时间花在**推导与手算**上。

> 分数结构：Part 1（Q1–Q2）≈ 50 分，Part 2（Q3–Q4）≈ 50 分——**两边都要拿**，不能只押 Part 2。

---

# 2. 题型一 — MLE / MAP / EM

## 2.1 通用套路

```
1. 写 likelihood L(θ) = Π p(x_i | θ)（i.i.d.）
2. 取 log：ℓ(θ) = Σ log p(x_i | θ)
3. 对 θ 求导，令 0 → 解 θ̂
4. 检查边界/二阶导（最大值还是最小值）
5. 若有 prior：最大化 log L + log p(θ) → MAP
6. 若有隐变量：写 complete-data log-likelihood → E-step 求期望 → M-step 最大化
```

**常用导数**：

$$
\frac{d}{d\theta}\ln\theta=\frac1\theta,
\qquad
\frac{d}{d\theta}\ln(1-\theta)=-\frac{1}{1-\theta}
$$

## 2.2 Bernoulli / Binomial 的 MLE

数据 $x_i\in\{0,1\}$，$p(x_i\mid\theta)=\theta^{x_i}(1-\theta)^{1-x_i}$：

$$
\ell(\theta)=\sum_i\big[x_i\ln\theta+(1-x_i)\ln(1-\theta)\big]
$$

$$
\frac{d\ell}{d\theta}=\frac{\sum x_i}{\theta}-\frac{n-\sum x_i}{1-\theta}=0
\quad\Longrightarrow\quad
\boxed{\;\hat{\theta}=\frac{\sum x_i}{n}=\frac{r}{n}\;}
$$

**例（2024-25 S2 Q1a）**：100 行人中 20 vulnerable ⇒ $\hat\theta_0=0.2$；50 骑车人中 5 ⇒ $\hat\theta_1=0.1$。

## 2.3 Exponential 的 MLE 与 MAP

$p(x\mid\lambda)=\lambda e^{-\lambda x}$，$x\ge0$：

$$
\ell(\lambda)=n\ln\lambda-\lambda\sum_i x_i
$$

$$
\frac{d\ell}{d\lambda}=\frac{n}{\lambda}-\sum_i x_i=0
\quad\Longrightarrow\quad
\boxed{\;\hat{\lambda}_{\mathrm{MLE}}=\frac{n}{\sum_i x_i}=\frac{1}{\bar{x}}\;}
$$

**MAP**：若先验 $p(\lambda)\propto\lambda e^{-\lambda/3}$（即 Gamma(2, 1/3)）：

$$
\ell_{\mathrm{post}}=(n+1)\ln\lambda-\lambda\left(\sum_i x_i+\frac13\right)+\text{const}
$$

$$
\boxed{\;\hat{\lambda}_{\mathrm{MAP}}
=\frac{n+1}{\sum_i x_i+1/3}\;}
$$

**真题（2023-24 S2 Q1）**：$r=d+\varepsilon$，$\varepsilon\sim\mathrm{Exp}(\lambda)$；数据 $\varepsilon=(0.4,0.3,0.2,0.1)$，$\sum\varepsilon=1$。

- MLE：$\hat\lambda=4/1=4$；
- MAP（prior $\propto\lambda e^{-\lambda/3}$）：$\hat\lambda=(4+1)/(1+1/3)=5/(4/3)=3.75$。

⭐ **为什么用 Exponential 而不是 Gaussian**：$\varepsilon\ge0$（反射路径 ≥ 直射路径），Gaussian 的 support 是 $(-\infty,\infty)$，会产生物理上不可能的负值。**模型选择要看 support / 物理约束**。

## 2.4 截断/删失几何分布的 MLE（2025-26 S2 Q1b）

pmf：

$$
p(x=k\mid\theta)=\theta^{k-1}(1-\theta),\quad k=1,\dots,r;
\qquad
p(x=r+1\mid\theta)=\theta^{r}
$$

（前 $r$ 个值正常观测，$r+1$ 表示"至少 $r$ 次"的删失。）

设 $n_k$ 为取值为 $k$ 的样本数（$k=1,\dots,r+1$）。

**Step 1 — log-likelihood**：

$$
\ell(\theta)=\sum_{k=1}^{r}n_k\big[(k-1)\ln\theta+\ln(1-\theta)\big]
+n_{r+1}\,r\ln\theta
$$

合并 $\ln\theta$ 项：

$$
\sum_{k=1}^{r}n_k(k-1)+r\,n_{r+1}=\sum_{i=1}^{n}x_i-n
$$

（因为每个 $x_i\le r$ 贡献 $x_i-1$，$x_i=r+1$ 贡献 $r$。）

合并 $\ln(1-\theta)$ 项：

$$
\sum_{k=1}^{r}n_k=n-n_{r+1}
$$

所以

$$
\ell(\theta)=\Big(\sum_i x_i-n\Big)\ln\theta
+\big(n-n_{r+1}\big)\ln(1-\theta)
$$

**Step 2 — 求导令零**：

$$
\frac{d\ell}{d\theta}
=\frac{\sum x_i-n}{\theta}
-\frac{n-n_{r+1}}{1-\theta}=0
$$

**Step 3 — 解**：

$$
\boxed{\;\hat{\theta}_{\mathrm{MLE}}
=\frac{\sum_{i=1}^{n}x_i-n}{\sum_{i=1}^{n}x_i-n_{r+1}}\;}
$$

⭐ **易错点**：$x=r+1$ 的概率是 $\theta^r$（不是 $\theta^{r}(1-\theta)$）；求和时要把 $n_{r+1}$ 单独处理。

## 2.5 MAP 与共轭先验

**Bayes**：

$$
p(\theta\mid D)\propto p(D\mid\theta)\,p(\theta)
$$

**共轭先验（conjugate prior）**：后验与先验同族。

| Likelihood | Conjugate prior | Posterior | MAP |
|---|---|---|---|
| Bernoulli/Binomial | Beta$(a,b)$ | Beta$(a+r,\ b+n-r)$ | $\dfrac{r+a-1}{n+a+b-2}$ |
| Categorical/Multinomial | Dirichlet$(\alpha)$ | Dirichlet$(\alpha+n)$ | $\dfrac{n_k+\alpha_k-1}{N+\sum\alpha-2}$ |
| Gaussian（已知 $\sigma$） | Gaussian | Gaussian | 加权平均 |
| Exponential | Gamma | Gamma | $\dfrac{n+\alpha-1}{\sum x_i+\beta}$ |

**真题（2024-25 S2 Q1b）**：Beta$(a,b)$ with $a=2,b=3$：

$$
\hat\theta_0^{\mathrm{MAP}}=\frac{20+2-1}{100+2+3-2}=\frac{21}{103}\approx0.204
$$

$$
\hat\theta_1^{\mathrm{MAP}}=\frac{5+2-1}{50+2+3-2}=\frac{6}{53}\approx0.113
$$

## 2.6 EM 算法

**为什么需要 EM**：有隐变量 $z$ 时，

$$
p(x\mid\theta)=\sum_z p(x,z\mid\theta)
$$

log 里面套 summation：

$$
\ell(\theta)=\sum_i\ln\sum_z p(x_i,z\mid\theta)
$$

**不能**交换 log 与 sum，直接求导通常不可解。

### 2.6.1 EM 两步

**E-step**：用当前参数 $\theta^{(t)}$ 求 complete-data log-likelihood 的条件期望：

$$
Q(\theta\mid\theta^{(t)})
=\mathbb{E}_{z\mid x,\theta^{(t)}}\big[\ln p(x,z\mid\theta)\big]
$$

**M-step**：

$$
\theta^{(t+1)}=\arg\max_\theta Q(\theta\mid\theta^{(t)})
$$

⭐ EM 保证 **log-likelihood 单调不降**（每个 iteration 都不变差）。

### 2.6.2 GMM 的 EM（必背）

模型：

$$
p(x)=\sum_{k=1}^{K}\pi_k\,\mathcal{N}(x\mid\mu_k,\Sigma_k),
\qquad
\sum_k\pi_k=1
$$

**E-step（responsibility）**：

$$
r_{ik}=\frac{\pi_k\,\mathcal{N}(x_i\mid\mu_k,\Sigma_k)}
{\sum_{j}\pi_j\,\mathcal{N}(x_i\mid\mu_j,\Sigma_j)}
$$

**M-step**：

$$
\pi_k^{\mathrm{new}}=\frac{1}{n}\sum_i r_{ik},
\qquad
\mu_k^{\mathrm{new}}=\frac{\sum_i r_{ik}x_i}{\sum_i r_{ik}}
$$

$$
\Sigma_k^{\mathrm{new}}=\frac{\sum_i r_{ik}(x_i-\mu_k^{\mathrm{new}})(x_i-\mu_k^{\mathrm{new}})^{T}}{\sum_i r_{ik}}
$$

### 2.6.3 真题（2023-24 S2 Q1c）

模型 $r=d+\varepsilon$，只观测 $r$，$d\sim\mathrm{Unif}[1,3]$，$\varepsilon\sim\mathrm{Exp}(\lambda)$。

- **Complete data** = $(r,d)$（或 $(r,\varepsilon)$）；
- **E-step**：对每个观测 $r_i$，求 $d_i\mid r_i,\lambda^{(t)}$ 的条件分布，并计算

$$
Q(\lambda\mid\lambda^{(t)})
=\mathbb{E}_{d\mid r,\lambda^{(t)}}\big[\ln p(r,d\mid\lambda)\big]
$$

- **M-step**：最大化 $Q$ 得 $\lambda^{(t+1)}$。

⭐ 答题时写清："complete data 是什么、E-step 对谁取期望、M-step 最大化什么"即可，不必化简。

---

# 3. 题型二 — HMM 与 Baum-Welch

## 3.1 定义

- 隐状态 $z_t\in\{s_1,\dots,s_K\}$；观测 $x_t$；
- **初始分布** $\pi(s_k)=P(z_1=s_k)$；
- **转移矩阵** $T(i,j)=P(z_{t+1}=s_j\mid z_t=s_i)$；
- **发射概率** $p(x_t\mid z_t)$；
- **Markov property**：$z_{t+1}$ 只依赖 $z_t$。

联合分布：

$$
p(z_{1:L},x_{1:L})
=\pi(z_1)\,p(x_1\mid z_1)
\prod_{t=2}^{L}T(z_{t-1},z_t)\,p(x_t\mid z_t)
$$

## 3.2 真题（2025-26 S2 Q2）

设定：

$$
\pi(s_1)=\pi(s_2)=\frac12,
\qquad
T=\begin{bmatrix}a&1-a\\1-b&b\end{bmatrix}
$$

$$
p(o_1\mid s_1)=p,\quad p(o_2\mid s_1)=1-p,
\qquad
p(o_1\mid s_2)=q,\quad p(o_2\mid s_2)=1-q
$$

### (a)(i) $L=2$ 的 joint probability

观测 $x_1=o_2,\ x_2=o_1$。四种状态组合：

$$
p(z_1=s_1,z_2=s_1)=\frac12(1-p)\,a\,p
$$

$$
p(z_1=s_1,z_2=s_2)=\frac12(1-p)(1-a)\,q
$$

$$
p(z_1=s_2,z_2=s_1)=\frac12(1-q)(1-b)\,p
$$

$$
p(z_1=s_2,z_2=s_2)=\frac12(1-q)\,b\,q
$$

（通用写法：$\pi(z_1)\,p(x_1\mid z_1)\,T(z_1,z_2)\,p(x_2\mid z_2)$。）

### (a)(ii) Likelihood（只观测 emission）

把四种组合相加：

$$
p(x_1=o_2,x_2=o_1)
=\frac12\Big[(1-p)\big(ap+(1-a)q\big)+(1-q)\big((1-b)p+bq\big)\Big]
$$

### (b)(i) 有标注序列的 MLE

四条独立序列（状态与观测都给出）：

```
(s1,s1), (s1,s2), (s2,s2), (s2,s1)
```

统计转移次数：

- 从 $s_1$ 出发 2 次：$s_1\to s_1$ 1 次，$s_1\to s_2$ 1 次 ⇒ $\hat a=\frac12$；
- 从 $s_2$ 出发 2 次：$s_2\to s_2$ 1 次，$s_2\to s_1$ 1 次 ⇒ $\hat b=\frac12$。

$$
\boxed{\;\hat a=\hat b=\frac12\;}
$$

⭐ 有标注时，转移概率的 MLE 就是**数转移次数**，与 emission 无关。

### (b)(ii) 无标注（HMM）的 MLE

只有一条观测序列 $(o_2,o_1)$。对 likelihood 关于 $a$ 求导：

$$
\frac{\partial L}{\partial a}
=\frac12(1-p)(p-q)
$$

对 $b$：

$$
\frac{\partial L}{\partial b}
=\frac12(1-q)(q-p)
$$

- 若 $p>q$：$a$ 的系数为正 ⇒ $a=1$；$b$ 的系数为负 ⇒ $b=0$；
- 若 $p<q$：$a=0,\ b=1$。

⭐ 直观：**观测更像哪个状态的发射，就把转移概率全压到那个状态**。

### (c) 5 条长度 20 的序列，用什么算法？

**Baum-Welch（EM for HMM）**：没有标注、有隐状态 ⇒ 用前向-后向算法在 E-step 求 $\gamma,\xi$，M-step 更新 $\pi,T,$ emission。

## 3.3 Forward-Backward 与 Baum-Welch

**Forward**：

$$
\alpha_t(j)=p(x_{1:t},z_t=s_j)
=p(x_t\mid s_j)\sum_i\alpha_{t-1}(i)T(i,j)
$$

**Backward**：

$$
\beta_t(i)=p(x_{t+1:L}\mid z_t=s_i)
=\sum_j T(i,j)p(x_{t+1}\mid s_j)\beta_{t+1}(j)
$$

**Posterior（$\gamma$）**：

$$
\gamma_t(i)=p(z_t=s_i\mid x_{1:L})
=\frac{\alpha_t(i)\beta_t(i)}{\sum_j\alpha_t(j)\beta_t(j)}
$$

**Pairwise（$\xi$）**：

$$
\xi_t(i,j)=p(z_t=s_i,z_{t+1}=s_j\mid x_{1:L})
\propto \alpha_t(i)T(i,j)p(x_{t+1}\mid s_j)\beta_{t+1}(j)
$$

**M-step（Baum-Welch 更新）**：

$$
\pi_i^{\mathrm{new}}=\gamma_1(i),
\qquad
T_{ij}^{\mathrm{new}}
=\frac{\sum_{t=1}^{L-1}\xi_t(i,j)}{\sum_{t=1}^{L-1}\gamma_t(i)}
$$

$$
b_i(o)^{\mathrm{new}}
=\frac{\sum_{t:x_t=o}\gamma_t(i)}{\sum_{t=1}^{L}\gamma_t(i)}
$$

## 3.4 Viterbi（解码）

$$
\delta_1(i)=\pi_i\,p(x_1\mid s_i)
$$

$$
\delta_t(j)=\max_i\big[\delta_{t-1}(i)T(i,j)\big]\,p(x_t\mid s_j)
$$

回溯得到最可能路径。

## 3.5 Standard Markov model with emissions vs HMM

| 模型 | 状态可观测 | 状态不可观测 |
|---|---|---|
| Standard Markov with emissions | ✅（$z$ 与 $x$ 都给出） | — |
| HMM | — | ✅（只给 $x$） |

- 有标注 ⇒ 直接数转移；
- 无标注 ⇒ 似然要对所有状态路径求和（前向算法）⇒ EM/Baum-Welch。

---

# 4. 题型三 — Sampling 与 MCMC

## 4.1 Inverse CDF（逆变换采样）

若 $U\sim\mathrm{Unif}(0,1)$，令 $x=F^{-1}(u)$，则 $x\sim F$。

- 适用于 CDF 可解析求逆的分布（Exponential、Uniform 等）。

## 4.2 Rejection Sampling

目标 $p(x)=\tilde p(x)/Z$，proposal $q(x)$，常数 $M$ 使

$$
\tilde p(x)\le M q(x)\quad\forall x
$$

步骤：

1. 采样 $x\sim q$；
2. 采样 $u\sim\mathrm{Unif}(0,1)$；
3. 若 $u\le\dfrac{\tilde p(x)}{M q(x)}$ 则接受，否则拒绝。

**接受概率**：

$$
P(\text{accept})=\frac{1}{M}
$$

⭐ $M$ 越小越好（效率越高）；proposal 的 support 必须覆盖 target。

**真题（2023-24 S2 Q2a）**：$\tilde p(x)$ 是两段三角形；用**单个均匀分布**覆盖整个 support：

- $q(x)=\mathrm{Unif}(a,b)$，其中 $[a,b]$ 是 $\tilde p>0$ 的整个区间；
- $M=\max_x \tilde p(x)/q(x)= (b-a)\max\tilde p(x)$；
- 按上面的 1–3 步执行。

## 4.3 Importance Sampling

目标：

$$
\mathbb{E}_p[f(x)]=\int f(x)p(x)\,dx
$$

用 proposal $q$：

$$
\mathbb{E}_p[f(x)]
=\mathbb{E}_q\!\left[\frac{p(x)}{q(x)}f(x)\right]
\approx\frac1n\sum_i w_i f(x_i),
\qquad
w_i=\frac{\tilde p(x_i)/q(x_i)}{\sum_j\tilde p(x_j)/q(x_j)}
$$

- $q$ 的支撑要覆盖 $p$；
- $q$ 越接近 $p$，方差越小。

**真题（2023-24 S2 Q2c）**：用两个均匀分布的混合作为 proposal（按 15%/85% 质量分配到两段），采样后按权重加权求 $\mathbb{E}_p[\log\tilde p(x)]$。

## 4.4 MCMC：Metropolis-Hastings

目标 $\pi(x)$（可未归一化）。proposal $q(x,y)$。

**接受概率**：

$$
\boxed{\;A(x,y)=\min\left(1,\;
\frac{\tilde\pi(y)\,q(y,x)}{\tilde\pi(x)\,q(x,y)}
\right)\;}
$$

- 若 $q$ 对称（如 Gaussian random walk），$q$ 项消掉：

$$
A(x,y)=\min\left(1,\frac{\tilde\pi(y)}{\tilde\pi(x)}\right)
$$

**真题（2024-25 S2 Q2a）**：$\tilde\pi(x)=e^{-|x|}$，$q(x,y)=\mathcal{N}(y\mid x,1)$，$x=1,y=2$：

$$
A=\min\left(1,\frac{e^{-2}}{e^{-1}}\right)
=\min(1,e^{-1})=e^{-1}\approx0.368
$$

## 4.5 Gibbs Sampling

对每个变量 $z_i$，从其**全条件分布**采样：

$$
z_i^{(k)}\sim p(z_i\mid z_{-i},x)
$$

- 全条件可由联合分布求得：

$$
p(z_i\mid z_{-i})\propto p(z_1,\dots,z_d)
$$

- 坐标轮换更新；每轮用**已更新**的变量。

**真题（2024-25 S2 Q2b）**：手稿字符 $z_i\in\{D,U\}$，邻域耦合：

$$
p(z_i\mid z_{-i})\propto\gamma^{\mathbf 1[z_i=z_{i-1}]+\mathbf 1[z_i=z_{i+1}]}
$$

全条件：

$$
p(z_i=D\mid z_{-i},x_i)
\propto\gamma^{\mathbf 1[z_{i-1}=D]+\mathbf 1[z_{i+1}=D]}
\cdot\alpha^{\mathbf 1[x_i=D]}(1-\alpha)^{\mathbf 1[x_i=U]}
$$

（$U$ 同理，把 $D$ 换成 $U$、$\alpha$ 换成 $\beta$。）

## 4.6 Burn-in 与 Thinning

| 概念 | 含义 | 为什么用 |
|---|---|---|
| **Burn-in** | 丢弃链刚开始的若干样本 | 链还未收敛到 stationary distribution |
| **Thinning** | 每隔 $k$ 步保留一个样本 | 降低样本间的自相关 |

⭐ 简答题两三句话即可。

## 4.7 MCMC 对比表

| 方法 | 需要 proposal | 接受/拒绝 | 适用 |
|---|---|---|---|
| Rejection | 需要，且要有 $M$ | 有 | 低维、$M$ 好找 |
| Importance | 需要 $q$ | 无（加权） | 求期望 |
| MH | 需要 $q$ | 有 | 高维 posterior |
| Gibbs | 不需要 | 无（总接受） | 条件分布可采样 |

---

# 5. 题型四 — NN / CNN 计算

## 5.1 Softmax 与 cross-entropy

$$
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
$$

**Cross-entropy（one-hot $y$）**：

$$
L=-\sum_k y_k\ln p_k
$$

**Binary cross-entropy（BCE）**：

$$
L=-\big[y\ln\hat y+(1-y)\ln(1-\hat y)\big]
$$

## 5.2 真题（2025-26 S2 Q3）：CNN 计算

网络：

- 输入 $32\times32\times3$；
- Layer 1：8 个 $5\times5\times3$ filters，stride 1，no padding，ReLU；
- Layer 2：$2\times2$ max pooling，stride 2；
- Layer 3：16 个 $3\times3\times8$ filters，stride 1，no padding，ReLU；
- Layer 4：Flatten + FC(10) + softmax。

**(a) 各层输出尺寸**

$$
\text{L1: } (32-5+1)\times(32-5+1)\times8 = 28\times28\times8
$$

$$
\text{L2: } 28/2=14 \Rightarrow 14\times14\times8
$$

$$
\text{L3: } (14-3+1)\times(14-3+1)\times16 = 12\times12\times16
$$

**(b) 参数量**

$$
\text{L1}=8\times(5\cdot5\cdot3+1)=8\times76=608
$$

$$
\text{L3}=16\times(3\cdot3\cdot8+1)=16\times73=1168
$$

**(c) Flatten 维度与 FC 参数量**

$$
12\times12\times16=2304
$$

$$
\text{FC}=(2304+1)\times10=23050
$$

**(d) Softmax**：$z=[3,1,-3,0,\dots,0]$（10 个 logits）

$$
e^3=20.086,\quad e^1=2.718,\quad e^{-3}=0.050,\quad e^0=1\ (\times7)
$$

$$
\sum=20.086+2.718+0.050+7=29.854
$$

$$
p_1=\frac{20.086}{29.854}=0.673,
\qquad
p_2=\frac{2.718}{29.854}=0.091
$$

## 5.3 真题（2024-25 S2 Q3）：BCE 与 SGD

**(a) BCE**：$Y=1,\ \hat y=0.85$

$$
L=-[1\cdot\ln0.85+0]=-\ln0.85\approx0.1625
$$

**(b) SGD 更新**：$w=0.04$，$\partial L/\partial w=0.45$，$\eta=0.1$

$$
w\leftarrow w-\eta\frac{\partial L}{\partial w}
=0.04-0.1\times0.45=0.04-0.045=-0.005
$$

## 5.4 真题（2024-25 S2 Q4）：卷积手算

输入 $7\times7$，filter $3\times3$，stride 1，no padding：

$$
(7-3+1)\times(7-3+1)=5\times5
$$

$$
W=\begin{bmatrix}1&0&-1\\1&0&-1\\1&0&-1\end{bmatrix}
$$

左上角输出（第 1 行第 1 列）取输入 $3\times3$：

$$
\begin{bmatrix}1&2&3\\8&9&10\\15&16&17\end{bmatrix}
$$

$$
(1-3)+(8-10)+(15-17)=-2-2-2=-6
$$

第 1 行第 2 列：

$$
\begin{bmatrix}2&3&4\\9&10&11\\16&17&18\end{bmatrix}
\Rightarrow (2-4)+(9-11)+(16-18)=-6
$$

⭐ 该 filter 是**竖直边缘检测器**（左列 +1、右列 −1）。

## 5.5 通用公式

$$
W_{out}=\frac{W_{in}-F+2P}{S}+1
$$

$$
\text{params}=F\cdot F\cdot C\cdot D+D
$$

$$
\text{FC params}=(\text{flatten dim}+1)\times\text{output dim}
$$

---

# 6. 题型五 — ReLU 网络理论

## 6.1 网络形式

$$
f(x)=\sum_{i=1}^{m}v_i\,\phi(w_ix+b_i)+c,
\qquad
\phi(z)=\max(0,z)
$$

- 每个隐藏神经元贡献一个 **ReLU**；
- 输出层线性（$c$ 为输出 bias）。

## 6.2 图形与 kink

- 每个 ReLU 在 $w_ix+b_i=0$（即 $x=-b_i/w_i$）处**斜率突变**；
- 因此 $f(x)$ 是**分段线性函数**，最多 **$m$ 个 kink**（若多个 kink 重合则更少）；
- 两段之间斜率恒定。

**真题（2025-26 S2 Q4a,b）**：描述图形时说明：在 $x=-b_i/w_i$ 处可能突然变斜率；每个隐藏神经元最多贡献一个 kink，所以 $f$ 最多 $m$ 个突变点。

## 6.3 用 ReLU 构造 $\lvert x\rvert$（$m=2$）

$$
f(x)=\mathrm{ReLU}(x)+\mathrm{ReLU}(-x)
$$

取：

$$
w_1=1,\ b_1=0,\ v_1=1;
\qquad
w_2=-1,\ b_2=0,\ v_2=1;
\qquad
c=0
$$

验证：

- $x\ge0$：$f=x+0=x$；
- $x<0$：$f=0+(-x)=-x$。

⇒ $f(x)=|x|$。

## 6.4 万能逼近与线性激活的失败

**(a) 为什么增加 $m$ 能逼近 $x^2$**：

- ReLU 网络是**分段线性**的；
- $m$ 越大，分段越多，可以用**折线**任意逼近连续函数（universal approximation）；
- 在 $[-1,1]$ 上，用足够多的小线段逼近抛物线。

**(b) 若 $\phi(z)=z$（线性激活）**：

$$
f(x)=\sum_i v_i(w_ix+b_i)+c
=\Big(\sum_i v_iw_i\Big)x+\Big(\sum_i v_ib_i+c\Big)
=Ax+B
$$

无论 $m$ 多大，$f$ 都只是**一条直线**，无法逼近 $x^2$（除非 $x^2$ 本身是直线）。

⭐ 结论：**非线性激活是深度网络表达能力的必要条件**。

## 6.5 一层隐藏层能表示什么（Week 13 例题）

| 函数 | 能否精确表示 | 理由 |
|---|---|---|
| 一次多项式 | ✅ | 线性神经元即可 |
| Hinge loss $\max(1-x,0)$ | ❌ | 线性 + 阶跃组合无法表示带尖角的分段线性 |
| 二次多项式 | ❌ | 只能得到带尖角的分段函数，无法光滑 |
| 分段常数 | ✅ | 每个方波 = 两个阶跃相减 |

---

# 7. 题型六 — 概念判断与简答（T/F）

> 2025-26 S2 Q1(a) 一次考了 3 条 T/F，每条要**判断 + 说明理由**。以下汇总高频判断点。

| 陈述 | 判断 | 理由 |
|---|---|---|
| 给定 pdf，MLE 就是让 likelihood 最大的参数 | ✅ | 定义 |
| K-means 更新 cluster center 时随机选一个点 | ❌ | 取该簇所有点的**均值** |
| 用 $\mathrm{Unif}(-1,1)$ 作为 $\mathcal N(0,1)$ 的 proposal 做 rejection sampling | ❌ | proposal 的 support 必须覆盖 target 的整个 support；Gaussian 在 $(-1,1)$ 外仍有质量 |
| MLE 一定无偏 | ❌ | MLE 只是渐近有效，有限样本可能有偏（如方差估计） |
| MAP 在 uniform prior 下等于 MLE | ✅ | 先验常数不影响 argmax |
| EM 的 log-likelihood 每步单调不降 | ✅ | EM 的基本性质 |
| Baum-Welch 是有监督学习 | ❌ | 无标注，是 EM |
| Gibbs sampling 需要计算接受率 | ❌ | 全条件采样，总接受 |
| MH 的 proposal 必须对称 | ❌ | 非对称时用 $q(y,x)/q(x,y)$ 修正 |
| ReLU 网络是分段线性函数 | ✅ | 有限个 ReLU 之和 |
| 线性激活的多层网络等价于单层 | ✅ | 复合仍是线性 |
| Dropout 在测试时随机丢神经元 | ❌ | 测试时不丢（或用期望/缩放） |
| BatchNorm 在训练和测试时行为相同 | ❌ | 测试用 running statistics |
| CNN 的卷积层参数比同尺寸 FC 少 | ✅ | 参数共享 |
| 池化层有可学习参数 | ❌ | 无参数 |
| Softmax 输出之和为 1 | ✅ | 归一化 |
| Cross-entropy 可以配合 softmax 求导简化 | ✅ | $\partial L/\partial z=p-y$ |
| GAN 的 discriminator 输出是类别概率 | ✅ | 真/假 |
| 数据增强对 GAN 训练总是有帮助 | ❌ | 某些增强（如翻转）会改变语义（如字符/octopus 方向） |
| 过拟合时训练误差低、测试误差高 | ✅ | 定义 |

---

# 8. Week 13 官方复习课例题（Part 2 必看）

> `Part 2.4 Examples & Reviews` 是 Wang Lipo 亲自给的复习课，题目风格=考试风格。

## 8.1 单神经元 OR / AND

- OR：$W=[1,1]^T$，取边界过 $(0,0.5)$ ⇒ $b=-0.5$；
- AND：$W=[1,1]^T$，取边界过 $(1.5,0)$ ⇒ $b=-1.5$。

⭐ 边界方向由 $W$ 决定，位置由 $b$ 决定；$W,b$ 同乘常数边界不变。

## 8.2 3 层网络设计

- 第 1 隐藏层 4 个神经元 → 4 条边界；
- 第 2 隐藏层 2 个神经元 → 两个 AND；
- 输出层 → OR；
- 用 **0 权重屏蔽**无关连接。

## 8.3 Gradient Descent 四步

1. 初始化 $\theta_0$；
2. 算 $\nabla L(\theta)$；
3. 更新 $\theta_{\mathrm{new}}=\theta_{\mathrm{old}}-\alpha\nabla L$；
4. 重复直到收敛。

## 8.4 训练曲线诊断

| 现象 | 判断 | 措施 |
|---|---|---|
| train/val 都上升，gap 小 | 没训够 | 训练更久 |
| train 升、val 降，gap 大 | overfitting | 正则、更多数据、augmentation、early stopping |
| 两边都低、无 gap | underfitting | 更复杂模型、训练更久 |

## 8.5 CNN 计算（复习课例题）

输入 $32\times32\times3$，10 个 $5\times5$ filters，stride 1，pad 2：

- 输出 $32\times32\times10$；
- 每个 filter $5\cdot5\cdot3+1=76$ ⇒ 总 **760** 参数。

## 8.6 100 层网络权重不更新

- **Vanishing gradient**；
- 加数据/调 learning rate **无效**；
- 解法：**Leaky ReLU**、**BatchNorm**（让 tanh 落在线性区）、残差连接。

## 8.7 Linear regression 手算

三点 $(1,1),(2,2),(3,1)$：对称 ⇒ 水平线 $y=b$；

$$
e=\frac13[2(b-1)^2+(b-2)^2],
\qquad
b=\frac43,
\qquad
e=\frac29\approx0.222
$$

---

# 9. A4 Reference Sheet 双面模板

> 考试只允许**一张双面 A4**。建议**按"公式 + 触发词"排版**，不要抄概念解释。

## 9.1 Side 1 — 概率与推断

```
【分布】Bernoulli/Binomial/Categorical/Multinomial/Gaussian/Beta/Dirichlet/Uniform/Exponential 的 pdf 与归一化常数

【MLE】
Bernoulli: θ̂ = r/n
Gaussian: μ̂ = x̄, σ̂² = (1/n)Σ(xi−μ̂)²
Exponential: λ̂ = n/Σxi
截断几何: θ̂ = (Σxi−n)/(Σxi−n_{r+1})

【MAP】
Beta-Bernoulli: (r+a−1)/(n+a+b−2)
Gamma-Exponential: (n+α−1)/(Σxi+β)

【EM】
Q(θ|θ⁽ᵗ⁾)=E_{z|x,θ⁽ᵗ⁾}[ln p(x,z|θ)]
E-step: responsibilities
M-step: 最大化 Q

【GMM】
r_ik = πk N(xi|μk,Σk) / Σj πj N(xi|μj,Σj)
πk=Σr/n, μk=Σr x/Σr, Σk=Σr(x−μ)(x−μ)ᵀ/Σr

【HMM】
joint: π(z1)p(x1|z1)Π T(z_{t−1},z_t)p(x_t|z_t)
α, β, γ, ξ 公式
Baum-Welch: π=γ1, T=Σξ/Σγ, b=Σγ·1[x=o]/Σγ

【Sampling】
rejection: accept if u ≤ p̃(x)/(M q(x)); P(accept)=1/M
importance: w=p̃/q, normalize
MH: A=min(1, π(y)q(y,x)/(π(x)q(x,y)))
Gibbs: z_i ~ p(z_i|z_{−i})
```

## 9.2 Side 2 — 深度学习

```
【激活】sigmoid, tanh, ReLU, Leaky ReLU 及导数
【前向】o=Wᵀx+b, h=f(o)
【Loss】MSE, CE, BCE, softmax+CE
【Backprop】δ_out, δ_hidden, 梯度公式
【优化】GD/SGD/momentum/Adam
【正则】L1/L2, dropout, early stopping, BN
【CNN】
out=(W−F+2P)/S+1
params=F²C·D+D
pool 无参数
flatten=H·W·C
FC=(flatten+1)·out
【ReLU 网络】
f=Σvi ReLU(wix+bi)+c
kink at x=−bi/wi；≤m 个 kink
|x|=ReLU(x)+ReLU(−x)
线性激活 ⇒ 直线
```

⭐ 建议：**先写公式，再写适用条件/触发词**（如 "mixture → EM"、"latent → Baum-Welch"）。

---

# 10. 公式速查表

## 10.1 概率与估计

$$
p(\theta\mid D)\propto p(D\mid\theta)p(\theta)
$$

$$
\ell(\theta)=\sum_i\ln p(x_i\mid\theta)
$$

$$
\hat\theta_{\mathrm{MLE}}=\arg\max_\theta \ell(\theta)
$$

$$
\hat\theta_{\mathrm{MAP}}=\arg\max_\theta\big[\ell(\theta)+\ln p(\theta)\big]
$$

## 10.2 EM / GMM

$$
Q(\theta\mid\theta^{(t)})=\mathbb E_{z\mid x,\theta^{(t)}}[\ln p(x,z\mid\theta)]
$$

$$
r_{ik}=\frac{\pi_k\mathcal N(x_i\mid\mu_k,\Sigma_k)}{\sum_j\pi_j\mathcal N(x_i\mid\mu_j,\Sigma_j)}
$$

## 10.3 HMM

$$
\alpha_t(j)=p(x_t\mid s_j)\sum_i\alpha_{t-1}(i)T(i,j)
$$

$$
\beta_t(i)=\sum_jT(i,j)p(x_{t+1}\mid s_j)\beta_{t+1}(j)
$$

$$
\gamma_t(i)=\frac{\alpha_t(i)\beta_t(i)}{\sum_j\alpha_t(j)\beta_t(j)}
$$

## 10.4 Sampling / MCMC

$$
P(\text{accept})=\frac1M
$$

$$
w_i=\frac{\tilde p(x_i)/q(x_i)}{\sum_j\tilde p(x_j)/q(x_j)}
$$

$$
A(x,y)=\min\left(1,\frac{\tilde\pi(y)q(y,x)}{\tilde\pi(x)q(x,y)}\right)
$$

## 10.5 NN / CNN

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

$$
f(x)=\sum_i v_i\max(0,w_ix+b_i)+c
$$

---

# 11. 模拟卷（4 题）

> 按三套真题的题型自编，限时 **2 小时**、闭卷（仅 A4）。

## Q1（25 分）

某设备寿命 $x\in\{1,\dots,r+1\}$，pmf 为

$$
p(x=k)=\theta^{k-1}(1-\theta)\ (k\le r),
\qquad
p(x=r+1)=\theta^r
$$

观测 $n$ 个样本，$n_k$ 为取 $k$ 的个数。

(a) 写出 log-likelihood（用 $n_k$ 表示）。（8 分）
(b) 求 MLE $\hat\theta$。（8 分）
(c) 若先验 $p(\theta)\propto\theta^{a-1}(1-\theta)^{b-1}$，求 MAP。（9 分）

## Q2（25 分）

HMM：$\pi=(1/2,1/2)$，$T=\begin{bmatrix}a&1-a\\1-b&b\end{bmatrix}$，发射概率 $p(o_1|s_1)=p,\ p(o_1|s_2)=q$。

(a) 写出观测序列 $(o_1,o_1)$ 的 likelihood。（10 分）
(b) 若 4 条标注序列的转移为 $s_1\to s_1$、$s_1\to s_2$、$s_2\to s_2$、$s_2\to s_1$，求 $a,b$ 的 MLE。（7 分）
(c) 若只有未标注序列，说明用什么算法及 E/M 步各做什么。（8 分）

## Q3（25 分）

输入 $16\times16\times3$；CONV3-16（pad 1, stride 1）→ ReLU → POOL2（2×2, stride 2）→ CONV3-32（pad 1, stride 1）。

(a) 写出每层输出尺寸。（8 分）
(b) 计算两层卷积的参数量。（8 分）
(c) Flatten 后接 FC-10，求 flatten 维度与 FC 参数量。（5 分）
(d) 给 logits $[2,0,-1]$，求 softmax 概率（3 位小数）。（4 分）

## Q4（25 分）

单隐藏层 ReLU 网络：

$$
f(x)=\sum_{i=1}^{m}v_i\max(0,w_ix+b_i)+c
$$

(a) 解释为什么 $f$ 是分段线性的，kink 在哪里，最多几个。（8 分）
(b) 用 $m=2$ 构造 $f(x)=|x|$，给出参数。（8 分）
(c) 说明为什么增加 $m$ 能逼近 $x^2$；若改成线性激活会怎样。（9 分）

## 11.1 答案要点

### Q1

(a)

$$
\ell(\theta)=\Big(\sum_i x_i-n\Big)\ln\theta+(n-n_{r+1})\ln(1-\theta)
$$

(b)

$$
\hat\theta=\frac{\sum x_i-n}{\sum x_i-n_{r+1}}
$$

(c) 加先验后：

$$
\ell_{\mathrm{post}}=\Big(\sum x_i-n+a-1\Big)\ln\theta
+\big(n-n_{r+1}+b-1\big)\ln(1-\theta)
$$

$$
\hat\theta_{\mathrm{MAP}}
=\frac{\sum x_i-n+a-1}{\sum x_i-n_{r+1}+a+b-2}
$$

### Q2

(a)

$$
L=\frac12\Big[(1-p)\big(ap+(1-a)q\big)+(1-q)\big((1-b)p+bq\big)\Big]
$$

（只保留 $o_1$ 的发射项；若序列为 $(o_1,o_1)$，把 $1-p,1-q$ 换成 $p,q$。）

(b) $\hat a=\hat b=1/2$。

(c) Baum-Welch：E-step 前向-后向求 $\gamma,\xi$；M-step 更新 $\pi,T,b$。

### Q3

输入 $16\times16\times3$：

- CONV3-16, pad1, stride1 → $16\times16\times16$，参数 $16(3\cdot3\cdot3+1)=448$；
- POOL2 → $8\times8\times16$；
- CONV3-32, pad1 → $8\times8\times32$，参数 $32(3\cdot3\cdot16+1)=4640$；
- Flatten $=8\cdot8\cdot32=2048$；FC-10 参数 $2049\times10=20490$；
- Softmax $[2,0,-1]$：$e^2=7.389,e^0=1,e^{-1}=0.368$，和 $=8.757$，$p=[0.844,0.114,0.042]$。

### Q4

(a) 每个 ReLU 在 $x=-b_i/w_i$ 处斜率突变；$m$ 个神经元最多 $m$ 个 kink。
(b) $w_1=1,b_1=0,v_1=1$；$w_2=-1,b_2=0,v_2=1$；$c=0$。
(c) 分段线性折线可逼近连续函数；线性激活时 $f(x)=Ax+B$，只是一条直线。

---

# 12. 考前 2 天计划

| 时间 | 内容 | 目标 |
|---|---|---|
| 第 1 天上午 | MLE / MAP / EM：把 Q1 的三类分布各推一遍 | 闭卷写出 log-likelihood 与解 |
| 第 1 天下午 | HMM：joint、likelihood、Baum-Welch、Viterbi | 能写前向/后向与更新公式 |
| 第 1 天晚上 | Sampling / MCMC：rejection、importance、MH、Gibbs | 会写接受率与全条件 |
| 第 2 天上午 | NN/CNN：shape、params、softmax、CNN 手算 | 10 分钟算完 Q3 |
| 第 2 天下午 | ReLU 理论 + Week 13 例题 + 概念 T/F | 简答不丢分 |
| 第 2 天晚上 | 模拟卷（限时 2 小时）＋ 检查 A4 sheet | 查漏补缺 |

**考场策略**：

1. **先写会做的计算题**（MLE、CNN 计算最稳）；
2. **推导题写清每一步**（log-likelihood、求导、令零）；
3. **概念题写"定义 + 理由 + 一句结论"**，不要空；
4. **A4 sheet 上优先写**：分布 pdf、MLE/MAP 结果、EM/HMM 公式、MH 接受率、CNN 公式、ReLU 性质；
5. 时间：每题 **25–30 分钟**，留 10 分钟检查。

---

> **最后提醒**：Week 13 的 `Part 2.4 Examples & Reviews` 是官方复习课，里面的例题（OR/AND、3 层网络、GD、训练曲线、CNN 参数、vanishing gradient、linear regression）**必须会**；Part 1 的 MLE/MAP/EM/HMM/Sampling/MCMC 每年都在 Q1/Q2 出现，**不要只复习 Part 2**。
