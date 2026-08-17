# EE6407 — Genetic Algorithms and Machine Learning（遗传算法与机器学习）

> 课程学习笔记总览。每周一节，按周总结重点内容。
> 第一周（开课周）特别关注考核要求与课程定位。
>
> **权威来源说明**：本笔记由 `week1/week1.txt` 录播转写整理，并以 `week1/L1(2-1).pdf`（官方课件，36 页，作者 Meng-Hiot Lim）核对修正。转写有较多语音识别噪声，以 PDF 为准。

---

## Week 1 — 开课周：课程介绍 + 问题分类 + 进化计算起源

### 1. 课程基本信息

- **课程名称**：EE6407 Genetic Algorithms and Machine Learning
- **课程定位**：遗传算法（GA）与机器学习**紧密相关**——许多 ML 问题可被建模为 GA 优化问题（如神经网络训练 = 最小化误差的优化）。GA 是受自然/生物进化启发的元启发式（metaheuristic）方法。
- **术语说明**：GA（遗传算法）只是进化计算（Evolutionary Computing, EC）这一大类下的**一种**具体技术；但因 GA 最流行，人们习惯把所有进化类方法统称 "GA"。本课中 evolutionary algorithm / evolutionary computing / genetic algorithm 混用，视为同义。
- **任课教师**：
  - **前 4 周（Week 1–4）**：**A/P LIM Meng Hiot**（School of EEE，办公室 S1-B1b-46，emhlim@ntu.edu.sg），主讲遗传算法/进化计算。
  - **后半（Week 5 起，机器学习部分）**：由另一位教授接手（转写误拼为 "prop mole"/"Malco"，**待 Week5 课件确认**）。
- **教材**：课件标注一本参考书（老师因与作者为友可自由使用其材料）。复杂度理论部分引用经典书 **Garey & Johnson, *Computers and Intractability***。

### 2. ⭐ 考核要求（重要）

| 成分 | 占比 | 说明 |
|---|---|---|
| **Continuous Assessment (CA)** | **40%** | 贯穿全学期；分为两段 |
| └ CA Part 1（Lim 的 4 周内） | **10%** | **仅一次 Quiz**，**无作业、无考勤考核** |
| └ CA Part 2（后半 ML 部分） | **30%** | 由后半任课教授安排（待后续课件确认） |
| **Final Exam 期末** | **60%** | 3 小时，覆盖全课程所有内容 |

#### 关键：前 4 周（Lim 部分）的考核

- **只有一次 Quiz，占 10%**，在 **Week 4**（Lim 部分结束时）进行。
- **闭卷（closed book）**、受控环境、书面作答（在控制环境下的 written quiz）。
- **没有作业**（no homework），**不考核出勤**（attendance 不计入 CA，来否自便）。
- 期末考试占大头（60%），需掌握全课程内容；CA 可拉分也可能保底，老师期望 CA 能帮你提分而非拉分。

> 提示：前 4 周内容"贴近生活、可关联实际"，重在理解思路而非刷题；通过实例掌握 GA/EC 的动机与问题建模方式即可应对 quiz。

### 3. 问题的四种分类视角（本周核心知识内容）

课程先教你**理解问题**再谈算法。从四个角度对问题分类：

#### 3.1 Black Box Model（黑箱模型）

把问题求解系统拆成三部分：**input（输入）— model（模型/技术）— output（输出）**。哪一部分"缺失"决定问题类型：

- **缺 input（找最佳输入）→ 优化问题 (Optimization)**
  - 已知 model 与期望 output，求 input。
  - 例子：大学排课、呼叫中心/医院排班、设计规格、TSP（旅行商问题）、八皇后问题、卫星结构设计（最大化隔振）。
  - 关键：优化问题总由**目标 (objective)** 驱动；**fitness（适应度）** 与目标值紧密相关（如卫星设计的 fitness = 抗振能力）。
  - **Evolutionary creativity（进化创造性）**：GA 因随机生成解，常产出人意料的、与已知方案很不同的解 → 这就是"创造性"，可用于时尚设计、珠宝设计、进化艺术等。
- **缺 model（找模型）→ 建模问题 (Modelling)**
  - 已知 input-output 对，求能对每个已知 input 给出正确 output 的模型。
  - 例子：训练神经网络（找权重）、进化机器学习、股价预测（时间序列建模）、智能家居语音控制、贷款人信用评估。
  - **建模问题可转化为优化问题**（如把 NN 训练看成最小化误差的优化）。
- **缺 output → 仿真问题 (Simulation)**
  - 已知 input 和 model，求 output（"what-if" 分析）。
  - 例子：进化经济学、人工生命、天气预报系统、新税制影响分析、人工社会演化。
  - 与优化/建模不同：仿真不搜索巨大解空间，而是给定输入看输出。

#### 3.2 Search Problems（搜索问题视角）

- 把求解视为在**搜索空间 (search space)** 中找解。
- 关注：搜索空间多大、多复杂（如 TSP 的 n 城市有 n! 量级可能路线）。
- 区分：**search problem**（定义搜索空间）vs **problem-solver**（如何在空间中移动寻解）。

#### 3.3 Optimization vs. Constraint Satisfaction（优化 vs 约束满足）

- **Objective function（目标函数）**：给一个可能解赋一个反映其质量的值。
- **Constraint（约束）**：二元判断（是/否），不可"半满足"。
- 两者组合成四类问题：

| | 有约束 | 无约束 |
|---|---|---|
| **有目标函数** | **Constrained Optimization (COP)** 约束优化 | **Free Optimization (FOP)** 自由优化 |
| **无目标函数** | **Constraint Satisfaction (CSP)** 约束满足 | "No problem"（非问题） |

