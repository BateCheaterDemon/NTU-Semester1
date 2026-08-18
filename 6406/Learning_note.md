# EE6406 — Analytic and Ensemble Machine Learning（解析式与集成机器学习）

> 课程学习笔记总览。每周一节，按周总结重点内容。
> 第一周（开课周）特别关注考核要求、任课教师、课程定位与整体结构。
>
> **权威来源说明**：本笔记先由 `week1.txt` 录播转写整理，再以 `EE6406-Lecture1-LZP-v1.pdf`（官方讲义，Zhiping Lin，AY2026-27 S1）核对修正。转写有大量语音识别噪声（如 "Dinger Ping" 实为 Zhiping Lin、"proto/Tok" 实为 Toh Kar-Ann、"Simon Le/Dell" 实为 Simon Liu、"seemal/on sample" 实为 ensemble、"sample learning" 实为 ensemble learning、"pyro" 等概率词本周较少），均以 PDF 为准修正。Week 1 转写仅覆盖 Lecture 1（课程导论），Lecture 2（Data Preprocessing）与 Lecture 2 Supplement（Mathematics Review）虽已下发但属下周内容，本周不展开。

---

## Week 1 — 开课周：课程导论 + 机器学习概览 + Analytic/Ensemble 两大范式引入

### 1. 课程基本信息

- **课程名称**：EE6406 **Analytic and Ensemble Machine Learning**（解析式与集成机器学习）。
- **课程定位**：本学期起成为 **SPM（Signal Processing/相关方向）August 2026 新生的 SE（Specialized Elective / 必修性选修）课程**；对其他 program 仍是 GE（General Elective）。SPM 老生（去年/今年 1 月入学）选本课仍算 GE。但**考核、考试、注册流程无差异**，SPM 学生直接确认入班，其他 program 学生需等空位（当前近 400 人选课）。
- **课程协调人**：**Zhiping Lin**（ezplin@ntu.edu.sg），full-time，SPM program director，1999 年加入 NTU。本周与下周由他主讲，同时负责 CA/exam 协调。

#### 教学团队（3 位教授，分两段教学）

| 教授 | 身份 | 授课周 | 负责内容 |
|---|---|---|---|
| **Zhiping Lin** | full-time，course coordinator，program director of SPML | Week 1–2（2 周） | Lecture 1 Introduction + Lecture 2 Data Preprocessing（含数学复习补充），兼管 CA/exam |
| **Kar-Ann Toh**（Toh，转写误为 "proto/Tok"） | part-time，新加坡籍，延世大学（Yonsei, 韩国）任教 20 年，2025 年 3 月退休为 emeritus professor，NTU 1999 PhD校友，machine learning & pattern recognition，多本顶刊 AE | Week 3–8（6 周） | **Analytic Learning 主体**（Lecture 3–8），课程主讲部分、教材主作者 |
| **Simon Liu**（转写误为 "Simon Le/Dell"） | part-time，Trust Decision 首席 DA & AI 官，前 Lazada SVP；多伦多大学 PhD（上过 Hinton 的课）；也教 EE6405 NLP | Week 9–13（5 周） | **Ensemble Learning**（Lecture 9–13），含行业应用 |

> 教学周分配为 **2 + 6 + 5**。Analytic 部分占比大（Part 1 共 8 周），Ensemble 部分 5 周（Part 2）。

### 2. ⭐ 考核要求（重要）

| 成分 | 占比 | 说明 |
|---|---|---|
| **Final Exam 期末** | **60%** | 共 4 题：**2.5 题来自 Part 1（Week 1–8），1.5 题来自 Part 2（Week 9–13）**，按内容比例分配 |
| **CA（仅 quiz）** | **40%** | 见下方明细，三次 online quiz |

| Quiz | 覆盖 | 占比 | 时间 | 形式 |
|---|---|---|---|---|
| **CA1** | Part I 前半 | **10%** | **Week 5** | online quiz，**in class（必须到课）**，**closed-book**，需 lockdown browser |
| **CA2** | Part I（至 Week 7） | **15%** | **Week 8**（recess 后，有较多准备时间） | 同上 |
| **CA3** | Part II | **15%** | **Week 12**（由 Simon Liu 安排） | 同上 |

