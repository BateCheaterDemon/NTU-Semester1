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
> **笔记约定**：本课英文授课、英文考试，核心术语保留英文（machine learning, supervised/unsupervised/semi-supervised/reinforcement learning, analytic learning, ensemble learning, closed-form solution, iterative optimization, gradient descent, SGD, Adam, hyperparameter, learning rate, bagging, boosting, random forest, Adaboost, gradient boosting, XGBoost, LightGBM, bias, variance, diversity, voting, averaging, regularization, least-squares, kernel ridge regression, matrix inversion, overfitting, interpretability, generalization, continual learning, hybrid learning, lockdown browser, pattern recognition pipeline, feature extraction/selection, dimension reduction, PCA, ICA, SIFT, nominal/ordinal/interval/ratio data, one-hot encoding, rank encoding, Hamming/Spearman/Chebyshev/Minkowski distance, metric/metric space, triangle inequality, L1/L2/Lp-norm, cleansing, completeness/consistency/uniformity/validity, alignment, min-max scaling, standardization, z-score, median absolute deviation (MAD), data leakage, log/exp/sigmoid/tanh transform, vector/matrix, transpose, inner/dot product, determinant, cofactor, adjugate, identity matrix, invertible/nonsingular, linearly dependent/independent, set, domain/codomain/range, linear/affine function, offset/bias, local/global minimum, max/argmax, gradient, Jacobian, Lagrangian, Lagrange multiplier, constrained optimization, analytic regression, over-determined/under-determined system, normal equation, least-squares solution, minimum-norm solution, pseudo-inverse, ridge regression, weight decay, Tikhonov regularization, shrinkage, primal/dual ridge, Gram matrix, representer theorem, kernel regression, kernel trick, kernel ridge regression / KRR, threshold classification, feature matrix, one-vs-rest, multi-category learning 等）。中文用于组织句意与补充释义。

---

## Week 4 — Lecture 4：Learning Score Functions（损失函数 / 分类评估 / ROC-AUC）

> **权威来源说明**：本周无录播转写，基于官方课件 `week4/EE6406-Lecture4-TKA-v2.pdf`（Toh Kar-Ann，62 页，标题 *Learning Score Functions*）整理。无口述补充，所有内容以 PDF 为准。本周承接 Week 3 的 Linear Parametric Models，把学习模型 $g(x,w)$ 嵌入到 score/loss metric 中构造 learning objective function，分 regression accuracy / classification accuracy / ranking & operating characteristics 三条主线。

### 1. 本周主线

Week 3 建立了线性参数模型 $g(x,w)=w^\top x$（及多项式 / linear parametric 形式）。本周回答"如何**度量**模型好坏"——用 **loss function（损失函数）** 单样本计罚、求和成 **learning cost function / objective function** $J(w)$，再用 Week 2 的矩阵代数求解 $\arg\min_w J(w)$。

三大 cost function 对应三类学习任务：

| 任务 | accuracy 类型 | 核心 loss | cost function |
|---|---|---|---|
| **Regression** | 距离型 | squared error loss | MSE / SSE |
| **Classification** | 计数型 | 0-1 loss（及 surrogate） | misclassification error / TER |
| **Ranking** | 排序型 | pair-wise ranking | ROC / AUC |

### 2. 基本概念：error function vs loss function

- **Error function（误差函数）**：量化预测值与真实值的**偏离**（deviation）。
- **Loss function（损失函数）**：评估该误差的**不良后果**，按误差大小赋予 penalty。
  - regression 中常为 squared error；classification 中评估 misclassification 数量。
- 二者常互换使用，但有 subtle difference：error 量偏差、loss 量代价。

### 3. ⭐ Learning Cost Function 的一般形式

$$
\arg\min_w J(w)=\arg\min_w\sum_{i=1}^{m}L\bigl(g(x_i,w),y_i\bigr)+\lambda R(w)
$$

| 符号 | 含义 |
|---|---|
| $J(w)$ | **Learning cost function**（optimization criterion） |
| $L(\cdot)$ | **Loss function**（aka **Score function**） |
| $g(x_i,w)$ | Learning model |
| $x_i$ | Learning model input vector |
| $w$ | Learning parameter vector |
| $y_i$ | Learning target |
| $m$ | Sample size |
| $R(w)$ | **Regularization function** |
| $\lambda$ | **Regularization factor** |

**Building blocks of learning algorithms（四大构件）**：
1. Learning model $g$ —— 对 $x_i\to y_i$ 关系的 belief。
2. Loss function $L$ —— 预测 $g_w(x_i)$ 而真值为 $y_i$ 时的 penalty。
3. Regularization $R$ —— 鼓励更简模型（less complex）。
4. Cost function $J$ —— 最终 optimization criterion；外加 optimization routine 求 $w$。

### 4. 为何需要不同 loss function（Motivation）

- Regression：连续 target → squared error（距离）。
- Classification：离散 label → 需 discrete counting loss，如 $\frac12\sum\bigl[1-\operatorname{sgn}(y_i g(x_i,w))\bigr]$。
- 课件 1D/2D 例子对比：
  - **error-distance loss**（squared）：对 outlier 极敏感（outlier 在 (1000,1000) 把 8th-order 多项式拉偏）。
  - **error-counting loss**（discrete）：对 outlier 鲁棒（只计对错，不看距离大小）。
- ⇒ 不同 loss 适合不同任务/数据特性，这是本周核心动机。

### 5. 常见 Loss Functions（六种，必背）

| Loss | 公式 | 用途 |
|---|---|---|
| **Squared error**（quadratic loss） | $L(e)=e^2=(g(x,w)-y)^2$ | regression |
| **Binary / 0-1 loss** | $L=\frac{1+\operatorname{sgn}(-y\,g(x,w))}{2},\ y\in\{-1,+1\}$ | classification counting |
| **Logistic loss** | $L=\frac{1}{1+e^{y\,g(x,w)}}$ | classification（LogitBoost） |
| **Hinge loss** | $L=\max(0,-y\,g(x,w))$ | classification（**SVM**） |
| **Exponential loss** | $L=e^{-y\,g(x,w)}$ | classification（**AdaBoost**） |
| **Cross-entropy loss** | $L=-y\log p-(1-y)\log(1-p)$ | classification（logistic regression / NN） |

### 6. Regression Accuracy

#### 6.1 MSE 与 SSE

$$
\text{MSE:}\ J(w)=\frac{1}{m}\sum_{i=1}^{m}\bigl[g(x_i,w)-y_i\bigr]^2 \tag{4.1}
$$

$$
\text{SSE:}\ J(w)=\sum_{i=1}^{m}\bigl[g(x_i,w)-y_i\bigr]^2 \tag{4.2}
$$

- loss = squared error distance $[g(x_i,w)-y_i]^2$。
- 求 minimizer 时系数 $1/m$ **immaterial**（不影响最优解位置），故 SSE 与 MSE 等价用于优化。

#### 6.2 Example 4.1：矩阵-向量形式

含 intercept/bias 的样本矩阵（每行 $\begin{bmatrix}1 & x_{i,1} & \cdots & x_{i,d}\end{bmatrix}$）：

$$
X=\begin{bmatrix}1 & x_{1,1} & \cdots & x_{1,d}\\ \vdots & \vdots & & \vdots\\ 1 & x_{m,1} & \cdots & x_{m,d}\end{bmatrix},\quad y=\begin{bmatrix}y_1\\\vdots\\y_m\end{bmatrix}
$$

- 线性模型 $g=w^\top x$：$J(w)=(Xw-y)^\top(Xw-y)$。
- 一般 linear parametric 形式（特征变换 $p(x_i)$ 堆叠成 $P$）：$J(w)=(Pw-y)^\top(Pw-y)$。
- ⭐ 矩阵-向量形式允许用 **matrix algebra** 求 closed-form 解（回到 Week 3 的 normal equations / pseudo-inverse）。

### 7. Classification Accuracy

#### 7.1 Confusion Matrix（混淆矩阵，二分类）

四种分类结果：class-0 正确为 0、class-1 正确为 1、0 误判为 1、1 误判为 0。

| | 预测 P | 预测 N |
|---|---|---|
| **真实 P** | **TP**（true positive） | **FN**（false negative，type II error） |
| **真实 N** | **FP**（false positive，type I error） | **TN**（true negative） |

衍生指标：
- **Sensitivity / Recall / TPR** = $\frac{TP}{TP+FN}=\frac{TP}{n^+}$
- **Specificity / TNR** = $\frac{TN}{FP+TN}=\frac{TN}{n^-}$
- **Precision / PPV** = $\frac{TP}{TP+FP}$
- **NPV** = $\frac{TN}{FN+TN}$
- **Accuracy** = $\frac{TP+TN}{TP+TN+FP+FN}$

#### 7.2 四个 rate 及其冗余

$$
TPR=\frac{TP}{n^+},\quad TNR=\frac{TN}{n^-},\quad FPR=\frac{FP}{n^-},\quad FNR=\frac{FN}{n^+}
$$

$$
TPR+FNR=1,\quad TNR+FPR=1 \tag{4.12-4.13}
$$

⇒ **只需两个 rate（每式各一）即可完整描述**分类器性能，如 $\{TPR,TNR\}$ 即可推出 $\{FNR,FPR\}$。

#### 7.3 多类 Confusion Matrix

$c$ 类，$P_i$ 为第 $i$ 类样本数，$P_{i,\hat j}$ 为真实类 $i$ 被预测为类 $j$ 的数量。对角线 = 正确预测：

$$
P_{i,\hat i}=P_{\hat i}-\sum_{i}P_{i,\hat j}\quad(\text{列补}),\qquad P_{i,\hat i}=P_i-\sum_{j}P_{i,\hat j}\quad(\text{行补}) \tag{4.14-4.15}
$$

#### 7.4 Accuracy / Precision / F-measure（含 skewing factor $s=n^-/n^+$）

| 指标 | 定义（$s=n^-/n^+$） |
|---|---|
| Accuracy | $\frac{TPR+s\cdot TNR}{1+s}=\frac{TP+TN}{n^++n^-}$ |
| Precision | $\frac{TPR}{TPR+s\cdot FPR}=\frac{TP}{TP+FP}$ |
| **F-measure** | $\frac{2TPR}{TPR+s\cdot FPR+1}=\frac{2TP}{TP+FP+n^+}$ |

- $s$ 为 skewing factor，常取 $s=n^-/n^+$ 以平衡类别不平衡。

#### 7.5 Misclassification Error 与 Total Error Rate

$$
err(g,y)=\mathbf{1}_{(g\ne y)},\qquad \text{err}=\frac{FP+FN}{n}=1-\text{Accuracy}\big|_{s=n^-/n^+} \tag{4.17-4.18}
$$

$$
\text{TER}=FPR+FNR \tag{4.19}
$$

- **HTER（half total error rate）**$=\frac{FPR+FNR}{2}=\frac{1}{2}(2-TER)=1-\text{Accuracy}\big|_{s=1}$。
- 多类 misclassification error = confusion matrix 所有 **off-diagonal** 之和。

### 8. Equal Error Rate（EER）

- 二分类 predictor 输出归一化到 $[0,1]$，变动 threshold $\tau\in[0,1]$ → 得一系列 FPR/FNR。
- **FPR 随 $\tau$ 递减、FNR 随 $\tau$ 递增**；两曲线交点 = **Equal Error Rate (EER)**。
- EER 是 threshold 选取的自然平衡点（FPR=FNR）。

### 9. Loss Functions（margin 视角，分类统一表达）

定义 **margin** $\mu_i=y_i g(x_i)$（$y_i\in\{-1,+1\}$）：
- $\mu>0$ ⇒ 同号 ⇒ 分类正确。
- $\mu<0$ ⇒ 异号 ⇒ 分类错误。
- 隐含零阈值分隔正负。

| Loss | margin 形式 | 备注 |
|---|---|---|
| **0-1 loss** | $L_{01}(\mu)=0$ if $\mu>0$, else $1$ | 离散；**梯度零或未定义，很少直接用于训练** |
| **Squared loss** | $\sum(g(x_i)-y_i)^2$ | 回归用 |
| **Hinge loss** | $L_{\text{hinge}}(\mu)=\max(0,1-\mu)$ | **SVM** |
| **Logistic loss** | $L_{\text{logistic}}(\mu)=\log(1+e^{-\mu})$（或归一化 $(\log2)^{-1}\log(1+e^{-\mu})$） | **LogitBoost** |
| **Exponential loss** | $L_{\exp}(\mu)=e^{-\mu}$ | **AdaBoost** |

⭐ **关键 remarks**：0-1 step loss 因梯度零或未定义，**很少直接用于训练**；改用 **smooth continuous surrogate**（logistic / hinge / exponential）以利优化。

### 10. Logistic Regression 与 Cross-Entropy

#### 10.1 Log-odds 与 sigmoid

拟合线性模型 $g(x)=\alpha_0+\alpha^\top x$ 到 **log-odds**：

$$
\log\frac{p}{1-p}=g(x)\quad\Rightarrow\quad p=\sigma(g(x))=\frac{1}{1+e^{-g(x)}}=\frac{e^{g(x)}}{1+e^{g(x)}} \tag{4.30-4.31}
$$

- $\sigma(\cdot)=\frac{1}{1+e^{-\cdot}}$ 为 **logistic function / sigmoid function**。

#### 10.2 Log-likelihood 与 Cross-Entropy（对偶）

$$
L_{\text{log-likelihood}}(p)=y\log p+(1-y)\log(1-p)\quad(\text{maximize}) \tag{4.32}
$$

$$
L_{\text{cross-entropy}}(p)=-y\log p-(1-y)\log(1-p)\quad(\text{minimize}) \tag{4.33}
$$

多类 cross-entropy：

$$
L_{\text{cross-entropy}}(p)=-\sum_{i=1}^{c}y_i\log(p_i) \tag{4.34}
$$

- $y_i$ = 第 $i$ 类 target label，$p_i$ = 第 $i$ 类预测概率。
- ⭐ cross-entropy 是 log-likelihood 的**负值**（对偶：maximize likelihood ⇔ minimize cross-entropy）。

### 11. Regularization Term

cost function 含两个 loss 组件 $L$ 与 $R$：

$$
J(w)=\sum_{i=1}^{m}L\bigl(\mu_i(w)\bigr)+\lambda R(w) \tag{4.35}
$$

正则化家族 $R_q=\frac{1}{q}\bigl(\sum_i|w_i|^q+\epsilon\bigr)^{1/q}$（PDF 公式 4.36）：

| 正则 | 形式 | 名称 | 作用 |
|---|---|---|---|
| $R_0$ | $\|\{i:w_i\ne0\}|$ | **subset selection** | 计非零参数个数 |
| $R_1$ | $\sum_i|w_i|$ | **lasso** | L1，稀疏解 |
| $R_2$ | $\frac{1}{2}\|w\|_2^2$ | **ridge regression** | L2，缩缩解 |
| $R_q$ | 一般 $q$ | general family | $q\to$ 大趋近 max-norm |

- $\lambda$ 是 scalar regularization weighting factor，平衡 data fit 与 model complexity。
- Week 2 已建立的 bias-variance / overfitting 在此落地：$R$ 抑制过参化。

### 12. Ranking & Operating Characteristics

#### 12.1 ROC Curve（受试者工作特征曲线）

- 变动 threshold $\tau$，画 $FNR(\tau)$ vs $FPR(\tau)$（或 $TPR(\tau)$ vs $FPR(\tau)$）得单一曲线 = **ROC curve**。
- 曲线**越弯向原点**（或 TPR-FPR 版本越弯向左上角）→ 分类器越好。
- 对角线 = 随机分类器（AUC=0.5）。

#### 12.2 ⭐ AUC（Area Under ROC Curve）

$$
\text{AUC}=\frac{1}{m^+m^-}\sum_{i=1}^{m^+}\sum_{j=1}^{m^-}u(\xi_{ij}),\quad \xi_{ij}=g(x_i^+)-g(x_j^-) \tag{4.38}
$$

$$
u(\xi)=\begin{cases}1,&\xi>0\\0.5,&\xi=0\\0,&\xi<0\end{cases}
$$

- AUC = **正负样本对中被正确排序的比例**（probability that positive score > negative score）。
- ⭐ **AUC 只看 score order，不看 score value**（ranking-based，threshold-free）。

#### 12.3 Lorenz Curve 与 Gini Coefficient

- **Gini coefficient** = $2\times\text{AUC}-1$（AUC 的线性重标）。
- $G=A/(A+B)$，$(A+B)=0.5$ ⇒ $A=\text{AUC}-0.5$。
- Gini=0（AUC=0.5）⇒ 无判别力（non-discriminative classifier）；Gini=1（AUC=1）⇒ 完美分类。

### 13. ⭐ LSE / MCE / TER / AUC 四种 cost function 对比

$$
\text{MSE:}\ J(w)=\frac{1}{m}\sum(g(x_i,w)-y_i)^2\quad\text{(regression)} \tag{4.39}
$$

$$
\text{MCE:}\ J(w)=\frac{1}{m}\sum\bigl(u(y_i g(x_i,w))-1\bigr)^2\quad\text{(classification)} \tag{4.40}
$$

$$
\text{TER:}\ J(w)=\frac{1}{m^-}\sum u\bigl(y_i^- - g(x_i^-,w)\bigr)+\frac{1}{m^+}\sum u\bigl(g(x_i^+,w)-y_i^+\bigr)\quad\text{(classification)} \tag{4.41}
$$

$$
\text{AUC:}\ J(w)=\frac{1}{m^+m^-}\sum\sum u\bigl(g(x_i^+,w)-g(x_j^-,w)\bigr)\quad\text{(ranking order)} \tag{4.42}
$$

| cost | 度量性质 | 任务 | 关键 |
|---|---|---|---|
| **MSE/LSE** | 距离 | regression | squared error |
| **MCE** | 计数 | classification | 0-1 型 |
| **TER** | 加权计数 | classification | FPR+FNR |
| **AUC** | 排序 | ranking | 正负对排序，与 threshold 无关 |

### 14. 考点速查表

| 考点 | 要点 |
|---|---|
| error vs loss | error 量偏差、loss 量代价 |
| cost function 三要素 | $L$（loss）+ $R$（regularization）+ $\lambda$ |
| 六种 loss | squared / 0-1 / logistic / hinge / exponential / cross-entropy |
| 0-1 loss 不直接训练 | 梯度零/未定义 → 用 surrogate（hinge/logistic/exponential） |
| SVM 用 hinge | AdaBoost 用 exponential，LogitBoost 用 logistic |
| confusion matrix | TP/FP/FN/TN；type I=FP，type II=FN |
| rate 冗余 | $TPR+FNR=1$，$TNR+FPR=1$，只需两个 |
| F-measure | $\frac{2TP}{TP+FP+n^+}$，含 skewing factor |
| TER / HTER | $TER=FPR+FNR$，$HTER=TER/2$ |
| EER | FPR=FNR 交点 |
| cross-entropy = −log-likelihood | maximize likelihood ⇔ minimize cross-entropy |
| 正则化 | $R_1$=lasso（稀疏），$R_2$=ridge（缩缩） |
| AUC | 正负对正确排序比例，只看 order 不看 value |
| Gini | $2\cdot\text{AUC}-1$ |

