# EE6407 Quiz 1 详解（考前学习用）

> **用途**：把 Quiz 1 的**现题（AY25-26 S1，你本次要考的）**与**往年题（AY24-25 S2，参考）**逐题给出题目 + 答案 + 详解，并映射回 `Learning_note.md` 的 Week 1–2 考点，用于备考学习。
>
> **覆盖范围**：Week 1–2 内容——问题分类（black box / NP / P vs NP）、EA 框架、representation、selection、三种 crossover（PMX / OX / CX）、fitness proportional selection、No Free Lunch。
>
> **考核信息**：Quiz 1 占 CA Part 1 全部 10%（前 4 周唯一评分项）；**9 月 1 日 9:30–10:30**，约 15 分钟，**闭卷**，三考场（LT 19A/2A/5），带 ID+笔，不需计算器，禁手机。
>
> ⚠️ 现题（25-26 S1）的答案是我做的**参考解答**，非官方答案 key；往年题（24-25 S2）答案同理。拿不准的题会标注【存疑】并说明理由。

---

## 一、现题：EE6407 QUIZ 1 (25-26 S1)

### Q1. True / False（10 题）

| # | 答案 | 题目（精简） | 详解 |
|---|---|---|---|
| 1 | **F** | EA 三实体（population/parents/offspring）中，offspring pool 的 diversity 大概最高 | **最高 diversity 在初始化时的 population**（随机初始化，见 24-25 题 b 为 True）。selection 减多样性→parents 低；recombination+mutation 注入新组合→offspring 比 parents 高，但 offspring 由"已 selection 过的 parents 的 alleles"生成，多样性有上限，不会超过初始随机种群的展开度。故"offspring 最高"错。【这是本题最易错项】 |
| 2 | **F** | GA 是 metaheuristic，通常能在 P 时间内找到最优解 | GA 是 metaheuristic ✓，但**不保证最优**、**无多项式时间保证**；它只在合理时间找"很好"的解（Week 1：NP-hard → 用近似/metaheuristic，无最优保证）。 |
| 3 | **F** | 算力足够就能证明 P = NP | P vs NP 是关于**算法/复杂度类**的理论问题，与计算资源多少无关；更多资源不改变复杂度类的定义。 |
| 4 | **T** | Metaheuristics 是非确定性方法，能在合理时间内求解 NP 问题 | metaheuristic 本质 stochastic（non-deterministic）✓；用于在合理时间近似求解 NP（-hard）问题 ✓——这正是 Week 1 用 GA 解 NP-hard 的动机。 |
| 5 | **F** | "class NP" 意思是 "non-polynomial deterministic" | NP = **Nondeterministic Polynomial**（非确定性多项式）：解能在**多项式时间内验证**。不是"non-polynomial"。常见陷阱。 |
| 6 | **F** | N-queens 问题是 class P 的例子 | N-queens 的**搜索/求解**是 NP 类（组合搜索/约束）；**验证**一个给定配置无冲突虽是多项式，但"找出"解才是难点，不属 P。 |
| 7 | **F** | 偶数 n>10，permutation `<1,3,5,…,n−1,2,4,6,…,n>` 是无攻击的合法配置 | **反例**：第 1 行列=1、第 n 行列=n → 同在主对角线上 → 攻击。推导：第一半 odds 在 row i 列 2i−1，第二半 evens 在 row n/2+k 列 2k；取 row 1(col 1) 与 row n(col n)：列差 = 行差 = n−1 ⇒ 同对角线冲突。 |
| 8 | **T** | NP-complete 问题需要多项式算法来验证解 | 按定义 NP-complete ∈ NP，而 NP = 可在多项式时间内**验证** ✓。 |
| 9 | **F** | 在复杂地图中找两点间的可行路径是 class NP 问题 | 可行路径/可达性用 BFS/DFS 即可在多项式时间求解 → 属 **class P**，不是 NP。 |
| 10 | **F** | branch-and-bound 是 metaheuristic 之一 | branch-and-bound 是**确定性精确算法**（保证最优，有运行时界），不是 metaheuristic（metaheuristic 是随机/启发式、无最优保证）。 |

**答案汇总**：1-F 2-F 3-F 4-T 5-F 6-F 7-F 8-T 9-F 10-F（2 真 8 假）。

---

