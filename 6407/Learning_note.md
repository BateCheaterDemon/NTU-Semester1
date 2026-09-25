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
  - **后半（Week 5–13，机器学习部分）**：**Mao Kezhi**（School of EEE，办公室 S2-B2c-84，ekzmao@ntu.edu.sg），主讲 Machine Learning（Week 5–13，共 9 周）。转写误拼为 "prop mole"/"Malco"。
- **教材**：课件标注一本参考书（老师因与作者为友可自由使用其材料）。复杂度理论部分引用经典书 **Garey & Johnson, *Computers and Intractability***。
- **参考论文**：`week1/IJCAT NQ.pdf` — Bah-Hwee Gwee & Meng-Hiot Lim, *An evolution search algorithm for solving N-queen problems*, IJCAT 2003。演示 N-queens 的 GA 求解（N-permutation 编码、适应度度量、可解到 2000 皇后），与课程 N-Queens 主题直接相关。

### 2. ⭐ 考核要求（重要）

| 成分 | 占比 | 说明 |
|---|---|---|
| **Continuous Assessment (CA)** | **40%** | 贯穿全学期；分为两段 |
| └ CA Part 1（Lim 的 4 周内） | **10%** | **仅一次 Quiz**，**无作业、无考勤考核** |
| └ CA Part 2（后半 ML 部分） | **30%** | Assignments 1&2 共 20%（Week 7/8 发布，Week 10 前提交）+ Quiz 2 共 10%（11 Nov 2026 周二 9:30–10:30，venue 待定） |
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

---

## Week 5 — Machine Learning 导论（Mao Kezhi 接手，Weeks 5–13）

> **教授**：本周起由 **Mao Kezhi** 教授接手（前半 LIM/EA/GA 部分 LIM 教授的 Quiz 1 已结束）。课程从 Genetic Algorithm / 进化计算转向 **Machine Learning**，共 9 周（Week 5–13）。
>
> **课件**：`week5/ML-Slides1.pdf`（52 页，标题 *EE6407 Genetic Algorithms and Machine Learning*）。本周为 ML 导论 + 考核说明 + AI/ML/NN/DL 关系 + ML 三步骤 + 三类 ML + tools/issues。

### 1. ⭐⭐ ML 部分考核安排（开课周必记）

| 项目 | 占比 | 细节 |
|---|---|---|
| **CA（Continual Assessment）总** | **40%** | 全课程；含前半 LIM/EA 的 Quiz 1 (10%) + ML 部分 CA (30%) |
| — Quiz 1（LIM/EA 部分） | 10% | 已于 Week 4 进行 |
| **ML 部分 CA** | **30%** | = 两个 Assignment (20%) + Quiz 2 (10%) |
| — Assignment ×2 | **20%** | 用同一数据训练**两个不同 classifier**，预测测试数据 class label 并比较性能；两份合并为单一 PDF 提交。**Week 7 & 8 release，Week 10 提交**（NTULearn portal 上传 PDF） |
| — **Quiz 2** | **10%** | **周二 11 月 10 日（Week 13，最后一周）9:30–10:30**（紧接课后，因 ~800 名学生需用大阶梯教室；否则改周六/晚上） |
| **Final Exam** | **60%** | 4 道题，其中约 **3 题来自 ML 部分**（覆盖后半）、1 题来自前半。**每年换题**——只刷往年题会挂，往年题仅作 format 参考 |

> ⚠️ **重要提醒**：
> - ML 部分在 CA 与 Final Exam 中都占大头（9 周 / 13 周 ≈ 69% 课时，Final 4 题中 3 题）。
> - Assignment 同一数据集、两个不同 classifier——考察对多种分类器的掌握与对比。
> - 老师强调题目**逐学期更换**，不要依赖刷题；理解原理与方法为主。

### 2. AI / ML / NN / DL 层级关系

四个术语各有 scope，须分清：

```
AI ⊃ Machine Learning ⊃ Neural Networks ⊃ Deep Learning
```

| 术语 | 定义 | 说明 |
|---|---|---|
| **AI（Artificial Intelligence）** | 模拟/模仿人类智能，最宽 | 含 computer vision、NLP、电子鼻（模拟嗅觉）等任何模仿人类行为/智能的技术 |
| **Machine Learning** | data-driven 方法，从数据学模型 | 区别于 rule-based expert system（1950s–80s 主流）；ML 不靠人工编码规则 |
| **Neural Networks** | ML 的子领域，用数据训练的神经网络 | 一种非线性模型；线性模型（linear model）也属 ML 但非 NN |
| **Deep Learning** | 多层 NN | NN 中层数多的一类 |

- 历史脉络：1950s–1980s 主导 **rule-based / expert system**（专家知识 → 编码成规则）；之后转向 **data-driven ML**。
- 实践中 rule-based 与 ML 常整合（hybrid）以提升 robustness、explainability；非二选一。
- ⭐ **本课范围**：只讲 Machine Learning，**不涵盖 Neural Networks / Deep Learning**（NN/DL 在另一门课 EE6207 / EE7207 讲）。

### 3. ⭐ Machine Learning 三步骤

ML 过程由三部分组成：

| 步骤 | 名称 | 含义 |
|---|---|---|
| 1 | **Data Input** | 输入训练数据（如带 label 的图像） |
| 2 | **Abstraction（抽象）** | 从输入数据学一个 **model**（模型可为规则、decision、数学方程，线性或非线性） |
| 3 | **Generalization（泛化）** | 将学得的 model 应用到**未来/新数据**做预测 |

- **Abstraction** = 训练阶段（fit a model from training samples）。
- **Generalization** = 推断阶段（apply trained model to future data）。
- ⭐ **Overfitting 的危害**：模型在训练范围内表现好，但**范围外泛化极差**——这正是要避免 overfitting 的原因。Generalization capability 是衡量模型质量的关键。
- 数据质量决定模型质量（garbage in, garbage out）：data → model → generalization capability，环环相扣。

### 4. ⭐ 三类 Machine Learning

| 类型 | 数据 | 任务 | 本课 |
|---|---|---|---|
| **Supervised Learning** | 有 label | **classification**（离散、有限类）+ **regression**（连续实值） | ✅ 讲 |
| **Unsupervised Learning** | 无 label | **clustering**（聚类）+ **association analysis**（关联分析） | ✅ 讲 clustering；association 仅提及 |
| **Reinforcement Learning** | reward/punishment 反馈 | agent 与 environment 交互、试错学策略 | ❌ 不讲（仅引入概念） |

**Supervised Learning 两大问题**：
- **Classification（分类）**：输出为**离散、有限的类别**。例：肿瘤恶性/良性、邮件 spam/non-spam、人脸识别（类别数可达成千上万，如 ImageNet 1000 类、人脸 ID 几千）。虽类别数可很大但**仍有限** → classification。
- **Regression（回归）**：输出为**连续实值、可能值无限**。例：房价预测、销量预测、温度预测。
- ⭐ 区分依据：**输出取值个数有限 → classification；连续无限 → regression**。Regression 多见于统计学，Classification 多见于 AI/ML。

**Unsupervised Learning**：
- 数据无 label，仍可从中学到结构。
- **Clustering（聚类）**：把相似样本聚成簇。
- **Association Analysis（关联分析）**：市场购物篮分析（market basket analysis）——发现物品间关联（频繁共现），minor topic，本课不深入。

**Reinforcement Learning（概念引入，不考）**：
- agent 在 environment 中行动，依 reward/punishment 反馈学最优策略；"从错误中学习"。
- 自主驾驶、ChatGPT 的 RLHF（人类反馈强化学习）等受此启发。

### 5. ML 相关类型与延伸概念

- **Transfer Learning（迁移学习）**：把一个 domain/task 的知识迁移到另一 task；若两 domain 完全无关则迁移无效，甚至**negative transfer**（负迁移）。
- **Human Learning 的类比**（老师提及）：memorization（记忆）、analogy（类比）、discovery/pattern recovery（模式发现）等不同学习类型，可作为评估 ML 的视角。

### 6. ⭐ 数据准备（Data Preparation）