### 15. 本周要点小结

- **Learning cost function** 一般形式 $\arg\min_w\sum L(g(x_i,w),y_i)+\lambda R(w)$；四大构件 model/loss/regularization/optimization。
- **Regression** 用 squared error → MSE/SSE；矩阵形式 $(Xw-y)^\top(Xw-y)$ 回到 Week 3 closed-form。
- **Classification** 用 0-1 counting loss；confusion matrix 衍生 TP/FP/FN/TN → TPR/TNR/FPR/FNR（两两冗余）→ Accuracy/Precision/F-measure/TER/HTER/EER。
- **Loss 统一 margin 视角** $\mu=yg(x)$：0-1 / hinge（SVM）/ logistic（LogitBoost）/ exponential（AdaBoost）；0-1 不直接训练，用 smooth surrogate。
- **Logistic regression**：sigmoid + cross-entropy（= −log-likelihood）。
- **Regularization** $R_q$ 家族：$R_1$=lasso、$R_2$=ridge，平衡 data fit 与 complexity。
- **Ranking**：ROC curve（TPR vs FPR）→ AUC（正负对排序比例，threshold-free）→ Gini = 2·AUC−1。
- **四种 cost 对比**：MSE（距离/regression）、MCE（计数）、TER（加权计数）、AUC（排序）。

---

> **下周（Week 5）预告**：本周建立了 loss/cost function 框架。按 Toh 的 Analytic Learning 主线，预计 Week 5 进入 **具体学习算法的 cost function 求解**——可能是 logistic regression 的迭代优化（gradient descent / IRLS）、SVM 的 hinge + regularization 求解，或 ridge/lasso 的 closed-form 与 sparse 解。本周的 cost function 公式（4.39–4.42）与正则化（4.36）是直接前置。具体以 Lecture 5 课件为准。

---

## Week 5 — Lecture 5：Over- and Under-determined Analytic Regression

> **教授**：Toh Kar-Ann（TKA，Week 3–8 主讲）。本周回到 Lecture 3 的 regression 解析求解框架，系统讲完 over/under-determined、Primal/Dual Ridge、Kernel/Kernel Ridge Regression，最后接 threshold 做 classification。
>
> 老师口述定位："This lecture will be focused on **analytic regression**… lecture five for **regression**, lecture six directly optimize **classification**。"即 Lecture 5 用 regression 学习 + threshold 切割做分类，Lecture 6 才直接对 classification 优化。

### 1. 本课定位：Regression → Threshold → Classification

- Learning 的目标是 **regression**（学一个 predictor $g(\mathbf{x},\mathbf{w})$ 拟合连续 target $y$）。
- 回归学到的 $g$ 经 **thresholding**（阈值切割）即可用于 **classification**：$g(\mathbf{x},\hat{\mathbf{w}})>\tau$ 归一类、否则另一类。
- 故本周先讲 regression 的解析解；最后一步补 threshold 即成 classifier。
- 与 Week 3 的关系：Lecture 3 讲了 closed-form regression 的基础，本周是其完整化（over/under-determined + 正则化 + kernel）。

### 2. SSE Minimization（cost function 与 normal equation）

**模型**：线性 predictor $g(\mathbf{x},\mathbf{w})=\mathbf{w}^T\mathbf{x}$（含偏置），堆叠 $m$ 个训练样本为 feature matrix $P\in\mathbb{R}^{m\times(D+1)}$、target $\mathbf{y}\in\mathbb{R}^{m}$。

**SSE cost function**（Week 4 已建立）：

$$
J_{\text{SSE}}(\mathbf{w})=\|\mathbf{y}-P\mathbf{w}\|_2^2=(\mathbf{y}-P\mathbf{w})^T(\mathbf{y}-P\mathbf{w})\tag{5.3}
$$

**Normal equation**（一阶导 $\nabla_{\mathbf{w}}J=0$）：

$$
-2P^T(\mathbf{y}-P\mathbf{w})=\mathbf{0}\quad\Longrightarrow\quad P^TP\,\mathbf{w}=P^T\mathbf{y}\tag{5.5}
$$

- $P^TP$ 即 (scaled) sample covariance matrix；$P^T\mathbf{y}$ 即 feature-target 互相关。

### 3. ⭐ Over-determined 系统（$m>D+1$）：唯一解

样本多于参数（$m>D+1$），$P^TP$ 非奇异（observations 独立），unique 最优解：

$$
\boxed{\;\hat{\mathbf{w}}=(P^TP)^{-1}P^T\mathbf{y}\;}\tag{5.6}
$$

- 此即 **least-squares 解** / normal equation 解；$J$ 是凸二次函数 → 此解为全局最优。
- $\hat{\mathbf{w}}$ 是由 $P,\mathbf{y}$ 唯一确定的 fixed point。

### 4. Multi-category Learning：堆叠输出矩阵

对 $C$ 类，把 $C$ 个 binary one-vs-rest target 向量并列成 $Y\in\mathbb{R}^{m\times C}$，权重堆叠 $W\in\mathbb{R}^{(D+1)\times C}$：

$$
J_{\text{SSE}}(W)=\|Y-PW\|_F^2,\qquad\hat{W}=(P^TP)^{-1}P^TY
$$

- 列向 = 类别；每列独立是一个 binary regression。
- 预测：$\text{cls}(g(\mathbf{x}_j,W))=\arg\max_k\,g(\mathbf{x}_j,\mathbf{w}_k)$。

### 5. ⭐ Under-determined 系统（$m<D+1$）：最小范数解

样本少于参数（$m<D+1$），$P^TP\in\mathbb{R}^{(D+1)\times(D+1)}$ 奇异（$P$ 最多 $m$ 个独立行，$\text{rank}(P)\le m$），无唯一解——**有无穷多解**。

此时取**最小范数解**（minimum-norm solution）：

$$
\min_{\mathbf{w}}\|\mathbf{w}\|_2^2\quad\text{subject to}\quad\mathbf{y}-P\mathbf{w}=\mathbf{0}\tag{5.26}
$$

用 Lagrangian（Lagrange multiplier $\boldsymbol{\alpha}$）求解，得：

$$
\hat{\mathbf{w}}=P^T(PP^T)^{-1}\mathbf{y}
$$

- 注意对偶形式：over-determined 用 $(P^TP)^{-1}$（$(D+1)\times(D+1)$），under-determined 用 $(PP^T)^{-1}$（$m\times m$，更小可逆）。
- ⚠️ Under-determined 即使加 weight-decay 正则化仍可能 **numerically ill-conditioned**，预测可很不准。

### 6. ⭐ Primal Ridge Regression（加正则化的 closed-form）

**动机**：$P^TP$ 可能奇异或病态 → 加正则化（weight decay / Tikhonov / ridge）保证可逆并控制复杂度。

**Regularized cost**：

$$
J_{\text{SSE}_r}(\mathbf{w})=\|\mathbf{y}-P\mathbf{w}\|_2^2+\lambda\|\mathbf{w}\|_2^2
$$

一阶导 $\nabla_{\mathbf{w}}J=0$ 得 **Primal Ridge 解**：

$$
\boxed{\;\hat{\mathbf{w}}=(P^TP+\lambda I)^{-1}P^T\mathbf{y}\;}\tag{5.31}
$$

- $\lambda>0$ 使 $(P^TP+\lambda I)$ **恒可逆**（即使 $P^TP$ 奇异）；同时收缩权重（weight decay / shrinkage），降低 overfitting。
- Multi-category：$\hat{W}=(P^TP+\lambda I)^{-1}P^TY$。
- 老师强调："Ridge regression is also known as **weight decay regularization**"——名称不同、本质相同。

### 7. ⭐ Dual Ridge Regression（在小空间求逆）

**思想**：在 $(P^TP+\lambda I)$（$(D+1)\times(D+1)$）与 $(PP^T+\lambda I)$（$m\times m$）中选**较小者**求逆。

由 $(P^TP+\lambda I)\mathbf{w}=P^T\mathbf{y}$ 令 $\mathbf{w}=P^T\boldsymbol{\alpha}$（representer 形式）代入：

$$
(PP^T+\lambda I)\boldsymbol{\alpha}=\mathbf{y}
$$

定义 **Gram matrix** $K=PP^T$，则：

$$
\boxed{\;\hat{\boldsymbol{\alpha}}=(K+\lambda I)^{-1}\mathbf{y},\qquad\hat{\mathbf{w}}=P^T\hat{\boldsymbol{\alpha}}\;}
$$

- Multi-category：$\hat{A}=(K+\lambda I)^{-1}Y$，$\hat{W}=P^T\hat{A}$。
- ⭐ **何时用 dual**：样本数 $m$ < 特征维数 $D+1$（如 kernel 方法、高维特征），在 $m\times m$ 空间求逆更省。

### 8. ⭐ Kernel Regression（用 kernel 替代内积）

据 **representer theorem**：任意 RKHS 下带正则化的 cost minimizer 都可写成训练数据的线性组合 $\mathbf{w}=P^T\boldsymbol{\alpha}$，因此**无需显式构造高维特征**，直接用 kernel $k(\mathbf{x}_i,\mathbf{x}_j)=\phi(\mathbf{x}_i)^T\phi(\mathbf{x}_j)$ 计算内积。

- Gram matrix $K$ 中每项 $K_{ij}=k(\mathbf{x}_i,\mathbf{x}_j)=\phi(\mathbf{x}_i)^T\phi(\mathbf{x}_j)$。
- 在 dual 空间解 $\boldsymbol{\alpha}$：$\hat{\boldsymbol{\alpha}}=(K+\lambda I)^{-1}\mathbf{y}$。
- **预测**（unseen $\mathbf{x}_j$）：

$$
g(\mathbf{x}_j,\hat{\mathbf{w}})=\sum_{i=1}^{m}\hat{\alpha}_i\,k(\mathbf{x}_i,\mathbf{x}_j)=\mathbf{k}(\mathbf{x}_j,P)(K+\lambda I)^{-1}\mathbf{y}
$$

- ⭐ 核心收益：**避免显式映射到高维（甚至无限维）feature space**——kernel 直接计算高维内积，计算量由 $m$ 决定而非特征维数。

### 9. Kernel Ridge Regression（KRR）

Kernel Regression + Ridge 正则化合一，即 **Kernel Ridge Regression (KRR)**：

$$
\hat{\boldsymbol{\alpha}}=(K+\lambda I)^{-1}\mathbf{y},\qquad g(\mathbf{x}_j)=\mathbf{k}(\mathbf{x}_j,P)(K+\lambda I)^{-1}\mathbf{y}
$$

- Multi-category：$\hat{A}=(K+\lambda I)^{-1}Y$，$\hat{G}_t=\mathbf{k}(\mathbf{x}_j,P)(K+\lambda I)^{-1}Y$。
- 训练只需 Gram matrix $K$ + 解线性方程 $(K+\lambda I)\boldsymbol{\alpha}=\mathbf{y}$；预测只需 kernel 求值。

### 10. Threshold 与 Classification Decision

学得 regression 输出 $g(\mathbf{x},\hat{\mathbf{w}})$ 后，加 threshold $\tau$ 做分类：

$$
\text{cls}(g)=\begin{cases}1 & g(\mathbf{x},\hat{\mathbf{w}})>\tau\\ 0 & g(\mathbf{x},\hat{\mathbf{w}})<\tau\end{cases}
$$

- 归一化输出 $g\in[0,1]$（$y\in\{0,1\}$）取 $\tau=0.5$；$g\in[-1,+1]$（$y\in\{-1,+1\}$）取 $\tau=0$。
- ⭐ **regression vs classification**：regression 学连续输出、**不需要 threshold**（逼近 target 即可）；classification 学完再加 threshold 切割成离散类。
- Multi-category：$\text{cls}(g(\mathbf{x}_j,W))=\arg\max_k\,g(\mathbf{x}_j,\mathbf{w}_k)$。

### 11. ⭐ 公式速查表

| 方法 | 解 / 公式 | 适用 |
|---|---|---|
| **Normal equation** | $P^TP\mathbf{w}=P^T\mathbf{y}$ | SSE 一阶条件 |
| **Over-determined** | $\hat{\mathbf{w}}=(P^TP)^{-1}P^T\mathbf{y}$ | $m>D+1$，$P^TP$ 可逆 |
| **Multi-category** | $\hat{W}=(P^TP)^{-1}P^TY$ | $C$ 类堆叠 |
| **Under-determined min-norm** | $\hat{\mathbf{w}}=P^T(PP^T)^{-1}\mathbf{y}$ | $m<D+1$，$(PP^T)^{-1}$ |
| **Primal Ridge** | $\hat{\mathbf{w}}=(P^TP+\lambda I)^{-1}P^T\mathbf{y}$ | 加正则化，恒可逆 |
| **Dual Ridge** | $\hat{\boldsymbol{\alpha}}=(K+\lambda I)^{-1}\mathbf{y}$，$\hat{\mathbf{w}}=P^T\hat{\boldsymbol{\alpha}}$，$K=PP^T$ | 小空间求逆 |
| **Kernel Regression** | $g(\mathbf{x}_j)=\mathbf{k}(\mathbf{x}_j,P)\hat{\boldsymbol{\alpha}}$，$\hat{\boldsymbol{\alpha}}=(K+\lambda I)^{-1}\mathbf{y}$ | kernel 隐式高维内积 |
| **Kernel Ridge (KRR)** | 同上 + ridge 正则 | Kernel + Ridge |
| **Threshold** | $\text{cls}(g)=1$ if $g>\tau$（$\tau=0.5$ 或 $0$） | regression→classification |

### 12. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| **SSE normal equation** | $-2P^T(\mathbf{y}-P\mathbf{w})=0$ → $P^TP\mathbf{w}=P^T\mathbf{y}$ |
| **over-determined 解** | $\hat{\mathbf{w}}=(P^TP)^{-1}P^T\mathbf{y}$，唯一、凸最优 |
| **under-determined** | $P^TP$ 奇异 → 无穷解 → 取 min-norm $\hat{\mathbf{w}}=P^T(PP^T)^{-1}\mathbf{y}$ |
| **Primal Ridge** | $\hat{\mathbf{w}}=(P^TP+\lambda I)^{-1}P^T\mathbf{y}$；$\lambda$ 使恒可逆 + shrinkage |
| **Dual Ridge** | $\hat{\boldsymbol{\alpha}}=(K+\lambda I)^{-1}\mathbf{y}$，$K=PP^T$（Gram）；选小空间求逆 |
| **Gram matrix** | $K=PP^T$ |
| **Representer theorem** | $\mathbf{w}=P^T\boldsymbol{\alpha}$，解在 dual 空间 |
| **Kernel Regression** | 用 $k(\cdot,\cdot)$ 隐式高维内积，避免显式映射 |
| **KRR** | Kernel + Ridge，$\hat{\boldsymbol{\alpha}}=(K+\lambda I)^{-1}\mathbf{y}$ |
| **Threshold classification** | regression 学完加 $\tau$ 切割；$\tau=0.5$（$\{0,1\}$）或 $0$（$\{-1,+1\}$） |
| **regression vs classification** | regression 无需 threshold；classification 才 threshold |
| **ill-conditioned** | under-determined 即使加正则仍可能病态 |

### 13. 本周要点小结

- **SSE 框架**：$J=\|\mathbf{y}-P\mathbf{w}\|^2$，normal equation $P^TP\mathbf{w}=P^T\mathbf{y}$，凸二次 → 唯一最优（over-determined）。
- **Over vs Under-determined**：$m>D+1$ 用 $(P^TP)^{-1}$；$m<D+1$ 时 $P^TP$ 奇异，取 min-norm 解 $P^T(PP^T)^{-1}\mathbf{y}$（对偶，小空间求逆）。
- **Ridge Regression**：加 $\lambda\|\mathbf{w}\|^2$ 正则 → $(P^TP+\lambda I)^{-1}$ 恒可逆 + 权重收缩 = weight decay = Tikhonov。
- **Dual Ridge**：$\mathbf{w}=P^T\boldsymbol{\alpha}$，在 Gram matrix $K=PP^T$ 上解 $\hat{\boldsymbol{\alpha}}=(K+\lambda I)^{-1}\mathbf{y}$；选较小维数求逆。
- **Kernel / KRR**：representer theorem + kernel trick 隐式高维内积，计算量由 $m$ 决定；KRR = Kernel + Ridge 一体。
- **Threshold**：regression 学连续输出 → 加 $\tau$（0.5 或 0）切割成 classification。Lecture 5 = regression（解析），Lecture 6 = 直接优化 classification。

---

> **下周（Week 6）预告**：老师明确 "lecture six directly optimize **classification**"——下周从 regression+threshold 转向**直接对 classification cost 优化**的学习方法（如 logistic regression、SVM 的解析/迭代求解），threshold 由模型本身隐含而非后接。本周的 SSE/Ridge/Kernel 公式是直接前置。具体以 Lecture 6 课件为准。

---

## Week 6 — Lecture 6：Advanced Analytic Classification（直接优化分类目标）

> **教授**：Toh Kar-Ann（TKA）。本周转回 classification 直接优化视角：不先做 regression 再加 threshold，而是把 classification metric（TER / AUC）本身作为 learning cost function 直接求 closed-form 解。全讲分四部分：(1) Introduction（classification error based learning 动机）、(2) Total Error Rate Learning、(3) Operating Characteristics Learning（AUC based）、(4) A Generalized Learning Framework（通过 data transformation 统一 LSE/TER/AUC/FLD）。
>
> 老师口述定位："This class, we are moving on to **classification** learning in **analytic** way… we want to introduce a way to solve the classification error **directly**. This has not been able to solve in analytic form [previously]… We'll introduce two solutions: one is **total error rate**, one is the **AUC** solution."即两种分类器学习解均可 closed-form 求得且具有 nonlinear mapping capability（通过 polynomial/kernel 的 $p(x)$ 嵌入）。

### 1. 从 Regression 到 Classification：动机与思路

- **回顾**：Lecture 5 用 regression（SSE / Ridge / Kernel）学连续 predictor $g(\mathbf{x},\mathbf{w})$，再加 threshold $\tau$ 做 classification——classification 只是 regression 的后接副产物。
- **本周核心问题**：既然目标是 classification，**为何不直接优化 classification metric 本身**（如 misclassification count、TER、AUC），而要绕道 regression？
- **难点**：classification metric 是 **counting nature**（计数型，如 0-1 loss），导致 cost function **non-differentiable**（不可微）——传统方法只能用 iterative numerical optimization 求解，无 closed-form。
- **本周突破**：介绍两个 **closed-form** classification 学习解：
  1. **TER based learning**：直接用 Total Error Rate（$FPR+FNR$）作 objective function。
  2. **AUC based learning**：用 Area Under ROC Curve 作 objective function。
