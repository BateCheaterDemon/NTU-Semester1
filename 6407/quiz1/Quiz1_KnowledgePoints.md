# EE6407 Quiz 1 知识点总结（知识点 + 英文术语）

> 范围：Week 1–3（Lecture 1 + Lecture 2 + 收尾）。闭卷，15 分钟，无计算器，带 photo ID + 笔。
> 本文档以**考点**为单位组织，所有核心术语保留英文原词，中文仅作释义与连接。

---

## 1. Black Box Model — 问题分类四视角

把求解系统拆成 **input — model — output**，缺哪个决定问题类型：

| 缺什么 | 问题类型 | 英文术语 | 例子 |
|---|---|---|---|
| 缺 input | 优化问题 | **optimization** | TSP, 排课, 八皇后, 卫星设计 |
| 缺 model | 建模问题 | **modelling** | 神经网络训练, 股价预测 |
| 缺 output | 仿真问题 | **simulation** | 天气预报, 新税制影响 |

- **关键桥接**：modelling 可转 optimization（定义 error 的 objective function 即可，如 NN 训练 = 最小化误差）。
- **simulation 与 optimization 区别**：simulation 不搜索巨大 search space，而是给定 input 看 output（what-if 分析）。

---

## 2. Optimization vs Constraint Satisfaction 四象限

| | 有约束 (constraint) | 无约束 |
|---|---|---|
| 有 objective function | **COP**（Constrained Optimization） | **FOP**（Free Optimization） |
| 无 objective function | **CSP**（Constraint Satisfaction） | 非问题 |

### 2.1 核心区分（高频考点）

- **Objective function（目标函数）**：给每个 candidate solution 一个**连续的质量评分**（continuous quality score）。
- **Constraint（约束）**：**二元 yes/no 判断**（binary feasibility test），不可"半满足"。

> ⚠️ 陷阱：constraint 不是连续评分，连续评分属于 objective function。

### 2.2 约束分类

- **Hard constraint**：不可协商，必须满足（must satisfy）。
- **Soft constraint**：最好满足，不满足仍是 feasible solution。

### 2.3 八皇后投票示例（判 CSP/COP/FOP）

1. "放 n 皇后使 ≥98% 非攻击" → **CSP**（硬要求）。
2. "最大化非攻击皇后数" → **FOP**（纯目标）。
3. "随机初始、每后只动一次、步数最小且非攻击最大化" → **COP**（约束 + 目标，类 local search）。

---

## 3. Search Problems 视角

- 把求解视为在 **search space** 中找解。
- **search problem**：定义 search space；**problem-solver**：如何在空间中移动寻解。
- search space 含所有 candidate objects，**包括 desired solution**。
- 例 TSP n 城市有 $n!$ 量级可能 tour。

---

## 4. NP 复杂度类（必考概念）

### 4.1 基本量

- **Problem size**（问题规模 $n$）：维度/变量取值数。
- **Running time**：算法终止所需操作数，取最坏情况关于 $n$ 的函数：**polynomial / super-polynomial / exponential**。
- **Problem reduction**（问题归约）：把一个问题映射成另一个；若映射在 polynomial time 内完成则可复用算法。

### 4.2 复杂度类定义

| 类 | 定义 |
|---|---|
| **Class P** | 可在 polynomial time 内**求解** |
| **Class NP**（Nondeterministic Polynomial） | 解可在 polynomial time 内**验证**（verifiable）；**P ⊆ NP** |
| **NP-complete** | 属 NP，且**所有** NP 问题可 polynomial 归约到它 |
| **NP-hard** | 至少与 NP-complete 一样难，但**不一定属 NP**，解**不一定可验证** |

### 4.3 关键结论

- **P vs NP 未解决**（P = NP? 仍未证明）；普遍接受 P ≠ NP。
- ⚠️ **NP-hard 不保证 polynomial time 可验证**（如 TSP 求最优距离）。
- 对 NP-hard 问题采用 **metaheuristic**（GA 即一种 metaheuristic = "heuristic about heuristics"）。

> ⚠️ 陷阱词："currently known that P is different from NP" = **False**。

---

## 5. EC 起源与生物启发

### 5.1 历史脉络

| 年 | 人物 | 贡献 |
|---|---|---|
| 1948 | Turing | "genetical or evolutionary search" |
| 1962 | Bremermann | 进化与重组优化 |
| 1964 | Rechenberg | **evolution strategies** |
| 1965 | Fogel, Owens & Walsh | **evolutionary programming** |
| **1975** | **Holland** | **Genetic Algorithm (GA)** — 转折点，引入 **crossover** |
| 1992 | Koza | **Genetic Programming (GP)** |