数据是 ML 基础，质量决定上限。涉及：
- **Labeling（标注）**：supervised 需 label；标注昂贵、耗时，有时需专家知识；可用 consensus / majority voting 提高标注质量。
- **Data preprocessing**：处理 missing value、noisy data、outlier；清洗、归一化等。
- 老师强调模型性能**取决于数据质量**。

### 7. ⭐ Tools（实现工具）

| 工具 | 说明 |
|---|---|
| **Python** + **scikit-learn** | 当下最流行 ML 语言/库；assignment 首选 |
| **R** | 统计/商业领域常用高级语言 |
| **MATLAB** | 工程背景熟悉，有 ML toolbox；老师自 1989 年起用 |
| **C** | 底层实现，用于训练/部署大模型 |

- 实现路径：(1) 按公式手写程序实现 classifier（加深理解）；(2) 直接用 toolbox / 库函数。
- Assignment 可自写或用库；关键是理解原理。

### 8. ⭐ Issues（ML 应用注意事项）

| Issue | 要点 |
|---|---|
| **Privacy（隐私）** | 医疗等应用涉及个人数据；即使无隐私顾虑也不应把姓名等敏感属性作 feature |
| **Reliability（可靠性）** | 模型预测**未必可靠**——质量由数据决定，数据有 bias / 遗漏 → 不可信；需运用 human judgment 判断是否信任 |
| **Bias（偏差）** | 模型可对某些群体/观点有 bias（如大语言模型因训练数据偏西方而对"中国人吃什么"等给出偏向性答案） |
| **Ethical（伦理）** | bias、公平性等伦理问题 |
| **Legal（法律）** | regulation（法规）、privacy、mitigation of bias、transparency 等 |

- ⭐ 老师反复强调：模型预测不一定可信，**始终运用 human judgment**；并关注 ethical / legal / privacy 问题。

### 9. 本课 ML 部分主题路线（预告）

老师预告后续主题（按 ML-Slides1）：
- 先讲 **classifier 设计**：Linear Discriminant Analysis (LDA)、Support Vector Machine (SVM) 等——含公式、可手写实现。
- 再讲其他 supervised / unsupervised 方法。
- 具体 classifier 与顺序以每周课件为准。

### 10. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| **考核占比** | CA 40%（Quiz1 10% + ML CA 30%=Assignment 20%+Quiz2 10%），Final 60%（4 题中 3 题 ML） |
| **Quiz 2** | 10%，周二 11 月 10 日 9:30–10:30（Week 13） |
| **Assignment** | 20%，Week 7&8 release、Week 10 提交；同一数据两 classifier 对比 |
| **AI⊃ML⊃NN⊃DL** | 层级关系；本课只讲 ML，不含 NN/DL |
| **ML 三步骤** | Data Input → Abstraction（学 model）→ Generalization（应用到新数据） |
| **Generalization / Overfitting** | overfitting → 范围外泛化差；数据质量→模型质量→泛化能力 |
| **三类 ML** | supervised（有 label）、unsupervised（无 label）、reinforcement（reward） |
| **Classification vs Regression** | 输出有限离散→classification；连续实值→regression |
| **clustering / association** | unsupervised 两任务；association = market basket |
| **Tools** | Python+scikit-learn / R / MATLAB / C |
| **Issues** | privacy、reliability、bias、ethical、legal；需 human judgment |
| **换题** | Final 逐学期换题，刷往年题不够 |

### 11. 本周要点小结

- **课程切换**：Week 5 起 Mao Kezhi 接手，进入 ML（9 周，CA 与 Final 占大头）。
- **考核**：ML CA 30%（Assignment 20% Week 7&8 出/Week 10 交 + Quiz 2 10% 11/10）；Final 60%（4 题 3 题 ML，换题）。
- **AI/ML/NN/DL 层级**：AI ⊃ ML ⊃ NN ⊃ DL；本课仅 ML。
- **ML 三步骤**：Data Input → Abstraction（学 model）→ Generalization（用 model 预测新数据）；overfitting 损害泛化。
- **三类 ML**：supervised（classification + regression）、unsupervised（clustering + association）、reinforcement（本课不讲）。
- **Classification vs Regression**：输出有限离散 vs 连续实值。
- **Tools**：Python/scikit-learn、R、MATLAB、C。
- **Issues**：privacy、reliability（需 human judgment）、bias、ethical、legal。

---

> **下一周（Week 6）预告**：按 ML-Slides1 路线，下周起进入具体 **classifier 设计**——预计从 Linear Discriminant Analysis (LDA)、Support Vector Machine (SVM) 等监督分类器开始，含公式推导与实现。本周的 ML 三步骤、classification/regression 区分是直接前置。具体以 Week 6 课件为准。

---

## Week 6 — Machine Learning 数据准备（Data Preparation for ML）

> **教授**：Mao Kezhi（Week 5–13 ML 部分，第 2 周）。
>
> **课件**：`week6/ML-Slides2.pdf`（64 页，标题 *Lecturer Organization / School of EEE*，§2 Data Preparation for Machine Learning）。本周承接 Week 5 的 ML 三步骤（Data Input → Abstraction → Generalization），专门展开第一步 **Data Input** 的准备工作——数据是 ML 基础，"garbage in, garbage out"，数据质量直接决定模型质量与泛化能力。
>
> ⚠️ **本周实际主题为 Data Preparation（数据准备），不是 Week 5 预告中的 classifier design。** 转写末尾老师明确说 "next week we will just use this well prepared data to learn different types of models"，即 **Week 7 才进入 classifier design（分类器设计）**。
>
> 转写噪声修正（以 PDF 为准）：
> - "mache / machen / machina" → machine / machine learning
> - "abstion / exploation / espion / exploation" → exploration
> - "pession / pssion / prepsion / presion / purple session / perception" → preprocessing
> - "domint / domino / domnot / dominoy / dmin / minaltis" → dimensionality / dimension
> - "fatie / fathe / fisie / fishie / fisie striation / fish station / facial elation / fat elation" → feature extraction / feature selection
> - "subsclation / selation / subselation" → subset selection
> - "mission value / misson" → missing value；"autis / ats / ties / alias / at value" → outliers
> - "linu / linual / linear / lanu / lining" → learning（上下文中多指"训练"）
> - "CGP / C GPA / CGB / CDP" → CGPA；"snivion / sivan / sini / vision / suni vision" → standard deviation
> - "vars" → variance；"trial classified / atrial classified" → a typical classifier
> - "pan classification / p classified" → pattern classification / classifier
> - "ha unhealthy" → happy/unhappy；"barrel class" → basic class

### 1. 本周主线：数据准备为什么重要

ML 并非"拿到数据丢进 scikit-learn 就出模型"那么简单——数据收集后必须**仔细准备**才能喂给算法。老师反复强调：**数据质量直接决定模型质量，进而决定预测的可靠性**。

数据准备活动（PDF §2.1）：

1. **Understand the type of data**（理解数据类型）——不同模型对数据类型有假设（如要求 continuous 且服从 normal distribution），不满足则性能下降。
2. **Explore the nature and quality**（探索数据性质/质量）——噪声、spread、分布形态。
3. **Explore relationships amongst data elements**（探索变量间关系）——inter-feature relationship，发现 redundant/irrelevant features。
4. **Find potential issues**（发现潜在问题）——missing value、outliers。
5. **Do remediation**（补救/修复）——impute missing values、handle outliers。
6. **Apply preprocessing**（应用预处理）——scaling/normalization、dimensionality reduction。

数据准备好后，学习任务才开始（PDF §2.1 p3）：
- **Supervised learning**：把数据分成 **training data + test data**（有时加 validation data 用于确定 hyperparameter）。
- 考虑不同 model/learning algorithm，基于 training data 训练，再应用到 test data 评估性能。
- **Unsupervised learning**：无需 train/test 分割，直接对 input data 施加算法。

⭐ **Hyperparameter vs. Parameter**（本周关键区分）：
- **Parameter（参数）**：从 training data **估计**得到（如线性模型权重）。
- **Hyperparameter（超参数）**：训练前**手动设定**，不由数据估计（如 kNN 的 k、正则化系数 C）；用 **validation data** 选择合适取值。

### 2. ⭐ 数据类型（Types of Data）

数据集（data set）是相关记录的集合。约定：**一行 = 一个 sample（样本）**，**一列 = 一个 attribute/feature/variable（属性/特征/变量）**。术语在不同领域同义：
- Computer Science：**feature**
- Pattern recognition / classification：**feature** 或 **attribute**
- Statistics：**variable**