### Q2. PMX（Partially Matched Crossover）—— 长度 16 排列

**父母**（高亮段为位置 1–6）：
- P1 = `F E D C B A 9 8 7 6 5 4 3 2 1 0`（段 `F E D C B A`）
- P2 = `B A 8 1 D 9 7 C 2 E 6 0 3 F 4 5`（段 `B A 8 1 D 9`）

**PMX 步骤**：
1. 互换段：offspring1 的位置 1–6 = P2 段 `B A 8 1 D 9`；offspring2 的位置 1–6 = P1 段 `F E D C B A`。
2. 段外位置从"同源 parent"复制，遇重复（与已放入的 P2/P1 段元素冲突）则按**位置配对映射**替换，并沿映射链走到不在段内的元素为止。

**段内位置配对映射**（P1[i]↔P2[i]，i=1..6）：
`F↔B, E↔A, D↔8, C↔1, B↔D, A↔9`

**Offspring 1**（段=`B A 8 1 D 9`，段外取 P1 的位置 7–16 = `9 8 7 6 5 4 3 2 1 0`，替换与 {B,A,8,1,D,9} 冲突者）：
- 位7 `9`→(9↔A)→A→(A↔E)→**E**
- 位8 `8`→(8↔D)→D→(D↔B)→B→(B↔F)→**F**
- 位9 `7`→不冲突→7
- 位10 `6`→6；位11 `5`→5；位12 `4`→4；位13 `3`→3；位14 `2`→2
- 位15 `1`→(1↔C)→**C**
- 位16 `0`→0

→ **Offspring 1 = `B A 8 1 D 9 E F 7 6 5 4 3 2 C 0`**

**Offspring 2**（段=`F E D C B A`，段外取 P2 的位置 7–16 = `7 C 2 E 6 0 3 F 4 5`，替换与 {F,E,D,C,B,A} 冲突者）：
- 位7 `7`→7
- 位8 `C`→(C↔1)→**1**
- 位9 `2`→2
- 位10 `E`→(E↔A)→A→(A↔9)→**9**
- 位11 `6`→6；位12 `0`→0；位13 `3`→3
- 位14 `F`→(F↔B)→B→(B↔D)→D→(D↔8)→**8**
- 位15 `4`→4；位16 `5`→5

→ **Offspring 2 = `F E D C B A 7 1 2 9 6 0 3 8 4 5`**

校验：两者均为 0–9 与 A–F 的合法全排列（16 个元素无重复）。✓

---

### Q3. 三进制编码（Trinary coding）求实数值【存疑：位数】

题：**10-digit trinary** 编码系统表示实数区间 **[0,100]**，求 `<022102112>` 对应实数值。

> ⚠️ 题目说"10-digit"但图中所给字符串为 **9 位**：`0 2 2 1 0 2 1 1 2`。可能为题目/转写笔误。下面按**所给 9 位**计算，并附"若确为 10 位系统"的换算。

**Step 1：把三进制串转成整数（base 3，最高位在前）**

$$
N=\sum_{i=0}^{n-1} d_i\cdot 3^{n-1-i}
$$

n=9，权重 3⁸…3⁰ = 6561, 2187, 729, 243, 81, 27, 9, 3, 1：

$$
N = 0\cdot6561 + 2\cdot2187 + 2\cdot729 + 1\cdot243 + 0\cdot81 + 2\cdot27 + 1\cdot9 + 1\cdot3 + 2\cdot1
$$

$$
= 4374 + 1458 + 243 + 54 + 9 + 3 + 2 = \mathbf{6143}
$$

**Step 2：整数 → [0,100] 实数（归一化）**

- 按 **9 位系统**（3⁹−1 = 19682 为最大值，映射到 100）：
  $$\text{real}=\frac{6143}{3^9-1}\times 100=\frac{6143}{19682}\times100\approx \mathbf{31.21}$$
  （若用 3⁹=19683 为分母则 ≈ 31.20，几乎相同）

- 若题意确为 **10 位系统**且此串作 10 位（前置 0），最大值 3¹⁰−1=59048：
  $$\text{real}=\frac{6143}{3^{10}-1}\times100=\frac{6143}{59048}\times100\approx \mathbf{10.41}$$

**建议**：先确认字符串位数。若 9 位 → **≈ 31.21**；若 10 位系统且串为 9 位（缺前导 0）→ **≈ 10.41**。公式已给，位数定了即可定答案。