- 两者均通过 **quadratic approximation + data manipulation** 把 non-differentiable step loss 转为可微 convex 问题，从而得到 closed-form 解。
- ⭐ **关键 insight**：solution 的结构类似 regression（normal equation 形式），但 data 按 class 分拆、class-specific normalization——本质是 **weighted least squares**。

### 2. Total Error Rate（TER）Based Learning

#### 2.1 TER 作为 objective function

回顾 Week 4 的 TER 定义（$TER=FPR+FNR$）。用 threshold $\tau$ 表达：

$$
\text{TER}=FPR+FNR=\frac{1}{m^-}\sum_{j=1}^{m^-}\mathrm{cls}\bigl(g(\mathbf{x}_j^-, \mathbf{w})>\tau\bigr)+\frac{1}{m^+}\sum_{i=1}^{m^+}\mathrm{cls}\bigl(g(\mathbf{x}_i^+, \mathbf{w})<\tau\bigr) \tag{5.65}
$$

- $\mathrm{cls}(\cdot)$ 为 classification function：条件成立时输出 1（error），否则 0。
- $m^+$、$m^-$ 分别为 positive / negative 样本数。

#### 2.2 变量替换统一 loss 形式

利用 $g(\mathbf{x}_j^-)>\tau$ 与 $g(\mathbf{x}_i^+)<\tau$ 的对称性，做 change of variables 统一为"threshold at zero"：

$$
\varepsilon_j = g(\mathbf{x}_j^-, \mathbf{w})-\tau,\quad j=1,\dots,m^- \qquad \epsilon_i = \tau - g(\mathbf{x}_i^+, \mathbf{w})-\Delta,\quad i=1,\dots,m^+
$$

- $\Delta\to 0$ 处理严格不等号，实际可忽略。
- 统一后两式的 error 均 $>0$ 时计为错误。

$$
\text{TER}=\frac{1}{m^-}\sum_{j=1}^{m^-}L(\varepsilon_j>0)+\frac{1}{m^+}\sum_{i=1}^{m^+}L(\epsilon_i>0) \tag{5.66}
$$

- 学习目标：$\hat{\mathbf{w}}=\arg\min_{\mathbf{w}}\text{TER}$。
- $L(\cdot)$ 是 threshold at zero 的 classification decision function，targets 为 $\{-1,+1\}$（而非 $\{0,1\}$）。

#### 2.3 ⭐ Sigmoid 近似及其问题

(5.67) 的 step loss **不可微**，自然用 smooth sigmoid 近似：

$$
\sigma(\theta)=\frac{1}{1+e^{-\gamma\theta}},\quad \gamma>0 \tag{5.69}
$$

- $\gamma$ 控制 slope：$\gamma$ 大则接近 step function。
- 近似后 TER 变为 smooth differentiable 问题 (5.70)。

**但 sigmoid 近似有两个问题**：
1. **Nonlinear formulation w.r.t. $\mathbf{w}$**：$\sigma(\varepsilon)$ 中 $\varepsilon$ 是 $\mathbf{w}$ 的函数，故 $\sigma(\mathbf{w})$ 非线性 → **多个 local solutions**，不同 initialization 收敛到不同 local optimum，需 trial-and-error。
2. **Local plateaus**：sigmoid 的 flat regions 叠加后梯度近零，迭代搜索 stuck、进展缓慢。

> 老师口述补充：早期神经网络（1960s–70s backpropagation）广泛用 sigmoid activation，至今 deep learning 仍用 sigmoid 变体。local minima 问题仍在，但大数据量下"many local minima 给出的解对人眼足够好"——理论未解决但实践可用。

#### 2.4 ⭐ Link-Loss Functional Pair：Linear Link + Quadratic Loss

**关键思路**：用 **link function**（模型 $g$）与 **loss function**（$L$）的匹配 pair 保证 convex → closed-form。

- **Linear link** $g(\mathbf{x},\mathbf{w})=\mathbf{w}^T\mathbf{x}$（含 polynomial/kernel 的 $p(\mathbf{x})$ 嵌入，linear w.r.t. $\mathbf{w}$）。
- **Quadratic loss** $L(\cdot)=(\cdot)^2$。
- **Linear + Quadratic → convex → closed-form 可解**。

**但 quadratic loss 的逻辑问题**：quadratic 两端均高（$|\varepsilon|$ 大时 loss 大），而 classification 需要的是"错误高、正确低"（monotonic，类似 step function）——quadratic 不区分正负，不能直接用。

#### 2.5 ⭐ Offset Trick：只用 quadratic 的一臂

**解决方法**：给 error 加一个 uniform offset $\eta$，把 quadratic curve 推到一侧，使 data 只落在 quadratic 的**单臂**上：

$$
\text{TER}(\mathbf{w})\approx\min_{\mathbf{w}}\left[\frac{1}{2m^-}\sum_{j=1}^{m^-}(\varepsilon_j+\eta)^2+\frac{1}{2m^+}\sum_{i=1}^{m^+}(\epsilon_i+\eta)^2\right] \tag{5.71}
$$

- $\eta$ 把 quadratic 中心偏移，使得错误样本 $(\varepsilon>0$ 或 $\epsilon>0)$ 落在高 loss 臂、正确样本落在低 loss 区。
- 系数 2 来自两个 square 项的微分归一化。
- ⭐ **核心技巧**：用 monotonic 的单臂 quadratic 近似 step loss，既可微又保持 convex。

#### 2.6 ⭐ TER Closed-form Solution（Primal）

加入 weight decay regularization $b\|\mathbf{w}\|_2^2$，线性 predictor $g=\mathbf{w}^T p(\mathbf{x})$：

$$
\min_{\mathbf{w}}\left[\frac{b}{2}\|\mathbf{w}\|_2^2+\frac{1}{2m^-}\sum_{j=1}^{m^-}\bigl(\mathbf{w}^T p(\mathbf{x}_j^-)-\tau+\eta\bigr)^2+\frac{1}{2m^+}\sum_{i=1}^{m^+}\bigl(\tau-\mathbf{w}^T p(\mathbf{x}_i^+)+\eta\bigr)^2\right] \tag{5.72}
$$

对 $\mathbf{w}$ 求一阶偏导令零（first-order necessary condition；quadratic → 充分），得：

$$
\boxed{\;\hat{\mathbf{w}}=\left[bI+\frac{1}{m^-}\sum_{j=1}^{m^-}p_j^-{p_j^-}^T+\frac{1}{m^+}\sum_{i=1}^{m^+}p_i^+{p_i^+}^T\right]^{-1}\left[\frac{(\tau-\eta)}{m^-}\sum_{j=1}^{m^-}p_j^-+\frac{(\tau+\eta)}{m^+}\sum_{i=1}^{m^+}p_i^+\right]\;}
$$

- $p_j^-=p(\mathbf{x}_j^-)\in\mathbb{R}^{D+1}$，$p_i^+=p(\mathbf{x}_i^+)\in\mathbb{R}^{D+1}$。
- $b$ 控制 regularization 强度（默认 $10^{-4}$）。

**矩阵形式**（$P^+$、$P^-$ 分别为 positive/negative 样本的 projection matrix）：

$$
\hat{\mathbf{w}}=\left[bI+\frac{1}{m^-}{P^-}^T P^-+\frac{1}{m^+}{P^+}^T P^+\right]^{-1}\left[\frac{(\tau-\eta)}{m^-}{P^-}^T\mathbf{1}^-+\frac{(\tau+\eta)}{m^+}{P^+}^T\mathbf{1}^+\right] \tag{5.76}
$$

- ⭐ **与 regression 解的对比**：regression 用统一的 $P^TP$；TER 把 $P$ 按 class 拆成 $P^-$、$P^+$，分别 normalize（$1/m^-$、$1/m^+$），target 也分拆为 $y^-=(\tau-\eta)$ 和 $y^+=(\tau+\eta)$。本质是 **class-specific weighted least squares**。
- **balanced class**（$m^+=m^-$）时 TER 退化为 regression 解（权重相同）；**imbalanced class** 时 TER 的 class-specific normalization 使决策边界不受类别密度影响——这是 TER 优于 regression 的关键。

#### 2.7 Multi-category TER

$C$ 类，每类用 one-hot indicator。第 $k$ 类的 positive target $y_k^+=(\tau+\eta)\mathbf{1}^+$，negative target $y_k^-=(\tau-\eta)\mathbf{1}^-$。解堆叠：

$$
\hat{W}=[\hat{\mathbf{w}}_1,\cdots,\hat{\mathbf{w}}_C] \tag{5.78}
$$

- 每个 $\hat{\mathbf{w}}_k$ 独立求解（类似 multi-category regression 的列独立），但 $P_k^+$、$P_k^-$ 对每个类的正负划分不同（one-hot encoding 导致）。

#### 2.8 ⭐ TER Dual Space 解

定义 class-specific diagonal weighting matrices $M^-$、$M^+$（对角元素 $1/m^-$、$1/m^+$），$M=M^-+M^+$：

$$
\hat{\mathbf{w}}=\left[bI+P^T(M^-+M^+)P\right]^{-1}P^T(M^-+M^+)\mathbf{y}=\left[bI+P^TMP\right]^{-1}P^T M\mathbf{y} \tag{5.82}
$$

- target 向量 $\mathbf{y}$ 按类排列：前 $m^-$ 个为 $(\tau-\eta)/m^-$，后 $m^+$ 个为 $(\tau+\eta)/m^+$。

用 representer 形式 $\mathbf{w}=P^T M\boldsymbol{\alpha}$（类似 dual ridge regression 推导）：

$$
\boxed{\;\hat{\boldsymbol{\alpha}}=(bI+P^TP M)^{-1}\mathbf{y},\qquad \hat{\mathbf{w}}=P^T M(bI+P^T P M)^{-1}\mathbf{y}\;} \tag{5.83-5.84}
$$

- Multi-category：$\hat{\mathbf{w}}_k=P_k^T M_k(bI+P_k P_k^T M_k)^{-1}\mathbf{y}_k$，$k=1,\dots,C$ (5.86)。
- ⭐ **Primal vs Dual 选择**：$m\ge D+1$（over-determined）用 Primal（在 $(D+1)\times(D+1)$ 求逆）；$m<D+1$（under-determined）用 Dual（在 $m\times m$ 求逆），与 Week 5 ridge regression 策略一致。

#### 2.9 Example 5.4（TER 学习示例）

- 5 个 2D 训练样本，labels $\{1,0,1,0,0\}$（imbalanced：3 个 class-0、2 个 class-1），3rd-order polynomial model。
- Python 代码用 `PolynomialFeatures(3)` 生成 $P$，`TERtrain` 函数自动选 Primal/Dual（$m\ge D$ 用 Primal，否则 Dual）。
- 测试 2 个点，预测正确率 100%。Decision boundary 在 threshold 0（one-hot encoding 隐含，不同于 Example 3 的 explicit $\tau=0.5$）。

> **考试提示**：老师强调"for quiz two and exam, use it to hand calculate these values"——需能手算小规模 TER 解。MCQ 多考概念（如 TER vs regression 在 imbalanced data 下的差异）。

### 3. ⭐ Operating Characteristics Learning：AUC Based Learning

#### 3.1 从 single threshold 到 all thresholds

- TER 在**单一** threshold $\tau$ 下优化 error rate。
- ROC curve 覆盖**所有** operating thresholds，但曲线是 range 非 scalar，不便于 optimization。
- **AUC**（Area Under ROC Curve）是自然替代：单一 scalar 值概括所有 threshold 下的 ranking 性能。

#### 3.2 AUC 的 Wilcoxon-Mann-Whitney 统计形式

定义正负样本预测值差 $\xi_{ij}=g(\mathbf{x}_i^+)-g(\mathbf{x}_j^-)$，Heaviside step function：

$$
u(\xi)=\begin{cases}1,&\xi>0\\0.5,&\xi=0\\0,&\xi<0\end{cases} \tag{5.87}
$$

$$
\text{AUC}(\mathbf{w},\mathbf{x})=\frac{1}{m^+m^-}\sum_{i=1}^{m^+}\sum_{j=1}^{m^-}u(\xi_{ij})=\frac{1}{m^+m^-}\sum_{i=1}^{m^+}\sum_{j=1}^{m^-}u\bigl(g(\mathbf{x}_i^+)-g(\mathbf{x}_j^-)\bigr) \tag{5.88}
$$

- AUC = 正负样本对中正确排序的比例（$\xi_{ij}>0$ 即 positive score > negative score）。
- 此式即 **Wilcoxon-Mann-Whitney statistic**（Week 4 已建立）。

#### 3.3 AAC（Area Above Curve）minimization

AUC 是 maximization，转为 minimization 用 **AAC**（Area Above ROC Curve）：

$$
\min_{\mathbf{w}}\text{AAC}(\mathbf{w},\mathbf{x})=\min_{\mathbf{w}}\frac{1}{m^+m^-}\sum_{i=1}^{m^+}\sum_{j=1}^{m^-}u(-\xi_{ij}) \tag{5.89}
$$