数据分为两大类，每类再分两子类（PDF §2.2）：

```
              Attributes
    /                     \
Qualitative/Categorical   Quantitative/Numeric
  /          \              /          \
Nominal    Ordinal      Interval     Ratio
```

| 大类 | 子类 | 特点 | 可执行运算 | 例子 |
|---|---|---|---|---|
| **Qualitative（定性）/ Categorical（类别）** | **Nominal（名义）** | 命名值，**无序**；可能值数有限 | 仅能判等（=≠）；**不能**加减乘除、不能算 mean/variance | 血型 A/B/O/AB、国籍、性别 |
| | **Ordinal（有序）** | 命名值，**可排序** | 可排大小、可算 **median**、quartile；**不能**加减乘除、**不能** mean | 成绩等级 A/B/C、满意度 happy/unhappy、金属硬度 |
| **Quantitative（定量）/ Numeric（数值）** | **Interval（区间）** | 有序且差值已知，**无绝对零** | 加减、mean、median、mode、standard deviation；**不能**乘除（ratio 无意义） | 摄氏温度、日期/时间 |
| | **Ratio（比率）** | 有序、差值已知、**有绝对零** | 加减乘除全部可；mean、median、mode、standard deviation 均可 | 长度、高度、重量、价格 |

⭐ **为什么要分清数据类型？** 因为 classifier design 中常需对数据做运算（mean、variance 等），nominal 数据上做加法无意义。理解数据类型才能选对模型、选对预处理方式。

按取值个数还可分：
- **Discrete（离散）**：有限或可数无穷（countably infinite）个可能值。Nominal/ordinal 属此类；某些 numeric（如 count）也属。**Binary attribute** 是 discrete 的特例（两个取值）。
- **Continuous（连续）**：可取任意实数值。Interval/ratio 属此类。

### 3. ⭐ 探索数据结构（Exploring Structure of Data）

#### 3.1 Data Dictionary（数据字典）

每个规范数据集应附 **data dictionary**（metadata repository）——记录每个 attribute 的描述、数据类型、是否有 missing value 等。如 Auto MPG 数据集字典会标明：
- 数据集特征（features 数、samples 数 398）、关联任务（regression）、各 attribute 类型（continuous/integer）。
- **Target variable（目标变量）**：要预测的变量（如 MPG），不是 feature。
  - target 为 **categorical → classification 问题**；target 为 **continuous → regression 问题**。

#### 3.2 探索数值数据（Exploring Numerical Data）

**Central Tendency（集中趋势）**：
- **Mean（均值）**：$$\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$$。**对 outlier 敏感**。
- **Median（中位数）**：排序后中间值。**对 outlier 鲁棒**（robust）。Mean 与 median 差异大 ⇒ 数据 **skewed（偏斜）**，需 drill down 找原因。
- **Mode（众数）**：出现最频繁的值。主要用于 **nominal data** 的 central tendency（ordinal 可用 median，更好）。

**Data Spread（数据分散度）**：
- **Variance（方差）**：$$\sigma^2=\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})^2$$
- **Standard Deviation（标准差）**：$$\sigma=\sqrt{\sigma^2}$$

⭐ 老师把 variance 引申到模型评估：同一算法不同 train/test 划分会得到不同性能，重复实验后报告 **mean ± standard deviation**——std 小 ⇒ 模型 **robust（鲁棒）**；std 大 ⇒ 不确定性高、不鲁棒。这是研究论文的标准做法。

**Data Value Position（位置度量）——Five-Number Summary（五数概括）**：
- 排序后将数据分为四等分，得 **minimum、Q1、Q2(median)、Q3、maximum**。
  - **Q1**：前半部分的中位数（25th percentile）
  - **Q2**：整体中位数（50th percentile）
  - **Q3**：后半部分的中位数（75th percentile）
- **IQR（Inter-Quartile Range，四分位距）** = Q3 − Q1。
- 五数之间间距不等可反映 **skewness**：如 Auto MPG 中 displacement 的 Q2 到 Q3 距离（113.5）远大于 Q1 到 Q2（44.3）⇒ 大值端更分散 ⇒ 右偏（right-skewed）。

#### 3.3 可视化（Visualization）

**Box Plot（箱线图，PDF §2.4.3.1）**：
- 箱体从 Q1 到 Q3，中间横线为 median。
- **Whisker（须）**：从 Q1 向下延伸至 `Q1 − 1.5×IQR` 内的最大数据点；从 Q3 向上延伸至 `Q3 + 1.5×IQR` 内的最小数据点。
- **超出 whisker 的点 = outliers**。
- 例：Q1=73, median=76, Q3=79, IQR=6 ⇒ 下界 64、上界 88。若数据中有 70、63、60，下须落在 70（最接近 64 且 ≥64 的点）。
- 箱体形状可揭示分布：median 居中且对称 ⇒ 近对称分布；Q1 与箱体距离不均 ⇒ skewed。

**Histogram（直方图，PDF §2.4.3.2）**：
- 将值域分为等宽 **bins**（默认 10），统计每个 bin 中数据点数（count）。
- 形态可揭示分布类型：
  - 各 bin count 相近 ⇒ **uniform distribution（均匀分布）**
  - 单峰对称 ⇒ **normal distribution（正态分布）**
  - 双峰 ⇒ **bimodal distribution（双峰分布）**——可能需用两个 Gaussian 函数建模
  - 长尾在右 ⇒ **right-skewed**；长尾在左 ⇒ **left-skewed**
- ⭐ 老师强调：下周学 classification 的基本 decision rule 时要**近似数据分布**（density function），需先通过 histogram 判断分布形态，不能盲目假设 normal。

#### 3.4 探索类别数据（Exploring Categorical Data）

类别数据可能值少，用**频数表**展示各取值的样本数（如 car.name 每种车各多少、cylinders 3/4/5/6/8 各多少辆）。

#### 3.5 探索变量间关系（Exploring Relationships）

| 方法 | 说明 |
|---|---|
| **Scatter Plot（散点图，§2.6.1）** | 两变量构成二维点，点的分布形态揭示相关性。若点呈趋势（非随机散布）⇒ 两变量相关。用于 feature↔target（判断 feature 是否有用）或 feature↔feature（发现 redundancy）。完全相同两 feature ⇒ 所有点落在 45° 直线上。 |
| **Two-way Cross-tabulation（交叉表 / Contingency Table，§2.6.2）** | 矩阵形式，展示两 categorical attribute 的联合频率。如各 origin 区域下不同 cylinder 数的车辆数。 |

⭐ Scatter plot 判断 feature 有无价值：feature 与 target 的散点若呈趋势 ⇒ 该 feature 与 target 相关、应纳入模型；若随机散布 ⇒ 该 feature 对预测无用、应排除。

### 4. ⭐ 数据质量与修复（Data Quality and Remediation）

两类常见问题（PDF §2.7）：

#### 4.1 Missing Value（缺失值）

成因：数据收集时信息不可得、录入遗漏。表现：表格中空缺或 `?`。

**处理策略**：
1. **Eliminate samples（删除样本）**：缺失样本占比小时可行（如 Auto MPG 398 中仅 6 个 horsepower 缺失 ⇒ 删除后剩 392，够用）。占比高时不可删（数据损失大）。
2. **Imputation（插补）**：
   - 用 **mean/median/mode** 替换：
     - Quantitative attribute ⇒ 用 mean 或 median（有 outlier 时用 median）
     - Qualitative attribute ⇒ 用 mode
     - **Supervised 问题中按 class 分别计算**：同类样本 feature 值相近，应从同类样本估统计量再填充。
   - **Similarity-based imputation（基于相似性的插补）**：在同类样本中找最相似的若干样本，用其 mean/median/mode 填充——比全类均值更精确。
   - **Estimate via feature relationship（利用特征关系估算）**：若 feature 间有相关，可建立回归关系 $x_1 \approx f(x_2,\dots)$，用其他 feature 预测缺失 feature 值。

#### 4.2 Outliers（异常值）

成因：记录错误（如身高记成 179 而非 1.79）、测量错误、或代表真实异常群体（如高血压患者）。