---

### Q4. No Free Lunch Theorem 论述题

**要点（论述时逐条展开）**：

1. **定理内容**（Wolpert & Macready）：跨**所有**可能的问题取平均，**任意两个算法（含 random search）的期望性能完全相同**。在某类问题上获得的性能提升，必在另一类问题上以等量损失偿还。
2. **推论 1——无万能算法**：不存在一个对所有问题都最优的"all-purpose"算法；寻找通用最优算法是 **fruitless** 的。
3. **推论 2——性能与适用范围此消彼长**：要在某一类问题上获高性能，须注入 **domain knowledge**（专用 representation、专用 variation operator、repair、local search）→ 即 90 年代的 **memetic algorithm（EA + local search）** 趋势，使性能曲线发生 **curve deformation**（在窄域更高、他域更低）。
4. **实践启示**：
   - 选 representation / variation operator 要"**按问题定制**"（Week 2：choose representation to suit problem）；
   - 不要指望一套 GA 参数通吃所有问题；需在 **exploration（多样性）与 exploitation（聚焦）间针对问题平衡**；
   - 现实中我们只关心**特定问题类**，故定制+领域知识是合理且必要的，NFL 只是从理论上否定"通吃"。
5. **一句话总结**：NFL 告诉我们"优化没有免费午餐"——性能的提升必以适用范围的收窄为代价，因此问题求解应面向具体问题做定制，而非追求普适最优。

---

## 二、往年题：EE6407 QUIZ 1 (24-25 S2) 参考

### Q1. True / False（a–j）

| # | 答案 | 题目（精简） | 详解 |
|---|---|---|---|
| a | **F** | 复杂地图找两点可行路径是 NP 问题 | 同现题 9：可达性/路径 = BFS/DFS = **class P**。 |
| b | **T** | GA 初始化时种群 diversity 最高 | 随机初始化 → 多样性最大（selection 随后逐年降低）。 |
| c | **T** | parent selection 降低多样性，recombination 增加多样性 | selection↓（聚焦 quality）、recombination↑（创造新组合）均符合 Week 2 两股力。 |
| d | **F** | 用 GA 求 NN 权重矩阵 → 这是 simulation 问题 | 求权重 = 已知 input-output 对求 model → 属 **modeling**（black box 缺 model），非 simulation（simulation 是已知 input+model 求 output）。 |
| e | **F** | N-queens 是 class P 的例子 | 同现题 6：N-queens 搜索属 NP 类，非 P。 |
| f | **F** | 二叉树表示下，布尔式 F=abcdef 应有 12 条边 | F=abcdef（6 变量 AND）的**满二叉表达式树**：6 叶 + 5 内部 = 11 节点 → **10 条边**（满二叉树 edges = 2×内部节点 = 10）。12 错。 |
| g | **F** | EA 仅靠 recombination 也能工作 | Week 2 老师明确："若只能留一个算子，**只有 mutation 能独立求解**"；recombination 不能引入新 allele，单独用一般无法有效探索。【注：对 permutation 表示，recombination 可重排已有元素、部分可探索，故此题有争议；按老师口径判 F】 |
| h | **F** | NP = non-distinguishable polynomial | NP = **Nondeterministic Polynomial**，非 "non-distinguishable"。 |
| i | **F** | recombination 增多样性，mutation 减多样性 | 反了：mutation **增**多样性（注入随机），selection **减**；recombination 也增。故"mutation 减"错 → 整句 F。 |
| j | **F** | 算力足够就能证明 P = NP | 同现题 3：P vs NP 与资源无关。 |

**答案汇总**：a-F b-T c-T d-F e-F f-F g-F h-F i-F j-F（2 真 8 假，与现题同分布）。

---

### Q2. Order One Crossover (OX) —— `<abcdefghij>` × `<jaibhcgdfe>`，段位 4–8

**父母**：
- P1 = `a b c [d e f g h] i j`（段 `d e f g h`）
- P2 = `j a i [b h c g d] f e`（段 `b h c g d`）

**OX 步骤**：段从 P1 进 offspring1、从 P2 进 offspring2；段外从**另一 parent** 自段后绕回取、跳过已存在元素。

