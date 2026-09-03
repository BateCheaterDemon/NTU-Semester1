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

## Week 2 — 进化算法 (EA) 框架 + Representation/Mutation/Recombination 算子 + Eight-Queens/SGA 建模实例

> **权威来源说明**：本周官方课件为 `week2/L2(2-1).pdf`（**Representation, Mutation, and Recombination**，作者 Meng-Hiot Lim，59 页），并对照 `week1/L1(2-1).pdf` 后段框架页。转写 `week2/week2.txt` 噪声较多，以 PDF 为准。本周典型错拼修正：
> - "Rul hw / Ruled wheel / Rule view / ult wheel / Ruleth" → **roulette wheel**（轮盘赌）
> - "low side L OCI" → **loci**（locus 的复数）；"all / allege / allo" → **allele**
> - "eight quin / Queensb / Qin" → **eight queens**；"veristy / verity / eth / Arty" → **arity**
> - "Dubinim / neo Dubinim" → **Neo-Darwinism**；"meting of the fits" → **mating of the fittest**
> - "survival of the fits / fitters" → **survival of the fittest**
> - "memetic / mimetic" → **memetic algorithm**；"Gb / Ober" → **Goldberg**
> - "figure of merit" → figure of merit；"NT n / NTN" → **NTULearn**
> - "fitters" → fittest；"algor m / algorm" → algorithm；"etionary strategy / programming" → evolution strategies / evolutionary programming

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

### 7. Variation Operators（变异算子）— 按 arity 分类

按 **arity（输入个体数）** 分类：

| arity | 算子 | 说明 |
|---|---|---|
| 1 | **mutation** | 作用于 1 个 genotype，小随机扰动 |
| >1 | **recombination** | 合并多亲本信息；arity=2 即 **crossover**；arity>2 少用 |

- variation operator **必须匹配 representation**——这是本周 Lecture 2 的主线：不同表示有不同 mutation/crossover 实现。
- **mutation vs recombination 谁更重要？** 都重要。但若**只能留一个**，**只有 mutation 能独立求解**（早期 evolution strategies / evolutionary programming 基本只靠 mutation）。recombination 需配合 mutation 用。
- **Crossover OR mutation（PDF 三页结论，重要）**：
  - **mutation-only EA 可行；crossover-only EA 不可行**（crossover 不改变 allele 频率——例：首 bit 50% 为 0 的种群做任意次 crossover，0 的比例不变；要达到 optimum 常需一次 lucky mutation）。
  - **exploration vs exploitation**（PDF 的另一种分工视角，与 §2.2 的"两股力"互补）：
    - **Crossover is explorative**：跳到两亲本"之间"的某区域，大跳跃。
    - **Mutation is exploitative**：在亲本附近做小幅扰动，就地优化。
  - 两者既有 **co-operation 又有 competition**。
- **mutation**：binary 串上以小概率逐 gene 翻硬币，命中则 0↔1 翻转——改动很小，但可能引起 phenotype 巨变；随机性是它与其它 unary 启发式的本质区别；可保证搜索空间连通性。
- **recombination/crossover**：≥2 亲本，传递 traits（一种"学习"）；定义 **crossover site（切点）**，切后互换。
  - 例 `1 1 1 | 1 1 1 1` + `0 0 0 | 0 0 0 0` → `1 1 1 0 0 0 0` + `0 0 0 1 1 1 1`。

---

### 7A. ⭐ 五种 Representation 下的算子详解（Lecture 2 核心，按 PDF 顺序）

> 建立任何 GA，**先选表示 → 再按表示选 variation operator**。selection 只用 fitness，与表示无关，故通用。下表汇总五种主流表示及其 mutation/crossover。

#### 7A.1 Binary Representation（二进制，最早最经典）

genotype = 二进制串。历史对应 **Genetic Algorithms (Holland 1975)**。