**识别**：box plot 中超出 whisker 的点；或距 mean 超过若干个 standard deviation。

**处理策略**：
1. **Remove outliers（移除）**：outlier 数量少（如 1–2%）且移除不影响建模结果时可行——最简单。
2. **Imputation（插补）**：用 mean/median/mode 替换（同 missing value 思路，按 class 分别估）。
3. **Capping（盖帽）**：超出 `Q1 − 1.5×IQR` 或 `Q3 + 1.5×IQR` 的值用 **5th percentile 或 95th percentile** 替换；或用 box plot 的 min/max 替换。
4. **Separate modeling（分离建模）**：outlier 数量显著时，可能代表新模式（如高血压人群），应把数据分成两部分分别建模——类似 bimodal 场景。
5. **Natural outliers 保留**：若 outlier 是真实有意义的（非错误），不应修改。

### 5. ⭐ 数据预处理（Data Pre-processing）

#### 5.1 Feature Scaling（特征缩放，PDF §2.8.1）

目的：把不同特征的取值转换到**相似尺度**，避免大数值 feature 主导模型。

**为何需要——两个理由**：

| 场景 | 理由 |
|---|---|
| **Distance-based algorithms（基于距离的算法）** | classifier 用 Euclidean distance 等度量样本相似度。若一 feature 取值范围远大于另一（如 CGPA 0–5 vs salary 60000–70000），大值 feature **dominate 距离计算**，小值 feature 被忽略。scaling 后各 feature 对距离贡献均衡。 |
| **Gradient descent-based algorithms（基于梯度下降的算法）** | 参数更新 $\theta_i \leftarrow \theta_i - \eta\frac{\partial L}{\partial\theta_i}$，更新幅度 $\propto x_i$。若 feature $x_i$ 数值大则更新大 ⇒ **训练不稳定、可能不收敛**。scaling 后更新幅度均衡，梯度下降更快收敛到 minima。 |

⭐ **Euclidean distance 公式**（老师口述）：
$$d(x,y)=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}$$
每个 feature 的差值平方求和再开方。feature 尺度差异会让大值 feature 主导此项。

⭐ **Gradient descent 参数更新**（老师口述，下周 classifier 会复用）：
$$\theta_i \leftarrow \theta_i - \eta\frac{\partial L}{\partial\theta_i}$$
其中 $\eta$ 为 learning rate，$L$ 为 loss function，$x_i$ 为第 $i$ 个 feature。$x_i$ 大 ⇒ 更新大 ⇒ 不稳定。

#### 5.2 ⭐ Normalization（归一化，Min-Max Scaling，§2.8.2）

把数据映射到 **[0,1]** 区间：

$$x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

- $x_{\min}$、$x_{\max}$ 为该 feature 的最小、最大值（outlier 与 missing value 已处理后再算）。
- $x = x_{\min} \Rightarrow x'=0$；$x = x_{\max} \Rightarrow x'=1$。
- **线性变换**，简单直观，范围固定。

#### 5.3 ⭐ Standardization（标准化，§2.8.3）

把数据中心化到 **mean=0、standard deviation=1**：

$$x' = \frac{x - \mu}{\sigma}$$

- $\mu$ 为 mean、$\sigma$ 为 standard deviation（处理完 outlier/missing 后计算）。
- 变换后 **mean=0, std=1**，但**取值无固定范围**（可能超出 [−1,1]）。
- 适合数据近似服从正态分布的场景。

⭐ **Normalization vs. Standardization 对比**：

| 特性 | Normalization（Min-Max） | Standardization（Z-score） |
|---|---|---|
| 范围 | 固定 [0,1] | 无固定范围 |
| 中心 | 最小值→0 | mean→0 |
| 尺度 | max−min | std=1 |
| 对 outlier | **敏感**（max/min 受 outlier 影响） | 相对鲁棒（mean/std 受影响但较小） |
| 适用 | feature 范围已知、需固定区间 | 数据近似正态、距离/梯度算法 |

> 老师指出：文献中两术语有时混用，关键理解变换效果——Min-Max 映射到 [0,1]，Z-score 映射到 mean=0/std=1。

#### 5.4 ⭐ Dimensionality Reduction（降维，§2.8.4）

高维数据计算开销大，且并非所有 feature 都有用。降维可减少复杂度、降低 overfitting 风险、提升泛化能力。

两类方法：

| 方法 | 说明 | 本课 |
|---|---|---|
| **Feature Extraction（特征提取）** | 创建新 feature（原 feature 的线性组合），如 **PCA（Principal Component Analysis）**、**SVD（Singular Value Decomposition）**。新 feature **不可解释**（如 0.5×CGPA+0.7×gender+0.6×weight，语义模糊） | ❌ 不讲（其他课程覆盖） |
| **Feature Subset Selection / Feature Selection（特征子集选择）** | 从原 feature 集中选最优子集，**不创建新 feature**，保留原 feature 语义 ⇒ 模型可解释 | ✅ 本课将讲（某周会介绍） |

⭐ 老师强调本课选讲 **feature selection** 而非 feature extraction，因为 feature selection **保留 feature 原始语义**，模型更可解释（interpretable）。

### 6. 数据准备完整流程汇总

```
收集数据
  → 探索数据类型（qualitative/quantitative, nominal/ordinal/interval/ratio）
  → 探索数据结构（data dictionary, central tendency, spread, box plot, histogram, scatter plot, cross-tab）
  → 发现问题：missing value, outliers
  → 修复：imputation / removal / capping（按 class 分别处理）
  → 预处理：feature scaling（normalization 或 standardization）
  → 降维：feature selection（本课）或 feature extraction（PCA/SVD，本课不讲）
  → 得到高质量数据集
  → 划分 train/validation/test
  → 进入模型学习（Week 7 起 classifier design）
```

### 7. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| **数据类型四级分类** | Qualitative（nominal/ordinal）vs Quantitative（interval/ratio）；各自可执行的运算 |
| **central tendency 选法** | nominal→mode, ordinal→median（或 mode）, interval/ratio→mean（outlier 时用 median） |
| **five-number summary** | min, Q1, Q2, Q3, max；IQR=Q3−Q1 |
| **box plot whisker** | Q1−1.5×IQR / Q3+1.5×IQR；超界点=outlier |
| **histogram 判分布** | 单峰/双峰/均匀/左偏/右偏；为下周 decision rule 选 density function 做准备 |
| **outlier 处理** | remove / impute / cap(5th/95th percentile) / 分离建模 / 自然则保留 |
| **missing value 处理** | eliminate（占比小）/ impute（mean/median/mode，按 class 分别；或 similarity-based）/ estimate via feature relationship |
| **feature scaling 必要性** | distance-based（避免大值 dominate）+ gradient descent（更新均衡稳定） |
| **Normalization 公式** | $x'=(x-x_{\min})/(x_{\max}-x_{\min})$，映射到 [0,1] |
| **Standardization 公式** | $x'=(x-\mu)/\sigma$，mean=0, std=1, 无固定范围 |
| **降维两路线** | feature extraction（PCA/SVD，新 feature 不可解释，本课不讲）vs feature selection（子集，保留语义，本课讲） |
| **hyperparameter vs parameter** | hyperparameter 训练前设定（validation data 选）；parameter 从 train data 估计 |
| **classification vs regression** | target 离散→classification；target 连续→regression |
| **variance 用于模型评估** | 重复实验报告 mean±std；std 小=robust |

### 8. 本周要点小结

- **本周主题**：Data Preparation（数据准备），不是 classifier design。承接 Week 5 的 ML 三步骤，展开第一步 Data Input 的完整流程。
- **数据类型**：Qualitative（nominal/ordinal）与 Quantitative（interval/ratio）四级分类；不同类型可执行的运算不同，决定可用模型与预处理方式。
- **探索工具**：central tendency（mean/median/mode）、data spread（variance/std）、five-number summary、box plot（whisker=1.5×IQR 判 outlier）、histogram（判分布形态）、scatter plot（判 feature↔target/feature↔feature 关系）、cross-tab（两 categorical 变量）。
- **数据质量**：missing value（eliminate/impute/similarity-based/feature-relationship）与 outliers（remove/impute/cap/分离建模/自然保留）。
- **预处理**：feature scaling 分 normalization（Min-Max→[0,1]）与 standardization（Z-score→mean=0,std=1）；动机=distance-based 算法避免大值 dominate + gradient descent 更新均衡稳定。
- **降维**：feature extraction（PCA/SVD，新 feature 不可解释，本课不讲）vs feature selection（子集，保留语义，本课讲）。
- **模型评估**：重复实验报告 mean±std，std 衡量 robustness。

