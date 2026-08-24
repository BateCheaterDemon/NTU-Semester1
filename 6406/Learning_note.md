# EE6406 — Analytic and Ensemble Machine Learning（解析式与集成机器学习）

> 课程学习笔记总览。每周一节，按周总结重点内容。
> 第一周（开课周）特别关注考核要求、任课教师、课程定位与整体结构。
>
> **权威来源说明**：本笔记先由各周录播转写（`week1.txt`、`week2.txt`…）整理，再以对应官方讲义 PDF（`EE6406-Lecture1/2-LZP-v1.pdf`、`EE6406-Lecture2Suppl-LZP-v1.pdf`，Zhiping Lin，AY2026-27 S1）核对修正。转写有大量语音识别噪声（如 "Dinger Ping/P L" 实为 Zhiping Lin、"proto/Tok" 实为 Toh Kar-Ann、"Simon Le/Dell" 实为 Simon Liu、"seemal/on sample" 实为 ensemble、"sample learning" 实为 ensemble learning、"fear" 实为 field、"etction" 实为 extraction、"n by n/n to n dives" 实为 end-to-end、"mean ski/Mosk/means co ski" 实为 Minkowski、"humming" 实为 Hamming、"matrix" 常实为 metric、"lacung/lacungan/logngan" 实为 Lagrange(Lagrangian)、"copian" 实为 Jacobian、"fi" 实为 affine、"S score/score stang" 实为 z-score(standardization)、"packing lot" 实为 log、"sikmoi" 实为 sigmoid、"biliion/valian/variant" 实为 variance、"neumic/neumatical" 实为 numeric(numerical)、"Odiner" 实为 ordinal、"chromo" 实为 cofactor、"alg gate/adj gate" 实为 adjugate、"atom" 实为 codomain 等），均以 PDF 为准修正。Week 1 转写仅覆盖 Lecture 1（课程导论）；Week 2 转写覆盖 Lecture 2（Data Preprocessing）与 Lecture 2 Supplement（Mathematics Review）。

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

## Week 2 — Data Preprocessing（Lecture 2）＋ Mathematics Review（Lecture 2 Supplement）

> 本周由 Zhiping Lin 主讲，是 Part 1 的共用基础。转写覆盖 Lecture 2（Data Preprocessing，50 页）与 Lecture 2 Supplement（Mathematics Review，43 页）两份 PDF。Lecture 1 不进 quiz/exam，**但 Lecture 2（data preprocessing）会进 quiz 与 final exam**，本周内容务必重视。

### 0. 课前行政提醒

- **Quiz logistics**：第一次 quiz（CA1）在 **Week 5**（距本周三周），仅 **15 分钟**，in-class，需 **lockdown browser**。计划在 **Week 4 开头**用 10–15 分钟做一次 try-run 测试设备。**PC + Windows 最稳**；Mac/Unix 可能有麻烦；iPad 可用但不稳。Lecture 8 由两位教授合上（Part 1 收尾）；之后由 Toh (proto) 接手。
- **教材**：主教材电子版在 NTU 图书馆可免费访问（用学号登录），应可下载 PDF；书中每章有习题 + 解答，作为练习资源足够，无需额外索题。录像已上 NTULearn。
- **本周录播中无新的考勤/签到安排**；与考勤相关的只有上述 in-class quiz 要求。

---

### Part A：Lecture 2 — Data Preprocessing

#### 1. Pattern Recognition Pipeline（学习管线）

机器学习/模式识别的通用流程（本周聚焦其中的 preprocessing 与 feature extraction）：

```
Raw data → Preprocessing → Feature Extraction → Training Features / Test Features
        → Model Selection → Learning → Learned Model
        → (Test) Trained Prediction / Test Prediction
        → Decision & Performance Evaluation
```

- **Data Preprocessing**：为数据准备有意义的表示。
  - **Normalization**（此处泛指规整）：去除非代表性或冗余部分、做相关调整；主要目的是 **防止 anomalies（异常）主导分析**。
  - **Data conversion**：在 nominal/ordinal/interval/ratio 等不同 data type 间转换。