#### ⭐ Quiz 关键规则（务必注意）

- **online quiz 但必须在课堂内完成**——不能在家或海外做。
- 需使用 **lockdown browser**：启动后会切断其他软件，只能访问 NTULearn。需提前安装。
- **closed-book 闭卷**。
- 设备建议：**PC + Windows 最稳定**；Mac/unix 可能有问题；**iPad 可用但不稳定**。可在同一台 PC 上既装 lockdown browser 又用 Windows。Week 4 可能安排一次 try-run 测试设备是否可用。
- 三次 quiz 中 CA1+CA2 覆盖 Part 1（Week 1–8），CA2 只考到 Week 7（recess 前内容），recess 后再考；CA3 覆盖 Part 2。
- 过去两年此安排运行良好，多数学生无问题。

### 3. 教材与参考书

- **主教材** [1]：**Toh, Zhuang, Liu, Lin**, *Analytic Learning Methods for Pattern Recognition*, **Springer, 2025**（NTU 图书馆可免费下载电子版）。四位作者中三位是本课教学成员；涵盖大部分章节、习题与解答。课程无需额外索取练习题——书中习题充足。书名虽聚焦 pattern recognition，但技术可用于更一般任务。
- 参考：
  - [2] Kuncheva, *Combining Pattern Classifiers: Methods and Algorithms*, 2nd ed, Wiley, 2014.（集成学习经典）
  - [3] Hastie, Tibshirani, Friedman, *The Elements of Statistical Learning*, 2nd ed, Springer, 2017.
  - [4] Tom M. Mitchell, *Machine Learning*, 1997.（机器学习经典定义来源）
  - [5] Chen & Guestrin, *XGBoost*, KDD 2016.
  - [6] Ke et al., *LightGBM*, NIPS 2017.

### 4. 课程内容总览（13 讲，权威，取自 PDF Contents）

| Lecture | 内容 | 主讲 | Week |
|---|---|---|---|
| L1 | Introduction | Lin | 1 |
| L2 | Data Preprocessing（含数学复习补充） | Lin | 2 |
| L3 | Linear Parametric Models | Toh | 3 |
| L4 | Learning Score Functions | Toh | 4 |
| L5 | Over- and Under-determined Analytic Regression | Toh | 5 |
| L6 | Advanced Analytic Classification | Toh | 6 |
| L7 | Analytic Methods for Penalized Learning | Toh | 7 |
| L8 | Performance Evaluation and Statistical Inference | Toh | 8 |
| L9 | Introduction to Ensemble Learning, Bagging and Boosting | Liu | 9 |
| L10 | Classical Ensemble Algorithms – Random Forest, Adaboost, Gradient Boosting | Liu | 10 |
| L11 | Advanced Boosting Algorithms – XGBoost and LightGBM | Liu | 11 |
| L12 | Reinforcement Learning with Ensemble Methods | Liu | 12 |
| L13 | Industrial Applications – End-to-end Ensemble Models | Liu | 13 |

> **两大范式**：
> - **Part 1（L1–L8，8 周）**：**Analytic Learning**——用 closed-form 数学解直接求模型参数，无需迭代优化。L1–L2 为共用基础（导论+数据预处理+数学复习），L3–L8 为核心方法（线性参数模型→score function→回归→分类→penalized learning→性能评估）。L8 性能评估同时服务 Part 1 与 Part 2。
> - **Part 2（L9–L13，5 周）**：**Ensemble Learning**——多 learner 组合提升性能。从 bagging/boosting → 经典算法（Random Forest/Adaboost/Gradient Boosting）→ 进阶（XGBoost/LightGBM）→ 强化学习+集成 → 工业应用。

### 5. 机器学习基本概念（Lecture 1 知识内容）

#### 5.1 定义（Mitchell 1997）

- 机器学习是让计算机从 data 和 experience 中学习，而非为每个任务显式编程。
- **Tom Mitchell (1997) 定义**：A computer program is said to learn from experience **E** with respect to some task **T** and performance measure **P**, if its performance at tasks T, as measured by P, improves with experience E.
- **三要素**：
  - **Experience (E)**：training data 或 interactions。
  - **Task (T)**：classification、regression、clustering 等。
  - **Performance (P)**：accuracy、error rate、F1-score、reward 等。