---

> **下一周（Week 7）预告**：本周结束老师明确说 "next week we will just use this well prepared data to learn different types of models"，即 Week 7 正式进入 **classifier design（分类器设计）**——预计从 Linear Discriminant Analysis (LDA)、Support Vector Machine (SVM) 等 supervised classifier 开始，含公式推导与实现。本周的数据类型、feature scaling、hyperparameter 等概念是直接前置。具体以 Week 7 课件为准。

---

## Week 7 — Classifier Design：Bayesian Decision Theory、GMM/EM 与 Naïve Bayes

> **权威来源说明**：本周转写 `week7/week7.txt` 噪声极多（整段无标点），以下内容以官方课件 `week7/ML-Slides3.pdf`（52 页）与 `week7/Python_Implementation.pdf`（8 页代码示例）为权威来源修正。转写中 "pyro"/"p probability"→prior、"livelihood"→likelihood、"po zero/pus probability"→posterior probability、"dismal/desimal/dial function"→discriminant function、"gau mist/gauche/gai mission"→Gaussian mixture、"question Mr"→Gaussian mixture model、"chronometris/cron matrix/cent matrix"→covariance matrix、"Bani/bul/binno/nu base"→Naïve Bayes 等，均按 PDF 修正。
>
> **本周主题**：正式进入 classifier design（分类器设计）。本周从 **Bayesian Decision Theory（贝叶斯决策理论）** 入手，建立 probability-based classifier 的完整框架：prior、class-conditional density、posterior、discriminant function → Gaussian 假设下的 parameter estimation（maximum-likelihood）→ 多模态数据用 **GMM + EM algorithm** → 简化假设下的 **Naïve Bayes**（Gaussian/Bernoulli/Multinomial 三型）。课件 `ML-Slides3.pdf` 共 52 页覆盖以上内容；`Python_Implementation.pdf` 给出 SVM、LDA、GaussianNB、DecisionTree 的 sklearn 实现代码。

### 1. ⭐ Bayesian Decision Theory——概率框架下的分类

#### 1.1 鱼分类问题引入（PDF p.1）

课件以经典 fish classification（鱼分类）为例：sea bass（鲈鱼）vs salmon（鲑鱼），需开发 ML classifier 自动分类。人眼可凭 length、lightness（颜色深浅）、width 等特征区分，但机器需通过 probability-based decision rule 实现。

#### 1.2 四个核心概率概念

⭐ 本周最重要的一组概念——**四个概率**，必须能区分：

| 概念 | 符号 | 含义 | 如何获得 |
|---|---|---|---|
| **prior probability（先验概率）** | $P(\omega_j)$ | 在看到任何证据前，样本属于类 $\omega_j$ 的初始概率 | 从训练数据中各类样本占比直接估计 |
| **class-conditional probability density function（类条件概率密度函数）** | $p(\boldsymbol{x}\mid\omega_j)$ | 已知类别 $\omega_j$ 时，特征 $\boldsymbol{x}$ 的分布 | 从训练数据估计（假设分布族后用 MLE） |
| **posterior probability（后验概率）** | $P(\omega_j\mid\boldsymbol{x})$ | 看到特征 $\boldsymbol{x}$ 后，样本属于 $\omega_j$ 的概率 | 由 Bayes theorem 计算 |
| **joint probability（联合概率）** | $p(\boldsymbol{x},\omega_j)=p(\boldsymbol{x}\mid\omega_j)\,P(\omega_j)$ | $\boldsymbol{x}$ 与 $\omega_j$ 同时发生的概率 | Bayes theorem 的分子（忽略分母 $p(\boldsymbol{x})$） |

**prior probability 的意义**（PDF p.2）：在考虑新证据前，基于已有知识（如训练数据中各类比例）对事件概率的初始信念。

例：EE6407 课堂 60% 男生、40% 女生 ⇒ $P(\text{male})=0.6,\;P(\text{female})=0.4$。若不看任何特征仅凭 prior 决策，则所有样本都判为 male（prior 大的类），40% 女生被错分——说明**仅靠 prior 不足**，需引入 class-conditional density。

#### 1.3 ⭐ Bayes Theorem 与决策规则（PDF p.5-6）

$$P(\omega_j\mid\boldsymbol{x})=\frac{p(\boldsymbol{x}\mid\omega_j)\,P(\omega_j)}{p(\boldsymbol{x})}$$

其中分母 $p(\boldsymbol{x})=\sum_{k}p(\boldsymbol{x}\mid\omega_k)\,P(\omega_k)$ 为 **evidence**（scale factor），对所有类别相同，决策时可忽略。

**Bayes decision rule（贝叶斯决策规则）**：

$$\text{Decide }\omega_1\text{ if }P(\omega_1\mid\boldsymbol{x})>P(\omega_2\mid\boldsymbol{x});\quad\text{Decide }\omega_2\text{ otherwise.}$$

⭐ **关键理解**：决策应基于 **posterior probability**（融合了 prior + 新证据 $\boldsymbol{x}$），而非仅靠 prior。忽略 $p(\boldsymbol{x})$ 后，等价于用 **joint probability** $p(\boldsymbol{x},\omega_j)=p(\boldsymbol{x}\mid\omega_j)\,P(\omega_j)$ 做 decision。

#### 1.4 推广：多特征 + 多类（PDF p.8-10）

- **多特征**：$\boldsymbol{x}=(x_1,x_2,\dots,x_d)^T$ 为 $d$ 维 feature vector。
- **多类**：$\omega_1,\omega_2,\dots,\omega_C$ 共 $C$ 个类。
- posterior 推广为：
$$P(\omega_j\mid\boldsymbol{x})=\frac{p(\boldsymbol{x}\mid\omega_j)\,P(\omega_j)}{\sum_{k=1}^{C}p(\boldsymbol{x}\mid\omega_k)\,P(\omega_k)}$$

#### 1.5 ⭐ Discriminant Function（判别函数，PDF p.9-10）

**一般化分类架构**：对每个类 $\omega_j$ 定义 discriminant function $g_j(\boldsymbol{x})$，classifier 将 $\boldsymbol{x}$ 分入 $g_j(\boldsymbol{x})$ 最大的类：

$$\text{Assign }\boldsymbol{x}\text{ to }\omega_j\text{ if }g_j(\boldsymbol{x})=\max_{k}g_k(\boldsymbol{x})$$

在 Bayes classifier 中，discriminant function 可取以下**三种等价形式**：

| 形式 | $g_j(\boldsymbol{x})=$ | 说明 |
|---|---|---|
| posterior probability | $P(\omega_j\mid\boldsymbol{x})$ | 最直接，但需算 $p(\boldsymbol{x})$ |
| joint probability | $p(\boldsymbol{x}\mid\omega_j)\,P(\omega_j)$ | 省略 $p(\boldsymbol{x})$，最常用 |
| log-joint probability | $\ln p(\boldsymbol{x}\mid\omega_j)+\ln P(\omega_j)$ | 乘法→加法，数值更稳定，避免下溢 |

⭐ discriminant function 是**通用概念**——不同 classifier 有不同 $g_j$，Bayes classifier 只是一种（用 posterior/joint）。后续其他 classifier（LDA、SVM）有各自的 discriminant function 形式。

### 2. Gaussian 假设下的 Parameter Estimation

#### 2.1 Univariate Normal Density（PDF p.11-12）

$$p(x\mid\omega_j)=\frac{1}{\sqrt{2\pi}\,\sigma_j}\exp\!\left(-\frac{(x-\mu_j)^2}{2\sigma_j^2}\right)$$

参数：$\mu_j$（mean）、$\sigma_j^2$（variance），完全由这两个参数确定。

#### 2.2 ⭐ Multivariate Normal Density（PDF p.13-14）