- $-\xi_{ij}>0$（即 $g(\mathbf{x}_j^-)>g(\mathbf{x}_i^+$，错误排序）时 $u=1$，计为 error。
- 与 TER 同理：step function 不可微 → 用 quadratic approximation。

#### 3.4 ⭐ AUC Quadratic Approximation + Offset

对 linear parametric predictor $g(\mathbf{x},\mathbf{w})=\mathbf{w}^T p(\mathbf{x})$，用 quadratic + offset $\eta$ + weight decay：

$$
\min_{\mathbf{w}}\text{AAC}(\mathbf{w},\mathbf{x})\approx\min_{\mathbf{w}}\left[\frac{b}{2}\|\mathbf{w}\|_2^2+\frac{1}{2m^+m^-}\sum_{i=1}^{m^+}\sum_{j=1}^{m^-}\bigl((p(\mathbf{x}_j^-)-p(\mathbf{x}_i^+))^T\mathbf{w}+\eta\bigr)^2\right] \tag{5.90}
$$

- ⭐ **与 TER 的区别**：TER 的 error 是 $g(\mathbf{x})-\tau$（单样本 vs threshold）；AUC 的 error 是 $g(\mathbf{x}_j^-)-g(\mathbf{x}_i^+)$（正负样本**对** vs 对），故 AUC 有**双重求和** $m^+\times m^-$ 项。
- $g\in[0,1]$ 时 $\xi_{ij}\in[-1,+1]$，选 $\eta=\pm 1$ 使得错排样本的 quadratic 值高于正确排样本——只用 quadratic 单臂。

#### 3.5 Offset $\eta$ 的方向选择（Fig. 3）

| $\eta$ | 效果 |
|---|---|
| $\eta=+1$ | 错排（$\xi_{ij}<0$，solid-line）的 $(-\xi_{ij}+1)^2$ **高于** 正排（dashed-line）→ 可用 |
| $\eta=-1$ | 错排的 $(-\xi_{ij}-1)^2$ **低于** 正排 → 不可用（方向反了） |

- 选对 $\eta$ 的符号使 quadratic 单臂对错排给高 penalty、正排给低 penalty。

#### 3.6 ⭐ AUC Closed-form Solution

对 (5.90) 求梯度令零，得 closed-form：

$$
\boxed{\;\hat{\mathbf{w}}=\left[bI+\frac{1}{m^+m^-}\sum_{i=1}^{m^+}\sum_{j=1}^{m^-}(p_j^- - p_i^+)(p_j^- - p_i^+)^T\right]^{-1}\left[\frac{-\eta}{m^+m^-}\sum_{i=1}^{m^+}\sum_{j=1}^{m^-}(p_j^- - p_i^+)\right]\;}
$$

$$\tag{5.91}
$$

- ⭐ 解在**单步**求得（single evaluation），least-squares optimal 但在 AUC sense。
- 预测 unseen data：$\hat{g}(\{x_1,\dots,x_n\})=P_n\hat{\mathbf{w}}$（与 regression 相同的 stacking）。
- **无 explicit threshold**：AUC 优化覆盖所有 threshold，解对所有 operating point 最优。

#### 3.7 ⭐ Optimal Threshold for TER（从 AUC 解出发）

AUC 解无 explicit threshold，但实际应用需特定 threshold。用 (5.91) 的 $\hat{\mathbf{w}}$，对 approximated TER (5.71) 关于 $\tau$ 优化：

$$
\tau=\frac{1}{2m^-}\sum_{j=1}^{m^-}\hat{\mathbf{w}}^T p_j^-+\frac{1}{2m^+}\sum_{i=1}^{m^+}\hat{\mathbf{w}}^T p_i^+ \tag{5.92}
$$

- 即正负类预测均值的**加权平均**——class-balanced 最优 threshold。
- 实际应用可据 security 需求偏移（banking 要低 FPR、手机解锁要低 FNR）。

#### 3.8 AUC vs TER vs Regression 对比

| 特性 | Regression（LSE） | TER | AUC |
|---|---|---|---|
| **优化目标** | $\|\mathbf{y}-P\mathbf{w}\|^2$（距离） | $FPR+FNR$（计数） | 正负对排序比例（ranking） |
| **threshold** | 后接（需另选） | 嵌入 formulation（固定 $\tau$） | 无 explicit（覆盖所有 $\tau$） |
| **class normalization** | 无（统一） | class-specific（$1/m^+$, $1/m^-$） | class-specific + pairwise |
| **imbalanced data** | 受密度影响（拟合密度） | 不受密度影响（只计数） | 不受密度（ranking-based） |
| **求和结构** | 单重 $\sum$ | 单重 $\sum$（按 class 分拆） | **双重** $\sum\sum$（pairwise） |
| **计算复杂度** | 低 | 中 | 高（$m^+\times m^-$ 对） |
| **closed-form** | 是 | 是 | 是 |
| **nonlinear capability** | 通过 $p(\mathbf{x})$ | 通过 $p(\mathbf{x})$ | 通过 $p(\mathbf{x})$ |

> ⭐ **TER vs Regression 在 imbalanced data 下的差异**：balanced class（$m^+=m^-$）时 TER 退化为 regression；imbalanced 时 TER 的 class-specific weighting 使决策边界不受多数类主导。Regression 拟合数据密度（多数类拉偏曲线），TER 只计数错分（与密度无关）。老师示例中 AUC/TER 的 decision boundary（蓝虚线）与 regression（绿线）不同——imbalanced 时差异明显。

### 4. A Generalized Learning Framework：Data Transformation 统一视角

> 老师口述："part four, you only need to know the **concept** wise, you don't have to know the detailed deliberation."本节只需理解全局概念：LSE/TER/AUC/FLD 等分类器可通过**简单的 data manipulation** 相互联通。

#### 4.1 Data Transformation 设定

对输入 $\mathbf{x}\in\mathbb{R}^d$，label $y\in\{0,1\}$，定义 additive linear transformation：

$$
\tilde{\mathbf{x}}=T\mathbf{x}+\mathbf{a} \tag{5.93}
$$

- $T$：$d\times d$ scaling matrix；$\mathbf{a}$：$d\times 1$ translation vector。
- 也可在 projection 空间操作：$\tilde{p}(\mathbf{x})=Tp(\mathbf{x})+\mathbf{a}$ (5.95)。
- $K$ 组不同的 $(T^k, \mathbf{a}^k)$ 产生 $m\times K$ 个变换样本 (5.94)。

#### 4.2 Transformed AUC（TAUC）

在变换空间上的 AUC learning formulation (5.98) 的 closed-form 解 $\tilde{\mathbf{w}}_{\text{TAUC}}$ (5.99) 包含三重求和（$m^+\times m^-\times K$）。

#### 4.3 ⭐ 各分类器作为 TAUC 的特例（Table 1 核心）

通过设置不同的 scaling（$\beta_1,\beta_2,\gamma_1,\gamma_2$）和 translation（$u_1,u_2,v_1,v_2$）参数，TAUC 退化为不同分类器：

| Classifier | $m^+$ | $m^-$ | $b$ | $\eta$ | $\beta_1$ | $\beta_2$ | $\gamma_1$ | $\gamma_2$ | $u_1$ | $u_2$ | $v_1$ | $v_2$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **FLD** | 1 | 1 | $b$ | 1/2 | 1 | 0 | 0 | 1 | $\boldsymbol{\mu}^+$ | 0 | 0 | $\boldsymbol{\mu}^-$ |
| **LSE** | 1 | 1 | $b$ | 1/2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| **TER** | $m^+$ | $m^-$ | $b$ | 1/2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| **AUC** | $m^+$ | $m^-$ | $b$ | 1/2 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| **Novel** | $m^+$ | $m^-$ | $b$ | 1/2 | $r$ | $r$ | $r$ | $r$ | $r$ | $r$ | $r$ | $r$ |

- $b=10^{-4}$（regularization），$r$ 为 random number（novel/g generalized classifier）。
- $\boldsymbol{\mu}^+=\frac{1}{m^+}\sum_{i=1}^{m^+}p(\mathbf{x}_i^+)$，$\boldsymbol{\mu}^-=\frac{1}{m^-}\sum_{j=1}^{m^-}p(\mathbf{x}_j^-)$（类内均值）。

**关键关系**：
- **AUC → TAUC**：当 $\beta_1=\beta_2=\gamma_1=\gamma_2=1$，$a_k=0$，TAUC (5.101) 退化为标准 AUC (5.91)。
- **TAUC → TER**：当 $K=2$，$\gamma_1=\beta_2=0$，$\beta_1=\gamma_2=1$，$a_k=0$，TAUC (5.102) 退化为 TER（除默认 $\tau=0$ 外）。
- **TAUC → FLD**：当 $b=\gamma_1=\beta_2=0$，$\beta_1=\gamma_2=1$，$\eta=1/2$，$u_2=v_1=0$，$u_1=\boldsymbol{\mu}^-$，$v_2=\boldsymbol{\mu}^+$，TAUC (5.104) 退化为 **Fisher Linear Discriminant**（FLD）。FLD 是 TER 的 centered 版本。
- **TER → LSE**：不加 regularization 时 TER (5.105) = Weighted Least Squares；Weighted-LS 与 LS 的关系已知 → AUC 在 scaling space 提供统一框架涵盖 TER / Weighted-LS / LS。

#### 4.4 与 Bayesian Inference 的关系

- TER 的 quadratic approximation 可视为 **dual-Gaussian regression**：正负两类各有 Gaussian noise $\mathcal{N}(0,\sigma_{\pm}^2)$，target 为 $y_j^-=\tau-\eta$ 和 $y_i^+=\tau+\eta$。
- Likelihood 为双 Gaussian 乘积 (5.112)，加 Gaussian prior $\mathbf{w}\sim\mathcal{N}(0,\Sigma_p)$ 得 posterior：

$$
p(\mathbf{w}|\mathbf{y},X)\sim\mathcal{N}(\bar{\mathbf{w}},\Sigma) \tag{5.109}
$$

$$
\bar{\mathbf{w}}=\left(\frac{1}{\sigma_-^2}{X^-}^T X^-+\frac{1}{\sigma_+^2}{X^+}^T X^++\Sigma_p^{-1}\right)^{-1}\left(\frac{1}{\sigma_-^2}{X^-}^T\mathbf{y}^-+\frac{1}{\sigma_+^2}{X^+}^T\mathbf{y}^+\right) \tag{5.115}
$$

- ⭐ posterior mean $\bar{\mathbf{w}}$ 与 TER solution 结构一致——TER 的 quadratic approximation 对应 Gaussian likelihood + Gaussian prior 的 MAP 估计。
- AUC 的 quadratic approximation 可视为以 pairwise data $(\mathbf{x}_j^- - \mathbf{x}_i^+)$ 为输入的 Gaussian process。

### 5. ⭐ 考点速查表

| 考点 | 要点 |
|---|---|
| **TER objective** | $TER=FPR+FNR$，class-specific normalized error count |
| **TER 变量替换** | $\varepsilon_j=g(\mathbf{x}_j^-)-\tau$，$\epsilon_i=\tau-g(\mathbf{x}_i^+)$，统一 threshold at zero |
| **Sigmoid 近似问题** | local solutions + local plateaus（非线性 w.r.t. $\mathbf{w}$） |
| **Link-loss pair** | linear link + quadratic loss → convex → closed-form |
| **Offset trick** | 加 $\eta$ 偏移 quadratic 中心，只用单臂，使 loss monotonic |
| **TER closed-form** | $[bI+\frac{1}{m^-}{P^-}^TP^-+\frac{1}{m^+}{P^+}^TP^+]^{-1}[\cdots]$，class-specific weighting |
| **TER = Weighted LS** | 本质是 class-specific weighted least squares |
| **TER vs regression** | imbalanced 时 TER 不受密度影响，regression 拟合密度 |
| **AUC objective** | Wilcoxon-Mann-Whitney statistic，正负对排序比例 |
| **AAC** | $\min\text{AAC}=\min\frac{1}{m^+m^-}\sum\sum u(-\xi_{ij})$，AUC 的 minimization 版 |
| **AUC closed-form** | pairwise $p_j^- - p_i^+$，双重求和，single evaluation |
| **AUC threshold** | 无 explicit；optimal $\tau$ via (5.92) = 加权类均值 |
| **TAUC 统一框架** | FLD/LSE/TER/AUC 均为 data transformation 特例 |
| **FLD = TER centered** | FLD 是 TER 加 class mean centering |
| **Bayesian 对应** | TER quadratic approx ≈ dual-Gaussian MAP |

### 6. 本周要点小结

- **动机**：从 regression+threshold 转为**直接优化 classification metric**（TER / AUC），避免绕道。
- **TER Learning**：用 offset $\eta$ 把 quadratic 推到单臂近似 step loss → convex → closed-form。解按 class 分拆 $P^+/P^-$，class-specific normalization $1/m^+$、$1/m^-$ → 本质 weighted LS。Primal/Dual 选择同 Week 5（选小空间求逆）。
- **AUC Learning**：用 Wilcoxon-Mann-Whitney statistic 把 AUC 表达为正负对排序比例，quadratic + offset 近似后 closed-form。双重求和 $m^+\times m^-$ 计算量大；无 explicit threshold，可用 (5.92) 求最优 TER threshold。
- **Generalized Framework**：通过 data transformation（scaling + translation），FLD / LSE / TER / AUC 都是 TAUC 的特例——**changing algorithm = changing data**。FLD 是 TER 的 centered 版本；TER 是 Weighted-LS；AUC 在 scaling space 统一三者。
- **Bayesian 对应**：TER quadratic approximation 等价于 dual-Gaussian likelihood + Gaussian prior 的 MAP 估计。
- **实践**：Python 代码（`TERtrain`/`TERtest`，Primal/Dual 自动选择）；手算小规模示例用于 quiz/exam；imbalanced data 下 TER/AUC 优于 regression。

---

> **下周（Week 7）预告**：本周未讲完 Part 4（Generalized Framework 的 data transformation 细节），老师明确说"next week we have a bit of time, we can continue remaining just a few more slides"。预计 Week 7 补完 TAUC/FLD/LSE 关系的剩余 slides 后进入 **Lecture 7 — Analytic Methods for Penalized Learning**（Toh 的 Part 1 收尾段，penalized/regularized learning 的解析方法，对应课程大纲 L7）。本周的 TER/AUC closed-form 解与 quadratic approximation 是直接前置。具体以 Lecture 7 课件为准。

---

## Week 7 — Lecture 6 收尾（TAUC Generalized Framework）+ Lecture 7: Analytic Methods for Penalized Learning

> **材料**：转写 `week7/week7.txt`（ASR 噪声多），官方课件 `week7/EE6406-Lecture7-TKA-v1.pdf`（权威，67 slides）。本周前半补完 Lecture 6 末尾的 generalized framework（TAUC → AUC/TER/FLD/Regression 的 data transformation 关系），后半正式进入 Lecture 7。
>
> **CA2 重要通知**（转写开头）：CA2 在 **Week 8（recess week 后两周）** 举行，online quiz 形式，与 CA1 相同规则（lockdown browser，closed-book，in-class）。**CA2 占 15%**（比 CA1 的 10% 高），final exam 60%。**CA2 考试范围：Lecture 5–7**（regression/classification learning methods + penalized learning），concept 为主 + 少量 basic calculation（参考 lecture slides 的 examples，不需做书末难题）。Week 9 起 **Simon Liu** 接手 Ensemble Learning 部分，CA3 在 Week 12。

### 0. ⭐ CA2 考试信息（Week 8，recess 后）

| 项目 | 详情 |
|---|---|
| **时间** | Week 8（recess week 后，即本周后两周） |
| **占比** | **15%**（CA1=10%, CA2=15%, CA3=15%, Final=60%） |
| **范围** | **Lecture 5–7**：L5 regression learning、L6 TER/AUC learning、L7 penalized learning |
| **形式** | online quiz，in-class，lockdown browser，closed-book |
| **题型** | concept 为主 + basic calculation（类似 CA1），不做书末复杂计算题 |
| **准备** | 重点 lecture slides 中的 examples + 书中基础练习；recess week 有较多准备时间 |

- 转写中 TKA 原话："concept holds more mass than calculations, similar to CA one"——概念题占比高于计算题。
- "do some practice based on those examples given in the lecture slides, and also those behind the book would be enough, but don't worry about those computational or more difficult problems"——以 slides 上的 example 和书后基础题为主，不做复杂计算。

---

### 1. Lecture 6 收尾：TAUC Generalized Framework 补完

> 上周（Week 6）已记录 TAUC 的统一框架与 Table 1（FLD/LSE/TER/AUC 作为 TAUC 特例）。本周开头的转写补完了 data transformation 的直觉和 TAUC → AUC/TER/FLD 的参数退化路径，以及 Bayesian 对应关系。以下为补充要点。

#### 1.1 Data Transformation 的直觉

- **核心思想**："changing algorithm = changing data"——通过 data manipulation（scaling、translation、duplication）改变数据，使不同分类器的解可以统一在 TAUC 框架下。
- **两层变换**：
  1. **Feature 变换** $p(\mathbf{x})$：如 polynomial 或 kernel transformation（Lecture 3/5 已述）。
  2. **Data 变换** $\tilde{p}=Tp+\mathbf{a}$：$T$ 为 scaling matrix，$\mathbf{a}$ 为 translation vector；可 duplicate 数据 $K$ 组（不同 $(T^k,\mathbf{a}^k)$），扩大训练池。
- **动机**：更多变换数据 → 更多 training restriction → 更好 generalization（类似 data augmentation / noise injection 的思想）。

#### 1.2 ⭐ TAUC → 各分类器的退化路径

| 退化路径 | 操作 | 结果 |
|---|---|---|
| **TAUC → AUC** | 令 $T=I$（identity），$\mathbf{a}=0$（无 translation），或令 $\beta_1=\beta_2=\gamma_1=\gamma_2=1$ | 回到标准 AUC |
| **TAUC → TER** | 通过设置部分 $\beta,\gamma=0$，移除一个 summation（double→single） | 双重求和退化为单重求和 → TER |
| **TAUC → FLD** | 在 TER 基础上加 mean-centering：$u_1=\boldsymbol{\mu}^-$, $v_2=\boldsymbol{\mu}^+$ | FLD = centered TER |
| **TER → Regression** | 加权合并 $m^+,m^-$ → weighted LS | TER = class-specific weighted least squares |
| **Regression → Bayesian MLE** | Gaussian likelihood + Gaussian prior | MAP = regularized regression |

- ⭐ **关键概念**：$\beta,\gamma$ 控制 scaling（乘或不乘），$u,v$ 控制 translation（mean-centering 或不 centering）。设置不同的 $\beta,\gamma,u,v$ 值即可在 AUC/TER/FLD/Regression 之间转换——"like a periodic table, we link up everything together"。
- **FLD vs TER**：FLD 是 TER 的 **mean-centered** 版本——数据减去类均值后做同样的 TER。结果几乎相同，仅差 centering offset。
- **TER vs Regression**：TER 是 class-specific weighted LS（$m^+/m^-$ weighting）；regression 是单一 Gaussian 假设下的 MLE。

#### 1.3 ⭐ Bayesian 对应（补充 Week 6 内容）

- **Regression ↔ single Gaussian MLE**：线性 regression 的 closed-form 解等价于假设所有 noise 为 $\mathcal{N}(0,\sigma^2)$ 的 maximum likelihood 估计。covariance 矩阵中的 regularization diagonal 项对应 Gaussian prior。
- **TER ↔ dual-Gaussian MAP**：TER 把正负两类分开，每类用一组 Gaussian noise $\mathcal{N}(0,\sigma_\pm^2)$，target 分别为 $\tau\pm\eta$。likelihood 为两组 Gaussian 乘积 → 加 Gaussian prior $\mathbf{w}\sim\mathcal{N}(0,\Sigma_p)$ → posterior mean $\bar{\mathbf{w}}$ 结构与 TER solution 一致。
- **AUC ↔ pairwise Gaussian process**：AUC 的 quadratic approximation 可视为以 pairwise data $(p_j^- - p_i^+)$ 为输入的 Gaussian process。

---

### 2. Lecture 7 Introduction：Penalized Learning 的动机

#### 2.1 What Is Penalized Learning?

Penalized learning（惩罚学习）是在学习目标中添加 penalty term 的建模框架，目标是平衡 data fit 与 model complexity：

$$
\min_\theta\;L(\theta)+\lambda P(\theta) \tag{7.1}
$$

完整的学习目标（learning components）：

$$
\arg\min_\mathbf{w}\;J(\mathbf{w})=\arg\min_\mathbf{w}\left[\sum_{i=1}^m L\bigl(g(\mathbf{x}_i,\mathbf{w}),y_i\bigr)+\lambda R(\mathbf{w})\right] \tag{7.2}
$$

| 符号 | 含义 |
|---|---|
| $J(\mathbf{w})$ | Learning cost function（optimization criterion） |
| $L(\cdot)$ | Loss function |
| $g(\mathbf{x}_i,\mathbf{w})$ | Learning model |
| $\mathbf{x}_i$ | Learning model input vector |
| $\mathbf{w}$ | Learning parameter vector |
| $y_i$ | Learning target |
| $m$ | Sample size |
| $R(\mathbf{w})$ | Regularization function |
| $\lambda$ | Regularization factor |

#### 2.2 ⭐ Why Do We Need Penalization?

- **Overfitting**：仅最小化 training error 会导致 overfitting——复杂模型拟合 noise 而非 structure。
- 特别在 **under-determined system**（参数多于数据，$m<D+1$）时，训练误差可降到零，但对 unseen data 预测极差。
- **Penalization = regularization**：限制参数大小 → 更好 generalization（泛化能力）。
- **Overfitting vs Regularization 示意图**：
  - Training error 随 model complexity 单调下降（可到零）。
  - Test error 先降后升，在 **optimal complexity** 处最低。
  - Penalization 鼓励模型停留在 optimal complexity 附近。
- ⭐ **稳定性直觉**（转写补充）：参数值大 → $\mathbf{w}^T p(\mathbf{x})$ 对 $p$ 的微小变化敏感 → 输出 swing 大；参数值小 → 输出稳定。"data change quite smoothly, like temperature, it will not suddenly go to 1000 degrees"——penalization 使预测不剧烈波动。

#### 2.3 三大应用

**Application 1: Penalized Linear Regression**

| 方法 | Penalty | 特点 |
|---|---|---|
| **Ridge regression** | $L_2$: $\|\mathbf{w}\|_2^2$ | 所有系数均匀缩小，不压到零 |
| **LASSO** | $L_1$: $\|\mathbf{w}\|_1$ | 系数可压到零 → feature selection |
| **Bridge regression** | $L_p$: $\|\mathbf{w}\|_p^p$ | $p$ 在 0–2 之间，generalization of Ridge/LASSO |

- **$L_1$ vs $L_2$ geometry**：$L_2$ penalty 的 constraint region 是圆球（smooth），$L_1$ 是菱形（有 sharp corners）。cost function 的等高线与 $L_1$ 的 corner 相交时，部分系数恰为零 → sparsity。

**Application 2: Feature Selection**

- 高维数据（genomics、text mining、finance）中，$L_1$ penalization 鼓励 sparse solution → automatic feature selection + interpretability。
- 只有少数 feature 的系数非零，其余被压零。

**Application 3: Neural Networks and Inverse Problems**

- Neural network 的 **weight decay** 就是 $L_2$ penalization，防止 overfitting。
- Inverse problem（逆问题）依赖 penalty 保证 stable solution（矩阵可能 singular，需 regularization）。
- Penalization 可将 prior knowledge 融入学习。

#### 2.4 Key Takeaways

- Penalized learning 扩展了 standard empirical risk minimization。
- 控制 complexity → 改善 generalization。
- 支持 sparsity、stability、interpretability。
- 现代统计学习的 foundational concept。

---

### 3. Coefficient Shrinkage：Regularization 与 Least-Norm 两种途径

#### 3.1 两种 problem formulation

Coefficient shrinkage（系数收缩）可通过两种对偶的 formulation 实现：

| 途径 | Formulation | 名称 |
|---|---|---|
| **Regularization approach**（primal） | $\min_\mathbf{w}\;\text{SSE}$ subject to $\|\mathbf{w}\|_2^2\le t$ | Penalized learning / regularization |
| **Least-norm approach**（dual） | $\min_\mathbf{w}\;\|\mathbf{w}\|_2^2$ subject to $\mathbf{y}=P\mathbf{w}$ | Minimum-norm solution |

- 两者本质上是对偶的：一个以 error 为主目标、norm 为约束，另一个以 norm 为主目标、error 为约束。
- ⭐ **Primal** 对应 **over-determined system**（$m>D+1$），**Dual** 对应 **under-determined system**（$m<D+1$）——与 Lecture 3/5 的 primal/dual regression 一致。

#### 3.2 Regularization Approach（Primal）

**Ridge regression**（$L_2$ penalty）：

$$
J_{\text{SSE}_r}(\mathbf{w})=\frac{1}{2}\sum_{i=1}^m\bigl(y_i-\mathbf{p}_i^T\mathbf{w}\bigr)^2+\frac{\lambda}{2}\|\mathbf{w}\|_2^2 \tag{6.1}
$$

- 等价于：minimize SSE subject to $\|\mathbf{w}\|_2^2\le t$, $t\in\mathbb{R}^+$。
- $\lambda$ 是 regularization factor，控制 error term 与 weight term 的权重。

**LASSO**（$L_1$ penalty）：

$$
J_{\text{lasso}}(\mathbf{w})=\sum_{i=1}^m\bigl(y_i-\mathbf{p}_i^T\mathbf{w}\bigr)^2+\lambda\|\mathbf{w}\|_1 \tag{6.2}
$$

- $\|\mathbf{w}\|_1=\sum_{j=0}^D|w_j|$。
- 等价于：minimize SSE subject to $\|\mathbf{w}\|_1\le c$, $c\in\mathbb{R}^+$。
- ⭐ $L_1$ penalty 有 sharp corners（菱形 constraint），解倾向于落在角上 → 部分系数恰为零 → feature selection。

**Bridge regression**（$L_p$ penalty，generalization）：

$$
\text{SSE}_{\text{bridge}}(\mathbf{w})=\sum_{i=1}^m\bigl(y_i-\mathbf{p}_i^T\mathbf{w}\bigr)^2+\lambda\|\mathbf{w}\|_p^p \tag{6.4}
$$

$$
\|\mathbf{w}\|_p=\left(\sum_{j=0}^D|w_j|^p\right)^{1/p} \tag{6.3}
$$

- $0\le p<2$ 是关注范围：
  - $0\le p\le 1$：parametric subset selection，部分系数压到零。
  - $1<p<2$：parametric compression（缩小但不一定到零）。
- $p=2$ → Ridge；$p=1$ → LASSO；$p\to 0$ → pure subset selection（只选不压缩）。

#### 3.3 Least-Norm Approach（Dual）

将参数 norm 作为主目标：

$$
\min_\mathbf{w}\;\|\mathbf{w}\|_2^2 \quad\text{subject to}\quad \mathbf{y}-P\mathbf{w}=0 \tag{6.5}
$$

解析解（right pseudoinverse）：

$$
\hat{\mathbf{w}}=P^T(PP^T)^{-1}\mathbf{y} \tag{6.6}
$$

- 当 $PP^T$ non-singular 时成立。
- ⭐ 这里 $P^T(PP^T)^{-1}$ 是 **right pseudoinverse**，取代了 LSE 的 left pseudoinverse $(P^TP)^{-1}P^T$。
- 适用于 **under-determined system**（$m<D+1$）。

推广到 $L_p$ norm：

$$
\min_\mathbf{w}\;\|\mathbf{w}\|_p^p \quad\text{subject to}\quad \mathbf{y}-P\mathbf{w}=0 \tag{6.7}
$$

Lagrangian form：

$$
\min_\mathbf{w}\;\|\mathbf{w}\|_p^p+\boldsymbol{\alpha}^T(\mathbf{y}-P\mathbf{w}) \tag{6.8}
$$

- $\boldsymbol{\alpha}$ 是 Lagrange multipliers，每个对应一个 data sample。
- ⭐ 这里的 $\boldsymbol{\alpha}$ 与 Lecture 5 under-determined system 中的 dual variable 结构一致。

---

### 4. Ridge Regression：Primal 与 Dual 推导

#### 4.1 回顾（Lecture 5 结果）

$$
\text{Primal ridge:}\quad\hat{\mathbf{w}}=(P^TP+\lambda I)^{-1}P^T\mathbf{y},\;\lambda>0 \tag{6.9}
$$

$$
\text{Dual ridge:}\quad\hat{\mathbf{w}}=P^T(PP^T+\lambda I)^{-1}\mathbf{y},\;\lambda>0 \tag{6.10}
$$

#### 4.2 ⭐ Dual Ridge 的 Lagrangian 推导（从 constrained optimization 出发）

**出发点**（least-norm formulation）：

$$
\min_\mathbf{w}\;\|\mathbf{w}\|_2^2 \quad\text{subject to}\quad \mathbf{y}=P\mathbf{w} \tag{6.12}
$$

**Step 1**：Lagrangian form（引入 Lagrange multipliers $\boldsymbol{\alpha}$）：

$$
\min_\mathbf{w}\;\frac{1}{2}\|\mathbf{w}\|_2^2+\boldsymbol{\alpha}^T(\mathbf{y}-P\mathbf{w}) \tag{6.13}
$$

**Step 2**：对 $\mathbf{w}$ 求导令零：

$$
\mathbf{w}=P^T\boldsymbol{\alpha} \tag{6.14}
$$

**Step 3**：代入 (6.13) 消去 $\mathbf{w}$，加入 $\boldsymbol{\alpha}$ 的 norm term（sign 可任意，因 $y-Pw=0$ 或 $Pw-y=0$ 均可）：

$$
\min_\boldsymbol{\alpha}\;\frac{1}{2}\boldsymbol{\alpha}^T PP^T\boldsymbol{\alpha}+\boldsymbol{\alpha}^T(\mathbf{y}-PP^T\boldsymbol{\alpha})-\frac{\lambda}{2}\boldsymbol{\alpha}^T\boldsymbol{\alpha} \tag{6.16}
$$

**Step 4**：对 $\boldsymbol{\alpha}$ 求导令零：

$$
PP^T\boldsymbol{\alpha}+\mathbf{y}-2PP^T\boldsymbol{\alpha}-\lambda\boldsymbol{\alpha}=0$$
$$\mathbf{y}=(PP^T+\lambda I)\boldsymbol{\alpha}$$
$$\hat{\boldsymbol{\alpha}}=(PP^T+\lambda I)^{-1}\mathbf{y},\;\lambda>0 \tag{6.17}
$$

**Step 5**：代回 (6.14)：

$$
\hat{\mathbf{w}}=P^T(PP^T+\lambda I)^{-1}\mathbf{y}
$$

即 dual ridge regression (6.10)。

#### 4.3 ⭐ 放松精确拟合假设（Error Term Formulation）

**问题**：(6.12) 要求 $\mathbf{y}=P\mathbf{w}$ 精确成立，实际中模型不可能完美拟合。放松为：

$$
\min_\mathbf{w}\;\|\mathbf{w}\|_2^2+\gamma\|\boldsymbol{\epsilon}\|_2^2 \quad\text{subject to}\quad \mathbf{y}=P\mathbf{w}+\boldsymbol{\epsilon},\;\gamma>0 \tag{6.18}
$$

- 引入 error term $\boldsymbol{\epsilon}$ 吸收 model inaccuracy。

**Lagrangian**：

$$
J(\mathbf{w},\boldsymbol{\alpha},\boldsymbol{\epsilon})=\mathbf{w}^T\mathbf{w}+\gamma\boldsymbol{\epsilon}^T\boldsymbol{\epsilon}+\boldsymbol{\alpha}^T(\mathbf{y}-P\mathbf{w}-\boldsymbol{\epsilon}) \tag{6.19}
$$

**推导步骤**（三步消元）：

1. 对 $\mathbf{w}$ 求导 → $\mathbf{w}=\frac{1}{2}P^T\boldsymbol{\alpha}$ (6.20)
2. 代入消 $\mathbf{w}$ → 对 $\boldsymbol{\epsilon}$ 求导 → $\boldsymbol{\epsilon}=\frac{1}{2\gamma}\boldsymbol{\alpha}$ (6.22)
3. 代入消 $\boldsymbol{\epsilon}$ → 对 $\boldsymbol{\alpha}$ 求导：

$$
\hat{\boldsymbol{\alpha}}=\frac{1}{2}(PP^T+\lambda I)^{-1}\mathbf{y},\quad\lambda=\frac{1}{\gamma},\;\gamma>0 \tag{6.24}
$$

代回 (6.20)：

$$
\hat{\mathbf{w}}=P^T(PP^T+\lambda I)^{-1}\mathbf{y},\quad\lambda=\frac{1}{\gamma},\;\gamma>0 \tag{6.25}
$$

⭐ **结论**：即使放松精确拟合假设（加入 error term），最终仍得到相同的 dual ridge regression 解，只是 $\lambda=1/\gamma$。说明 ridge regression 解对 model imperfection 具有鲁棒性——"no matter how you start off, it goes back to the same solution"。

- **实践意义**：(6.18) 的 formulation 更合理（不假设模型完美），但推导结果与 (6.12) 一致 → ridge regression 是 robust 的。

---

### 5. Bridge Regression：$L_p$ Norm 的解析方法

#### 5.1 ⭐ Smooth 近似：k-measure Operator

**问题**：$L_p$ norm 的绝对值 $|w_j|$ 在 $w_j=0$ 处不可微，无法直接求导。

**解决**：用 smooth approximation 替换绝对值：

$$
f(w_i)=\sqrt{w_i^2+\epsilon},\quad\epsilon>0\;\text{small}
$$

$$
|o\;\mathbf{w}\;o|_k:=\left(\sum_{j=0}^{D-1}f(w_j)^k\right)^{1/k} \tag{6.27}
$$

- $\lim_{\epsilon\to 0}f(w_i)=|w_i|$，即近似随 $\epsilon\to 0$ 趋于精确。
- ⭐ $|o\cdot o|_k$ 不构成 normed vector space（违反 absolute homogeneity axiom），故称为 **k-measure operator** 而非 norm。
- **Contour plots 对比**（Fig. 8）：
  - $p$-norm contour（top row）：$p=2$ → 圆，$p=1$ → 菱形，$p<1$ → 内凹星形。
  - $k$-measure contour（bottom row）：smooth 近似，形状相似但角圆滑。

| $p$ / $k$ 值 | Contour 形状 | 特性 |
|---|---|---|
| $p=2$ | 圆（smooth） | Ridge，无 sparsity，均匀缩小 |
| $p=1$ | 菱形（sharp corners） | LASSO，解在角上 → sparsity |
| $p<1$ | 星形（更尖锐） | 更强 sparsity，纯 subset selection |
| $1<p<2$ | 圆与菱形之间 | compression，部分系数缩小但不为零 |

⭐ **Sparsity 规律**（转写重点强调）：
- $p\le 1$：解倾向于落在 corner/axis 上 → feature selection（部分系数恰为零）。
- $p>1$：contour smooth 无角 → 系数被不等程度缩小但不到零 → compression only。
- $p=2$：完全对称，所有维度等概率缩小，无 sparsity。

#### 5.2 Proximal Bridge Regression — Primal Form（Over-determined）

对 $m>D+1$（over-determined system）：

$$
J(\mathbf{w})=(\mathbf{y}-P\mathbf{w})^T(\mathbf{y}-P\mathbf{w})+\lambda|o\;\mathbf{w}\;o|_k^k \tag{6.28}
$$

**解**：

$$
\hat{\mathbf{w}}=\left[\frac{\lambda k}{2}\text{diag}\{|\mathbf{w}|\circ(k-2)\}+P^TP\right]^{-1}P^T\mathbf{y} \tag{6.29}
$$

- $\circ$ 表示 element-wise operator（如 $A\circ k$ 表示对 $A$ 的每个元素取 $k$ 次幂）。
- $\text{diag}(\mathbf{a})$ 表示以 $\mathbf{a}$ 为对角线的对角矩阵。
- ⭐ **注意**：此解中 $\mathbf{w}$ 出现在等式两边（$|\mathbf{w}|\circ(k-2)$），需 **迭代求解**：先用初始 $\mathbf{w}$ 代入，计算新的 $\hat{\mathbf{w}}$，再循环。通常 **4–5 次迭代** 即可收敛。
- 当 $\frac{\lambda k}{2}\text{diag}\{|\mathbf{w}|\circ(k-2)\}+P^TP$ non-singular 时成立。
- **Reference**：K.-A. Toh, G. Molteni, Z. Lin, "Deterministic bridge regression for compressive classification", *Information Sciences*, vol. 648, pp. 1–22, Nov 2023.

#### 5.3 Proximal Bridge Regression — Dual Form（Under-determined）

对 $m<D+1$（under-determined system）：

$$
\min_\mathbf{w}\;|o\;\mathbf{w}\;o|_k^k \quad\text{subject to}\quad \mathbf{y}=P\mathbf{w} \tag{6.30}
$$

Lagrangian form：

$$
\min_\mathbf{w}\;|o\;\mathbf{w}\;o|_k^k+\boldsymbol{\beta}^T(\mathbf{y}-P\mathbf{w}) \tag{6.31}
$$

**解**：

$$
\hat{\mathbf{w}}=\text{sgn}(\boldsymbol{\theta})\circ\left[P^T(PP^T)^{-1}P\boldsymbol{\theta}\circ(k-1)\right]^{1/(k-1)} \tag{6.32}
$$

其中：

$$
\hat{\boldsymbol{\theta}}=\left[|P^T|\circ(k-1)\;P|P^T|\circ(k-1)\right]^{-1}\mathbf{y} \tag{6.33}
$$

- ⭐ **Dual form 是真正的 closed-form**：一旦知道 $P$ 即可计算 $\boldsymbol{\theta}$，取 sign，代幂运算，无需迭代（不像 primal form 需要 4–5 次迭代）。
- $1<k\le 2$ 时有效（under-determined case 中 $k$ 不能等于 1，否则不可逆）。
- $\text{sgn}(\cdot)$ 为 sign function，$\circ$ 为 element-wise 运算。

#### 5.4 ⭐ Primal vs Dual Bridge 对比

| 特性 | Primal p-bridge | Dual p-bridge |
|---|---|---|
| **系统类型** | Over-determined（$m>D+1$） | Under-determined（$m<D+1$） |
| **$k$ 取值** | $k$ 可取 1（$=1$ 时类似 LASSO） | $k$ 必须 $>1$（$k=1$ 不可逆） |
| **求解方式** | **迭代**（4–5 次收敛） | **Closed-form**（单步计算） |
| **矩阵求逆** | $(D+1)\times(D+1)$ | $m\times m$ |
| **适用场景** | 样本多于参数 | 参数多于样本（高维稀疏） |

#### 5.5 Multiple Outputs 扩展

当有 $C$ 个独立输出 $\{\mathbf{y}_1,\dots,\mathbf{y}_C\}$，且各输出独立时，可将各输出的解 stacked：

- **Primal**（over-determined）：

$$
\hat{\mathbf{w}}_l=\left[\frac{\lambda k}{2}\text{diag}\{|\mathbf{w}_l|\circ(k-2)\}+P^TP\right]^{-1}P^T\mathbf{y}_l,\quad l=1,\dots,C \tag{6.34}
$$

- **Dual**（under-determined）：

$$
\hat{\mathbf{w}}_l=\text{sgn}(\hat{\boldsymbol{\theta}}_l)\circ\left[P^T(PP^T)^{-1}P\hat{\boldsymbol{\theta}}_l\circ(k-1)\right]^{1/(k-1)},\quad l=1,\dots,C \tag{6.35}
$$

- $\hat{W}=[\hat{\mathbf{w}}_1,\dots,\hat{\mathbf{w}}_C]$，预测 $\hat{G}=P\hat{W}$。
- 假设各输出独立 → 同一 regressor matrix $P$ 可复用，与 least squares 的 multi-output stacking 方法一致。

---

### 6. Coefficient Profiles：实验示例

#### 6.1 ⭐ Example 6.1：Polynomial Fitting with p-bridge（Over-determined）

- **数据**：16 个 training samples，单输入 $x$，target $y=10x^2-x^3$。
- **模型**：10th-order polynomial（含 intercept，共 11 个参数）。
- **设置**：$\lambda=1$, $k=1.1$（接近 LASSO）。
- **结果**：$\hat{\mathbf{w}}\approx[0.017, 0, 9.944, -0.978, 0.009, -0.001, -0.0004, 0.0001, 0, 0, 0]^T$
  - ⭐ 仅 $x^2$（$\approx 9.94$）和 $x^3$（$\approx -0.98$）的系数显著非零，其余被压到接近零。
  - 完美恢复真实模型 $y=10x^2-x^3$ → **bridge regression 的 compressive classification 能力**。
- **Python 代码要点**：
  ```python
  P = np.hstack([x ** i for i in range(11)])  # polynomial features
  w = pbridge(P, y, k, lambda_, Primal)       # Primal=1 for over-determined
  y_est = PP @ w  # prediction
  ```

#### 6.2 ⭐ Example 6.2：Prostate Cancer Data（Over-determined）

- **数据集**：67 training samples，30 test samples，8 input variables + intercept = 9 coefficients。
- **系统类型**：over-determined（$m=67 > D+1=9$）。
- **Coefficient profiles**：随 $\lambda$ 变化的系数轨迹，以 effective degrees of freedom $df(\lambda)=\text{tr}[P(P^TP+\lambda I)^{-1}P^T]$ 为横轴。
  - **Ridge**（Fig. 10）：所有系数渐变缩小，无一提前到零。
  - **p-bridge at $k=1$**（Fig. 11a）：类似 LASSO，系数逐个到零（gleason、lcp 先被淘汰）。
  - **LASSO**（Fig. 11b）：与 p-bridge $k=1$ 形状相似（log scale plotting）。

**Prediction 结果对比**（Table 1）：

| Method | Tuned Parameter(s) | Test MSE | Variables Selected |
|---|---|---|---|
| OLS | – | 0.520 (0.174) | All |
| Ridge regression | $\lambda=1$ | 0.516 (0.175) | All |
| LASSO (Alpha=1) | $\lambda=0.02$ | **0.483 (0.160)** | (1,2,3,4,5,6,8) |
| Elastic-net | $\lambda=0.06$, $\alpha=0.11$ | 0.492 (0.164) | (1,2,3,4,5,6,8) |
| p-bridge ($k=1$) | $\lambda=2$ | 0.494 (0.167) | (1,2,3,4,5,6,8) |

- ⭐ **关键观察**：
  - LASSO 最低 MSE（0.483），p-bridge 次之（0.494），均优于 OLS（0.520）和 Ridge（0.516）。
  - LASSO、elastic-net、p-bridge 都选了相同的 7 个变量（排除 variable 7 = gleason）。
  - Ridge 和 OLS 保留所有变量（Ridge 无 sparsity）。
  - **最重要变量**：lcavol（最后才被压零）；**最不重要**：gleason、lcp（最早到零）。

#### 6.3 ⭐ Example 6.3：XOR Problem（Under-determined）

- **数据**：XOR 的 4 个 training points $(x_1,x_2)\in\{(0,1),(2,1),(1,0),(1,2)\}$，$y\in\{0,0,1,1\}$。
- **模型**：3rd-order polynomial，10 个参数（$\alpha_0,\dots,\alpha_9$）→ under-determined（$m=4<D+1=10$）。
- **Test data**：200 samples，4 个 Gaussian 中心（各 50 samples，identity covariance × 0.3）。

**Coefficient profiles**：

| Method | 特点 |
|---|---|
| **Kernel ridge** ($k=2$, Fig. 12) | 所有系数渐变缩小，无 sparsity |
| **Dual p-bridge** ($k=1.05$, Fig. 13a) | ⭐ 仅 $x_1^3$（$\alpha_6$）和 $x_2^3$（$\alpha_7$）存活，其余快速到零 |
| **LASSO** (Fig. 13b) | $x_1, x_2$ 也存活较久，但最终 $x_1^3, x_2^3$ 最重要 |

**Prediction 结果**（Table 3）：

| Method | Tuned Parameter(s) | Test MSE | Variables Selected |
|---|---|---|---|
| OLS | – | 0.513 (0.089) | All |
| Ridge | $\lambda=6$ | 0.503 (0.047) | (0,1,2,3,4,6,7,8,9) |
| LASSO ($\alpha=1,\lambda=0.1$) | – | **0.225 (0.011)** | (0,6,7) |
| Elastic-net | $\lambda=0,\alpha=0.01$ | 0.799 (0.189) | All |
| p-bridge ($k=1.05$) | $\lambda=30$ | 0.504 (0.040) | (6,7) |
| p-bridge | $\lambda=0,k=2$ | 0.513 (0.089) | All |

- ⭐ **Dual p-bridge** 选取最少变量（仅 $\alpha_6=x_1^3$, $\alpha_7=x_2^3$），对应 XOR 的三阶项——最 sparse 解。
- LASSO 的 MSE 最低（0.225），但保留了 intercept（$\alpha_0$）；p-bridge 更 sparse（仅 2 项）但 MSE 稍高。
- **Decision contours**（Fig. 14）：dual p-bridge 和 LASSO 的决策边界高度相似，都主要依赖 $x_1^3, x_2^3$。

#### 6.4 ⭐ p-bridge vs LASSO 总结

| 对比维度 | p-bridge | LASSO |
|---|---|---|
| **求解方式** | Primal: 迭代 4–5 次；Dual: closed-form | 数值优化（coordinate descent 等） |
| **Under-determined $k$ 限制** | $k>1$（$k=1$ 不可逆） | 无限制 |
| **Sparsity** | $k$ 接近 1 时高度 sparse | $L_1$ 天然 sparse |
| **计算效率** | 高维时矩阵求逆开销大 | 通常更高效（MATLAB glmnet） |
| **MSE** | 略高于 LASSO | 通常最低 |

---

### 7. ⭐ 考点速查表

| 考点 | 要点 |
|---|---|
| **Penalized learning 一般形式** | $\min_\theta L(\theta)+\lambda P(\theta)$，balance data fit 与 model complexity |
| **Overfitting 动机** | training error 可到零（under-determined），test error 先降后升 |
| **$L_1$ vs $L_2$ geometry** | $L_1$ 菱形有角 → sparsity；$L_2$ 圆球 → uniform shrinkage |
| **Ridge primal 解** | $(P^TP+\lambda I)^{-1}P^T\mathbf{y}$ |
| **Ridge dual 解** | $P^T(PP^T+\lambda I)^{-1}\mathbf{y}$ |
| **Dual ridge 推导** | Lagrangian → $\mathbf{w}=P^T\boldsymbol{\alpha}$ → 对 $\boldsymbol{\alpha}$ 求导 → $(PP^T+\lambda I)\hat{\boldsymbol{\alpha}}=\mathbf{y}$ |
| **Error term relaxation** | $\mathbf{y}=P\mathbf{w}+\boldsymbol{\epsilon}$ → 同样的 dual ridge 解，$\lambda=1/\gamma$ |
| **Least-norm solution** | $P^T(PP^T)^{-1}\mathbf{y}$，right pseudoinverse，under-determined |
| **Bridge regression** | $L_p$ norm，$0<p<2$；$p\le1$ → subset selection；$1<p<2$ → compression |
| **k-measure operator** | $|o\mathbf{w}o|_k$，$f(w_i)=\sqrt{w_i^2+\epsilon}$ smooth 近似，非真 norm |
| **Primal p-bridge 解** | 迭代求解，$[\frac{\lambda k}{2}\text{diag}\{|\mathbf{w}|\circ(k-2)\}+P^TP]^{-1}P^T\mathbf{y}$ |
| **Dual p-bridge 解** | closed-form，$\text{sgn}(\boldsymbol{\theta})\circ[\cdots]^{1/(k-1)}$，$k>1$ |
| **$k$ 取值限制** | Primal: $k$ 可取 1；Dual: $k$ 必须 $>1$ |
| **Sparsity 规律** | $p\le1$ → sparse（corner solution）；$p>1$ → compression only；$p=2$ → no sparsity |
| **Example 6.1** | 10th-order poly + p-bridge $k=1.1$ → 仅 $x^2,x^3$ 存活，恢复 $y=10x^2-x^3$ |
| **Prostate example** | Over-determined；LASSO MSE 最低；p-bridge 与 LASSO 选相同变量 |
| **XOR example** | Under-determined；dual p-bridge 仅选 $x_1^3,x_2^3$（最 sparse） |
| **Effective $df$** | $df(\lambda)=\text{tr}[P(P^TP+\lambda I)^{-1}P^T]$，$\lambda$ 越大 $df$ 越小 |
| **Primal/Dual 选择** | Over-determined → Primal（$P^TP$，$D+1$ 维求逆）；Under-determined → Dual（$PP^T$，$m$ 维求逆） |

---

### 8. 本周要点小结

- **Lecture 6 收尾**：TAUC generalized framework 通过 data transformation（scaling $\beta,\gamma$ + translation $u,v$）统一了 AUC/TER/FLD/Regression——"changing algorithm = changing data"。FLD = centered TER，TER = weighted LS，Regression = single-Gaussian MLE，TER = dual-Gaussian MAP。不需记复杂公式，重点是 data manipulation 的概念和各方法间的退化关系。

- **Lecture 7 核心概念**：
  - **Penalized learning** = data fit + penalty term，平衡 model complexity 与 generalization。
  - **两种 formulation**：Regularization approach（primal，min SSE s.t. $\|\mathbf{w}\|\le t$）与 Least-norm approach（dual，min $\|\mathbf{w}\|$ s.t. $\mathbf{y}=P\mathbf{w}$），两者对偶。
  - **Ridge regression**（$L_2$）：primal $(P^TP+\lambda I)^{-1}P^T\mathbf{y}$，dual $P^T(PP^T+\lambda I)^{-1}\mathbf{y}$。Dual 推导通过 Lagrangian + 消元。放松精确拟合假设后解不变（$\lambda=1/\gamma$）。
  - **Bridge regression**（$L_p$）：用 k-measure operator 做 smooth 近似。Primal 需迭代 4–5 次；Dual 为 closed-form。$k\le1$ → sparsity（feature selection），$1<k<2$ → compression，$k=2$ → Ridge（无 sparsity）。
  - **$L_1$ vs $L_2$**：$L_1$（LASSO）菱形有角 → sparse solution；$L_2$（Ridge）圆球 → uniform shrinkage，无 sparsity。
  - **实验验证**：Example 6.1（polynomial）恢复真实模型；Prostate（over-determined）中 LASSO/p-bridge 选相同变量且 MSE 优于 OLS/Ridge；XOR（under-determined）中 dual p-bridge 最 sparse（仅 $x_1^3,x_2^3$）。

- **考试重点**（CA2）：concept 为主（$L_1$ vs $L_2$ 特性、sparsity 规律、primal/dual 选择、over/under-determined 判断）+ basic calculation（ridge regression 解、dimension 判断、coefficient profile 解读）。不需推导 bridge regression 公式，但需知道 form 和功能。

---

### 下一周预告

> **Week 8 = Lecture 8 + CA2 Quiz**。CA2 在 Week 8 课上举行（recess week 后），范围 Lecture 5–7，online lockdown browser，closed-book，占比 15%。Lecture 8 内容 TKA 未明确说明，但从 Lecture 7 PDF 末尾的 summary 和课程大纲来看，Lecture 8 可能是 **Part 1 的收尾**（model selection / cross-validation / 正则化参数选择 $\lambda$ 的方法），或进入 penalized classification（penalized SVM / hinge loss + regularization 的解析方法）。转写中 TKA 提到 "O Part one is coming towards the final two lectures, including today"，Week 9 起由 **Simon Liu** 接手 Ensemble Learning。具体以 Lecture 8 课件为准。

---

## Week 8 — Lecture 8: Performance Evaluation and Statistical Inference（性能评估与统计推断）

> **材料**：转写 `week8/week8.txt`（ASR 噪声多；有效讲授内容止于 CA2 开考前，其后的考场座位安排与闲聊可忽略），官方课件 `week8/EE6406-Lecture8-TKA-v1.pdf`（Toh Kar-Ann，**权威来源**，41 slides + 封面，AY2026-27 S1）。本周是 **Part 1（Analytic Learning）的最后一讲**，回答的问题只有一个：**"学出来的 predictor/classifier 到底有多好？这个'好'有多可信？"**
>
> **课堂安排**：TKA 开场用约 20 分钟补完 Lecture 7 的剩余 slides（原话 "I tried to complete [Lecture 7] a little bit plus"），随后进入 Lecture 8；**7:50 收手机、开始 CA2 quiz**（见 §0）。Lecture 8 本身内容不算多（"the content for today's lecture is a relatively short one"），骨架只有两块：**NHST** 与 **Bayesian Analysis (BA)**，两者都是为"比较多算法实验结果"服务的。

> ⚠️ **权威来源说明 / 本周 ASR 错拼修正**：本周课件有一个重要特点——**McNemar statistic 与 t-test statistic 的公式课件没有列出**（只给 contingency table、假设和定性结论，因为实际使用交给 `statsmodels`/`scipy`）。本笔记中标 **⚠️ 补充** 的公式为标准统计教材内容，课件未给，仅为理解用；标 (1)(2)(3) 的公式才是课件原有编号。典型 ASR 错拼按 PDF 修正如下：
>
> | 转写 ASR | 正确术语 |
> |---|---|
> | "lecture aid" | Lecture 8 |
> | "batent / atient / basion / ba 分析 / patient analysis" | **Bayesian Analysis (BA)** |
> | "no hypothesis / now hypothesis / n hypothesis" | **null hypothesis**（$H_0$） |
> | "NHSD / NH ST / NHST / HST" | **NHST**（Null Hypothesis Significance Test） |
> | "magima test" | **McNemar's test** |
> | "sine rank test / sign rank test / sine test / sin test" | **Wilcoxon signed-ranks test** / **sign test** |
> | "frag test / Fagan test / F test" | **Friedman test** |
> | "Miami post hoc test / Nemenyi" | **Nemenyi post-hoc test** |
> | "confusion metric / computer metrics" | **contingency table**（2×2 列联表） |
> | "prometric / non prometric / non chiametric / non chromatic" | **parametric / non-parametric** |
> | "cross ventilation / cross valuation / 24 test / n f cross / n fo" | **cross-validation** / **two-fold test** / **N-fold cross-validation** |
> | "OCB / PO / NPO / L O OCB" | **LOOCV**（leave-one-out cross-validation） |
> | "INOVA / NOVA" | **ANOVA** |
> | "road / robe / rope" | **ROPE**（region of practical equivalence） |
> | "increase two" | **CA2** |
> | "dichotomous" | **dichotomous**（二分的） |
> | "critical value 39 / 38"（Wilcoxon） | **29 / 28**（按 PDF 修正） |
> | "c fier / cc / class fi" | **classifier** |

---

### 0. CA2 Quiz 信息（当天课上举行）

| 项目 | 详情 |
|---|---|
| **时间** | Lecture 8 之后、**同一节课内**（7:50 前回座并收手机，7:50 开始） |
| **范围** | **Lecture 5–7**（按 Week 7 通知：regression / classification learning + penalized learning） |
| **占比** | **15%**（CA1=10%, CA2=15%, CA3=15%, Final=60%） |
| **形式** | online quiz + **lockdown browser**（本次换成"掉线后可重新登录"的版本） |
| **允许物品** | 只允许 **approved calculator**；手机等电子设备一律收走 |
| **纪律** | **中途不得离开考场**——"once you leave this room, your results will not be counted" |
| **后续** | **CA3 在 4 周后（Week 12）**，"the same day, the same time, only four weeks later" |

- TKA 考前提醒：本次 quiz **计算量不小**（"you should be busy like quiz on quite a number of calculations"），建议"just do more rounds of checking"（多轮验算，可擦掉错误）。

---

### 1. Introduction：为什么需要 Performance Evaluation 与 Statistical Inference

#### 1.1 学习三大组件的回顾

| 组件 | 对应 Lecture |
|---|---|
| Learning model | Lecture 3（feature transformation $p(\mathbf{x})$ + parameter $\mathbf{w}$） |
| Learning loss / cost function | Lecture 4（learning score functions） |
| Optimization procedure | Lecture 5–7（closed-form analytic solutions + penalization） |

- 至此 Part 1（Analytic Learning）的方法已完备；剩下最后一个问题：**"我学到的 predictor/classifier 有多好？这个'好'有统计支撑吗？"**
- TKA 的现实动机对照：工作中的技术报告、写论文投顶会，都需要**用自己的方法 vs 先前方法**做实验对比，并声明"我的进展有多大"。但**不能只做定性比较**——"many things are quite grey, or quite continuous, not just yes or no"，需要统计工具来支撑"我确实更好"这个 claim。

#### 1.2 两个概念的分工（课件原话）

- **Performance evaluation**（性能评估）：provides a measure upon **how good can a learned predictor or classifier perform**。
- **Statistical inference**（统计推断）：provides **the confidence of such performance on unseen data**。

⭐ **关键前提：评估必须针对 unseen data（未见数据），而不是 training data。** 真正的 unseen data 不可得，于是做法是**从给定样本中 hold out 一部分作为 test set，用来模拟真实部署前的表现**（"you are simulating the real application before you pull your method out for real test"）。

- ⭐ **Lecture 4 的 learning score functions 直接复用为 performance measure**：你优化的 score（accuracy、precision、AUC、TER…）就是评估用的指标。选哪个**取决于应用场景**：
  - **Tight accuracy 场景**（banking / 转账验证）：绝不能让人冒名通过 → 极低 false accept。
  - **Loose accuracy 场景**（手机指纹解锁）：只有本人在用 → 宁可放宽，否则"you will always get rejected by fingerprint, then you get sick of the application"。

---

### 2. Empirical Evaluation（经验评估）

#### 2.1 Hold-Out Test（留出法）

**记号**：数据库含 $M$ 个样本 $(\mathbf{x}_i, y_i),\ i = 1, 2, \dots, M$，其中 $\mathbf{x}_i \in \mathbb{R}^d$ 为第 $i$ 个 **feature sample**，$y_i \in \{0,1\}$ 为对应的 **category indicator / target label**。

把数据库切成两份：

- **training set**：$m$ 个样本 —— 用于 classifier learning；
- **test set**：$n$ 个样本 —— 用于评估学到的 classifier 的性能；$m + n = M$。

- 若 $m \approx n$，可以做 **two-fold test**：第一轮 train/test 之后**把 training set 与 test set 互换（swap）**再跑一遍，**两个 test 结果取平均**作为最终结果。
- ⭐ two-fold 的好处：**所有数据既被训练过也被测试过**（"all the points are tested independently"）——每一轮里 classifier **只看到 training set**、完全看不到 test set，因此得到的评估是"诚实"的；两轮下来被评估的数据点翻倍，**statistical support 更强**。

**Transcript 补充（TKA 的实践经验）**：

- **Hold-out test 是当今最常用的做法**，因为深度学习时代数据集大（millions of samples 级别）；常见划分 **70/30 或 80/20**。
- 反过来，**小数据集（几百个样本量级）hold-out 不够用**：模型很容易 overfit，"hold-out test is not enough"。
- 即使今天数据多，仍有领域（采集 tedious / costly）只有小样本 → 必须用下面的 cross-validation。

#### 2.2 Cross-Validation Test（交叉验证）

**动机（课件原话）**：hold-out test **没有把所有给定数据都用于 classifier evaluation**；two-fold test 虽然覆盖全部数据，但对**小数据集**而言"may not be statistically informative"。

**Leave-One-Out Cross-Validation（LOOCV，留一法）**：

- 每次留 **1 个**样本做 testing，其余全部用于 training；重复 $M$ 次 → 得到 $M$ 个 test results，通常以**平均值**形式报告。
- ⭐ 课件原话：**"without re-sampling, the largest possible number of test cases without under-training the system is given by LOOCV."** —— 在不重采样（no re-sampling）的前提下，LOOCV 能给出**最多的测试样本数**，且每次训练都用了**尽可能多**的数据（$M-1$ 个）因而不至于 under-train。
- 缺点：若 $M$ 很大，需要循环训练 $M$ 次，**computing effort 巨大、不实际**（"nowadays nobody does this, only for small size"）。

**N-fold Cross-Validation（N 折交叉验证）**：

- 把整个数据集分成 **$N$ 个等份（equal portions）**，且**正负两类样本在各 partition 中均匀分布**（即 stratified 分层划分）。
- 每次取 1 份作 test、其余 $N-1$ 份作 training，重复 $N$ 次 → $N$ 个 test results，取平均报告。
- **典型 N 值：2、5、10**。
- ⭐ **two-fold test 就是 $N = 2$ 的特例**——transcript："the two-fold is just standardizing the two-fold to any number of partitions"。

#### 2.3 ⭐ 三种 empirical evaluation 对比

| 方法 | 训练轮数 | 每轮 train / test 规模 | 适用数据量 | 特点 |
|---|---|---|---|---|
| **Hold-out test** | 1 | $m$ / $n$（如 70/30、80/20） | 很大（millions） | 最快；小数据不可靠（易 overfit） |
| **Two-fold test** | 2 | 各约 $M/2$ | 中等 | $N=2$ 的 CV；两轮后覆盖全部数据 |
| **N-fold CV** | $N$（典型 2/5/10） | $(N-1)M/N$ / $M/N$ | 中等（≤ 数千） | compute 与 statistical support 的平衡点 |
| **LOOCV** | $M$ | $M-1$ / $1$ | **极小**（< 100） | 不重采样下测试量最大；$M$ 大时不可行 |

- **如何选 N**（transcript）："the choice is basically yours"——取决于你对数据量是否足够的判断；但写论文时还要遵守**领域惯例 / reviewer 设定的 standard**（"if the first person doing it and you want to compare with him, then you have to follow his number of folds"）。这也是"standardizing the testing"的意义。

---

### 3. Null Hypothesis Significance Test (NHST)

#### 3.1 什么是 Statistical Significance Test

- **Hypothesis testing 做 statistical inference** 是一种基于数据的 **confirmatory analysis（验证性分析）**。
- 用途：判断 experimental results **是否包含足够信息去 challenge conventional wisdom（挑战既有认知）**。
- 换句话说：assesses **the confidence in the occurrence of an experimental observation** using statistical methods。

**两种处理数据的思路**（transcript 补充，很关键）：

| 类型 | 含义 | 前提 | 优缺点 |
|---|---|---|---|
| **Parametric** | 先假设数据服从某个分布模型（如 Gaussian，用 mean 与 variance 描述），再用 model parameters 推断 statistic | 数据量要大到让分布"趋于 normal" | 数据多时更 accurate；数据少时模型不准 |
| **Non-parametric** | 不依赖某个固定分布模型，改用 **ranking / counting** 这类无分布假设的统计量 | 无需 normal 假设 | 更 flexible；⚠️ "non-parametric" **不等于没有参数**，只是**不 rigid 地绑定某一个特定模型** |

⭐ **NHST 的核心图像**（transcript）：把两组结果各自看成**一个分布**，判断这两个分布**是否 overlap**：

- overlap 大 → 两个方法没有显著差异 → **不拒绝 $H_0$**；
- overlap 小 → 显著不同 → **拒绝 $H_0$**。

判断依据是两分布的 **mean 与 variance**。

**核心术语**：

- **$H_0$（null hypothesis，零假设）**：默认立场——两个 classifier **没有显著差异**。
- **$H_1$（alternative hypothesis，备择假设）**：两者有显著差异。
- **p-value**：支持"拒绝 $H_0$"的强度度量。⭐ **large value of the test statistic → small p value → supports $H_1$ to reject $H_0$**。
- **Confidence level（置信水平）$\alpha$**：常用 $\alpha = 0.05$（= 95% confidence）。$p < \alpha$ → reject $H_0$。若要求更严格可取 $\alpha = 0.01$（99% confidence）。
- ⚠️ p-value 只是 **confidence**，**不是"绝对正确"**——这一点是 §7 批评的根源。

**三种比较场景**（本讲的骨架，课件明确分成三类）：

| 场景 | 数据规模 | 方法 | 本笔记章节 |
|---|---|---|---|
| (a) Two classifiers on **a single** data set | 1 个数据集 | **McNemar's test** | §4 |
| (b) Two classifiers over **multiple** data sets | $N$ 个数据集 | averaging / **t-test** / **Wilcoxon signed-ranks** / **sign test** | §5 |
| (c) **Multiple** classifiers over **multiple** data sets | $N$ 数据集 × $K$ 分类器 | **ANOVA** / **Friedman test** + **Nemenyi post-hoc** | §6 |

- 用多少个数据集取决于**研究领域的数据可得性**（availability / cost of acquiring data）；一般原则是**越多越好**——"nowadays, one dataset is usually not enough"（除非该数据集非常大且覆盖面广）。

---

### 4. 场景 (a)：Two Classifiers on a Single Data Set — McNemar's Test

#### 4.1 方法定位

- **Non-parametric** 方法，适用于 **nominal data（名义数据）**。
- 在 R、Python 及其他统计软件包中都有实现（Python：`statsmodels.stats.contingency_tables.mcnemar`）。
- ⭐ 历史注：早年要**手工填表 + 查分布表**；现在直接调库即可。

#### 4.2 2×2 Contingency Table 与假设

检验基于"两次 test 在 $n$ 个 subject 上的结果"构成的 **2×2 contingency table**：

**Table 1: Contingency table for McNemar's test**

| | | (Classifier B) 'Yes' | (Classifier B) 'No' |
|---|---|---|---|
| **(Classifier A)** | **'Yes'** | $a$ | $b$ |
| | **'No'** | $c$ | $d$ |

- $a$、$d$：两个 classifier **agree**（都对 / 都错）。
- $b$、$c$：**discordances（不一致）**——指对其中一个 classifier 是 'No' occurrence、对另一个却是 'Yes' occurrence。
- ⭐ **$H_0$：$p_b = p_c$**（两种 disagreement 的出现概率相等）→ 两个 classifier 的 **marginal proportions 没有显著差异**。
- ⭐ **McNemar's test 只用到 discordant cells $b$、$c$**；agree 的 $a$、$d$ 不进入统计量（但它们决定 $n$）。
- **判决规则**：test statistic 越大 → p-value 越小 → **支持 $H_1$、拒绝 $H_0$**。

**两个主要假设**：

1. **The classifier pair $(A, B)$ is mutually independent**——两个 classifier 相互独立（若 B 是由 A 派生/改进而来，则假设不成立）。
2. **Each classifier A and classifier B can be assigned to one of two possible categories**——在每个样本上每个 classifier 都落进两个类别之一。

> ⚠️ **补充（课件未给公式）**：标准 McNemar statistic 为
>
> $$\chi^2 = \frac{(b-c)^2}{b+c}, \qquad\text{或（含 Yates 连续性修正）}\qquad \chi^2 = \frac{\left(|b-c|-1\right)^2}{b+c} \tag{8.1}$$
>
> 自由度 $\text{df}=1$；当 $b+c$ 很小时应改用 **exact test**（`exact=True`）。

#### 4.3 Example 8.1（Python）

```python
from statsmodels.stats.contingency_tables import mcnemar
table = [[15, 4],
         [25, 6]]
result = mcnemar(table, exact=False, correction=True)
print(f"Statistic: {result.statistic:.4f}")
print(f"P-value:   {result.pvalue:.4f}")
alpha = 0.05
if result.pvalue < alpha:
    print("Reject the null hypothesis: Significant difference exists.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")
```

**读表**：$a=15$，$b=4$，$c=25$，$d=6$，$n = 50$；$b$ 与 $c$ 相差很大。按 (8.1) 含连续性修正：

$$\chi^2 = \frac{(|4-25|-1)^2}{4+25} = \frac{20^2}{29} = \frac{400}{29} \approx 13.79 \;\Longrightarrow\; p \approx 0.0002 < 0.05$$

→ **拒绝 $H_0$**：两个 classifier 存在显著差异。（$p$ 值为按 (8.1) 的自行核算，用于理解 `result.pvalue` 的来源。）

---

### 5. 场景 (b)：Two Classifiers over Multiple Data Sets

#### 5.1 Averaging over Data Sets（最直接，也最容易被批评）

- 做法：在多个数据集上分别算出 classification accuracy，**取平均**，比大小。
- 适用例子：比较不同 classifier 在"同一类诊断任务、来自不同机构的 medical databases"上的平均准确率。
- ⭐ **两个被批评的点**：
   1. **不可比性**：不同数据集的难度与性质差异很大（transcript："some are chemical problems, some are mathematical problems, some are physics problems"），**跨域 average accuracy 可能没有意义**。
   2. **对 outlier 敏感**：一个数据集上的极好（或极差）表现可以**主导整体结论**——"one excellent performance on one data set can prevail the overall poor performance, or vice versa"。transcript 的具体例子：若某个数据集上两个方法都接近 random guess（~50%），而其余都是 80–90%，这一个数据集会把整体平均整个拉偏。

#### 5.2 t-Test（parametric）

- **前提：数据正态分布**（因此是 parametric 方法）。可用 Matlab（statistics toolbox）与 Python（`scipy.stats`）。
- ⭐ 历史注：t-test 最初发表时叫 **Student's test**——作者用的是化名/笔名 "Student" 而非真名（"he wanted to hide his identity"）。
- 分为两类：

| 类型 | 别名 | 假设 | 典型场景 |
|---|---|---|---|
| **Unpaired t-test** | independent samples / Student's | 两个**正态总体**的 **mean 相等**（two-sample location test） | treatment 效果：一组人群测"处理前"，**另一组**人群测"处理后" |
| **Paired t-test** | dependent samples / repeated measures | 两次 response 测在 **same statistical unit** 上 | cancer treatment：对**同一批病人**测肿瘤在治疗前后的 size |

**三个必须满足的假设**（unpaired 情形，课件明确列出）：

1. 被比较总体**服从 normal distribution**；
2. 两个总体**方差相同**——"as though the distribution for one group was merely a shifted version of the other group, **without changing shape**"（只是平移，形状不变）；若一组很尖、一组很胖，则不可比；
3. 两组数据**独立采样**（data being sampled independently）。

> ⚠️ **补充（课件未给公式）**：
>
> - **Unpaired（equal-variance / pooled）**：
>
> $$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{\dfrac{1}{n_1}+\dfrac{1}{n_2}}},\qquad s_p^2 = \frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2},\qquad \text{df}=n_1+n_2-2 \tag{8.2}$$
>
> - **Paired**：
>
> $$t = \frac{\bar{d}}{s_d/\sqrt{n}},\qquad \bar{d}=\frac{1}{n}\sum_{i=1}^{n}\left(x_i-y_i\right),\qquad \text{df}=n-1 \tag{8.3}$$
>
> 其中 $s_p$ 为 **pooled standard deviation**；$s_d$ 为逐对差值的样本标准差。

