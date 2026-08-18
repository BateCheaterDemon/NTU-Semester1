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

> **下一周预告**：Week 2 将进入 **Bayesian Inference**（贝叶斯推断，含 MLE / MAP 估计）。
