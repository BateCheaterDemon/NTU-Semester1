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
- **参考论文**：`week1/IJCAT NQ.pdf` — Bah-Hwee Gwee & Meng-Hiot Lim, *An evolution search algorithm for solving N-queen problems*, IJCAT 2003。演示 N-queens 的 GA 求解（N-permutation 编码、适应度度量、可解到 2000 皇后），与课程 N-Queens 主题直接相关。

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

## Week 2 — 进化算法 (EA) 框架 + 算子 + Eight-Queens/SGA 建模实例

> **权威来源说明**：本周仍用 Week 1 的官方课件 `week1/L1(2-1).pdf`（第 34–72 页，作者 Meng-Hiot Lim），无新课件。转写 `week2/week2.txt` 噪声较多，以 PDF 为准。本周典型错拼修正：
> - "Rul hw / Ruled wheel / Rule view / ult wheel / Ruleth" → **roulette wheel**（轮盘赌）
> - "low side L OCI" → **loci**（locus 的复数）；"all / allege / allo" → **allele**
> - "eight quin / Queensb / Qin" → **eight queens**；"veristy / verity / eth / Arty" → **arity**
> - "Dubinim / neo Dubinim" → **Neo-Darwinism**；"meting of the fits" → **mating of the fittest**
> - "survival of the fits / fitters" → **survival of the fittest**
> - "memetic / mimetic" → **memetic algorithm**；"Gb / Ober" → **Goldberg**
> - "figure of merit" → figure of merit；"NT n / NTN" → **NTULearn**

### 1. 本周主线

Week 1 回答"如何**理解**问题"（black box / search / optimization-vs-constraint / NP 四视角）。本周回答"如何**构造**求解器"——把自然进化隐喻落实成可编程的 **Evolutionary Algorithm (EA)** 框架，并拆解其六大组件（representation / evaluation / population / parent selection / survivor selection / recombination / mutation），最后用 **eight-queens** 与 **SGA f(x)=x²** 两个完整手算实例串起来。

### 2. EA 框架：三实体 + 两股力

#### 2.1 三实体与流程

EA 只有三个实体：**population（种群）→ parents（父代）→ offspring（子代）**，实体间靠"变换"衔接：

```
Initialization → [Population] → Parent selection → [Parents]
   → Recombination(crossover) + Mutation → [Offspring]
   → Survivor selection → [新 Population] → … → Termination
```

伪代码：`initialize → evaluate`；然后循环 `select parents → recombine → mutate → evaluate → select survivors`，直到终止条件。

- **Population size 固定**（多数 EA）：父代+子代总数常超过定值，故需 survivor selection 决定谁进下一代。
- EA 属 **"generate and test"** 类算法：随机生成候选、用 fitness 检验、再驱动选择。
- **parallel search（并行搜索）**：种群=对搜索空间的多点采样，故 GA 本质是并行算法（虽在串行机上仿真，但可逐个体并行处理，难点在信息交换策略）。
- **Neo-Darwinism**：自然进化推动物种向"更高生命形式"（更适应环境）演化；在算法里则等价于"按 fitness 在 fitness landscape 上做 optimization"。两者同构但语境不同。

#### 2.2 ⭐ 两股力（two pillars / competing forces）——EA 调参的本质

| 力 | 作用 | 由谁驱动 | 效果 |
|---|---|---|---|
| **增加多样性** | 探索 novelty（exploration） | mutation + recombination | 注入随机性、跳出 local optimum |
| **减少多样性** | 聚焦 quality（exploitation） | parent selection + survivor selection | 让更优个体占更大比例 |

- **好优化 = 平衡这两股力**。若有人说"GA 不收敛"，本质是多样性没平衡好——调高 mutation/recombination 概率即可。
- 单 hill-climber 只有一个解不断改进；GA 用种群多点采样，故更不易困在 false peak。

### 3. Representation（表示）——解题第一步

接手任何问题，用 GA 第一件事是**如何编码解**。

#### 3.1 两层存在与两个映射

- **phenotype（表型）**：原问题真实世界中的解（如棋盘配置、TSP 路线）。
- **genotype（基因型）**：算法里操纵的编码，即"digital DNA"。
- **Encoding（编码）**：phenotype → genotype（可多对一，即同一问题可有多种表示）。
- **Decoding（解码）**：genotype → phenotype，**必须一对一**（一个编码不能歧义解释）。
- **目标**：genotype 空间必须能表示**所有**可行解，否则找不到 global optimum。

#### 3.2 术语（考试要分清）

