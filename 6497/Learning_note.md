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