#### 5.3 ⭐ Wilcoxon Signed-Ranks Test（paired t-test 的非参数替代）

**设置**：$N$ 个数据集，$d_i$ 为第 $i$ 个数据集上两个 classifier 的 accuracy 之差，$i=1,\dots,N$。

**步骤**：

1. 按 **$|d_i|$ 升序**给 rank——**差异越小 rank 越小**（rank 1 表示两方法几乎一样）。
   > ⚠️ 课件原句 "with the better-performed one having a smaller rank number" 表述含糊；按 Table 2（Example 8.2）的实际编号，**rank 依据 $|d_i|$ 升序**分配，与两个 classifier 谁赢无关。
2. **Tie（$|d_i|$ 相同，尤其 $d_i=0$）→ assign average rank**。例：$d=0.00$ 出现两次，本应占 rank 1 与 2 → 各得 **1.5**。
3. 定义两个 rank sum：
   - $R^+$ = **第二个 algorithm 胜出**（$d_i>0$）的数据集的 rank 之和；
   - $R^-$ = 相反情况（$d_i<0$）的 rank 之和；
   - ties（$d_i=0$）的 rank **一半分给 $R^+$、一半分给 $R^-$**；若 tie 数为**奇数**，"one rank is disregarded"（舍弃一个 rank）。