$$p(\boldsymbol{x}\mid\omega_j)=\frac{1}{(2\pi)^{d/2}\lvert\boldsymbol{\Sigma}_j\rvert^{1/2}}\exp\!\left[-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu}_j)^T\boldsymbol{\Sigma}_j^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_j)\right]$$

参数：
- $\boldsymbol{\mu}_j$：$d$ 维 mean vector
- $\boldsymbol{\Sigma}_j$：$d\times d$ covariance matrix（对称正定）
- $\lvert\boldsymbol{\Sigma}_j\rvert$ 为 determinant，$\boldsymbol{\Sigma}_j^{-1}$ 为 inverse

⭐ 两个参数确定后，density function 完全确定。

#### 2.3 ⭐ Maximum-Likelihood Parameter Estimation（PDF p.15-21）

实际中 prior 和 class-conditional density 均未知，需从 training samples 估计。

**思路**：假设各类样本独立同分布（IID），参数 $\boldsymbol{\theta}=(\boldsymbol{\mu},\boldsymbol{\Sigma})$ 的 likelihood 为：

$$p(\mathcal{D}\mid\boldsymbol{\theta})=\prod_{k=1}^{n}p(\boldsymbol{x}_k\mid\boldsymbol{\theta})$$

**log-likelihood**：

$$\ell(\boldsymbol{\theta})=\ln p(\mathcal{D}\mid\boldsymbol{\theta})=\sum_{k=1}^{n}\ln p(\boldsymbol{x}_k\mid\boldsymbol{\theta})$$

⭐ 因 logarithm 单调递增，最大化 $\ell(\boldsymbol{\theta})$ 等价于最大化 likelihood。取 log 后指数变加法，计算更简便。

**必要条件**：$\frac{\partial \ell}{\partial \boldsymbol{\theta}}=0$

**Case 1: 仅 $\boldsymbol{\mu}$ 未知（$\boldsymbol{\Sigma}$ 已知）**（PDF p.19-20）

对 log-likelihood 求 $\boldsymbol{\mu}$ 的偏导并令其为零，得：

$$\hat{\boldsymbol{\mu}}=\frac{1}{n}\sum_{k=1}^{n}\boldsymbol{x}_k$$

即样本均值——MLE 估计与直觉公式一致。

**Case 2: $\boldsymbol{\mu}$ 和 $\boldsymbol{\Sigma}$ 均未知**（PDF p.21）

$$\hat{\boldsymbol{\mu}}=\frac{1}{n}\sum_{k=1}^{n}\boldsymbol{x}_k,\qquad \hat{\boldsymbol{\Sigma}}=\frac{1}{n}\sum_{k=1}^{n}(\boldsymbol{x}_k-\hat{\boldsymbol{\mu}})(\boldsymbol{x}_k-\hat{\boldsymbol{\mu}})^T$$

⭐ 对每个类 $\omega_j$，用该类的样本单独估 $\hat{\boldsymbol{\mu}}_j$ 和 $\hat{\boldsymbol{\Sigma}}_j$（各类独立处理）。

#### 2.4 ⭐ 完整 Bayes Classifier 设计流程（PDF p.22-26，Example 1）

200 个训练样本（class 1、class 2 各 100），步骤：

1. 估 prior：$P(\omega_1)=n_1/N=100/200=0.5$，$P(\omega_2)=0.5$
2. 估 class 1 参数：$\hat{\boldsymbol{\mu}}_1=\frac{1}{n_1}\sum_{\boldsymbol{x}\in\omega_1}\boldsymbol{x}$，$\hat{\boldsymbol{\Sigma}}_1=\frac{1}{n_1}\sum(\boldsymbol{x}-\hat{\boldsymbol{\mu}}_1)(\boldsymbol{x}-\hat{\boldsymbol{\mu}}_1)^T$
3. 同理估 class 2 的 $\hat{\boldsymbol{\mu}}_2$、$\hat{\boldsymbol{\Sigma}}_2$
4. 构造 class-conditional density $p(\boldsymbol{x}\mid\omega_j)$（代入 multivariate normal 公式）
5. 构造 discriminant function $g_j(\boldsymbol{x})=p(\boldsymbol{x}\mid\omega_j)\,P(\omega_j)$
6. 对 test sample $\boldsymbol{x}$：若 $g_1(\boldsymbol{x})>g_2(\boldsymbol{x})$ → class 1；$g_1<g_2$ → class 2；$g_1=g_2$ → decision boundary（无法判定）

⭐ **decision boundary**：$g_1(\boldsymbol{x})=g_2(\boldsymbol{x})$ 的点的集合。此例中 boundary 为**曲线（non-linear）**——因 density function 含指数项，故 Bayes classifier 本质是 non-linear classifier。

### 3. ⭐ Gaussian Mixture Model 与 EM Algorithm（PDF p.27-51）

#### 3.1 动机：多模态数据（PDF p.27-28）

若某类（如 class 2）的数据分布为**多模态（multimodal）**——由多个 Gaussian 分布叠加而成——则单个 Gaussian 无法拟合，需用 **GMM**。

#### 3.2 GMM 定义（PDF p.29）

$$p(\boldsymbol{x}\mid\omega_j)=\sum_{i=1}^{M}\alpha_i\,\mathcal{N}(\boldsymbol{x}\mid\boldsymbol{\mu}_i,\boldsymbol{\Sigma}_i)$$

- $M$：Gaussian components 数量
- $\alpha_i$：第 $i$ 个 component 的 weight，$\sum_{i=1}^{M}\alpha_i=1$
- $\boldsymbol{\mu}_i,\boldsymbol{\Sigma}_i$：第 $i$ 个 component 的参数

⭐ GMM 可逼近任意密度函数（universal approximator），但 $M$ 是 **hyperparameter**——需 trial and error 确定。

#### 3.3 Parameter Estimation 与 EM Algorithm（PDF p.30-35）

对 GMM，MLE 无 closed-form 解——因参数互相依赖（chicken-egg problem）。引入 **EM algorithm（Expectation-Maximization）**。

**隐变量**：$\gamma_{ik}=P(\omega_i\mid\boldsymbol{x}_k)$ 表示样本 $\boldsymbol{x}_k$ 属于第 $i$ 个 Gaussian component 的概率（responsibility）。

$$\gamma_{ik}=\frac{\alpha_i\,\mathcal{N}(\boldsymbol{x}_k\mid\boldsymbol{\mu}_i,\boldsymbol{\Sigma}_i)}{\sum_{m=1}^{M}\alpha_m\,\mathcal{N}(\boldsymbol{x}_k\mid\boldsymbol{\mu}_m,\boldsymbol{\Sigma}_m)}$$

⭐ **EM 迭代两步**：

| 步骤 | 内容 |
|---|---|
| **E-Step（Estimation Step）** | 给定当前 $\alpha_i^{(j-1)},\boldsymbol{\mu}_i^{(j-1)},\boldsymbol{\Sigma}_i^{(j-1)}$，计算所有 $\gamma_{ik}$ |
| **M-Step（Maximization Step）** | 用 $\gamma_{ik}$ 更新参数：$\boldsymbol{\mu}_i=\frac{\sum_k\gamma_{ik}\boldsymbol{x}_k}{\sum_k\gamma_{ik}}$，$\boldsymbol{\Sigma}_i=\frac{\sum_k\gamma_{ik}(\boldsymbol{x}_k-\boldsymbol{\mu}_i)(\boldsymbol{x}_k-\boldsymbol{\mu}_i)^T}{\sum_k\gamma_{ik}}$，$\alpha_i=\frac{1}{n}\sum_k\gamma_{ik}$ |

⭐ 与单 Gaussian MLE 的区别：每个样本对 $\boldsymbol{\mu}_i$ 的贡献不再是等权重（1），而是按 $\gamma_{ik}$ 加权——样本属于该 component 的概率越大，贡献越大。

**EM Algorithm 流程**（PDF p.34-35）：
1. **Initialization**（$j=0$）：随机初始化 $\alpha_i^{(0)},\boldsymbol{\mu}_i^{(0)},\boldsymbol{\Sigma}_i^{(0)}$
2. **E-Step**（$j\geq 1$）：算 $\gamma_{ik}$
3. **M-Step**：更新 $\alpha_i,\boldsymbol{\mu}_i,\boldsymbol{\Sigma}_i$
4. 重复 2-3 直到收敛（参数稳定或达最大迭代次数，如 1000 次）