### 5.2 Darwinian Evolution（达尔文进化）

- 资源有限 → 竞争 → **selection**。
- **Fitness**：派生的次级度量，后代多者更 fit。
- **Phenotypic traits**：影响环境响应的性状，部分遗传、部分发育、部分随机。
- ⭐ **个体是 unit of selection；种群是 unit of evolution**（进化 = 种群随时间变化）。

### 5.3 Genetics（遗传学）

- **Genotype 决定 phenotype**；映射复杂：
  - **Pleiotropy**（基因多效性）：一个基因影响多个性状。
  - **Polygeny**（多基因性）：多个基因影响一个性状。
- **Chromosome** 含 gene；**Diploidy**（二倍体）；**Genome**（基因组）。
- **Mutation**：复制时遗传物质小变化；后果可能灾难性/中性/有利。

---

## 6. EA 框架（三实体 + 两股力）

### 6.1 三实体与伪代码

**Population → Parents → Offspring**

```
initialize → evaluate
loop:
  select parents → recombine → mutate → evaluate → select survivors
until terminate
```

- EA 属 **generate-and-test** 类算法。
- 本质 **parallel search**（种群 = 多点采样）。
- **Neo-Darwinism**：在 fitness landscape 上做 optimization。

### 6.2 ⭐ 两股力（Two Pillars / Competing Forces）

| 力 | 作用 | 驱动者 | 效果 |
|---|---|---|---|
| **增多样性** | exploration（探索 novelty） | mutation + recombination | 注入随机性、跳 local optimum |
| **减多样性** | exploitation（聚焦 quality） | parent selection + survivor selection | 让更优个体占更大比例 |

- **好优化 = 平衡这两股力**。GA 不收敛 = 多样性没平衡好。
- ⚠️ 陷阱："parent selection 增加 diversity" = **False**（selection 减 diversity）。

---

## 7. Representation（表示）

### 7.1 两层存在与两个映射

- **Phenotype**（表型）：真实世界解。
- **Genotype**（基因型）：算法里操纵的编码（"digital DNA"）。
- **Encoding**（编码）：phenotype → genotype，**可多对一**。
- **Decoding**（解码）：genotype → phenotype，**必须一对一**（不可歧义）。
- genotype 空间必须能表示**所有** feasible solution，否则找不到 global optimum。

### 7.2 术语（必考辨析）

- **Chromosome**：一条 DNA 串，含多个 **gene**。
- **Locus**（单数）/ **loci**（复数）：gene 在串上的**位置**。
- **Allele**：gene 的**取值**。
- 例 TSP `5 4 3 2 1`：gene 2 的 locus 是第 2 位，allele = 4。

### 7.3 五种表示对应流派

| 表示 | 历史 EA 流派 |
|---|---|
| Binary string | **Genetic Algorithms (GA)** |
| Real-valued vector | **Evolution Strategies** |
| Finite State Machine (FSM) | **Evolutionary Programming** |
| LISP tree / program | **Genetic Programming (GP)** |

现代观点：**按问题选 representation → 按表示选 variation operator**。selection 只用 fitness，与表示无关。

---

## 8. Evaluation / Fitness Function

- 又叫 **quality function / objective function**。
- 给每个 phenotype 赋**单一实值 fitness**。
- 通常 **maximize**；minimization 转 maximization 很简单。
- **区分度越大越好**。
- ⭐ **Fitness 是"真实问题"与"算法"的唯一桥梁**——GA 通用性的来源。

---

## 9. Population

- 形式上是 individual 的 **multiset**（多重集，允许重复）。
- Population 是 **evolution 的单位**；**selection 作用在 population 层，variation 作用在 individual 层**。
- **Diversity** 三种含义须说清：fitness diversity / phenotype diversity / genotype diversity。

---

## 10. Selection Mechanism

### 10.1 Parent Selection（通常 **stochastic**）

- 高质量个体更可能被选，但**不保证**；最差个体通常也有**非零概率**（有助跳 local optima）。
- **Roulette wheel selection**（轮盘赌）：slot 大小 ∝ fitness。
- **Ranking selection**：按 fitness 排名，弱化绝对差异。

### 10.2 Survivor Selection（通常 **deterministic**）