- 学习目标：给定 data → 定义 learning model/algorithm → 用 performance measure 衡量 → 实现 task，且随经验提升 performance。

#### 5.2 简单示例：Spam Email Classification（垃圾邮件分类）

- 任务：自动判别 incoming email 为 **Spam**（垃圾）或 **Non-spam / Ham**（有用，ham 非 harmful）。
- Pipeline：收集标注邮件 → 特征提取（feature extraction，传统法；深度学习可 end-to-end）→ 训练模型 → 对新邮件分类 → 评估。
- 关键观察：计算机从 examples 学习；**数据质量越高，分类/预测性能越好**；同一框架适用众多应用。
- 真实例：NTU 邮箱有 spam 过滤但精度有限——垃圾邮件会漏进收件箱、好邮件会误入 spam 桶，说明算法优劣差异明显。**核心思想：从数据学习，给更多例子则改进**。

#### 5.3 机器学习类型

| 类型 | 数据 | 说明 |
|---|---|---|
| **Supervised Learning 监督学习** | 有 label `(x_i, y_i)` | 最常用、最基础；本课主要聚焦 |
| **Unsupervised Learning 无监督学习** | 无 label，仅数据 | 如 clustering 聚类 |
| **Semi-supervised Learning 半监督** | 少量 label + 大量无 label | 介于两者之间 |
| **Reinforcement Learning 强化学习** | 与环境交互、奖励/惩罚 | 动态、adaptive；用于机器人/控制；非直接用训练数据，而是 action+reward 反馈 |

> 强化学习在 SPML 7 月 special term 有专门课程（由 Lin 的已毕业 PhD 生、现华南理工大学副教授讲授 **continual analytic learning**）；EEE 全院目前无整门强化学习课，故本课 Part 2 用一讲结合集成学习简介。

#### 5.4 机器学习的演进（按"数据"视角分阶段）

1. **Rule-based AI（早期）**：专家系统（expert system），基于规则与事实。现少用。
2. **Statistical/Probabilistic Modeling（统计/概率建模）**：用概率、PDF 等建模数据，找 pattern 做学习/分类——即 pattern recognition。
3. **Data-Driven Machine Learning**：更直接从数据学习、强调泛化与算法优化。
4. **Deep Learning（representation learning，~10+ 年前）**：神经网络等学表示，大数据、end-to-end 黑箱。
5. **Foundation Models（当前）**：transformer block、LLM、多模态 AI，海量多模态数据，强泛化。

### 6. AI/ML 重大突破案例（老师用以展示 ML 能力与局限）

| 案例 | 时间 | 要点 |
|---|---|---|
| **AlphaGo**（Google DeepMind） | 2016.03 | 4:1 击败李世石（围棋世界冠军）；围棋复杂度远超国际象棋，此前 IBM Deep Blue 1997 击败国际象棋冠军但被认为非突破性；AlphaGo 用 deep learning + reinforcement learning，自学百万局、"直觉"评估，非暴力计算。2026.07 世界第一申真谞与开源 Go AI KataGo 三番棋（受让两子 handicap），人类赢两局——AI 非万能。 |
| **AlphaFold**（DeepMind） | 2020 CASP14 | 从氨基酸序列（1D）预测蛋白质 3D 结构，精度达原子宽度量级，CASP 组织者宣布蛋白质折叠问题"已被解决"；此后竞赛停办（AI 永远胜出）。数据库从百万级增至 2 亿+结构。2024 Nobel Chemistry 部分授予相关工作；同年 Nobel Physics 授予 Hinton（deep learning 奠基）。 |
| **Tesla FSD（Full Self-Driving）** | 持续 | end-to-end AI：原始图像直接输出转向/制动/加速；纯视觉（camera only，不用 radar/LiD），仿人眼驾驶；fleet learning 持续改进。 |
| **ChatGPT** | 2022.11.30 公开 | 转折点：AI 从专用、需技术门槛、碎片化 → 对话式、通用、adaptive；语言成为人-AI 主接口；LLM 兴起。 |

> 老师观点：AI 在硬件/机器人（如机器人足球团队协作）距人仍远，并非所有领域 AI 都能短期超越人类。