数学形式（课件式 (1)、(2)）：

$$R^{+} = \sum_{d_i>0}\text{rank}(d_i) + \frac{1}{2}\sum_{d_i=0}\text{rank}(d_i) \tag{1}$$

$$R^{-} = \sum_{d_i<0}\text{rank}(d_i) + \frac{1}{2}\sum_{d_i=0}\text{rank}(d_i) \tag{2}$$

4. ⭐ **判决规则**：当 $\min\left(R^{+},R^{-}\right)$ **小于或等于** statistical table 中的 **critical value** 时，**拒绝 $H_0$**。

#### 5.4 ⭐ Example 8.2（Wilcoxon signed-ranks 完整手算）

**Table 2: Classification accuracies of LSE-based and TER-based learning**

| No. | Data | LSE-based Ave（$x$，% acc） | TER-based Ave（$y$，% acc） | Diff（$d=y-x$） | Rank |
|---|---|---|---|---|---|
| 1 | Shuttle-l-contr | 99.03 | 99.06 | +0.03 | 7 |
| 2 | BUPA-liver | 72.17 | 72.16 | −0.01 | 3.5 |
| 3 | Monk-1 | 89.90 | 90.55 | +0.65 | 15 |
| 4 | Monk-2 | 66.16 | 68.27 | +2.11 | 16 |
| 5 | Monk-3 | 90.39 | 91.02 | +0.62 | 13.5 |
| 6 | Pima-diabetes | 77.73 | 77.73 | 0.00 | 1.5 |
| 7 | Tic-tac-toe | 98.22 | 98.24 | +0.02 | 5.5 |
| 8 | Breast-cancer-W | 97.26 | 97.37 | +0.11 | 8.5 |
| 9 | StatLog-heart | 83.25 | 83.07 | −0.19 | 11 |
| 10 | Credit-app | 86.65 | 86.64 | −0.01 | 3.5 |
| 11 | Votes | 94.24 | 94.27 | +0.02 | 5.5 |
| 12 | Mushroom | 100.00 | 100.00 | 0.00 | 1.5 |
| 13 | Wdbc | 96.18 | 96.80 | +0.62 | 13.5 |
| 14 | Wpbc | 79.60 | 79.49 | −0.11 | 8.5 |
| 15 | Ionosphere | 89.18 | 89.63 | +0.45 | 12 |
| 16 | Sonar | 81.78 | 81.96 | +0.17 | 10 |