- **chromosome（染色体）**：一条 DNA 串，含多个 **gene（基因）**。
- gene 在串上的位置叫 **locus（单数）/ loci（复数）**，gene 的取值叫 **allele（等位基因）**。
- 例 TSP 五城市编码 `5 4 3 2 1`：gene number 2 的 **locus** 是第 2 位，其 **allele** 是 4；gene 4 的 allele 是 2。
- 二进制编码例：phenotype 整数 18 ↔ genotype `10010`；9 ↔ `1001`；2 ↔ `10`。

#### 3.3 不同表示对应不同历史流派

| 表示 | 历史 EA 流派 |
|---|---|
| 二进制串 | **Genetic Algorithms (GA)** |
| 实值向量 | **Evolution Strategies** |
| 有限状态机 (FSM) | **Evolutionary Programming** |
| LISP 树/程序 | **Genetic Programming (GP)** |

现代观点：**按问题选表示 → 按表示选 variation operator**；selection 只用 fitness，与表示无关，故可通用。

### 4. Evaluation / Fitness Function

- role：代表"要解决的任务/环境"；为 selection 提供比较依据。又叫 **quality function / objective function**。
- 给每个 phenotype 赋**单一实值 fitness**；**区分度越大越好**（不同个体尽量有不同 fitness 值）。
- 通常**最大化** fitness；minimization 问题转 maximization 很简单。
- ⭐ **fitness 是"真实问题"与"算法"之间的唯一桥梁**：GA 本身不在乎问题多复杂，只要有 encoding/decoding + fitness 就能跑——它只在 fitness 数值上驱动选择。这是 GA 通用性的来源。

### 5. Population

- 形式上是 individual 的 **multiset（多重集，允许重复）**。
- population 是 **evolution 的单位**（个体不"进化"，种群才进化）；selection 作用在 population 层，**variation 作用在 individual 层**。
- **diversity（多样性）** 可指三种不同含义，需说清是哪一种：**fitness 多样性 / phenotype 多样性 / genotype 多样性**（基因值很接近但解码后 phenotype 差异可能很大）。
- 高级 EA 可给 population 加空间结构（如 grid）。

### 6. Selection Mechanism

#### 6.1 Parent selection（通常 stochastic）

- 高质量个体更可能被选，但**不保证**；最差个体通常也有**非零概率**——这种随机性有助**跳出 local optima**。
- **Roulette wheel selection（轮盘赌）**：轮盘 slot 大小 ∝ fitness。
  - 例 A=3, B=1, C=2，总和 6 ⇒ A 占 50%、B 占 17%、C 占 33%。转盘选，A 概率最高。又叫 **biased roulette wheel（偏向高 fit）**。
- **Ranking selection（排名选择）**：按 fitness 排名，弱化绝对差异（差 0.001 也分高低，但不放大绝对值偏差）。

#### 6.2 Survivor selection（通常 deterministic）

- 因种群大小固定，要从 (parents + offspring) 合并池中选出下一代。
- **Fitness-based**：合并后按 fitness 排序取前 N（新种群可含 offspring 与 parents）。
- **Age-based**：生多少子代就删多少父代。
- **Elitism（精英保留）**：stochastic 与 deterministic 混合，保住最优不丢。

### 7. Variation Operators（变异算子）

按 **arity（输入个体数）** 分类：

| arity | 算子 | 说明 |
|---|---|---|
| 1 | **mutation** | 作用于 1 个 genotype，小随机扰动 |
| >1 | **recombination** | 合并多亲本信息；arity=2 即 **crossover**；arity>2 少用 |

- variation operator **必须匹配 representation**。
- **mutation vs recombination 谁更重要？** 都重要。但若**只能留一个**，**只有 mutation 能独立求解**（早期 evolution strategies / evolutionary programming 基本只靠 mutation）。recombination 需配合 mutation 用。
- **mutation**：binary 串上以小概率（如 1%）逐 gene 翻硬币，命中则 0↔1 翻转——改动很小，但可能引起 phenotype 巨变；随机性是它与其它 unary 启发式的本质区别；可保证搜索空间连通性。
- **recombination/crossover**：≥2 亲本，传递 traits（一种"学习"）；定义 **crossover site（切点）**，切后互换。
  - 例 `1 1 1 | 1 1 1 1` + `0 0 0 | 0 0 0 0` → `1 1 1 0 0 0 0` + `0 0 0 1 1 1 1`。

### 8. Initialization & Termination

- **Initialization**：
  1. **随机**：最常用，天然带来多样性；虽初始质量差，但进化会变好。
  2. **用 prior knowledge / 启发式 seed**：初始质量高，但**把搜索限制在局部空间**——利于找 local optimum，却可能远离 global optimum。故做**全局优化时不宜过度 seed**。