#### 什么让这些突破成为可能（5 大因素）

1. **Massive Data**：大规模多样数据让模型泛化而非死记；self-play/simulation（AlphaGo）、fleet data（Tesla）可放大有效数据量；数据规模常与性能正相关。
2. **Hardware**：CPU → GPU（大规模并行）→ TPU/AI 加速器（优化深度学习矩阵运算）；训练从月级降到天/小时级；能效使大规模 AI 经济可行。
3. **Software / Open Source**：TensorFlow、PyTorch、CUDA 等框架与库降低门槛；开放数据集/benchmark/预训练模型加速；产学反馈循环；将 AI 从孤立研究变为全球运动（但也加剧行业竞争，大学难与大公司抗衡）。
4. **Algorithms**：深度神经网络、transformer、强化学习、self-supervised learning、diffusion model 等架构创新；end-to-end 学习取代脆弱的规则系统；算法将数据与算力转化为智能。
5. **Feedback Loops & Continuous Learning**：模型从自身输出（self-play、simulation）学习；真实使用反馈持续再训练；性能随时间复合提升而非停滞；AI 动态而非静态演进。

### 7. ⭐ 本课核心：Analytic Learning（解析式学习）— Part 1 主线

#### 7.1 为什么需要 Analytic Learning（动机）

现代主流 ML 依赖 **iterative optimization（迭代优化）**：Gradient Descent (GD)、SGD、Adam 等。问题：
- 训练常需数百上千次迭代才收敛。
- 性能依赖众多 hyperparameter：learning rate、initialization、batch size、optimizer 选择。
- 收敛不保证。
- 大规模问题需大量计算资源。

→ **核心问题：能否不经迭代优化、直接求得模型？**

#### 7.2 Analytic Learning 是什么

- 词源：希腊语 *analytikos*——"把整体分解为组成部分并分析"的能力。分析（analysis）vs 综合（synthesis）。
- **思路**：用 **prior knowledge 作基底**，通过分析概念的结构与组成部分，理性描述概念、生成假设、做推广。允许学习者把信息分解为组件、用 critical & logical thinking 生成假设。
- **关键**：用 **closed-form mathematical solution（闭式数学解）** 直接计算模型参数，**无需迭代优化**。解通过线性代数与优化理论求得。
- 学习变成"**直接求解一个数学问题**"，而非"反复试错优化"。

#### 7.3 Analytic Learning 的好处与局限

| 好处 | 局限 |
|---|---|
| Fast training（快速训练） | 仅在合适模型假设下适用 |
| Deterministic solution（确定性解） | 对高度非线性问题不够灵活（可用 kernel 方法映射） |
| Few hyperparameters（少超参） | 某些方法需 matrix inversion（矩阵求逆），矩阵大时计算量大 |
| Good interpretability（可解释性好） | Scalability 仍是活跃研究课题 |
| Computational efficiency（中小规模计算高效） | — |
| Improved reproducibility（可复现性好） | — |
| 适合 small/medium-scale real-time 应用、edge device | 大规模问题不如迭代优化 |

> **定位**：Analytic learning 是**补充（complement）而非替代**迭代学习——是可选的替代方案，按问题选用。

#### 7.4 Closed-form Learning 所需数学工具

- Linear algebra（线性代数）
- Matrix decomposition（矩阵分解）
- Least-squares estimation（最小二乘估计）
- Regularization（正则化）
- Convex optimization（凸优化）

> 这些数学工具下周（Lecture 2 + Supplement）复习。

#### 7.5 代表性 Analytic Learning 算法（对应周次）

| 方法 | 对应 Lecture/Week |
|---|---|
| Linear regression、Ridge regression | L3 (Week 3) 起线性参数模型 |
| Kernel ridge regression | 后续 kernel 方法 |
| **Recursive classification TER learning**（Total Error Rate learning，Toh 教授发明，本课独有） | L6 Advanced Analytic Classification |
| Analytic regression & classification（penalized） | L5–L7 |

> 教学路径：L3 linear parametric models（least squares）→ L4 learning score functions → L5 over/under-determined analytic regression → L6 advanced analytic classification → L7 penalized learning → L8 performance evaluation & statistical inference。

