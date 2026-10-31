# EE6497 — Pattern Recognition and Deep Learning（模式识别与深度学习）

> 课程学习笔记总览。每周一节，按周总结重点内容。
> 第一周（开课周）特别关注考核要求、考勤、quiz、期末等行政性信息。
>
> **权威来源说明**：本笔记先由 `week1/week1.txt` 录播转写整理，再以 `week1/1_Introduction.pdf`（官方课件）和 `week1/Week 1.pdf`（标注讲义，AY26-27-S1，2026-07-28）核对修正。转写有较多语音识别噪声，以 PDF 为准。

---

## Week 1 — 开课周：课程介绍 + 概率论复习

### 1. 课程基本信息

- **课程名称**：EE6497 Pattern Recognition and Deep Learning
- **课程定位**：模式识别 + 机器学习 + 深度学习。前半学期偏模式识别（理论、概率建模），后半学期偏深度学习（神经网络）。
- **任课教师**（以 PDF 为准）：
  - **前 7 周（Week 1–7）**：**Tay Wee Peng**（wptay@ntu.edu.sg），负责模式识别/概率建模部分。
  - **后 6 周（Week 8–13，recess week 之后）**：**Wang Lipo**（elpwang@ntu.edu.sg），负责深度学习 / AI 架构部分。
- **授课形式**：Week 1 因节假日改为 Teams 线上，Week 2 起恢复 LT 线下面授。录像会传到 **NTULearn** 平台。
- **课程特点**：与其他 ML 课程（EE6483、EE4414、EE6405/6406/6407 等）相比，本课**重在概念与底层理论**（概率方法、可解释模型、数学推导），而非单纯套用架构解决问题。可视为其他 ML 课程的"入门/理论先导课"。

### 2. ⭐ 考核要求（重要，MSC/研究生 EE6497 适用）

| 成分 | 占比 | 说明 |
|---|---|---|
| **Final Exam 期末** | **60%** | 带一张双面 A4 参考页（reference sheet），可手写任意公式，无需死记 |
| **Quiz ×2** | 10% 各，共 20% | 同样可带 A4 reference sheet |
| **Homework ×2** | 5% 各，共 10% | 不允许迟交（no late submission）；提交为**单个 PDF** |
| **Class Participation 课堂参与** | 5% | 见下方考勤说明 |
| **Survey Report 调研报告** | 5% | 期末提交 |

> UG 本科生另有单独的评分表，比例不同。

#### 关键时间节点

- **Homework 1**：约在 **Week 5** 在线提交（通过系统提交 PDF）。Homework 2 在后半学期约 **Week 11**；Quiz 2 约 **Week 12**，覆盖 Week 8–11；Survey Report（仅 PG）约 **Week 13**。
- **Quiz（前半学期唯一一次）**：**Week 7**，覆盖 **Week 1–4** 内容。
  - 形式：**在线 quiz，但需到 lecture theater 现场完成**（需自带 laptop/tablet）。
  - 通过 **NTULearn** 完成。无有效 LOA/MC 缺考记 0 分。

#### ⭐ 考勤 / Class Participation（5%，PG；UG 为 10%）

- 使用 **Wooclap**（课堂答题平台）进行随堂答题。
- 全学期共约 **13 次讲座**，**参加 ≥9 次并提交 Wooclap 答案** 即可拿到满分。
- **只要提交答案就算一次参与，答错不扣分**（attempt 即计分，不要求正确）。
- ⚠️ 必须通过 **NTULearn** 登录 → 课程页面 → Wooclap 链接进入，否则系统无法识别你的账号、无法记录出勤。
- 即使不答对，只要 attempt 即可，**鼓励每题都尝试**。

### 3. 学习要求与先修知识

- **数学**：基础微积分（derivative、partial derivative、求极值）、概率论（PDF、PMF、expectation、variance、covariance）。
- **概率论薄弱**：建议修 EE7401（概率理论，周四晚，覆盖基础）。
- **Python**：前半学期不作为考核重点（不考 Python 代码）；后半学期（Prof. Wang Lipo）可能要求解释/讨论代码。课程提供示例 Python notebook 供参考，但不细讲。
- **练习题（Practice Problems）**：每周课件末附有练习题，附解答（蓝色标注）。**先自己做再看答案/问 AI**，理解而非死记。
- **学习态度**：老师强调先独立思考解题，再借助 AI（如 NTU 提供的 Gemini），重点是从中学习，理解为什么。

### 4. 教材（官方引用，见课件致谢页）

1. **[B07] Christopher Bishop, *Pattern Recognition and Machine Learning*, Springer, 2007**（主教材，课程材料大量取自本书）。
2. **[M12] Kevin P. Murphy, *Machine Learning: A Probabilistic Perspective*, MIT Press, 2012**（部分 Python 代码取自本书，见 https://github.com/probml/pyprobml，略有修改）。
3. **[HTF09] T. Hastie, R. Tibshirani, J. Friedman, *The Elements of Statistical Learning*, Springer, 2009**（部分数据取自本书）。
- 补充材料（supplementary）仅供参考，**不考**。

### 5. 机器学习三大类别（课程内容概览）

- **Supervised Learning 监督学习**：有标签（ground truth）。
  - 分类（classification）：如 MNIST 数字识别（0–9）、AV 目标检测/识别。
  - 回归（regression）：y 为任意实数（温度、湿度等）。
- **Unsupervised Learning 无监督学习**：无标签。
  - 聚类（clustering）：按相似性分组。
  - 潜在因子（latent factors）：如人脸 = 若干 latent face 的线性组合，降维建模。
  - 相关与结构学习（correlation / structure learning）。
- **Reinforcement Learning**：课程提及较少。

### 6. 概率论复习（本周核心知识内容）

#### 6.1 随机变量与 PDF

- 用随机变量建模输入特征 x 与输出 y（均视为随机）。
- **PMF**（离散）/ **PDF**（连续）。PMF 可视为 PDF 的特例。
- PDF 曲线下面积 = 区间概率；PDF 积分恒 = 1（归一化）。
- 输入与输出联合分布 → 联合 PDF（joint PDF）。

#### 6.2 常见分布

- **Bernoulli 伯努利**：x ∈ {0,1}，P(x=1)=θ，P(x=0)=1−θ。紧凑写法：θ^x(1−θ)^(1−x)。可用 indicator function 写更一般形式（如 x∈{−1,+1}）。
- **Uniform 均匀**：区间 [a,b] 上高度 1/(b−a)。
- **Exponential 指数**：θe^(−θx)。
- **Categorical**（伯努利的 K 类推广）：参数 θ₁..θ_K，∑θ=1，θ≥0。indicator 函数紧凑写法。

#### 6.3 重要性质与公式

- **Marginal 边缘 PDF**：积分消去不关心的变量。
- **Conditional PDF**：p(y|x) = p(x,y)/p(x)。
- **联合 PDF 链式分解**：p(x,y,z)=p(x)·p(y|x)·p(z|x,y)。
- **⭐ Bayes' Rule 贝叶斯公式**：p(θ|x) = p(x|θ)p(θ) / p(x)。常用于把"对 y 的条件"转成"对 x 的条件"，因为很多场景下 p(x|θ) 比 p(θ|x) 更容易算。分母 p(x) 不依赖 θ，求 θ 最优值时常可忽略（∝）。
- **Independence 独立**：x,y 独立 ⇒ p(x,y)=p(x)p(y)，且条件 = 边缘。
- **IID 假设**：训练/测试数据独立同分布。联合 PDF = 各点 PDF 之积；取 log 后变求和（便于计算，且 log 单调，不改变最优解）。
- **Expectation 期望**：E[f(x)]；线性性 E[x+y]=E[x]+E[y]，E[cx]=cE[x]；独立 ⇒ E[xy]=E[x]E[y]。
- **Conditional Expectation**：条件下的期望，PDF 换为条件 PDF。
- **Variance 方差**：Var(x)=E[(x−E[x])²]=E[x²]−(E[x])²。
- **Covariance 协方差**：Cov(x,y)=E[xy]−E[x]E[y]。
  - 独立 ⇒ Cov=0（不相关）；但 **Cov=0 ⇏ 独立**（有反例）。
  - Var(x+y)=Var(x)+Var(y)+2Cov(x,y)。

#### 6.4 向量/矩阵情形

- x 为高维随机向量（如 256×256×3 图像展平）。
- expectation：对各分量分别求。
- **Covariance matrix Σ_x** = E[(x−μ)(x−μ)ᵀ]，主对角为各分量方差，其余为分量间协方差。
- **Cross-covariance**：两向量间协方差矩阵 Σ_xy。
- 矩阵/向量求导公式（如 ∂(aᵀx)/∂x = a 等）可直接查表使用，不必死记、不必自己推导。

#### 6.5 Parametric vs Non-parametric Models

- **Parametric 参数模型**：假设分布形式已知，参数 θ 固定维数未知，用数据估计最优 θ。训练快、需做分布假设。本课前半主要讲这类。
- **Non-parametric 非参数模型**：参数数量可随数据量增长（"非参数"=不限定参数个数），更灵活但大数据下可能不可解（如聚类数随数据变化）。

#### 6.6 ⭐ 后验、似然、先验、共轭先验（核心概念）

- 用 Bayes rule 推参数 θ 的后验：
  - posterior p(θ|x) ∝ **likelihood** p(x|θ) · **prior** p(θ)。
  - **likelihood 似然**：给定 θ 时观测到 x 的可能性。
  - **prior 先验**：观测前对 θ 的信念（如设计者已知参数大致范围）。
  - 分母 p(x) 是归一化常数，常可忽略；PDF 只需知道"函数形式"（∝），常数可由归一化唯一确定。
- **Conjugate Prior 共轭先验**：选 prior 使 prior × likelihood 得到的 posterior 仍与 prior 同分布族。
  - 好处：可写出解析闭式后验，易于计算与解释（参数被"更新"）。
  - 缺点：特殊情况才成立，不够灵活；不满足时 → Week 6 用 MCMC。
  - **典型共轭对**：
    - Bernoulli / Binomial 的似然 → **Beta 先验**。
    - Categorical 的似然 → **Dirichlet 先验**。
    - Gaussian 似然（对均值 μ）→ **Gaussian 先验**。

#### 6.7 Bernoulli + Beta 共轭（推导示例）

- 单次观测：prior Beta(a,b) → posterior Beta(x+a, 1−x+b)。
- N 次 IID 观测：posterior 参数更新为
  - new_a = (sum of x_i) + a
  - new_b = (N − sum of x_i) + b
- 解释：先验"计数" a,b 被观测计数更新。

#### 6.8 ⭐ Gaussian 分布（最重要）

- PDF：指数上有 x 的二次型；钟形曲线，μ 为均值，σ² 为方差。
- μ=0, σ²=1 → 标准正态（standard normal）。
- 性质：
  - 仿射变换：aX+b 仍正态，mean=aμ+b, var=a²σ²。
  - 任意正态 = σ·(标准正态) + μ。
  - **独立正态之和仍正态**（mean、variance 各自相加）——其他分布无此性质。
- **Multivariate / Joint Gaussian 多元高斯**：任意线性组合 aᵀx 都是一维高斯 ⇒ x 联合高斯。
  - 构造：x = Az + μ，z 为 IID 标准正态 ⇒ x 联合高斯，均值 μ，协方差 AAᵀ。
  - 二元情形：相关系数（correlation）控制 PDF 形状/倾斜；不相关且等方差 → 圆对称；相关增大 → 沿对角拉长/倾斜。
- 识别技巧：PDF 指数上是 θ 的二次型 ⇒ 必为高斯（配方可得 μ、σ²）。

### 7. 本课整体进度表（权威，取自课件 Course Content 页）

| Week | Topic | CA（due） |
|---|---|---|
| 1 | Introduction, Probability Review | — |
| 2 | Bayesian Inference | — |
| 3 | Mixture Models and the EM Algorithm | — |
| 4 | Markov Models and Hidden Markov Models | — |
| 5 | Sampling | **Homework 1** |
| 6 | Markov Chain Monte Carlo (MCMC) | — |
| 7 | Summary | **Quiz 1（覆盖 Week 1–4）** |
| — | *Recess* | — |
| 8 | Neural Networks | — |
| 9 | Deep Learning (CNN) | — |
| 10 | Training Deep Networks | — |
| 11 | Training Deep Networks | **Homework 2** |
| 12 | Deep Network Architectures | **Quiz 2（覆盖 Week 8–11）** |
| 13 | Applications | **Survey Report（仅 PG）** |

> 第一半（概率参数模型，可解释、易训练、工业仍常用）→ 第二半（loss-based 深度网络）。求最优参数：前半用 MLE/MAP、EM、Baum-Welch、MCMC；后半用 loss + 梯度下降。评估时度量 accuracy / precision / recall 等。

### 8. 其他提示

- 老师可邮件联系（wptay@ntu.edu.sg），也鼓励在 Wooclap/平台讨论区提问，让同学共同受益。
- 兼职本科生可随时联系老师寻求额外帮助。
- 选课注册问题走 program office 申诉，教授无法直接加人；本学期注册不到可下学期再选（下学期本科生优先）。
- NTU 提供付费版 Gemini 供学生用于学习。
- 老师研究方向：信号处理与图网络机器学习（molecules/交通/社交网络）、AV 视觉定位（与 Continental Automotive 合作）；其 2024 模型用到本课将学的 Bayes inference、EM、MCMC + 图神经网络。

---

## Week 2 — Bayesian Inference（MLE / MAP）

> **权威来源说明**：本节先由 `week2/week2.txt` 录播转写整理，再以 `week2/2_Bayesian_Inference.pdf`（官方课件，38 页）核对修正。转写噪声较多（如 "data" 实为参数 θ、"ads" 实为 x、"five" 实为设计矩阵 Φ、"pyro/pr" 实为 prior、"livelihood/lilihood/hod/Lightho" 实为 likelihood、"gaucin/galsiu/g" 实为 Gaussian、"Bn/Berny/Bernov/nudi" 实为 Bernoulli、"n one/n zero" 实为 N₁/N₀、"Psych learn" 实为 scikit-learn），以 PDF 为准。

### 1. 本周主线

Week 1 复习了概率论与参数模型（parametric model）的概念：假设分布形式已知、参数 θ 未知、用数据估计最优 θ。本周回答核心问题——**如何确定"最优"的 θ？** 引出两条估计准则：

- **MLE（Maximum Likelihood Estimation，极大似然估计）**：只用数据 D，找使 likelihood 最大的 θ。
- **MAP（Maximum A Posteriori，最大后验估计）**：在 MLE 基础上加入 prior（先验），找使 posterior 最大的 θ。

二者都源自 Bayesian inference（贝叶斯推断）框架。

### 2. Likelihood Model（似然模型）

- 训练数据 D = {x₁,…,xₙ}，假设 **IID**（独立同分布）。
- likelihood function（似然函数）：p(D|θ)，即在"θ 已知"的前提下观测到 D 的概率，衡量模型对数据的拟合程度。
  - 注意视角切换：θ 是变量时 p(D|θ) 叫 likelihood；x 是变量时同一个式子叫 PDF。本周固定 D，把 θ 当变量求最大。
- IID ⇒ 联合 likelihood = 各点之积；取 log 后变求和：

$$
\log p(D|\theta) = \sum_{i=1}^{n}\log p(x_i|\theta)
$$

log 是单调函数，不改变 argmax 的最优解，但把乘积变求和，大大简化推导——这是"为什么可以用 log"的标准答案。

**三种典型 likelihood model（取自课件）：**

| 分布 | 参数 | likelihood p(D\|θ) |
|---|---|---|
| Bernoulli | θ∈[0,1] | θ^{N₁}(1−θ)^{N₀}，N_k=Σ 1{x_i=k} |
| Exponential | λ>0 | λⁿ exp(−λ Σx_i) |
| Gaussian | θ=(μ,σ²) | (2πσ²)^{−n/2} exp[−Σ(x_i−μ)²/(2σ²)] |

例：D={0,1,1,0,1,1,1,0,1,1}，N₁=7，N₀=3，则 p(D|θ)=θ⁷(1−θ)³；θ=0.6 时 p(D|θ)=0.6⁷·0.4³，反映"θ=0.6 生成该数据"的可能性。

### 3. MLE 定义与求法

$$
\theta_{ML}=\arg\max_\theta p(D|\theta)
$$

通用求法：对 log-likelihood 求导（derivative）、令其为零、解方程（依赖 concavity / 凹凸性保证是最大值）。

#### 3.1 Bernoulli MLE

$$
\log p(D|\theta)=N_1\log\theta + N_0\log(1-\theta)
$$

对 θ 求导令零：

$$
\frac{N_1}{\theta_{ML}}-\frac{N_0}{1-\theta_{ML}}=0
\;\Rightarrow\;
\theta_{ML}=\frac{N_1}{N_0+N_1}=\frac{N_1}{n}
$$

例 N₁=7, N₀=3 ⇒ θ_ML=0.7。直觉：用"1 出现的频率"估计 θ。

#### 3.2 Exponential MLE

$$
\log p(D|\lambda)=n\log\lambda-\lambda\sum_{i=1}^{n}x_i
$$

求导令零：n/λ_ML = Σx_i ⇒ λ_ML = n / Σx_i。

例 D={0.15, 0.28, 0.23, 0.14, 0.35}, n=5, Σx=1.15 ⇒ λ_ML = 5/1.15 ≈ 4.35。

#### 3.3 不可导情形（Wooclap 示例）

某自定义分布的 log-likelihood 含绝对值 |θ−y|，对 θ 不可导（non-differentiable）。此时最大化等价于最小化 |θ−y|，最小值为 0，在 **θ=y** 取得。结论：单观测下 θ_ML = y。这类情况不能用"求导令零"，改用直接分析目标函数的极值。

### 4. KL Divergence 视角（Supplementary，不考但帮助理解 MLE 的合理性）

**Strong Law of Large Numbers（SLLN，强大数定律）**：IID 样本均值当 n→∞ 时几乎必然收敛于期望 E[X₁]。

设 θ₀ 是真实参数。n 大时：

$$
\frac1n\sum_i \log p(x_i|\theta)\approx E_{\theta_0}[\log p(x|\theta)]
$$

因此 MLE 近似最小化：

$$
-E_{\theta_0}[\log p(x|\theta)]+\underbrace{E_{\theta_0}[\log p(x|\theta_0)]}_{\text{const}}
= E_{\theta_0}\!\left[\log\frac{p(x|\theta_0)}{p(x|\theta)}\right]
\triangleq D(p_{\theta_0}\|p_\theta)
$$

即 **KL divergence（Kullback-Leibler 散度）**，衡量两个分布"有多不同"。

**Shannon (1948) 定理**：D(p‖q) ≥ 0，当且仅当 p(x)=q(x)（以概率 1）时取等。

- 证明用 **Jensen 不等式**：凸函数 f 有 E[f(X)] ≥ f(E[X])，严格凸时等号成立当且仅当 X 为常数。
- 推论：MLE 在 n 大时最小化 D(p_{θ₀}‖p_θ)，即找一个使 p_θ 尽可能"接近"真实分布 p_{θ₀} 的参数。这就从理论上解释了 MLE"为什么合理"。

### 5. ⭐ Cross-entropy Loss 的推导（重点，连接 MLE 与深度学习）

分类问题有 K 个类，真实标签 y∈{1,…,K}。用模型 q(·|x,θ) 输出 K 类上的概率分布。用 MLE 最大化训练数据 D={(x_i,y_i)} 的 log-likelihood：

$$
\sum_i \log p(x_i,y_i|\theta)=\sum_i\log q(y_i|x_i,\theta)+\underbrace{\sum_i\log p(x_i|\theta)}_{\text{与 θ 无关，const}}
$$

引入 **indicator function** 1{y_i=k} 把同标签项合并：

$$
=\sum_i\sum_{k=1}^{K}1\{y_i=k\}\log q(k|x_i,\theta)+\text{const}
$$

最大化上式 ⇔ 最小化：

$$
-\sum_i\sum_{k}1\{y_i=k\}\log q(k|x_i,\theta)
$$

这恰好就是 **cross-entropy loss（交叉熵损失）**。

- 要点：indicator 起到"按标签分组"的作用；当 n 大时 1{y_i=k}/n 近似 P(y_i=k)，所以也有人写成 P(y_i=k) 形式，但那只是近似，indicator 才是精确写法。
- 结论：**分类中用 MLE 估计 θ，等价于最小化 cross-entropy loss**——这正是深度学习分类网络默认 loss 的理论来源。

### 6. Linear Regression（线性回归，MLE 的连续应用）

模型：response y 依赖输入特征 x=(x₁,…,x_D)，线性关系 + 高斯噪声：

$$
y=w^\top x+\epsilon,\qquad \epsilon\sim\mathcal N(0,\sigma^2)
$$

条件分布：p(y|x,w) = N(y; wᵀx, σ²)。对 IID 训练数据，log-likelihood：

$$
\log p(y|\Phi,w)=-\frac{1}{2\sigma^2}\sum_i(y_i-w^\top x_i)^2+\text{const}
=-\frac{1}{2\sigma^2}\|\Phi w-y\|^2+\text{const}
$$

其中 Φ=[x₁⋯xₙ]ᵀ（设计矩阵 design matrix）。MLE ⇔ 最小化 ‖Φw−y‖²（least squares 最小二乘）。

#### 6.1 Basis Function Expansion（基函数扩展）

为拟合非线性关系，用基函数 φ_i: ℝ^D→ℝ（i=1,…,M）替换原始特征：

$$
\phi(x)=\begin{bmatrix}\phi_1(x)\\\vdots\\\phi_M(x)\end{bmatrix},\quad y=w^\top\phi(x)+\epsilon
$$

例 x=[x₁,x₂]，取 φ(x)=[1, x₁, x₂, x₁², x₂²] ⇒ y=w₁+w₂x₁+w₃x₂+w₄x₁²+w₅x₂²+ε。

- **仍是 linear regression**：只要对参数 w 是线性的即可，x 上可任意非线性变换。
- Wooclap 判定题：判断是否为 linear regression，只看 **w 是否线性**——x 的任意次幂/对数变换都不影响。

#### 6.2 MLE 的闭式解

设计矩阵 Φ（n 行 = 数据点，M 列 = 基函数）。用矩阵求导公式 ∂(aᵀx)/∂x=a、∂(xᵀAx)/∂x=(A+Aᵀ)x：

$$
\Phi^\top\Phi\,w_{ML}-\Phi^\top y=0
\;\Rightarrow\;
w_{ML}=(\Phi^\top\Phi)^{-1}\Phi^\top y
$$

- 要求 ΦᵀΦ 可逆 ⇔ Φ 列满秩 ⇔ **n ≥ M**（数据点数 ≥ 基函数个数，即数据多于参数维度）。
- 不可逆时用 pseudo-inverse（伪逆），此时解不唯一，伪逆给出其中一个解。
- 实操建议：直接调 scikit-learn，不要手写矩阵求逆（数值敏感），需自己构造好 design matrix 即可。

### 7. Goodness of Fit（拟合好坏评估）

| 指标 | 定义 |
|---|---|
| **RSS**（残差平方和） | Σ(y_i−ŷ_i)² |
| **RMSE**（均方根误差） | √(RSS/n) |
| **R²**（决定系数） | 1 − RSS/TSS，TSS=Σ(y_i−ȳ)² 为总平方和（经验方差） |

- R² 衡量"模型解释了数据中多少 variance"，越大越好。
- ŷ_i=ȳ（恒预测均值）⇒ R²=0（与常数模型一样差）。
- **R² 可为负**（"R²"只是名字，不是数学平方）：模型比常数预测还差时 R²<0。

### 8. ⭐ Overfitting（过拟合，核心警示）

课件 notebook 用不同 degree 多项式拟合同一组（真实为二次的）数据：

| degree | Train R² | Test R² |
|---|---|---|
| 1（直线） | 较低 | 0.473 |
| 2（真值） | 0.871 | **0.813** |
| 14 | 较高 | 0.626 |
| 20 | ≈1（几乎完美拟合训练点） | **−5167.893** |

- Train error 随 degree 单调下降，但 **Test error 在某点后反向上升**。
- degree=20 模型"记住"了训练数据，泛化极差 → 经典 **overfitting**。
- 经验法则：比较 train/test 的 R²，二者接近才算健康；test 远低于 train 即过拟合。
- 选模型需在 **复杂度（complexity）与性能（performance）间权衡**（本课不深入，见更高级 ML 课）。

### 9. MAP 估计（加入先验）

当有参数的 prior knowledge（先验知识）时，用 Bayes rule：

$$
p(\theta|D)\propto p(D|\theta)\,p(\theta)
$$

**MAP 估计**：

$$
\theta_{MAP}=\arg\max_\theta p(\theta|D)
$$

取 log：

$$
\log p(\theta|D)=\underbrace{\log p(D|\theta)}_{\text{log-likelihood}}+\underbrace{\log p(\theta)}_{\text{log-prior}}+\text{const}
$$

- MLE 只最大化第一项；MAP 多加了 prior 项，把"系统设计者对 θ 范围的信念"注入训练。
- prior 在高 PDF 区域给 θ 加权，引导估计落入合理范围。

#### 9.1 Bernoulli + Beta prior（MAP 推导）

likelihood p(D|θ)=θ^{N₁}(1−θ)^{N₀}，取 prior p(θ)=Beta(θ|a,b)（Bernoulli 的 conjugate prior，见 Week 1）：

$$
\log[p(D|\theta)p(\theta)]=(N_1+a-1)\log\theta+(N_0+b-1)\log(1-\theta)
$$

求导令零：

$$
\frac{N_1+a-1}{\theta_{MAP}}-\frac{N_0+b-1}{1-\theta_{MAP}}=0
\;\Rightarrow\;
\theta_{MAP}=\frac{N_1+a-1}{n+a+b-2}
$$

- 对比 MLE：θ_ML=N₁/n。MAP 的分子多了 (a−1)、分母多了 (a+b−2)，hyperparameter a、b 把先验"计数"叠加到观测计数上。
- a、b 怎么选取取决于对 θ 的信念（Week 1 的 Beta 形状图）。

#### 9.2 Classification 即 MAP

对特征 x，决策规则 δ(x)=k 当 x∈R_k（把输入空间划分为 K 个区域）。

分类误差 = P(Y≠δ(x)|x) = 1 − P(Y=δ(x)|x)。最小化误差 ⇔ 最大化 P(Y=δ(x)|x)（即 posterior p(y|x)）⇔ 取 **MAP 估计 of y given x**。

- 对比：分类中用 **MLE** 估 θ ⇒ cross-entropy loss；用 **MAP** 决策 ⇒ 最小化 error probability。两者是不同层面的"最优"。

#### 9.3 Naive Bayes（朴素贝叶斯，MAP 的应用）

MNIST 手写数字识别。每张图展平为特征向量 x=(x₁,…,x_D)，标签 y=数字类别。

**核心假设（naive / 朴素）**：给定类别 y，各像素特征条件独立：

$$
p(x|y=c,\theta)=\prod_{d=1}^{D}p(x_d|\theta_{dc})
$$

θ_dc 为类别 c、特征 d 的参数。先验 π(c)=P(y=c)（通常取 uniform）。后验：

$$
p(y=c|x,\theta)\propto \pi(c)\prod_{d}p(x_d|\theta_{dc})
$$

- 二值化 MNIST：x_d∈{0,1}，x_d|y=c ∼ Bern(θ_dc)。
- 模型虽"naive"（现实中像素并不独立），仍达 **test accuracy 84.3%**（远低于 CNN 的 99%+，但作为最简单模型已不错）。

### 10. Practice Problems（课件末，附解答）

**Q1**：x₁,…,xₙ ∼ N(μ, σ²) IID，σ² 已知，求 μ 的 MLE。

log-likelihood = −(1/2σ²)Σ(x_i−μ)² + const。对 μ 求导令零：

$$
\mu_{ML}=\frac1n\sum_{i=1}^{n}x_i=\bar{x}\quad(\text{样本均值})
$$

**Q2**：续上，设 prior μ ∼ N(μ₀, 1)，求 μ 的 MAP。

log posterior = −(1/2σ²)Σ(x_i−μ)² − (1/2)(μ−μ₀)² + const。求导令零：

$$
\mu_{MAP}=\frac{\frac1{\sigma^2}\sum_i x_i+\mu_0}{\frac{n}{\sigma^2}+1}
$$

- 当 n 大（数据多）⇒ MAP ≈ 样本均值 ≈ MLE（prior 影响被稀释）。
- 当 n 小 ⇒ prior μ₀ 拉动估计，体现先验作用。

**Q3**：解释 scikit-learn 代码片段——Line 1 建 LinearRegression 对象；Line 2 建 degree=d 含 bias 的 PolynomialFeatures；Line 3 生成训练特征矩阵；Line 4 拟合模型。

### 11. 本周要点小结

- **MLE**：只用数据，θ_ML=argmax p(D|θ)，等价于最大化 log-likelihood；Bernoulli→N₁/n，Exponential→n/Σx，Gaussian→样本均值；最小二乘 = 线性回归的 MLE；分类 MLE = cross-entropy loss。
- **KL divergence 视角**（补充）：MLE 在大 n 下最小化 D(p_{θ₀}‖p_θ)，由 Shannon 定理 D≥0 保证合理性。
- **MAP**：在 MLE 上加 prior，θ_MAP=argmax p(θ|D)=argmax[log likelihood + log prior]；Bernoulli+Beta ⇒ (N₁+a−1)/(n+a+b−2)；分类最小误差决策 = MAP of y|x。
- **Naive Bayes**：条件独立假设下简单有效的分类器。
- **Overfitting**：复杂度↑→train error↓但 test error 可能反弹；用 train/test R² 对比监控。

---

> **下一周预告**：Week 3 将进入 **Mixture Models and the EM Algorithm**（混合模型与 EM 算法）——当模型有隐变量（latent variable）、MLE 无闭式解时，用 EM（Expectation-Maximization）迭代求最优参数。

---

## Week 3 — Mixture Models and the EM Algorithm（混合模型与 EM 算法）

> **权威来源说明**：本周官方课件为 `week3/3_Mixture_Models_and_EM.pdf`（Tay W.P.，46 页），转写 `week3/week3.txt` 噪声较多，以 PDF 为准。本周转写典型噪声：`p(y|data)` 中的 data 实为 θ（参数）；`lot/lilihod` → likelihood；`gauing/gusin/gausin/Gausia/Gusel` → Gaussian；`Cigma/Cima/cigma` → Σ（协方差）；`amphDo/amd/VDA` → AMD（股票代码）；`invidious` → previous；`art em/EM` → hard EM；`pier` → prior；`clap/your clap` → Wooclap。
> 本周回顾上周 MLE/MAP 后进入新主题：**混合模型**（mixture model，含 latent variable）以及求解其 MLE 的 **EM 算法**（Expectation-Maximization），并以 **GMM**（Gaussian Mixture Model）为主要实例，最后给出 **K-Means 是 EM 在 GMM 上的特例**。

### 1. 本周主线

- 上周回顾：MLE `θ_ML=argmax p(D|θ)`，等价于最大化 log-likelihood（因 log 单调递增，optimizer 不变；且 IID 下乘积变求和，求导可交换进求和号）。MAP `θ_MAP=argmax[log likelihood + log prior]`，当 prior 均匀时退化为 MLE。
- 本周问题：当模型含**隐变量**（latent variable，未被观测到的变量），其 MLE 直接求导无闭式解（log 与 sum 不可交换）→ 需用 **EM 算法** 迭代逼近。
- 全周逻辑链：**为什么要 mixture** → **mixture 形式与 latent variable** → **直接 MLE 的三大困难**（singularity / unidentifiability / intractable optimization）→ **EM 基本思想**（complete data 易优化，用 expectation 替代未知的 y）→ **GMM 的 EM 闭式解** → **K-Means 是特例** → **EM for MAP**（加 prior 抑制 singularity）→ **Monotonicity**（每步 log-likelihood 只增不减）。

### 2. 为什么要 Mixture Models（混合模型）

- 现实数据常无法用单一分布拟合。例：
  - **图像**中含多个不同物体（大象、斑马），其像素分布是多个分布的叠加，需多个 Gaussian 分量表示。
  - **LiDAR / 点云**（point cloud）：用 50 个 Gaussian 分量拟合点云形状。
  - **兔子点云**：100 个 Gaussian 分量。
- 直觉：当总体分布是若干"子群体"分布按某种比例混合而成，单一参数模型不够 → 需 mixture。

### 3. Mixture Model 形式与 Latent Variable

- 设观测 $x$ 可由 $K$ 个可能 pdf 之一生成 $p(x|\eta_1),\dots,p(x|\eta_K)$，"由哪一个生成"未知/未观测。
- 令 $z$ 为生成 pdf 的索引，建模为随机变量 $z\sim\mathrm{Cat}(z|\pi)$（categorical distribution），即 $p(z=k)=\pi(k)$。
- 因 $z$ 未被观测，称为 **latent variable（隐变量）**。于是
$$
p(x|\theta)=\sum_{k=1}^{K}p(x,z=k|\theta)=\sum_{k=1}^{K}\pi(k)\,p(x|\eta_k),\quad \theta=(\pi,\{\eta_k:k=1,\dots,K\}). \tag{3.1}
$$
- 关键：mixture 的边缘分布 $p(x|\theta)$ 把 latent variable $z$ **求和消去**（marginalize）。

#### 3.1 GMM（Gaussian Mixture Model）

- 最常见的 mixture：所有分量都是 Gaussian：
$$
p(x|\theta)=\sum_{k=1}^{K}\pi(k)\,\mathcal{N}(x|\mu_k,\Sigma_k),\quad \theta=(\pi,\{\mu_k,\Sigma_k\}_{k=1}^{K}). \tag{3.2}
$$
- 课件示例：3 分量，$\pi=(0.3,0.3,0.4)^T$，均值 $\mu_1=[0,0]^T,\mu_2=[0,4]^T,\mu_3=[4,4]^T$，各自协方差不同。
- **应用例（clustering）**：把 $K=5$ 个 Gaussian 拟合二维数据，得到 Voronoi 式分区（见 `03_kmeans_voronoi.ipynb`）。

### 4. MLE 的三大算法性困难（Algorithmic Issues）

给定 IID 观测 $x_1,\dots,x_n$，log-likelihood 为
$$
\log p(x_1,\dots,x_n|\theta)=\sum_{i=1}^{n}\log\sum_{k=1}^{K}\pi(k)\,p(x_i|\eta_k). \tag{MLE}
$$

#### 4.1 ⭐ Singularity（奇点）— 似然可发散

- GMM 特例 $p(x_i|\theta)=\sum_k\pi(k)\mathcal{N}(x_i|\mu_k,\sigma_k I)$。若对某个 $k$ 取 $\mu_k=x_i$ 且 $\sigma_k\to0$（"collapsing 坍缩"），则
$$
\mathcal{N}(x_i|\mu_k,\sigma_k I)\propto\frac{1}{\sigma_k}\to\infty,
$$
似然函数出现**奇点**，可被无限放大 → MLE 无意义。
- **heuristic 应对**：检测到某分量坍缩时，把该均值重置为随机值、协方差重置（reset）。
- ⚠️ 此问题 EM 也**无法**解决（见 §8 MAP 用 prior 抑制）。

#### 4.2 Unidentifiability（不可辨识）

- **identifiable（可辨识）**：不同参数 $\theta_1\neq\theta_2$ ⇒ 不同分布 $P_{\theta_1}\neq P_{\theta_2}$，这样参数才有可解释含义。
- mixture MLE：$p(x|\theta)=\sum_k\pi(k)p(x|\eta_k)$，对任一 $\theta_{ML}$ **置换分量标号 $k$**（permute indices）得到另一组参数给出**相同的整体 pdf**。
- 后果：log-likelihood **没有唯一全局最优**。目标定为"找到一个 good overall likelihood"即可（不纠结标号）。

#### 4.3 Optimization（不可解）