- **Termination**：达到目标 fitness / 最大代数 / 最小多样性（steady state）/ 连续 N 代无 fitness 改进（**convergence**，如 best fitness 卡在 0.98 持续 50 代）。

### 9. ⭐ 实例一：Eight-Queens 完整建模

问题：8×8 棋盘放 8 皇后互不攻击（同行/同列/同对角线即冲突）。目标可表述为"最小化冲突数"或"最大化非攻击皇后数"。

#### 9.1 Representation

- phenotype = 棋盘配置；genotype = **1–8 的 permutation**（整数编码，比二进制更自然）。
- 约定 **gene = column（列号位），allele = row（行值）**（也可反过来 gene=row, allele=column，等价）。
  - 如 `1 3 5 2 6 4 7 8`：gene 4 的 allele = 2；gene 7 的 allele = 7。
- ⭐ 由于是 permutation（alleles 互异），**同列约束天然满足**；gene 位置只有 8 个故**同行约束也天然满足**——剩下只需查**对角线冲突**。这是表示选择"顺便"消化了约束，降低 fitness 计算复杂度。

#### 9.2 Fitness 公式推导

设配置 $Q=(Q_1,\dots,Q_8)$，$Q_i$ 为第 $i$ 行皇后所在列。冲突计数：

$$
C(Q)=\sum_{i=1}^{8}\sum_{k=i+1}^{8}\delta_{ik},\qquad
\delta_{ik}=\begin{cases}1,& |Q_i-Q_k|=|i-k|\ (\text{同对角线})\\0,&\text{otherwise}\end{cases}
$$

- $|Q_i-Q_k|=|i-k|$ 即行列差相等 ⇒ 在同一对角线 ⇒ 冲突，记 1 分 penalty（取 $\delta=1$）。
- **最坏情况**（全部在同一对角线）冲突数 $=7+6+5+4+3+2+1=28$。
- 归一化 fitness 到 $[0,1]$（1 最优、0 最差）：

$$
\text{fitness}(Q)=1-\frac{C(Q)}{28}
$$

- $C(Q)=0$（无冲突，即解）⇒ fitness=1。一般问题若不知最大冲突数，可除以一个大常数 $M$。

#### 9.3 算子（permutation 表示下）

- **Mutation**：交换一对 allele（如把 gene 3 的值与随机选的值互换），保持仍是 permutation。
- **Recombination（permutation crossover）**：选 crossover site，第一段从 parent1 复制，第二段按 **parent2 中出现的顺序**填入、**跳过已有值**。
  - 例 `1 3 5 | 2 6 4 7 8` + `8 7 6 5 4 3 2 1` → `1 3 5 4 2 8 7 6`（后半 4,2,8,7,6 取自 parent2 的顺序，跳过已出现的 1,3,5）。
  - offspring 从 parent1 继承前段、从 parent2 继承"顺序"——对**顺序/序列决定解质量**的问题尤其重要。
- **Selection**：可用 roulette wheel；也可"随机挑 5 个亲本取最优 2 个做 crossover"。Survivor 通常 deterministic（按 fitness）。

### 10. ⭐ 实例二：SGA 手算 $f(x)=x^2$（Goldberg 经典）

最大化 $f(x)=x^2$，$x\in\{0,\dots,31\}$ 整数。6 步手算：

1. **Encoding**：5-bit 二进制（$0$–$31$）。
2. **Initial population**（随机，size=4）：
3. **Decode + evaluate**：

| 串 | 解码 $x$ | fitness $f(x)=x^2$ | 占比 |
|---|---|---|---|
| 01101 | 13 | 169 | 14.4% |
| 11000 | 24 | 576 | 49.2% |
| 01000 | 8 | 64 | 5.5% |
| 10011 | 19 | 361 | 30.9% |
| **合计** | | **1170**（avg 293） | |

4. **Selection（roulette wheel）**：按 fitness 比例分配进入 mating pool 的 copy 数。最 fit 的 `11000` 得 2 份，其余各 1 份（`01000` 因占比最低得 0 份），pool ≈ {`01101`,`11000`,`11000`,`10011`}。
5. **Crossover**：随机配对 + 随机切点（gene 4）。例 `01101`+`11000` 在切点 4 互换 → 子代 `01100`（=12）。
6. **Mutation**：$p_{mut}=0.001$，种群共 20 bit ⇒ 期望 0.02 bit 翻转 ⇒ 本代几乎不变。

**子代评估**（据转写手算结果）：含 `01100→12→144` 等，**total=1754, avg=439**（远高于初代 1170/293）。

> **观察**：仅一代，种群平均 fitness 显著上升——源于**选择压力**（高 fit 个体多复制）+ **recombination**（组合双亲好的片段）。多代后 fitness 持续爬升。终止条件常用：达到代数上限 / 目标 fitness / 连续若干代无改进。