#### 7.6 应用示例：Face Recognition（人脸识别）

- CMU face dataset：640 张人脸图像，20 个 subject，每人 32 张（不同 pose/expression/是否戴眼镜）。每张全分辨率 120×128 pixels，256 gray levels。CC BY 4.0 许可。
- 用 analytic learning：提取面部特征（landmark/corner points 等）→ closed-form 解做身份识别。**高效闭式学习实现快速准确人脸识别**。
- 应用：海关、银行系统、NTU 门禁（老师口罩也能识别，特征主要在眼上半脸）。

#### 7.7 Analytic Learning 近年发展

- Closed-form deep architectures（闭式深度架构）
- **Continual analytic learning（持续解析学习）**——Lin 的已毕业 PhD 生（现华南理工副教授）主攻方向，已发表 ~30 篇会议/期刊论文；有学生学后数月即在 *Neural Networks*（顶刊）发表论文。
- Distributed and edge AI、Large-scale analytic optimization
- Explainable analytic models
- **Hybrid analytic–iterative learning**（解析+迭代混合，Toh 擅长：base 模型 + analytic 模块叠加效果更好）

### 8. ⭐ 本课另一核心：Ensemble Learning（集成学习）— Part 2 主线

#### 8.1 动机

- **核心问题：多个 learner 能否胜过单个 learner？**
- 现实：没有单一算法在所有数据集上都最优——发论文比方法时"七成数据集更好"已足够，审稿人会质疑"永远最优"的声称。
- 思路：组合多个学习模型，追求 **higher accuracy + better robustness + improved generalization**。
- 类比中文"三个臭皮匠顶个诸葛亮"/集思广益——但需**建设性组合**，不能互相抵消。

#### 8.2 定义

- **Ensemble learning**：训练多个 learner → 组合其预测 → 产生最终决策；整体称 ensemble。
- **关键观察：整体可优于部分之和（the whole can be better than the individual parts）**。

#### 8.3 为什么有效（三要素）

1. **Accurate learners（准确的 learner）**：各 learner 本身要合理可用。
2. **Diverse learners（多样的 learner）**：各 learner 需彼此不同（diversity）；若只是微调参数给出相同结果则无意义。类似团队需要多样性。
3. **Effective combination strategy（有效组合策略）**：合理组合方式。

> **成功的 ensemble learning 同时需要 accuracy 与 diversity。**

#### 8.4 基本组合策略

- **Voting（投票）**：如 majority voting——3 个 classifier（decision tree、SVM、neural network）投票，2:1 多数决。类比选举。
- **Averaging（平均）**：对数值输出取平均，有效且简单。
- **Weighted combination（加权组合）**：给更强的 learner 更高权重，弱者低权重。

#### 8.5 两大主要策略：Bagging vs Boosting

| | **Bagging** | **Boosting** |
|---|---|---|
| 训练方式 | **parallel**（并行训练各 learner） | **sequential**（串行：learner 1 结果传给 learner 2 改进…） |
| learner 关系 | 独立 | **dependent**（后者依赖前者输出） |
| 主要目的 | **reduce variance**（降低方差）→ 更稳定、抗噪/抗过拟合 | **reduce bias**（降低偏差）→ 预测更接近真值 |
| 特点 | less sensitive to noise & overfitting | higher predictive accuracy |

> 两者都是 ensemble 但目标不同，无绝对优劣，按需求选。

#### 8.6 代表性 Ensemble 方法（对应周次）

| 方法 | 对应 Lecture |
|---|---|
| Bagging、Boosting | L9 (Week 9) |
| **Random Forest、Adaboost、Gradient Boosting** | L10 (Week 10) 经典 |
| **XGBoost、LightGBM** | L11 (Week 11) 进阶 boosting，工业常用 |
| Reinforcement Learning with Ensemble | L12 (Week 12) |
| Industrial Applications（端到端集成模型，含 Simon Liu 公司 Trust Decision 风险预测相关） | L13 (Week 13) |

#### 8.7 Ensemble Learning 好处与局限