- **Mutation**：逐 gene 独立以概率 $p_m$（mutation rate）翻转 0↔1。$p_m$ 通常取 **1/pop_size 到 1/chromosome_length** 之间。
  - 单点翻转可能引起 phenotype 巨变 → 可用 **gray coding（格雷码）** 缓冲（相邻整数二进制只差 1 bit，减小 Hamming cliffs）。
- **1-point crossover**：随机选切点，两亲本交换尾部产生两子代。$p_c$ 通常 **0.6–0.9**。
- **n-point crossover**：选 n 个切点，沿切点交替拼接两亲本片段（1-point 的推广，仍有 positional bias）。
- **Uniform crossover**：给一个亲本"正面"、另一个"反面"，逐 gene 抛硬币决定第一个子继承谁，第二个子取反；**继承与位置无关**（无 positional bias）。
- **为何需要多种 crossover？** 1-point 的性能**依赖表示中变量的排列顺序**——相邻 gene 更易被一起保留，但**永远无法同时保留串两端的 gene**。这叫 **Positional Bias（位置偏置）**：若了解问题结构可利用之，否则换用 n-point / uniform。

#### 7A.2 Integer Representation（整数）

现代认为数值变量直接编码（整数/浮点）更好；图像处理参数等天然整数；类别变量取自固定集（如 {blue, green, yellow, pink}）。

- **Crossover**：直接复用 binary 的 n-point / uniform。
- **Mutation**（bit-flip 的推广）：
  - **Creep mutation（爬行）**：以概率 $p$ 给每个 gene 加一个小整数（正或负），倾向于移到**相近值**。
  - **Random resetting（随机重置）**：以 $p_m$ 给 gene 随机选一个新值（类别变量尤其用此）。
- **图着色（graph coloring / k-colouring）** 是典型整数表示应用：找最小颜色数 k 使相邻区域不同色。问"k=3 时编码？目标函数？能否解？k=4 时改写？"——常见建模练习。

#### 7A.3 Real-Valued / Floating-Point Representation（实值/浮点）

对应连续参数优化 $f:\mathbb{R}^n\to\mathbb{R}$（如 Ackley function，EC 常用 benchmark）。

- **Mapping real values on bit strings**（二进制近似实值）：区间 $[x,y]$ 用 L-bit 串 $\{a_1,\dots,a_L\}\in\{0,1\}^L$ 表示，须 **one phenotype per genotype**（可逆）：

$$
g(a_1,\dots,a_L) = x + \frac{y-x}{2^L-1}\sum_{j=0}^{L-1} a_{L-j}\cdot 2^j \in [x,y]
$$

  - 仅 $2^L$ 个离散值代表无穷集；**L 决定最大精度**——精度高则 chromosome 长、进化慢。
  - 例 $A=\langle1000100011\rangle$，$z\in[0.25,1.88]$ → 求 $g(A)$（按公式代入）。

- **Uniform Mutation**：$x'_i$ 从 $[LB_i, UB_i]$ 均匀随机抽取（类比 binary bit-flip / integer random resetting）。
- **Non-uniform Mutation**：给每变量加随机扰动，最常见为加 **$N(0,\sigma)$ 高斯扰动**后截断到范围：

$$
x'_i = x_i + N(0,\sigma)
$$

  - 标准差 $\sigma$ 是 **mutation step size**，控制变化幅度（约 2/3 的采样落在 $[-\sigma,+\sigma]$）。
- **Self-Adaptive Mutation（自适应变异，重要）**：把 step size $\sigma$ 也编入 genome $\langle x_1,\dots,x_n,\sigma\rangle$，让 $\sigma$ **自己参与变异与选择**、随进化协同演化（用户不手动设）。
  - **顺序很重要**：先变 $\sigma\to\sigma'$，再用新 $\sigma'$ 变 $x\to x'=x+N(0,\sigma')$。原因：新 $\langle x',\sigma'\rangle$ 被**双重评估**——主：$x'$ 好当 $f(x')$ 好；次：$\sigma'$ 好当它产生的 $x'$ 好。反过来变则失效。