#### 3.4 GMM Example（PDF p.36-51，Example 2）

class 2 由 2 个 Gaussian component 生成，用 EM 估计参数后：
- GMM（2 components for class 2 + 1 for class 1）→ **14 misclassifications**
- 单 Gaussian for class 2 → **15 misclassifications**（欠拟合）

⭐ **确定 $M$ 的方法——分析 $\alpha_i$**：
- $M=3$（多猜 1 个）：$\alpha=[0.05,0.05,0.5,0.44]$ → 一个 component 的 $\alpha$ 很小 → 该 component 不重要，可删
- $M=5$（多猜 3 个）：$\alpha=[0.46,0.42,0.03,0.05,0.02]$ → 3 个小 $\alpha$ → 这些 component 不重要

⭐ **Overfitting 问题**（PDF p.51）：
- $M$ 过多 → decision boundary 过于复杂 → 训练集表现好但测试集差（**overfitting**）
- 小 $\alpha$ 值可指示冗余 component → 删去后重新估计参数以缓解 overfitting

### 4. ⭐ Naïve Bayes Classifier（PDF p.52-71）

#### 4.1 核心假设——Feature Independence（PDF p.53-54）

对 $d$ 维 feature vector $\boldsymbol{x}=(x_1,\dots,x_d)$，Bayes theorem 给出：

$$P(\omega_j\mid\boldsymbol{x})=\frac{p(\boldsymbol{x}\mid\omega_j)\,P(\omega_j)}{p(\boldsymbol{x})}$$

**Naïve 假设**：各 feature 相互独立（conditionally independent given class）：

$$p(\boldsymbol{x}\mid\omega_j)=\prod_{i=1}^{d}p(x_i\mid\omega_j)$$

⭐ 因此 posterior 简化为：

$$P(\omega_j\mid\boldsymbol{x})\propto P(\omega_j)\prod_{i=1}^{d}p(x_i\mid\omega_j)$$

**为何"Naïve"**：假设 feature 间独立在实际中很少成立，但即便如此 Naïve Bayes 在实际中表现良好（尤其 text classification、spam filtering）。

**优势**：
- 只需估计各 feature 的 1D 分布（无需估 $d\times d$ covariance matrix）→ 大幅简化、缓解 curse of dimensionality
- 训练数据需求少、计算极快

#### 4.2 ⭐ 三种 Naïve Bayes（PDF p.55）

| 类型 | 适用数据 | 特征分布 |
|---|---|---|
| **Gaussian Naïve Bayes** | continuous data | 每个特征假设服从 normal distribution，估 $\mu_{ij},\sigma_{ij}$ |
| **Bernoulli Naïve Bayes** | discrete/binary data | Bernoulli distribution（0/1，yes/no） |
| **Multinomial Naïve Bayes** | text classification | 用 word count 表示文本，估各词频率 |

#### 4.3 Gaussian Naïve Bayes（PDF p.56）

每个 continuous feature $x_i$ 在类 $\omega_j$ 下假设服从 normal distribution：

$$p(x_i\mid\omega_j)=\frac{1}{\sqrt{2\pi}\,\sigma_{ij}}\exp\!\left(-\frac{(x_i-\mu_{ij})^2}{2\sigma_{ij}^2}\right)$$

其中 $\mu_{ij}$、$\sigma_{ij}$ 为 feature $i$ 在类 $\omega_j$ 下的 mean 和 standard deviation，用 MLE 从类 $\omega_j$ 的样本中估计。

⭐ 与完整 Bayes classifier 的区别：Gaussian Naïve Bayes 假设各 feature 独立 → covariance matrix 变为对角阵 → 只需估各 feature 的 1D 参数，不估 off-diagonal 元素。

#### 4.4 Bernoulli Naïve Bayes（PDF p.57-63）

**Bernoulli distribution**：$P(x_i=1)=p$，$P(x_i=0)=1-p$。

⭐ **考试例题（PDF p.58-63）**：5 个训练样本，3 个 feature（Confident, Studied, Sick，均 Yes/No），label 为 Pass/Fail。分类新样本 Confident=Yes, Studied=Yes, Sick=No。

**步骤**：
1. 估 prior：$P(\text{Pass})=3/5=0.6$，$P(\text{Fail})=2/5=0.4$
2. 估各 feature 的 class-conditional probability（从训练样本中数频次）：
   - $P(\text{Confident=Yes}\mid\text{Pass})=2/3$（3 个 Pass 中 2 个 Confident=Yes）
   - $P(\text{Studied=Yes}\mid\text{Pass})=2/3$
   - $P(\text{Sick=No}\mid\text{Pass})=1/3$
   - 同理算 $P(\cdot\mid\text{Fail})$
3. 算 joint probability（discriminant function）：
   - $g_{\text{Pass}}=P(\text{Pass})\times P(\text{Conf=Yes}\mid\text{Pass})\times P(\text{Stud=Yes}\mid\text{Pass})\times P(\text{Sick=No}\mid\text{Pass})$
   - $g_{\text{Fail}}=P(\text{Fail})\times\cdots$
4. 比较 $g_{\text{Pass}}$ vs $g_{\text{Fail}}$，取大者 → 分类为 **Pass**

⭐ $p(\boldsymbol{x})$ 是公共分母，可忽略——直接比较分子（joint probability）即可。

#### 4.5 ⭐ Multinomial Naïve Bayes 与 Laplace Smoothing（PDF p.64-70）

用于 **text classification**：将文本表示为 word count vector。

**例题（PDF p.64-70）**：5 个训练样本（Sports / Not sports），分类 "A very close game"。

**class-conditional probability 估计**：

$$p(x_i\mid\omega_j)=\frac{N_{x_i,\omega_j}}{N_{\omega_j}}$$

其中 $N_{x_i,\omega_j}$ 为词 $x_i$ 在类 $\omega_j$ 的所有文本中出现的次数，$N_{\omega_j}$ 为类 $\omega_j$ 的文本总词数。

⭐ **零概率问题**：若词 $x_i$ 在训练数据中未出现于类 $\omega_j$，则 $p(x_i\mid\omega_j)=0$ → 整个乘积为零 → 后验为零。

**Laplace smoothing（Add-1 smoothing）**：

$$p(x_i\mid\omega_j)=\frac{N_{x_i,\omega_j}+1}{N_{\omega_j}+V}$$

- $V$：所有训练数据中 **unique words（唯一词）** 的总数
- 分子加 1 确保不为零；分母加 $V$ 保证概率和为 1

例（PDF p.68-70）：词 "close" 在 Sports 类出现 0 次 → 无 smoothing 为 $0/11=0$；Laplace smoothing 后为 $1/(11+14)=1/25$。最终 "A very close game" 分为 Sports（joint probability > Not sports 的 joint probability）。

#### 4.6 Naïve Bayes 要点（PDF p.71）

1. 尽管 independence 假设过于简化，Naïve Bayes 在 document classification、spam filtering 等实际任务中效果很好，且只需少量训练数据。
2. 计算极快：各 feature 的 class-conditional distribution 可独立估计为 1D distribution，缓解 curse of dimensionality。

### 5. ⭐ 各分类器对比总结

| 分类器 | 核心原理 | 假设 | 参数 | 优势 | 劣势 |
|---|---|---|---|---|---|
| **Bayes classifier（单 Gaussian）** | posterior → discriminant function | 数据服从 single multivariate Gaussian | $\boldsymbol{\mu}_j,\boldsymbol{\Sigma}_j$ per class | 理论最优（若假设成立） | 多模态数据不适用 |
| **Bayes classifier + GMM** | GMM 拟合多模态 density | 数据为多个 Gaussian 的混合 | $\alpha_i,\boldsymbol{\mu}_i,\boldsymbol{\Sigma}_i$ per component | 可逼近任意分布 | $M$ 需 trial and error；易 overfit |
| **Gaussian Naïve Bayes** | feature 独立 → 1D 估计 | feature 间独立 + 各 feature Gaussian | $\mu_{ij},\sigma_{ij}$ per feature per class | 快、简单、少数据 | 独立假设常不成立 |
| **Bernoulli Naïve Bayes** | binary feature 独立 | binary feature + 独立 | $p_{ij}$ per feature per class | 适合 0/1 特征 | 仅适用 binary feature |
| **Multinomial Naïve Bayes** | word count 独立 | 词频独立 + Laplace smoothing | 词频 $p(x_i\mid\omega_j)$ | text classification 首选 | 不适合 continuous |