- **Feature Extraction**：从大批数据中提取 informative、relevant、non-redundant 成分，常大幅降低数据维度，故与 **dimension reduction** 相关，常涉及 data transformation。
  - **Feature selection**（= variable selection）：选 relevant feature 子集，相对简单（按准则选/赋权）。
  - **Feature extraction**：做变换使特征更具代表性，可进一步降维。
  - 两大路线：
    - **Generic dimension reduction**：**PCA**（principal component analysis）、**ICA**（independent component analysis）、isomap、multilinear subspace learning、autoencoder。
    - **Extracting semantic features**：edge detection、corner detection、blob detection、ridge detection、**SIFT**（scale-invariant feature transform）。
  - 即便 end-to-end deep learning 可把这些步骤一并学，理解各步仍重要——尤其中小规模实际问题。
- **Learning**：学一个函数 $Y = f(X)$（$X$ 输入、$Y$ 输出，均可为 scalar 或 vector）。$f$ 的形式未知，任务是评估手头算法哪个最好描述问题。
- **Decision & Performance Evaluation**：
  - 训练后用 optimized model $f$ 对 unseen data $X_t$ 得预测 $Y_t = f(X_t)$；classification 时再加 threshold decision 定类别。
  - **Generalization capability** 关键——训练数据常受采集与预算限制，模型须在有限样本上仍能泛化。
  - **N-fold cross-validation**：数据均分 N 折，N−1 折训练、1 折测试，轮换使每折恰好做一次测试集，最终性能取 N 次平均；充分利用全部数据。**Lecture 8（Toh）会详讲 performance evaluation**。

#### 2. What is Data?

据 Wikipedia：data 是 "a collection of discrete or continuous values that convey information, describing the quantity, quality, fact, statistics, other basic units of meaning, or simply sequences of symbols"。**datum** 是其中单个值。

- 要点：data 携带的信息**未必正确**——可能是错误或误导信息，故 raw data 后仍需考察质量。
- 例子：
  - **Optdigit dataset**：手写数字 0–9，用 gray level/intensity 表示，像素值 0–255。
  - **Spiral pattern**（高度非线性，多 spiral 同属一类）与 **bar graph**（日常分布可视化，如各国/各校学生人数）——常用于测试模型能否识别非线性结构。
- **Discrete vs Continuous**：
  - Discrete variable：可映射到可数集，可无限大（如整数）或仅有限范围；相邻值间有间隔。
  - Continuous variable：稠密，任意两值间总能取另一值，不可数（如 $[0,1]$ 内有无穷多个值）。
  - 物理量（如温度）本质 continuous，但计算机处理时常 **sampling** 成 discrete。

#### 3. Data Types（四类，按度量层次）

| 类型 | 别名 | 是否有序 | 数值? | 绝对零点? | 例子 |
|---|---|---|---|---|---|
| **Nominal** | categorical / qualitative | 无 | 否 | — | gender、race、blood type、place、ID、鱼/水果名 |
| **Ordinal** | — | 有 | 否（仅 rank） | — | good/better/fair、excellent/good/average、patient priority、survey satisfaction、small/medium/large、undergrad→MSc→PhD |
| **Interval** | — | 有 | 是 | **否**（零点 arbitrary，负值允许） | Celsius 温度（0℃ ≠ 无温度，故 60℃ ≠ 30℃ 的两倍热） |
| **Ratio** | — | 有 | 是 | **是**（absolute zero） | Kelvin 温度、age、height、weight（40kg = 20kg 的两倍） |

- **层级关系**：qualitative（nominal）→ quantitative（discrete/continuous）。Continuous 再细分为 interval 与 ratio（区别在于有无 natural/absolute zero point）。Discrete 为 nominal 与 ordinal 共用（类别数不能无穷）。
- **Binary / Non-binary**：binary 仅 0/1；non-binary 可 0,1,2,…。

##### 3.1 Nominal data 的数值编码（Numeric Conversion / Data Encoding）

- **Arbitrary assignment**（如 male=1, female=2）：简单，但大/小数值在计算中可能造成"大值更具影响力"的误导；且会丢失内在关系（如 north/east/south/west=1/2/3/4 丢失邻近关系）。
- **Binary coding**：按位数丰富表示，含 binary-coded decimal、n-ary gray codes、**one-hot encoding**。
  - **One-hot encoding**：每个类别用一个向量，仅对应位置为 1 其余为 0，用位置标记类别，避免赋值带来虚假序。**处理无序类别（如水果名）时推荐**。
- 进阶编码会考虑各 attribute 的 probability distribution。转换后 binary feature vector 可用 **Hamming distance、Spearman distance** 等比较。

