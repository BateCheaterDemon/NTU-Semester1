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