- **Crossover（实值专用，重要考点）**：
  - **Discrete**：每 allele 从一亲本取，$z_i=x_i$ 或 $y_i$（可用 n-point/uniform）。
  - **Intermediate（= arithmetic recombination）**：$z_i=\alpha x_i+(1-\alpha)y_i$，$\alpha\in[0,1]$。$\alpha$ 可为常量（**uniform arithmetical crossover**）、随种群年龄变、或每次随机取。
  - **Single arithmetic crossover**：随机选一个 gene $k$，子1为 $x_1,\dots,x_{k-1},\alpha y_k+(1-\alpha)x_k,x_{k+1},\dots,x_n$（子2反之）。
  - **Simple arithmetic crossover**：随机选 gene $k$，$k$ 之前保持亲本1，$k$ 及之后混合：$\dots,\alpha y_k+(1-\alpha)x_k,\dots,\alpha y_n+(1-\alpha)x_n$。
  - **Whole arithmetic crossover**：**最常用**，全分量混合 $z_i=\alpha x_i+(1-\alpha)y_i$（子2反之）。
  - **Blend Crossover (BLX)**：设 $x_i<y_i$，$d_i=y_i-x_i$，$z_i\in[x_i-\alpha d_i,\, x_i+\alpha d_i]$ 均匀采样；原作者最佳结果用 $\alpha=0.5$。
  - 几何含义（PDF Fig.28）：single/simple/whole arithmetic 落在 inner box（$\alpha=0.5$），blend crossover 落在 outer box（范围更宽）。
- **Multi-parent recombination（多亲本重组）**：不受自然限制，mutation 用 1 亲本、传统 crossover 用 2，推广到 $n>2$ 自 1960s 起即有，仍少用但研究表明有用。两类：
  - **Type 1（分段重组）**：diagonal crossover 对 n 个亲本选 n−1 个切点，沿"对角"拼接 n 个子代——推广 1-point crossover。
  - **Type 2（算术组合）**：子代第 i 个 allele = n 个亲本第 i 个 allele 的平均 → 产生"质心"子代。GA 中少见，但 evolution strategies 早已使用。

#### 7A.4 Permutation Representation（排列，对应 TSP / 排序类问题）

n 个变量排成 n 个整数、每个恰好出现一次。两类关注点：
- **生产调度**：关心**顺序**（谁先于谁）。
- **TSP**：关心**邻接**（谁挨着谁）。
- search space 极大：30 城市 ≈ $30!\approx10^{32}$ 种 tour。
- **为何不能用普通算子？** bit-wise mutation 改一个值会重复（某值出现两次、某值消失）→ 不可行解。故须至少改两个值，并采用专用算子。

**Mutation（四种）：**

| 算子 | 操作 |
|---|---|
| **Swap mutation** | 随机选两个 allele 交换位置 |
| **Insert mutation** | 随机选两个 allele 值，把第二个移到紧随第一个之后，其余后移——**保留大部分顺序与邻接信息** |
| **Scramble mutation** | 随机选一个 gene 子集，打乱这些位置上的 allele 重排 |
| **Inversion mutation** | 随机选两个 allele，反转其间子串——**保留大部分邻接**（只断两条链）**但破坏顺序** |

- permutation 下 mutation 概率通常指"某算子作用于**整条串一次**"的概率，而非逐位置。

**Crossover（五种，保留顺序/邻接信息）：**

| 算子 | 核心思想 |
|---|---|
| **Order 1 crossover** | 保留元素出现的**相对顺序**：从亲本1复制一段，余下位置从切点起按**亲本2的顺序**填入（跳过已有、wrap-around），子2对调亲本角色 |
| **Partially Mapped Crossover (PMX)** | 随机选段从 P1 复制；段内 P2 未复制的元素通过映射放回 P2 中对应位置；段外从 P2 填 |
| **Cycle crossover** | 每 allele 连同其**位置**一起继承自一个亲本；构造 P1 的 cycle（首位置→P2 同位→P1 同值位→…回到首位），cycle 内放子1的 P1 位置，交替 cycle 放两子代 |
| **Edge Recombination** | 构造两亲本的**邻接边表**（共同边标 +）；随机选起点，每次优先选共同边或**候选列表最短**的邻接，构造子代 tour |