##### 3.2 Ordinal data 的数值编码

- 可用 percentage / frequency of occurrence；与 nominal 不同，**赋数值后可算 mean、median、mode**——但 mean 须谨慎（rank 间距未知，mean 可能非整数、意义可疑；mode/median 更稳）。
- **Rank encoding with normalization**：rank $r=1,\dots,R$ 归一化到 $[0,1]$：

$$
d = \frac{r-1}{R-1} \tag{1}
$$

- 比较两 rank 向量的距离：
  - **Spearman distance**：正比于两 rank 向量 Euclidean 距离的平方。例：$x=[2,3,1]$、$y=[3,2,1]$，$d(x,y) \propto \sqrt{(2-3)^2+(3-2)^2+(1-1)^2}=\sqrt{2}$（课件写正比于 2，即未开方的平方和）。
  - **Hamming distance**：等长 rank 串中对应位置不同的个数。$[2,3,1]$ vs $[3,2,1]$ → 前两位不同 → 2。
  - **Chebyshev distance**（= maximum value distance）：两 ordinal 向量各分量绝对差的最大值。
  - 其它：Kendall、Cayley、Ulam distance。

##### 3.3 Interval vs Ratio（关键区别）

- 唯一区别：**有无 absolute zero point**。
- **Celsius = interval**（0℃ 非绝对零点，不能说 60℃ 是 30℃ 的两倍）；**Kelvin = ratio**（0 K = 分子运动完全停止 = 绝对零点，60 K 确为 30 K 的两倍）。
- 两类都可定义两点距离，但 **scaling 后解释不同**，故 normalization 时须注意 scaling 的影响。

#### 4. Distance Metrics（距离度量）

> 在 unsupervised learning / clustering 中尤其重要——无 ground truth 时靠度量样本间距离判断聚合。

##### 4.1 定义与四公理

距离映射 $d(x,y): \mathcal{X}\times\mathcal{X} \mapsto [0,\infty)$，须满足：

| 公理 | 条件 |
|---|---|
| Non-negativity | $d(x,y) > 0$ |
| Identity of indiscernibles | $d(x,y) = 0 \iff x=y$ |
| Symmetry | $d(x,y)=d(y,x)$ |
| Triangle inequality | $d(x,z) \le d(x,y)+d(y,z)$ |

满足者称 **metric**；带 metric 的集合称 **metric space**。

##### 4.2 常见 metric

| 距离 | 别名 / 关系 |
|---|---|
| **Hamming distance** | 是 metric（满足四公理） |
| **Euclidean metric** | 2-norm / $L_2$-norm，几何距离 |
| **Manhattan / taxicab metric** | 1-norm / $L_1$-norm |
| **Minkowski distance** | p-norm metric，$L_1$/$L_2$ 的推广 |

公式（$d$ 维）：

$$
\text{1-norm: } d=\sum_{i=1}^d |x_i-y_i|,\quad
\text{2-norm: } d=\Big(\sum_{i=1}^d |x_i-y_i|^2\Big)^{1/2},\quad
\text{p-norm: } d=\Big(\sum_{i=1}^d |x_i-y_i|^p\Big)^{1/p}
$$

$$
\text{$\infty$-norm: } d=\lim_{p\to\infty}\Big(\sum_{i=1}^d |x_i-y_i|^p\Big)^{1/p} = \max_i |x_i-y_i|
$$

- **关键考点**：**Minkowski distance 当 $p \ge 1$ 时是 metric**（满足四公理）；**$p < 1$ 时不是 metric**——**违反 triangle inequality**。
- 课件 Fig.5 画了 $L_{0.1}, L_{0.5}, L_1, L_2, L_3, L_{10}$ 的单位等距线：$p<1$ 时等距线凹（concave），两中转点之间不满足三角不等式；$p\ge1$ 时凸。**往年考题有相关题，务必会判断 $p<1$ 非 metric。**

#### 5. Preprocessing Methods

数据可能来自 nominal/ordinal/interval/ratio 多种类型、多个来源、长时间跨度，空间维度大、含时序，须做 preprocessing 以保证 representation 的一致性。

##### 5.1 Cleaning / Cleansing（数据清洗）

检测、纠正、移除 corrupted、incomplete、erroneous、inaccurate 样本。四项质量要求：