**Offspring 1**（段=`d e f g h`→占 {d,e,f,g,h}；段外从 P2 自位 9 绕回取，跳过 {d,e,f,g,h}）：
- P2 自位 9 起：`f e j a i b h c g d` → 跳过 f,e,h,g,d → 保留 `j a i b c`
- 填入空位 9,10,1,2,3：j,a,i,b,c

→ **Offspring 1 = `i b c d e f g h j a`**

**Offspring 2**（段=`b h c g d`→占 {b,h,c,g,d}；段外从 P1 自位 9 绕回取，跳过 {b,h,c,g,d}）：
- P1 自位 9 起：`i j a b c d e f g h` → 跳过 b,c,d,g,h → 保留 `i j a e f`
- 填入空位 9,10,1,2,3：i,j,a,e,f

→ **Offspring 2 = `a e f b h c g d i j`**

校验：两者均为 a–j 全排列。✓

---

### Q3. PMX —— 同上父母，段位 4–8

**段**：P1 `d e f g h`，P2 `b h c g d`

**配对映射**（位置 4–8 逐位）：`d↔b, e↔h, f↔c, g↔g(自环), h↔d`
→ 链：`b—d—h—e`（b↔d 由位4，d↔h 由位8，h↔e 由位5）；`f—c`；`g` 自环。

**Offspring 1**（段=`b h c g d`，段外取 P1 的位 1,2,3,9,10 = `a b c i j`，替换与 {b,h,c,g,d} 冲突者）：
- 位1 `a`→a
- 位2 `b`→b↔d→d↔h→h↔e→**e**
- 位3 `c`→c↔f→**f**
- 位9 `i`→i；位10 `j`→j

→ **Offspring 1 = `a e f b h c g d i j`**

**Offspring 2**（段=`d e f g h`，段外取 P2 的位 1,2,3,9,10 = `j a i f e`，替换与 {d,e,f,g,h} 冲突者）：
- 位1 `j`→j；位2 `a`→a；位3 `i`→i
- 位9 `f`→f↔c→**c**
- 位10 `e`→e↔h→h↔d→d↔b→**b**

→ **Offspring 2 = `j a i d e f g h c b`**

校验：均为 a–j 全排列。✓

---

### Q4. Cycle Crossover (CX) —— 同上父母

**CX 步骤**：按 index 构成"环"，环内位取 P1、环外位取 P2（offspring1）；反之得 offspring2。

P1 = `a b c d e f g h i j`，P2 = `j a i b h c g d f e`

**求环（从位 1 起）**：
- 位1 取 P1[1]=`a`；P2[1]=`j` → 找 `j` 在 P1 的位 10 → 位10 取 P1[10]=`j`
- P2[10]=`e` → `e` 在 P1 位 5 → 位5 取 P1[5]=`e`
- P2[5]=`h` → `h` 在 P1 位 8 → 位8 取 P1[8]=`h`
- P2[8]=`d` → `d` 在 P1 位 4 → 位4 取 P1[4]=`d`
- P2[4]=`b` → `b` 在 P1 位 2 → 位2 取 P1[2]=`b`
- P2[2]=`a` → `a` 在 P1 位 1 → 已填，**环闭合**

环位 = {1, 2, 4, 5, 8, 10}（取 P1 值）；非环位 = {3, 6, 7, 9}（取 P2 值）。

**Offspring 1**（环位取 P1，非环位取 P2）：
- 位1=a 位2=b 位4=d 位5=e 位8=h 位10=j；位3=P2[3]=i 位6=P2[6]=c 位7=P2[7]=g 位9=P2[9]=f

→ **Offspring 1 = `a b i d e c g h f j`**

**Offspring 2**（环位取 P2，非环位取 P1）：
- 位1=j 位2=a 位4=b 位5=h 位8=d 位10=e；位3=P1[3]=c 位6=P1[6]=f 位7=P1[7]=g 位9=P1[9]=i

→ **Offspring 2 = `j a c b h f g d i e`**

校验：均为 a–j 全排列。✓（CX 不依赖"段"，由父母串唯一确定；题中阴影段仅作提示。）

---

### Q5. Fitness Proportional Selection 在不同阶段的有效性（论述）