> 转写中老师手算的 eight-queens permutation crossover（§9.3）正是 **Order 1 crossover**：`1 3 5 | 2 6 4 7 8` + `8 7 6 5 4 3 2 1` → `1 3 5 4 2 8 7 6`（后半 4,2,8,7,6 取自 parent2 顺序，跳过已出现的 1,3,5）。

#### 7A.5 Tree Representation（树，对应 Genetic Programming, GP）

genotype 为非线性的树（GA/ES/EP 的 chromosome 是线性定长结构；GP 的树**可变深宽**）。可表示算术式、逻辑式、程序。

- **定义 symbolic expression**：由 **terminal set T** 与 **function set F**（各 function 有其 arity）递归定义——每个 $t\in T$ 是合法表达式；$f(e_1,\dots,e_n)$ 合法当 $f\in F,\mathrm{arity}(f)=n$ 且各 $e_i$ 合法。
- **closure property**：GP 表达式通常**无类型**，任何 $f\in F$ 可接受任何 $g\in F$ 作参数。
- **Mutation**：随机选子树，用随机生成的新树替换（最常见）。两参数：选 mutation 的概率 $p_m$、选内部点作替换子树根的概率。$p_m$ 建议 **0**（Koza 1992）或极小如 **0.05**（Banzhaf et al. 1998）。子代可能比亲本大。
- **Recombination**：两亲本各随机选子树**交换**。两参数：选 recombination 的概率 $p_c$、在亲本内选内部点作切点的概率。子代可能比亲本大。

### 7B. 五种表示速查表

| 表示 | 历史 EA | Mutation | Crossover |
|---|---|---|---|
| **Binary** | GA | bit-flip（逐位以 $p_m$，范围 1/pop_size–1/len；可用 gray coding） | 1-point / n-point / uniform（$p_c$≈0.6–0.9） |
| **Integer** | — | creep（加小整数）/ random resetting | 复用 binary 的 n-point / uniform |
| **Real-valued** | Evolution Strategies | uniform / non-uniform（Gaussian $N(0,\sigma)$）/ self-adaptive（$\sigma$ 入 genome） | discrete / intermediate（single/simple/whole arithmetic）/ blend（BLX）/ multi-parent |
| **Permutation** | 排序/TSP | swap / insert / scramble / inversion | Order 1 / PMX / cycle / edge recombination |
| **Tree** | Genetic Programming | 子树替换（$p_m$≈0–0.05） | 子树交换 |

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
- **Variation**：arity1=mutation（可独立求解、跳局部最优），arity≥2=recombination/crossover（传 traits）；**mutation-only 可行，crossover-only 不可行**；crossover explorative / mutation exploitative。
- **实例**：eight-queens（permutation 表示+对角线冲突公式+fitness=1−C/28）、SGA x²（一代后 avg fitness 293→439）。
- **⭐ 五种表示的算子**（Lecture 2 新课件）：binary（bit-flip/1-point/n-point/uniform，注意 positional bias、可用 gray coding）、integer（creep/random resetting）、real-valued（Gaussian mutation、self-adaptive $\sigma$、arithmetic/blend crossover）、permutation（swap/insert/scramble/inversion + Order 1/PMX/cycle/edge recombination）、tree（GP，子树替换/交换）。
- **性能观**：Goldberg(GA 稳健)>random；加 domain knowledge→curve deformation/memetic；**No Free Lunch**：跨所有问题平均所有算法相同。
- **Quiz**：9 月 1 日 9:30–10:30，三考场，闭卷，带 ID+笔，不需计算器，禁手机。

---