| 要求 | 含义 |
|---|---|
| **Completeness** | 所有必需测量都可得；不可得则重测或移除缺失样本 |
| **Consistency** | 相近条件下测量可复现；stationary data 不应 drift，non-stationary 的 drift 需建模 |
| **Uniformity** | 同一 unit/scale 表示（如 kg vs pounds 须统一） |
| **Validity** | 符合既定约束（如百分比总和须为 100%） |

> 老师举的 validity 实例：院系教授绩效评估本应 40% research + 40% teaching + 20% service = 100%，结果有人填成 40/50/20，被当场质疑——百分比类数据必须总和 100%。

##### 5.2 Alignment（对齐）

图像处理中常需先提取相关区域。如 face recognition 中，基于眼/鼻/嘴位置裁出人脸（排除头发与饰物），只比较这些 landmark 周围区域；**不做对齐会导致错误比较**。

##### 5.3 Normalization（归一化，本周重点）

测量数据范围可能很大，ML 模型通常更易处理落在 normalized range（如 $[0,1]$、$[-1,1]$）的输入。三种方法：

**(1) Min-max scaling**（已知 bounds 或可估 $\min/\max$）：

$$
x_i = \frac{x_i^{raw} - x_{\min}}{x_{\max} - x_{\min}},\quad i=1,\dots,M \tag{8}
$$

**(2) Standardization（z-score）**（数据近似 normal distribution，或 $\min/\max$ 不可知——如 Gaussian 理论上 $\min/\max$ 无穷）：

$$
x_i = \frac{x_i^{raw} - E[X]}{\sigma(X)},\quad i=1,\dots,M \tag{9}
$$

实际 $E[X],\sigma(X)$ 常未知，用样本估计：

$$
\hat\mu = \frac{1}{M}\sum_{i=1}^M x_i,\qquad \hat\sigma^2 = \frac{1}{M}\sum_{i=1}^M (x_i-\hat\mu)^2 \tag{10,11}
$$

此过程统计学中亦称 **standardization**。

**(3) Median Absolute Deviation (MAD)**——用 median 替代 mean 作参考，对 outlier 更稳健：

$$
\mathrm{MAD} = \mathrm{median}\big(|x_i - \mathrm{median}(X)|\big),\qquad x_i = \frac{x_i^{raw} - \mathrm{median}(X)}{\mathrm{MAD}} \tag{12,13}
$$

> **为何用 median？** 100 人工资中若有一人挣百万（outlier），mean 被拉高、给出"平均工资很高"的误导印象；**median（中位点）更具代表性**。故有 outlier 时用 MAD 而非 z-score。图像处理中 **median filter** 也因此常用。

##### 5.4 Other Transformations

- **平移/缩放**：乘、加、减某值把数据线性移到目标范围。
- **log 变换** $\log(x_i)$：数据跨指数尺度（如 1 到 1 百万）时，取 log 压缩范围、削弱大值对小值的 masking。**注意：log 仅适用于非负值**（负值取 log 数学上无意义）。
- **exp 变换** $\exp(x_i)$：数据过于平坦/密集时拉伸，凸显差异。
- **非线性拉伸**：**sigmoid** 与 **hyperbolic tanh**（神经网络常用）：

$$
x_i = \frac{1}{1+e^{-h(x_i^{raw})}},\qquad x_i = \tanh\big(h(x_i^{raw})\big) \tag{14,15}
$$

其中 $h(\cdot)$ 可取上述任一 normalization 形式（如 (9)）。

##### 5.5 ⭐ Normalization 与 Train/Test 的 data leakage（重要）

- **若在切分 train/test 前对整个数据集做 global preprocessing**（如算 global mean/variance），会导致 **data leakage（train-test contamination）**。
- **正确做法**：normalization 参数**只在 training set 上计算**，再应用到 validation/test set。
- 否则相当于用测试集信息训练，不公平且高估泛化性能。

#### 6. Lecture 2 小结

- **Data**：discrete/continuous、convey information（可能错误/误导）。
- **Data types**：nominal（categorical）、ordinal（有序但差异未知）、interval & ratio（numeric，区别在 absolute zero）。
- **Distance metrics**：$L_1, L_2, L_p$ 等；**Minkowski 仅 $p\ge1$ 为 metric**。
- **Data normalization**：min-max、z-score standardization、MAD 等；**train/test 分离防 leakage**。

---