| 好处 | 局限 |
|---|---|
| Higher prediction accuracy | Higher computational cost（相对单 learner） |
| Improved robustness | Reduced interpretability（相对单个） |
| Reduced overfitting | More complex model management |
| Better handling of complex problems | Diminishing returns（收益递减） |
| Flexibility（可选不同 learner/数量） | **Dependent on diversity**（缺多样性则失效） |

> **Ensemble learning 用更高计算复杂度、更低可解释性，换取更高预测性能与鲁棒性。** 金融业仍偏好 ensemble（如 XGBoost/LightGBM）而非深度学习/LLM，正因其可解释性相对更好。

#### 8.8 应用示例：Credit Assessment（信用评估）

- 输入申请人数据 → 多个 base learner（如 decision tree）判定 high/low risk → ensemble 组合（bagging/boosting/进阶法）→ aggregate 预测 → 低风险批准、高风险复审或拒绝。组合多 learner 提升预测可靠性与鲁棒性。

#### 8.9 两大范式按应用场景选择

| 应用 | 推荐范式 | 原因 |
|---|---|---|
| 人脸识别 | Analytic | — |
| 医学诊断（需可解释） | Ensemble | 医生需解释 |
| 金融风险评估 | Ensemble（XGBoost/LightGBM） | 可解释性 |
| 工业检测（任务多样） | Analytic + Ensemble 结合 | 需求多样 |
| 自动驾驶（大数据模型） | Ensemble | — |
| 智能制造（多样问题） | Analytic + Ensemble 结合 | — |

> **核心信息：没有单一最优算法适用所有问题**，需据场景选择或组合。

#### 8.10 Ensemble Learning 近年发展

- Deep ensemble learning
- Ensemble methods for foundation models
- Distributed ensemble learning
- Online and streaming ensembles
- Ensemble reinforcement learning
- Explainable ensemble models

### 9. 机器学习未来方向

- **Efficient Learning**：fast and scalable learning algorithms
- **Explainable AI**：提升模型透明度与可解释性
- **Continual Learning**：学新知识不忘旧知识
- **Hybrid Learning**：结合 analytic learning、deep learning、ensemble learning

> ML 持续向更高效、智能、可信的系统演进。

### 10. 本课整体路线图与学习目标

- L1（本周）：Introduction（已完成）。
- **L2（下周）**：Data Preprocessing + 数学复习补充——**共用基础，服务 Part 1 与 Part 2**。强调 **data quality**："garbage in, garbage out"——数据质量是 ML 成功基础，不可忽视。
- L3–L8：Analytic Learning 主体（Toh）。
- L9–L13：Ensemble Learning（Liu），含工业应用（可能加一个 analytic 工业案例）。

#### 学完本课应能：

1. 理解 analytic learning 原理。
2. 理解 ensemble learning 原理。
3. 比较不同 ML paradigm。
4. 为实际应用选择合适学习方法。
5. 了解现代 ML 近年发展。

> **强调理解原理（principles）而非死记算法**——与 6222/6497 老师理念一致。

### 11. Week 1 关键要点（Key Takeaways）

- 机器学习让计算机从数据学习。
- **Analytic learning** 提供**高效 closed-form 解**（无迭代优化）。
- **Ensemble learning** 通过组合多个 learner 提升鲁棒性。
- 不同学习范式适用不同应用——了解各自优劣是构建有效智能系统的关键。
- 本课兼顾基本原理与实用方法。

---

> **下周（Week 2）预告**：Lecture 2 **Data Preprocessing**——What is data、data types、distance metrics、preprocessing methods，外加 **Mathematics Review**（线性代数、矩阵分解、最小二乘、正则化、凸优化等 analytic learning 所需工具）。本周不展开，待学后整理。
>
> **笔记约定**：本课英文授课、英文考试，核心术语保留英文（machine learning, supervised/unsupervised/semi-supervised/reinforcement learning, analytic learning, ensemble learning, closed-form solution, iterative optimization, gradient descent, SGD, Adam, hyperparameter, learning rate, bagging, boosting, random forest, Adaboost, gradient boosting, XGBoost, LightGBM, bias, variance, diversity, voting, averaging, regularization, least-squares, kernel ridge regression, matrix inversion, overfitting, interpretability, generalization, continual learning, hybrid learning, lockdown browser 等）。中文用于组织句意与补充释义。