> **下一周预告**：Week 2 已系统讲完 EA 的 representation 与 variation 算子（crossover/mutation 各表示下的具体操作）。按 Week 1 给出的 EA 框架，剩余核心组件为 **selection**（parent/survivor selection）、**initialization** 与 **termination**，预计 Week 3 进入这些内容并配合实操/调参；Week 3 末临近 Week 4 的 Quiz（**9 月 1 日**），会进入复习。具体主题以课件为准。

---

## Week 4 — Quiz 1 复习周 + 历年真题精讲（无新内容，划定考试范围）

> **权威来源说明**：本周无新课件 PDF，官方课件仍为 `week3/L2(2-1).pdf`（Lecture 2，29 页，slides 1–58 在 Week 2/3 已讲完）。本周录播 `week4/59451 - 0_j0xo2ru3 - PID 117.txt` 为 **Quiz 1 前的复习课**，老师明确说"不覆盖任何新内容"，仅做 recap + 讲解历年真题。转写噪声以课堂口语为主，无术语 PDF 可对照，按语义修正：
> - "Lure / L week" → Lecture（本周 lecture）；"egg birth" → at birth（"假设每个人出生时…")
> - "eight / eight" → 80（resting heartbeat 80 次/分）；"fifty / 50" → 50（g(x) 在 x→1 时趋近 50）
> - "one minus absolute f x -50, y -50 … divided by 70" → fitness $F=1-|f(x)-50|/70$
> - "Anne Queens / Anne / n Qin / en Qin" → **N-Queens**（general n 皇后）
> - "veal value coded" → **real-valued coded**；"aromatic crossover" → **arithmetic crossover**
> - "flexible Alpha / flexible alfa" → **flexible $\alpha$ approach**
> - "apportionment" → apportionment（按比例分配给两亲本）
> - "C n two / C n 2" → $\binom{n}{2}=n(n-1)/2$（最大冲突数）
> - "EE 6227 / 66227" → **EE6227**（本课旧代号，library archive 里的历年真题仍用此号，与 EE6407 等价）
> - "big number three / big three" → Lecture 2/3 的"representation 三讲"收尾点

### 1. 本周性质：复习周，不考新内容

- 老师开篇即明确："I won't cover anything new… whatever you're responsible for is up to what we have covered up to（Lecture 2/3 的 representation 部分）。"
- ⭐ **考试范围红线**：**slide 60 及以后不考**（老师原话："beyond slide 60 and after I won't set any questions on it… slide 60-74 you can put it aside when you study for exam"）。
  - 即：Lecture 2 课件 **slide 1–58 已覆盖**（五种 representation 的算子），**slide 60–74 不考**。
  - 不考的内容（仅作兴趣提及）：fitness rescaling、ranking-based selection 细节、population management 的 distributed/island model 等。
- 本周后半段进行 **Quiz 1**（9:30 开始，闭卷，无计算器，带 photo ID + 笔，三考场，隔座就坐，禁手机/智能设备，违者拍照取证交学校调查）。

### 2. 五种 Representation 的总 recap（老师口述版）

老师用三段 recap 把前三周串起来，强调"每种 representation 有自己独特的 crossover 与 mutation"：

| Representation | 要点回顾 |
|---|---|
| **Binary** | GA 最早的表示，scalable、simple（只有 0/1，变异即翻转）；很多早期 GA 全用 binary |
| **Real-valued** | 现实问题多为连续值，binary 编码会牺牲精度（连续→离散）；mutation/crossover 用 **apportionment parameter $\alpha$**（$\alpha$ 给亲本1，$1-\alpha$ 给亲本2），$\alpha$ 可 fixed / random / adaptive（self-adaptive 把 step size 编入串中） |
| **Integer** | 有限离散值集（如 3 类→{1,2,3}、灰度 1–256、graph coloring 的 4 色）；bin packing 等也用整数 |
| **Permutation** | sequence/ordering 重要的问题（scheduling、TSP、N-Queens）；要求结果**仍是 permutation**——可用专用算子（cycle crossover、edge recombination、PMX、Order 1），也可先做普通算子再 **repair** 修复成 permutation |
| **Tree (GP)** | 进化程序/过程/finite state machines；每个 **subtree 也是 tree**（递归性质）；mutation = 把某 subtree 换成新树，recombination = 两亲本交换 subtree |