- 关键困难：$\log\sum_k(\cdot)$ 中 **log 不能与 sum 交换**，目标函数一般**非凹**（not concave），难直接解。
- 即便 $\pi$ 已知，对 $\theta'$ 求导令零需解
$$
\sum_{i=1}^{n}\sum_{k=1}^{K}\frac{\pi(k)}{\sum_{k'}\pi(k')p_{k'}(x_i|\theta')}\cdot\frac{\partial p_k(x_i|\theta)}{\partial\theta'}=0,
$$
耦合方程组，无闭式解。
- **转折（EM 的动机）**：若额外观测到 latent variables $z_1,\dots,z_n$（complete data），则 likelihood 变得极易最大化：
$$
\log p((x_1,z_1),\dots,(x_n,z_n)|\theta)=\sum_{i=1}^{n}\bigl(\log\pi[z_i]+\log p(x_i|\eta_{z_i})\bigr),
$$
log 与 sum **可交换**，求导解耦 → 闭式 MLE。

### 5. Complete vs Incomplete Data（EM 的核心设定）

- 设想若知道每个 $x_i$ 来自哪个分量 $z_i$，则 GMM 的 MLE 是标准闭式：
  - 记 $y_i=(x_i,z_i)$ 为 **complete data（完整数据）**，$x=T(y)$（这里 $T$ 取 $y$ 的第一坐标）为实际观测到的 **incomplete data（不完整数据）**。
  - complete data log-likelihood：
$$
\log p(y_1,\dots,y_n|\theta)=\sum_{k=1}^{K}\sum_{i:z_i=k}\bigl(\log\pi(k)+\log\mathcal{N}(x_i|\mu_k,\Sigma_k)\bigr).
$$
  - 据此直接得闭式 MLE：
$$
\hat\mu_k=\frac{1}{n}\sum_{i:z_i=k}x_i,\qquad
\hat\Sigma_k=\frac{1}{n}\sum_{i:z_i=k}(x_i-\hat\mu_k)(x_i-\hat\mu_k)^T.
$$
- 但现实中 $z_i$ 未知 → 不能直接用。EM 的思路：**既然 $y$ 未知无法算 likelihood，就取它的 expectation（期望）**。
  - 老师比喻：给你一个未知样本来自某 Gaussian（参数已知但你不知具体取值），你对样本的最佳猜测就是用该分布的**均值**近似。同理，用对 $y$ 的期望替代未知的 $y$。

### 6. ⭐ EM 算法（Expectation-Maximization）

#### 6.1 基本思想（一般形式）

- 设 $p(y|\theta)$ 易最大化，但观测的是 $x=T(y)$（incomplete），$\log p(x|\theta)$ 难算/难优化。
- MLE $\theta_{ML}=\arg\max_\theta\log p(x|\theta)$ 难。
- **思路**：用对 $y$ 的期望替代未知的 $y$，在一个"猜测" $\hat\theta$（当前估计）下取期望：
$$
\mathbb{E}_{p(y|x,\hat\theta)}\bigl[\log p(y|\theta)\bigr].
$$

#### 6.2 算法步骤

1. 选初始猜测 $\theta^{(0)}$。
2. **E step（第 $m+1$ 次迭代）**：计算 **Q 函数**
$$
Q(\theta|\theta^{(m)})=\mathbb{E}_{p(y|x,\theta^{(m)})}\bigl[\log p(y|\theta)\bigr]=\int \log p(y|\theta)\,p(y|x,\theta^{(m)})\,dy.
$$
   - 即：在"假设 $\theta^{(m)}$ 是真值"的假设下，对 $\log p(y|\theta)$ 求期望。注意 $\theta$ 是待优化变量，$\theta^{(m)}$ 用于构造可计算的分布。
3. **M step**：更新
$$
\theta^{(m+1)}=\arg\max_{\theta\in\Theta}Q(\theta|\theta^{(m)}).
$$
4. 重复 E、M 直到收敛（如 log-likelihood 变化 $|L^{(m+1)}-L^{(m)}|\le\epsilon$）。

- **实现说明**（老师口述）：若 mixture 模型 tractable（如 GMM），$Q$ 与 $\theta^{(m+1)}$ 都有**闭式公式**，M step 无需数值优化；否则 $Q$ 是代码里的函数，M step 需用 gradient descent 等通用优化。

### 7. ⭐ EM for GMM（核心实例，必记闭式解）

#### 7.1 E step — responsibility（责任度）

- complete data $y=(x_i,z_i)_{i=1}^n$，$z_i\in\{1,\dots,K\}$ 指示 $x_i$ 来自哪个 Gaussian。
- Q 函数展开：
$$
Q(\theta|\theta^{(m)})=\sum_{i=1}^{n}\sum_{k=1}^{K}r_{ik}^{(m)}\log\{\pi(k)\mathcal{N}(x_i|\mu_k,\Sigma_k)\}.
$$
- 由 Bayes' theorem，**responsibility $r_{ik}^{(m)}=p(z_i=k|x_i,\theta^{(m)})$**：
$$
r_{ik}^{(m)}=\frac{\pi^{(m)}(k)\,\mathcal{N}(x_i|\mu_k^{(m)},\Sigma_k^{(m)})}{\sum_{k'=1}^{K}\pi^{(m)}(k')\,\mathcal{N}(x_i|\mu_{k'}^{(m)},\Sigma_{k'}^{(m)})}. \tag{E step}
$$
- 直觉：$r_{ik}$ 是第 $k$ 个分量对数据点 $x_i$ 的"负责比例"，是 $[0,1]$ 上的软分配（soft assignment），$\sum_k r_{ik}=1$。
- 记 $n_k^{(m)}=\sum_{i=1}^n r_{ik}^{(m)}$（第 $k$ 分量的有效点数）。

#### 7.2 M step — 闭式更新

在 $\sum_k\pi(k)=1,\,\pi(k)\ge0,\,\Sigma_k\succ0$ 约束下最大化 $Q$。

- **π 的更新（Lagrangian）**：构造 $L=\sum_k n_k^{(m)}\log\pi(k)-\lambda(\sum_k\pi(k)-1)$，对 $\pi(k)$ 求偏导令零 $\Rightarrow \pi(k)=n_k^{(m)}/\lambda$；由约束 $\sum_k\pi(k)=1$ 得 $\lambda=\sum_k n_k^{(m)}=n$，故
$$
\boxed{\;\pi^{(m+1)}(k)=\frac{n_k^{(m)}}{n}\;}\qquad\text{（每个分量的混合权 = 其有效点占比）}.
$$

- **μ_k 的更新**：对 $\mu_k$ 求导令零（$\partial Q/\partial\mu_k=\Sigma_k^{-1}\sum_i r_{ik}^{(m)}(x_i-\mu_k)=0$）得
$$
\boxed{\;\mu_k^{(m+1)}=\frac{1}{n_k^{(m)}}\sum_{i=1}^{n}r_{ik}^{(m)}\,x_i\;}\qquad\text{（责任度加权均值）}.
$$

- **Σ_k 的更新**：对 $\Sigma_k$ 求导令零得
$$
\boxed{\;\Sigma_k^{(m+1)}=\frac{1}{n_k^{(m)}}\sum_{i=1}^{n}r_{ik}^{(m)}(x_i-\mu_k^{(m+1)})(x_i-\mu_k^{(m+1)})^T\succ0\;}.
$$

#### 7.3 EM for GMM 完整算法摘要

```
输入 π^(0), μ_k^(0), Σ_k^(0) (k=1..K)；L^(0)=初始 log-likelihood
repeat:
  E step: 对所有 i,k 算 responsibility r_ik^(m)（E step 公式），n_k^(m)=Σ_i r_ik^(m)
  M step: 更新 π^(m+1)(k)=n_k^(m)/n,  μ_k^(m+1)=Σ_i r_ik^(m)x_i / n_k^(m),
          Σ_k^(m+1)=Σ_i r_ik^(m)(x_i−μ_k^(m+1))(·)^T / n_k^(m)
  算 L^(m+1)=Σ_i log Σ_k π^(m+1)(k) N(x_i|μ_k^(m+1),Σ_k^(m+1))
until |L^(m+1)−L^(m)| ≤ ε
```
- 演示 notebook：`03_mix_gauss_demo_faithful.ipynb`（Old Faithful 数据集拟合 GMM）。

### 8. ⭐ K-Means 是 EM on GMM 的特例

- 设定：GMM 中令 $\Sigma_k=\sigma^2 I$（各向同性、**所有分量共享同一 $\sigma^2$**，固定已知）、$\pi(k)=1/K$（均匀、固定已知），**只推断 $\mu_k$**。
- **E step 变为 hard EM（硬分配）**：responsibility 退化为 one-hot：
$$
r_{ik}^{(m)}=\begin{cases}1,&k_i=\arg\min_k\|x_i-\mu_k^{(m)}\|^2\\0,&k\ne k_i\end{cases}
$$
即每个 $x_i$ **全权分配给最近的聚类中心**（欧氏距离），而非软分配。
- 此时 $Q(\theta|\theta^{(m)})=-\frac{1}{2\sigma^2}\sum_i\|x_i-\mu_{k_i}\|^2+\text{const}$，M step 是最小二乘优化：
$$
\mu_k^{(m+1)}=\frac{1}{N_k}\sum_{i:k_i=k}x_i,\quad N_k=\sum_i\mathbf{1}\{k_i=k\}.
$$
- 结论：**K-Means = hard EM 下的 GMM 特例**——E step 按最近中心硬分配，M step 取该簇点均值更新中心，循环至收敛。
- **选 K**（老师口述）：K 未知时试不同值，看 loss 随 K 衰减曲线，在衰减明显变缓处（"elbow"）选 K（K=n 时 loss=0 但无意义）。
- 演示：`03_kmeans_voronoi.ipynb`（K=5 迭代更新 centroid + 重分配直至 Voronoi 区域稳定）。

### 9. EM for MAP（用 prior 抑制 singularity）

- **动机**：EM 不解决 singularity（§4.1）。MLE of GMM 在某 $\Sigma_k\to0$ 时仍奇异；尤其**维度 $D$ 大**时参数量爆炸，优化在高维空间遇**奇异矩阵**等数值问题，失败率随 $D$ 上升趋近 1（课件图：MLE 在 $D\gtrsim50$ 几乎必失败，而 MAP 几乎为 0）。
- **做法（Bayesian）**：对 $\theta$ 加 prior $p(\theta)$，penalize $\Sigma_k\to0$ 的取值。posterior
$$
p(\theta|x)=\frac{p(x|\theta)p(\theta)}{p(x)},\qquad \theta_{MAP}=\arg\max_\theta\bigl(\log p(x|\theta)+\log p(\theta)\bigr).
$$
- **EM for MAP**：E step 与 MLE 的 EM **完全相同**；M step 只是在最大化 $Q$ 上**多加 $\log p(\theta)$**：
$$
\theta^{(m+1)}=\arg\max_\theta\bigl(Q(\theta|\theta^{(m)})+\log p(\theta)\bigr).
$$
- 直觉（老师口述）：prior 把 $\mu_k,\Sigma_k$ **约束在良好空间**，阻止优化发散到奇异矩阵；GMM 对 $\pi,\mu_k,\Sigma_k$ 加 prior 的具体形式见 [M12]。
- **MAP 一定优于 MLE 吗**：不一定。MLE 只要数据足够就**一致（consistent）**、收敛到真值；MAP 若 prior 选得与真数据不符，反而**不一致**。MAP 的价值在于小样本或高维下用领域知识正则化、抑制数值失败（见 §11 小结的权衡）。

### 10. Practice Problems（课件末，附解答）

#### P1：GMM 的均值与协方差

证明 $E[x]=\sum_k\pi(k)\mu_k$，$\mathrm{cov}(x)=\sum_k\pi(k)(\Sigma_k+\mu_k\mu_k^T)-E[x]E[x]^T$。

**解**：令 $z$ 为 latent variable，用 **law of total expectation** 与 **law of total covariance**：
$$
E[x]=E[E[x|z]]=\sum_k\pi(k)E[x|z=k]=\sum_k\pi(k)\mu_k.
$$
对二阶矩，$\Sigma_k=E[(x-\mu_k)(x-\mu_k)^T|z=k]=E[xx^T|z=k]-\mu_k\mu_k^T$ ⇒ $E[xx^T|z=k]=\Sigma_k+\mu_k\mu_k^T$。故
$$
\mathrm{cov}(x)=E[xx^T]-E[x]E[x]^T=\sum_k\pi(k)(\Sigma_k+\mu_k\mu_k^T)-E[x]E[x]^T.
$$

#### P2：读 GMM 的 EM 代码（行级解释，从 Line 13 起）

- Line 13：为每个 mixture component 建一个 normal distribution 对象 $\mathcal{N}(\cdot|\mu_i,\Sigma_i)$。
- Line 14：对每行 $i$（数据 $x_i$）算各 $k$ 的 $\pi^{(m)}(k)\mathcal{N}(x_i|\mu_k^{(m)},\Sigma_k^{(m)})$。
- Line 15：算 responsibility $r_{ik}^{(m)}=\frac{\pi^{(m)}(k)\mathcal{N}(x_i|\mu_k^{(m)},\Sigma_k^{(m)})}{\sum_{k'}\pi^{(m)}(k')\mathcal{N}(x_i|\mu_{k'}^{(m)},\Sigma_{k'}^{(m)})}$。

#### P3：行人/骑车者 mixture（latent = 出行方式）

- 情境：步道上行人:骑车者 = 4:1。vulnerable（易受伤害）判定：年龄 <10、>65 或 handicapped。行人 vulnerable 概率 $\theta_0$，骑车者 $\theta_1$。Hua 调查 100 人记录 $x_i\in\{0,1\}$（是否 vulnerable）但**未记录**其是行人还是骑车者。
- **(i)** log-likelihood：
$$
\log p(x_1,\dots,x_{100}|\theta_0,\theta_1)=\sum_{i=1}^{100}\log\bigl[0.8\cdot\theta_0^{x_i}(1-\theta_0)^{1-x_i}+0.2\cdot\theta_1^{x_i}(1-\theta_1)^{1-x_i}\bigr].
$$
  （混合权 0.8=行人占比、0.2=骑车者占比；每个分量是 Bernoulli。）
- **(ii)** 适合算法：**EM**。因这是 mixture model，$\log\sum(\cdot)$ 中 log 与 sum 不可交换，直接求导解根困难；EM 迭代求 $\theta_0,\theta_1$ 的 MLE。

### 11. ⭐ Monotonicity（EM 的单调性，补充证明）

- **结论**：EM **不保证找到全局 MLE**（可能停在 local maximum）；实践中常从多个随机初值启动取最优。但**每次迭代 log-likelihood 只增不减**（monotonically non-decreasing）→ 必收敛到某 local optimum。
- **证明骨架**（用 Jensen 不等式）：
  - 设 $x=T(y)$ 为 incomplete、$y$ 为 complete。对任意 $\theta$，
$$
\log p(x|\theta)=\log\int_{T(y)=x}p(y|\theta)\,dy=\log\int_{T(y)=x}\frac{p(y|\theta)}{p(y|x,\theta^{(m)})}p(y|x,\theta^{(m)})\,dy.
$$
  - 对 $\log$（凹函数）用 **Jensen 不等式**（以 $p(y|x,\theta^{(m)})$ 为权重取期望）：
$$
\log p(x|\theta)\ge \int_{T(y)=x}\log\frac{p(y|\theta)}{p(y|x,\theta^{(m)})}p(y|x,\theta^{(m)})\,dy = Q(\theta|\theta^{(m)}) + \text{entropy term (与 $\theta$ 无关)}.
$$
  - 该下界在 $\theta=\theta^{(m)}$ 处与 $\log p(x|\theta)$ **相切**（取等），故最大化 $Q$（M step 使 $Q(\theta^{(m+1)}|\theta^{(m)})\ge Q(\theta^{(m)}|\theta^{(m)})$）⇒ 下界提升 ⇒ $\log p(x|\theta^{(m+1)})\ge\log p(x|\theta^{(m)})$。
- 直觉：$Q$ 是 log-likelihood 的**紧致下界**（evidence lower bound, ELBO），EM 每步提升这个下界，因下界在当前点贴合故 log-likelihood 必不降。

### 12. 真实应用：GMM 判别牛/熊市（stock market）

- 老师在投行用过 GMM 这类传统模型（不止深度学习）。notebook：`GMM_Stock` + Yahoo Finance 数据。
- 取 AMD 股票多年收盘价，算 **log return** 与 **volatility**（两维特征，便于可视化；实际投行用更多因子）。
- 假设数据由 **2 个 Gaussian 分量**生成：分量1 = **bull market（牛市）**（低波动、高收益），分量2 = **bear market（熊市）**（高波动、低/负收益）。
- 用历史数据经 EM 估计 $\pi_1,\pi_2,\mu_1,\Sigma_1,\mu_2,\Sigma_2$，进而聚类每天为 bull/bear。结果：低波动点归牛市、高波动点归熊市，符合直觉；熊市分量收益跨度大（含大幅负收益也有偶发大正收益）。
- 用途：判断当天牛/熊市状态，供 portfolio optimization / 客户推荐。
- **latent variable = 当天是牛还是熊**（不可直接观测），正是 mixture model 的典型场景。

### 13. 本周要点小结

- **Mixture model**：$p(x|\theta)=\sum_k\pi(k)p(x|\eta_k)$，GMM 最常用；latent variable $z$ 指示来源分量，边缘分布把 $z$ marginalize 掉。
- **直接 MLE 三大困难**：singularity（$\sigma_k\to0$ 似然发散，EM 也无法解决）、unidentifiability（置换分量标号同 pdf，无唯一最优）、optimization intractable（$\log\sum$ 不可换，非凹）。
- **EM 算法**：complete data 易优化但 $z$ 未知 → 取期望。E step 算 Q 函数（在当前 $\theta^{(m)}$ 下对 $\log p(y|\theta)$ 求期望）；M step 最大化 Q。迭代至 log-likelihood 收敛。
- **GMM 闭式更新（必记）**：responsibility $r_{ik}=\pi(k)\mathcal{N}(x_i|\mu_k,\Sigma_k)/\sum_{k'}(\cdot)$；$\pi^{(m+1)}(k)=n_k/n$，$\mu_k^{(m+1)}=\sum_i r_{ik}x_i/n_k$，$\Sigma_k^{(m+1)}=\sum_i r_{ik}(x_i-\mu_k^{(m+1)})(\cdot)^T/n_k$。
- **K-Means**：GMM 在 $\Sigma_k=\sigma^2I$、$\pi(k)=1/K$ 固定下、只学 $\mu_k$ 的特例；E step 是 hard assignment（最近中心），M step 取簇内均值。
- **EM for MAP**：E step 不变，M step 加 $\log p(\theta)$；用 prior 抑制高维下的 singularity/数值失败（MLE 失败率随 $D$ 趋 1，MAP 几乎为 0）。MAP 不一定优于 MLE（prior 不准则不一致），价值在小样本/高维正则化。
- **Monotonicity**：EM 每步 log-likelihood 只增不减（Jensen 不等式证 $Q$ 是 ELBO、当前点取等），故收敛到 local optimum；多随机初值缓解局部最优。
- **应用**：GMM 判别牛/熊市（latent = 当天市场状态）。

---

> **下一周预告**：Week 4 预计继续概率建模/模式识别主题（Tay Wee Peng 部分），可能进入 Bayesian networks / Markov models 或进一步的概率图模型与推断；具体主题以课件为准。Week 1 进度表所列后续主题包括 Hidden Markov Models、Classification 等。

---

## Week 4 — Markov Models and HMM

> **权威来源说明**：本周无录播转写，基于官方材料整理。来源为 `week4/4_Markov_Models_and_HMM.pdf`（官方课件，作者 Tay W.P.，51 页）与 `week4/Week 4.pdf`（标注讲义）。无老师口述补充，仅据课件结构整理。本周主题承接 Week 3 的 mixture model / EM：当 latent variable 带上**时间结构**，就得到 Markov chain 与 HMM，Baum-Welch 即 EM 在 HMM 上的具体实例。

### 1. 主线与动机

- Week 3 的 mixture model 把每个样本独立地归入一个 latent 分量；Week 4 引入**时间序列**——latent variable $z[t]$ 随时间演化、彼此相关。
- 动机（PDF p2）：speech recognition（根据部分句子推断上一个词）、text generation（预测下一字符/词）——本质都是"基于当前 state 预测下一 state"，即 **Markov chain**。

### 2. Markov Chains（马尔可夫链）

#### 2.1 Markov property 与 transition matrix

- 离散时间随机变量序列 $x[0],x[1],\ldots$，每个 $x[t]\in\{1,\ldots,M\}$（状态空间，state space）。
- **Markov property（马尔可夫性质）**：

$$
p(x[t]\mid x[1],\ldots,x[t-1])=p(x[t]\mid x[t-1])
$$

- 直觉："The future is independent of the past, given the present."（给定现在，未来与过去独立。）
- **Transition probability（转移概率）**：

$$
T(i,j)=P(x[t]=j\mid x[t-1]=i)
$$

- 本课只考虑 **homogeneous MC（齐次马尔可夫链）**——$T$ 不随时间 $t$ 变。
- **Transition matrix（转移矩阵）** $T=[T(i,j)]_{i,j=1}^M$，每行求和为 1（**row stochastic matrix**，行随机矩阵）。

#### 2.2 状态分布的演化

- 设 $x[0]$ 的分布为行向量 $p_0=[p_0(1),\ldots,p_0(M)]$，则

$$
p_1(i)=\sum_{j=1}^M p(x[1]=i\mid x[0]=j)\,p_0(j)=\sum_{j=1}^M T(j,i)\,p_0(j)=(p_0T)(i)
$$

- 一般地 $p_t=p_{t-1}T=p_0T^t$。

#### 2.3 例子（PDF p7）

$T=\begin{bmatrix}0.2&0.8\\0.7&0.3\end{bmatrix}$，$p_0=[0.5,0.5]$：

$$
p_1=p_0T=[0.45,0.55],\quad p_2=p_1T=[0.475,0.525]
$$

- **序列概率**：$p(x[0]=1,x[1]=2,x[2]=1)=p_0(1)\,T(1,2)\,T(2,1)=0.5\times0.8\times0.7$。

#### 2.4 应用：Language Modeling（语言建模）

- **Statistical language model**：学习词序列的概率分布。应用：sentence completion（句子补全）、data compression（数据压缩，高频串用短码字）、text classification（文本分类）。
- **Unigram model**：$p(x[t]=x)$——词的边际概率。
- **Bigram model**：$p(x[t]\mid x[t-1])$——依赖前一个词（一阶 Markov）。
- **n-gram model**：$p(x[t]\mid x[t-1],\ldots,x[t-n+1])$——依赖前 $n-1$ 个词（$(n-1)$ 阶 Markov）。

#### 2.5 应用：PageRank

- 网站 $i$ 的权威分 $\pi_i$：被其他权威网站链接则更权威。

$$
\pi_i=\sum_j T(j,i)\,\pi_j
$$

- 用户访问构成 Markov chain；$T(j,i)$ 为从 $j$ 跳到 $i$ 的概率（无链接则 $T(j,i)=0$）。

### 3. Markov Chain 的 MLE

#### 3.1 完整数据的 likelihood

观测 $n$ 条序列 $D=\{x^1[0:t_1],\ldots,x^n[0:t_n]\}$，参数 $\theta=(\pi,T)$：

$$
p(x[0],\ldots,x[t]\mid\pi,T)=\pi(x[0])\,T(x[0],x[1])\,T(x[1],x[2])\cdots T(x[t-1],x[t])
$$

$$
\log p(D\mid\pi,T)=\sum_{x=1}^M N_x\log\pi(x)+\sum_{x=1}^M\sum_{y=1}^M N_{xy}\log T(x,y)
$$

- $N_x=\sum_{i=1}^n\mathbf{1}\{x^i[0]=x\}$（状态 $x$ 作为**起始状态**的次数）。
- $N_{xy}=\sum_{i=1}^n\sum_{t=1}^{t_i}\mathbf{1}\{x^i[t-1]=x,x^i[t]=y\}$（从 $x$ 转到 $y$ 的次数）。

#### 3.2 MLE 闭式解

对 $\log\pi(x)$、$\log T(x,y)$ 求偏导并解根（含约束 $\sum_x\pi(x)=1$、$\sum_y T(x,y)=1$）：

$$
\hat\pi(x)=\frac{N_x}{n},\qquad \hat T(x,y)=\frac{N_{xy}}{\sum_{z=1}^M N_{xz}}
$$

- 直觉：$\hat\pi(x)$ = 状态 $x$ 作为起点的频率；$\hat T(x,y)$ = 从 $x$ 出发转到 $y$ 的频率。
- **零计数问题**：若某状态对在训练数据中计数为 0，模型会预测该串概率为 0（overfitting）。例 50,000 词的 bigram 有 25 亿参数，必有无覆盖词对 → 需 smoothing。

#### 3.3 数值例子（PDF p15）

状态空间 $\{1,2\}$，$D=\{x^1[0{:}2],x^2[0{:}1],x^3[0{:}3]\}$：

| 序列 | 内容 |
|---|---|
| $x^1[0{:}2]$ | $(1,2,1)$ |
| $x^2[0{:}1]$ | $(2,2)$ |
| $x^3[0{:}3]$ | $(1,1,2,1)$ |

- $N_1=2$（$x^1,x^3$ 起点为 1），$N_2=1$（$x^2$ 起点为 2）$\Rightarrow\hat\pi(1)=2/3,\hat\pi(2)=1/3$。
- $N_{11}=1,N_{12}=2,N_{21}=2,N_{22}=1$ $\Rightarrow\hat T=\begin{bmatrix}1/3&2/3\\2/3&1/3\end{bmatrix}$。

### 4. Hidden Markov Models（HMM，隐马尔可夫模型）

#### 4.1 定义

HMM 由两部分构成：
1. **隐状态的 Markov chain**：$z[t]\in\{1,\ldots,M\}$（hidden states / latent variables），初始分布 $\pi$、转移矩阵 $T$。
2. **Observation model（观测模型）**：emission probability（发射概率）$p(x[t]\mid z[t])=p(x[t]\mid\phi_{z[t]})$，参数 $\phi=(\phi_1,\ldots,\phi_M)$。

- 结构：$z[0]\to z[1]\to\cdots$（隐状态 Markov 链），每个 $z[t]$ 独立发射观测 $x[t]$。
- 关键：**观测 $x[0],x[1],\ldots$ 不假设 Markov 性**；长程依赖通过 latent variables $z[t]$ 捕捉。

#### 4.2 应用

- **Speech recognition**：$x[t]$ = 语音特征向量，$z[t]$ = 正在说的词；$p(z[t]\mid z[t-1])$ = language model，$p(x[t]\mid z[t])$ = acoustic model。
- **Activity recognition**：$x[t]$ = 图像/视频帧特征，$z[t]$ = 活动类型。
- **Gene finding**：$x[t]$ = DNA nucleotide（A,C,G,T），$z[t]$ = 是否在 gene-coding region。
- **Emission 例子**：$z[t]=k\Rightarrow x[t]\sim p(x[t]\mid\phi_k)=\mathcal{N}(x[t]\mid\mu_k,\Sigma_k)$。

#### 4.3 骰子 Toy Example（PDF p19–20）

- 两个骰子：fair die（均匀 $\phi_1=(1/6,\ldots,1/6)$）与 loaded die（$\phi_2=(1/10,\ldots,1/10,5/10)$，6 占一半）。
- $z[t]\in\{1,2\}$ 指示用哪个骰子；观测 $x[t]\in\{1,\ldots,6\}$。
- 参数：初始 $\pi$（起始用哪个骰子）、转移 $T$（换骰子概率，一般很小）、emission $\phi_1,\phi_2$。

### 5. HMM 的三大问题

| 问题 | 名称 | 公式 | 算法 |
|---|---|---|---|
| **Evaluation** | 给参数算观测序列概率 | $p(x[0{:}T]\mid\theta)$ | Forward algorithm |
| **Decoding** | 给观测找最可能隐状态序列 | $z^*[0{:}T]=\arg\max_{z}p(z[0{:}T]\mid x[0{:}T])$ | **Viterbi algorithm** |
| **Learning** | 从观测学参数 | $\hat\theta=\arg\max_\theta\log p(D\mid\theta)$ | **Baum-Welch**（EM） |

#### 5.1 推断任务细分（PDF p32–33）

- **Filtering（滤波）**：$p(z[t]\mid x[0{:}t])$——用至当前时刻的观测推断当前隐状态（online）。Forward algorithm。
- **Smoothing（平滑）**：$p(z[t]\mid x[0{:}T])$——离线，用过去+未来观测。Forward-Backward algorithm。
- **Fixed lag smoothing**：$p(z[t-l]\mid x[0{:}t])$——延迟 $l$ 步的 online 推断。Forward-Backward。
- **Prediction（预测）**：$p(z[t+h]\mid x[0{:}t])=\sum_{z[t:\cdot]}\big(\prod_{i=1}^h p(z[t+i]\mid z[t+i-1])\big)p(z[t]\mid x[0{:}t])$，horizon $h>0$。也可 $p(x[t+h]\mid x[0{:}t])=\sum_{z[t+h]}p(x[t+h]\mid z[t+h])\,p(z[t+h]\mid x[0{:}t])$。
- **MAP sequence**：$z^*[0{:}T]=\arg\max_z p(z[0{:}T]\mid x[0{:}T])$ → Viterbi。

### 6. Baum-Welch Algorithm（EM for HMM）

#### 6.1 从 vanilla MLE 到 EM

- 若隐状态 $z^i$ 可观测，likelihood 为（Exercise）：

$$
\log p(D\mid\theta)=\sum_{i=1}^n\log\pi(z^i[0])+\sum_{i=1}^n\sum_{t=1}^{t_i}\log T(z^i[t-1],z^i[t])+\sum_{i=1}^n\sum_{t=0}^{t_i}\log p(x^i[t]\mid\phi_{z^i[t]})
$$

- 但 $z^i[t]$ 未知 → **Baum-Welch（EM 实例）**。

#### 6.2 E step：Q 函数与两个后验

$$
Q(\theta\mid\theta^{(m)})=\sum_{i=1}^M\gamma_{i,0}(z)\log\pi(z)+\sum_{i,t}\sum_{z,z'}\xi_{i,t}(z,z')\log T(z,z')+\sum_{i,t}\sum_z\gamma_{i,t}(z)\log p(x^i[t]\mid\phi_z)
$$

两个关键后验（由 forward-backward 计算）：

$$
\gamma_{i,t}(z)=p(z^i[t]=z\mid x^i[0{:}t_i],\theta^{(m)})
$$

$$
\xi_{i,t}(z,z')=p(z^i[t-1]=z,z^i[t]=z'\mid x^i[0{:}t_i],\theta^{(m)})
$$

- $\gamma$ = 单时刻的 marginal posterior；$\xi$ = 相邻两时刻的 joint posterior。

#### 6.3 M step：参数更新（式 4.1–4.4）

$$
\hat\pi(z)=\frac{\sum_{i=1}^n\gamma_{i,0}(z)}{n}
$$

$$
\hat T(z,z')=\frac{\sum_{i=1}^n\sum_{t=1}^{t_i}\xi_{i,t}(z,z')}{\sum_{i=1}^n\sum_{t=1}^{t_i}\sum_{u}\xi_{i,t}(z,u)}
$$

- Gaussian emission 下：

$$
\hat\mu_z=\frac{\sum_{i,t}\gamma_{i,t}(z)\,x^i[t]}{\sum_{i,t}\gamma_{i,t}(z)}
$$

$$
\hat\Sigma_z=\frac{\sum_{i,t}\gamma_{i,t}(z)\,(x^i[t]-\hat\mu_z)(x^i[t]-\hat\mu_z)^\top}{\sum_{i,t}\gamma_{i,t}(z)}
$$

- 直觉：把"硬"计数 $N_x,N_{xy}$ 换成"软"后验期望 $\gamma,\xi$——正是 Week 3 EM 的 responsibility 思想在时间序列上的推广。

### 7. Forward-Backward Algorithm（求 $\gamma,\xi$）

#### 7.1 分解思想（式 4.5）

$$
\gamma_{i,t}(z)=p(z^i[t]=z\mid x^i[0{:}t_i])\propto p(z^i[t]=z\mid x^i[0{:}t])\,p(x^i[t+1{:}t_i]\mid z^i[t]=z)
$$

- 由 Markov property，给定 $z[t]$，未来观测 $x[t+1{:}t_i]$ 与过去 $x[0{:}t]$ 独立。
- **Forward variable**：$\alpha_t(z)=p(z[t]=z\mid x[0{:}t])$。
- **Backward variable**：$\beta_t(z)=p(x[t+1{:}T]\mid z[t]=z)$。
- 归一化：

$$
\gamma_{i,t}(z)=\frac{\alpha_t(z)\,\beta_t(z)}{\sum_{z'}\alpha_t(z')\,\beta_t(z')}
$$

#### 7.2 Forward 递推

- **Predict**：

$$
p(z[t]=z\mid x[0{:}t-1])=\sum_{z'} T(z',z)\,\alpha_{t-1}(z')
$$

- **Update**（加入 $x[t]$）：

$$
\alpha_t(z)=\frac{p(x[t]\mid z[t]=z)\,\sum_{z'}T(z',z)\,\alpha_{t-1}(z')}{Z_t}
$$

- $Z_t=p(x[t]\mid x[0{:}t-1])=\sum_z p(x[t]\mid z[t]=z)\,p(z[t]=z\mid x[0{:}t-1])$ 为归一化常数。
- **初始化**：$\alpha_0(z)=\frac{1}{Z_0}p(x[0]\mid z[0]=z)\,\pi(z)$，$Z_0=\sum_z p(x[0]\mid z[0]=z)\,\pi(z)$。

#### 7.3 Backward 递推

$$
\beta_t(z)=\sum_{z'} T(z,z')\,p(x[t+1]\mid z[t+1]=z')\,\beta_{t+1}(z')
$$

- **初始化**：$\beta_T(z)=1$（因为 $\beta_T(z)=p(x[T+1{:}T]\mid z[T]=z)$ 为空序列概率 = 1）。

#### 7.4 求 $\xi$（式 4.5 推导）

$$
\xi_{i,t}(z,z')\propto \alpha_{t-1}(z)\,p(x[t]\mid z[t]=z')\,\beta_t(z')\,T(z,z')
$$

- 即 "past $\alpha$ × emission × transition × future $\beta$"。

### 8. Viterbi Algorithm（Decoding，求 MAP 路径）

#### 8.1 目标

$$
z^*[0{:}T]=\arg\max_{z[0:T]} p(z[0{:}T]\mid x[0{:}T])=\arg\max_{z[0:T]} \log p(z[0{:}T],x[0{:}T])
$$

$$
\log p(z[0{:}T],x[0{:}T])=\log\pi(z[0])+\log p(x[0]\mid z[0])+\sum_{t=1}^T\big(\log T(z[t-1],z[t])+\log p(x[t]\mid z[t])\big)
$$

#### 8.2 动态规划递推

- $\delta_t(z)=\max_{z[0:t-1]}\log p(z[0:t-1],z[t]=z,x[0:t])$——到时刻 $t$ 止于状态 $z$ 的**最优路径** log 概率。
- **最优子结构**：若最优路径在 $t$ 时刻经 $z$，则其前缀必是到 $t-1$ 时刻某状态 $z'$ 的最优路径。
- 递推：

$$
\delta_t(z)=\max_{z'}\big\{\delta_{t-1}(z')+\log T(z',z)\big\}+\log p(x[t]\mid z[t]=z)
$$

- **回溯指针**：

$$
a_t(z)=\arg\max_{z'}\big\{\delta_{t-1}(z')+\log T(z',z)\big\}
$$

- **初始化**：$\delta_0(z)=\log\pi(z)+\log p(x[0]\mid z[0]=z)$。
- **终止**：$z^*[T]=\arg\max_z\delta_T(z)$。
- **回溯**：$z^*[t]=a_{t+1}(z^*[t+1])$，$t=T-1,\ldots,0$。

#### 8.3 Viterbi 例子（PDF p37–38）

$z\in\{S_1,S_2,S_3\}$，$x\in\{C_1,\ldots,C_7\}$，$\pi(z)=1/3$，观测 $x[0{:}3]=(C_1,C_3,C_4,C_6)$。

- $\delta_0(S_1)=-\log 3+\log 0.5$；$\delta_0(S_2)=\delta_0(S_3)=-\infty$（因 $p(C_1\mid S_2)=p(C_1\mid S_3)=0$）。
- $\delta_1(S_1)=\delta_0(S_1)+\log 0.3+\log 0.3=-\log 3+\log 0.045$（$S_1\to S_1$，$T=0.3$，emission $p(C_3\mid S_1)=0.3$）。
- $\delta_1(S_2)=\delta_0(S_1)+\log 0.7+\log 0.2=-\log 3+\log 0.07$（$S_1\to S_2$，$T=0.7$，emission $p(C_3\mid S_2)=0.2$）。
- 其余 $S_3$ 各步由 Exercise 自行验证。

### 9. Finance 应用（notebook `04_finance_hmm.ipynb`）

- 用 **3 状态 HMM** 建模股票价格 regime；观测为日 **log return** 与 **volatility**。
- 对应 Week 3 的牛/熊市思路，但状态数扩展到 3，且状态间有 Markov 转移（不再是独立的 mixture）。

### 10. Practice Problems（PDF p42–44，考点）

**戒指传感器题**：可穿戴戒指追踪手指运动，状态 $z\in\{S,U,D\}$（still / moving up / moving down），IMU 测三维加速度 $x=(x_1,x_2,x_3)$。

a) **GMM 表示**：

$$
p(x)=\sum_{z\in\{S,U,D\}}\pi(z)\,p(x\mid z)=\sum_{z\in\{S,U,D\}}\pi(z)\,\mathcal{N}(x\mid\mu_z,\Sigma_z)
$$

b) **用 HMM 还是 Markov chain？** 用 **HMM**——因为传感器状态在处理端**不可直接观测**（latent），只能通过 IMU 测量间接推断。

c) **转移图**：$S$ 可长期停留（$T(S,S)$ 大），可转 $U$ 或 $D$；但 $U$ 只能转 $D$（$T(U,D)=1$），$D$ 只能转 $U$（$T(D,U)=1$）。即 $U\leftrightarrow D$ 互转，$S$ 自环 + 出边到 $U,D$。

d) **Baum-Welch 估计的参数**：$\pi(z)$（初始）、$p(z'\mid z)$（转移）、以及每状态的 emission 参数 $\mu_z,\Sigma_z$（Gaussian）。

e) **求最可能状态序列**：用 **Viterbi algorithm**。

### 11. MLE Derivation（补充，PDF p46–51）

#### 11.1 完整观测时的 MLE

当 $z$ 可观测，对 $\log p(D\mid\theta)$ 建 Lagrangian：
- 对 $\pi(z)$：$\hat\pi(z)=N_z^0/n$，$N_z^0=\sum_i\mathbf{1}\{z^i[0]=z\}$。
- 对 $T(z,z')$：$\hat T(z,z')=N_{zz'}/\sum_u N_{zu}$，$N_{zu}=\sum_i\sum_t\mathbf{1}\{z^i[t-1]=z,z^i[t]=u\}$。
- 对 Gaussian emission（$p(x\mid\phi_z)=\mathcal{N}(x\mid\mu_z,\Sigma_z)$）：

$$
\hat\mu_z=\frac{\sum_{i,t}\mathbf{1}\{z^i[t]=z\}\,x^i[t]}{\sum_{i,t}\mathbf{1}\{z^i[t]=z\}}=\frac{\bar x_z}{N_z}
$$

$$
\hat\Sigma_z=\frac{\sum_{i,t}\mathbf{1}\{z^i[t]=z\}(x^i[t]-\hat\mu_z)(x^i[t]-\hat\mu_z)^\top}{\sum_{i,t}\mathbf{1}\{z^i[t]=z\}}
$$

#### 11.2 Baum-Welch 的对应

Baum-Welch 只是把完整观测 MLE 中的**硬计数 $\mathbf{1}\{\cdot\}$** 换成**软后验 $\gamma,\xi$**：
- $\hat\pi(z)=\frac{\sum_i\gamma_{i,0}(z)}{n}$（对应 $N_z^0/n$）。
- $\hat T(z,z')=\frac{\sum_{i,t}\xi_{i,t}(z,z')}{\sum_{i,t,u}\xi_{i,t}(z,u)}$（对应 $N_{zz'}/\sum_u N_{zu}$）。
- $\hat\mu_z,\hat\Sigma_z$ 同理把 $\mathbf{1}\{z^i[t]=z\}$ 换成 $\gamma_{i,t}(z)$。

### 12. 考点速查表

| 概念 | 要点 |
|---|---|
| **Markov property** | $p(x[t]\mid x[1{:}t-1])=p(x[t]\mid x[t-1])$ |
| **Transition matrix** | 行随机；$p_t=p_0T^t$ |
| **MC MLE** | $\hat\pi(x)=N_x/n$，$\hat T(x,y)=N_{xy}/\sum_z N_{xz}$ |
| **HMM 三要素** | hidden states $z$ + transition $T$ + emission $p(x\mid\phi_z)$ |
| **三大问题** | Evaluation / Decoding / Learning → Forward / Viterbi / Baum-Welch |
| **Filtering/Smoothing** | $p(z[t]\mid x[0{:}t])$（Forward） / $p(z[t]\mid x[0{:}T])$（Forward-Backward） |
| **$\gamma,\xi$** | 单时刻后验 / 相邻两时刻联合后验 |
| **Forward $\alpha$** | $\alpha_t(z)\propto p(x[t]\mid z)\sum_{z'}T(z',z)\alpha_{t-1}(z')$ |
| **Backward $\beta$** | $\beta_t(z)=\sum_{z'}T(z,z')p(x[t+1]\mid z')\beta_{t+1}(z')$；$\beta_T=1$ |
| **Baum-Welch M** | $\hat\pi,\hat T$ 用 $\gamma,\xi$ 替换硬计数；Gaussian emission 用 $\hat\mu_z,\hat\Sigma_z$ |
| **Viterbi** | $\delta_t(z)=\max_{z'}\{\delta_{t-1}(z')+\log T(z',z)\}+\log p(x[t]\mid z)$；回溯 $a_t(z)$ |

### 13. 本周要点小结

- **Markov chain** = 带时间结构的 latent 模型；Markov property 使序列概率可分解为 $\pi(x[0])\prod_t T(x[t-1],x[t])$；状态分布演化 $p_t=p_0T^t$。
- **MC 的 MLE**：起始频率 $\hat\pi(x)=N_x/n$，转移频率 $\hat T(x,y)=N_{xy}/\sum_z N_{xz}$；零计数导致 overfitting，需 smoothing。
- **HMM** = 隐状态 Markov chain + emission model；观测不满足 Markov 性，长程依赖经 latent 捕捉。三要素 $\theta=(\pi,T,\phi)$。
- **三大问题**：Evaluation（Forward）/ Decoding（Viterbi）/ Learning（Baum-Welch = EM for HMM）。
- **Baum-Welch**：E step 用 forward-backward 算 $\gamma$（单时刻后验）与 $\xi$（相邻联合后验）；M step 把完整观测 MLE 的硬计数换成 $\gamma,\xi$ 的软期望。GMM 的 responsibility 推广到时间序列。
- **Forward-Backward**：$\gamma\propto\alpha\beta$；$\alpha$ 正向 predict-update 递推，$\beta$ 反向递推（$\beta_T=1$）；$\xi\propto\alpha\cdot\text{emission}\cdot\text{transition}\cdot\beta$。
- **Viterbi**：动态规划求 MAP 路径；$\delta_t(z)=\max_{z'}\{\delta_{t-1}(z')+\log T(z',z)\}+\log p(x[t]\mid z)$，回溯指针 $a_t(z)$。
- **应用**：language modeling（n-gram）、PageRank、speech/activity/gene、finance regime（3 状态 HMM）。

---

> **下一周预告**：Week 5 预计进入 Bayesian networks / 概率图模型或 classification 主题（Week 1 进度表后续）；HMM 的 forward-backward 与 Viterbi 是后续 graph model 推断的基础。具体主题以课件为准。

## Week 5 — Sampling（采样方法：标准分布 / Rejection / Importance Sampling）

> **权威来源说明**：本节先由 `week5/week5.txt` 录播转写整理，再以 `week5/5_Sampling.pdf`（官方课件，Tay W.P.，44 页）核对修正。转写噪声（"pyro"→prior、"livelihood"→likelihood、"gaucin"→Gaussian、"dozing/goal"→Gaussian、"bona wash/long watch"→Baum-Welch、"concrete ys"→conjugate prior、"combo of volume"→Kolmogorov、"strong or large numbers"→Strong Law of Large Numbers (SLLN)、"sling/sent/seclin/cyta"→sampling、"Miz/Miz/biz/piz/Maze"→mock quiz、"lure/LP"→LT（lecture theater）、"tarn is/NTN Cis"→NTULearn、"responders/Dog dow"→Respondus lockdown browser、"trig ac"→matric card 等），均以 PDF 为准修正。

### 0. ⭐ 行政公告（开课先讲）

老师开场给出 Quiz 1 与 review session 安排：

| 事项 | 安排 |
|---|---|
| **Quiz 1** | **Week 7 周一**，在 LT 现场进行，**60 分钟**，覆盖 **Week 1–4**（不含本周 Week 5 与下周 Week 6） |
| 形式 | NTULearn + **Respondus lockdown browser**；**fill-in-the-blank** 填空题（不是选择题） |
| 准备 | 课前务必先**安装并测试 lockdown browser**；有 mock quiz 可练手（熟悉填空格式，避免输入方式被判错） |
| **Reference sheet** | 可带 **1 张 A4 size reference sheet**（手写一切），**不允许 sticky notes** |
| 考勤 | Quiz 当场**点名 + 出示 photo ID**（passport 或 matric card） |
| **Review session** | **9 月 16 日（周一）10:00 AM**，线上 Teams，会录像；带问题来澄清 |

> ⚠️ Homework 1 在本周（Week 5）提交（按 Week 1 进度表）。本周起进入"如何求模型参数"的两周 sampling 专题。

### 1. 为什么需要 Sampling（动机）

前几周讲**如何建模数据**（standard distribution → mixture model → Markov/HMM），并用 MLE/MAP/EM 估参数。但仍有缺口：

- **Bayesian inference** 中 posterior 的闭式解通常只对 **conjugate prior** 或 exponential family likelihood 才有——这**限制了建模选择**。
- **高维分布**（如 image denoising 的 posterior $p(z|y)$）无法解析处理。

**图像去噪例子**（贯穿全章的动机）：每个像素 $z_j \in \{-1, 1\}$ 是干净图像的隐值，观测 $y$ 是加噪版本。

- **Likelihood**：$p(y|z)=\prod_j \mathcal{N}(y_j | z_j, \sigma^2)$——每个像素**独立**被 Gaussian noise 腐蚀。
- **Prior** $p(z)$：相邻像素高度相关（黑像素邻居多为黑），需建模邻域关系 → 不能分解成独立乘积 → **高维分布**。
- **Posterior**：
  $$p(z|y)=\frac{p(y|z)p(z)}{p(y)}$$
  因 $p(z)$ 含邻域耦合，$p(z|y)$ 无解析形式，$p(y)$ 是高维积分难算。
- **解决思路**：**即使写不出分布的解析式，只要能从中采样，就能近似它**——用样本估期望、找 MAP 等。

> 老师强调：sampling 与 MCMC 让你"几乎可以处理任何分布/模型"，不再受"能否解析推导"的限制。本周讲基础 sampling，**下周讲 MCMC**（高维分布的主力）。

### 2. 用样本估期望 — Strong Law of Large Numbers

对任意可测函数 $f$，若能生成 i.i.d. 样本 $x_1, x_2, \dots \sim p(x|\theta)$，则由 **SLLN（Strong Law of Large Numbers，强大数律）**：

$$\mathbb{E}[f(x)|\theta] = \int f(x)p(x|\theta)\,dx \approx \frac{1}{n}\sum_{i=1}^n f(x_i)$$

- 样本足够多时，经验平均渐近真实期望（Kolmogorov 证明）。
- **不要求事先知道期望的解析值**——抽样本、取平均即可。

**采样过程有效的判据**：一个 procedure 是否合法采样，看**多次抽样后直方图是否逼近目标 PDF**。单次或少量样本无法验证；最可靠的方式是**数学证明**该 procedure 有效（PDF 给出各方法的证明）。

### 3. Standard Distributions — CDF Inverse Method（逆 CDF 采样）

#### 3.1 原理

设 $X$ 的 CDF 为 $F(x)=P(X\le x)$。令 $U \sim \text{Unif}([0,1])$，取 $X = F^{-1}(U)$，则：

$$P(X \le x) = P(F^{-1}(U) \le x) = P(U \le F(x)) = F(x)$$

故 $X$ 服从 $F$。**采样步骤**：① 从 uniform 采样 $U$；② 施加 $F^{-1}(U)$ 得到 $F$ 的样本。

- Python：`random.random()` 或 `random.uniform(a,b)` 生成 uniform（底层是 pseudo-random number generator，统计上逼近真随机）。
- 该方法是其他复杂方法的**子程序**（subroutine）。

#### 3.2 Pseudo-inverse（补充，CDF 非双射时）

$F$ 未必双射。对 $u \in [0,1]$，定义 pseudo-inverse：

$$F^{-1}(u) = \inf\{x : u \le F(x)\}$$

性质：$u \le F(x) \iff F^{-1}(u) \le x$。

#### 3.3 例：Exponential（精确逆）

$X \sim \text{Exp}(\lambda)$，$F(x) = 1 - e^{-\lambda x}$，可解析求逆：

$$X = -\frac{1}{\lambda}\log(1-U), \quad U \sim \text{Unif}(0,1)$$

#### 3.4 例：Bernoulli（分段）

$X \sim \text{Bern}(\theta)$：若 $U \in [0, 1-\theta]$ 取 $X=0$；否则取 $X=1$。

### 4. Transformations（变量变换法）

若 $Y = f(X)$，则对每个 $y$：

$$p_Y(y) = \sum_{k=1}^K \frac{p_X(x_k)}{|f'(x_k)|}$$

其中 $x_1, \dots, x_K$ 是 $f(x)=y$ 的所有解。需知道 $f(x)=y$ 的解析解与 $f'$。

**例**：
- $Y = aX + b$：$p_Y(y) = \frac{1}{|a|} p_X\!\left(\frac{y-b}{a}\right)$。若 $p_X = \text{Unif}(0,1)$，则 $p_Y$ 也是 uniform（缩放平移）。
- $Y = X^2$：解 $x_1 = \sqrt{y}, x_2 = -\sqrt{y}$，$f'(x)=2x$：

  $$p_Y(y) = \frac{1}{2\sqrt{y}}\bigl(p_X(\sqrt{y}) + p_X(-\sqrt{y})\bigr)$$

### 5. 复杂分布的分解

能分解成简单分布就分解。

**例：Gamma($a$, $b$)，$a$ 为正整数**。若 $Y \sim \text{Gamma}(y|a,b) = \frac{b^a}{\Gamma(a)} y^{a-1} e^{-by}$，则 $Y = \sum_{i=1}^a X_i$，其中 $X_1, \dots, X_a \overset{\text{iid}}{\sim} \text{Exp}(b)$。

- 采样：用变换法生成 $a$ 个 $\text{Exp}(b)$ 样本，求和得 $Y$ 的样本。
- **但 $a$ 非整数时此法失效** → 用 rejection sampling。

### 6. ⭐ Rejection Sampling（拒绝采样）

#### 6.1 设定

只能算 $p(z)$ 到一个**乘性常数**：

$$p(z) = \frac{1}{M}\tilde{p}(z), \quad M \text{ 未知}$$

（回忆 posterior $p(\theta|D) = \frac{p(D|\theta)p(\theta)}{p(D)}$，$p(D)$ 难算——正是此情形。）

选一个**易采样的 proposal pdf** $q(z)$ 与常数 $k$，使：

$$k q(z) \ge \tilde{p}(z), \quad \forall z$$

且 $\text{supp}\, p \subseteq \text{supp}\, q$（$q$ 的支撑要覆盖 $p$）。

#### 6.2 算法

1. 从 $q(\cdot)$ 采 $z$。
2. 从 $\text{Unif}[0, kq(z)]$ 采 $u$。
3. 若 $u \le \tilde{p}(z)$ 则**接受** $z$；否则**拒绝**，重复。

> 几何直觉（转写老师强调）：等价于在 $\tilde{p}(z)$ 曲线下方均匀撒点，被接受的 $z$ 服从 $p(z)$。

#### 6.3 接受概率

$$P(z\text{ accepted}) = \int P(\text{acc}|z)q(z)\,dz = \int \frac{\tilde{p}(z)}{kq(z)}q(z)\,dz = \frac{M}{k}$$

- 平均需 **$O(k)$ 次**尝试才得到一个 $p(z)$ 样本。
- **要 $k$ 尽可能小**，但仍满足 $kq(z) \ge \tilde{p}(z)$。

#### 6.4 正确性证明

证明被接受样本的 CDF 恰为 $p(z)$ 的 CDF：

$$P(z \le z_0 | z\text{ accepted}) = \frac{\int_{z\le z_0} \tilde{p}(z)\,dz / k}{M/k} = \frac{1}{M}\int_{z \le z_0} \tilde{p}(z)\,dz = \int_{z\le z_0} p(z)\,dz$$

#### 6.5 例：Gamma（$a$ 非整数）

- 用 $q(z) = \text{Gamma}(z | c, b-1)$，$c = \lfloor a \rfloor$。比值 $\frac{p(z)}{q(z)} = \frac{\Gamma(c)b^a}{\Gamma(a)(b-1)^c} z^{a-c} e^{-z}$ 在 $z = a-c$ 处取最大 → 取该最大值为 $k$。
- 更好的 proposal：**Cauchy distribution** $q(z) = \frac{1}{\pi\gamma(1+(z-c)^2/\gamma^2)}$，$c=(a-1)/b$，$\gamma^2=(2a-1)/b^2$，最小 $k = \frac{\pi(a-1)^{a-1}\sqrt{2a-1}\,e^{1-a}}{\Gamma(a)}$。

#### 6.6 Rejection Sampling for Bayesian Inference

posterior $p(\theta|D) = \frac{p(D|\theta)p(\theta)}{p(D)}$，对 $\tilde{p}(\theta) = p(D|\theta)p(\theta)$ 做 rejection sampling。

- 若选 $q(\theta) = p(\theta)$（prior 作 proposal）：

  $$k = \max_\theta \frac{\tilde{p}(\theta)}{q(\theta)} = \max_\theta p(D|\theta)$$

  即 $\theta$ 的 **MLE**。直觉：prior 作 proposal 时，包络常数就是 likelihood 的最大值。

### 7. ⭐ Importance Sampling（重要性采样）

#### 7.1 动机

需算期望 $\mathbb{E}_p[f(z)] = \int f(z)p(z)\,dz$（如 EM 的 E step）。

- 直接从 $p$ 采样可能低效：若 $f(z)p(z)$ 在某些区域大，应**多采那些区域**。
- 例：$f(z) = \mathbf{1}\{z \in E\}$，$E$ 是**稀有事件（rare event）**。直接从 $p$ 采可能要等很久才碰到 $E$ 中的样本。

#### 7.2 算法

$p$ 难采样、$q$ 易采样时：

$$\mathbb{E}_p[f(z)] = \int f(z)\frac{p(z)}{q(z)}q(z)\,dz = \int f(z)w(z)q(z)\,dz \approx \frac{1}{n}\sum_{i=1}^n w(z_i)f(z_i)$$

其中 **importance weights** $w(z) = \frac{p(z)}{q(z)}$，样本 $z_1, \dots, z_n \overset{\text{iid}}{\sim} q$。

#### 7.3 与 rejection sampling 的区别（老师强调）

| | Rejection sampling | Importance sampling |
|---|---|---|
| 拒绝样本 | **有**，接受率 $M/k$ | **无**，所有样本都用 |
| $q \ge p$ 要求 | 需 $kq \ge \tilde{p}$（全局包络） | **不需要** $q \ge p$；权重随 $z$ 变化 $w(z)$ |
| 支撑要求 | $\text{supp}\, p \subseteq \text{supp}\, q$ | $\text{supp}\, f \cdot p \subseteq \text{supp}\, q$（$f=0$ 处可不管） |
| 收敛 | 取决于 $k$（高维时 $k$ 爆炸） | 取决于 $q$ 与 $\|f\|p$ 的匹配程度 |

#### 7.4 例：Tail Probability（稀有尾部事件）

估 $P(X > a)$（$a$ 大，稀有事件）。直接从 $p(x)$ 采要很多样本才碰到 $X > a$。

- 选 proposal $q(z)$ 支撑为 $(a, \infty)$（如 shifted exponential），所有样本都 $> a$。
- $P(X > a) \approx \frac{1}{n}\sum_i w(z_i)$，$w(z) = p(z)/q(z)$。

#### 7.5 实例：S&P 500 ETF（SPY）黑天鹅

`05_importance_sampling_SPY.ipynb`：估 SPY 日 log return 跌破大负阈值 $P(X < a)$ 的概率（rare event，直接采样要 $10^{14}$ 次才平均碰到一次）。用 shifted Gaussian 作 proposal + importance weights 估计。这是金融 risk management 的 **variance-reduction technique**。

#### 7.6 Unnormalized Version（只知常数倍）

若 $p, q$ 都只知到 normalizing constant（$p(z) = \tilde{p}(z)/M_p$，$q(z) = \tilde{q}(z)/M_q$），用**归一化权重**：

$$\bar{w}_n(z_i) = \frac{w(z_i)}{\sum_j w(z_j)}, \quad \mathbb{E}_p[f(z)] \approx \sum_{i=1}^n \bar{w}_n(z_i) f(z_i)$$

- 因 $\mathbb{E}_q w(z) = \int \frac{p(z)}{q(z)} q(z)\,dz = \int p = 1$，故 $\sum w \to n$，归一化后只用**未归一化的 $p, q$** 即可。
- 后验推断中极有用：$p(\theta|D) \propto p(D|\theta)p(\theta)$，$p(D)$ 不必算。

### 8. Sampling Importance Resampling（SIR）

Importance sampling 给出**加权样本**。若要**不加权样本**（from $p$）：

1. 从 $q$ 采 $z_1, \dots, z_n$。
2. 算归一化权重 $\bar{w}_n(z_1), \dots, \bar{w}_n(z_n)$。
3. 按 $\bar{w}_n$ **有放回重采样**得 $\tilde{z}$。

**为何有效**：$\tilde{z}$ 服从 $\{z_i\}$ 上的 multinomial，$P(\tilde{z} \le a | z_1, \dots, z_n) \to \int_{z \le a} p(z)\,dz$（$n \to \infty$，almost surely）。实践中取 $n \gg m$（重采样 $m$ 个则原样本 $n$ 要远大）。

#### SIR for Bayesian Inference

取 $\tilde{p}(\theta) = p(D|\theta)p(\theta)$，$q(\theta) = p(\theta)$（prior 作 proposal）：

$$\bar{w}_n(\theta_i) = \frac{p(D|\theta_i)}{\sum_j p(D|\theta_j)}$$

按此权重重采样 → 得 posterior $p(\theta|D)$ 的样本。

### 9. Sampling for EM

EM 的 E step 需算 $Q(\theta|\theta^{(m)}) = \int p(z|x,\theta^{(m)}) \log p(x,z|\theta)\,dz$。若该期望难解析，可从 $p(z|x,\theta^{(m)})$ 采样 $z_1, \dots, z_n$ 近似：

$$Q(\theta|\theta^{(m)}) \approx \frac{1}{n}\sum_{i=1}^n \log p(x, z_i | \theta)$$

> ⚠️ **rejection 与 importance sampling 在高维下收敛慢，不适合高维分布** → 引出 MCMC（下周，先复习 Markov chain）。

### 10. Practice Problems（课件末 5 题，含解答）

1. **$Y = -3X$，求 $p_Y$ 与 $p_X$ 关系**：$p_Y(y) = \frac{1}{3} p_X(-y/3)$（变换法 $|a|=3$）。
2. **只知 $\tilde{p}(z)$（$p=\tilde{p}/M$，$M$ 未知），证明用 $\tilde{p}/q$ 算 $\bar{w}_n$ 与用 $p/q$ 相同**：
   $$\frac{\tilde{p}(z_i)/q(z_i)}{\sum_j \tilde{p}(z_j)/q(z_j)} = \frac{Mp(z_i)/q(z_i)}{\sum_j Mp(z_j)/q(z_j)} = \frac{p(z_i)/q(z_i)}{\sum_j p(z_j)/q(z_j)} = \bar{w}_n(z_i)$$
   $M$ 在分子分母约掉。
3. **$p(x) = \text{Unif}(0,1)$，$q(x) = \text{Unif}(0, 1/2)$，$f(x) = x^2$，$\mathbb{E}_q[\frac{f p}{q}] = \mathbb{E}_p[f]$？** **否**：$\text{supp}\, p \not\subseteq \text{supp}\, q$（$p$ 在 $(1/2,1)$ 有质量，$q$ 没有），$\int_0^{1/2} f p\,dx \neq \int_0^1 f p\,dx$。支撑不覆盖会漏掉区间。
4. **代码题（解释每行，识别方法与分布）**：rejection sampling of $p'(x) \propto e^{-x^2}\mathbf{1}\{x \ge 0\}$（half-Gaussian），proposal $q = \mathcal{N}(50, 30)$。Line 14 循环；Line 15 采 $\mathcal{N}(50,30)$ 的 $z$；Line 16 采 $\text{Unif}(0, kq(z))$ 的 $u$；Line 18 接受条件 $u \le p(z)$。
5. **Black swan（黑天鹅稀有事件）**：$X \sim \mathcal{N}(0, \sigma^2)$，估 $\mathbb{E}[R(X)\mathbf{1}\{X > 6\sigma\}]$。策略：importance sampling，proposal $q$ 支撑为 $(6\sigma, \infty)$（如 shifted exponential by $6\sigma$），$\mathbb{E} \approx \sum \bar{w}_n(x_i) R(x_i)$，$w(x) = \mathcal{N}(x|0,\sigma^2)/q(x)$。

### 11. 考点速查表

| 概念 | 要点 |
|---|---|
| **SLLN 近似期望** | $\mathbb{E}[f]\approx \frac{1}{n}\sum f(x_i)$，$x_i \overset{\text{iid}}{\sim} p$ |
| **CDF inverse method** | $X = F^{-1}(U)$，$U \sim \text{Unif}(0,1)$；需 $F$ 可逆 |
| **Pseudo-inverse** | $F^{-1}(u) = \inf\{x: u \le F(x)\}$（非双射时） |
| **变换法** | $p_Y(y) = \sum_k p_X(x_k)/\|f'(x_k)\|$ |
| **Rejection sampling** | $kq \ge \tilde{p}$；接受率 $M/k$；平均 $O(k)$ 次；高维失效 |
| **Importance sampling** | $w = p/q$；不拒绝；不需 $q \ge p$；需 $\text{supp}\, fp \subseteq \text{supp}\, q$ |
| **归一化权重** | $\bar{w}_n = w/\sum w$；只需 unnormalized $p, q$ |
| **SIR** | 采样 + 归一化权重 + 有放回重采样 → 不加权样本 from $p$ |
| **稀有事件** | 用支撑在事件区的 proposal 做 importance sampling（variance reduction） |
| **Bayesian rejection** | $q=p(\theta)$（prior）⇒ $k = \max p(D\|\theta)$ = MLE |
| **Sampling for EM** | E step 难解析时从 $p(z\|x,\theta^{(m)})$ 采样近似 $Q$ |

### 12. 本周要点小结

- **动机**：高维 posterior 无解析形式（conjugate prior 才有闭式），但**能采样就能近似**——SLLN 保证经验平均渐近期望。
- **CDF inverse method**：$X = F^{-1}(U)$，$U \sim \text{Unif}(0,1)$；适合有解析逆的低维标准分布（Exp/Bernoulli），是复杂方法的 subroutine。
- **变换法**：$Y=f(X)$ 的 PDF 由 $f(x)=y$ 的解与 $f'$ 决定；可分解复杂分布（Gamma 整数 $a$ = $a$ 个 Exp 求和）。
- **Rejection sampling**：用 $kq \ge \tilde{p}$ 包络，接受率 $M/k$；只知 unnormalized $p$ 即可；**高维下 $k$ 爆炸、接受率骤降** → 失效。
- **Importance sampling**：不拒绝，用权重 $w = p/q$ 估期望；不需 $q \ge p$；适合稀有事件（tail probability）；归一化权重 $\bar{w}_n$ 只需 unnormalized $p, q$。
- **SIR**：importance sampling + 重采样 → 不加权样本 from $p$；Bayesian 中 $q = \text{prior}$，权重 $\propto$ likelihood。
- **局限**：rejection/importance 在高维收敛慢 → 下周 **MCMC**（先复习 Markov chain）。

---

> **下一周预告**：Week 6 进入 **MCMC（Markov Chain Monte Carlo）**——先复习 Markov chain（transition matrix、stationary distribution、ergodicity），再讲 **Metropolis-Hastings** 与 **Gibbs sampler**，处理本周方法失效的高维分布。MCMC 是 sampling 专题的第二周，也是 Week 7 Quiz 1（覆盖 Week 1–4，不含 Week 5–6）前最后一周新课。

---

## Week 6 — Markov Chain Monte Carlo（MCMC：Metropolis-Hastings 与 Gibbs Sampling）

> **权威来源说明**：本节先由 `week6/week6.txt` 录播转写整理，再以 `week6/6_MCMC.pdf`（官方课件，Tay W.P.，42 页）核对修正。转写噪声较多（"tic mark chain Marcel chain Multi Color"→Markov Chain Monte Carlo (MCMC)，"syncing/sencing/centering/sering"→sampling，"pyal/pyro/pier"→prior，"posior/poste"→posterior，"lot livelihood/lilihood/hod"→likelihood，"gaucin/galsiu/dozing/goal/Dalcen/galsin"→Gaussian，"Ming Mal/mean ski/Mosk"→Minkowski，"apoal/apo"→posterior，"bone Wah/bona wash/long watch"→Baum-Welch，"verte B"→Viterbi，"CLAP/clap"→Wooclap，"Tang"→Tay Wee Peng，"Depo"→Wang Lipo，"Ciford/pile Ciford"→Clifford，"speciation"→statistician，"pedo number"→pseudo-random number，"ez one to four"→Weeks one to four，"lock down browser/lock quiz"→lockdown browser/mock quiz，"com a review/comb a review"→conduct a review，"pizzer/pizza/pizzel/pit"→pixel，"dousing/dozing"→Gaussian，"sendling/sent"→sampling，"resembling"→resampling，"per side/per side x"→ψ(x)，"sikmoi"→sigmoid，"godic/agobi/gobi"→ergodic，"redu/reduc/reducer"→irreducible/reducible，"costly recurrent"→positive recurrent，"APD/AP/APOE/ePod"→aperiodic），均以 PDF 为准修正。本周主题是 MCMC——sampling 专题的第二周，也是 Quiz 1 前最后一周新课。

### 0. ⭐ 行政公告（Quiz 1 最终确认）

老师开场再次确认 Quiz 1 安排（与 Week 5 一致，此处补充细节）：

| 事项 | 安排 |
|---|---|
| **Quiz 1** | **下周（Week 7）lecture 时段**，约 **7:00 PM** 开始，**60 分钟** |
| 覆盖范围 | **Week 1–4**（Week 5 sampling 与 Week 6 MCMC **不含**于 quiz，但**期末考**会考） |
| 形式 | NTULearn + **lockdown browser**；需提前**安装并测试**（有 mock quiz 可练手，现场安装来不及） |
| **Review session** | **9 月 16 日（周三）10:00 AM**，Teams 线上，会录像上传 NTULearn；review questions 已发布 |
| 提交方式 | 在 lecture theater 现场用自带 laptop/tablet 完成 |

> 老师强调：本周是前半学期**最后一节完整新课**。Week 7 quiz 之后会做 summary review（讲解 past exam questions、复习要点），然后进入 recess week，后半学期由 Wang Lipo 讲深度学习。

### 1. MCMC 动机：为什么需要它

#### 1.1 回顾：上周 sampling 方法的局限

Week 5 讲了 standard distributions（CDF inverse method）、rejection sampling、importance sampling——这些方法只适用于**低维分布**（标量或至多二维）。

- 当维度达到**数百、数千**（如 image denoising 的 $z \in \mathbb{R}^{\text{像素数}}$），rejection sampling 的包络常数 $k$ 指数爆炸、接受率骤降；importance sampling 的权重方差爆炸。
- 但这些方法仍可作为**子程序**（subroutine）在 MCMC 内部使用（如从 proposal distribution 采样）。

#### 1.2 核心动机：高维 posterior

回到 Week 5 的 image denoising 例子（贯穿两周）：

- 干净图像 $z$（每个像素 $z_j \in \{-1, 1\}$），观测 $y$ 是加噪版本。
- **Posterior**：

$$
p(z|y) = \frac{p(y|z)p(z)}{p(y)}
$$

- **Likelihood** $p(y|z) = \prod_j \mathcal{N}(y_j | z_j, \sigma^2)$——各像素独立被 Gaussian noise 腐蚀，可分解。
- **Prior** $p(z)$：相邻像素高度相关（白像素邻居多为白），需建模邻域关系 → **不能分解成独立乘积** → 高维分布。
- 分母 $p(y) = \int p(y|z)p(z)\,dz$ 是**高维积分**，无法解析计算。

结论：$p(z|y)$ 是高维分布，无解析形式（conjugate prior 不适用），但**只要能从中采样就能近似它**（SLLN）。MCMC 就是高维分布采样的主力方法。

#### 1.3 MCMC 的历史地位

MCMC 被誉为**20 世纪最重要的十大算法之一**。

| 年份 | 人物 | 贡献 |
|---|---|---|
| 1953 | Metropolis（物理化学） | 提出 Metropolis algorithm（最初用于物理/化学） |
| 1970 | Hastings（统计） | 推广为更一般版本 → **Metropolis-Hastings** |
| 1984 | Geman & Geman | 提出 **Gibbs sampling**（MH 的特例） |
| 1990 | Gelfand & Smith | 普及 MCMC，使其成为现代统计/ML 的基石 |

老师引用 Peter Clifford（1993）的话：

> "…from now on we can compare our data with the model we actually want to use rather than with a model which has some mathematically convenient form. This is surely a revolution."

直觉：MCMC 让你不再受"能否解析推导"的限制——几乎可以处理任何分布/模型，只需从中采样即可。

### 2. Markov Chain 基础回顾（MCMC 的数学基础）

#### 2.1 Markov chain 与 transition kernel

- 离散时间随机变量序列 $Z_0, Z_1, Z_2, \ldots$，满足 **Markov property**：$Z_m$ 只依赖 $Z_{m-1}$，与更早的历史无关。
- **Transition probability**（转移概率）$T(x, y) = P(Z_m = y | Z_{m-1} = x)$，本周只考虑 **homogeneous MC**（$T$ 不随 $m$ 变）。
- 状态分布演化：$\pi_t(y) = \sum_x \pi_{t-1}(x) T(x, y)$，即 $\pi_t = \pi_{t-1} T = \pi_0 T^t$。

#### 2.2 ⭐ Stationary Distribution（平稳分布）

$\pi$ 是 **stationary distribution**（平稳分布）若：

$$
\sum_x \pi(x) T(x, y) = \pi(y), \quad \forall y
$$

即 $\pi T = \pi$——分布经过转移后**保持不变**。

- 求解：解线性方程组 $\pi T = \pi$（加上 $\sum \pi = 1, \pi \ge 0$）。
- **例**（3 状态 MC，PDF p7）：

$$
T = \begin{bmatrix} 0.2 & 0.2 & 0.6 \\ 0.3 & 0.5 & 0.2 \\ 0.5 & 0.0 & 0.5 \end{bmatrix}, \quad \text{解 } \pi T = \pi \Rightarrow \pi = \frac{1}{69}\begin{bmatrix} 25 & 10 & 34 \end{bmatrix}
$$

#### 2.3 Stationary Distribution 的存在条件（Supplementary）

| 条件 | 含义 |
|---|---|
| **Irreducible（不可约）** | 从任一状态出发，有限步内正概率到达任一其他状态 → 每个状态被无限次访问 |
| **Positive recurrent（正常返）** | 从状态 $i$ 出发，返回 $i$ 的期望时间有限 → 每个状态占用时间比例为正 |

- **有限状态**的 irreducible MC **一定** positive recurrent → 一定有 stationary distribution。
- 图例（PDF p6）：左图 1↔2↔3↔1 irreducible；右图 1↔2 但 3 孤立 → reducible。

#### 2.4 ⭐ Asymptotic Convergence（渐近收敛）与 Ergodicity

**问题**：从任意初始分布 $\pi_0$ 出发，$\pi_k = \pi_0 T^k$ 是否收敛到 $\pi$？

**收敛条件**（ergodic MC，遍历链）：

| 条件 | 含义 |
|---|---|
| Irreducible + positive recurrent | stationary distribution 存在 |
| **Aperiodic（非周期）** | 不在少数状态间振荡 |

- **周期性反例**（PDF p9）：$T = \begin{bmatrix}0&1\\1&0\end{bmatrix}$，在状态 1,2 间振荡，$T^k$ 在 $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ 和 $\begin{bmatrix}1&0\\0&1\end{bmatrix}$ 间交替，**不收敛**。
- **Aperiodic**：周期为 1（不存在这种振荡）。
- **Ergodic MC（遍历链）** = irreducible + positive recurrent + aperiodic ⇒ $\pi_k \to \pi$（无论初始分布）。

> 本课总是假设上述条件成立。经过足够长的 **burn-in period** $m$ 后，$k > m$ 时刻的分布近似为 $\pi$。

#### 2.5 ⭐ Reversible MC（可逆链）与 Detailed Balance

**Reversible（可逆）** 的充分（非必要）条件——**detailed balance（细致平衡）**：

$$
\pi(x) T(x, y) = \pi(y) T(y, x), \quad \forall x, y
$$

- 概率"从 $x$ 流向 $y$"等于"从 $y$ 流向 $x$"——平衡。
- 由此可推出 $\pi$ 是 stationary distribution：

$$
\sum_x \pi(x) T(x, y) = \sum_x \pi(y) T(y, x) = \pi(y) \sum_x T(y, x) = \pi(y)
$$

> **MCMC 的核心策略**：要采样 from target $\pi(x)$，设计一个 transition probability $T(x,y)$ 使得 MC **reversible**（满足 detailed balance）且 **aperiodic** → $\pi$ 是 stationary distribution → 运行 MC 足够长后样本近似 from $\pi$。

### 3. ⭐ Metropolis-Hastings Algorithm（MH 算法）

#### 3.1 算法

**目标**：采样 from $\pi(x)$，$x \in \mathcal{X}$（如 $\mathcal{X} = \mathbb{R}^{1000}$，高维）。

**假设**：
- 能计算 **unnormalized target** $\tilde{\pi}(x)$（即 $\pi(x) = \tilde{\pi}(x) / Z$，$Z$ 未知）。
- 选一个 **proposal distribution**（建议分布）$q(x, y) = q(y|x)$——irreducible、aperiodic、**易采样**。

**算法**（每步 $m$）：

1. 令 $x = Z_{m-1}$（当前状态）。
2. 从 $q(x, y)$ 采样 $y$（候选状态）。
3. 计算 **acceptance probability**（接受概率）：

$$
A(x, y) = \min\left(1, \frac{\tilde{\pi}(y) q(y, x)}{\tilde{\pi}(x) q(x, y)}\right)
$$

4. 以概率 $A(x,y)$ **接受** $y$：生成 $U \sim \text{Unif}[0,1]$，若 $U \le A(x,y)$ 则 $Z_m = y$；否则 $Z_m = x$（停留在原地）。

> 实现：从 $\tilde{\pi}(x)$、$q(x,y)$ 各算一次，取比值即可——不需 normalizing constant。

#### 3.2 MH 的关键性质

- $Z_0, Z_1, \ldots$ 是 **Markov chain**（$Z_m$ 只依赖 $Z_{m-1}$，因 proposal 与 acceptance 都只依赖 $x = Z_{m-1}$）。
- 与 rejection/importance sampling 一样，**不需知道 normalizing constant**。
- 适合高维：每步只需从"简单的" $q(x, \cdot)$ 采样，而非直接从 $\pi$ 采样。
- 与上周方法的精确性对比（老师强调）：
  - **Standard distributions + rejection sampling**：给出**精确**的 target 样本。
  - **Importance sampling / SIR / MCMC**：给出**近似**样本（SLLN 渐近），burn-in 越长近似越好。

#### 3.3 ⭐ Proof of MH（Supplementary，可逆性证明）

**Lemma**：MH 构造的 MC 是 reversible 的，$\pi(x)$ 是其 stationary distribution。

**Proof**（对 $x \ne y$）：

$$
\pi(x) T(x, y) = \pi(x) q(x, y) A(x, y) = \pi(x) q(x, y) \min\left(1, \frac{\pi(y) q(y, x)}{\pi(x) q(x, y)}\right)
$$

$$
= \min\big(\pi(x) q(x, y),\; \pi(y) q(y, x)\big) = \pi(y) q(y, x) \min\left(\frac{\pi(x) q(x, y)}{\pi(y) q(y, x)}, 1\right) = \pi(y) T(y, x)
$$

- 关键步骤：$\min(a, b) = \min(b, a)$，对称性使两边相等。
- 若 MC irreducible（positive recurrent）aperiodic ⇒ $Z_n$ 分布 → $\pi$。
- **设计巧妙**：acceptance probability 的形式恰好使 detailed balance 成立。

#### 3.4 Proposal Distribution 的选择

| 类型 | 形式 | 特点 |
|---|---|---|
| **Random walk MH** | $q(x, y) = q(y - x)$，如 $y - x \sim \mathcal{N}(0, \Sigma)$ 或 $\text{Unif}[-\delta, \delta]^d$ | 在状态空间随机游走；需选合适的方差 |
| **Independence chain MH** | $q(x, y) = q(y)$（与 $x$ 无关） | 取决于 $q$ 逼近 $\pi$ 的程度；需 $q$ 比 $\pi$ **heavy-tailed** |
| **Exploit $\pi$ 结构** | $\pi(x) \propto \psi(x) h(x)$，$h$ 可采样，$\psi$ 有界；取 $q(x,y) = h(y)$ | $A(x,y) = \min(1, \psi(y)/\psi(x))$ |

**Random walk MH 的特例——Metropolis Algorithm**：

当 $q(x, y) = q(y, x)$（对称 proposal，如 Gaussian、Uniform）：

$$
A(x, y) = \min\left(1, \frac{\tilde{\pi}(y) q(y, x)}{\tilde{\pi}(x) q(x, y)}\right) = \min\left(1, \frac{\tilde{\pi}(y)}{\tilde{\pi}(x)}\right)
$$

> 老师强调：Gaussian 与 Uniform 都是标准选择，采样方法已内置（含高维 multivariate Gaussian 也有标准程序）。

#### 3.5 ⭐ Proposal Variance 的调参

$\sigma$（proposal 的标准差）至关重要：

| $\sigma$ | 效果 |
|---|---|
| **太小** | 每步移动很小，探索空间慢；acceptance rate 太高；2000 步可能仍困在局部区域 |
| **太大** | 步子大但 acceptance rate 很低，长期卡在原地不动 |

**Rules of thumb（经验法则）**：

| MH 类型 | 目标 acceptance rate |
|---|---|
| Random walk MH | **0.25 – 0.5** |
| Independence chain MH | **接近 1** |

> PDF 演示（p20）：$\sigma$ 太小时 2000 样本全挤在一个小区域，从未到达另一高概率区。

#### 3.6 MH 示例（PDF p19）

$$
\pi(x) \propto \exp(-x^2)\, x^2\, (5 + \sin(2x))
$$

- 用 Gaussian random walk proposal $q(x, y) = \mathcal{N}(y | x, \sigma^2) = \mathcal{N}(x | y, \sigma^2) = q(y, x)$（对称）。
- $A(x, y) = \min(1, \tilde{\pi}(y)/\tilde{\pi}(x))$。
- 每步：采 $y \sim q(Z_m, y)$；采 $U \sim \text{Unif}[0,1]$；若 $U \le A(Z_m, y)$ 则 $Z_{m+1} = y$，否则 $Z_{m+1} = Z_m$。

### 4. ⭐ Burn-In 与 Thinning（MCMC 收敛诊断）

#### 4.1 Burn-In（预热/烧入期）

- **Burn-in phase**：丢弃 MC 初始阶段的样本（此时分布尚未接近 stationary distribution）。
- 典型值：丢弃前 **1000 – 5000** 步。
- **难点**：难以诊断何时"已烧入"。例（PDF p22）：$\text{Unif}(\{0,1,\ldots,20\})$ 的 MC 要跑 **400+ 步**才"忘记"起始点。
- 老师补充：MH 实现很简单、很快，即使丢弃 5000 步也不费时。

#### 4.2 Thinning（稀疏化）

- MC 样本**不独立**（相邻样本相关），通过**每隔 $d$ 步取一个**来降低相关性。
- $d$ 越大 → 样本间相关性越低，近似 i.i.d.；但浪费更多样本。
- 适用场景：$\sigma$ 太大导致长期卡在同一位置时，thinning 可避免重复值。

#### 4.3 获取近似 i.i.d. 样本的两种方式

1. **多条独立链**：生成 $r$ 条独立 Gibbs/MH 序列（各长 $m$），取每条最终值。
2. **单条长链 + thinning**：生成一条长序列，丢弃 burn-in，每 $d$ 步取一个。

### 5. ⭐ Gibbs Sampling（吉布斯采样）

#### 5.1 算法

Gibbs sampling 是 **MH 的特例**，用于采样 from 多维分布 $p(z_1, \ldots, z_d)$（高维时直接采样困难）。

**关键**：若能计算各分量的 **full conditional**（满条件分布）$p(z_i | z_{-i})$，其中 $z_{-i} = \{z_1, \ldots, z_{i-1}, z_{i+1}, \ldots, z_d}$，则：

1. 初始化 $(z_1^{(0)}, \ldots, z_d^{(0)})$。
2. 每次迭代 $k$，按顺序逐分量采样：

$$
z_1^{(k)} \sim p(\cdot | z_2^{(k-1)}, \ldots, z_d^{(k-1)})
$$

$$
z_2^{(k)} \sim p(\cdot | z_1^{(k)}, z_3^{(k-1)}, \ldots, z_d^{(k-1)})
$$

$$
\vdots
$$

$$
z_j^{(k)} \sim p(\cdot | z_1^{(k)}, \ldots, z_{j-1}^{(k)}, z_{j+1}^{(k-1)}, \ldots, z_d^{(k-1)})
$$

$$
\vdots
$$

$$
z_d^{(k)} \sim p(\cdot | z_1^{(k)}, \ldots, z_{d-1}^{(k)})
$$

3. 丢弃 burn-in 期的样本。

> 注意：更新 $z_j$ 时用**已更新的** $z_1^{(k)}, \ldots, z_{j-1}^{(k)}$ 与**尚未更新的** $z_{j+1}^{(k-1)}, \ldots, z_d^{(k-1)}$。

#### 5.2 Gibbs = MH with acceptance probability = 1（Supplementary）

Gibbs 的每一步等价于一个 MH step，其中 proposal $q_j(x_{-j}, y_j) = p(z_j | x_{-j})$（full conditional），且：

$$
A(x_j, y_j) = \frac{p(y_j)\, q_j(y_j, x_j)}{p(x_j)\, q_j(x_j, y_j)} = \frac{p(y_j)\, p(z_j | x_{-j})}{p(x_j)\, p(z_j | x_{-j})} = \frac{p(z_j | x_{-j})\, p(x_{-j})\, p(z_j | x_{-j})}{p(z_j | x_{-j})\, p(x_{-j})\, p(z_j | x_{-j})} = 1
$$

即 **acceptance probability 恒为 1**——Gibbs 总是接受，不需计算接受概率。这是它比一般 MH 高效的原因。

#### 5.3 如何求 Full Conditional

$$
p(z_1 | z_2, \ldots, z_d) = \frac{p(z_1, \ldots, z_d)}{p(z_2, \ldots, z_d)}
$$

**步骤**：
1. 写出 joint distribution $p(z_1, \ldots, z_d)$。
2. **忽略所有不含 $z_1$ 的项**（它们是关于 $z_{-1}$ 的常数）。
3. 识别剩余部分的**已知分布**（如 Gaussian、Beta、Binomial、Poisson 等）。

#### 5.4 Gibbs Sampling 示例（PDF p30）

$$
p(x, y, n) \propto \binom{n}{x} y^x (1-y)^{n-x} e^{-\lambda} \frac{\lambda^n}{n!}
$$

其中 $a, b, \lambda$ 为正常数。分解各 full conditional：

| 条件分布 | 形式 | 识别结果 |
|---|---|---|
| $p(x | y, n)$ | $\propto \binom{n}{x} y^x (1-y)^{n-x}$ | $\text{Bin}(x | n, y)$ |
| $p(y | x, n)$ | $\propto y^{x+a-1} (1-y)^{n-x+b-1}$ | $\text{Beta}(y | x+a, n-x+b)$ |
| $p(n | x, y)$ | $\propto \frac{((1-y)\lambda)^{n-x}}{(n-x)!}$ | $\text{Pois}(n | (1-y)\lambda) + x$ |

> 即使只想采样 $x$，也可用 Gibbs 采样 joint $(x, y, n)$ 再丢弃 $y, n$——因为直接求 $p(x)$（marginal）很困难，但 full conditionals 都是已知分布。

### 6. ⭐ 应用：Image Denoising with Ising Model（Ising 模型图像去噪）

这是贯穿 Week 5-6 的核心应用，MCMC 的典型场景。

#### 6.1 模型设定

- 干净图像 $z_j \in \{-1, 1\}$（hidden），观测 $y$ 是加噪版本。
- **Likelihood**（各像素独立被 Gaussian noise 腐蚀）：

$$
p(y|z) = \prod_j \mathcal{N}(y_j | z_j, \sigma^2)
$$

- **Ising prior**（建模邻域相关性）：

$$
p(z_j | z_{-j}) \propto \prod_{s \in \mathcal{N}_j} \psi(z_s, z_j), \quad \psi(u, v) = \exp(Juv), \quad J > 0
$$

其中 $\mathcal{N}_j$ 是像素 $j$ 的邻域（如 4-邻接），$J$ 是 coupling strength（耦合强度）。

- $J > 0$ 意味着**相同值的邻居更可能**（$z_s = z_j$ 时 $\psi = e^J > 1$；$z_s \ne z_j$ 时 $\psi = e^{-J} < 1$）。

#### 6.2 Ising Prior 的 Full Conditional

计算 $p(z_j | z_{-j})$（$z_j$ 二值，只有 $\pm 1$）：

$$
p(z_j | z_{-j}) = \frac{\prod_{s \in \mathcal{N}_j} \psi(z_s, z_j)}{\prod_{s \in \mathcal{N}_j} \psi(z_s, z_j) + \prod_{s \in \mathcal{N}_j} \psi(z_s, -z_j)}
$$

$$
= \frac{\exp\big(J \sum_{s \in \mathcal{N}_j} z_s z_j\big)}{\exp\big(J \sum_{s \in \mathcal{N}_j} z_s z_j\big) + \exp\big(-J \sum_{s \in \mathcal{N}_j} z_s z_j\big)}
$$

$$
= \frac{1}{1 + \exp\big(-2J \sum_{s \in \mathcal{N}_j} z_s z_j\big)} = \text{sigmoid}(2J \eta_j)
$$

其中 $\text{sigmoid}(u) = \frac{1}{1+e^{-u}}$，$\eta_j = \sum_{s \in \mathcal{N}_j} z_s z_j$。

#### 6.3 Posterior 的 Full Conditional（Gibbs 所需）

$$
p(z_j | z_{-j}, y) = p(z_j | z_{-j}, y_j) = \frac{p(z_j | z_{-j})\, p(y_j | z_j)}{p(y_j | z_{-j})}
$$

$$
= \frac{\text{sigmoid}(2J\eta_j)\, p(y_j | z_j)}{\text{sigmoid}(2J\eta_j)\, p(y_j | z_j) + \text{sigmoid}(-2J\eta_j)\, p(y_j | -z_j)}
$$

$$
= \text{sigmoid}\left(2J\eta_j - \log\frac{\mathcal{N}(y_j | -z_j, \sigma^2)}{\mathcal{N}(y_j | z_j, \sigma^2)}\right)
$$

- $z_j$ 二值 → 用此条件分布直接采样（伯努利）。
- **Gibbs sampling**：逐像素更新 $z_j$，迭代至收敛，取样本均值估计 posterior mean。
- Notebook：`06_ising_image_denoise_demo.ipynb`。

#### 6.4 Bayesian Neural Networks（补充应用）

- 传统神经网络只给一个输出值；**Bayesian neural network**（贝叶斯神经网络）估计输出的 **posterior probability** $p(\text{output} | \text{input})$。
- 这是高维 posterior，解析不可行 → 用 **MCMC 训练**，估计输出的 standard deviation（不确定性度量）。
- 老师提及这是 MCMC 在深度学习中的现代应用（后半学期 Wang Lipo 部分可能涉及）。

### 7. ⭐ Wooclap 例题

本周结尾有一道 Wooclap 判断题（转写 "one last set clap"）：

> **题**："To ensure fast convergence, you should accept every sample."（为确保快速收敛，应该接受每个样本。）

> **答案**：**False**。
>
> MH algorithm 的 acceptance probability $A(x,y)$ 必须严格遵循 $\min\big(1, \frac{\tilde{\pi}(y)q(y,x)}{\tilde{\pi}(x)q(x,y)}\big)$ 的形式，才能保证 Markov chain 收敛到 stationary distribution $\pi$。不能随意设 $A = 1$（除非是 Gibbs sampling 这种 full conditional 作 proposal 的特例）。乱改 acceptance probability 会破坏 detailed balance，MC 不会收敛到正确分布。

### 8. ⭐ MH vs Gibbs vs Rejection/Importance Sampling 对比

| 特性 | Rejection sampling | Importance sampling | **MH (MCMC)** | **Gibbs (MCMC)** |
|---|---|---|---|---|
| 样本精确性 | **精确** | 近似（SLLN） | 近似（burn-in 后） | 近似（burn-in 后） |
| 需要 normalizing constant | 否 | 否（归一化权重） | 否 | 否 |
| 需要 $kq \ge \tilde{p}$ | **是** | 否 | 否 | 否 |
| 高维适用性 | **差**（$k$ 爆炸） | **差**（权重方差大） | **好** | **好** |
| 样本独立性 | i.i.d. | i.i.d.（加权） | **不独立**（MC 相关） | **不独立**（MC 相关） |
| Acceptance | 概率 $M/k$ | 全接受（加权） | $A(x,y) = \min(1, \cdot)$ | **恒为 1** |
| 需要的条件 | $kq \ge \tilde{p}$，support 覆盖 | support 覆盖 $fp$ | proposal $q$ 易采样 | full conditional 可算 |
| 收敛诊断 | 不需要 | 不需要 | **burn-in + thinning** | **burn-in + thinning** |

### 9. Practice Problems（PDF p39-42，考点）

#### P1：MH 退化条件

**题**：若 $q(x, y) = \pi(y)$（proposal = target），证明 MH 退化为普通采样。

**解**：

$$
A(x, y) = \min\left(1, \frac{\pi(y) q(y, x)}{\pi(x) q(x, y)}\right) = \min\left(1, \frac{\pi(y) \pi(x)}{\pi(x) \pi(y)}\right) = \min(1, 1) = 1
$$

acceptance probability 恒为 1 → 每步都接受 → 等于直接从 $\pi$ 采样。

#### P2：Gibbs 采样推导 full conditionals

**题**：$p(z_1, z_2, z_3) \propto z_1^{z_2+a-2}(1-z_1)^{b-1} \frac{z_2^{z_1}}{z_2!} \mathbf{1}\{z_3 \in [0, z_1]\}$，求各 full conditional。

**解**：

| 条件分布 | 推导 | 结果 |
|---|---|---|
| $p(z_1 | z_2, z_3)$ | $\propto z_1^{z_2+a-2}(1-z_1)^{b-1} \mathbf{1}\{z_1 \ge z_3\}$ | $\text{Beta}(z_1 | z_2+a-1, b)$，截断 $z_1 \ge z_3$ |
| $p(z_2 | z_1, z_3)$ | $\propto \frac{z_2^{z_1}}{z_2!} \cdot z_1^{z_2}$ → $\propto \frac{(z_1 z_2)^{z_1}}{z_2!} = \frac{e^{z_1 z_2 \cdot \text{?}}}{z_2!}$ | $\text{Pois}(z_2 | z_1)$ |
| $p(z_3 | z_1, z_2)$ | $\propto \mathbf{1}\{z_3 \in [0, z_1]\}$ | $\text{Unif}(z_3 | (0, z_1))$ |

#### P3：综合题（rejection + importance + MH）

给定某 PDF $p(x)$（图示，峰值约 0.0407）：

**(a) Julia 用 rejection sampling 从截断分布 $p_1(x) \propto p(x)\mathbf{1}\{0 \le x \le 125\}$ 采样，proposal 用 Uniform：**

- $q(x) = \text{Unif}(0, 125)$，$k = 0.0407 / (1/125) = 5.0875$，使 $kq(x) \ge \tilde{p}_1(x)$。

**(b) Freddy 用 importance sampling 估 tail probability $\int_{100}^\infty p(x)\,dx$：**

- Proposal $q(x) = \lambda \exp(\lambda(x-100))\mathbf{1}\{x > 100\}$（shifted exponential），采 $z_1, \ldots, z_n$，算 $w(z_i) = p(z_i)/q(z_i)$，估 $\frac{1}{n}\sum_i w(z_i)$。

**(c) Russell 用 random walk MH 采样，$q(x,y) = \mathcal{N}(y-x | 0, 1)$，trajectory 有问题——为什么？**

- **标准差太小**（$\sigma = 1$），acceptance rate 过高，移动太慢，困在局部。
- **修正**：增大 $\sigma$ 使 acceptance rate 达到 **0.25–0.5**（如 $\sigma = 15$）。

### 10. 考点速查表

| 概念 | 要点 |
|---|---|
| **MCMC 动机** | 高维 posterior 无解析形式，rejection/importance 在高维失效；MCMC 用 MC 收敛到 stationary distribution |
| **Stationary distribution** | $\pi T = \pi$；存在需 irreducible + positive recurrent |
| **Ergodic MC** | irreducible + positive recurrent + aperiodic ⇒ $\pi_k \to \pi$ |
| **Detailed balance** | $\pi(x)T(x,y) = \pi(y)T(y,x)$ ⇒ $\pi$ 是 stationary distribution（充分非必要） |
| **MH acceptance** | $A(x,y) = \min\big(1, \frac{\tilde{\pi}(y)q(y,x)}{\tilde{\pi}(x)q(x,y)}\big)$；不需 normalizing constant |
| **Metropolis algorithm** | $q(x,y)=q(y,x)$（对称）⇒ $A = \min(1, \tilde{\pi}(y)/\tilde{\pi}(x))$ |
| **Random walk MH** | $q(x,y) = q(y-x)$，如 Gaussian/Uniform；acceptance rate 0.25–0.5 |
| **Independence chain MH** | $q(x,y) = q(y)$，与 $x$ 无关；需 heavy-tailed；acceptance 接近 1 |
| **Burn-in** | 丢弃初始 1000–5000 步；难诊断何时收敛 |
| **Thinning** | 每隔 $d$ 步取一个，降低 MC 样本相关性 |
| **Gibbs sampling** | MH 特例；逐分量从 full conditional $p(z_i | z_{-i})$ 采样；$A \equiv 1$ |
| **Full conditional 求法** | 写 joint，忽略不含目标变量的项，识别已知分布 |
| **Ising model** | $p(z_j | z_{-j}) = \text{sigmoid}(2J\eta_j)$，$\eta_j = \sum_{s \in \mathcal{N}_j} z_s z_j$ |
| **MH 可逆性证明** | $\pi(x)q(x,y)A(x,y) = \min(\pi(x)q(x,y), \pi(y)q(y,x)) = \pi(y)q(y,x)A(y,x)$ |

### 11. 本周要点小结

- **MCMC 动机**：上周的 rejection/importance sampling 只适合低维；高维分布（如 image denoising 的 $p(z|y)$）需 MCMC。核心思想：设计一个 reversible + aperiodic 的 Markov chain，使其 stationary distribution = target $\pi$，运行足够长后样本近似 from $\pi$。
- **Markov chain 基础**：stationary distribution $\pi T = \pi$（存在需 irreducible + positive recurrent）；ergodic MC（+ aperiodic）保证 $\pi_0 T^k \to \pi$；detailed balance $\pi(x)T(x,y) = \pi(y)T(y,x)$ 是 stationary 的充分条件——MCMC 的设计工具。
- **Metropolis-Hastings**：每步从 proposal $q(x,y)$ 采 $y$，以 $A(x,y) = \min\big(1, \frac{\tilde{\pi}(y)q(y,x)}{\tilde{\pi}(x)q(x,y)}\big)$ 接受/拒绝；不需 normalizing constant；proof 用 detailed balance；proposal 选择影响效率（random walk 需调 $\sigma$，acceptance rate 0.25–0.5）。
- **Burn-in & thinning**：丢弃初始样本（1000–5000 步）；thinning 降低样本相关性；两种获取近似 i.i.d. 样本方式（多条短链 or 单条长链 + thinning）。
- **Gibbs sampling**：MH 特例，$A \equiv 1$；逐分量从 full conditional $p(z_i | z_{-i})$ 采样；求法：写 joint、忽略无关项、识别已知分布；即使只想采样 marginal，也可 Gibbs 采样 joint 再丢弃多余分量。
- **Ising model 应用**：image denoising 的 posterior $p(z|y)$ 用 Gibbs 采样；Ising prior 给出 $p(z_j | z_{-j}) = \text{sigmoid}(2J\eta_j)$；posterior full conditional 结合 prior 与 likelihood；Bayesian neural network 是 MCMC 在深度学习中的现代应用。
- **与上周对比**：rejection/standard 给精确样本但高维失效；MCMC 给近似样本但高维可行；importance sampling 不拒绝、用权重估期望，MCMC 用 acceptance + MC 相关性。

---

> **下一周预告**：Week 7 是 **Quiz 1**（覆盖 Week 1–4，60 分钟，lockdown browser，填空题）+ **Summary Review**。Quiz 后老师会讲解 past exam questions 并复习 Week 1–4 的重点。Week 5–6 内容（sampling + MCMC）不在 Quiz 1 范围内，但**会在期末考**。Quiz 1 之后进入 recess week，后半学期（Week 8–13）由 Wang Lipo 讲授 Neural Networks / Deep Learning。

---

## Week 7 — Quiz 1 + Half-Semester Recap（前半学期回顾）

本周为 **Quiz 1 + recap week**，没有新知识点。前半节进行 Quiz 1，后半节老师系统回顾 Week 1–6 的逻辑框架，并讲解 past year exam questions。以下按老师 recap 的框架整理。

### 0. ⭐ Quiz 1 行政信息

| 项目 | 说明 |
|---|---|
| 形式 | **60 分钟**，fill-in-the-blank（填空题），使用 lockdown browser |
| 范围 | **Week 1–4**（概率复习 + MLE/MAP + EM/Mixture + Markov/HMM） |
| 不含 | Week 5–6（Sampling + MCMC）不在 Quiz 1 范围，但**会在 final exam** |
| 技术问题 | 登录失败可到前排取 paper quiz；passcode 会更换以防泄题 |
| 结束后 | 可自行提交，交卷后不要打扰同学，可离开教室 |

> ⭐ 老师明确提示：**final exam 覆盖全部内容**，包括 sampling/MCMC 部分。不要因为 Quiz 1 不考就忽略 Week 5–6。

### 1. ⭐ Machine Learning Pipeline（机器学习流水线总框架）

这是老师 recap 的核心——前半学期所有内容可纳入以下三阶段框架（对应 `_overview.pdf`）：

```
┌──────────────────────────────────────────────────────────────┐
│  1. Choose model M ∈ 𝓜  →  根据应用场景和数据类型选模型      │
│  2. Infer parameters θ   →  从 training set 估计最优参数      │
│  3. Utilize trained model →  在 inference time 应用并评估     │
└──────────────────────────────────────────────────────────────┘
```

#### 阶段 1：Choose Model（选模型）

模型分为两大类：

| 类型 | 模型举例 | 特点 |
|---|---|---|
| **Probabilistic models** | Standard distributions（Bern, Exp, Normal）、Mixture models（GMM）、Markov models、HMM | 可解释性强，用概率解释模型 |
| **Loss models**（后半学期） | MLP / DNN、CNN、RNN / LSTM | 现代深度学习模型，minimize loss/risk |

- 模型 $M$ 由参数 $\theta$ 定义，即 $M$ 给出 $p(\cdot \mid \theta)$。
- 典型参数化形式：

| 模型 | $p(x \mid \theta)$ 的形式 |
|---|---|
| Bernoulli | $\text{Bern}(x \mid \theta)$ |
| Gaussian | $\mathcal{N}(x \mid \mu, \Sigma)$ |
| GMM（mixture） | $p(x \mid \theta) = \sum_{k=1}^{K} \pi_k\, p(x \mid \eta_k)$ |
| Markov chain | $p(x_0, \ldots, x_t \mid \pi, T) = \pi(x_0)\, T(x_0, x_1)\, T(x_1, x_2) \cdots T(x_{t-1}, x_t)$ |
| HMM | 参数 $\theta = (\pi, T, \phi)$ |
| DNN（后半学期） | network weights $\theta$ |

> ⭐ 老师强调：probabilistic models 在很多应用中仍是首选，因为**可解释**（interpretable）——能用概率解释模型行为。后半学期的 neural networks 是更"黑箱"的现代方法。

#### 阶段 2：Infer Parameters $\theta$（参数估计）

从 training set 学习最优参数 $\theta^*$。前半学期覆盖的方法按递进逻辑排列：

| 方法 | 适用场景 | 核心思想 |
|---|---|---|
| **MLE** | 有完整数据、likelihood 可直接优化 | 最大化 $\log p(\mathcal{D} \mid \theta)$ |
| **MAP** | 有 prior belief / 领域知识 | 最大化 $\log p(\mathcal{D} \mid \theta) + \log p(\theta)$ |
| **EM algorithm** | 隐变量 / incomplete data（如 GMM） | E-step 算 conditional expectation，M-step 更新 $\theta$ |
| **Baum-Welch** | HMM（EM 的特化版本） | EM 专门用于 HMM 的参数估计 |
| **Sampling / MCMC** | 分布太复杂、无 closed form | 通过采样近似 posterior，算 expectation、confidence interval |
| **SGD**（后半学期） | 通用优化，minimize loss/risk | stochastic gradient descent，适用于所有模型但可能慢 |

递进逻辑：
1. **简单分布** → 直接 MLE/MAP（Week 2）。
2. **Mixture models**（GMM）→ likelihood 中 log 与 summation 不能交换，解析不可行 → **EM**（Week 3）。
3. **HMM** → 隐变量 + 时序结构 → **Baum-Welch**（EM 特例）（Week 4）。
4. **更复杂的分布** → 连 closed form 都写不出 → **Sampling / MCMC**（Week 5–6）。

> ⭐ 老师提示：SGD（stochastic gradient descent）是另一种通用方法，后半学期详讲。虽然 SGD 理论上可用于 mixture models 等所有模型，但 **EM 对特定问题更高效**——SGD 在 mixture model 上收敛很慢。通用方法不等于万能方法，**针对性方法在合适场景下更优**。

#### 阶段 3：Utilize Trained Model（应用与评估）

用训练好的 $p(\cdot \mid \theta^*)$ 在 inference time 做 prediction / inference，并评估泛化能力：

- **Goodness of fit**（拟合优度）
- **Classification metrics**：Accuracy、Precision、Recall、F1、AUC
- **Regression metrics**：RMSE、MAE

### 2. ⭐ Past Year Exam Questions 回顾

老师现场带做了几道 past year exam questions（AY24-25 和 AY23-24），以下是题目要点和解题思路。

#### Q1（AY24-25）：MLE / MAP — Pedestrian & Cyclist Vulnerability

**题设**：
- 行人（pedestrian）为 vulnerable 的概率 $\theta_0$（未知），骑车人（cyclist）为 vulnerable 的概率 $\theta_1$（未知）。
- 调查 100 个行人（20 vulnerable）、50 个骑车人（5 vulnerable），数据独立。
- (a) 求 MLE of $\theta_0, \theta_1$。
- (b) 加 Beta prior $\theta_k \sim \text{Beta}(a, b)$（$a=2, b=1$），求 MAP。
- (c) 另一人只记录 vulnerable 与否、不记录身份 → mixture distribution，需用 EM。

**解**：

**(a) MLE**：因数据独立，行人和骑车人可分开处理。

$$
\hat{\theta}_k^{\text{MLE}} = \frac{r_k}{n_k}
$$

- $\hat{\theta}_0^{\text{MLE}} = 20/100 = 0.2$
- $\hat{\theta}_1^{\text{MLE}} = 5/50 = 0.1$

**(b) MAP**：$\log \text{likelihood} + \log \text{prior}$，对 $\theta_k$ 求导置零：

$$
\hat{\theta}_k^{\text{MAP}} = \frac{r_k + a - 1}{n_k + a + b - 2}
$$

- $\hat{\theta}_0^{\text{MAP}} = \frac{20+1}{100+1} = \frac{21}{103}$
- $\hat{\theta}_1^{\text{MAP}} = \frac{5+1}{50+1} = \frac{6}{51}$

**(c) Mixture + EM**：不记录身份时，$x_i \sim \frac{4}{5}\text{Bern}(\theta_0) + \frac{1}{5}\text{Bern}(\theta_1)$（混合比来自 Part 1 的 4:1 比例）。

$$
\log p(x_i \mid \theta) = \log\left[\frac{4}{5}\theta_0^{x_i}(1-\theta_0)^{1-x_i} + \frac{1}{5}\theta_1^{x_i}(1-\theta_1)^{1-x_i}\right]
$$

log 与 summation 不能交换 → 直接求导 intractable → **用 EM algorithm**。

> ⭐ 考试要点：遇到 mixture distribution 时，**必须说明为什么用 EM**——log-likelihood 中 log 包裹 summation，无法直接求导。

#### Q2（AY24-25）：Metropolis-Hastings Acceptance Probability

**题设**：target $\tilde{\pi}(x) = e^{-|x|}$（unnormalized Laplace），proposal $q(x,y) = \mathcal{N}(y \mid x, 1)$（Gaussian random walk），当前 $x=1$，提议 $y=2$，求 acceptance probability。

**解**：

$$
A(x,y) = \min\left(1, \frac{\tilde{\pi}(y)\, q(y,x)}{\tilde{\pi}(x)\, q(x,y)}\right)
$$

代入 $\tilde{\pi}(1) = e^{-1}$，$\tilde{\pi}(2) = e^{-2}$；$q$ 对称（Gaussian，$\sigma^2=1$），$q(x,y) = q(y,x)$，指数部分 $e^{-(x-y)^2/2}$ 上下相同可消去。

$$
A = \min\left(1, \frac{e^{-2}}{e^{-1}}\right) = \min(1, e^{-1}) = e^{-1} \approx 0.3679
$$

> ⭐ 老师提示：**acceptance probability 公式要写在 reference sheet 上**，不需死记。

#### Q3（AY24-25）：HMM + Gibbs Sampling — Damaged Manuscript

**题设**：手稿由字符序列组成，真实状态 $z_i \in \{D, U\}$（damaged/undamaged，latent），观测 $x_i \in \{D, U\}$（observed）。这是一个 **HMM**。

- **Emission probabilities**：

| 真实状态 $z_i$ | $P(x_i=D \mid z_i)$ | $P(x_i=U \mid z_i)$ |
|---|---|---|
| $D$ | $\alpha$ | $1-\alpha$ |
| $U$ | $\beta$ | $1-\beta$ |

- **Transition（Markov chain on $z$）**：$z_i$ 仅依赖 $z_{i-1}$ 和 $z_{i+1}$（Markov property），条件概率：

$$
p(z_i \mid z_{-i}) \propto \gamma^{\mathbf{1}[z_i = z_{i-1}] + \mathbf{1}[z_i = z_{i+1}]}
$$

即邻居一致时乘 $\gamma$。

- **任务**：用 **Gibbs sampling** 估计 $z$ 的 posterior。

**解**：用 Bayes rule 求 full conditional $p(z_i \mid z_{-i}, x_i)$：

$$
p(z_i = D \mid z_{-i}, x_i) \propto p(z_i = D \mid z_{i-1}, z_{i+1}) \cdot p(x_i \mid z_i = D)
$$

$$
= \gamma^{\mathbf{1}[z_{i-1}=D] + \mathbf{1}[z_{i+1}=D]} \cdot \alpha^{\mathbf{1}[x_i=D]} (1-\alpha)^{\mathbf{1}[x_i=U]}
$$

同理 $p(z_i = U \mid z_{-i}, x_i)$ 将 $D$ 换成 $U$、$\alpha$ 换成 $\beta$。

**Gibbs sampling 步骤**：
1. 初始化所有 $z_1, \ldots, z_n$。
2. 第 $k$ 次迭代：
   - 采样 $z_1^{(k)} \sim p(z_1 \mid z_2^{(k-1)}, z_n^{(k-1)}, x_1)$（边界 wrap-around：$z_0 \equiv z_n$）。
   - 采样 $z_2^{(k)} \sim p(z_2 \mid z_1^{(k)}, z_3^{(k-1)}, x_2)$（用已更新的 $z_1^{(k)}$）。
   - 依次类推至 $z_n^{(k)}$（用 $z_{n-1}^{(k)}$ 和 $z_1^{(k)}$）。
3. 丢弃 burn-in 样本。

> ⭐ 考试要点：此题与 lecture 中的 image denoising（2D Ising model）**结构完全相同**，只是 1D 序列而非 2D 图像。核心是**写出 full conditional 并描述 Gibbs 步骤**，注意区分 $z_i^{(k)}$（已更新）与 $z_i^{(k-1)}$（未更新）。

#### Q4（AY23-24）：Exponential MLE / MAP / EM — Non-Line-of-Sight

**题设**：信号反射路径 $R = D + \epsilon$（$D$ = direct line-of-sight 距离，$\epsilon$ = 额外路径长度，恒非负）。

**(a) 为什么用 Exponential 而非 Gaussian 建模 $\epsilon$？**

$\epsilon \ge 0$ 恒成立（反射路径 ≥ 直射路径）。Gaussian 的 support 是 $(-\infty, \infty)$，可能产生负值，**物理不合理**。Exponential 的 support 是 $[0, \infty)$，与约束一致。

> ⭐ **模型选择原则**：选分布时必须考虑数据的物理约束（support、非负性等），不能盲目用 Gaussian。

**(b) MLE of $\lambda$**（4 个观测值 $\epsilon_1, \ldots, \epsilon_4$）：

$$
\log L = \sum_{i=1}^{4} \log(\lambda e^{-\lambda \epsilon_i}) = 4\log\lambda - \lambda \sum_{i=1}^{4} \epsilon_i
$$

$$
\hat{\lambda}^{\text{MLE}} = \frac{4}{\sum \epsilon_i}
$$

**(c) MAP**（prior $p(\lambda) \propto \lambda \, e^{-\lambda}$，即 Gamma(2,1)）：

$$
\log L + \log p(\lambda) = 4\log\lambda - \lambda \sum \epsilon_i + \log\lambda - \lambda + \text{const}
$$

$$
\hat{\lambda}^{\text{MAP}} = \frac{5}{\sum \epsilon_i + 1}
$$

**(d) 只观测 $R$、不观测 $D$ → incomplete data → EM**：

E-step：计算 conditional expectation $E[\log p(R, D \mid \lambda) \mid R, \lambda^{(t-1)}]$，即对 complete data log-likelihood 关于 $D \mid R, \lambda^{(t-1)}$ 取条件期望。

> ⭐ **EM 的本质**：当 observed data 是 incomplete data（缺少部分变量）时，用 EM 估计 MLE。E-step 算 $Q(\theta \mid \theta^{(t-1)}) = E[\log p(\text{complete} \mid \text{observed}, \theta^{(t-1)})]$，M-step 最大化 $Q$。

### 3. ⭐ 前半学期逻辑链总结

老师 recap 的递进逻辑：

```
Week 1: 概率论基础（Bayes rule, distributions）
  ↓
Week 2: MLE / MAP — 有完整数据 + 简单分布
  ↓
Week 3: EM algorithm — 隐变量 / mixture models（log ∑ 不可分）
  ↓
Week 4: HMM — 隐变量 + 时序 → Baum-Welch（EM 特例）+ Viterbi
  ↓
Week 5: Sampling — 标准分布采样 / Rejection / Importance（低维有效）
  ↓
Week 6: MCMC — Metropolis-Hastings / Gibbs（高维 posterior 近似）
  ↓
Week 7: Quiz 1 (Week 1-4) + Recap
  ↓
Week 8-13: Neural Networks / Deep Learning（Wang Lipo）
```

### 4. ⭐ 考试相关提示

| 要点 | 说明 |
|---|---|
| **Final exam 覆盖全部内容** | 包括 sampling / MCMC（Week 5–6），不要遗漏 |
| **Reference sheet** | acceptance probability 公式等应写在 reference sheet 上，不需死记 |
| **Past year papers** | 应能在 NTULearn / NTU library website 找到近 3–5 年 past paper；老师提到有同学反映找不到，会去确认 |
| **概念题写法** | 简答题只需几句话说明，不要写整段/整页（如 burn-in / thinning 解释） |
| **计算题** | 代入公式即可，注意 proposal 对称时 $q$ 项可消去 |

### 5. 本周要点小结

- **本周性质**：Quiz 1 + half-semester recap，无新知识点。
- **总框架**：Machine learning pipeline = Choose model → Infer $\theta$ → Utilize & evaluate。前半学期聚焦 probabilistic models + 参数估计方法（MLE → MAP → EM → Baum-Welch → MCMC）。
- **模型分类**：Probabilistic models（可解释）vs Loss models（后半学期的 DNN/CNN/RNN，黑箱但 powerful）。
- **方法递进**：简单分布直接 MLE/MAP → mixture/隐变量用 EM → 更复杂分布用 MCMC → 通用优化用 SGD（后半学期）。
- **EM 使用场景**：incomplete data / 隐变量 / log-likelihood 中 log 包裹 summation 无法直接求导时。
- **MCMC 使用场景**：分布无 closed form、高维 posterior，通过采样近似期望与不确定性。
- **考试提醒**：final exam 覆盖全部内容；acceptance probability 等公式写 reference sheet；概念题简答即可。

---

### 下一周预告

Recess week 后，**Week 8 起由 Wang Lipo 教授讲授 Neural Networks / Deep Learning**（Week 8–13），进入课程后半段。内容将涵盖 MLP / DNN、CNN、RNN / LSTM 等 loss-based models，以及 stochastic gradient descent 等训练方法。probabilistic models 部分（前半学期）到此结束，但 final exam 会覆盖全部内容。

---

## Week 8 — Part 2.1: Introduction to Neural Networks and Deep Learning（神经网络与深度学习导论）

本周是**下半学期第一讲**，任课教师由 **Tay Wee Peng** 换成 **Wang Lipo**。内容对应官方课件 `Part 2.1_Intro_NN_DL(1).pdf`（Wang Lipo，50 页）：从生物神经元到 artificial neuron model、decision boundary 的几何、OR/AND 单神经元设计、single-layer perceptron 的局限（**XOR 线性不可分**）、多层解法，以及 universal approximation（万能逼近）。

> **权威来源说明**：本节先由 `week8/week8.txt` 录播转写整理，再以 `week8/Part 2.1_Intro_NN_DL(1).pdf`（官方课件，Wang Lipo，50 页）核对修正，并参考配套 notebook `week8/mlp_mnist_tf.ipynb`。**注意：本周起老师换人，人名与术语在转写中错拼极多**："depo/Wang Li Po"→**Wang Lipo**、"School of tb / School of Trip E"→School of EEE、"new network / near network / neo network / nan / miron / irons"→neural network / neuron、"perception / precept"→perceptron、"sycmoid / sigmo / sikmoi"→sigmoid、"Rosenblad"→Rosenblatt、"Minsk and Pepper / pets"→Minsky and Papert、"Rumor Hart / Ruma Hart"→Rumelhart、"Hot field / Half field / H field / Hock"→Hopfield、"SL state / Sul State / SR state / S State"→solid state、"boards Mnuchin / boards Mnuche / bold M"→Boltzmann machine、"mycolic pz / mycolic pizza"→McCulloch-Pitts、"Jeffrey Hinto / Hint"→Geoffrey Hinton、"Alex at"→AlexNet、"alpha goal"→AlphaGo、"L D"→Lee Sedol、"CBT / CPT / GBT / CGP / cheat TPT / GPD"→ChatGPT / GPT、"PSOE / P SLE / PSE"→PSLE、"walk club / w clap / walk clock"→**Wooclap**、"cancel flow"→TensorFlow、"Pyka"→PyPI、"syne / synapsis"→synapse、"denis / dentoi / dendros / dentid"→dendrite，"nuclus / anuclus"→nucleus、"typ / typo / tiger"→dipole、"image net"→ImageNet。人名、公式、网络结构一律以 PDF 与 notebook 为准。

### 0. ⭐ 换老师 + 下半学期行政信息（Wang Lipo 亲述）

下半学期的一切安排由新老师重新交代，以下是完整行政信息。

| 项目 | 内容 |
|---|---|
| 任课教师 | **Wang Lipo**（School of EEE，information engineering 方向） |
| Email | `elpwang@ntu.edu.sg`（老师自述**最方便的答疑方式**；"you can draw some graph and take a picture and send to me"） |
| 办公室 | **S1-B1C-98**；电话 6916 3162 ext.3013（老师打趣：搬到新号码后"no one has called me yet"） |
| 答疑方式 | 发 email / 预约时间 / **随时 drop by**——"you're welcome to just come in and we can discuss"；但"sometimes I'm not there"，要保证有人在就预约；建议与意见"the earlier the better"（学期末才提只能改进到下个学期） |
| 讲座时长 | 本时段为 **3 × 50 min**；课上投票决定：**只休息一次**，约 1.5 小时后休息 **10 分钟** |
| 课程结构（Week 8–13） | 三块：① **NN/DL 导论**（本周）② **训练**——"how do you train a shallow neural network, how you train a deep neural network. So they're very similar" ③ **CNN**（convolutional neural network） |
| 其他网络结构 | RNN/LSTM 等**课上不覆盖**——"I put them in a supplementary folder. So if you want, you can read about them" |
| **Python 编程** | **不考**——"We're not going to test you Python programming in the final exam or in the quiz, **not even in the quiz**." 但 **homework 会包含编程** |
| 用 AI 写作业程序 | **不禁止**——"unless you're going to use AI, you're going to use ChatGPT to do the program, I can't stop you. If you want to do that, that's fine... Well, that's a skill as well." |
| 出勤（Wooclap） | **本周老师忘记开 Wooclap**——下课才想起："I forgot... Maybe next time. Next time, we'll do Wooclap." 出勤仍按 Wooclap 记录（Class Participation **5%**，共 13 次讲座需参加 **≥9 次**，attempt 即得分），下次补上 |

> ⭐ 关于"为什么讲得慢"：老师明确说这三块会讲得"reasonably slowly"，重点在**原理**而非 API。理由是——如果不关心原理，neural network 就是一个 **black box**（黑箱），输入进、输出出，"you can probably learn it in a few minutes... everything now is packaged in Python, you just use this library"；但只有懂原理，才能像当年那些"smart guys"一样**发明新的网络结构**。他也用亲身经历说明：EE School 六个 division 的老师现在都会答"yes"说自己懂 AI，"because everybody now can do it"——差别就在原理。

### 1. Deep learning 是什么

老师给的最简定义：

> "What basically deep learning is, is a neural network. **It's just a deeper neural network.** If you have a small neural network, you can call it network training, but if it's very deep, then it's called deep learning."

所以 "deep learning" 并不是新物种，只是层数多的 neural network——这也解释了后半学期为什么把 shallow 与 deep 的训练放在一起讲（"they're very similar"）。

### 2. 从 biological neuron（生物神经元）到 artificial neuron model（人工神经元模型）

#### 2.1 Biological neuron 的结构

| 生物结构（英文） | 作用 | 对应人工神经元 |
|---|---|---|
| **dendrite**（树突） | "impulses carried toward cell body"，接收其他神经元的输入 | 输入 $x_1, \ldots, x_m$ |
| **cell body / nucleus**（胞体/细胞核） | 对输入做处理（整合、判断） | summing function + activation function |
| **axon**（轴突） | "impulses carried away from cell body"，把输出送给别的神经元 | 输出 $y$ |
| **synapse**（突触） | presynaptic terminal 与其他神经元接触的部位，信息经化学方式传递 | 权重 $w_j$（synaptic weights） |

规模（PDF 首页数据）：**人脑约有 $10^{11}$ 个 neuron 与 $10^{15}$ 个 synaptic connections**。老师课上的一手见闻：做脑实验时要把染料（ink）注入单个 neuron 才能看清它的一棵树状结构，"it's very hard for the ink to travel to a different neuron"，所以对脑的认识极其有限。

#### 2.2 Artificial neuron model（人工神经元模型）

人工神经元只保留"线性组合 + 非线性阈值"两步：

$$
v = \sum_{j=0}^{m} w_j x_j, \qquad w_0 = b,\ x_0 = +1
$$

$$
y = f(v)
$$

其中：

- $x_1, \ldots, x_m$：**input signal**（输入信号）；
- $w_1, \ldots, w_m$：**synaptic weights**（突触权重）；
- $b = w_0$：**bias**（偏置），实现方式是**加一个恒为 $+1$ 的输入 $x_0$**，于是 bias 被吸收进加权和里，形式统一；
- $v$：**local field**（局部场，即加权和）；
- $f(\cdot)$：**activation function**（激活函数），非线性；
- $y$：output。

> ⭐ **bias 与 threshold 的关系**（老师口述）：bias 就是一个常数项，即使没有输入，neuron 仍"有某种 level of excitation"。若把它看成负的（$-b$），那么输入必须**超过这个 threshold** 才能让 $v > 0$、输出为正。所以"bias"和"threshold"讲的是同一件事的两面。

#### 2.3 Activation function（激活函数）

课件给出的第一个例子是 **sigmoid activation function**，一个非线性的 S 形映射：

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

其导数为（补充，训练部分要用）：

$$
\frac{d\sigma(x)}{dx} = \sigma(x)\bigl(1 - \sigma(x)\bigr)
$$

常见的 activation function 对比：

| 名称 | 表达式 | 值域 | 特点 |
|---|---|---|---|
| **step function**（阶跃/阈值函数） | $f(v) = \mathbf{1}[v \ge 0]$ | $\{0, 1\}$ | McCulloch-Pitts 原始模型用的就是这个；不可导，无法梯度训练 |
| **sigmoid** | $\sigma(v) = \dfrac{1}{1+e^{-v}}$ | $(0, 1)$ | 连续可导，把 $v$ 的符号"软化"成 0/1 之间的概率式输出 |
| **tanh** | $\tanh(v) = \dfrac{e^{v}-e^{-v}}{e^{v}+e^{-v}}$ | $(-1, 1)$ | 零中心化版本 |
| **ReLU**（rectified linear unit） | $\text{ReLU}(v) = \max(0, v)$ | $[0, \infty)$ | 分段线性、计算便宜，现代深层网络最常用（见 §11 notebook） |

老师强调：$f$ 可以有很多种，但"the inside of which is a **linear combination** process"，非线性只作用在这一步之后——这正是后面 XOR 与 universal approximation 的关键。

#### 2.4 课件里的 PyTorch 示例（不考编程，但看结构）

课件用一段 PyTorch 片段说明"一个 layer 加上一个 activation 就是几行代码"，并明确标注 **"You will not be tested with Python programming"**：

```python
import torch
in_dim, out_dim = 100, 200          # Input and output dimensions
linear = torch.nn.Linear(in_dim, out_dim)
relu = torch.nn.ReLU()              # Activation function
x = torch.randn(50, in_dim)         # Input tensor (50 samples, 100 features)
x = linear(x)                       # Linear transformation (50, 200)
x = relu(x)                         # Apply ReLU activation
```

即：`Linear` 做 $Wx + b$，`ReLU` 做非线性，两层叠起来就是一个 hidden layer。

### 3. Biological vs. Artificial Neural Networks（生物 vs. 人工神经网络）

#### 3.1 结构与速度的差异

| 维度 | Biological | Artificial |
|---|---|---|
| **connectivity**（连接方式） | 极其复杂、看似无序，"you can't really tell who's connected to whom, where is the input and where's the output" | **organized into regular layers**，神经元等大同形状、连接规整 |
| 组织原因 | 生物演化结果 | **设计上的 simplicity**——只有规整才能用数学描述。"If you want to use mathematics to describe a total mess, that is very hard" |
| 响应速度 | 约 $10^{-3}$ s（毫秒级） | 约 $10^{-9}$ s（纳秒级），快约 **$10^6$ 倍** |
| 并行性 | **massively parallel**，$10^{11}$ neurons × 约 $10^4$ connections/neuron；任一时刻约 20% 神经元在 firing | 逐层串行（layer by layer）；只有**同一层内**的 neuron 是并行计算的 |
| 已知程度 | 单颗 neuron 已知的 process 就要用 supercomputer 模拟 | 数学上完全可控 |

> ⭐ 老师反复强调第一点：人工网络"organized into layers for **design simplicity**"，是为了能用数学描述、能设计、能训练——不是因为它更接近真实大脑。

#### 3.2 GPT 的参数量：从 $10^8$ 到 $10^{12}$

课件用 GPT 系列的参数量做对比（注意：这里的"参数（connections）"就是 §2.2 里的 weights + biases 总数）：

| 模型 | 年份 | 约参数（Approx. Parameters） |
|---|---|---|
| GPT-1 | 2018 | $10^8$ |
| GPT-2 | 2019 | $10^9$ |
| GPT-3 | 2020 | $10^{11}$ |
| GPT-3.5（first ChatGPT） | 2022 | $10^{11}$ |
| GPT-4 | 2023 | $10^{12}$（estimated） |
| GPT-5 | 2026 | $10^{12}$（estimated） |

对比人脑的 $10^{15}$ connections：$10^{12}$ 仍比人脑少约 **1000 倍**——但老师说，我们并没有因此比 AI"聪明 1000 倍"（见 §3.4）。

#### 3.3 ⭐ 为什么 2023 年之后参数量不再快速增长

课件给出三条原因（老师课上逐条讲，并据此论证"要学原理"）：

1. **Diminishing returns（收益递减）**：达到 trillion-parameter 规模（如 GPT-4）后，单纯继续加参数带来的性能提升越来越小。老师原话很直白："you add more parameters... they have tried, adding more and more and more, and it's **not that much better**." 2018–2023 那几年的做法是"**very brute force**——he just used money money money money"，规模一年涨 10 倍。
2. **More efficient architectures（更高效的架构）**：如 **Mixture-of-Experts（MoE）**，"activate only part of the model for each token"，能力提升而**激活参数**不增。老师："they got no choice. Probably they got no choice."
3. **Algorithm and data improvements（算法与数据改进）**：进步转而来自**更好的训练数据、alignment methods（对齐方法）、reasoning strategies（推理策略）、更长的 context window**。

> ⭐ 老师的结论直接指向本课程的价值："They go back to the basics... they have to figure out how the neural network works." 只靠堆规模的路子走到头了，"This is why I'm suggesting that it's very important to learn the basic principles. Then you can think of something." 他还鼓励在座学生：年轻、脑子有创造力，"one day you become famous"，而他会说"this guy is my student"。

#### 3.4 人脑仍然占优的地方

老师逐条评估，并**当场划掉已经失守的条目**：

| 任务 | 现状 |
|---|---|
| **Speech production**（生成逼真人声） | **老师划掉**——"now not anymore... AI generates very human speech, very hard to tell." |
| **Speech recognition under certain noisy conditions**（噪声下的语音识别 + contextual understanding） | 人仍占优；安静环境下人甚至可能比 AI 错得多 |
| **Cocktail party effect**（鸡尾酒会效应：嘈杂环境锁定单一说话人） | **人明显占优**——"a very noisy party... I think AI maybe not so good. Human can follow a conversation." |
| **Vision in complex situations**（复杂场景视觉/驾驶） | 人仍占优，但优势在缩小——特斯拉召回、自动驾驶仍受限（"only in the city... he cannot get out of the city and drive in the countryside"，例如泰国的农田路况） |

由此引出课件结论：

- "A **long (long) way to go** before we (if ever) build a computer that truly mimics the human brain"——"very little is known about the human brain"、"the human brain seems to be **too complex to model**"、"even the known processes a single biological neuron requires a **supercomputer** to simulate"。
- 但**是否需要模仿人脑才能达到（超）人类智能？"Probably not."** 老师的类比：飞机不必模仿鸟的扇翅也能飞得更快；汽车跑得比任何动物快。"We don't really need to mimic the human brain to be smarter than the human brain."

### 4. Neural networks 的历史（Historical Sketch）

老师专门讲历史，理由是①有趣，②"you may get some **inspiration** for future development"。

| 时期 | 人物 | 贡献 |
|---|---|---|
| **1940s** | **McCulloch and Pitts** | 第一个 neuron 的**数学模型**，把 neuron 视为 **all-or-none device**（用 step function，而非 sigmoid） |
| **1940s** | **Hebb** | 生物神经元**学习机制**——Hebbian learning rule |
| **1950s** | **Rosenblatt** | **Single-layer perceptron**（单层感知机，见 §6–§7） |
| **1960s** | **Minsky and Papert**（MIT） | 出版专书讨论 single-layer network 的**局限**；书末用**一段话（one-paragraph conjecture）**断言 multi-layer network 有同样局限——**这是错的** |
| **1980s** | **Hopfield** | 关于 **spin-like neural networks** 的论文，把 **solid state physics** 的数学搬进神经网络，引来研究者与经费；获 **2024 Nobel Prize in Physics** |
| **1980s** | **Rumelhart et al.** | **重新发现并普及 backpropagation（BP）**，使 multi-layer perceptron 可训练；其基本思想可追溯到 Bryson and Ho (1969) 的书 *Adaptive Optimal Control* |
| **2000s** | — | **Deep learning**（many layers）："**old science, better engineering**" |

#### 4.1 ⭐ Minsky & Papert 的"一段话"与第一次 AI 寒冬

老师对这段历史讲得最细，因为它是本讲 §8（线性不可分）的伏笔：

- 他们对 **single-layer** 的判断是**正确的**："the limitation of a single layer is real, very limited function."
- 但书末那段 conjecture 的论证是："if one layer cannot do it, what's the use of you putting another layer? One nothing plus another nothing is nothing." → 结论"multi-layer 也一样不行"——**是错的**。
- 后果：连两位 MIT 名教授都想不到多层可行，"worse than that is that **everybody in the world agree with them**... nobody would do anything about network for a long time. Only maybe **less than ten people** still working." 研究经费枯竭、研究暂停，从 1960s 到 1980s **约 20 年**——这就是所谓的**第一次 AI winter**。
- 老师感叹：这个反例其实**极其简单**（见 §9 的多层解法，只需 3 个 neuron 分两层），"It's just a PhD problem"，而全世界等到 20–30 年后才发现。

#### 4.2 Hopfield、Hinton 与 2024 Nobel Prize in Physics

课件写作 **2024 Nobel Prize in Physics**（转写中老师口误说成 "2004"，以 PDF 为准），2024 年由 **John Hopfield** 与 **Geoffrey Hinton** 分享。老师的评述（属个人观点，考试不会考这种评论，但有助于理解本课程关注的"什么才是真正有价值的贡献"）：

- **Hopfield**：贡献在于**建立 solid state physics 与 brain 之间的类比**——solid 中相邻 lattice site 的 magnetic dipole 有 up/down 自旋并相互作用，而 neuron 也是 on/off 两态的 all-or-none 器件，结构相似。于是物理学家手里那一整套数学（量子物理等）突然有了新用武之地，"so a whole patch of physicists dived in. **This is what happened to me**——I was doing physics, and then I became a network researcher." 但老师也直言：Hopfield network **本身"next to useless"**（没人用它做 machine learning / computer vision），而且"the model wasn't even new，it was invented ten years ago, maybe 20 years ago by somebody else"。
- **Hinton**：老师称为 "**godfather of AI**"，因为他做了 CNN，并与学生**第一个把 GPU 用于 deep learning 训练**（见 §5）。至于 Boltzmann machine："again, that thing is useless, because nobody's using Boltzmann machine to do computer vision or speech application"。老师认为 Hinton **deserved a Nobel Prize**，可惜"there was no Nobel Prize in computer science, no Nobel Prize in AI"，所以给了他 physics 奖。

#### 4.3 Rumelhart 与 backpropagation 的"重新发现"

- **Backpropagation（BP）**：训练 neural network（shallow 与 deep 都用）的方法。"If you don't know, it's okay, but we can talk about backprop."
- Rumelhart（Stanford）在 1980s 以为自己发明了 BP，很高兴，因为它终于能训 multi-layer network 做各种事。
- 但很快有人指出：**别人比他早约十年**提出过，而且那人因此成名、还进了 National Science Foundation 掌握科研经费（"he would decide the research money"）。Rumelhart 因此非常抑郁，甚至被指责抄袭（他书里没引用对方）——老师替他辩解：1980s 电脑与网络检索都不普及，"he really doesn't know the other guy's work"。
- 更戏剧的是，若干年后大家又发现：**那个人的工作其实也是 rediscovery**，真正的思想最早出自 **Bryson and Ho (1969)** 的书。老师点评："This kind of thing happens."（这也是为什么课件里 BP 的出处写成 Bryson & Ho。）

#### 4.4 2000s 的 deep learning：old science, better engineering

课件把这轮爆发的三个原因列得极为清楚，并强调"**nothing new scientifically**"：

| 驱动因素 | 内容 | 老师点评 |
|---|---|---|
| **Computers got faster** | **GPU** | GPU 早就存在，只是用来打游戏、做图像渲染，"GPU is not new... I don't think anybody will give a Nobel Prize for GPU"；Hinton 与学生**首个想到用 GPU 做 backpropagation**，"that's really good, they're very smart" |
| **Software environment got better** | **TensorFlow** 等框架、Python 库（老师口语的 "Pyka" 即 PyPI/package index） | "Again, nothing new here. It's just Python." |
| **Data sets got bigger** | **ImageNet**：一位女研究者整理出的约 **1 million images** 数据集 | "Nobody's going to give you a Nobel Prize for 1 million images" |

> ⭐ 老师的结论："These three things **caused the AI revolution**... none of these is worth a Nobel Prize, because there's no new science. It's just engineering. **Better engineering.**"（他计划去问 ChatGPT 这两位 2024 得主是否真的满足 Nobel 的评选条件——"We see what happens."）

#### 4.5 里程碑：AlexNet → AlphaGo → ChatGPT

| 年份 | 事件 | 关键数据 |
|---|---|---|
| **2012** | **AlexNet**（CNN，Hinton 的学生 Alex 提出） | 在 **200 GB 的 ImageNet 数据**上训练；当年 error 仍高于人类 |
| **~2017** | CNN 超越人类 | **human performance = 5.1% error**；CNN 一路降到人类水平以下 → 老师说"这是 AI 真正起飞的地方" |
| **2016** | **DeepMind AlphaGo** 击败前世界围棋冠军 **Lee Sedol** | 用 **deep learning + reinforcement learning**；老师说这位也拿了奖 |
| **2022** | **ChatGPT** | 见下 |

老师强调 2012 年的 CNN 结构"其实只是一堆 neuron"：

> "You can see it's just a bunch of neurons. It's a different layers... you can think of this just a whole bunch of neurons... trained with this stochastic gradient and backpropagation learning rule."

#### 4.6 ChatGPT 的 2022 与"PSLE 难题"

ChatGPT 的传播速度（课件数据）：**5 天 100 万用户**，对比 Netflix 3.5 年、Airbnb / Twitter / Facebook 约 10 个月、Instagram 2.5 个月。

能力清单：写程序代码、写文章与诗、通过 **Michigan Law** 与 **Wharton Business School** 考试（MCQ & essays）、通过美国 **Medical Licensing Exam**。

但反面是——它**过不了新加坡 PSLE（Primary School Leaving Examination，小学离校考试）**：

| 科目 | ChatGPT 得分 |
|---|---|
| Mathematics | **16%** |
| Science | **21%** |

老师当场让 ChatGPT 自陈原因，ChatGPT 的五点解释（课件原文要点）：

1. **Nature of the questions**：law / business / medical 考试测的是 conceptual understanding、reasoning、professional knowledge——"areas where AI trained on vast amount of structured information **excels**"；而 PSLE 的 math 与 English 要求 tricky problem solving、**lateral thinking**、独特的 contextual reasoning。
2. **Logic and abstract thinking**：PSLE 数学有 logic puzzles、heuristics、non-standard problem solving，需要**创造力**而非 pattern recognition；"AI models are trained on **statistical correlation** rather than true conceptual understanding."
3. **Ambiguity and cultural context**：PSLE 语言题要求深度 comprehension 与 inference。
4. **Short and precise answers**：专业考试允许 long-form reasoning，AI 能结构化作答；PSLE 要求 precise 且有时 unconventional 的答案。
5. **Familiarity of exam type in training data**：PSLE 题型多变，"strains the ability to process"。

老师追问要具体例子，ChatGPT 给了一道"realistic example"：

> *"Jen saw a number on the whiteboard. The number was 30–50 [介乎 30 与 50 之间]. It is a multiple of 7. The sum of its digits is ten. What is this number?"*

**ChatGPT 给了几步推理，但怎么都得不到 digit sum = 10**，最后承认"does not seem to have a valid answer"。老师借此说明 **hallucination（幻觉）**：

- 事实上 30–50 之间 7 的倍数只有 35、42、49，digit sum 分别是 8、6、13，**确实无解**——这题本身就是编造的。
- 老师："It has this hallucination... why AI hallucinate and give all these kinds of answers." 并补一句"now it's getting better, of course"，还好奇重考一次能否通过 PSLE。

#### 4.7 产业需求（EVERY INDUSTRY WANTS DEEP LEARNING）

| 行业 | 应用 |
|---|---|
| Cloud Service Provider | Image/Video classification、Speech recognition、Natural language processing |
| Medicine | Cancer cell detection、Diabetic grading、Drug discovery |
| Media & Entertainment | Video captioning、Content based search、Real time translation |
| Security & Defense | Face recognition、Video surveillance、Cyber security |
| Autonomous Machines | Pedestrian detection、Lane tracking、Recognize traffic sign |

### 5. Neural network basics：单个 neuron 的数学

#### 5.1 Bias 作为额外输入

见 §2.2 的公式。要点：**bias $b$ 可以建模为一个恒等于 $+1$ 的输入**，于是

$$
v = \sum_{j=0}^{m} w_j x_j, \qquad x_0 = +1,\ w_0 = b
$$

这使"bias 项"和"权重项"形式统一，便于写成矩阵/向量形式。

#### 5.2 双输入 single-neuron perceptron（二输入单神经元感知机）

取最简单的情形：两个输入 $p_1, p_2$，权重 $w_1, w_2$，bias $b$。神经元做的是

$$
W^{T}p + b = w_1 p_1 + w_2 p_2 + b
$$

然后按符号判类：

| 条件 | 输出 | 类别 |
|---|---|---|
| $W^{T}p + b > 0$ | 1 | **Class 1** |
| $W^{T}p + b \le 0$ | 0 | **Class 2** |

> 课件 Tip："Whether it's $> 0$ or $\ge 0$ doesn't matter **in practice**."（$W^Tp+b=0$ 恰好发生是概率为 0 的事件，不影响结论。）

#### 5.3 Decision boundary（决策边界）的几何

令

$$
W^{T}p + b = 0 \iff W^{T}p = -b
$$

几个必须记住的结论（老师逐条推导的那几页）：

1. **边界上所有点与 $W$ 的内积相同** → 因此它们**在 $W$ 上的投影（projection）相同**。（内积 = $|W|\cdot|p|\cos\theta$，投影 = $|p|\cos\theta$。）
2. 既然投影相同，这些点**必在同一条直线（高维则是 hyperplane）上**，且这条线**正交（orthogonal，即 perpendicular，90°）于 weight vector $W$**。老师反证式解释：若这些点移动时投影保持不变，唯一的可能就是这个方向对 $W$ 的投影不变，即该方向 $\perp W$。
3. **$W$ 决定 decision boundary 的方向（orientation）**——转动 $W$，与之垂直的边界线跟着转。
4. **$W$ 与 $b$ 共同决定边界的精确位置（location）**——同一方向的平行线有好几条，由 $b$ 选定是哪一条。
5. 把 $W$ 与 $b$ **同时乘任意常数**，边界不变（"Any constant factor may be multiplied simultaneously to the weight vector and the bias without changing the boundary location"）——因为方程两边同乘一个数还是同一个方程。这意味着**解不唯一**，只差一个尺度因子（见 §6 的设计过程）。

#### 5.4 Decision region（决策区域）

把边界两边的区域分开看：

- **weight vector 指向（pointed into）的那一侧**：$W^Tp + b > 0$，**正 activation**，输出 $+1$（step function）；
- **weight vector 背离（pointed away）的那一侧**：$W^Tp + b < 0$，**负 activation**，step function 输出 $0$，sigmoid 则输出**约等于 0**。

至此，神经元"做决定"的全部机制就讲完了：**算出 $W^Tp+b$，看符号**。老师用一个生活化的例子收尾：

> "You want the neural network to tell you this is my bottle / this is not a bottle. How does the neural network make a decision? Well, it just does this calculation. You give me this input, I calculate. Is it positive? Yes... I got a negative. Then I say no. **That's all it does.**"

推论（重要）：**单个 neuron 的能力上限 = 用一条直线（hyperplane）把输入空间切成两半** → 只能解决**线性可分（linearly separable）**问题。

### 6. 课堂例题 1：用单个 neuron 实现 OR

**训练数据**（input-output pair）：

| $p_1$ | $p_2$ | Output |
|---|---|---|
| 0 | 0 | **0** |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

（老师顺带复习逻辑：0 = false，1 = true；false OR false = false，其余皆为 true。）

**设计步骤**（课件三步法）：

1. **画一条 decision boundary**（不唯一）——要让 $(0,0)$ 单独在一侧，另三个点在另一侧。例如取过 $(0, 0.5)$ 与 $(0.5, 0)$ 的那条线。
2. **weight vector 与 boundary 正交，并指向 activation 为正（输出 1）的那一侧**（不唯一）——这条线斜率 $-1$，法向为 45°，故

$$
W = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

3. **在 boundary 上取一点求 bias**——取 $(0, 0.5)$：

$$
W^{T}p + b = \begin{bmatrix} 1 & 1 \end{bmatrix}\begin{bmatrix} 0 \\ 0.5 \end{bmatrix} + b = 0.5 + b = 0 \Rightarrow b = -0.5
$$

**答案**：$W = [1, 1]^T,\ b = -0.5$。验证 $(0,1)$：$0+1-0.5 = 0.5 > 0 \to 1$ ✓；$(0,0)$：$-0.5 < 0 \to 0$ ✓。

> ⭐ **关于"解不唯一"与自由度**（老师课上专门讨论）：待定的是 $w_1, w_2, b$ **三个未知数**，而要求边界过 $(0, 0.5)$ 与 $(0.5, 0)$ 只是**两个方程** → 欠定。之所以可解，是因为 $W$ 与 $b$ 同乘常数不改变边界，多出的那个自由度正是**尺度自由度**。所以我们可以任取 $W = [1,1]^T$（也可以用 $[2,2]^T$，对应 $b = -1$，是同一条线）。**这就是"训练"最朴素的形式**：把 weight 和 bias 定下来，"That's all you need. You need the weight and bias."

### 7. 课堂例题 2：用单个 neuron 实现 AND

**训练数据**：

$$
p_1 = \begin{bmatrix}0\\0\end{bmatrix}, t_1 = 0;\quad
p_2 = \begin{bmatrix}0\\1\end{bmatrix}, t_2 = 0;\quad
p_3 = \begin{bmatrix}1\\0\end{bmatrix}, t_3 = 0;\quad
p_4 = \begin{bmatrix}1\\1\end{bmatrix}, t_4 = 1
$$

（true AND true = true，其余皆为 false。）

**设计**：只需把 OR 的那条边界**往右上平移**——方向不变，所以

$$
W = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

取边界上一点 $(0, 1.5)$：

$$
W^{T}p + b = \begin{bmatrix} 1 & 1 \end{bmatrix}\begin{bmatrix} 0 \\ 1.5 \end{bmatrix} + b = 1.5 + b = 0 \Rightarrow b = -1.5
$$

**答案**：$W = [1, 1]^T,\ b = -1.5$。验证 $(1,1)$：$2 - 1.5 = 0.5 > 0 \to 1$ ✓；$(0,1)$：$0 + 1 - 1.5 = -0.5 < 0 \to 0$ ✓。

> ⭐ 课件原文的结论句："**Same decision boundary as in the OR solution, except shifted with a different bias $b$.**" 即：**OR 与 AND 的差别只在 bias（同一条线的平移）**——这就是为什么"bias alone can shift the boundary"，也是 §5.3 第 4 条的具体体现。

### 8. ⭐ Single-layer perceptron 的局限：线性不可分（linearly inseparable）

#### 8.1 结论

Single-layer perceptron 只能给出 **linear decision boundary** $W^Tp + b = 0$，因此**无法处理线性不可分问题**，最著名的反例是 **XOR（Exclusive-OR，异或）**：

| $p_1$ | $p_2$ | XOR Output |
|---|---|---|
| 0 | 0 | **0** |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **0** |

课件点题："But **multi-layer perceptrons can handle linearly inseparable problems!**"

#### 8.2 几何论证：为什么一条线永远不行

把四个点画在 $(p_1, p_2)$ 平面上：输出 1 的是 $(0,1)$ 与 $(1,0)$，输出 0 的是 $(0,0)$ 与 $(1,1)$——两组点落在**两条对角线上**，互相"穿插"。

老师课上把四种可能的放线位置逐一试过：

| 线的位置 | 结果 |
|---|---|
| 把 $(0,0)$ 单独划出 | 另一侧混着 0 与 1 → 失败 |
| 把 $(1,1)$ 单独划出 | 另一侧混着 0 与 1 → 失败 |
| 把 $(0,0)$ 与 $(1,1)$ 划在一起 | 同上，另一侧仍是混合 → 失败 |
| 把 $(0,1)$ 与 $(1,0)$ 划在一起 | 同上 → 失败 |

> "It doesn't matter where you put the line. **You cannot separate them.**" 数学上可严格证明：单条直线无法分开这两个集合。

#### 8.3 ⭐ 为什么"同一层多放几个 neuron"也救不了

学生的自然疑问是：一个 neuron 不行，那一层放很多 neuron 呢？老师课上手写了这个论证（他说"虽然我忘记做这一页幻灯片"）：

- 第 $i$ 个 neuron 给出自己的线性式：$W_i^Tp + b_i$；
- 同一层里所有 neuron **共享同一个输入 $p$**，各自只是不同的 $(W_i, b_i)$；
- 若把这一层的输出**线性组合**起来（例如作为下一层的一个 neuron 的输入），得到的是

$$
\sum_i \alpha_i\bigl(W_i^Tp + b_i\bigr) = \Bigl(\sum_i \alpha_i W_i\Bigr)^{T} p + \sum_i \alpha_i b_i = \tilde{W}^{T}p + \tilde{b}
$$

——**仍然是一个线性式**。

> ⭐ 老师的原话："**Linear plus linear plus linear is still linear.**" 所以"同一层里无论放多少 neuron、多少个 $W$ 和 $b$，decision boundary 仍是一条直线（hyperplane）"，XOR 依然解不了。**这正是 Minsky & Papert 那本书里说的、也确实是正确的部分**："no matter how many neurons you have in a layer, you cannot solve this simple XOR problem."

#### 8.4 翻转：Minsky & Papert 错在哪

- 他们**对**的地方："one layer cannot do it."
- 他们**错**的地方：由此推出"两层不行、三层不行、四层也不行"——**"which is not true"**。
- 老师课上明确说："**Can you do with two layers? You can do it. You can do it with multi-layer perceptron.**" 并感叹这题其实不难："It's just a PhD problem... Until 20, 30 years later, they find out: Oh, I can do it like this."

**关键区别**：单层的失败是因为"**输出仍是输入的线性函数**"。一旦在两层之间插入**非线性 activation**，线性就"断"了，表达力随层数指数级增长——见 §9 与 §10。

### 9. Multi-layer 解法：XOR 与一般线性不可分区域

#### 9.1 XOR 的 3-neuron 两层解（课件 Example 2）

结构：**2 个 hidden neuron + 1 个 output neuron**，共 3 个 neuron、两层（老师课上说"One layer with two neurons, one layer with one neuron. Three neurons. You can do it."）。

**两个 hidden neuron 的决策边界**：

$$
\underbrace{\begin{bmatrix}1\\1\end{bmatrix}^{T} p - 0.5 = 0}_{\text{hidden neuron \#1}: \ p_1 + p_2 = 0.5}
\qquad
\underbrace{\begin{bmatrix}-1\\-1\end{bmatrix}^{T} p + 1.5 = 0}_{\text{hidden neuron \#2}: \ p_1 + p_2 = 1.5}
$$

- neuron #1 触发（输出 1）当 $p_1 + p_2 \ge 0.5$ → 它负责**排除 $(0,0)$**；
- neuron #2 触发当 $p_1 + p_2 \le 1.5$ → 它负责**排除 $(1,1)$**。

**Output neuron 做 AND**：

$$
\text{AND operation: weights } 1, 1; \text{ bias } -1.5
\quad\Longrightarrow\quad
y = \sigma(h_1 + h_2 - 1.5)
$$

**逐点验证**（$\sigma$ 为 step function，$\ge 0$ 输出 1）：

| $p$ | $h_1 = [1,1]^Tp - 0.5$ | $h_2 = [-1,-1]^Tp + 1.5$ | $h_1 + h_2 - 1.5$ | $\hat{y}$ | 期望 |
|---|---|---|---|---|---|
| $(0,0)$ | $-0.5 \to 0$ | $1.5 \to 1$ | $-0.5 \to 0$ | **0** | 0 ✓ |
| $(0,1)$ | $0.5 \to 1$ | $0.5 \to 1$ | $0.5 \to 1$ | **1** | 1 ✓ |
| $(1,0)$ | $0.5 \to 1$ | $0.5 \to 1$ | $0.5 \to 1$ | **1** | 1 ✓ |
| $(1,1)$ | $1.5 \to 1$ | $-0.5 \to 0$ | $-0.5 \to 0$ | **0** | 0 ✓ |

> ⭐ **逻辑读法**：hidden #1 实现的是 NOT$(0,0)$，hidden #2 实现的是 NOT$(1,1)$，输出层把两者 **AND** 起来 → NOT$(0,0)$ AND NOT$(1,1)$ = XOR。**这就是"hidden layer 先把输入空间切成几块，再在输出层做逻辑组合"的雏形。**

#### 9.2 更一般的设计模式：AND-of-ANDs, OR-of-ANDs（课件 Example 1）

课件给了一个更一般的线性不可分问题（点集分布在**两个互相分离的矩形区域**），其解需要 **3 层、共 7 个 neuron**（4 + 2 + 1）。注意：老师课上展示了这个解与"结果"，但明说 **"I don't have time to show you how you get it, but we can show you next time"**——以下按课件补全。

**第 1 个 hidden layer：4 个 neuron，每 2 个构成一个 AND（切出一个矩形区域）**

| neuron | $W_i^T$ | 边界上的点 | 边界方程 | 解得 bias | 含义 |
|---|---|---|---|---|---|
| #1 | $[-1,\ 0]$ | $(0.5,\ 0)$ | $-p_1 + 0.5 = 0$ | $b = 0.5$ | $p_1 \le 0.5$ |
| #2 | $[0,\ -1]$ | $(0,\ 0.75)$ | $-p_2 + 0.75 = 0$ | $b = 0.75$ | $p_2 \le 0.75$ |
| #3 | $[1,\ 0]$ | $(1.5,\ 0)$ | $p_1 - 1.5 = 0$ | $b = -1.5$ | $p_1 \ge 1.5$ |
| #4 | $[0,\ 1]$ | $(0,\ 0.25)$ | $p_2 - 0.25 = 0$ | $b = -0.25$ | $p_2 \ge 0.25$ |

于是：

- **#5 = AND(#1, #2)** → 左下矩形 $\{p_1 \le 0.5,\ p_2 \le 0.75\}$；
- **#6 = AND(#3, #4)** → 右上矩形 $\{p_1 \ge 1.5,\ p_2 \ge 0.25\}$。

**第 3 层：1 个 neuron 做 OR**

- **#7 = OR(#5, #6)** → 两个矩形的**并集**，即 class 1 的完整区域。

**矩阵形式（课件原文）**：

$$
W_1^{T} = \begin{bmatrix}-1 & 0\\ 0 & -1\\ 1 & 0\\ 0 & 1\end{bmatrix},\quad
b_1 = \begin{bmatrix}0.5\\ 0.75\\ -1.5\\ -0.25\end{bmatrix};\qquad
W_2^{T} = \begin{bmatrix}1 & 1 & 0 & 0\\ 0 & 0 & 1 & 1\end{bmatrix},\quad
b_2 = \begin{bmatrix}-1.5\\ -1.5\end{bmatrix};\qquad
W_3^{T} = \begin{bmatrix}1 & 1\end{bmatrix},\quad b_3 = \begin{bmatrix}-0.5\end{bmatrix}
$$

**前向传播（forward propagation）三步**：

$$
h_1 = \sigma\bigl(W_1 p + b_1\bigr) \in \mathbb{R}^{4},\qquad
h_2 = \sigma\bigl(W_2 h_1 + b_2\bigr) \in \mathbb{R}^{2},\qquad
\hat{y} = \sigma\bigl(W_3 h_2 + b_3\bigr) \in \mathbb{R}^{1}
$$

> 课件 Tip：$\boldsymbol{x} \in \mathbb{R}^{n}$ 表示 $x$ **有 $n$ 行**（即 $n$ 维列向量）。

**课件给的算例**，取 $p = \begin{bmatrix}0 & 1\end{bmatrix}^{T}$：

$$
h_1 = \sigma\bigl([0.5,\ -0.25,\ -1.5,\ 0.75]^{T}\bigr) = [1,\ 0,\ 0,\ 1]^{T}
$$
$$
h_2 = \sigma\bigl([-0.5,\ -0.5]^{T}\bigr) = [0,\ 0]^{T}
$$
$$
\hat{y} = \sigma(-0.5) = 0
$$

（逐步核对：$W_1p = [0,-1,0,1]^T$，$+b_1 = [0.5,-0.25,-1.5,0.75]^T$，过 step 得 $[1,0,0,1]^T$；$W_2h_1 = [1,1]^T$，$+b_2 = [-0.5,-0.5]^T$，得 $[0,0]^T$；$W_3h_2 = 0$，$+b_3 = -0.5 < 0 \to 0$。即 $p=(0,1)$ 不在两个矩形内，与几何判断一致。）

> ⭐ 课件特意指出 **$W_2$ 里的那些 0**："#5 still does an AND for #1 and #2: **the extra 0 weights effectively ignore #3 and #4**. Similarly for #6." 也就是说，每一层的 neuron 只"看"自己需要的那些输入——这正是后面做 CNN 局部连接、稀疏权重时的思想起点。

**对应的 Python 实现（课件给出，NumPy；不考编程但看逻辑）**：

```python
import numpy as np
w1 = np.array([[-1, 0], [0, -1], [1, 0], [0, 1]])   # 4x2
w2 = np.array([[1, 1, 0, 0], [0, 0, 1, 1]])         # 2x4
w3 = np.array([[1, 1]])                             # 1x2
b1 = np.array([0.5, 0.75, -1.5, -0.25])
b2 = np.array([-1.5, -1.5])
b3 = np.array([-0.5])

p  = np.array([0, 1]).T
h1 = (w1 @ p + b1) >= 0     # step function
h2 = (w2 @ h1 + b2) >= 0
y  = (w3 @ h2 + b3) >= 0
```

> 课件 Tip：`@` 是 NumPy 数组 dot product 的简写。

> ⭐ **解的自由度**（呼应 §6）：这套 $W, b$ 显然不是唯一解——每个 neuron 的 $W_i$ 与 $b_i$ 可以整体同乘正常数；而且每条边界线的位置在不改变分类的前提下也能在小范围内挪动。课件自己在 OR/AND/XOR 三处都写了"not unique"。

### 10. ⭐ Universal approximation（万能逼近）

课件用三页把"层数与能表达的决策区域"逐级放大，这是本讲最重要的理论结论。

#### 10.1 层数与决策区域的关系

| 网络 | 能表达的 decision region | 直观 |
|---|---|---|
| **1-layer**（只有输入层 + 输出层，无 hidden layer） | 单个 **half-plane**（半平面） | 一条直线切一刀 |
| **2-layer**（1 个 hidden layer + 输出） | **单个 convex decision region**（凸区域） | 多条直线**取交（AND）**得到的凸多边形 |
| **3-layer**（2 个 hidden layer + 输出） | **任意（arbitrary）decision region**，包括不连通、非凸 | 先切出多个凸区域，再**取并（OR）** |

> 课件原文："Note that a 2-layer network can generate only a **single convex decision region**."——这也解释了 §9.2 的例子为什么**必须**用 3 层：class 1 是两个分离的矩形，既非凸也非连通。

#### 10.2 3-layer MLP 如何逼近任意决策区域

课件的构造逻辑（从下往上看）：

| 层 | 作用 |
|---|---|
| **第 1 个 hidden layer** | 有 $N$ 组、**每组 $2^d$** 个 neuron（用于 class $C_1$ 的 $N$ 个数据点附近，$d$ 为维度）——每组用若干超平面切出一个**凸区域**（在 $d$ 维需 $2^d$ 个半空间，2D 即 4 条边围成一个矩形，正是 §9.2 的 #1–#4） |
| **第 2 个 hidden layer** | 每个 neuron 做一个 **AND**——把第 1 层的一组 neuron 合成为一个凸区域 |
| **Output layer** | 做一次 **OR**——把所有凸区域并起来 |

> 课件结论："**Universal Approximation: the accuracy of an MLP can be arbitrarily high, if there are enough hidden neurons.**"（只要 hidden neuron 足够多，MLP 的精度可以任意高。）

#### 10.3 2-layer MLP 逼近任意连续函数

课件把上面的"区域逼近"升级成"函数逼近"：

> "A hidden layer of **nonconstant, bounded, and continuous neurons** (with weights and biases), plus a **linear output neuron** (with weights but **without bias**) can approximate **any continuous function** to any arbitrary accuracy if there are enough hidden neurons."

**Intuitive proof（直觉证明）的思路**——用"阶梯"拼出函数：

1. 权重取得足够大时，sigmoid 型 activation 逼近 **step function**，于是每个 hidden neuron 近似给出一个"从 0 跳到 1 的台阶"；
2. 取**一对** hidden neuron，权重分别为 $+1$ 与 $-1$，位置稍有错开，两者相减就得到一个**矩形脉冲 / bump**（在某个小区间内为常数，其余为 0）；
3. 把**许多个**这样的 bump（各自调到需要的高度、放在需要的位置）**加权求和**，就能逼近任意连续曲线——分段常数逼近，段数越多越精确；
4. "段数足够多"等价于"hidden neuron 足够多"。

> ⭐ 这一页解释了神经网络"为什么什么都能做"（§1 老师说的"why you can do so many things"），也解释了 §8.4 的关键：**是 activation function 的非线性使这一切成为可能**——如果 activation 是线性的，多层叠起来仍是线性，就永远只能画一条直线。

### 11. Notebook：MLP on (Fashion) MNIST with TensorFlow 2

配套文件：`week8/mlp_mnist_tf.ipynb`（来自 **pyprobml**，即 Kevin Murphy《Probabilistic Machine Learning》的配套代码；用 **TensorFlow 2 / Keras**）。它把 §2、§9、§10 的"neuron 堆叠"落到一个真实任务上。

#### 11.1 数据

```python
train_images, train_labels, test_images, test_labels, class_names = get_dataset(FASHION=False)
print(train_images.shape)   # (60000, 28, 28)
```

- 使用原始 **MNIST**（`FASHION=False`，所以是手写数字 0–9 而非 Fashion-MNIST）；
- 训练集 **60,000** 张 $28\times28$ 灰度图，另有 10,000 张测试图；
- `plot_dataset` 画出前 25 张并标出 `class_names`。

#### 11.2 模型结构（三层 MLP）

```python
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10,  activation=tf.nn.softmax),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
```

对应 §2.2 的语言：

| Keras 层 | 数学含义 |
|---|---|
| `Flatten(28,28)` | 把图像拉平成 $p \in \mathbb{R}^{784}$，即 §5 的 input $p$ |
| `Dense(128, relu)` | 128 个 hidden neuron，每个算 $W_i^{T}p + b_i$ 再过 **ReLU** |
| `Dense(128, relu)` | 第 2 个 hidden layer（对应 §10.1 的"3-layer network"） |
| `Dense(10, softmax)` | 10 个输出 neuron（10 类），softmax 给出类别概率 |

`model.summary()` 的参数量（= §3.2 里说的 "parameters"）：

| Layer (type) | Output Shape | Param # |
|---|---|---|
| flatten (Flatten) | (None, 784) | 0 |
| dense (Dense) | (None, 128) | **100,480** |
| dense_1 (Dense) | (None, 128) | **16,512** |
| dense_2 (Dense) | (None, 10) | **1,290** |
| **Total params** | | **118,282** |

> ⭐ 手算核对（就是 §2.2 的 $w_j x_j$ 堆起来）：$784\times128 + 128 = 100{,}480$；$128\times128 + 128 = 16{,}512$；$128\times10 + 10 = 1{,}290$。**每个 "+" 后面的常数就是 bias $b$**——与 §2.2 把 bias 写成 $x_0=+1$ 的输入完全一致。

#### 11.3 训练与结果

notebook 注释说明为何只训 1 个 epoch："(1) it is faster, and (2) it produces **more errors, which makes for a more interesting plot** :)"。

| 阶段 | loss | accuracy |
|---|---|---|
| 第 1 epoch 训练中（1875 步） | 0.2288 | 0.9319 |
| **Train（1 epoch 后）** | 0.1004 | **0.9700** |
| **Test（1 epoch 后）** | 0.1162 | **0.9646** |
| 第 2 epoch 训练中 | 0.0948 | 0.9711 |
| **Train（2 epochs 后）** | 0.0622 | **0.9810** |
| **Test（2 epochs 后）** | 0.0896 | **0.9732** |

（1 个 epoch 在 CPU 上约 **2.2 秒**——notebook 同时打印了 "No GPU was detected. DNNs can be very slow without a GPU."，正好呼应 §4.4 里 **GPU 是深度学习爆发的三大驱动之一**。）

#### 11.4 预测与"有意思"的错误样本

```python
# 单张图：需要 reshape 成 (N,D,D)，N=1
img = np.expand_dims(test_images[0], 0)   # (28,28) -> (1,28,28)
predictions_single = model.predict(img)   # (1,10) 类别概率

# 全测试集
predictions = model.predict(test_images)  # (10000, 10)
ndx = find_interesting_test_images(predictions, test_labels)
plot_interesting_test_results(test_images, test_labels, predictions, class_names, ndx)
```

`find_interesting_test_images` 挑出**预测得最"有意思"的测试样本**（错得离谱或置信度很低的），`plot_interesting_test_results` 把它们画出来（返回 354 个这样的样本）。

#### 11.5 这个 notebook 想说明什么

1. **本讲的概念是真的能跑起来的**：§2 的"linear combination + activation"、§9 的 hidden layer 堆叠，落到代码里就是 4 行 `keras.layers`，参数总量 118,282——比 §3.2 的 GPT-1（$10^8$）还小好几个数量级，却已能识别手写数字。
2. **universal approximation 的实践意义**（§10）：仅仅是"足够多的 hidden neuron"，1 个 epoch 就达到 **96.46% test accuracy**，2 个 epoch 升到 **97.32%**。
3. **但离"完美"还差得远**：仍有约 3% 的错误，而且错得很"人类"（`plot_interesting_test_results` 里能看到连人都难以辨认的样本）。**这说明通用的 MLP 不是终点**——对图像这类具有空间结构的数据，需要利用局部性/平移不变性的专门结构，也就是后面的 **CNN**。
4. 提升方向：训练轮数、网络宽度/深度、optimizer、loss 的选择——正是第二块"训练（training）"要讲的内容（forward propagation 已在本讲出现，backpropagation 与 SGD 在后续讲）。

### 12. 课堂插曲：学生项目答疑（deepfake detection）

课间休息时一位学生（转写作 "Paki"）找老师讨论自己的 project（deepfake/anti-spoofing 方向），要点如下，可作为一个"课堂上讲的东西怎么落地"的例子：

| 项目要点 | 内容（转写） |
|---|---|
| 任务 | Deepfake / spoof 检测（"Deepfake detection and spoof"，用于防护目的） |
| 模型 | 选了 "**ASIS**" 模型（转写拼写不确定，属 anti-spoofing 一类模型），学生自报为 "N Lead Learning"，已训练约 3 个模型 |
| 硬件 | 尝试部署到 **Raspberry Pi 4**——算力有限，"I can't handle that much compute"，因此只能用较小版本模型 |
| 训练资源 | 申请到 **MLDA cluster**（NTU 的机器学习/深度学习集群）的使用权限，在集群上训练后与 Raspberry Pi 集成 |
| 指标 | **EER（equal error rate）= 1.8%** |

老师反馈是正面的（"All right. All right. That's good."），并约了后续讨论 loss 与 metric 的时间。

### 13. 本周要点小结

- **换老师与课程结构**：Week 8–13 由 **Wang Lipo** 讲，分三块——**NN/DL 导论 → 训练（shallow + deep）→ CNN**；其他网络结构（RNN/LSTM 等）放 **supplementary folder** 选读。**Python 编程不考**（"not even in the quiz"），但 homework 含编程；用 AI 写程序不禁止。
- **人工神经元 = 线性组合 + 非线性**：$v = \sum_{j=0}^{m} w_j x_j$（$x_0=+1$ 吸收 bias），$y = f(v)$；常见 $f$ 有 step、sigmoid $\sigma(x)=1/(1+e^{-x})$（$\sigma' = \sigma(1-\sigma)$）、tanh、ReLU。
- **decision boundary 的几何**：$W^{T}p + b = 0$ 是一条（高维为 hyperplane）**与 $W$ 正交**的线；$W$ 定**方向**、$W$ 与 $b$ 共同定**位置**；$W,b$ 同乘常数边界不变；$W$ 指向的一侧 activation 为正（输出 1），背离的一侧为负（输出 0）。
- **单 neuron 只能做线性分类**：OR（$W=[1,1]^T, b=-0.5$）与 AND（同 $W$、$b=-1.5$）都靠"画一条线 + 取线上一点解 bias"完成，二者只差 **bias（平移）**。
- **⭐ XOR 是分水岭**：**linear separability** 之外的都做不到，而且 **"linear + linear + linear is still linear"**——**同一层里加多少 neuron 都没用**。Minsky & Papert 对单层的判断正确，由此推出的多层也不行**是错的**，却导致了约 20 年的第一次 AI winter。
- **多层解法**：XOR 只需 **3 个 neuron 分两层**（2 hidden 做 NOT$(0,0)$ 与 NOT$(1,1)$，输出层做 AND）；一般线性不可分区域用 **3 层 7 neuron**（1st hidden 切凸区域 → 2nd hidden 做 AND → output 做 OR）。
- **⭐ Universal approximation**：1-layer 只能给 half-plane；**2-layer 只能给单个 convex region**；**3-layer 可逼近任意 decision region**；2-layer MLP（非线性 hidden layer + 线性输出 neuron）可**任意精度逼近任意连续函数**。前提都是"**hidden neuron 足够多**"。
- **历史与现状**：1940s McCulloch-Pitts / Hebb → 1950s Rosenblatt（single-layer perceptron）→ 1960s Minsky-Papert（AI winter）→ 1980s Hopfield（2024 Nobel Prize in Physics）与 Rumelhart（backpropagation，思想可溯至 Bryson & Ho 1969）→ 2000s deep learning = **old science + better engineering**（GPU / TensorFlow / ImageNet）→ 2012 AlexNet → 2016 AlphaGo → 2022 ChatGPT。GPT 参数量 2023 年后基本停在 $10^{12}$：**diminishing returns + MoE 等高效架构 + 算法与数据改进**。
- **Notebook 实证**：3 层 MLP（Flatten → Dense128 ReLU → Dense128 ReLU → Dense10 softmax，共 118,282 参数）在 MNIST 上 **1 epoch 得 test accuracy 96.46%，2 epochs 得 97.32%**——印证 universal approximation 的实践威力，也说明通用 MLP 之后还需要 CNN。

---

### 下一周预告

**Week 9 继续 Part 2（Neural Network 的 training）**。课件本讲末尾留下两条明说的线索：① 老师课堂上说 §9.2 那套 **3 层 = 4 + 2 + 1 的设计"how to get it"会下次讲**（即"如何系统地设计多个 hidden neuron 的边界"）；② 讲完 §10 的 **universal approximation**（2-layer MLP 逼近任意连续函数）后，自然进入"**这些 weight 和 bias 到底怎么求出来**"——也就是 **forward propagation（本周已出现）+ backpropagation + SGD** 的训练部分。本周只做了"人手工设计权重"（OR/AND/XOR 都是手算出来的），老师已明确预告"in general, we don't train network this way"，训练方法将是后续重点。此外请注意 **Quiz 2 范围是 Week 8–11**，本周内容（neuron 模型、linear separability、XOR 需多层、universal approximation）属于必考基础。

---

## Week 9 — Part 2.1（续）：多层网络设计、Forward Propagation 与 Universal Approximation

本周继续 Wang Lipo 的 **Part 2.1: Introduction to Neural Networks and Deep Learning**。Week 8 停在 universal approximation 的结论页，并预告"§9.2 的 3 层 4+2+1 设计 how to get it 下次讲"；本周先把这笔账还上：完整推导 **4+2+1 三层网络**每个 neuron 的 weight 与 bias，再讲 **training 的定义**、**forward propagation（前向传播）** 的逐层计算与矩阵形式，最后用"矩形脉冲"给出 **universal approximation** 的直观证明。

> ⚠️ **进度说明（很重要）**：本周转写 `week8-9/week9.txt` 在 forward propagation 之后结束，老师原话是 **"we can continue the next episode. We continue next time."**——**backpropagation 本周只做了预告，正式推导在 Week 10**。因此本笔记 §9 的 backpropagation / gradient descent / SGD 完整推导，是**为 Week 10 "Training Deep Networks" 和 Quiz 2 预先整理的数学准备**，已明确标注，不是本周课堂内容。Week 1 进度表把 Week 9 写成 "Deep Learning (CNN)"，实际进度比表慢：本周仍在 Part 2.1，CNN 与 training 顺延到后面。

> **权威来源说明**：本节由 `week8-9/week9.txt` 录播转写整理，并以 `week8-9/Part 2.1_Intro_NN_DL(1).pdf`（Wang Lipo，50 页）核对。注意：**该 PDF 只包含 Week 8 的 50 页**，到 universal approximation 为止，没有 training/backprop 的幻灯片；因此本周的 4+2+1 设计细节、forward propagation 数值例、training/inference 讨论主要来自转写，公式与网络结构仍以 PDF 第 40–50 页为准，notebook `mlp_mnist_tf.ipynb` 仅作辅助。转写是 ASR 输出，术语错拼极多，下表是本周典型对照。

**本周 ASR 错拼对照表**

| 转写 | 正确 | 说明 |
|---|---|---|
| new network / near network / neo network / newer / ne never / near newer | **neural network** | 本周最高频错拼 |
| neuron 的各种变体：neon / uro / nero / ero / mon / murals / near newer | **neuron(s)** | 单复数都有 |
| lat | **one / slide**（指代） | "very important lat" 指 XOR 那张图，不是术语 |
| Minsky and Pepper | **Minsky and Papert** | 与 Week 8 一致 |
| Perception / precept | **perceptron** | single-layer perceptron |
| x problem / X all problem / X war / x or | **XOR problem** | Exclusive-OR |
| end / n / and（动词用法） | **AND** | 如 "do a end" = "do an AND" |
| war / or（动词用法） | **OR** | 如 "do a war" = "do an OR" |
| swash / streure / stretchhl | **threshold** | bias / threshold 同义 |
| weight actor / void vector / wait invector | **weight vector** | $W$ |
| hyperpne | **hyperplane** | 高维决策边界 |
| se neurons | **three neurons** | XOR 最小解 |
| Sigma / C moi / sim / Sigmoi / sikmoi | **sigmoid** | $\sigma(x)=1/(1+e^{-x})$ |
| heat layer / heated layer / hen layer / hey | **hidden layer** | 输入与输出之间 |
| Romaart / David Romard | **Rumelhart（David Rumelhart）** | backpropagation 的普及者 |
| Back publication | **backpropagation** | BP |
| Paul verbals | **Paul Werbos** | 老师提到的更早提出者 |
| Yan Lacoon / Yan Lac | **Yann LeCun** | 手写数字识别 / 早期 CNN |
| met lab / metab / meta / Mt lab | **MATLAB** | MAT = matrix |
| EI | **AI** | artificial intelligence |
| Chch BD / gibty | **ChatGPT / GPT** | 老师举例 |
| School of trip | **School of EEE** | 与 Week 8 一致 |
| Millennian price problem | **Millennium Prize Problem** | 千禧年大奖难题 |
| the u, R / Room / Brandon | **ReLU** | rectified linear unit |
| sock market | **stock market** | 股价预测 |
| inco | **input** | 如 "this input is [1, -1]" |
| 62a0 82 | **[0.982, 0.12]** | 玩具网络的输出 |
| break out（疑） | **black box** | 口语"神经网络像黑箱" |

> **术语提醒**：老师课上把 weight 和 bias 口语称为 **"hyperparameters of neural network"**。严格按机器学习术语，**weight 和 bias 是 parameters（参数）**，由训练数据学习得到；**hyperparameters（超参数）** 是训练前人为设定的量（层数、每层 neuron 数、learning rate、batch size、epoch 数、activation 选择、optimizer 等）。考试按标准术语作答，见 §4.2。

### 0. 本周定位与行政信息

| 项目 | 内容 |
|---|---|
| 本周实际内容 | ① 回顾 linear separability / XOR / Minsky-Papert；② **4+2+1 三层网络完整设计**（Week 8 承诺的 "how to get it"）；③ **training 的定义**：找 weights + biases；④ **forward propagation** 逐层计算与矩阵形式；⑤ **universal approximation** 的直观证明；⑥ deep network 的含义 |
| 未讲内容 | **backpropagation、gradient descent、SGD** 本周只预告，下周正式讲（见 §9 的预习） |
| Wooclap | 本周老师终于开了 Wooclap：**答对答错都算 attendance**——"If you get it right, you get the attendance. But if you get it wrong, you also get attendance. Because I'm just going to recall the participation, not the score." 题目内容转写未记录 |
| 考试计算 | 老师明确说考试可能要求**用笔和计算器手算 forward pass**："in the exam, you may have to do this kind of stuff... you just use your pen... maybe a calculator." **Python 编程不考**（与 Week 8 一致），但 forward propagation 的数值计算要会 |
| MATLAB 插曲 | 老师感叹早年 MATLAB  licence 贵、要排队；Python 免费后 everyone can do neural network。MATLAB 的 "MAT" 就是 matrix——矩阵运算才是重点（§5.6） |
| PG survey paper | 老师建议 PG 学生可把 **universal approximation for ReLU** 作为 survey paper 题目：经典定理要求 bounded & continuous，而 ReLU 无界；"如果有人证出来，你可以写篇论文" |

### 1. 回顾：linear separability、XOR 与 Minsky-Papert

Week 8 已详细讲过，这里只保留本周老师 recap 的逻辑链，作为 §2 的铺垫。

#### 1.1 单层为什么不行

单个 neuron 的决策边界是

$$
W^{T}p + b = 0,
$$

一条直线（高维为 hyperplane）。**同一层里放多个 neuron 也没用**：设第 $i$ 个 neuron 输出 $W_i^{T}p+b_i$，把它们线性组合给下一层，得到

$$
\sum_i \alpha_i\bigl(W_i^{T}p+b_i\bigr)
= \Bigl(\sum_i \alpha_i W_i\Bigr)^{T}p+\sum_i \alpha_i b_i
= \tilde{W}^{T}p+\tilde{b},
$$

仍然是线性式。老师原话："**Linear plus linear plus linear is still linear.**" 所以单层（无论多少 neuron）只能解决 **linearly separable** 问题。

#### 1.2 XOR：最著名的反例

| $p_1$ | $p_2$ | XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

四个点落在两条对角线上，任何一条直线都无法把 $\{0,1\}$ 与 $\{1,0\}$ 和 $\{0,0\}$ 与 $\{1,1\}$ 完全分开。

#### 1.3 Minsky & Papert 的对与错

- **对的**：single-layer perceptron 不能解决 XOR；同一层加多少 neuron 都不行。
- **错的**：他们书末用一段 conjecture 断言"多层也一样不行"——论证是"one nothing plus another nothing is nothing"。
- **后果**：全世界信了约 20 年，神经网络研究进入 **第一次 AI winter**。
- **本周要展示的**：多层不仅能做，而且**非常简单**——XOR 只需 **3 个 neuron、2 层**；一般的线性不可分区域用 **3 层 4+2+1** 就能解决。

> ⭐ 老师反复强调的方法论："You should not believe people telling you things no matter how famous they are... you don't believe until you see a proof." 这也是他讲这段历史的用意。

### 2. ⭐ 3 层 4+2+1 网络：Week 8 承诺的 "how to get it"

Week 8 的 Example 1 是一个**线性不可分**问题：class 1 的点落在两个互相分离的矩形区域里，class 0 在其余地方。课件直接给出了 3 层、7 个 neuron 的解（4 + 2 + 1），但老师说 **"I don't have time to show you how you get it, but we can show you next time."** 本周兑现。

#### 2.1 问题与设计思路

设输入 $p=\begin{bmatrix}p_1\\p_2\end{bmatrix}$，两个 class 1 区域是：

- **左下矩形**：$p_1\le 0.5,\ p_2\le 0.75$；
- **右上矩形**：$p_1\ge 1.5,\ p_2\ge 0.25$。

设计思路与 Week 8 §10.2 的 universal approximation 构造完全一致：

| 层 | neuron 数 | 作用 | 逻辑 |
|---|---|---|---|
| 第 1 个 hidden layer | 4 | 每个矩形用 2 条边切出来 | 半平面（half-plane） |
| 第 2 个 hidden layer | 2 | 每个矩形把 2 条边合起来 | **AND** |
| Output layer | 1 | 两个矩形合起来 | **OR** |

即：**先用半平面切出凸区域，再用 AND 合成凸区域，最后用 OR 合并多个凸区域**。这正是"1-layer = half-plane；2-layer = 单个 convex region；3-layer = arbitrary region"的具体实现。

#### 2.2 第一层：4 个 neuron 切出两个矩形

每个 neuron 仍由 **weight vector $W_i$ + bias $b_i$** 完全描述。规则：

1. 决策边界与 $W_i$ **正交**；
2. $W_i$ **指向正激活（输出 1）的一侧**；
3. 边界过某已知点 $p_0$ 时，用 $W_i^{T}p_0+b_i=0$ 解出 $b_i$。

| neuron | $W_i$ | 边界过点 | 边界方程 | 解得 $b_i$ | 正激活区域 |
|---|---|---|---|---|---|
| #1 | $\begin{bmatrix}-1\\0\end{bmatrix}$ | $(0.5,\ 0)$ | $-p_1+b_1=0$ | $b_1=0.5$ | $p_1\le 0.5$ |
| #2 | $\begin{bmatrix}0\\-1\end{bmatrix}$ | $(0,\ 0.75)$ | $-p_2+b_2=0$ | $b_2=0.75$ | $p_2\le 0.75$ |
| #3 | $\begin{bmatrix}1\\0\end{bmatrix}$ | $(1.5,\ 0)$ | $p_1+b_3=0$ | $b_3=-1.5$ | $p_1\ge 1.5$ |
| #4 | $\begin{bmatrix}0\\1\end{bmatrix}$ | $(0,\ 0.25)$ | $p_2+b_4=0$ | $b_4=-0.25$ | $p_2\ge 0.25$ |

**逐条推导**（以 #1、#3 为例，其余同理）：

- #1：边界是竖线 $p_1=0.5$，$W_1$ 必须水平；要让它指向 $p_1<0.5$ 的一侧（正激活），取 $W_1=[-1,0]^T$。代入边界点 $(0.5,0)$：

$$
W_1^{T}p_0+b_1=[-1,\ 0]\begin{bmatrix}0.5\\0\end{bmatrix}+b_1=-0.5+b_1=0
\Rightarrow b_1=0.5.
$$

- #3：边界是竖线 $p_1=1.5$，正激活在 $p_1>1.5$ 一侧，取 $W_3=[1,0]^T$。代入 $(1.5,0)$：

$$
W_3^{T}p_0+b_3=[1,\ 0]\begin{bmatrix}1.5\\0\end{bmatrix}+b_3=1.5+b_3=0
\Rightarrow b_3=-1.5.
$$

> ⭐ **为什么 $W$ 可以取 $\pm1$ 这种"随便"的值？** 因为 $W$ 与 $b$ 同乘一个正常数，决策边界不变（Week 8 §5.3 第 5 条）。例如 #1 取 $W=[-2,0]$，则 $b=1$，仍是同一条线。所以真正重要的只有**方向**和**边界位置**。

#### 2.3 第二层：2 个 AND neuron

第一层输出 $h_1,\dots,h_4\in\{0,1\}$。第二层要做 **AND**：只有两个输入同时为 1，输出才为 1。

**#5 = AND(#1, #2)**：权重只连 #1、#2，#3、#4 的权重为 0：

$$
W_5^{T}=\begin{bmatrix}1&1&0&0\end{bmatrix},\qquad b_5=-1.5.
$$

为什么 $b=-1.5$？设两个输入之和为 $s=h_1+h_2\in\{0,1,2\}$，neuron 计算 $s-1.5$，再过 step function（$\ge0$ 输出 1）：

| $h_1$ | $h_2$ | $s$ | $s-1.5$ | 输出 |
|---|---|---|---|---|
| 0 | 0 | 0 | $-1.5$ | 0 |
| 1 | 0 | 1 | $-0.5$ | 0 |
| 0 | 1 | 1 | $-0.5$ | 0 |
| 1 | 1 | 2 | $0.5$ | **1** |

一般地，若约定 $z>0$ 输出 1，AND 两个二值输入的 bias 只需满足

$$
-2<b\le -1;
$$

若约定 $z\ge0$ 输出 1，则条件改为 $-2<b<-1$。$-1.5$ 在两种约定下都成立，只是方便的选择。**bias 就是老师说的"bar"**：两个输入必须一起跨过它。

**#6 = AND(#3, #4)**：同理

$$
W_6^{T}=\begin{bmatrix}0&0&1&1\end{bmatrix},\qquad b_6=-1.5.
$$

**#5 与 #6 的物理含义**：

- #5 输出 1 $\iff$ $p_1\le0.5$ **且** $p_2\le0.75$（左下矩形）；
- #6 输出 1 $\iff$ $p_1\ge1.5$ **且** $p_2\ge0.25$（右上矩形）。

#### 2.4 第三层：1 个 OR neuron

**#7 = OR(#5, #6)**：

$$
W_7^{T}=\begin{bmatrix}1&1\end{bmatrix},\qquad b_7=-0.5.
$$

验证：设 $s=h_5+h_6$，

| $h_5$ | $h_6$ | $s-0.5$ | 输出 |
|---|---|---|---|
| 0 | 0 | $-0.5$ | 0 |
| 1 | 0 | $0.5$ | **1** |
| 0 | 1 | $0.5$ | **1** |
| 1 | 1 | $1.5$ | **1** |

一般地，若约定 $z>0$ 输出 1，OR 的 bias 只需满足 $-1<b\le0$；若约定 $z\ge0$ 输出 1，则为 $-1\le b<0$。$-0.5$ 在两种约定下都成立，是方便的选择。两个矩形任意一个命中，输出就是 1——这正是 OR 的逻辑。

#### 2.5 矩阵形式与"零权重"的全连接

把三层写成矩阵（这里的 $W^{(l)}$ 直接采用"行 = neuron、列 = 输入"的 $n_l\times n_{l-1}$ 约定；课件把第一层的 $4\times2$ 矩阵记作 $W_1^{T}$）：

$$
W^{(1)}=
\begin{bmatrix}
-1 & 0\\
0 & -1\\
1 & 0\\
0 & 1
\end{bmatrix},\qquad
b^{(1)}=\begin{bmatrix}0.5\\0.75\\-1.5\\-0.25\end{bmatrix};
$$

$$
W^{(2)}=
\begin{bmatrix}
1 & 1 & 0 & 0\\
0 & 0 & 1 & 1
\end{bmatrix},\qquad
b^{(2)}=\begin{bmatrix}-1.5\\-1.5\end{bmatrix};
$$

$$
W^{(3)}=\begin{bmatrix}1 & 1\end{bmatrix},\qquad b^{(3)}=-0.5.
$$

于是 forward propagation 就是

$$
h_1=\sigma\bigl(W^{(1)}p+b^{(1)}\bigr)\in\mathbb{R}^{4},\qquad
h_2=\sigma\bigl(W^{(2)}h_1+b^{(2)}\bigr)\in\mathbb{R}^{2},\qquad
\hat{y}=\sigma\bigl(W^{(3)}h_2+b^{(3)}\bigr)\in\mathbb{R}^{1},
$$

其中 $\sigma$ 是 step function。

> ⭐ **为什么 $W^{(2)}$ 里有那么多 0？** 因为 #5 只需要 #1、#2，#6 只需要 #3、#4。物理上本来可以不连，但为了写成规整的矩阵、让每一层"全连接"，就把不需要的连接权重设为 **0**。课件原话："the extra 0 weights effectively ignore #3 and #4." 这既是矩阵化的技巧，也是后面 **CNN 稀疏/局部连接** 的思想起点。

> ⭐ **解不唯一**：每个 neuron 的 $W_i,b_i$ 可以同乘正常数；边界在不改变分类的前提下也能小幅移动。课件在 OR/AND/XOR 三处都写了 "not unique"。

### 3. XOR 的两种解法

#### 3.1 最小解：2 层 3 neuron

结构：**2 个 hidden neuron + 1 个 output neuron**，共 3 个 neuron、2 层。

| neuron | $W$ | $b$ | 正激活条件 | 作用 |
|---|---|---|---|---|
| hidden #1 | $\begin{bmatrix}1\\1\end{bmatrix}$ | $-0.5$ | $p_1+p_2>0.5$ | 排除 $(0,0)$ |
| hidden #2 | $\begin{bmatrix}-1\\-1\end{bmatrix}$ | $1.5$ | $p_1+p_2<1.5$ | 排除 $(1,1)$ |
| output | $\begin{bmatrix}1\\1\end{bmatrix}$ | $-1.5$ | $h_1+h_2>1.5$ | **AND** |

**边界推导**：

- hidden #1：边界 $p_1+p_2=0.5$，过 $(0.5,0)$ 或 $(0,0.5)$；$W=[1,1]^T$ 指向右上方（正激活一侧）。代入 $(0.5,0)$：$0.5+b=0\Rightarrow b=-0.5$。
- hidden #2：边界 $p_1+p_2=1.5$，过 $(1.5,0)$；$W=[-1,-1]^T$ 指向左下方（正激活一侧）。代入 $(1.5,0)$：$-1.5+b=0\Rightarrow b=1.5$。
- output：AND 两个 hidden 输出，$W=[1,1]^T$，$b=-1.5$（与 §2.3 的 AND 完全一样）。

**逐点验证**（step function，$\ge0$ 输出 1）：

| $p$ | $h_1$ | $h_2$ | $h_1+h_2-1.5$ | $\hat{y}$ | XOR |
|---|---|---|---|---|---|
| $(0,0)$ | 0 | 1 | $-0.5\to0$ | 0 | 0 ✓ |
| $(0,1)$ | 1 | 1 | $0.5\to1$ | 1 | 1 ✓ |
| $(1,0)$ | 1 | 1 | $0.5\to1$ | 1 | 1 ✓ |
| $(1,1)$ | 1 | 0 | $-0.5\to0$ | 0 | 0 ✓ |

> ⭐ **逻辑读法**：hidden #1 = NOT$(0,0)$，hidden #2 = NOT$(1,1)$，输出层做 AND → NOT$(0,0)$ AND NOT$(1,1)$ = XOR。**3 个 neuron 就够了**——这就是 MIT 两位教授 20 年没"看见"的解。

#### 3.2 3 层 7 neuron 解：通用构造的雏形

老师还给了 XOR 的另一种解法：**第一层 4 个 neuron，第二层 2 个 AND，第三层 1 个 OR**，共 7 个 neuron、3 层。

- 对 class 1 的两个点 $(0,1)$、$(1,0)$，各用**一个小矩形**框住；
- 每个矩形需要若干半平面（2D 内部点需 $2^2=4$ 条边；但 XOR 的点在数据域 $[0,1]^2$ 的**角上**，数据域边界已经提供了两条边，所以每个点只需 **2 个 neuron**）；
- 两个矩形分别用一个 AND neuron 合成；
- 最后用一个 OR neuron 把两个矩形并起来。

所以第一层共 $2+2=4$ 个 neuron，第二层 2 个，第三层 1 个——正好是 **4+2+1** 拓扑。课件原话：这个解法 **"less efficient, but useful for universal approximation"**——它不省 neuron，但它展示了"任意区域 = 多个凸区域之并"的通用配方。

> ⭐ **角点 vs 内部点**：如果 class 1 的点在数据域内部，需要 $2^d$ 个半平面把它围成一个封闭小盒（2D 是 4 条边）；在角上，数据域的两条边界免费提供两条边，所以只要 $d=2$ 个 neuron。这解释了为什么 XOR 的 3 层解只需要 4 个第一层 neuron，而一般 2D 点需要 4 个/点。

#### 3.3 两种解对比

| 解法 | 层数 | neuron 数 | 优点 | 缺点 |
|---|---|---|---|---|
| 2 层 3 neuron | 2 | 3 | **最省**，直接利用 XOR 的几何对称性 | 只适用于这个特殊问题，不易推广 |
| 3 层 7 neuron（4+2+1） | 3 | 7 | **通用配方**：任意区域 = 凸区域之并 | neuron 更多，是"存在性"构造 |

考试若问"用最少 neuron 解 XOR"，答 3 个、2 层；若问 universal approximation 的构造思想，答 4+2+1（或更一般的 $N\cdot2^d+N+1$）。

### 4. 什么是 training？weights、biases 与 inference

#### 4.1 Training = 找 weights 和 biases

老师在讲完 4+2+1 的逐层设计后，突然点题：

> "This is actually **training**. ... Training is to get the **weights and bias**. These are called hyperparameters of neural network. You get these parameters weight and bias to get a neural network to do what you want to do."

这句话是后半学期的分水岭：

- 前面 OR / AND / XOR / 4+2+1 的 $W,b$ 都是**人用手算出来的**——老师称为"训练"，但其实是**手工设计**；
- 真正的 training 是**给定数据，让算法自动把 $W,b$ 找出来**；
- 数据就是 **(input, output) pair**：对 4+2+1，数据是"哪些点应该输出 1、哪些应该输出 0"；对 XOR，是那 4 行 truth table；对 MNIST，是 60,000 张图 + 标签。

> ⭐ 老师对"你们没看到我训练"的解释："Well, you might say, Oh, I didn't see you train neural network. How is a training? Well, you have to know what is training. Training is to get the weights and bias." 手工画线、解 bias，本质上也是在"定参数"，只是用的是人的几何直觉，不是优化算法。

#### 4.2 parameters vs hyperparameters（术语澄清）

老师口语把 $W,b$ 叫 **hyperparameters**；标准术语不是这样。考试请用下表：

| 术语 | 定义 | 例子 |
|---|---|---|
| **parameter**（参数） | 模型内部、由训练数据**学习**得到的变量 | weight $W$、bias $b$ |
| **hyperparameter**（超参数） | 训练前**人为设定**、控制训练过程或模型结构的量 | 层数 $L$、每层 neuron 数、activation 选择、learning rate $\eta$、batch size、epoch 数、optimizer、正则化系数 |

所以："4+2+1" 里的 4、2、1 是 hyperparameters（结构）；每个 neuron 的 $W_i,b_i$ 是 parameters（要被训练的东西）。

#### 4.3 Training 与 inference 两个阶段

| 阶段 | weight/bias | 做什么 | 目的 |
|---|---|---|---|
| **training** | **更新** | forward pass → loss → backward → update | 从数据中学 $W,b$ |
| **inference**（推断） | **冻结（frozen）** | 只做 forward pass | 对新输入给预测 |

老师原话："Once you've done that, you let the neural [network] **fix**—you can call it **frozen**. You've frozen your network. Don't change the weight and bias, nothing changes anymore. And now you want it to do **inference**."

> ⭐ ChatGPT 的例子：训练阶段学参数；部署/考试阶段冻结参数，输入一句话，forward 一遍，输出答案。老师说这就是 "train, inference, train, inference" 的循环。

#### 4.4 手工设计 vs 学习；泛化问题

| 维度 | 手工设计（本周的 4+2+1 / XOR） | 学习（真正的 training） |
|---|---|---|
| 参数来源 | 人画边界、解方程 | 数据 + 优化算法 |
| 适用维度 | 2D 玩具问题 | 高维图像/语音/文本 |
| 可扩展性 | 每换一个问题都要重新画 | 同一套算法可复用 |
| 精度 | 玩具问题上可 100% | 真实问题通常达不到 100%，"acceptable accuracy" 即可 |

老师用 ImageNet 说明"为什么不能靠手工/暴力构造"：

- 1 million 张训练图，每张 1000×1000 ≈ 1 million 像素；
- 如果按 universal approximation 的构造，每个点要 $2^d$ 个第一层 neuron（$d=10^6$），数量是天文数字；老师用极粗略的口径说"**至少 10^12 个 neuron**"；
- 更糟的是**没有泛化**：这个构造本质上把每张训练图"记"在一个小盒子里；换一张稍微不同的图，就落在所有盒子外面，输出错误。

> ⭐ 结论：universal approximation 只保证"**存在**一个足够大的网络能做"，不保证"**高效**"或"**能泛化**"。这正是接下来要学 training 和 CNN 的原因。

### 5. ⭐ Forward propagation（前向传播）

#### 5.1 定义

**Forward propagation（前向传播）**：输入从第 1 层逐层传到第 $L$ 层，每一层的输出成为下一层的输入，中间没有任何反馈或循环。老师原话："It's like some kind of propagation of sigma... people will call this **forward propagation**."

对一个 $L$ 层网络：

$$
a^{(0)}=x
\;\longrightarrow\;
z^{(1)}=W^{(1)}a^{(0)}+b^{(1)}
\;\longrightarrow\;
a^{(1)}=f_1(z^{(1)})
\;\longrightarrow\;
\cdots
\;\longrightarrow\;
\hat{y}=a^{(L)}.
$$

> **Motivating example（老师的引子）**：手写数字识别。输入是一张 $16\times16=256$ 像素的小图（像素排成一列作为输入向量），输出层放 **10 个 neuron**，分别对应数字 0–9。老师说这是 **Yann LeCun** 最早为 post office 做**邮政编码识别**时用的任务，也是早期 **CNN** 的著名应用——输入是"一堆像素"，输出是"10 类之一"，这正是 classification 的标准设定。后面的 forward propagation 数值例，就是在这个设定下"输入 → 逐层算 → 10 类得分"的缩小版。

#### 5.2 单层公式

对第 $l$ 层（$n_{l-1}$ 个输入、$n_l$ 个 neuron）：

$$
z^{(l)}=W^{(l)}a^{(l-1)}+b^{(l)},\qquad
a^{(l)}=f_l\bigl(z^{(l)}\bigr),
$$

其中

- $W^{(l)}\in\mathbb{R}^{n_l\times n_{l-1}}$：第 $l$ 层的 weight matrix，**每一行对应一个 neuron**；
- $b^{(l)}\in\mathbb{R}^{n_l}$：bias vector；
- $z^{(l)}\in\mathbb{R}^{n_l}$：**local field / pre-activation**（加权和，未过 activation）；
- $f_l$：activation function，**逐元素**作用；
- $a^{(l)}\in\mathbb{R}^{n_l}$：该层输出（activation）。

单个 neuron 就是

$$
z=\sum_{j=0}^{m}w_j a_j+b,\qquad a=f(z),
$$

与 Week 8 §2.2 完全一致（$a_0=+1$ 吸收 bias）。

> ⭐ **层数怎么数**：**输入层的节点不是 neuron**——它们没有 weight、bias，也没有 activation，只是把特征值传给第一层，所以不计入层数。**hidden layer（隐藏层）** 是输入与输出之间的层，"hidden" 指它的输出不直接暴露给外界。因此课程里的 **"2-layer network" = 1 个 hidden layer + 1 个 output layer**；"3-layer network" = 2 个 hidden + 1 个 output。老师特意纠正："This is not input neuron; people say input neuron—it's misleading. There is no neuron here because there is no operation."

#### 5.3 数值例 1：2-2 sigmoid 网络

考虑一个最简单的单层网络：2 个输入、2 个 neuron、sigmoid activation。

$$
x=\begin{bmatrix}1\\-1\end{bmatrix},\qquad
W=\begin{bmatrix}1&-2\\-1&1\end{bmatrix},\qquad
b=\begin{bmatrix}1\\0\end{bmatrix}.
$$

**逐 neuron 计算**：

第一个 neuron：

$$
z_1=1\cdot1+(-2)\cdot(-1)+1=1+2+1=4,
\qquad
a_1=\sigma(4)=\frac{1}{1+e^{-4}}\approx0.982.
$$

第二个 neuron：

$$
z_2=(-1)\cdot1+1\cdot(-1)+0=-1-1=-2,
\qquad
a_2=\sigma(-2)=\frac{1}{1+e^{2}}\approx0.119.
$$

所以

$$
a=\sigma(Wx+b)=\sigma\left(\begin{bmatrix}4\\-2\end{bmatrix}\right)
=\begin{bmatrix}0.982\\0.119\end{bmatrix}.
$$

> 转写里的 "62a0 82" 就是 **[0.982, 0.12]** 的 ASR 乱码。老师特意说："The output will be very close to one, not exactly one... 0.98... this will be close to zero... 0.12."

**矩阵形式**：

$$
z=Wx+b,\qquad a=\sigma(z)\quad\text{(elementwise)}.
$$

这是一个非线性映射 $f:\mathbb{R}^2\to\mathbb{R}^2$。虽然每层只是"矩阵乘 + 逐元素非线性"，但多层复合后可以表示很复杂的函数。

> ⭐ 如果还有下一层，就把 $a$ 当作新的输入，重复 $z'=W'a+b'$、$a'=\sigma(z')$。**整个网络就是同一个操作重复 $L$ 次。**

#### 5.4 数值例 2：4+2+1 网络逐层验证

用 §2.5 的 $W^{(1)},b^{(1)},W^{(2)},b^{(2)},W^{(3)},b^{(3)}$，activation 取 step function：

$$
\sigma(z)=\mathbf{1}[z\ge0].
$$

取 $p=\begin{bmatrix}0\\1\end{bmatrix}$：

**第 1 层**：

$$
W^{(1)}p=
\begin{bmatrix}-1&0\\0&-1\\1&0\\0&1\end{bmatrix}
\begin{bmatrix}0\\1\end{bmatrix}
=\begin{bmatrix}0\\-1\\0\\1\end{bmatrix},
$$

$$
z^{(1)}=W^{(1)}p+b^{(1)}
=\begin{bmatrix}0\\-1\\0\\1\end{bmatrix}
+\begin{bmatrix}0.5\\0.75\\-1.5\\-0.25\end{bmatrix}
=\begin{bmatrix}0.5\\-0.25\\-1.5\\0.75\end{bmatrix},
\qquad
h_1=\sigma(z^{(1)})=\begin{bmatrix}1\\0\\0\\1\end{bmatrix}.
$$

**第 2 层**：

$$
W^{(2)}h_1=
\begin{bmatrix}1&1&0&0\\0&0&1&1\end{bmatrix}
\begin{bmatrix}1\\0\\0\\1\end{bmatrix}
=\begin{bmatrix}1\\1\end{bmatrix},
$$

$$
z^{(2)}=W^{(2)}h_1+b^{(2)}
=\begin{bmatrix}1\\1\end{bmatrix}
+\begin{bmatrix}-1.5\\-1.5\end{bmatrix}
=\begin{bmatrix}-0.5\\-0.5\end{bmatrix},
\qquad
h_2=\sigma(z^{(2)})=\begin{bmatrix}0\\0\end{bmatrix}.
$$

**第 3 层**：

$$
z^{(3)}=W^{(3)}h_2+b^{(3)}=0-0.5=-0.5,
\qquad
\hat{y}=\sigma(-0.5)=0.
$$

结果 $\hat{y}=0$，与"$(0,1)$ 不在两个矩形内"一致。✓

**多取几个点验证**（step 用 $\ge0$）：

| $p$ | $z^{(1)}$ | $h_1$ | $z^{(2)}$ | $h_2$ | $z^{(3)}$ | $\hat{y}$ | 期望 |
|---|---|---|---|---|---|---|---|
| $(0,1)$ | $[0.5,-0.25,-1.5,0.75]$ | $[1,0,0,1]$ | $[-0.5,-0.5]$ | $[0,0]$ | $-0.5$ | 0 | 0 ✓ |
| $(0.25,0.25)$ | $[0.25,0.5,-1.25,0]$ | $[1,1,0,1]$ | $[0.5,-0.5]$ | $[1,0]$ | $0.5$ | 1 | 1 ✓ |
| $(0.75,0.5)$ | $[-0.25,0.25,-0.75,0.25]$ | $[0,1,0,1]$ | $[-0.5,-0.5]$ | $[0,0]$ | $-0.5$ | 0 | 0 ✓ |
| $(1.75,0.5)$ | $[-1.25,0.25,0.25,0.25]$ | $[0,1,1,1]$ | $[-0.5,0.5]$ | $[0,1]$ | $0.5$ | 1 | 1 ✓ |

> ⭐ **考试提示**：老师明确说考试可能让你**手算 forward pass**。步骤固定：$z^{(l)}=W^{(l)}a^{(l-1)}+b^{(l)}$ → 过 activation → 下一层。注意矩阵行是 neuron、列是输入；bias 逐行加。若某个点恰好落在边界上（$z=0$），用 $\ge0$ 还是 $>0$ 可能改变该 neuron 的输出，但通常不影响最终分类；课件说 "whether it's $>0$ or $\ge0$ doesn't matter in practice."

#### 5.5 一般 $L$ 层网络的 forward propagation

$$
\boxed{
\begin{aligned}
a^{(0)}&=x,\\
z^{(l)}&=W^{(l)}a^{(l-1)}+b^{(l)},\\
a^{(l)}&=f_l\bigl(z^{(l)}\bigr),\qquad l=1,2,\dots,L,\\
\hat{y}&=a^{(L)}.
\end{aligned}}
$$

**维度表**：

| 量 | 维度 | 说明 |
|---|---|---|
| $a^{(l)}$ | $n_l\times1$ | 第 $l$ 层输出；$n_0$ = 输入维度，$n_L$ = 输出维度 |
| $W^{(l)}$ | $n_l\times n_{l-1}$ | 第 $l$ 层 weight matrix |
| $b^{(l)}$ | $n_l\times1$ | 第 $l$ 层 bias |
| $z^{(l)}$ | $n_l\times1$ | pre-activation |

**mini-batch 版本**（$m$ 个样本同时算）：

$$
A^{(0)}=X\in\mathbb{R}^{n_0\times m},\qquad
Z^{(l)}=W^{(l)}A^{(l-1)}+b^{(l)}\mathbf{1}_m^{T},\qquad
A^{(l)}=f_l(Z^{(l)}),
$$

其中 $\mathbf{1}_m$ 是全 1 列向量，$b^{(l)}\mathbf{1}_m^{T}$ 把 bias **广播**到每个样本。这样一次矩阵乘就算完整个 batch——这是 GPU 喜欢的形式。

#### 5.6 矩阵形式为什么重要

老师花了很长一段讲这件事，核心就三句：

1. **写法紧凑**：一层的"每个 neuron 各自加权求和"被写成 $z=Wa+b$，比逐 neuron 写清楚得多。
2. **计算高效**：矩阵乘法可以被 BLAS、GPU 高度并行化。老师原话："Once you put into a matrix, **everything becomes easy**."
3. **硬件契合**：GPU 本来是为图形渲染（大量矩阵运算）设计的；神经网络也全是矩阵运算，所以 GPU 能把训练加速几个数量级。老师说这个"GPU + neural network"的联想花了大家约 10 年才普遍意识到——这正是 Week 8 §4.4 讲的 deep learning 三大驱动力之一。

> MATLAB 的名字就来自 **MAT**rix；老师感叹早年 MATLAB licence 贵、要排队，Python 免费后 "everything's free... you can do neural network, AI, whatever."

#### 5.7 Inference：冻结权重后的 forward pass

- **Training**：forward → loss → backward → update（Week 10 讲）。
- **Inference**：$W,b$ 冻结，只做 forward。老师原话："You frozen your network... nothing changes anymore... you have an input... see the neural network output... that's your inference."
- 对 4+2+1 玩具问题，训练集上可以做到 **100% accuracy**；对真实问题（如 ChatGPT），做不到 100%，只要 **accuracy acceptable** 即可。

### 6. ⭐ Universal approximation（本周的直观证明）

Week 8 已给出结论；本周老师用"切盒子 / 矩形脉冲"给出**非严格但直观**的证明，并强调定理的边界条件。

#### 6.1 Classification：1/2/3 层能表示的区域

| 网络层数（不计输入层） | hidden layer 数 | 能表示的 decision region | 直观 |
|---|---|---|---|
| **1-layer** | 0 | **half-plane**（半平面） | 一条直线切一刀 |
| **2-layer** | 1 | **单个 convex region**（凸区域） | 多条半平面取交（AND） |
| **3-layer** | 2 | **任意区域**（arbitrary，含非凸、不连通、带洞） | 多个凸区域取并（OR） |

> 课件原文："Note that a 2-layer network can generate only a **single convex decision region**." 所以 §2 的两个分离矩形**必须**用 3 层；XOR 的 2 层 3-neuron 解之所以可行，是因为它用两个半平面的**交**直接构造了一个凸区域（带状），再在输出层做 AND——它并没有试图用单个凸区域去表示 XOR 的两个分离点，而是用了"两个半平面 + AND"的特殊结构。更一般地，2 层网络的每个输出 neuron 只能给出一个凸区域。

#### 6.2 3 层 MLP 的构造性证明

设：

- 输入维度 $d$；
- 两个 class $C_1,C_2$；
- $C_1$ 有 $N$ 个数据点。

**构造**：

1. **第 1 个 hidden layer**：对 $C_1$ 的每个点，用 **$2^d$ 个 neuron** 切一个很小的凸区域（2D 时 $2^d=4$，正好对应围住一个小矩形的 4 条边；更高维的严格几何解释不是本课重点，记住课件这个计数即可）。按课件口径记：**每组 $2^d$ 个第一层 hidden neuron**。
2. **第 2 个 hidden layer**：每个 neuron 做一个 **AND**，把一组 $2^d$ 个半平面合成为一个凸区域。$N$ 个点 → $N$ 个 AND neuron。
3. **Output layer**：一个 **OR** neuron，把 $N$ 个凸区域并起来。任意一个盒子命中，输出就是 $C_1$。

**总数**：

$$
\underbrace{N\cdot 2^d}_{\text{第 1 个 hidden layer}}
+\underbrace{N}_{\text{第 2 个 hidden layer}}
+\underbrace{1}_{\text{output}}.
$$

2D 时就是 $4N+N+1$（XOR 的两个点在数据域角上，数据域边界免费提供两条边，所以 §3.2 只需 7 个；一般内部点才按 $4N+N+1$ 计）。只要盒子足够小、$N$ 足够大，任何 decision region 都能被任意精度逼近——这就是 **universal approximation for classification**。

> ⭐ 这个证明是**存在性**的：它告诉你"能"，不告诉你"怎么高效地找"。老师原话："The universal approximation theorem doesn't tell you how to do it. It just tells you you can do it."

#### 6.3 为什么这个构造不实用：$10^{12}$ 个 neuron 与记忆

老师用 ImageNet 算了一笔账：

- $N=10^6$ 张训练图；
- 每张图 $1000\times1000\approx10^6$ 像素，即 $d=10^6$；
- 按构造，第一层需要 $N\cdot2^d$ 个 neuron——这是天文数字；老师用极粗略的"每像素至少 1 个 neuron"口径说"**至少 $10^{12}$ 个**"，已经远超任何实际模型；
- 而且这是**死记硬背**：每个训练图有自己的小盒子，换一张稍微不同的图就落在所有盒子外，**没有 generalization**。

> ⭐ 所以 universal approximation 的意义是"**理论上的底气**"：神经网络不是瞎试，它原则上能表示任何函数/区域。但真正要做的是**高效训练**（backprop + SGD）和**利用数据结构的架构**（CNN），而不是暴力构造。老师原话："There are good ways, smart ways to do it. You don't do brute force."

#### 6.4 Function approximation：2 层 MLP 与"矩形脉冲"

Classification 之外，神经网络还擅长 **regression / function approximation**（如用历史价格预测明天股价）。

**定理（课件版）**：

> A hidden layer of **nonconstant, bounded, and continuous** neurons (with weights and biases), plus a **linear output neuron** (with weights but **without bias**) can approximate **any continuous function** to any arbitrary accuracy if there are enough hidden neurons.

注意这里是 **2-layer network**：1 个 hidden layer + 1 个 linear output layer；输入层不计。

**直观证明（back-of-the-napkin）**：

1. **单个 step neuron 给出一个台阶**。取

$$
s(z)=\mathbf{1}[z\ge0],
$$

一个 weight 为 $w$、bias 为 $-wt$ 的 neuron 计算 $s(w(x-t))$：$x<t$ 输出 0，$x>t$ 输出 1，台阶在 $t$。

2. **两个错开的台阶相减得到一个矩形脉冲**。取

$$
\phi_{\Delta,t}(x)=s\bigl(w(x-t)\bigr)-s\bigl(w(x-t-\Delta)\bigr).
$$

第一个 neuron 在 $t$ 处上升，第二个在 $t+\Delta$ 处上升；相减后，只在 $[t,t+\Delta)$ 区间内为 1，其余为 0——一个宽度 $\Delta$、高度 1 的矩形。

3. **多个脉冲加权求和，拼出阶梯函数**：

$$
g(x)=\sum_{k=1}^{K}c_k\,\phi_{\Delta,t_k}(x).
$$

每个脉冲的高度 $c_k$ 对应函数在该小区间的值；$K$ 个脉冲就是 $K$ 段阶梯。

4. **把宽度 $\Delta$ 缩小**，阶梯越来越细；对连续函数 $f$，当 $\Delta\to0$、$K\to\infty$ 时，$g\to f$ 任意精度。

5. **输出层是线性的**：它只做 $\sum_k c_k(\cdot)$，没有 bias，也没有非线性——这正是定理要求的 "linear output neuron (with weights but without bias)"。

> ⭐ 老师把这种证明叫 **"back of the napkin" proof**（餐巾纸上的证明）：在 McDonald's 拿张餐巾纸就能写。严格的数学证明约 **30 页**，非常 dense；课上说 "we're not going to do it."

#### 6.5 定理的严格条件与边界

| 条件 | 含义 | 反例/注意 |
|---|---|---|
| **nonconstant** | hidden activation 不能是常数 | 常数 neuron 的输出与输入无关，什么也表示不了 |
| **bounded** | 输出有界 | **ReLU** 无界（$z\to+\infty$ 时输出 $\to+\infty$），严格按定理不满足；老师课上把它列为"是否有 universal approximation 证明"的开放问题 |
| **continuous** | 输出连续 | **step function** 在 0 处跳变，不连续；老师指出严格按定理它也不满足，但实际中 step function 网络仍然能做很多事 |
| **linear output neuron** | 输出层线性、可无 bias | 课件版定理的设定；用非线性输出"应该也能 work"，但老师说他没见到证明 |
| **enough hidden neurons** | neuron 足够多 | 定理只说"存在"，不给出具体数量 |

> ⭐ **充分条件 ≠ 必要条件**：step function 不满足"连续"，不代表它不能逼近；ReLU 不满足"有界"，也不代表它不能。定理给的是**一类充分条件**。考试若问"定理的条件"，按课件答 nonconstant, bounded, continuous + linear output without bias；若问"step/ReLU 行不行"，答"课件把严格证明留作开放问题，但实践中 step/ReLU 非常常用"。

#### 6.6 定理没有告诉你的事

老师逐条列了 universal approximation 的"无能"：

| 问题 | 定理是否回答 |
|---|---|
| 需要多少 hidden neuron？ | ❌ 不知道；只能试：5 个、20 个、25 个、30 个…… |
| 怎么找到 $W,b$？ | ❌ 不知道；这是 training / backprop 的事 |
| 用几层最好？ | ❌ 不知道；1 层够不够、2 层够不够、要不要更深，没有理论答案 |
| 每个 neuron 用什么 activation？ | ❌ 只知道"非恒定"这类很弱的条件；具体选择靠经验 |
| 训练效率、泛化能力？ | ❌ 完全不保证；暴力构造甚至会死记硬背 |

> ⭐ 老师原话："It's frustrating. Sometimes people say neural network is like a black box... some trick. Somebody knows a trick... Unfortunately, so far it's like that." 这就是为什么后半学期要讲 training 和 architecture，而不是停在"存在性"。

### 7. Deep network 到底"深"在哪里

| 概念 | 传统说法 | 现代理解 |
|---|---|---|
| **shallow network** | 1–2 个 hidden layer | 仍指层数少 |
| **deep network** | >2 个 hidden layer；早期 9 层就算"非常深"，"only crazy people will use nine layers" | **不只是层数多**，而是"层以什么方式组织"——对图像就是 **CNN** 的 convolution / pooling 等结构 |
| 深度 vs 宽度 | 100 个 neuron 放一层，还是 50+50，还是 25+25+25+25？ | **没有理论答案**；老师："Nobody knows. You just try." |

要点：

- Universal approximation 说 **1–2 个 hidden layer 原则上足够**，但"足够"不等于"高效"：同样的函数，深网络可能用少得多的参数表示。
- 老师强调："Deep network in the general sense is **not just more layers**... it's **how the layers are done**." 对图像，CNN 的层有特定结构（局部连接、权重共享），不是随便堆全连接层。
- 课程进度：本周仍在 NN 基础；接下来先讲 **training**（Week 10–11），再讲 **CNN / deep architectures**（Week 12 左右）。Week 1 表把 CNN 放在 Week 9，是原计划，实际顺延。

### 8. 本周要点小结

- **4+2+1 三层网络的完整设计**：第 1 层 4 个 neuron 用半平面切出两个矩形（$W$ 定方向、$b$ 定位置）；第 2 层 2 个 AND neuron（$W=[1,1,0,0]$ 或 $[0,0,1,1]$，$b=-1.5$）；第 3 层 1 个 OR neuron（$W=[1,1]$，$b=-0.5$）。
- **AND / OR 的 bias 选择**：AND 需 $-2<b\le-1$；OR 需 $-1<b\le0$。bias 就是"门槛/bar"。
- **XOR 最小解**：2 层、3 个 neuron（2 hidden + 1 output）；hidden #1 排除 $(0,0)$，hidden #2 排除 $(1,1)$，输出层 AND。3 层 4+2+1 也能解，且是 universal 构造的雏形。
- **Training 的定义**：从数据中找 **weights + biases**；它们是 **parameters**，不是 hyperparameters。Training 后 **freeze**，进入 **inference**（只做 forward）。
- **Forward propagation**：$a^{(0)}=x$，$z^{(l)}=W^{(l)}a^{(l-1)}+b^{(l)}$，$a^{(l)}=f_l(z^{(l)})$；逐层重复，直到 $\hat{y}=a^{(L)}$。矩阵形式 $Z=WA+b$ 是 GPU 加速的关键。
- **数值例**：2-2 sigmoid 网络 $W=\begin{bmatrix}1&-2\\-1&1\end{bmatrix}$、$b=[1,0]^T$、$x=[1,-1]^T$ → $a=[0.982,0.119]^T$；4+2+1 网络对 $p=(0,1)$ → $\hat{y}=0$。
- **Universal approximation（classification）**：1 层 half-plane；2 层单个 convex region；3 层任意区域。构造：$N\cdot2^d$ 个第一层 neuron + $N$ 个 AND + 1 个 OR。
- **Universal approximation（function）**：2 层 MLP（nonconstant, bounded, continuous hidden + linear output without bias）可任意精度逼近任意连续函数；直观证明用"两个错开 step 相减 = 矩形脉冲，多个脉冲拼函数"。
- **定理的局限**：只保证存在，不保证高效/泛化；不告诉你 neuron 数、层数、$W,b$ 怎么求。暴力构造会死记硬背，$10^6$ 张图 × $10^6$ 像素需要至少 $10^{12}$ 个 neuron（老师口径），不可行。
- **Backprop 本周只预告**：老师明确说 "we can continue the next episode"；正式推导在 Week 10。§9 是预习，不是本周课堂内容。

---

### 9. ⚠️ 衔接 Week 10：Backpropagation、Gradient Descent 与 SGD 完整数学准备

> **再次说明**：以下内容**不是 Week 9 课堂讲授**。`week9.txt` 在 forward propagation 后结束，老师原话 "we can continue the next episode. We continue next time." 本节是为 Week 10 **Training Deep Networks** 和 **Quiz 2（Week 8–11）** 预先整理的完整推导；Week 10 上课时再对照老师版本。已掌握 forward propagation 的读者可以把它当作下一讲的预习。

#### 9.1 为什么需要 backprop

Forward propagation 只回答"给定 $W,b$，输出是什么"。Training 要回答相反的问题：

> 给定训练数据 $\{(x_k,y_k)\}_{k=1}^{m}$，如何调整所有层的 $W^{(l)},b^{(l)}$，使输出 $\hat{y}_k$ 尽量接近 $y_k$？

做法：

1. 定义 **loss function（损失函数）** $L(W,b)$ 衡量预测与目标的差距；
2. 用 **gradient descent（梯度下降）** 沿负梯度方向更新参数；
3. 用 **backpropagation（反向传播）** 高效计算 $\partial L/\partial W^{(l)}$、$\partial L/\partial b^{(l)}$——即**链式法则（chain rule）** 在计算图上的反向应用。

> ⭐ 为什么不能直接数值求导？参数有 $P$ 个，数值差分要对每个参数做一次 forward（或两次），复杂度 $O(P)$ 次网络前传；backprop 一次 forward + 一次 backward 就能得到**所有**参数的梯度，复杂度与一次 forward 同阶。这是神经网络能训练的关键。

#### 9.2 Loss function（损失函数）

| 任务 | 输出层 activation | 常用 loss | 公式（单样本） |
|---|---|---|---|
| **regression**（回归） | linear（identity） | **MSE**（mean squared error） | $L=\frac12\sum_i(y_i-\hat{y}_i)^2$ |
| **binary classification**（二分类） | sigmoid | **BCE**（binary cross-entropy） | $L=-\sum_i\bigl[y_i\log\hat{y}_i+(1-y_i)\log(1-\hat{y}_i)\bigr]$ |
| **multi-class classification**（多分类） | softmax | **CE**（cross-entropy） | $L=-\sum_i y_i\log\hat{y}_i$ |

- $y_i$ 是 **one-hot** 标签（正确类为 1，其余为 0）；
- $\hat{y}_i$ 是模型给出的概率；
- 多分类时 $\sum_i\hat{y}_i=1$，$\sum_i y_i=1$。
- 若把 MSE 用于 sigmoid 输出，梯度含 $\sigma'$，饱和区梯度很小；**cross-entropy + sigmoid/softmax** 的梯度会化简为 $\hat{y}-y$，数值上更稳定（见 §9.7）。

#### 9.3 Gradient descent 与 weight update

**Gradient descent（梯度下降）** 的更新规则：

$$
\boxed{
W^{(l)}\leftarrow W^{(l)}-\eta\,\frac{\partial L}{\partial W^{(l)}},\qquad
b^{(l)}\leftarrow b^{(l)}-\eta\,\frac{\partial L}{\partial b^{(l)}}}
$$

其中 $\eta>0$ 是 **learning rate（学习率）**。

- 梯度 $\partial L/\partial W$ 指向 loss **上升最快**的方向；取负号就是下降最快方向。
- $\eta$ 控制步长：太大会越过最小值、震荡甚至发散；太小则收敛慢。
- 对所有层、所有 neuron、所有 weight/bias 同时做这个更新，就完成一次 **weight update（权重更新）**。

#### 9.4 Chain rule：从标量例子开始

先看一个 neuron：

$$
z=wx+b,\qquad \hat{y}=\sigma(z),\qquad L=\frac12(y-\hat{y})^2.
$$

要求 $\partial L/\partial w$。链式法则逐段乘：

$$
\frac{\partial L}{\partial w}
=
\frac{\partial L}{\partial \hat{y}}
\cdot
\frac{\partial \hat{y}}{\partial z}
\cdot
\frac{\partial z}{\partial w}.
$$

逐项算：

$$
\frac{\partial L}{\partial \hat{y}}=-(y-\hat{y}),\qquad
\frac{\partial \hat{y}}{\partial z}=\sigma'(z)=\hat{y}(1-\hat{y}),\qquad
\frac{\partial z}{\partial w}=x.
$$

所以

$$
\boxed{
\frac{\partial L}{\partial w}=-(y-\hat{y})\,\sigma'(z)\,x
}
$$

同理

$$
\frac{\partial L}{\partial b}=-(y-\hat{y})\,\sigma'(z).
$$

> ⭐ 这就是 backprop 的全部思想：**从 loss 往回，一层一层乘上局部导数**。多层的区别只是链条更长、需要复用中间量。

#### 9.5 两层网络的完整 backprop 推导

考虑一个 2 层网络（1 个 hidden layer + 1 个 output layer）：

$$
x\in\mathbb{R}^{n_0},\qquad
z^{(1)}=W^{(1)}x+b^{(1)},\qquad
a^{(1)}=\sigma(z^{(1)}),
$$

$$
z^{(2)}=W^{(2)}a^{(1)}+b^{(2)},\qquad
\hat{y}=\sigma(z^{(2)}).
$$

Loss 取 MSE：

$$
L=\frac12\sum_i(y_i-\hat{y}_i)^2.
$$

**定义误差项（error term）**：

$$
\delta^{(l)}\equiv\frac{\partial L}{\partial z^{(l)}}.
$$

##### 第 2 层（output layer）

对每个输出分量 $i$：

$$
\delta_i^{(2)}
=
\frac{\partial L}{\partial z_i^{(2)}}
=
\frac{\partial L}{\partial \hat{y}_i}
\cdot
\frac{\partial \hat{y}_i}{\partial z_i^{(2)}}
=
-(y_i-\hat{y}_i)\,\sigma'(z_i^{(2)})
=
(\hat{y}_i-y_i)\,\sigma'(z_i^{(2)}).
$$

写成向量（$\odot$ 为逐元素乘）：

$$
\boxed{
\delta^{(2)}=(\hat{y}-y)\odot\sigma'(z^{(2)})
}
$$

对 weight 的偏导，注意 $z_i^{(2)}=\sum_j W_{ij}^{(2)}a_j^{(1)}+b_i^{(2)}$，所以 $\partial z_i^{(2)}/\partial W_{ij}^{(2)}=a_j^{(1)}$：

$$
\frac{\partial L}{\partial W_{ij}^{(2)}}
=
\frac{\partial L}{\partial z_i^{(2)}}
\cdot
\frac{\partial z_i^{(2)}}{\partial W_{ij}^{(2)}}
=
\delta_i^{(2)}a_j^{(1)}
$$

$$
\boxed{
\frac{\partial L}{\partial W^{(2)}}=\delta^{(2)}\bigl(a^{(1)}\bigr)^{T}
}
$$

对 bias：

$$
\frac{\partial L}{\partial b_i^{(2)}}=\delta_i^{(2)}
\qquad\Longrightarrow\qquad
\boxed{\frac{\partial L}{\partial b^{(2)}}=\delta^{(2)}}.
$$

##### 第 1 层（hidden layer）

要把误差从 $z^{(2)}$ 传回 $z^{(1)}$。对 hidden 分量 $j$：

$$
\delta_j^{(1)}
=
\frac{\partial L}{\partial z_j^{(1)}}
=
\sum_i
\frac{\partial L}{\partial z_i^{(2)}}
\cdot
\frac{\partial z_i^{(2)}}{\partial a_j^{(1)}}
\cdot
\frac{\partial a_j^{(1)}}{\partial z_j^{(1)}}.
$$

逐项：

$$
\frac{\partial L}{\partial z_i^{(2)}}=\delta_i^{(2)},\qquad
\frac{\partial z_i^{(2)}}{\partial a_j^{(1)}}=W_{ij}^{(2)},\qquad
\frac{\partial a_j^{(1)}}{\partial z_j^{(1)}}=\sigma'(z_j^{(1)}).
$$

所以

$$
\delta_j^{(1)}
=
\left(\sum_i \delta_i^{(2)}W_{ij}^{(2)}\right)\sigma'(z_j^{(1)})
=
\left[(W^{(2)})^{T}\delta^{(2)}\right]_j\sigma'(z_j^{(1)}).
$$

向量形式：

$$
\boxed{
\delta^{(1)}=(W^{(2)})^{T}\delta^{(2)}\odot\sigma'(z^{(1)})
}
$$

于是

$$
\boxed{
\frac{\partial L}{\partial W^{(1)}}=\delta^{(1)}x^{T}
}
\qquad
\boxed{
\frac{\partial L}{\partial b^{(1)}}=\delta^{(1)}
}
$$

> ⭐ **检查维度**：$\delta^{(2)}\in\mathbb{R}^{n_2}$，$a^{(1)}\in\mathbb{R}^{n_1}$，所以 $\delta^{(2)}(a^{(1)})^T\in\mathbb{R}^{n_2\times n_1}$，与 $W^{(2)}$ 同形；$(W^{(2)})^T\delta^{(2)}\in\mathbb{R}^{n_1}$，与 $\delta^{(1)}$ 同形。维度对得上，公式就大概率没写错。

#### 9.6 向量化与一般 $L$ 层公式

对 $L$ 层网络，定义

$$
\delta^{(l)}=\frac{\partial L}{\partial z^{(l)}},\qquad l=1,\dots,L.
$$

**输出层**（$l=L$）：

$$
\delta^{(L)}=\nabla_{\hat{y}}L\odot f_L'(z^{(L)}).
$$

**反向递推**（$l=L-1,\dots,1$）：

$$
\boxed{
\delta^{(l)}=(W^{(l+1)})^{T}\delta^{(l+1)}\odot f_l'(z^{(l)})
}
$$

**参数梯度**：

$$
\boxed{
\frac{\partial L}{\partial W^{(l)}}=\delta^{(l)}\bigl(a^{(l-1)}\bigr)^{T}
}
\qquad
\boxed{
\frac{\partial L}{\partial b^{(l)}}=\delta^{(l)}
}
$$

**更新**：

$$
W^{(l)}\leftarrow W^{(l)}-\eta\,\delta^{(l)}\bigl(a^{(l-1)}\bigr)^{T},
\qquad
b^{(l)}\leftarrow b^{(l)}-\eta\,\delta^{(l)}.
$$

**mini-batch**（$m$ 个样本）取平均：

$$
\frac{\partial L}{\partial W^{(l)}}=\frac1m\sum_{k=1}^{m}\delta_k^{(l)}\bigl(a_k^{(l-1)}\bigr)^{T},
\qquad
\frac{\partial L}{\partial b^{(l)}}=\frac1m\sum_{k=1}^{m}\delta_k^{(l)}.
$$

> ⭐ **记忆口诀**：**forward 存 $a$，backward 传 $\delta$；weight 梯度 = 本层 $\delta$ 乘上层 $a$ 的转置；bias 梯度 = 本层 $\delta$。** 这就是所有深度学习框架 `loss.backward()` 做的事。

#### 9.7 Cross-entropy + softmax 的化简

多分类最常用 **softmax + cross-entropy**：

$$
\hat{y}_i=\frac{e^{z_i}}{\sum_j e^{z_j}},\qquad
L=-\sum_i y_i\log\hat{y}_i.
$$

**结论**：

$$
\boxed{
\delta_i^{(L)}=\frac{\partial L}{\partial z_i}=\hat{y}_i-y_i
}
$$

即 $\delta^{(L)}=\hat{y}-y$。推导（用 $\sum_i y_i=1$）：

$$
\frac{\partial L}{\partial z_i}
=
-\frac{y_i}{\hat{y}_i}\hat{y}_i(1-\hat{y}_i)
+\sum_{j\ne i}\frac{y_j}{\hat{y}_j}\hat{y}_j\hat{y}_i
=
-y_i(1-\hat{y}_i)+\hat{y}_i\sum_{j\ne i}y_j
=
-y_i+\hat{y}_i(y_i+\sum_{j\ne i}y_j)
=
\hat{y}_i-y_i.
$$

**sigmoid + BCE** 同理：

$$
\delta^{(L)}=\hat{y}-y.
$$

> ⭐ 这就是为什么分类任务几乎都用 cross-entropy 而不是 MSE：**梯度形式极简，且不会因为 sigmoid/softmax 饱和而消失**。

**常用组合表**：

| 任务 | 输出 activation | loss | $\delta^{(L)}$ |
|---|---|---|---|
| regression | linear | MSE | $\hat{y}-y$ |
| binary classification | sigmoid | BCE | $\hat{y}-y$ |
| multi-class | softmax | CE | $\hat{y}-y$ |

#### 9.8 数值例：对 §5.3 的玩具网络做一次梯度下降

用 §5.3 的网络：

$$
x=\begin{bmatrix}1\\-1\end{bmatrix},\quad
W=\begin{bmatrix}1&-2\\-1&1\end{bmatrix},\quad
b=\begin{bmatrix}1\\0\end{bmatrix},\quad
\hat{y}=a=\begin{bmatrix}0.982\\0.119\end{bmatrix}.
$$

设目标 $y=\begin{bmatrix}1\\0\end{bmatrix}$，loss 用 MSE：

$$
L=\frac12\bigl[(1-0.98201)^2+(0-0.11920)^2\bigr]
=\frac12(0.0003235+0.0142093)
\approx0.007266.
$$

**Step 1：算 $\delta$**。

$$
\sigma'(z_1)=\hat{y}_1(1-\hat{y}_1)=0.98201\times0.017986\approx0.017663,
$$
$$
\sigma'(z_2)=\hat{y}_2(1-\hat{y}_2)=0.11920\times0.88080\approx0.104993.
$$

$$
\delta=(\hat{y}-y)\odot\sigma'(z)
=
\begin{bmatrix}0.98201-1\\0.11920-0\end{bmatrix}
\odot
\begin{bmatrix}0.017663\\0.104993\end{bmatrix}
=
\begin{bmatrix}-0.017986\times0.017663\\0.11920\times0.104993\end{bmatrix}
\approx
\begin{bmatrix}-0.0003177\\0.0125155\end{bmatrix}.
$$

**Step 2：算梯度**。

$$
\frac{\partial L}{\partial W}=\delta x^{T}
=
\begin{bmatrix}-0.0003177\\0.0125155\end{bmatrix}
\begin{bmatrix}1&-1\end{bmatrix}
=
\begin{bmatrix}
-0.0003177 & 0.0003177\\
0.0125155 & -0.0125155
\end{bmatrix},
$$

$$
\frac{\partial L}{\partial b}=\delta=
\begin{bmatrix}-0.0003177\\0.0125155\end{bmatrix}.
$$

**Step 3：取 $\eta=0.1$ 更新**。

$$
W\leftarrow W-\eta\frac{\partial L}{\partial W}
=
\begin{bmatrix}
1.0000318 & -2.0000318\\
-1.0012516 & 1.0012516
\end{bmatrix},
$$

$$
b\leftarrow b-\eta\frac{\partial L}{\partial b}
=
\begin{bmatrix}
1.0000318\\
-0.0012516
\end{bmatrix}.
$$

**Step 4：检查 loss 是否下降**（新的 forward）：

$$
z'_1=1.0000318\cdot1+(-2.0000318)\cdot(-1)+1.0000318\approx4.0000953,
$$
$$
z'_2=(-1.0012516)\cdot1+1.0012516\cdot(-1)+(-0.0012516)\approx-2.0037547,
$$
$$
\hat{y}'\approx[0.982015,\ 0.118809],\qquad
L'\approx\frac12[(0.017985)^2+(0.118809)^2]\approx0.007220.
$$

$L'<L$，说明这一步方向正确（下降量很小，因为 $\eta$ 小且输出已接近目标）。

> ⭐ 这个例子说明：**backprop 的公式不神秘，就是链式法则 + 矩阵转置**。考试若给一个小网络和 target，要求"算一次 forward、一次 backward、一次 update"，按 §9.5 的公式逐步代入即可。

#### 9.9 SGD、mini-batch、epoch、learning rate

**三种梯度下降**：

| 方法 | 每次更新用的样本数 | 梯度 | 优点 | 缺点 |
|---|---|---|---|---|
| **Batch GD**（批量梯度下降） | 全部 $m$ | 精确（全数据平均） | 稳定、方向准 | 每步慢、内存大；大数据集不可行 |
| **SGD**（stochastic gradient descent） | 1 | 单样本，噪声大但无偏 | 更新快、可跳出局部极小/鞍点 | 波动大、收敛不稳定 |
| **Mini-batch GD** | $B$（32/64/128/256…） | batch 平均 | GPU 友好、方差与速度折中 | 需要选 $B$；实践标准 |

**四个容易混的概念**：

| 术语 | 定义 |
|---|---|
| **batch size** $B$ | 一次 forward/backward 用多少样本 |
| **iteration / step** | 一次参数更新（处理一个 batch） |
| **epoch** | 把整个训练集完整遍历一次 |
| **iterations per epoch** | $\lceil m/B\rceil$ |

例：$m=60{,}000$，$B=128$ → 每个 epoch 约 $469$ 次 iteration。

**Learning rate $\eta$**：

| $\eta$ | 现象 |
|---|---|
| 太大 | loss 震荡、爆炸、出现 NaN；可能越过最小值 |
| 太小 | 收敛极慢；容易停在平坦区/局部极小 |
| 合适 | loss 平滑下降，train/val 都改善 |

常见做法（Week 10–11 会展开）：learning rate decay（step decay、exponential decay、cosine annealing）、warmup、SGD + momentum、Adam / RMSProp 等自适应 optimizer。典型初值：$0.1$、$0.01$、$0.001$；实际靠 validation loss 调。

#### 9.10 训练技巧速查

| 现象 | 可能原因 | 对策 |
|---|---|---|
| loss 完全不降 | learning rate 太小；标签/数据 bug；梯度算错 | 调大 $\eta$；检查数据 pipeline；gradient check |
| loss 爆炸 / NaN | $\eta$ 太大；数值溢出 | 调小 $\eta$；gradient clipping；输入归一化 |
| train accuracy 高、val 低 | **overfitting** | 更多数据、data augmentation、weight decay、dropout、early stopping |
| train/val 都低 | **underfitting** | 更大模型、更多 epoch、更好特征、调 $\eta$ |
| 深层网络梯度消失 | sigmoid 导数 $\le0.25$，连乘后趋 0 | ReLU、合理初始化（Xavier/He）、batch norm、residual connection |
| 训练太慢 | batch 太小、没用 GPU、Python 循环 | 增大 batch、GPU、向量化 |

> ⭐ **Gradient check**（调试技巧）：用数值差分
> $$
> \frac{\partial L}{\partial\theta}\approx\frac{L(\theta+\epsilon)-L(\theta-\epsilon)}{2\epsilon}
> $$
> 与 backprop 结果比较；相对误差小于 $10^{-4}$ 左右通常说明实现正确。只在调试时用，训练时不用（太慢）。

#### 9.11 Backprop 的直觉与复杂度

- **直觉**：backprop 是 **reverse-mode automatic differentiation**（反向模式自动微分）在神经网络上的特例。它把网络看成一个计算图，从 loss 出发，沿边反向传播"局部导数 × 上游梯度"。
- **复用**：$\delta^{(l)}$ 只算一次，就被用来算 $W^{(l)}$ 和 $b^{(l)}$ 的梯度，并继续往 $l-1$ 传——动态规划，避免重复计算。
- **复杂度**：一次 forward 约 $O(\sum_l n_l n_{l-1})$；一次 backward 同阶（常数约 2–3 倍）。相比数值差分的 $O(P)$ 次 forward，backprop 是神经网络可训练的根本原因。
- **内存**：backward 需要 forward 时保存的 $a^{(l)}$、$z^{(l)}$；深层大模型因此显存吃紧（activation checkpointing 是常用技巧）。

### 10. 考点速查与自测

#### 10.1 术语速查

| 英文术语 | 中文 | 一句话 |
|---|---|---|
| **forward propagation** | 前向传播 | 输入逐层算到输出 |
| **backpropagation (BP)** | 反向传播 | 用链式法则从 loss 往回算梯度 |
| **chain rule** | 链式法则 | $\frac{\partial L}{\partial w}=\frac{\partial L}{\partial \hat{y}}\frac{\partial \hat{y}}{\partial z}\frac{\partial z}{\partial w}$ |
| **gradient** | 梯度 | loss 对参数的偏导向量 |
| **gradient descent** | 梯度下降 | $W\leftarrow W-\eta\nabla L$ |
| **SGD** | 随机梯度下降 | 用单样本/小 batch 的噪声梯度更新 |
| **learning rate** | 学习率 | 步长 $\eta$ |
| **loss function** | 损失函数 | 衡量预测与目标差距 |
| **weight update** | 权重更新 | 用梯度改 $W,b$ |
| **epoch** | 轮次 | 遍历整个训练集一次 |
| **batch / mini-batch** | 批 | 一次更新用的样本集合 |
| **parameter** | 参数 | $W,b$，由训练学习 |
| **hyperparameter** | 超参数 | 层数、宽度、$\eta$、batch size 等，训练前设定 |
| **hidden layer** | 隐藏层 | 输入与输出之间的层 |
| **inference** | 推断 | 冻结参数，只做 forward |
| **universal approximation** | 万能逼近 | 足够多 neuron 可任意精度逼近函数/区域 |
| **MLP** | 多层感知机 | multi-layer perceptron，即多层全连接网络 |
| **convex decision region** | 凸决策区域 | 2 层网络能表示的单个区域 |

#### 10.2 自测题（Quiz 2 风格）

1. **Forward pass 手算**：给定 $W^{(1)}=\begin{bmatrix}1&-2\\-1&1\end{bmatrix}$、$b^{(1)}=[1,0]^T$、$x=[1,-1]^T$、sigmoid activation，求 $a^{(1)}$。  
   **答案**：$z=[4,-2]^T$，$a\approx[0.982,0.119]^T$。

2. **4+2+1 设计**：为什么第一层 4 个 neuron 的 $W$ 分别是 $[-1,0],[0,-1],[1,0],[0,1]$？为什么第二层 bias 取 $-1.5$、第三层取 $-0.5$？  
   **答案**：前两个切左下矩形的上/右边界，后两个切右上矩形的下/左边界；AND 的 bias 需 $-2<b\le-1$，OR 的 bias 需 $-1<b\le0$，取 $-1.5$、$-0.5$ 方便。

3. **XOR 最小解**：画出 2 层 3-neuron 结构，给出所有 $W,b$。  
   **答案**：hidden #1 $W=[1,1],b=-0.5$；hidden #2 $W=[-1,-1],b=1.5$；output $W=[1,1],b=-1.5$。

4. **为什么单层不行、多层行**？  
   **答案**：单层（无论多少 neuron）的输出仍是输入的线性函数，决策边界是 hyperplane；插入非线性 activation 后，多层复合可以表示非线性/非凸区域。

5. **Universal approximation**：1/2/3 层分别能表示什么区域？定理对 activation 有什么要求？  
   **答案**：1 层 half-plane；2 层单个 convex region；3 层任意区域。Function approximation 的 2 层定理要求 hidden activation nonconstant, bounded, continuous，输出层 linear 且无 bias，hidden neuron 足够多。

6. **Backprop 推导**：写出 2 层网络（MSE + sigmoid）的 $\delta^{(2)}$、$\delta^{(1)}$、$\partial L/\partial W^{(2)}$、$\partial L/\partial W^{(1)}$。  
   **答案**：见 §9.5；$\delta^{(2)}=(\hat{y}-y)\odot\sigma'(z^{(2)})$，$\delta^{(1)}=(W^{(2)})^T\delta^{(2)}\odot\sigma'(z^{(1)})$，$\partial L/\partial W^{(2)}=\delta^{(2)}(a^{(1)})^T$，$\partial L/\partial W^{(1)}=\delta^{(1)}x^T$。

7. **Batch vs SGD vs mini-batch**：各自用什么梯度？epoch 和 iteration 有什么区别？  
   **答案**：batch 用全数据平均；SGD 用单样本；mini-batch 用 $B$ 个样本平均。epoch 是遍历整个训练集一次；iteration 是一次参数更新；每个 epoch 有 $\lceil m/B\rceil$ 次 iteration。

8. **Parameters vs hyperparameters**：$W,b$、层数、learning rate、batch size 分别属于哪类？  
   **答案**：$W,b$ 是 parameters；层数、learning rate、batch size 是 hyperparameters。

### 下一周预告

**Week 10 — Training Deep Networks（正式进入训练）**。本周结束时老师明确说 **"we can continue the next episode. We continue next time."**，结合 Week 1 进度表（Week 10–11 都是 **Training Deep Networks**，Week 11 交 **Homework 2**）：

- **Backpropagation 的正式推导**：老师会从本周的 forward propagation 接着讲，用链式法则算每层梯度；
- **Gradient descent / SGD / mini-batch**：weight update、learning rate、epoch/batch 的实际用法；
- **Loss function**：MSE、cross-entropy 与输出层 activation 的搭配；
- **训练技巧**：初始化、learning rate schedule、optimizer（SGD momentum / Adam）、过拟合与正则化；
- 之后进入 **CNN / deep architectures**（Week 12 左右），以及 **Quiz 2（Week 12，覆盖 Week 8–11）**。

> ⭐ **Quiz 2 范围是 Week 8–11**，本周内容必考：4+2+1 设计与 forward pass 手算、XOR 最小解、single-layer 局限、universal approximation（1/2/3 层区域、定理条件与局限）、parameters vs hyperparameters、training/inference 的区别。§9 的 backprop 推导是 Week 10 的内容，但既然 Quiz 2 覆盖 Week 8–11，建议提前掌握。

---

## Week 11 — Part 2.2（续）：Training Deep Networks 收尾（正则化/优化）＋ CNN 导论

> **本周材料**：`week10-11/week11.txt`（录播转写）、`week10-11/Part 2.2_Training(1).pdf`（Wang Lipo，*Training Deep Networks*，81 页）。⚠️ 课件覆盖 **training** 部分；本周后半段老师已开始讲 **CNN（Convolutional Neural Network）**，这部分**没有对应 PDF**（可能用另一份 slides），本笔记按转写整理并标注。
>
> **本周是 Week 10 "Training Deep Networks" 的接续**：Week 10 讲 forward/backprop/GD/优化器；Week 11 从 **generalization** 开始，讲正则化、dropout、early stopping、batch norm、超参数调优，然后进入 **CNN**。
>
> **权威来源说明**：典型 ASR 错拼：
>
> | 转写 | 正确 |
> |---|---|
> | e pch / approach | **epoch** |
> | arrow / era | **error** |
> | sta | **theta / parameters** |
> | parents / patients | **patience** |
> | patch normalization | **batch normalization** |
> | internal variance shift | **internal covariate shift** |
> | hyper pameter | **hyperparameter** |
> | basion | **Bayesian** |
> | cross variation | **cross-validation** |
> | near network / neur newer | **neural network** |
> | Covent / convolution on | **CNN / convolution** |
> | Lc / Banjo | **LeCun / Bengio** |
> | Alex sNt | **AlexNet** |
> | Hub and Whistle / Cuban whistle | **Hubel & Wiesel** |
> | Mx pulling | **max pooling** |
> | rest net | **ResNet** |
> | dense net | **DenseNet** |
> | dying lu | **dying ReLU** |
> | lure | **lecture** |

### 1. Week 10 内容回顾（本周的前半部分基础）

> Week 10 的笔记未单独成节；为便于理解本周，先压缩回顾 PDF 的前半部分。

| 主题 | 要点 |
|---|---|
| **MLP forward** | $a^{(l)}=\sigma(W^{(l)}a^{(l-1)}+b^{(l)})$；矩阵形式 $y=f(x)=\sigma(W^L\cdots\sigma(W^1x+b^1)\cdots+b^L)$ |
| **Softmax** | $y_i=e^{z_i}/\sum_j e^{z_j}$；输出非负且和为 1；多分类输出层用 softmax（二分类可用 sigmoid） |
| **Activations** | Sigmoid（0–1，会饱和）、Tanh（-1–1，zero-centered，优于 sigmoid）、**ReLU**（$\max(0,x)$，最常用，缓解 vanishing gradient）、Leaky ReLU（解决 dying ReLU）、Linear（回归输出层） |
| **Loss** | Cross-entropy（分类）、MSE（回归） |
| **Gradient descent** | $\theta_{new}=\theta_{old}-\alpha\nabla L(\theta_{old})$；可能停在 local minimum / saddle point / plateau |
| **Backprop** | 链式法则从输出往输入算梯度；一次 forward + 一次 backward 更新一次参数 |
| **Mini-batch / SGD** | Mini-batch GD（32–256）是实际常用；SGD 单样本噪声大；库里的 "SGD" 通常指 mini-batch GD + momentum |
| **Momentum / Adam** | Momentum 用历史梯度平滑；Adam 用一阶矩 + 二阶矩自适应学习率；最常用 Adam / SGD+momentum |
| **Learning rate** | 太小 → 收敛慢；太大 → 震荡/发散；可用 decay / warmup |
| **Vanishing gradient** | 梯度逐层变小；用 ReLU、batch norm 缓解 |

### 2. Generalization：underfitting vs overfitting

#### 2.1 为什么 generalization 重要

> 训练 NN 的目的**不是**在 training data 上拿满分——如果只是"输入问题、输出答案"，那和 **lookup table** 没区别。真正难的是：**给一个没见过的、但相似的输入，模型也能答对**，这就是 **generalization**。

#### 2.2 Underfitting（欠拟合）

两种可能：

1. **模型太简单**：例如需要 100 个 neuron，你只给了 1–2 个，参数不够，training error 降不下去；
2. **训练不够**：模型容量够，但 epoch 太少，还没收敛。

特征：**training error 高，validation error 也高**。

#### 2.3 Overfitting（过拟合）

形成条件（老师强调**两个都要**）：

1. **很多 neuron**（容量大）；
2. **训练很久**（training error 接近 0）。

结果：模型**记住**了 training data（包括 noise），training error 很低，但 validation/test error 高。

| | Training error | Validation error |
|---|---|---|
| **Underfitting** | 高 | 高 |
| **Just right** | 低 | 低 |
| **Overfitting** | 很低（≈0） | 高 |

⭐ 老师用一个 2D 二分类例子：
- 3 个 hidden neurons → 边界较平滑，少量错误，可能是"just right"；
- 6 个 hidden neurons → 边界出现很奇怪的"楔形"凸起，把每个训练点都分对，但**太 sharp、太奇怪**，很可能 overfit。

回归例子（$g(p)=1+\sin(\pi p/4)$）：
- 1-1-1 / 1-2-1：neuron 太少 → underfit；
- 1-3-1：对简单区域够用；
- 1-5-1：对更复杂区域刚好；
- 1-9-1：neuron 太多 → 曲线剧烈上下波动，穿过每个训练点，**overfit**。

⭐ 没有先验公式能直接告诉你"多少个 neuron 正好"；只能**试**（trial and error），用 validation data 判断。

### 3. Regularization（正则化）

#### 3.1 L2 regularization（weight decay）

在 loss 上加一个惩罚大权重的项：

$$\mathcal{L}_{reg}(\theta)=\mathcal{L}(\theta)+\lambda\sum_k\theta_k^2$$

- $\theta$ 包括所有 weights 和 biases；
- $\lambda$ 是 **regularization coefficient / hyperparameter**；
- $\lambda$ 越大 → 惩罚越强 → 权重被压小 → 模型更"regular"、更平滑；
- $\lambda$ 太大 → regularization term 主导，data loss 被忽略 → **underfit**；
- $\lambda$ 太小 → 几乎无正则 → **overfit**；
- 典型值：$0.1,\ 0.01,\ 0.001$（具体问题要试）。

⭐ 直觉：如果某些权重特别大，平方后更大；加进 loss 后，梯度下降会** discourages 大权重**，最终权重更均匀、更小，决策边界更平滑。

#### 3.2 L1 regularization

$$\mathcal{L}_{reg}(\theta)=\mathcal{L}(\theta)+\lambda\sum_k|\theta_k|$$

- 用 L1 norm（绝对值）而不是平方；
- 在 NN 中**不如 L2 常用**，通常表现更差；
- L1 在 0 点不可导；L2 处处可导；
- 可以组合 L1 + L2 → **elastic net**：

$$\mathcal{L}_{reg}=\mathcal{L}+\lambda_1\sum_k|\theta_k|+\lambda_2\sum_k\theta_k^2$$

#### 3.3 PyTorch 实现

```python
# 0.01 L2 regularization
optimizer = torch.optim.SGD(model.parameters(), lr=0.1, weight_decay=0.01)
```

⭐ 正则化通常写在 **optimizer** 的 `weight_decay` 参数里。

### 4. Dropout（随机失活）

#### 4.1 做法

- 训练时，每个 neuron 以固定概率 $p$ **独立**被"丢弃"（连同它的 weights/biases）；
- 常用 $p=20\%$–$50\%$（具体要调）；
- 被丢弃的 neuron 不参与 forward/backward；每次 mini-batch 都重新随机丢弃。

```
原网络： 16 neurons
dropout 后：约 9 neurons 保留（丢掉约 7 个）
```

#### 4.2 为什么有效

- 减少参数量 → 网络变简单 → 降低 overfitting；
- 可以看作 **ensemble learning**：每个 mini-batch 训练一个**不同的子网络**（不同架构），最后相当于很多子网络"投票"/平均。
- 老师用"committee machine"类比：让很多个模型投票，通常比单个模型更稳。

#### 4.3 ⭐ 测试时必须关闭 dropout

```python
network = torch.nn.Sequential(
    torch.nn.Linear(2, 2),
    torch.nn.Dropout(p=0.5),
)
network(torch.tensor([0, 1], dtype=torch.float))  # 训练模式：输出随机
network.eval()                                      # 评估模式：关闭 dropout
```

- `model.train()`：启用 dropout / batch norm 的训练行为；
- `model.eval()`：关闭 dropout，使用全部 neuron；
- 若评估时忘记 `.eval()`，同一输入会得到不同输出。

### 5. Early Stopping（早停）

- 从 training data 中分出一部分作为 **validation set**（常见 75/25，或 90/10；比例是经验值）；
- 每个 epoch 后用 validation set 评估（**不参与 backprop**）；
- 当 validation accuracy/loss **连续 $n$ 个 epoch 没有改善**时停止训练；$n$ 叫 **patience**；
- 为什么：training error 可以一直降到 0，但 validation error 会在某点**plateau 或开始上升**——再训练就是 overfit；
- 为什么要 patience：validation 曲线会波动，第一次上升可能是假信号；等几个 epoch 确认。

⭐ Validation data 的定位：训练过程中使用（决定何时停、选超参数），但**不参与梯度更新**；test data 完全留到最后。

### 6. Batch Normalization（批归一化）

#### 6.1 做法

对每一层的 mini-batch 激活做标准化：

$$\hat{x}=\frac{x-\mu}{\sigma}$$

其中 $\mu,\sigma$ 是该 batch 的均值和标准差；输出零均值、单位方差。

#### 6.2 作用

- 类似 input data preprocessing，但**每一层都做**；
- 减轻对参数初始化的敏感度；
- 减少 **internal covariate shift**（训练中激活分布随参数更新而变化）；
- 允许使用**更大的 learning rate**而不发散；
- 训练更快、更稳定；
- 在 CNN 中非常常用。

#### 6.3 PyTorch

```python
network = torch.nn.Sequential(
    torch.nn.Linear(2, 2),
    torch.nn.BatchNorm1d(2),
    torch.nn.Linear(2, 2),
)
```

### 7. Hyperparameter Tuning（超参数调优）

#### 7.1 哪些是 hyperparameters

| Hyperparameter | 典型范围/说明 |
|---|---|
| Number of layers | 3、5、10、100… |
| Number of neurons per layer | 每层宽度 |
| Initial learning rate | 0.1、0.01、0.001… |
| Learning rate decay schedule | step / exponential / cosine / warmup |
| Optimizer type | SGD、SGD+momentum、Adam、RMSprop… |
| Regularization parameters | L2 $\lambda$、dropout rate |
| Batch size | 32–256 |
| Activation function | ReLU、Leaky ReLU、tanh… |
| Loss function | cross-entropy、MSE… |

⭐ **Parameter vs Hyperparameter**：
- **Parameters**：$W,b$，由训练（backprop）学习；
- **Hyperparameters**：层数、宽度、学习率、batch size、$\lambda$、dropout rate…，**训练前设定**，不能由梯度下降直接学。

#### 7.2 搜索方法

| 方法 | 做法 | 优缺点 |
|---|---|---|
| **Grid search** | 在每个超参数的候选值上做笛卡尔积，逐个试 | 最可靠，但组合爆炸、非常耗时 |
| **Random search** | 随机采样超参数组合 | 通常更高效，实践中常优先 |
| **Bayesian optimization** | 用代理模型指导下一步采样 | 活跃研究方向 |

#### 7.3 用 K-fold CV 调超参数

当数据量小（如医学图像只有几十/几百张）时常用：

1. 先划出 **test set**（不碰）；
2. 把剩余 training data 分成 $K$ 个 fold（如 5）；
3. 每次用 1 个 fold 作 **validation**，其余 $K-1$ 个作 training；
4. 重复 $K$ 次，平均 validation performance；
5. 选最好的 hyperparameters；
6. 最后在 test set 上评估一次。

⭐ 老师举例：与生物学家/化学家合作时，显微镜非常昂贵，数据只有 50–100 张，这种场景下 K-fold 特别重要。

### 8. Deep vs Shallow Networks

- **Deep network** 通常比 **shallow network** 表现更好（同样数量的 neuron，分层放置往往比全放一层好）；
- 但深度有上限：超过一定层数后 performance **plateaus**；
- "deep" 最初指 >4 层；后来 **CNN** 才真正让 deep learning 成功；
- 例子：4 个 neuron 全放一个 hidden layer vs 2+2 两层；后者通常更好。

### 9. CNN（Convolutional Neural Network）导论

> ⚠️ 以下内容来自 Week 11 转写后半段；对应 slides 未包含在 `Part 2.2_Training(1).pdf` 中。

#### 9.1 为什么 MLP 不适合图像

**Translation（平移）问题**：

- 同一个 object 在图像中向左/向右平移，语义上**还是同一个 object**；
- 但 MLP 把图像 flatten 成一维向量，平移后向量每个位置都变了 → MLP 看到的是**完全不同的输入**；
- 所以 MLP **不具备 translation invariance**；同一个 object 在左边响应强、移到右边响应弱。

⭐ 这是 CNN 出现的核心动机之一。

#### 9.2 生物学灵感：Hubel & Wiesel（1950s–60s）

- 用猫做实验，发现视觉皮层中有**对特定方向敏感**的细胞（vertical / horizontal / oblique）；
- 皮层有 **topographic mapping**：相邻细胞对应视野相邻区域；
- **Hierarchical organization**：
  - **Simple cells**：对光的方向敏感；
  - **Complex cells**：对方向和运动敏感；
  - **Hypercomplex cells**：对运动 + 端点敏感；
- 这项工作是视觉神经科学的基础，获诺贝尔奖。

#### 9.3 从 Neocognitron 到 AlexNet

| 阶段 | 工作 | 要点 |
|---|---|---|
| 1980s | **Neocognitron**（Fukushima） | 模仿 simple/complex cells 的层级结构；但 filter **handcrafted** |
| 1989–1998 | **LeCun / Bengio** | 把 **backprop** 用到 CNN；手写数字/邮编识别（LeNet） |
| 2012 | **AlexNet**（Krizhevsky, Sutskever, Hinton） | 1M images；GPU；deep CNN 的起点 |

⭐ 关键转变：早期 filter 是**手工设计**的；后来用 **backprop + 大量数据**让 filter **自己学**。

#### 9.4 Convolution（卷积）的定义

**1D continuous**：

$$(f*g)(t)=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\,d\tau$$

- $g$ 是 **kernel / filter**；先**翻转**（$g(-\tau)$），再滑动、相乘、积分。

**Discrete**：

$$(f*g)[n]=\sum_k f[k]g[n-k]$$

**2D**：filter 在 image 上滑动，element-wise 相乘再求和。

⭐ ⭐ **深度学习中的"convolution"其实是 cross-correlation**：
- 数学定义要 flip kernel；深度学习框架（PyTorch/TensorFlow）**不 flip**；
- 因为 filter 是**学出来的**：flip 与不 flip 只是学到一套"翻转的"filter，网络表达能力相同；
- 所以实践中不用纠结，统一叫 convolution。

#### 9.5 Convolution 作为 feature extractor

- 一个 3×3 filter 在图像上滑动，得到一个 **response map**；
- 当 filter 与图像局部 pattern **相似**时，response 大；
- 例：edge detection filter（如 $\begin{bmatrix}1&1&1\\1&1&1\\-4&0&0\end{bmatrix}$ 之类）会在边缘处产生大响应，在平坦区域响应为 0；
- 不同 filter 提取不同 feature（垂直边、水平边、对角边…）。

#### 9.6 关键概念

| 概念 | 含义 |
|---|---|
| **Local receptive field** | 每个 neuron 只连接上一层的一个局部区域（如 2×2/3×3），不是全连接 |
| **Parameter sharing** | 同一个 filter 在整张图上共享权重 → 参数量大大减少 |
| **Feature map depth** | 该层 filter 的数量 = 输出 feature map 的通道数 |
| **Stride** | filter 每次滑动的步长 |
| **Padding** | 边界补零，控制输出尺寸 |

#### 9.7 Pooling（池化）

| 类型 | 做法 |
|---|---|
| **Max pooling** | 在窗口内取最大值 |
| **Average pooling** | 在窗口内取平均值 |

- 窗口大小如 2×2，stride 2；
- 作用：**降低 spatial size**、减少参数、防止 overfitting；
- 与 convolution 一样，都会让 feature map 变小；
- Max vs average 差别通常不大。

#### 9.8 典型 CNN 架构

```
input image
  → [conv → ReLU] × 2 → max pool
  → [conv → ReLU] × 2 → max pool
  → [conv → ReLU] × 3 → max pool
  → flatten → fully connected (MLP) → softmax
```

⭐ 重要观察：
- **CNN 的"深度"主要来自 convolution 层**；
- **分类仍然由最后的 fully connected MLP 完成**；
- convolution 层参数很少（parameter sharing），参数大多集中在最后的 FC 层；
- convolution 做 **feature extraction**，pooling 做 **simplification**，FC 做 **classification**。

#### 9.9 ResNet 与 DenseNet

- **ResNet**：引入 **identity skip connection**：$x_{l+1}=x_l+\mathcal{F}(x_l)$；
  - 缓解 **vanishing gradient**；
  - 可以训练 **1000+ 层**；
  - 是很多 SOTA 模型的 backbone。
- **DenseNet**：每层与前面所有层连接（dense connection），进一步复用 feature。
- 这些 backbone 常作为研究/工程的 baseline。

#### 9.10 CNN 的应用

- Object detection、segmentation；
- Self-driving；
- Medical image recognition；
- Astronomy / scientific imaging；
- Image captioning（早期结果还很粗糙）；
- Style transfer。

### 10. ⭐ Quiz 2 与作业信息

- 老师在本周最后明确说：**"next time we're going to do a little quiz... at 9:00, we do a big quiz."**
- **Week 12 课上（19:30–21:30）**，约 **21:00** 开始 Quiz 2；
- 老师已发 **practice quiz**：题量、难度与真题相似；
- 按课程安排（Week 1 公布）：**Quiz 2 覆盖 Week 8–11**，10%，可带 **一张 A4 reference sheet**，线上题但需到 lecture theater 用自带 laptop 经 NTULearn 完成；
- **Homework 2**：Week 10 转写提到 due date 推迟到 **Week 12 末**；本周未重复，按 NTULearn 为准。

### 11. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| **Generalization** | 训练目标不是 memorization，而是 unseen data 表现 |
| **Underfitting** | 模型太简单 / 训练不够；train & validation error 都高 |
| **Overfitting** | 很多 neuron + 训练很久；train error≈0，validation error 高 |
| **Neuron 数量** | 没有公式；trial + validation；越多 capacity 越大 |
| **L2 regularization** | $\mathcal{L}+\lambda\sum\theta^2$；`weight_decay`；λ 太大会 underfit |
| **L1 regularization** | $\mathcal{L}+\lambda\sum|\theta|$；NN 中不如 L2 常用；0 点不可导 |
| **Elastic net** | L1 + L2 |
| **Dropout** | 训练时按概率 $p$ 丢弃 neuron；20–50%；测试时 `.eval()` 关闭 |
| **Dropout = ensemble** | 每个 mini-batch 训练不同子网络；投票/平均 |
| **Early stopping** | 用 validation set；patience $n$；validation 不再改善就停 |
| **Batch normalization** | 每层 $\hat x=(x-\mu)/\sigma$；减少 internal covariate shift；允许更大 LR |
| **Hyperparameters** | 层数、宽度、LR、decay、optimizer、λ、dropout、batch size、activation、loss |
| **Grid vs random search** | grid 可靠但组合爆炸；random 更高效；Bayesian 是研究方向 |
| **K-fold for tuning** | 小数据常用；train 分 K 折，轮流 validation，平均；最后 test 一次 |
| **Deep vs shallow** | 深通常更好，但有上限；CNN 让 deep learning 成功 |
| **MLP 为什么不适合图像** | translation：平移后输入向量完全不同；无 translation invariance |
| **Hubel & Wiesel** | simple/complex/hypercomplex cells；orientation；topographic map |
| **Neocognitron/LeNet/AlexNet** | handcrafted → backprop → 1M images/GPU |
| **Convolution** | 数学上 flip kernel；深度学习不 flip = cross-correlation；filter 学出来，无影响 |
| **CNN 关键概念** | local receptive field、parameter sharing、feature map depth、stride、padding |
| **Pooling** | max / average；降尺寸、减参数、防过拟合 |
| **CNN 架构** | conv+ReLU → pool → … → FC → softmax；conv 提特征，FC 分类 |
| **ResNet** | identity skip connection；缓解 vanishing gradient；1000+ 层 |
| **Quiz 2** | Week 12 课上一小时；21:00 开始；覆盖 Week 8–11；A4 reference sheet |

### 12. 本周要点小结

- **Generalization**：训练不是背训练集；要避免 underfit 和 overfit。Overfit 需要"大容量 + 长时间训练"两个条件。
- **正则化**：L2（weight decay）最常用，L1 可稀疏化但 NN 中较少用；λ 是超参数，太大会 underfit。
- **Dropout**：随机丢 neuron，等价于训练很多子网络并 ensemble；评估时务必 `.eval()`。
- **Early stopping**：用 validation set + patience；在 validation 开始变差前停下。
- **Batch normalization**：每层标准化，稳定训练、允许更大 LR、缓解 vanishing/exploding gradient。
- **超参数调优**：grid search 可靠但昂贵；random search 更实用；小数据用 K-fold。
- **CNN 的动机**：MLP 不具备 translation invariance；CNN 用 local receptive field + parameter sharing 解决。
- **Convolution**：filter 滑动 + 内积；深度学习实际是 cross-correlation；filter 由 backprop 学习。
- **Pooling / 架构**：conv 提特征，pool 降维，FC 分类；ResNet 用 skip connection 训练很深。
- **Quiz 2**：Week 12 课上一小时，21:00 开始，覆盖 Week 8–11；练习 quiz 已发，务必先做。

### 13. 下一周预告

- **Week 12**：继续 **CNN**（卷积层细节、pooling、经典架构），并在课上进行 **Quiz 2**（21:00 左右）。
- **Quiz 2 范围 Week 8–11**：神经网络导论、MLP/forward/backprop、训练技巧（正则化/dropout/batch norm/超参数）、CNN 基础。
- **Homework 2**：Week 12 末截止（以 NTULearn 为准）；内容是用神经网络逼近函数，注意 underfit / overfit / just-right 的对比。
- 之后 Week 13 进入 **CNN 的后续内容 / 课程收尾**，并准备 Final Exam（可带一张 A4 reference sheet）。