- **Fitness-based**：合并后按 fitness 排序取前 N。
- **Age-based**：生多少子代就删多少父代。
- **Elitism**（精英保留）：stochastic + deterministic 混合，保住最优不丢。

### 10.3 ⭐ Fitness Proportional Selection 早晚期的问题（高频简答）

- **Early stage**：fitness gap 大 → 少数个体 selection probability 过高 → selection pressure 过强 → diversity 快速丢失 → **premature convergence**（早熟收敛）。
- **Late stage**：fitness gap 小 → roulette wheel 概率近乎均等 → selection pressure 太弱 → 接近 random selection → **convergence 变慢**。

> 记忆线：early = gap 大 → pressure 太强；late = gap 小 → pressure 太弱。

---

## 11. Variation Operators（按 arity 分类）

| arity | 算子 | 说明 |
|---|---|---|
| 1 | **mutation** | 作用于 1 个 genotype，小随机扰动 |
| >1 | **recombination** | 合并多亲本信息；arity=2 即 **crossover** |

### 11.1 ⭐ 核心结论

- **Mutation-only EA 可行；crossover-only EA 不可行**。
  - 原因：crossover **不改变 allele 频率**，无法引入新 allele。
  - 例：首 bit 50% 为 0 的种群做任意次 crossover，0 的比例不变。
- 若只能留一个，**只有 mutation 能独立求解**。

### 11.2 Exploration vs Exploitation（Lecture 分工，高频简答）

| 算子 | 角色 | 行为 |
|---|---|---|
| **Crossover** | **explorative** | 组合两亲本信息，跳到"之间"区域，大跳 |
| **Mutation** | **exploitative** | 亲本附近小幅随机扰动，就地优化 |

- 两者既有 **co-operation 又有 competition**。
- 为何两者都要：crossover 组合 parent 信息但**不引入新 allele**；mutation 引入新 allele 但缺乏组合能力 → 互补。

> ⚠️ 注意："两股力"里 mutation+recombination 同属增多样性（exploration）；但 Lecture 在算子分工时把 crossover=exploration、mutation=exploitation（一个谈搜索行为，一个谈多样性来源，不矛盾）。

---

## 12. ⭐ 五种 Representation 下的算子详解

### 12.1 Binary Representation

- **Mutation**：逐 gene 以 $p_m$ 翻转 0↔1。$p_m$ 通常 **1/pop_size 到 1/chromosome_length**。
  - 可用 **gray coding**（格雷码）缓冲 **Hamming cliff**（相邻整数二进制只差 1 bit）。
- **1-point crossover**：随机切点，交换尾部。$p_c$ 通常 **0.6–0.9**。
- **n-point crossover**：选 n 个切点，交替拼接（仍有 positional bias）。
- **Uniform crossover**：逐 gene 抛硬币决定来源，**与位置无关**（消除 positional bias）。
- ⭐ **Positional bias**（位置偏置）：1-point 依赖基因排列顺序，**无法同时保留串两端的 gene**。了解问题结构可利用，否则用 n-point / uniform。

### 12.2 Integer Representation

- **Crossover**：复用 binary 的 n-point / uniform。
- **Mutation**：
  - **Creep mutation**（爬行）：加小整数（正或负），移到**相近值**。
  - **Random resetting**（随机重置）：随机选新值（类别变量尤其用此）。
- 典型应用：**graph coloring / k-colouring**。

### 12.3 Real-Valued Representation

**二进制近似实值**（区间 $[x,y]$，L-bit 串）：

$$g(a_1,\dots,a_L)=x+\frac{y-x}{2^L-1}\sum_{j=0}^{L-1}a_{L-j}\cdot 2^j\in[x,y]$$

- 仅 $2^L$ 个离散值代表无穷集；**L 决定最大精度**。
- ⚠️ **L-bit 不能精确表示无穷多实数**；**L 越长 precision 越高，但 chromosome 更长、进化更慢**。