### Part B：Lecture 2 Supplement — Mathematics Review

> 服务 Part 1（analytic learning 需数学工具；Part 2 要求略低）。EE 硕士项目无 machine learning/AI 数学基础课，故各课自带复习。本补充 PDF 已在 NTULearn。大纲：Linear Algebra → Systems of Linear Equations（Linear Dependency）→ Functions → Constrained Optimization。

#### 7. Linear Algebra：Notations, Vectors & Matrices

- **Scalar**：单一数值（如 68、$-3.13$），用斜体字母 $x, a$；本课聚焦**实数**。
- **Summation / Product**：$\sum_{i=1}^m x_i$、$\prod_{i=1}^m x_i$。
- **Vector**：有序标量列表（attributes），用**粗体小写** $\mathbf{x,w}$；常**列向量**表示，可视为多维空间中的点或箭头。元素用带下标的斜体 $a_j, x_j$（$j$ 表维度）。
- **Matrix**：行列排列的数表，用**粗体大写** $\mathbf{A,X,W}$。元素 $x_{i,j}$（先行后列）。变量可有多下标，如神经网络 $x_{l,u}^{(j)}$ 表第 $l$ 层第 $u$ 个 unit 的第 $j$ 个输入特征。
  - 例：Iris 数据集——4 个 feature（维度=4）、150 个样本、3 类（setosa/versicolor/virginica），用 $y$ 标 label。
- **向量运算**：加减按元素；标量乘除按元素（除数不为零）。
- **Transpose** $\mathbf{x}^T, \mathbf{X}^T$：列↔行；$m\times n$ 矩阵转置为 $n\times m$。
- **Dot product / Inner product**：$\mathbf{x}\cdot\mathbf{y}=\mathbf{x}^T\mathbf{y}=\sum x_i y_i$。
  - **几何定义**：$\mathbf{y}\cdot\mathbf{x}=\|\mathbf{y}\|\|\mathbf{x}\|\cos\theta$，$\theta$ 为夹角，$\|\mathbf{z}\|=\sqrt{\mathbf{z}\cdot\mathbf{z}}$ 为 Euclidean 长度。
  - $\theta=0$（同向）→ $\cos\theta=1$ → inner product 最大；$\theta=90°$（正交）→ $\cos\theta=0$ → inner product 为 0。
- **Matrix-Vector / Vector-Matrix / Matrix-Matrix product**：须**维度相容**（内维匹配）。矩阵乘矩阵可视为"矩阵逐列乘向量"组合。**考试常考简单乘法，务必熟练，维度不匹配会算错。**

##### 7.1 Matrix Inverse（矩阵逆）

- $d\times d$ 方阵 $\mathbf{A}$ **可逆（invertible / nonsingular）**当且仅当存在 $d\times d$ 方阵 $\mathbf{B}$ 使 $\mathbf{AB}=\mathbf{BA}=\mathbf{I}$（identity matrix）。
- 公式：

$$
\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})}\mathrm{adj}(\mathbf{A})
$$

- $\det(\mathbf{A})$ 为 determinant；$\mathrm{adj}(\mathbf{A})$（adjugate/adjoint）为 cofactor matrix 的转置。
- **可逆 ⟺ full rank ⟺ 行列线性无关 ⟺ $\det(\mathbf{A})\ne 0$**。

##### 7.2 Determinant 与 Cofactor

- **$2\times2$**：$\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$。
- **$3\times3$**：用 **cofactor（Laplace）展开**——任选一行（如第一行 $a,b,c$），交叉划掉对应行列后余 $2\times2$ 子式，符号 $+,-,+$ 交替：

$$
\det = a\cdot M_{11} - b\cdot M_{12} + c\cdot M_{13}
$$

- **Cofactor matrix** $C$：$c_{ij}=(-1)^{i+j}M_{ij}$（$M_{ij}$ 为删第 $i$ 行第 $j$ 列的 minor）。需对每位置算，符号棋盘格 $+,-,+,\dots$。
- **Adjugate** $\mathrm{adj}(\mathbf{A}) = C^T$（cofactor matrix 的转置）。
- **手动计算上限**：$2\times2$ 必会，$3\times3$ 是挑战但仍要求（展开/求逆/求 cofactor 都到 $3\times3$）；更高维极繁琐，不要求手算。
- **求逆步骤**：算 $\det$ → 算 cofactor matrix → 转置得 adjugate → 除以 $\det$。