> 老师补充：binary 之所以让 GA 流行，是因为"算法要 popular 必须 scalable 且 simple——参数不能太多"；他审稿时见过"听着 elegant 但要调一堆参数"的算法，认为那不是好算法。

### 3. 不考但提及的进阶话题（slide 60+，了解即可）

老师明确这些**不考**，但点出来帮助理解"为什么 GA 还有更多可挖"：

#### 3.1 Fitness 分布与 selection pressure 的关系（启发式思考）

- **早期世代**：fitness 分布**较宽**（个体差异大）→ fitness proportional selection（如 roulette wheel）有效，selection pressure 能区分优劣。
- **后期世代**：fitness 分布**变紧**（质量趋同）→ fitness 差异很小 → roulette wheel 近乎随机选择，**selection pressure 失效**。
- ⚠️ 这正是 Week 2 §10.3 讲的"fitness proportional selection 早晚期的毛病"——本周老师从"fitness 分布宽窄"角度再讲一遍：**fitness 越紧，selection 越不有效**。
- 对策（不考）：**fitness rescaling**（缩放 fitness 拉开差距）、**ranking selection**（只按排名做 preferential selection，忽略绝对差）。

#### 3.2 Population management（不考）

- **Distributed / island model**：把 population 分成若干子群（islands），各 island 独立进化，偶尔交换信息（migration）。
- 属"如何管理 population"的进阶课题。

### 4. ⭐ 历年真题精讲（本场重点）

老师讲了两套 past-year exam questions（均在 library archive，旧代号 **EE6227**），演示"题面长但求解直接"的风格。

#### 4.1 Sem 2 2022 — Q1：Heartbeat Optimization（单变量优化建模）

**题面（长故事）**：假设人出生时心跳总数固定，用完即生命结束。未锻炼者静息心率 80 次/分，锻炼时 120 次/分。设锻炼时间占比为 $x$，则平均心率：

$$f(x) = 120x + (1-x)\,g(x)$$

其中 $g(x)$ 为锻炼占比 $x$ 时的静息心率，要求：$x$ 很小时 $g(x)\to 80$；$x\to 1$ 时 $g(x)\to 50$（锻炼使静息心率下降）。

**Part 1 — 造表求近似最优 $x$**：
- 任选 20 个 $x\in(0,1)$（如 0.01, 0.02, 0.03, 0.04, …），计算 $g(x)$、$f(x)$。
- 找 $f(x)$ 最小者（目标是低静息心率 → 长寿）：表中 $x=0.04$ 时 $f(x)\approx 53.327$ 最小；更精细可取 $x\approx 0.037$–$0.038$。
- 换算成每日锻炼分钟数：$0.04\times 24\times 60 \approx$ **58 分钟/天**。
- 老师点评：这是**单变量 convex landscape**，易解，"not difficult"。

**Part 2 — 写合适的 fitness function**：
- 直接用 $f(x)$ 作 fitness 的问题：心率取值范围很窄（约 50–71），区分度不够，selection 效率低。
- 改进：利用模型下界 $f(x)\ge 50$，定义

$$F(x) = 1 - \frac{|f(x)-50|}{70}$$

- 分母 70（或 75、80，"只要合理都可接受"）用于把 fitness 拉到 $[0,1]$ 并放大差异。
- ⭐ 这体现了 Week 2 §4 的原则：**fitness 区分度越大越好**——当原始值挤在窄区间时，要 rescale 拉开差距。

#### 4.2 Sem 2 2022 — Q1 Part B：问题分类四例

按 black box 的 input-output model 给四个场景分类（Week 1 §3 内容）：