- 约束还可分：
  - **Hard constraints（硬约束）**：不可协商，必须满足（如房间数固定）。
  - **Soft constraints（软约束）**：最好满足，不满足仍是可行解（如连续 8 小时排课不理想但仍可行）。
- **N-Queens 课堂投票示例**（用八皇后问题演示 CSP/COP/FOP 判定）：
  1. "放置 n 皇后使 ≥98% 非攻击" → **CSP**（约束满足，须达 98% 这条硬要求）。
  2. "最大化非攻击皇后数" → **FOP**（纯目标驱动）。
  3. "随机初始、每后只动一次、移动步数最小且非攻击最大化" → **COP**（约束 + 目标，类似 **local search 局部搜索**；实例：送货路线遇路障做最小调整）。
  4. "固定 3 个皇后后，在限定计算时间/迭代数内最大化非攻击数" → 可视为 **FOP**（因强调"在有限时间内最大化"）。

#### 3.4 NP Problems（按问题难度/复杂度分类）

适用于**组合/离散优化**问题（离散值如整数；连续变量属另一类）。

- **问题规模 (problem size)**：维度/变量取值数（如 TSP 城市数 n）。
- **运行时间 (running time)**：算法终止所需操作数，取最坏情况关于 n 的函数：**polynomial / super-polynomial / exponential**。
- **问题归约 (problem reduction)**：把一个问题映射成另一个（若映射在多项式时间内完成则可复用已有算法）。
- 复杂度类：
  - **Class P**：可在多项式时间内求解（易，如排序）。
  - **Class NP**（非确定性多项式）：给定解可在多项式时间内**验证**；P ⊆ NP。
  - **NP-complete**：属 NP，且**所有** NP 问题都可多项式归约到它。
  - **NP-hard**：至少与 NP-complete 一样难，但解不一定能在多项式时间内验证（如 TSP 求"最优"距离——要证明最优需遍历整个空间）。
- **P vs NP**：是否 P≠NP 尚未证明；普遍接受 P≠NP。本课对 NP-hard 问题采用**近似算法与元启发式（metaheuristic）**——GA 即一种 metaheuristic（"关于启发式的启发式"，基于自然隐喻）。
- **Garey & Johnson 经典寓言**：老板让你设计高效算法，你三种回答——"我太笨"/"不存在这样的算法"/"所有名人都做不出"——后两者更能保住工作。说明**先理解问题复杂度再动手**很重要。

### 4. 进化计算 (EC) 的起源与生物启发

#### 4.1 历史脉络（Historical perspective）

- 1948 Turing 提出 "genetical or evolutionary search"。
- 1962 Bremermann 研究通过进化与重组优化。
- 1964 Rechenberg 提出**进化策略 (evolution strategies)**。
- 1965 Fogel, Owens & Walsh 提出**进化规划 (evolutionary programming)**。
- **1975 Holland 提出遗传算法 (GA)**——**转折点**：用二进制串编码解、种群、通过**crossover（交叉）**与 mutation 繁衍；crossover 是其核心新颖之处。
- 1992 Koza 提出**遗传编程 (genetic programming, GP)**——编码为程序/树/状态机（与 GA 的主要区别）。

#### 4.2 生物启发之一：达尔文进化 (Darwinian Evolution)

- 世界资源有限 → 种群规模受限；生命本能驱动**繁殖**；**竞争**最强者获得更多繁殖机会 → **选择 (selection)**。
- **Fitness（适应度）**：派生的次级度量，后代多者视为更 fit。
- **Phenotypic traits（表型性状）**：影响环境响应的行为/物理差异，部分遗传、部分发育、部分随机；利于繁殖且可遗传的性状在后代增多。
- 要点：种群含多样个体；更适应的性状组合占比增大；**个体是选择单位 (unit of selection)**；随机变异维持多样性；**种群是进化单位 (unit of evolution)**——进化指整个种群随时间的变化。

#### 4.3 生物启发之二：遗传学 (Genetics)

- DNA 含构建生物体的信息；**基因型 (genotype) 决定表型 (phenotype)**；映射复杂：
  - **Pleitropy（基因多效性）**：一个基因影响多个性状。
  - **Polygeny（多基因性）**：多个基因影响一个性状。
- 基因编码在 DNA 链即**染色体 (chromosome)** 上；多数细胞含两套染色体（**diploidy 二倍体**）；个体全部遗传物质 = **genome（基因组）**。
- **Mutation（突变）**：复制时遗传物质可能小变化；后果可能是灾难性（不可活）、中性、或有利；遗传密码冗余支持差错校验。

#### 4.4 EC 隐喻回顾 (Recap)

种群在有限资源环境中 → 竞争选出更适应者 → 经**recombination（重组/交叉）与 mutation（变异）**产生新一代 → 评估并再次竞争 → 自然选择使种群 fitness 随时间提升。这正是 GA 算法构造的依据（下讲展开 EA 的具体算子）。

### 5. 其他提示

- 老师可邮件联系（emhlim@ntu.edu.sg），回复可能不快，急可再发提醒；也可到办公室面谈。
- GA/EC 思想非全新，但 1975 Holland 提出后才流行；受限于早期算力，80 年代起才大规模仿真验证其潜力。
- 课堂用 QR code 投票（poll）帮助理解 CSP/COP/FOP 判定。

---

> **下一周预告**：Week 2 将进入**进化算法 (EA) 的具体构造**——编码、种群、选择、交叉、变异等算子的实现。