##### 7.3 Linear Dependency（线性相关/无关）

- $d$-向量组 $\mathbf{x}_1,\dots,\mathbf{x}_m$（$m>1$）**linearly dependent**：存在不全为零的标量 $\beta_1,\dots,\beta_m$ 使

$$
\beta_1\mathbf{x}_1+\cdots+\beta_m\mathbf{x}_m = \mathbf{0}
$$

- **linearly independent**：上式仅当所有 $\beta_i=0$ 时成立（即 not linearly dependent）。
- 几何直觉（2D）：两向量同向 → dependent；平面内两不同向量可张成平面，但无法表示平面外的第三向量 → 该第三向量与前两者 independent。
- 与矩阵可逆性直接挂钩（行列 independent ⟺ 可逆）。

#### 8. Set & Function

- **Set**：无序、元素唯一的集合；用花体大写 $\mathbb{R,N,C}$（实数/整数/复数；本课基本只用 real 与 integer）。
  - 有限集用花括号 $\{1,3,18\}$；可无限。
  - 区间：闭区间 $[a,b]$（含端点）、开区间 $(a,b)$（不含端点）；$\mathbb{R}$ 含全体实数。
  - 运算：交 $\cap$、并 $\cup$（并集不重复元素）。
- **Function**：把 domain（定义域）每个 $x$ 映射到 codomain（陪域）中单值 $y=f(x)$。
  - **Range / image**：实际映射到的子集（区别于 codomain 这个"可去"的全集）。
  - 可 scalar→scalar、vector→scalar、vector→vector 等；记法 $f:\mathbb{R}^d\to\mathbb{R}$ 表"d-向量到实数"的 scalar-valued function。

##### 8.1 Linear & Affine Function

- **Linear function** $f:\mathbb{R}^d\to\mathbb{R}$ 满足两性质（合称 **superposition**）：
  - **Homogeneity**：$f(\alpha\mathbf{x})=\alpha f(\mathbf{x})$。
  - **Additivity**：$f(\mathbf{x}+\mathbf{y})=f(\mathbf{x})+f(\mathbf{y})$。
- 内积函数 $f(\mathbf{x})=\mathbf{w}^T\mathbf{x}=\sum w_i x_i$ 是线性（可验证 superposition）。
- **Affine function**：$f(\mathbf{x})=\mathbf{w}^T\mathbf{x}+b$，即 linear 加一个标量 **offset / bias** $b$。
  - 几何区别：linear 过原点；affine 不过原点（有 offset）。例 $f(\mathbf{x})=2.3-2x_1+1.3x_2-x_3$ 是 affine（$b=2.3$）。

##### 8.2 Local / Global Minimum；max / argmax

- **Local minimum** at $x=c$：$f(x)>f(c)$ 在 $c$ 的某开区间内成立。
- **Global minimum**：所有 local minimum 中最小者。
- $\max_{a\in A} f(a)$：返回**最高函数值**（来自 range/codomain）。
- $\arg\max_{a\in A} f(a)$：返回**使 $f$ 最大的元素 $a$**（来自 domain）。$\min/\arg\min$ 同理。

##### 8.3 Derivative & Gradient

- 导数 $f'$ 描述 $f$ 增减快慢；$f'>0$ 增、$f'<0$ 减、$f'=0$ 处斜率水平。
- **标量函数对向量求导 → gradient**（$d\times1$ 向量）：

$$
\frac{df(\mathbf{x})}{d\mathbf{x}} = \nabla_{\mathbf{x}} f = \begin{bmatrix}\partial f/\partial x_1\\ \vdots\\ \partial f/\partial x_d\end{bmatrix}
$$

- **向量函数对向量求导 → Jacobian**（$h\times d$ 矩阵，$h$ 为函数输出维）：

$$
\frac{d\mathbf{f}(\mathbf{x})}{d\mathbf{x}} = \begin{bmatrix}\partial f_1/\partial x_1 & \cdots & \partial f_1/\partial x_d\\ \vdots & & \vdots\\ \partial f_h/\partial x_1 & \cdots & \partial f_h/\partial x_d\end{bmatrix}
$$

- **向量-矩阵求导公式**（考试会给，不必死记）：