| 场景 | 分类 | 理由 |
|---|---|---|
| 基于 IBM 历史股价预测未来股价（for trading） | **Modelling** | 已知历史 input-output 对，拟合预测模型使预测误差最小化 |
| 把不同尺寸箱子装进卡车 | **Optimization** | 卡车容积固定，目标 = 最小化未填充空间（unfilled space） |
| 国家经济政策制定 | **Simulation** | 给定政策（input）+ 模型，模拟 what-if 结果，看政策是否有 desired effect |
| 保安排班（rostering） | **Optimization**（也可 Simulation） | 适当分配时间/资源；若研究动态环境下的表现则可为 simulation |

> 老师强调："不管选哪个，要给 explanation。"rostering 那题 optimization 与 simulation 都可接受，关键是有合理依据。

#### 4.3 Sem 2 2024 — N-Queens 冲突计数与通用 fitness

**题面**：给定 N-Queens 的 permutation 编码 $Q=(Q_1,\dots,Q_n)$，$Q_i$ 为第 $i$ 个 gene 的 allele（列位置）。伪代码两层嵌套循环计算冲突数：$d_1=|Q_i-Q_j|$，$d_2=|i-j|$，若 $d_1=d_2$ 则 count++。

**(a) 写冲突数方程**（把伪代码翻成数学式）：

$$C(Q)=\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}\delta_{ij},\qquad \delta_{ij}=\begin{cases}1,& |Q_i-Q_j|=|i-j|\ (\text{同对角线})\\0,&\text{otherwise}\end{cases}$$

> 这与 Week 2 §9.2 的八皇后公式完全一致——两层嵌套循环 ↔ 两个 $\Sigma$。

**(b) 对 $Q=\langle 2,7,8,4,6,1,3,5\rangle$ 算 $C(Q)$**：
- 不必画棋盘，直接按方程逐对查：如 gene1=2 与 gene5=6，$d_1=|2-6|=4$，$d_2=|1-5|=4$ ⇒ 冲突。
- 老师示范逐对检查，得 $C(Q)=3$。
- 提示：画棋盘也不扣分，但理解方程后即使 $n=50$ 也能快速算（不用画）。

**(c) 写 general N-Queens 的 fitness function**（多数人卡在这）：
- 关键：分母是**最大可能冲突数**。对 $n$ 皇后，每两后最多冲突一次，共 $\binom{n}{2}=\frac{n(n-1)}{2}$ 对。
- Week 2 八皇后用 28 $=\binom{8}{2}$ 归一化；推广到 general $n$：

$$\boxed{\,F(Q) = 1 - \frac{2\,C(Q)}{n(n-1)}\,}$$

- $C(Q)=0$ ⇒ $F=1$（解）；$C(Q)=\binom{n}{2}$ ⇒ $F=0$（最差）。
- ⭐ **考点**：要从"八皇后分母 28"推广到"general n 分母 $n(n-1)/2$"——会 $C(n,2)$ 这个组合数即可。

#### 4.4 Sem 2 2024 — Real-valued GA 与 flexible $\alpha$ crossover

**题面**：$n=5$ 维函数 $F(x)=\sum_{i=1}^{n}x_i - \sum_{i=1}^{n}x_i^2$，用 real-valued coded GA 优化。两亲本 $A$、$B$（各 5 个分量），用 **flexible $\alpha$ approach** 做 arithmetic crossover：

$$\alpha = \frac{|f(A)-f(B)|}{f(A)+f(B)}$$

（即用两亲本 fitness 的归一化差作 $\alpha$，而非固定 0.5）。求 $F(A), F(B), F(A'), F(B')$（$A',B'$ 为 offspring）。

**Part 1 — 计算**：
- 由 Excel 算得 $f(A)=0.98$，$f(B)=0.67$ ⇒ $\alpha=|0.98-0.67|/(0.98+0.67)$。
- 用 $\alpha$ 做 whole arithmetic crossover：$A'_i=\alpha A_i+(1-\alpha)B_i$（$B'$ 反之），再算 $F(A'),F(B')$。
- 老师点评：计算本身简单，"用计算器即可"，考的是**对 real-valued crossover 的理解**。