### 11. EAs 作为问题求解器：性能视角

#### 11.1 Goldberg view (1989)

横轴=所有问题，纵轴=performance：

- **random search**：全域都一般，最低。
- **problem-specific custom method**：在窄域极高、他域很差（一个尖峰）。
- **GA**：全域都还不错，普遍优于 random search ⇒ **robust**。

#### 11.2 90s 趋势：curve deformation（曲线变形）

给 EA 注入 **domain knowledge**（特殊算子、repair 等）→ 在目标问题子集性能更好、他域更差，曲线"变形"成更窄更高的峰。这一分支即 **memetic algorithm（模因算法，EA + local search，老师创办了相关期刊）**。

#### 11.3 Michalewicz view (1996)

不同 EA（EA1–EA4）在不同问题域高低各异——没有单一 EA 通吃。

#### 11.4 ⭐ No Free Lunch Theorem（无免费午餐定理）

跨**所有**问题取平均，**所有算法（含 random search）性能相同**。

- 推论：**不存在万能的 all-purpose 算法**；追求某一类问题的高性能必然牺牲适用范围。
- 现代 theory 据此认为"寻找通用算法"是 fruitless 的。

### 12. EC vs Global/Local Optimization

| 路线 | 特点 | 哲学 |
|---|---|---|
| **Deterministic**（branch and bound / box decomposition） | 保证找 $x^*$，但运行时可能 super-polynomial，复杂问题常不适用 | "I don't care if it works as long as it **converges**" |
| **Heuristic / GA (generate and test)** | 无最优保证、无运行时界，但实用、能在合理时间找到很好解 | "I don't care if it **converges** as long as it **works**" |
| **Neighbourhood / local search (hill-climber)** | 给搜索空间加邻域结构，保证局部最优；但问题常含多个 local optima | — |

- **EA 的区分性特征**：用 population、多个 stochastic 搜索算子、尤其 arity>1 的 variation、stochastic selection。
- GA 与 neighbourhood search 常混合 → memetic algorithm。

### 13. ⭐ Quiz 具体安排（Week 2 末尾宣布，重要）

本周最后老师宣布了前半学期唯一一次 Quiz 的具体细节（与 Week 1 笔记的"Week 4 闭卷 Quiz 10%"一致，现补充）：

| 项目 | 内容 |
|---|---|
| **日期** | **9 月 1 日（周一，Week 4，Lim 部分最后一周）** |
| **时间** | **9:30 – 10:30**（因课后时段通常无课，便于订场地） |
| **时长** | 约 **15 分钟** |
| **考场** | **三个**：LT 19A（即上课的 LT）、LT 2A、LT 5。具体去哪个考场在 **NTULearn** 公布 |
| **规则** | 隔座就坐（相邻留空位）；带 **ID + 笔**；**不需要计算器**（题目会设计成无需计算器）；**手机及智能设备严禁** |
| **形式** | **闭卷**、受控环境、书面作答（与 Week 1 所述一致） |

> 提醒：前 4 周**无作业、不考核出勤**，整个 CA Part 1 只靠这一次 Quiz（10%）。务必按上述考场与规则参加。

### 14. 本周要点小结

- **EA 框架**：population→parents→offspring 三实体；伪代码 initialize→evaluate→循环(select→recombine→mutate→evaluate→survive)→terminate。
- **两股力**：mutation+recombination 增多样性（explore）vs selection 减多样性（exploit）；调参=平衡二者。
- **Representation**：phenotype/genotype、encoding(可多对一)/decoding(必须一对一)；术语 chromosome/gene/locus/allele。
- **Fitness** 是问题与算法的唯一桥梁；通常 maximize；区分度越大越好。
- **Selection**：parent 随机（roulette wheel / ranking，最差也有非零概率），survivor 确定性（fitness-based / age-based / elitism）。
- **Variation**：arity1=mutation（可独立求解、跳局部最优），arity≥2=recombination/crossover（传 traits）。
- **实例**：eight-queens（permutation 表示+对角线冲突公式+fitness=1−C/28）、SGA x²（一代后 avg fitness 293→439）。
- **性能观**：Goldberg(GA 稳健)>random；加 domain knowledge→curve deformation/memetic；**No Free Lunch**：跨所有问题平均所有算法相同。
- **Quiz**：9 月 1 日 9:30–10:30，三考场，闭卷，带 ID+笔，不需计算器，禁手机。

---

> **下一周预告**：Week 3 将临近 Week 4 的 Quiz（**9 月 1 日**），预计继续 EA 的算子细节与实操/调参，并进入复习；具体主题以课件为准。