**计算**（注意 $d=y-x$，正值 = TER 更好）：

$$R^{+} = (7+15+16+13.5+5.5+8.5+5.5+13.5+12+10) + (1.5) = 108$$

$$R^{-} = (3.5+11+3.5+8.5) + (1.5) = 28$$

- **自检**：$R^{+} + R^{-} = 108 + 28 = 136 = 1+2+\cdots+16$ ✓（rank 总和守恒）
- 在 confidence level $\alpha = 0.05$、$N = 16$ 时，Wilcoxon signed-ranks test table 的 **critical value = 29**。
- 因为较小的那个 rank sum 为 $28 \le 29$，**拒绝 $H_0$**：在 0.05 confidence level 下两个 classifier **不等价** → **TER-based learning 显著优于 LSE-based learning**。

> ⚠️ 转写把临界值念成 "the value in the table was 39, because we had 38"——按 PDF 修正为 **29 / 28**。

**Remark（课件）**：

- Python 实现：`scipy.stats.wilcoxon()`。
- ⭐ Wilcoxon signed-ranks test **比 paired t-test 更安全（safer）**，因为它**不假设 normal distribution**。
- 但**当 paired t-test 的假设满足时，Wilcoxon 反而不如 paired t-test 受偏好**（t-test 有更高 statistical power，Wilcoxon 是 less preferred）。

#### 5.5 Sign Test（计数法）

- 做法：**数一数在多少个数据集上某个 algorithm 是 overall winner**。
- $H_0$ 下两个算法各赢约一半：$N_{\text{win}} \approx N/2$ → 两者被视为 **equivalent**。
- Wins 的个数服从 **binomial distribution**，**critical number of wins $N_{\text{critical}}$** 从统计表查得（取决于 $N$ 与 $\alpha$）。
- ⭐ **判决**：某 classifier 只有在**至少 $N_{\text{critical}}$ 个数据集上胜过对手**时，才算 significantly better。
- ⭐ 注意：不能只看"6 比 5 这样的简单多数"——必须把 $N_{\text{win}}$ 与 **$N_{\text{critical}}$** 比较。

**Example 8.3**：在 Table 2 上做 sign test——TER-based learning 在 16 个数据集中赢了 **11** 个（把两个 tie 数据集中的一个也算作赢），查 sign test 表后 **在 0.05 confidence level 下不能拒绝 $H_0$**。（$N=16$ 时 $N_{\text{critical}} = 12$，11 < 12。）

⭐ **Remark（课件，重要考点）**：

> 若换一个 classifier，它在 16 个数据集中赢了 **12** 个（正好等于 critical value），**但所有 $d_i < 0.01\%$**——虽然 $H_0$ 被拒绝，但"两个 classifier 显著不同"这个结论**仍然值得怀疑**（"remains questionable"）。

→ 因此 **数据集个数少时做 hypothesis testing 必须格外小心**；**statistical significance ≠ practical / engineering significance（效应量 effect size 同样重要）**。

---

### 6. 场景 (c)：Multiple Classifiers over Multiple Data Sets

#### 6.1 为什么不能简单枚举所有 pair

- 上面的 **paired tests 完全可以枚举所有组合对**来比较多个 classifier。
- 但反对的理由是：**检验次数太多 → 可能纯粹因为随机性而拒绝 $H_0$**（multiple comparisons problem / family-wise error 膨胀）。
- 解决方案：**Analysis of Variance（ANOVA，parametric，假设数据 normal distribution）**，或它的 **non-parametric counterpart：Friedman test**。

#### 6.2 Friedman Test

- 做法：在**每个数据集内部**给 $K$ 个 classifier 排名——最准确的 rank 1、其次 2、3、…… 最差 rank $K$（tie 取平均 rank）；然后对每个 classifier 求**平均 rank（average rank）**。
- 用这些 ranks 构造 statistic（课件未给公式）来检验"所有 classifier 表现相同"的 $H_0$。
- 可用 Matlab（statistics toolbox）与 Python（`scipy.stats`）。

**Example 8.4**

**Table 3: Average accuracy and ranks**

| No. | Database name | RP-FLD | RP-LSE | RP-TER | RP-AUC |
|---|---|---|---|---|---|
| 1 | Shuttle-l-contr | 0.9811 (3.0) | 0.9861 (2.0) | 0.9909 (1.0) | 0.9574 (4.0) |
| 2 | BUPA-liver | 0.7038 (2.0) | 0.6995 (3.0) | 0.7217 (1.0) | 0.6513 (4.0) |
| 3 | Monks-1 | 0.9171 (1.0) | 0.8959 (4.0) | 0.9016 (3.0) | 0.9161 (2.0) |
| 4 | Monks-2 | 0.6570 (1.0) | 0.6174 (3.0) | 0.6157 (4.0) | 0.6471 (2.0) |
| 5 | Monks-3 | 0.9123 (1.0) | 0.8977 (3.0) | 0.9041 (2.0) | 0.8745 (4.0) |
| 6 | Pima-diabetes | 0.7591 (2.0) | 0.7073 (4.0) | 0.7776 (1.0) | 0.7549 (3.0) |
| 7 | Tic-tac-toe | 0.9827 (1.0) | 0.9814 (3.0) | 0.9822 (2.0) | 0.8660 (4.0) |
| 8 | Breast-cancer-W | 0.9720 (3.0) | 0.9695 (4.0) | 0.9740 (1.0) | 0.9725 (2.0) |
| 9 | Statlog-heart | 0.8324 (1.5) | 0.8255 (4.0) | 0.8318 (3.0) | 0.8324 (1.5) |
| 10 | Credit-app | 0.8671 (1.0) | 0.8592 (4.0) | 0.8667 (2.0) | 0.8632 (3.0) |
| 11 | Votes | 0.9414 (3.0) | 0.9408 (4.0) | 0.9424 (2.0) | 0.9439 (1.0) |
| 12 | mushroom | 1.0000 (2.0) | 1.0000 (2.0) | 1.0000 (2.0) | 0.9945 (4.0) |
| 13 | wdbc | 0.9654 (2.0) | 0.9445 (4.0) | 0.9650 (3.0) | 0.9716 (1.0) |
| 14 | wpbc | 0.6722 (2.0) | 0.6218 (4.0) | 0.7961 (1.0) | 0.6591 (3.0) |
| 15 | ionosphere | 0.8869 (1.0) | 0.8372 (4.0) | 0.8695 (2.0) | 0.8663 (3.0) |
| 16 | sonar | 0.8162 (2.0) | 0.8071 (4.0) | 0.8152 (3.0) | 0.8238 (1.0) |
| **Average** | | **0.8667 (1.781)** | **0.8494 (3.500)** | **0.8722 (2.063)** | **0.8497 (2.656)** |