**Part 2 — 论证 for / against 这种 crossover（开放式说理题）**：

- **Against（不支持）**：
  - 要算 $\alpha$ 需先算 $f(A),f(B)$，对 **hyper-dimensional** 问题（$n=500$–$1000$）这是显著的额外计算开销（overhead）。
  - GA 要跑很多代、population 很多个体，累积开销大；相比固定 $\alpha=0.5$，额外计算量 manifold 增加。
  - 而性能是否提升**未知**（solution landscape 未知），开销/收益不划算。
- **For（支持）**：
  - 若算法性能对 $\alpha$ 敏感，则按 fitness 自适应 $\alpha$ 可能值得这点开销。
  - 每次 crossover 产生两个 offspring，补满 population 所需 crossover 次数较少。
  - 问题 landscape 未知 ⇒ 可能存在某些问题恰好从这种 adaptive 方案受益。

> ⭐ **考点**：开放论证题要**给出具体理由**，不能只说"no good"或"good"。老师反复强调："you must have somewhat of a view or explanations why."两条思路都成立，关键是 justification。

### 5. 本周考点速查表

| 考点 | 来源 | 要点 |
|---|---|---|
| **考试范围** | 老师口头 | **slide 60 及以后不考**；只考 Lecture 1 + Lecture 2 slide 1–58（五种 representation + 算子）+ Week 1 问题分类 |
| **fitness rescale** | 真题 Q1 | 原始值挤在窄区间时用 $F=1-|f-下界|/常数$ 拉开区分度 |
| **问题分类四例** | 真题 Q1B | 股价预测=modelling、装箱=optimization、政策=simulation、排班=optimization/simulation，**须给 explanation** |
| **N-Queens 通用 fitness** | 真题 Q3 | 最大冲突数 $=\binom{n}{2}=n(n-1)/2$ ⇒ $F=1-2C(Q)/(n(n-1))$ |
| **flexible $\alpha$** | 真题 Q4 | $\alpha=|f(A)-f(B)|/(f(A)+f(B))$ + whole arithmetic crossover；会算 + 会论证 for/against |
| **selection pressure 与 fitness 分布** | recap | fitness 越紧 → selection pressure 越失效（后期） → 需 rescaling/ranking（不考） |
| **permutation repair** | recap | 可用专用算子或"普通算子+repair"恢复 permutation 结构 |

### 6. 本周要点小结

- **本周性质**：复习周，无新内容；老师明确 **slide 60+ 不考**，考试范围 = Week 1 问题分类 + Week 2/3 五种 representation 及其算子 + 两个手算实例（eight-queens、SGA）。
- **进阶话题（不考）**：fitness rescaling、ranking selection、island/distributed population model——只需知道"fitness 越紧 selection 越失效"这层直觉。
- **历年真题风格**：题面故事长但求解直接；必含 (1) 一个建模/手算题、(2) 一个问题分类题、(3) 一个对算子的理解/计算题、(4) 一个开放论证题（for/against）。
- **N-Queens 推广**：分母从 28 推广到 $\binom{n}{2}=n(n-1)/2$，fitness $F=1-2C(Q)/(n(n-1))$。
- **flexible $\alpha$**：按 fitness 归一化差定 $\alpha$，会算 offspring + 会从计算开销与 landscape 未知两方面论证。
- **Quiz 1 已于本周（9/1）进行**，后续进入 ML 部分。

---

> **下一周预告**：Week 4 是 A/P LIM 部分的最后一周（Quiz 1 已结束）。Week 5 起课程**由另一位教授接手**，进入 **Machine Learning** 部分（CA Part 2，占 30%）。预计从 supervised learning 基础、classification/regression 等主题开始；具体内容以 Week 5 课件为准。LIM 部分的历年真题（EE6227 archive）仍是 Final Exam（60%，覆盖全课程）的复习材料。