$$
\frac{d\mathbf{A}\mathbf{x}}{d\mathbf{x}}=\mathbf{A},\qquad \frac{d\mathbf{y}^T\mathbf{A}\mathbf{x}}{d\mathbf{x}}=\mathbf{A}^T\mathbf{y},\qquad \frac{d\mathbf{x}^T\mathbf{A}\mathbf{x}}{d\mathbf{x}}=(\mathbf{A}+\mathbf{A}^T)\mathbf{x}
$$

  - 第三式：若 $\mathbf{A}$ 对称则简化为 $2\mathbf{A}\mathbf{x}$。注意 $\mathbf{y}$ 视为独立于 $\mathbf{x}$。

#### 9. Constrained Optimization（约束优化）— Lagrangian

求 $f(\mathbf{x})$ 在约束 $g(\mathbf{x})=0$ 下的极值。构造 **Lagrangian**：

$$
\mathcal{L}(\mathbf{x},\lambda) = f(\mathbf{x}) + \lambda\, g(\mathbf{x}) \tag{2}
$$

其中 $\lambda$ 为 **Lagrange multiplier（拉格朗日乘子，标量）**。对 $\mathbf{x}$ 求导并令零：

$$
\frac{\partial\mathcal{L}}{\partial\mathbf{x}} = \frac{\partial f(\mathbf{x})}{\partial\mathbf{x}} + \lambda\frac{\partial g(\mathbf{x})}{\partial\mathbf{x}} = \mathbf{0} \tag{3}
$$

再结合 $\partial\mathcal{L}/\partial\lambda=0$（即 $g(\mathbf{x})=0$），用微积分方法联立解出 $\lambda$ 与极值点 $\mathbf{x}$。**把约束优化转为无约束问题**。细节留给 Toh 在后续 6 讲展开。

### 10. Week 2 关键要点（Key Takeaways）

- **Lecture 2 会进 quiz 与 final exam**（Lecture 1 不会）。
- 数据四类型（nominal/ordinal/interval/ratio）的区别与编码方式（尤其 one-hot、rank normalization）。
- **Minkowski distance 仅 $p\ge1$ 为 metric**（$p<1$ 违反 triangle inequality）——高频考点。
- Normalization 三法（min-max / z-score standardization / MAD）的选择依据（有 outlier 用 MAD）。
- **Normalization 参数只在 training set 上算**，防 data leakage。
- 数学工具：矩阵求逆（$\det$/cofactor/adjugate）、linear vs affine（offset）、gradient/Jacobian、Lagrangian 约束优化——为 Part 1 analytic learning（closed-form 解）铺路。

---

> **下周（Week 3）预告**：由 **Toh Kar-Ann** 接手，进入 **Lecture 3 — Linear Parametric Models**（Part 1 Analytic Learning 主体起点）。将用本周复习的线性代数与 least-squares 工具，从 closed-form 视角建立线性参数模型。本周数学补充是直接前置知识，建议先消化 gradient、matrix inverse、Lagrangian 三块。
>
> **笔记约定**：本课英文授课、英文考试，核心术语保留英文（machine learning, supervised/unsupervised/semi-supervised/reinforcement learning, analytic learning, ensemble learning, closed-form solution, iterative optimization, gradient descent, SGD, Adam, hyperparameter, learning rate, bagging, boosting, random forest, Adaboost, gradient boosting, XGBoost, LightGBM, bias, variance, diversity, voting, averaging, regularization, least-squares, kernel ridge regression, matrix inversion, overfitting, interpretability, generalization, continual learning, hybrid learning, lockdown browser, pattern recognition pipeline, feature extraction/selection, dimension reduction, PCA, ICA, SIFT, nominal/ordinal/interval/ratio data, one-hot encoding, rank encoding, Hamming/Spearman/Chebyshev/Minkowski distance, metric/metric space, triangle inequality, L1/L2/Lp-norm, cleansing, completeness/consistency/uniformity/validity, alignment, min-max scaling, standardization, z-score, median absolute deviation (MAD), data leakage, log/exp/sigmoid/tanh transform, vector/matrix, transpose, inner/dot product, determinant, cofactor, adjugate, identity matrix, invertible/nonsingular, linearly dependent/independent, set, domain/codomain/range, linear/affine function, offset/bias, local/global minimum, max/argmax, gradient, Jacobian, Lagrangian, Lagrange multiplier, constrained optimization 等）。中文用于组织句意与补充释义。