- 读法：括号外是 average accuracy，括号内是**该数据集内的 rank**。例如 dataset 12（mushroom）三个方法都是 1.0000 → 本应占 rank 1/2/3 → **各得 2.0**；dataset 9 中 RP-FLD 与 RP-AUC 打平 → 各得 1.5。
- ⭐ 注意 average accuracy 的排序（RP-TER 0.8722 最高）与 **average rank** 的排序（RP-FLD **1.781** 最好）**并不一致**——rank-based 方法不被个别数据集的极端值主导，这正是 Friedman/rank 方法的优势。

#### 6.3 ⭐ Nemenyi Post-Hoc Test

- 若 Friedman test **拒绝了 $H_0$**，可进一步做 **post-hoc Nemenyi test** 分析 classifier 两两之间的差异。
- 若两个 classifier 的 **average ranks 之差**至少达到 **critical difference**：

$$CD = q_{\alpha}\sqrt{\frac{K(K+1)}{6N}} \tag{3}$$

其中 $K$ = classifier 个数，$N$ = 数据集个数，$q_{\alpha}$ 为 studentized range statistic 的分位值（按 $\alpha$ 查表）。

- 则这两个 classifier 的 performance **significantly different**。
- ⭐ Transcript 重点：图里"**distance between each pair**"就是判据——只有 rank 距离超过 $CD$ 的组合才算真的不同；即便整体排序有先后，也要**逐对**比较才能下结论。
- **Figure 1** 是 Demšar (2006) 风格的 **CD diagram**：把每个 classifier 按其 average rank 放到坐标轴上，**用横线把彼此之间没有显著差异的 classifier 组连起来**（caption："groups of classifiers that are not significantly different are connected"）。
- 注意：这个图在常见软件包里**不是现成可用的**（transcript："it's not so available in many"），需按 Demšar (2006) 自己实现。

---

### 7. Bayesian Analysis (BA)

#### 7.1 动机：NHST 与 p-value 被滥用

- 有了 NHST 这一整套工具后，课件紧接着提醒：**p-value 的使用需要 extra care**（Ioannidis, 2005；Amrhein et al., 2019；Nuzzo, 2014）。
- 这些文献指出：**NHST 在很多场合并未被恰当使用**，可能造成了**研究发现的低可重复率（non-replication of research discoveries）**。
- ⭐ **两个 fundamental issues**：
   1. **the bias and the extent of repeated independent testing**——重复独立检验的 bias 与次数问题（检验做得越多，假阳性累积越多）；
   2. **the use of the p-value in a dichotomous way**——把 p-value 当作**二值判决**：$p<0.05$ 就宣称"我的方法绝对更好"。但 p-value 本质只是 **confidence**，"you only have 95% confidence"，不是 100% 确定。

**Transcript 补充**：

- 医学/论文领域的 over-claim、misrepresent 结果现象严重（"they overclaim their results"）。
- NHST **只比较两个 mean 的距离**，**完全不关心分布的形状**（"they may not care about the shape of the distribution"）；而分布的形状（胖/瘦）本身携带重要信息。
- 因此有学者主张**弃用 NHST**（Amrhein et al. 2019 的标题就是 "Retire statistical significance"），改用 Bayesian analysis。

#### 7.2 ⭐ Bayesian Analysis 的思路：不做二元判决，给后验概率

- 回到 Bayesian statistics：不输出"接受/拒绝"，而是**给出完整的 posterior distribution**，直接告诉你三种情形的概率：

$$\bigl\{\,A<B,\qquad A=B\ (\text{within ROPE}),\qquad A>B\,\bigr\}$$

- **ROPE（region of practical equivalence，实际等价区间）**：预先设定的**容差带**；若两方法的差异落在 ROPE 内，就认为它们在**实务上等价**。Example 8.5 中 ROPE 设为 **$\pm 0.01$**。
  > ⚠️ 课件原文把 ROPE 误印为 "**robe**"；transcript 又念成 "road"。正确术语是 **rope**，来自 Bayesian 分析中的 ROPE 概念。

- ⭐ 核心优势：给出的是**"有多大的信心说 A 比 B 好"的完整图像**，而不是 "A 赢 B" 这种**非黑即白**的结论。

#### 7.3 Example 8.5：Two Classifiers on a Single Data Set

两个 classifier A、B 在**同一数据集的 10 折**上的 accuracy（%）：

$$
A=\begin{bmatrix}
95.8707\\ 94.7935\\ 93.5368\\ 96.4093\\ 95.6912\\
94.2549\\ 94.6140\\ 95.5117\\ 96.2298\\ 95.1526
\end{bmatrix},
\qquad
B=\begin{bmatrix}
93.5368\\ 92.8187\\ 91.5619\\ 93.8959\\ 93.1777\\
93.1777\\ 94.7935\\ 91.7415\\ 94.6140\\ 94.0754
\end{bmatrix}
$$

调用 Lucy Kuncheva 提供的工具包：

```python
[probs, plot_data] = two_classifiers_one_dataset(x, rope, cvruns)
# https://github.com/LucyKuncheva/Bayesian-Analysis-for-Comparing-Classifiers
```

得到 posterior results：

$$\text{probs} = [\,0.0001,\ \ 0.0549,\ \ 0.9450\,] \quad := \quad [\,A<B,\ \ A=B\ (\text{rope}),\ \ A>B\,]$$

即 $P(A<B)=0.0001$、$P(A=B\ \text{within rope})=0.0549$、$P(A>B)=0.9450$（ROPE $=\pm 0.01$）。

- **自检**：A 的 10 折平均 $\approx 95.21$，B 的 10 折平均 $\approx 93.34$，差约 **+1.87**，远大于 ROPE $\pm0.01$ → $P(A>B)=0.945$ 符合直觉；同时 BA 还额外告诉你"仍有约 5.5% 的概率两者实务等价"。
- **Figure 2** 画出 $\Delta$Acc（A 与 B 的 accuracy 差）的 **posterior pdf**，峰值落在正区间。

#### 7.4 Example 8.6 / 8.7：Multiple Data Sets 与 effect size 敏感性

**Example 8.6**：用 Table 2 的 **16 个数据集**比较 TER 与 LSE，调用

```python
[samples, probs] = signed_rank_test_diff(x, rope, prior, T)
# https://github.com/LucyKuncheva/Bayesian-Analysis-for-Comparing-Classifiers
```

由于 Table 2 中两方法的 accuracy 差异**极小**（大多是 $0.0x\%$ 量级），分析给出一个**非常窄的分布**：

$$p(\text{Rope}) = 99.834\%,\qquad p(\text{TER}) = 0.166\%,\qquad p(\text{LSE}) = 0.000\%$$

**Figure 3** 中分布几乎压成一条竖线：左端 `p(LSE) = 0.000`，右端 `p(TER) = 0.166`，中间 `p(Rope) = 99.834`。

⭐ **与 NHST 的关键对照（本讲最重要的教学点）**：**同一组 Table 2 数据**——

| 方法 | 结论 |
|---|---|
| **Wilcoxon signed-ranks test**（§5.4） | $28 \le 29$ → **拒绝 $H_0$** → "两分类器显著不同（TER 更好）" |
| **Bayesian Analysis**（Example 8.6） | $p(\text{Rope}) = 99.834\%$ → **两者实务上等价** |

→ NHST 在小差异 + 稳定排序（rank 一致）的情况下会给出**误导性的"显著"**结论；BA 的结论才符合工程直觉。

**Example 8.7**：把 Table 2 的差异值**放大 10 倍**后重做同一分析：

$$p(\text{Rope}) = 38.662\%,\qquad p(\text{LSE}) = 0.004\%,\qquad p(\text{TER}) = 61.334\%$$

- 分布明显变宽，$P(\text{TER better})$ 从 0.166% 跳到 61.334% → 这演示了 **Bayesian Analysis 对 effect size（差异幅度）的敏感性**。
- ⭐ 对比之下，NHST 的 p-value **只看"是否偏离随机"，不看差异有多大**——这正是 BA 被认为更合理的原因。

#### 7.5 Multiple Classifiers 下的 Bayesian Analysis

- Benavoli et al. (2017) 引用 Gelman et al. (2012) 的论断：

> "in Bayesian analysis we usually do not have to worry about **multiple comparisons**. The reason is that we do not worry about **Type I error**, because the null hypothesis is hardly believable to be true."

- 建议对多分类器采用 **multilevel analysis / hierarchical Bayesian model**——即**逐一评估 classifier pair 的各种组合**。
- ⭐ 与 NHST 的对照逻辑：NHST 因为"要做二元判决"而害怕 multiple comparisons 导致 **Type I error** 膨胀（所以必须先做 ANOVA / Friedman 这类整体检验）；BA 认为 **point null hypothesis 几乎不可能为真**，不做二元判决也就没有 Type I error 可担心。

---

### 8. Summary Notes（课件结论与 TKA 的推荐做法）

1. **对 NHST 的承认**：承认 **null hypothesis significance testing 有 'black-and-white'（非黑即白）的倾向**，因此在**呈现推断结果（presenting inference results）与下结论时务必谨慎**。
2. **对 BA 的保留**：支持 BA 的论点是 "point-wise null hypotheses are practically always false"（基于 $H_0$ 存在的假设），但这一论断**比较 intricate（微妙）**——因为**对来自同一个 classifier 的两组不同观测，null hypothesis 未必同样适用**。
3. ⭐ **课件的推荐做法**：
   - **比较两个 classifier**（无论单个数据集还是多个数据集）→ **用 Bayesian Analysis**；
   - **比较多个 classifier** → 保留 **post-hoc Nemenyi test**，主要用于**可视化 classifier 的 ranking order**；
   - **最重要的一条**：**avoiding absolute 'black-and-white' claims can prevent misrepresentation**——避免绝对的黑白结论，能防止误述结果。

---

### 9. ⭐ 考点速查表

| 考点 | 要点 |
|---|---|
| **Performance evaluation vs statistical inference** | 前者给"有多好"的度量（针对 **unseen data**），后者给这份度量的 **confidence** |
| **Hold-out test** | 切成 training $m$ + test $n$，$m+n=M$；深度学习大数据常用 70/30、80/20；小数据不可靠（易 overfit） |
| **Two-fold test** | $m\approx n$ 时交换 train/test 再跑一次，两个结果取平均；= $N=2$ 的 CV |
| **LOOCV** | 每次留 1 个测试，共 $M$ 次取平均；不重采样下 **测试量最大且不 under-train**；$M$ 大时计算上不可行 |
| **N-fold CV** | 分 $N$ 个**等份**且**正负样本均匀分布**（stratified）；典型 $N=2,5,10$；结果取平均 |
| **如何选 N** | 数据量 + 领域惯例 / reviewer standard；"the choice is basically yours" |
| **Parametric vs non-parametric** | Parametric 先假设分布（如 normal，用 mean/variance）；Non-parametric 不绑定分布模型，用 rank / count（≠ 无参数） |
| **NHST 基本逻辑** | $H_0$：两方法无显著差异；statistic 越大 → p 越小 → 拒绝 $H_0$；$\alpha=0.05$=95% confidence，$\alpha=0.01$=99% |
| **三大比较场景** | (a) 单数据集 2 分类器；(b) 多数据集 2 分类器；(c) 多数据集 多分类器 |
| **McNemar's test** | 非参数、nominal data、单数据集；2×2 contingency table；$H_0$: $p_b=p_c$；**只用 discordance $b,c$** |
| **McNemar 两大假设** | (i) classifier pair $(A,B)$ mutually independent；(ii) 每个 classifier 落在两类之一 |
| **McNemar 实现** | `statsmodels.stats.contingency_tables.mcnemar(table, exact=False, correction=True)`；大 statistic + 小 p → 拒绝 $H_0$ |
| **Averaging over data sets** | 最直接但受批评：跨域结果不可比 + 对 outlier 敏感（一个数据集可主导整体） |
| **t-test 前提** | normal distribution + 两总体**同方差** + 独立采样；unpaired（两组不同 unit）vs paired（同一 unit 前后测） |
| **Wilcoxon signed-ranks** | paired t-test 的非参数替代：按 $|d_i|$ **升序**给 rank，tie 取 **average rank**，$\min(R^+,R^-) \le$ **critical value** → 拒绝 $H_0$ |
| **Example 8.2 数字** | $R^+ = 108$，$R^- = 28$，$N=16$、$\alpha=0.05$ 时 critical value $=29$ → $28\le29$ **拒绝 $H_0$**（TER 显著优于 LSE） |
| **Wilcoxon 建议** | 比 paired t-test **safer**（不假设 normal）；但 t-test 假设满足时 t-test 更好（power 更高） |
| **Sign test** | 数"赢的数据集个数"；wins ~ **binomial**；需 $\ge N_{\text{critical}}$（$N=16$ 时 = 12）才算显著 |
| **Sign test 陷阱** | 赢 12/16 但所有 $d_i < 0.01\%$ → 拒绝 $H_0$ 但结论**可疑**；significance ≠ effect size |
| **多分类器为何不能枚举 pair** | 检验次数过多 → 纯因随机性拒绝 $H_0$ 的概率累积（multiple comparisons） |
| **Friedman test** | ANOVA 的非参数对应；**每个数据集内部**排名（最好 rank 1），用**平均 rank** 检验；`scipy.stats` 可用 |
| **Example 8.4 平均 rank** | RP-FLD **1.781**（acc 0.8667）、RP-TER 2.063（0.8722）、RP-AUC 2.656（0.8497）、RP-LSE **3.500**（0.8494）——rank 排序与 accuracy 排序不同 |
| **Nemenyi post-hoc** | $CD = q_\alpha\sqrt{K(K+1)/(6N)}$；两 classifier **平均 rank 差 $\ge CD$** → 显著不同 |
| **CD diagram** | 用横线把"彼此无显著差异"的 classifier 组连起来，可视化排序（Demšar 2006） |
| **NHST 的两大批评** | (i) repeated independent testing 的 bias 与次数；(ii) p-value 的 **dichotomous use**（当作二元判决） |
| **BA 的输出** | 三个后验概率 $[\,P(A<B),\ P(A=B),\ P(A>B)\,]$，其中 $A=B$ 由 **ROPE** 界定（课件误印 "robe"） |
| **Example 8.5** | 单数据集 10 折；`probs = [0.0001, 0.0549, 0.9450]`，ROPE = $\pm 0.01$；调用 `two_classifiers_one_dataset(x, rope, cvruns)` |
| **Example 8.6（关键对照）** | 同一 Table 2：NHST **拒绝 $H_0$**，BA 给 $p(\text{Rope}) = 99.834\%$ → **实务等价** |
| **Example 8.7** | 差异放大 10× → $p(\text{TER})=61.334\%$、$p(\text{Rope})=38.662\%$ → **BA 对 effect size 敏感** |
| **BA 与 multiple comparison** | 不做二元判决 → 不担心 Type I error；多分类器建议 **hierarchical Bayesian model** |
| **课件推荐** | 两分类器比较用 **BA**；多分类器用 **Nemenyi** 可视化排序；**避免绝对黑白结论** |

---

### 10. 本周要点小结

- **本讲定位**：Part 1（Analytic Learning，Lecture 3–8）的**收尾讲**。前面 6 周解决的是"**怎么学**"（model / loss / optimization / penalization），本周解决"**学出来怎么评估、评估结果有多可信**"——这是写报告、投论文、做技术选型都绕不开的一步。

- **Empirical Evaluation（经验评估）**：
  - 核心：评估必须针对 **unseen data**，用 **hold-out** 模拟真实部署。
  - 三条路：**hold-out test**（大数据，70/30、80/20）、**N-fold CV**（$N = 2, 5, 10$，正负样本均匀分布）、**LOOCV**（$M$ 小时，不重采样下测试量最大）。
  - two-fold test = $N=2$ 的特例；$N$ 的选取既看数据量也看领域惯例。

- **NHST（零假设显著性检验）**：
  - 三种场景对应三套工具：**McNemar's test**（单数据集 2 分类器）→ **t-test / Wilcoxon signed-ranks / sign test**（多数据集 2 分类器）→ **ANOVA / Friedman + Nemenyi**（多数据集多分类器）。
  - ⭐ **必须记住手算流程的只有 Wilcoxon**：按 $|d_i|$ 升序给 rank（tie 取平均），算 $R^+$、$R^-$，与 critical value 比较（Example 8.2：$R^+ = 108$，$R^- = 28$，临界值 29 → 拒绝 $H_0$）。
  - 关键概念区分：**parametric（依赖 normal 假设）vs non-parametric（用 rank/count）**；**unpaired vs paired**；**ANOVA vs Friedman**；**只做两两比较会引发 multiple comparisons 问题**。
  - ⭐ **significance ≠ effect size**：Example 8.3 的 remark（赢 12/16 但差异都 < 0.01%）是核心警示。

- **Bayesian Analysis（BA）**：
  - 动机：NHST 的 p-value 被 **dichotomous**（二元）滥用 + 重复检验的 bias → 研究结果难以复现。
  - 做法：给出 **$\{A<B,\ A=B(\text{ROPE}),\ A>B\}$ 三个后验概率**，ROPE 由使用者设定（Example 8.5 为 $\pm 0.01$）。
  - ⭐ **最重要的对照**：同一组 Table 2 数据，Wilcoxon **拒绝 $H_0$**（显著），而 BA 给出 $p(\text{Rope}) = 99.834\%$（**实务等价**）；把差异放大 10× 后 BA 立刻翻转为 $p(\text{TER}) = 61.334\%$ → **BA 对 effect size 敏感，NHST 不敏感**。
  - 多分类器下 BA 不担心 Type I error，建议用 **hierarchical Bayesian model** 做 pair 组合评估。

- **Final exam 提醒**：Lecture 8 是 **Part 1 的最后一讲**，final 的 Part 1 考题（60% 中约 2.5 题）会覆盖 Lecture 1–8，本讲的 cross-validation 类型辨析、Wilcoxon rank 手算、Friedman/Nemenyi 概念、NHST vs BA 的对比属于**必考级**内容。

---

### 下一周预告

> **Week 9 = Ensemble Learning 开篇（Simon Liu 接手，Part 2）**。Toh Kar-Ann 的 Analytic Learning（Lecture 3–8）到此**全部结束**；从 Week 9 起由 **Simon Liu**（Trust Decision 首席 DA & AI 官，前 Lazada SVP）讲授 **Ensemble Learning（Lecture 9–13）**，会带行业应用。
>
> **考核节奏**：CA2 已于本周课上完成（15%）；**CA3 在 4 周后（Week 12）**，同一天、同一时间、同样形式（online lockdown browser，closed-book，approved calculator，不得中途离开考场）。final exam 60%，其中约 2.5 题来自 Part 1（Lecture 1–8）。
>
> Week 9 的具体内容（bagging / boosting / stacking / random forest 等哪个先讲）以 Lecture 9 课件为准。