⭐ **assignment 信息**（转写末尾，老师口述）：
- **Assignment 1** 已在 NTULearn 发布——feature 均为 continuous，用 normal function 建 class-conditional density
- **Assignment 2** 将在 **Week 8（recess 后）** 发布
- 两次 assignment 合并为**一份 PDF**提交（不含代码，只写 class label 值和预测结果）
- **截止日期：10 月 19 日**（约 3 周时间）
- 两次 assignment 合计占 **20%**（CA Part 2 的 30% 中的一部分）

### 6. Python 实现要点（Python_Implementation.pdf）

`Python_Implementation.pdf` 给出 5 个分类器的 sklearn 实现示例，数据均为 `np.random.normal` 生成的两类 2D 数据（各 100 样本）。

**通用数据生成模式**：
```python
np.random.seed(2)
x1 = np.random.normal(50, 10, 100); y1 = np.random.normal(50, 7, 100)   # Class 1
x2 = np.random.normal(60, 12, 100); y2 = np.random.normal(10, 10, 100)  # Class 2
X = np.vstack((np.column_stack((x1, y1)), np.column_stack((x2, y2))))
y = np.array([0]*100 + [1]*100)
```

⭐ **五个分类器 API 对比**：

| 分类器 | sklearn API | 关键参数 | 代码要点 |
|---|---|---|---|
| **SVM** | `svm.SVC(kernel="linear")` | `kernel`（linear/rbf/poly） | `clf.coef_[0]` 得 $w$，`clf.intercept_[0]` 得 $b$，决策线 $w_0 x+w_1 y+b=0$ → $y=-(w_0 x+b)/w_1$ |
| **LDA** | `LinearDiscriminantAnalysis()` | — | `lda.fit(X, y)` → `lda.predict(new_points)` |
| **Gaussian Naïve Bayes** | `GaussianNB()` | — | `gnb.fit(X, y)` → `gnb.predict(new_points)` |
| **Decision Tree** | `DecisionTreeClassifier(max_depth=3)` | `max_depth`（控制树深度防 overfitting） | `tree.fit(X, y)` → `tree.predict(new_points)` |

**数据可视化三种图**（复习 Week 6）：
- **Box plot**：`plt.boxplot([data1, data2], labels=[...], patch_artist=True)`，展示 Q1/median/Q3/IQR/outlier
- **Histogram**：`plt.hist(data, alpha=0.5, label=...)`，展示分布形态
- **Scatter plot**：`plt.scatter(x, y, c='blue', marker='x', label=...)`，展示 feature↔feature 关系

⭐ SVM 决策线绘制（常考）：
```python
w = clf.coef_[0]       # (w1, w2)
b = clf.intercept_[0]  # bias
xx = np.linspace(x_min, x_max, 200)
yy = -(w[0] * xx + b) / w[1]   # 从 w1*x + w2*y + b = 0 解出 y
```

### 7. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| **四个概率概念区分** | prior $P(\omega_j)$ / class-conditional $p(\boldsymbol{x}\mid\omega_j)$ / posterior $P(\omega_j\mid\boldsymbol{x})$ / joint $p(\boldsymbol{x},\omega_j)$ |
| **Bayes decision rule** | 选 posterior 最大的类；$p(\boldsymbol{x})$ 是公共 scale factor 可忽略 |
| **discriminant function** | $g_j(\boldsymbol{x})$ 三种形式：posterior / joint / log-joint；取最大值对应的类 |
| **MLE 估计 $\boldsymbol{\mu},\boldsymbol{\Sigma}$** | $\hat{\mu}=\frac{1}{n}\sum x_k$；$\hat{\Sigma}=\frac{1}{n}\sum(x_k-\hat{\mu})(x_k-\hat{\mu})^T$；对数似然求偏导令为零 |
| **Bayes classifier 设计流程** | 估 prior → 估 class-conditional density → 构造 $g_j$ → 比较 $g_1$ vs $g_2$ → 分到大者 |
| **GMM 定义** | $p(\boldsymbol{x}\mid\omega_j)=\sum_{i=1}^M\alpha_i\mathcal{N}(\boldsymbol{x}\mid\boldsymbol{\mu}_i,\boldsymbol{\Sigma}_i)$，$\sum\alpha_i=1$ |
| **EM 两步** | E-Step 算 $\gamma_{ik}$（responsibility）；M-Step 用 $\gamma_{ik}$ 加权更新 $\alpha_i,\boldsymbol{\mu}_i,\boldsymbol{\Sigma}_i$ |
| **GMM 过拟合** | $M$ 过大 → decision boundary 复杂 → overfitting；用小 $\alpha_i$ 判定冗余 component |
| **Naïve Bayes 独立假设** | $p(\boldsymbol{x}\mid\omega_j)=\prod_i p(x_i\mid\omega_j)$，无需估 covariance |
| **三种 Naïve Bayes** | Gaussian（continuous）/ Bernoulli（binary）/ Multinomial（text） |
| **Laplace smoothing** | $p(x_i\mid\omega_j)=\frac{N+1}{N_{\omega_j}+V}$，解决零概率问题 |
| **Bernoulli NB 手算** | 数频次估 prior 和 class-conditional，乘积比较，忽略公共分母 |
| **Multinomial NB 手算** | word count → 频率估计 → Laplace smoothing → joint probability 比较 |
| **sklearn API** | `SVC(kernel=)` / `LinearDiscriminantAnalysis()` / `GaussianNB()` / `DecisionTreeClassifier(max_depth=)` |
| **Assignment 1** | continuous feature，用 normal function 建 density；与 Assignment 2 合并为一份 PDF，10/19 截止，共 20% |

### 8. 本周要点小结

- **本周主题**：从 Bayesian Decision Theory 出发建立概率分类框架，展开 classifier design 的第一部分。
- **四个概率**：prior（初始信念）、class-conditional density（类内特征分布）、posterior（融合证据后的概率）、joint probability（决策直接用的量）。
- **Bayes decision rule**：分到 posterior 最大的类；可用 joint probability 或 log-joint 作 discriminant function（省略公共分母 $p(\boldsymbol{x})$）。
- **Gaussian 假设 + MLE**：假设数据服从 multivariate normal → 用 maximum-likelihood 估 $\boldsymbol{\mu}_j,\boldsymbol{\Sigma}_j$（各类独立估）→ 构造 density → 设计 Bayes classifier。
- **GMM + EM**：多模态数据用 Gaussian Mixture Model 拟合；参数估计无 closed-form → EM 迭代（E-Step 算 responsibility $\gamma_{ik}$，M-Step 加权更新参数）；$M$ 是 hyperparameter，过多 → overfitting，用小 $\alpha$ 判冗余。
- **Naïve Bayes**：假设 feature 间独立 → 1D 估计替代高维 covariance 估计 → 三型（Gaussian/Bernoulli/Multinomial）适配不同数据类型；Laplace smoothing 解决零概率。
- **Python 实现**：sklearn 中 `SVC`、`LinearDiscriminantAnalysis`、`GaussianNB`、`DecisionTreeClassifier` 的 API 与决策线绘制方法。
- **Assignment**：Assignment 1（continuous feature + Gaussian density）已发布，Assignment 2 在 Week 8 发布，合并提交，10/19 截止，共 20%。

---

> **下一周（Week 8）预告**：本周课件覆盖到 Naïve Bayes 结束。`Python_Implementation.pdf` 中已出现 SVM、LDA、Decision Tree 的代码示例，但课件 `ML-Slides3.pdf` 未展开其理论推导。转写末尾老师提到 Assignment 2 在 Week 8（recess 后）发布。推测 Week 8 可能展开 **LDA（Linear Discriminant Analysis）的理论推导**（Fisher criterion、within-class/between-class scatter matrix）与 **SVM（Support Vector Machine）的 maximum margin、hinge loss、kernel trick、soft margin**，或进入 **Decision Tree / 其他 classifier**。具体以 Week 8 课件确认。

---