**Mutation**：
- **Uniform mutation**：从 $[LB_i,UB_i]$ 均匀随机抽取。
- **Non-uniform mutation**：加 **$N(0,\sigma)$ 高斯扰动**后截断：$x'_i=x_i+N(0,\sigma)$。$\sigma$ = **mutation step size**。
- ⭐ **Self-adaptive mutation**：把 $\sigma$ 编入 genome $\langle x_1,\dots,x_n,\sigma\rangle$，$\sigma$ 自行协同演化。
  - **顺序（必考）**：**先变 $\sigma\to\sigma'$，再用新 $\sigma'$ 变 $x\to x'=x+N(0,\sigma')$**。
  - 原因：$\sigma'$ 被**双重评估**——$x'$ 好当 $f(x')$ 好；$\sigma'$ 好当它产生的 $x'$ 好。反过来变则失效。

**Crossover（实值专用）**：
- **Discrete**：每 allele 从一亲本取，$z_i=x_i$ 或 $y_i$。
- **Intermediate**（= arithmetic recombination）：$z_i=\alpha x_i+(1-\alpha)y_i$。
  - **Single arithmetic**：选一个 gene $k$ 混合，其余保持。
  - **Simple arithmetic**：$k$ 之前保持亲本1，$k$ 及之后混合。
  - **Whole arithmetic**：**最常用**，全分量混合 $z_i=\alpha x_i+(1-\alpha)y_i$。
- **Blend Crossover (BLX)**：$z_i\in[x_i-\alpha d_i,\,x_i+\alpha d_i]$ 均匀采样，$d_i=y_i-x_i$；$\alpha=0.5$ 最佳。
- 几何：single/simple/whole arithmetic 落 **inner box**；blend 落 **outer box**（范围更宽）。

**Multi-parent recombination**：
- **Type 1（分段重组）**：diagonal crossover，选 n−1 切点拼接 n 子代。
- **Type 2（算术组合）**：allele = n 亲本该 allele 的平均 → "质心"子代。

### 12.4 Permutation Representation（TSP / 排序类）

- n 个整数排成 n 位，每个恰好出现一次。
- **生产调度**关心 **order**（顺序）；**TSP** 关心 **adjacency**（邻接）。
- search space 极大：30 城市 ≈ $30!\approx 10^{32}$。
- ⚠️ **为何不能用普通算子**：bit-flip 改一个值会产生**重复/缺失 allele** → 不可行解。故须专用算子。

**Mutation（四种）**：

| 算子 | 操作 | 保留信息 |
|---|---|---|
| **Swap** | 交换两个 allele 位置 | 保留顺序与邻接 |
| **Insert** | 选两个 allele，第二个移到第一个之后，其余后移 | 保留大部分顺序与邻接 |
| **Scramble** | 选 gene 子集打乱重排 | — |
| **Inversion** | 反转两 allele 间子串 | 保留大部分邻接，破坏顺序 |

> ⚠️ random-reset / bit-flip 单基因重置对 permutation **不适用**（产生重复/缺失）。

**Crossover（四种，保留顺序/邻接）**：

| 算子 | 核心思想 |
|---|---|
| **Order 1 crossover (O1)** | 保留**相对顺序**：从 P1 复制一段，余下从切点起按 **P2 顺序**填入（跳过已有、wrap-around） |
| **Partially Mapped Crossover (PMX)** | 复制段 + 段内**allele 映射**修复段外冲突 |
| **Cycle Crossover (CX)** | 每 allele **连同位置**继承自一个亲本；按 **position cycle** 交替 |
| **Edge Recombination** | 构造两亲本**邻接边表**，优先共同边或最短候选 |

### 12.5 Tree Representation（GP）

- genotype 为**可变深宽**的树（GA/ES/EP 是线性定长）。
- 由 **terminal set T** 与 **function set F** 递归定义。
- **Closure property**：无类型，任何 function 可接受任何子表达式。
- **Mutation**：随机选**子树替换**为随机新树。$p_m$ 建议 **0**（Koza）或 **0.05**（Banzhaf）。子代可能比亲本大。
- **Recombination**：两亲本各选**子树交换**。子代可能比亲本大。

### 12.6 速查表

| 表示 | Mutation | Crossover |
|---|---|---|
| **Binary** | bit-flip（$p_m$≈1/pop_size–1/len；gray coding） | 1-point / n-point / uniform（$p_c$≈0.6–0.9）；注意 positional bias |
| **Integer** | creep / random resetting | 复用 binary 的 n-point / uniform |
| **Real-valued** | uniform / non-uniform（Gaussian $N(0,\sigma)$）/ self-adaptive（$\sigma$ 入 genome） | discrete / intermediate（single/simple/**whole** arithmetic）/ blend（BLX）/ multi-parent |
| **Permutation** | swap / insert / scramble / inversion | O1 / PMX / cycle / edge recombination |
| **Tree (GP)** | 子树替换（$p_m$≈0–0.05） | 子树交换 |

---

## 13. Initialization & Termination

### 13.1 Initialization

1. **Random**：最常用，天然带来 diversity；初始质量差但进化会变好。
2. **Prior knowledge / heuristic seed**：初始质量高，但**限制搜索区域** → 利于 local optimum，可能远离 global optimum。
- ⚠️ **过度 seed 增加 premature convergence 风险**；全局优化不宜过度 seed。

### 13.2 Termination

- 达目标 fitness / 最大代数 / 最小 diversity（steady state）/ 连续 N 代无 fitness 改进（**convergence**）。

---

## 14. ⭐ 实例：Eight-Queens 完整建模

### 14.1 Representation

- genotype = **1–8 的 permutation**（gene = 列位，allele = 行值）。
- ⭐ permutation 天然满足**同列、同行**约束，只剩**对角线冲突**。

### 14.2 Fitness 公式

$$C(Q)=\sum_{i=1}^{8}\sum_{k=i+1}^{8}\delta_{ik},\quad \delta_{ik}=\begin{cases}1,&|Q_i-Q_k|=|i-k|\ (\text{同对角线})\\0,&\text{otherwise}\end{cases}$$

- **最大冲突数 = 28**（$7+6+\dots+1$）。
- 归一化 fitness：

$$\text{fitness}(Q)=1-\frac{C(Q)}{28}$$

- $C(Q)=0$ ⇒ fitness = 1（解）。

### 14.3 算子

- Mutation：交换一对 allele（保持 permutation）。
- Recombination：Order 1 crossover。
- Selection：roulette wheel；survivor deterministic。

---

## 15. ⭐ 实例：SGA $f(x)=x^2$（Goldberg 经典）

- 5-bit 编码 $x\in\{0,\dots,31\}$，pop size = 4。
- 初始：`01101`(13,169)、`11000`(24,576)、`01000`(8,64)、`10011`(19,361)，total = 1170，avg = 293。
- Roulette wheel 按 fitness 比例：`11000` 占 49.2% 得 2 份，`01000` 占最低得 0 份。
- 一代后 total = 1754，avg = 439 ⇒ **selection pressure + recombination 使 avg fitness 显著上升**。

---

## 16. 性能观 + No Free Lunch

### 16.1 Goldberg view (1989)

- **random search**：全域最低。
- **problem-specific custom method**：窄域极高、他域很差（尖峰）。
- **GA**：全域都还不错，**robust**，普遍优于 random search。

### 16.2 Curve deformation（90s）

- 注入 domain knowledge → 目标问题子集性能更好、他域更差 → **memetic algorithm**（EA + local search）。

### 16.3 ⭐ No Free Lunch Theorem

- 跨**所有**问题取平均，**所有算法（含 random search）性能相同**。
- 推论：**不存在万能 all-purpose 算法**；追求某类问题高性能必然牺牲适用范围。

---

## 17. EC vs Global/Local Optimization

| 路线 | 特点 | 哲学 |
|---|---|---|
| **Deterministic**（branch and bound） | 保证找 $x^*$，但可能 super-polynomial | "I don't care if it works as long as it **converges**" |
| **Heuristic / GA**（generate and test） | 无最优保证、无运行时界，但实用 | "I don't care if it **converges** as long as it **works**" |
| **Neighbourhood / local search** | 保证局部最优，但含多个 local optima | — |

- **EA 区分性特征**：population、多个 stochastic 搜索算子、arity>1 variation、stochastic selection。

---

## 18. Permutation Crossover 手算模板（必考）

### 18.1 Order 1 Crossover (O1) 步骤

1. 复制 P1 的 **segment** 到 Child1 对应位置。
2. 从 **P2 的切点之后**开始**循环读取**（wrap-around），**跳过已出现元素**。
3. 按读取顺序填入 Child1 的**空位**（从切点之后第一个空位起）。
4. Child2 对调亲本角色。

**示例**：P1=`1 2 [3 4 5 6 7] 8 9 A`，P2=`9 1 [8 2 7 4 6] 3 5 A`，位置 3–7。
- Child1：段 `[3 4 5 6 7]`；从 P2 位置 8 后循环读 `3 5 A 9 1 8 2 7 4 6`，去段内已有 `{3,4,5,6,7}` 得 `A 9 1 8 2`，从位置 8 起填 → `<8 2 3 4 5 6 7 A 9 1>`。

### 18.2 PMX 步骤

1. 复制 P1 段到 Child1，复制 P2 段到 Child2。
2. 段内建 **allele 映射**（P1 段 ↔ P2 段，逐位置对应）。
3. 段外位置：若该 allele 在自己段内已出现，用映射替换；否则保留对方亲本的对应位置值。

**示例**（同上）：映射 `3↔8, 4↔2, 5↔7, 6↔4, 7↔6`。
- O1=`<9 1 3 4 5 6 7 8 2 A>`，O2=`<1 5 8 2 7 4 6 3 9 A>`。

### 18.3 Cycle Crossover (CX) 步骤

1. 从位置 1 起，沿 `P1[1]→P2[1]→P1中该值所在位置→…` 找 **cycle**（按位置走，回到起点算一个 cycle）。
2. 每 cycle 内 allele **连同位置**继承自同一亲本。
3. 交替 cycle 分别给两子代。

**示例**：P1=`<1 2 3 4 5 6 7 8 9 A>`，P2=`<9 1 8 2 7 4 6 3 5 A>`。
- C1={1,2,4,5,6,7,9}, C2={3,8}, C3={10}。
- O1=`<1 2 8 4 5 6 7 3 9 A>`，O2=`<9 1 3 2 7 4 6 8 5 A>`。

> ⚠️ 易错：cycle 按**位置**走，不是按值。单点 cycle 要单独算。

---

## 19. Graph Colouring 建模（应用题模板）

四件套：**Representation → Gene/Allele → Fitness → Optimum condition**。

1. **Representation**：integer，`Q=⟨q1,…,qn⟩`，`qi∈{1,2,3,4}`。
2. **Gene/Allele**：gene position i = 第 i 个 region；allele qi = 该 region 的 colour。
3. **Fitness**（两种等价定义）：
   - 最大化不同色邻接对：$F(Q)=\sum_{(i,j)\in E}[q_i\neq q_j]$，maximize。
   - 或最小化冲突：$C(Q)=\sum_{(i,j)\in E}[q_i=q_j]$，minimize。
4. **Optimum**：$C(Q)=0$（或 $F(Q)=|E|$）→ feasible 4-colouring。

> ⚠️ fitness 要映射到图的**邻接边集 E**，不是所有两两组合。

---

## 20. 应试速查

### 20.1 T/F 陷阱词

见到 **always / must / only / guaranteed / known** 立即怀疑。典型：
- "P is different from NP is currently known" → **False**。
- "crossover alone can create a new allele" → **False**。
- "NP-hard must be verifiable in polynomial time" → **False**。
- "parent selection increases diversity" → **False**。
- "L-bit can represent infinitely many reals exactly" → **False**。
- "starting exclusively from known good solutions always performs better" → **False**。

### 20.2 必背结论句

1. **Mutation-only EA works; crossover-only EA does not.**
2. **Crossover combines parent information; mutation introduces new alleles.**
3. **Crossover is explorative; mutation is exploitative.**
4. **Self-adaptive: mutate σ first, then use σ' to mutate x.**
5. **No Free Lunch: averaged over all problems, all algorithms perform equally.**
6. **P ⊆ NP; P vs NP unsolved.**
7. **NP-hard need not belong to NP / be verifiable in polynomial time.**

### 20.3 必手写过程

O1 / PMX / CX **必手写步骤**，不要只背最终 offspring——过程分在 wrap-around 与映射。

### 20.4 简答题结构

用**对比结构**作答（early vs late、exploration vs exploitation），各给一句"原因 + 后果"。

### 20.5 考前优先确认不混淆的对照

- optimization / modelling / simulation
- objective function / constraint
- P / NP / NP-complete / NP-hard
- selection / recombination / mutation
- exploration / exploitation
- O1 / PMX / CX
- fitness proportional selection early / late stage 的问题
- positional bias：1-point 有、n-point 仍有、uniform 消除
- L-bit precision：越长精度越高但 chromosome 更长

---

## 21. 考试安排

| 项目 | 内容 |
|---|---|
| 日期 | 9 月 1 日（周一） |
| 时间 | 9:30–10:30，约 15 分钟 |
| 范围 | Week 1–3（不含 Week 4） |
| 形式 | **closed book**、书面作答 |
| 必带 | **photo ID + 笔** |
| 不需 | 计算器（题目设计成无需计算器） |
| 禁止 | 手机及智能设备 |
| 考场 | LT 19A / LT 2A / LT 5（去哪个看 NTULearn） |
| 占分 | 10%（前半学期唯一一次考核，无作业、不考勤） |