**要点**：
- **早期（population 多样、fitness 分布散）**：roulette wheel 按 fitness 比例分配，差异大 → 选择压力足，高 fit 个体多复制，驱动种群快速改进 → **有效**。风险：若出现"超个体"（fitness 远超其余），会被过度选中 → **premature convergence（早熟收敛）**。
- **中期（fitness 整体上升且彼此接近）**：fitness 差距缩小 → 各个体被选概率趋近 → **区分度下降、选择压力减弱** → 收敛放缓 → 效果变差。
- **晚期（种群趋同、fitness 几乎相等）**：roulette wheel 几乎等概率（近似均匀）→ **几乎没有选择压力** → 停滞。此时**失效**。
- **改进手段**：**fitness scaling**（linear scaling / sigma truncation）拉大区分度；或改用 **ranking selection / tournament selection** 维持稳定压力；或引入 **elitism** 保住最优。
- **结论**：fitness proportional 在早期好用、晚期失效；实务中常随阶段切换或加 scaling 以维持选择压力。

---

## 三、⭐ 三种 Crossover 算子速查（Quiz 1 核心考点）

| 算子 | 机制 | 段外填充规则 | 适用 |
|---|---|---|---|
| **PMX**（部分匹配） | 互换段；段外按**位置配对映射**替换冲突元素，沿映射链走到不冲突 | 用 P1[i]↔P2[i] 配对建映射 | 通用，最常考 |
| **OX**（顺序/Order One） | 互换段；段外从**另一 parent** 自段后绕回取，**跳过已存在**元素 | 保"顺序"信息 | TSP 等顺序问题 |
| **CX**（循环） | 按 index 找**环**；环内位取 P1、环外位取 P2（offspring1 反之 offspring2） | 不需指定段，由父母串唯一决定 | 保"位置"信息 |

**共同点**：三者都保证 offspring 仍是合法 permutation（无重复）；区别在"段外元素如何确定"。

---

## 四、Quiz 1 考点速查（映射回 Learning_note.md）

| 考点 | 出处 | 关键结论 |
|---|---|---|
| black box 三类（optimization/modeling/simulation） | Week 1 §3.1 | 缺 input→优化；缺 model→建模；缺 output→仿真 |
| P / NP / NP-complete / NP-hard | Week 1 §3.4 | NP=多项式可**验证**；NP-hard 至少与 NP-complete 同难 |
| EA 三实体 + 两股力 | Week 2 §2 | mutation+recombination 增多样性；selection 减；初始多样性最高 |
| representation 术语 | Week 2 §3 | chromosome/gene/**locus**/**allele**；encoding 多对一、decoding 一对一 |
| selection（parent 随机 / survivor 确定） | Week 2 §6 | roulette wheel / ranking；elitism |
| fitness proportional 阶段性 | Week 2 §6.1 + 本 Q5 | 早期有效、晚期失效，需 scaling/换 ranking |
| PMX / OX / CX | Week 2 §9.3 + 本文件三 | 见速查表 |
| No Free Lunch | Week 2 §11.4 | 跨所有问题平均所有算法相同；无万能算法 |
| metaheuristic vs branch-and-bound | Week 1 §3.4 + Week 2 §12 | 前者随机无最优保证；后者确定性精确 |

---

## 五、易错点清单

1. **NP 的全称**：Nondeterministic Polynomial（非"non-polynomial"/"non-distinguishable"）——两份 quiz 都考，必考。
2. **路径/可达性是 P 不是 NP**——两份都考。
3. **求 NN 权重是 modeling 不是 simulation**——black box 分类高频陷阱。
4. **初始多样性最高**，不是 offspring——与"selection 减、variation 增"配合理解。
5. **mutation 才能独立求解**，recombination 单独不行（按老师口径）。
6. **PMX 段外要沿映射链走**，不能只替换一步（如本题 9→A→E，8→D→B→F）。
7. **OX 段外从"另一 parent"段后绕回取、跳过已存在**；不是从同源 parent 取。
8. **CX 不需要段**，由父母串的 index 环决定。
9. **branch-and-bound 是确定性精确算法，不是 metaheuristic**。
10. **trinary/二进制编码**：先按权展开求整数，再 `/(max)×区间长` 归一化；注意位数（本题 9 vs 10 存疑）。

---

> **下次更新**：若你添加 quiz2 / 往年 final 题，我用同样格式逐题详解，文件放对应文件夹（如 `6407/quiz2/`、`6407/final/`），并在此文件末尾追加索引链接。
