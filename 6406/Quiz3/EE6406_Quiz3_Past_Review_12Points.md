# EE6406 Quiz 3 往年重点回顾（12 条 + 相关知识点）

**Analytic and Ensemble Machine Learning · Simon Liu 部分**

> 用途：考前最后一遍“往年 Quiz 3 重点”回顾
> 考试：**2026-11-05（周四）20:00，50 分钟**；online + in-class + lockdown；**T/F + MCQ + Short Calculations**；范围 **Lecture 9–11**；notebook 不考
> 来源：你提供的 12 条往年重点 + `6406/week9–11` 官方 slides + `6406/Quiz3/EE6406_集成学习详细笔记.md`
> 配套：完整版复习资料见 `6406/Quiz3/EE6406_Quiz3_Review_L9-11.pdf`（23 页）；本文是**考前速览 + 相关知识点补充**。

---

## 0. 怎么用这份资料

1. 先看 §1 的 **12 条速查表**（2 分钟）。
2. 逐条看 §2 的 **考点 + 正确结论 + 相关知识点 + 陷阱**（约 25 分钟）。
3. 做 §3 的 **12 条 T/F 快问快答**（5 分钟）。
4. 考前 5 分钟只看 §4 的“一句话版”。
5. 如果还有时间，看 §5 的 **AdaBoost 补充**（往年也常混一题）。

---

## 1. 12 条速查表

| # | 你给的考点 | 正确结论 | 对应 Lecture |
|---|---|---|---|
| 1 | GB 的意义：每个新的预测 R | 新学习器拟合 **residual / pseudo-residual（负梯度）**，再加到 ensemble | L11 |
| 2 | 为什么用 R 树——高 var | **Bagging/RF 用深树**（high variance）→ 平均降 variance；**GBDT 用浅树**（high bias）→ boosting 降 bias | L9–L11 |
| 3 | Bagging 降 bias、var 不变？ | **❌ 错**：Bagging 主要降 **variance**，bias 近似不变 | L9 |
| 4 | Impurity-based 缺陷：偏向 ID 这种 | **✅ 偏向 high-cardinality 特征**（ID、唯一值多） | L10 |
| 5 | LightGBM 对 missing 免疫 | **能原生处理**（学 default direction）；“免疫”太绝对 | L11 |
| 6 | OOB ≈ 37% | **✅ 36.8%**；in-bag 约 63.2% | L10 |
| 7 | 非线性的特殊处理 | 树用 **axis-aligned splits** 分段常数，天然处理非线性和交互 | L9–L11 |
| 8 | EFB | **Exclusive Feature Bundling**：互斥稀疏特征合并 + offsets | L11 |
| 9 | Random feature 定义 | RF **每次 split 随机选 feature 子集**，再选最优 split | L10 |
| 10 | Pseudo-residual，squared loss | `r = -∂L/∂F`；`L=(y-F)^2` → `r=2(y-F)`；`L=1/2(...)²` → `r=y-F` | L11 |
| 11 | γ 的作用 | **XGBoost**：每叶惩罚，`Gain > γ` 才分裂；**GBDT**：步长 | L11 |
| 12 | 最纯 / Gini | `G=1-Σp_k²`；纯节点 **G=0**；二分类最大 0.5 | L9 |

---

## 2. 逐条精讲（考点 + 相关知识点 + 陷阱）

### 1️⃣ GB 的意义：每个新的预测 R

**正确结论**：Gradient Boosting 每一轮的新学习器拟合的是**当前模型的残差 / 伪残差（负梯度）**，不是原始目标 `y`。

**相关知识点**：

- 加性模型：

```
F_m(x) = F_{m-1}(x) + η * γ_m * h_m(x)
```

- 伪残差：

```
r_i = - ∂L(y_i, F) / ∂F |_{F=F_{m-1}(x_i)}
```

- 平方损失 `L=(y-F)^2` → `r=2(y-F)`；若 `L=1/2(y-F)^2` → `r=y-F`。
- 一般损失（如 logistic）→ 负梯度，不一定等于 `y-F`。

**可能的考法**：

- T/F：“GB 的每个新学习器都拟合原始 y” → ❌。
- MCQ：“GB 的每一轮拟合什么？” → residual / negative gradient。

**陷阱**：把 GB 和 AdaBoost 混——AdaBoost 改**样本权重**，GB 改**目标值（拟合残差/负梯度）**。

---

### 2️⃣ 为什么用回归树——高 variance

**正确结论**：要分两种方法说：

| 方法 | 用什么树 | 原因 |
|---|---|---|
| **Bagging / Random Forest** | **深树**（low bias, **high variance**） | 单棵树 variance 高；平均多棵树降 variance |
| **GBDT / Boosting** | **浅树**（**high bias**, low variance） | boosting 逐轮降 bias；浅树是 weak learner |

**相关知识点**：

- 单棵深树：低 bias、**高 variance**，对训练集小变化敏感；
- 平均 M 棵树的 variance：`Var = σ²(ρ + (1-ρ)/M)`；
- GBDT 用 depth 3–5（或 3–7）的浅树，避免一开始就过拟合。

**可能的考法**：

- T/F：“GBDT 用回归树是因为树 high variance” → ❌（不准确；high variance 是 bagging 用深树的理由）。
- MCQ：“为什么 RF 用深树？” → 单棵树高 variance，平均可降 variance。

**陷阱**：把 bagging 的“深树”理由套到 boosting 上。GBDT 用的是**浅树**。

---

### 3️⃣ Bagging 降低 bias、var 不变，对不对？

**正确结论**：**❌ 错，说反了。**

- **Bagging 主要降低 variance**；
- **bias 近似不变**（基模型同期望等假设下，平均不改变期望）；
- **Boosting 主要降低 bias**。

**相关知识点**：

```
Var(avg) = σ² ( ρ + (1-ρ)/M )
```

- ρ=0 → `σ²/M`（平均很有效）；
- ρ=1 → `σ²`（平均无效）；
- ρ 越小 → bagging 降 variance 越有效 → RF 随机选特征就是为了降低 ρ。

**可能的考法**：

- T/F：“Bagging reduces bias while variance stays unchanged” → ❌。
- 正确表述：“Bagging reduces variance; bias is approximately unchanged.”

**陷阱**：Bagging 不是“万能提升”；如果基模型本身很 biased，平均仍然是 biased。

---

### 4️⃣ Impurity-based 缺陷：偏向 ID 这种

**正确结论**：**✅ 对。** 基于不纯度下降的 feature importance 会偏向 **high-cardinality** 特征（ID、编号、唯一值很多的特征）。

**相关知识点**：

- Impurity-based importance：累计某特征分裂带来的加权 Gini/entropy 下降；
- 高基数特征有更多候选 split 点 → 更容易“碰巧”降低 impurity → 重要性虚高；
- ID 每个样本一个值，可以轻易把训练集切开，但对新数据没有预测力。

**改进**：

- **Permutation importance**：打乱某特征，看验证性能下降；
- **Drop-column importance**：删掉某特征重训；
- 删除 ID / 高基数无意义特征；
- 相关特征会互相替代 → 单特征重要性可能被低估。

**可能的考法**：

- T/F：“Impurity-based importance can be biased toward high-cardinality features” → ✅。
- MCQ：“ID 特征 importance 很高，最可能原因？” → high-cardinality bias。

---

### 5️⃣ LightGBM 对 missing 免疫

**正确结论**：LightGBM **能原生处理 missing values**，不需要手动 imputation；但“**免疫**”太绝对。

**相关知识点**：

- 每个 split 尝试把 missing 全分到左 / 全分到右；
- 选 gain 更大的方向作为 **default direction**；
- 训练和预测使用同一个 default direction；
- XGBoost 也有类似机制；
- 如果 missing 本身有信息（missing not at random），模型可能学到偏差；缺失编码/参数（如 `zero_as_missing`）仍会影响结果。

**可能的考法**：

- T/F：“LightGBM can handle missing values without imputation” → ✅；
- T/F：“LightGBM is immune to missing values” → ❌（过于绝对）。

**陷阱**：把“能处理”说成“完全不受影响”。

---

### 6️⃣ OOB ≈ 37%

**正确结论**：**✅ 36.8% ≈ 37%** 的样本在一个 bootstrap 样本中一次都没出现（OOB）。

**相关知识点**：

```
P(not selected) = (1 - 1/n)^n → e^(-1) ≈ 0.368
```

- 约 **36.8%** OOB；
- 约 **63.2%** 的不同原始样本 in-bag；
- OOB error：每条样本用“没抽到它的树”预测，聚合后算误差；
- OOB 是内部验证，不是所有场景下独立 test set 的替代品（时间序列、数据泄漏要额外设计）。

**可能的考法**：

- 计算：n=1000，OOB 比例？→ `(1-1/1000)^1000 ≈ 0.3677`。
- T/F：“OOB 约 37%” → ✅。

---

### 7️⃣ 非线性的特殊处理

**正确结论**：树模型通过**递归分裂**把特征空间切成 axis-aligned 区域，叶节点输出常数；多个 split 组合成分段常数边界，天然处理非线性和 feature interaction。

**相关知识点**：

- 每次 split：`x_j < threshold`；
- 叶节点：分类输出多数类，回归输出均值；
- 多个 split → 分段常数（piecewise constant）；
- 自动捕捉 interaction（例如 `x1` 和 `x2` 的组合规则）；
- Boosting 多棵树相加 → 逼近更复杂的非线性函数；
- 不需要显式构造 `x²`、`x1x2` 或核函数；不需要 feature scaling。

**局限**：

- axis-aligned 边界对某些平滑函数不够高效，需要很多棵树；
- 树多 → 模型复杂、可解释性下降。

**可能的考法**：

- 简答：“树模型如何处理非线性？” → 递归分裂 + 分段常数 + 多树叠加。
- T/F：“树模型需要先做非线性特征变换” → ❌。

---

### 8️⃣ EFB

**正确结论**：**EFB = Exclusive Feature Bundling**，LightGBM 的核心创新之一。

**相关知识点**：

- 互斥的稀疏特征（很少同时非零，如 one-hot）可以合并成一个 bundle；
- 用 **offset** 区分原特征；
- 例：`f1=8, f2=5, f3=3, f4=9`，offsets `0,10,20,30` → bundle 值 `8,15,23,39`；
- 好处：减少 feature 数 / 内存（最高约 80%），加速训练；
- 前提：特征**互斥或近似互斥**；有冲突时要处理。

**可能的考法**：

- T/F：“EFB bundles mutually exclusive sparse features” → ✅；
- MCQ：“LightGBM 的 EFB 目的？” → 降维/省内存/加速。

**陷阱**：说“EFB 对任何特征都无损” → ❌；需要互斥/近似互斥。

---

### 9️⃣ Random feature 定义

**正确结论**：Random Forest 的 “random feature” 指：**每次节点分裂时，从全部 p 个特征中随机选一个子集（`max_features`），只在这个子集里选最优 split。**

**相关知识点**：

- 分类常用 `√p`，回归常用 `p/3`（不是通用最优）；
- 目的：避免每棵树都优先用同一个强特征 → 降低树间 correlation ρ；
- 与 variance 公式配合：ρ 越小，bagging 降 variance 越有效；
- 不是 kernel 方法里的 “random Fourier features”。

**可能的考法**：

- 定义题：“What is random feature selection in RF?” → 每次 split 随机选 feature 子集。
- T/F：“RF 每次 split 使用全部特征” → ❌。

---

### 🔟 Pseudo-residual，squared error loss

**正确结论**：

```
r_i = - ∂L(y_i, F) / ∂F |_{F=F_{m-1}(x_i)}
```

| Loss | pseudo-residual |
|---|---|
| `L=(y-F)^2` | `r=2(y-F)` |
| `L=1/2(y-F)^2` | `r=y-F` |

例：`y=5, F=3`：

- `L=(y-F)^2` → `r=2*(5-3)=4`；
- `L=1/2(y-F)^2` → `r=2`。

**相关知识点**：

- GBDT 用回归树拟合 `r_i`；
- 一般 loss（logistic）→ `r=y/(1+e^{yF})`；
- 伪残差是“负梯度”，不是普通残差；平方损失下才恰好等于残差（差常数因子）。

**可能的考法**：

- 计算：给定 y、F、squared loss，求 pseudo-residual；
- T/F：“pseudo-residual always equals y-F” → ❌。

---

### 1️⃣1️⃣ γ 的作用

**正确结论**：看语境。

**XGBoost 的 γ**：

- 每增加一个叶子的复杂度惩罚；
- 分裂增益：

```
Gain = 1/2[G_L²/(H_L+λ) + G_R²/(H_R+λ) - G²/(H+λ)] - γ
```

- **Gain > 0** 才分裂；
- γ 越大 → 分裂门槛越高 → 树越简单、越不容易过拟合。

**GBDT 的 γ**：

- line search 得到的**步长**（step size），和 learning rate η 一起缩放新树；
- 不是叶子数惩罚。

**可能的考法**：

- 计算：给出 Gain 公式和 γ，判断是否分裂；
- T/F：“γ 越大，XGBoost 树越复杂” → ❌（越简单）。

**陷阱**：把 XGBoost 的 γ（叶子惩罚）和 GBDT 的 γ（步长）混。

---

### 1️⃣2️⃣ 最纯方法，Gini

**正确结论**：Gini impurity：

```
G = 1 - Σ_k p_k^2
```

- **纯节点**（只有一类）→ `G=0`（最纯）；
- 二分类 50/50 → `G=0.5`（最大）；
- 二分类可写 `G=2p(1-p)`；
- 多分类均匀分布 → `G=1-1/K`。

分裂时选 **Gini gain 最大**：

```
ΔG = G(parent) - (n_L/n) G(L) - (n_R/n) G(R)
```

**相关知识点**：

- Gini 和 entropy 都可用于分类树；
- **数值刻度不同，不能直接比**；
- CART 常用 Gini；ID3/C4.5 用 entropy / information gain；
- “最纯”= impurity 0，不是 Gini 值越大越好。

**可能的考法**：

- 计算：父节点与子节点的 Gini，求 gain；
- T/F：“Gini=0 表示节点最纯” → ✅。

---

## 3. 12 条 T/F 快问快答

| # | 陈述 | 答案 | 一句话 |
|---|---|---|---|
| 1 | GB 的每个新学习器拟合原始 y | ❌ | 拟合 residual / 负梯度 |
| 2 | GBDT 用回归树是因为树 high variance | ❌ | GBDT 用浅树；high variance 是 bagging 用深树的理由 |
| 3 | Bagging 降 bias、variance 不变 | ❌ | 降 variance，bias 近似不变 |
| 4 | Impurity-based importance 偏向 ID | ✅ | high-cardinality bias |
| 5 | LightGBM is immune to missing values | ❌ | 能处理，但不是“免疫” |
| 6 | OOB 比例约 37% | ✅ | 36.8% |
| 7 | 树模型需要显式非线性特征变换 | ❌ | axis-aligned splits 天然处理 |
| 8 | EFB 合并互斥稀疏特征 | ✅ | Exclusive Feature Bundling |
| 9 | RF 每次 split 使用全部特征 | ❌ | 随机选 feature 子集 |
| 10 | Squared loss 下 pseudo-residual = 2(y-F) | ✅ | 若 L=(y-F)^2 |
| 11 | XGBoost 的 γ 越大，树越复杂 | ❌ | γ 越大，树越简单 |
| 12 | Gini=0 表示节点最纯 | ✅ | 只有一类 |

---

## 4. 考前 5 分钟：一句话版

1. **GB**：新树拟合 residual / 负梯度，不是原始 y。
2. **树的高 variance**：bagging 用深树平均降 variance；GBDT 用浅树降 bias。
3. **Bagging**：降 variance，bias 近似不变（题目说反 → 错）。
4. **Impurity importance**：偏向 ID/高基数特征。
5. **LightGBM missing**：原生处理，但别写“免疫”。
6. **OOB**：36.8% ≈ 37%。
7. **非线性**：axis-aligned splits + 分段常数 + 多树叠加。
8. **EFB**：互斥稀疏特征 + offsets 合并。
9. **Random feature**：每次 split 随机选 feature 子集。
10. **Pseudo-residual**：squared loss → `2(y-F)`（或 `y-F`，看 1/2）。
11. **γ**：XGBoost 叶子惩罚；GBDT 步长。
12. **Gini**：纯节点 = 0；二分类最大 0.5；选 max gain。

---

## 5. 如果还有时间：AdaBoost 补充（往年也常混一题）

你给的 12 条没列 AdaBoost，但 L10 的核心，Quiz 3 很可能混一题。

### 5.1 算法

```
ε_m = Σ_i w_i * 1[ h_m(x_i) ≠ y_i ]
α_m = (1/2) ln( (1 - ε_m) / ε_m )
w_i ← w_i * exp(-α_m * y_i * h_m(x_i)) / Z_m
H(x) = sign( Σ_m α_m h_m(x) )
```

### 5.2 一轮例子

4 条样本，初始权重 0.25，弱分类器错 1 条：

```
ε = 0.25
α = 1/2 ln(0.75/0.25) = 1/2 ln 3 ≈ 0.5493
```

- 错分样本乘 `e^α = √3` → 权重变大；
- 正确样本乘 `e^-α = 1/√3` → 权重变小；
- 归一化后：错分 0.5，三条正确各 1/6。

### 5.3 关键结论

- AdaBoost 对**噪声/异常点敏感**（错分样本被反复加权）；
- ε=0.5 → α=0（不比随机好）；
- ε=0 → α→∞（完美分类器；实际要数值保护/提前停止）；
- 指数损失 `exp(-yF)` 下，最优分数是**半个 log-odds** `1/2 ln(p/(1-p))`。

---

## 6. 相关公式一页纸

```
Gini:        G = 1 - Σ_k p_k^2
Entropy:     H = -Σ_k p_k log2 p_k
Split gain:  ΔI = I(parent) - (n_L/n) I(L) - (n_R/n) I(R)

Bootstrap:   P(not selected) = (1 - 1/n)^n → e^(-1) ≈ 0.368
Bagging var: Var(avg) = σ² ( ρ + (1-ρ)/M )

AdaBoost:    ε = Σ w_i 1[wrong]
             α = 1/2 ln((1-ε)/ε)
             w_i ← w_i exp(-α y_i h_i) / Z

GBDT:        F_m = F_{m-1} + η γ_m h_m
             r = -∂L/∂F
             squared: r = 2(y-F)  [or y-F if L=1/2(...)²]
             global γ = Σ h_i(y_i-F_i) / Σ h_i²
             leaf γ = mean residual in leaf (squared loss)

XGBoost:     Ω = γT + (λ/2)Σw²
             w* = -G/(H+λ)
             Gain = 1/2[G_L²/(H_L+λ)+G_R²/(H_R+λ)-G²/(H+λ)] - γ

LightGBM:    leaf-wise; 4 leaves = 3 splits
             GOSS: keep top a%; sample b% of rest; scale (1-a)/b
             EFB: bundle mutually exclusive sparse features
```

---

> ⭐ 最后提醒：Quiz 3 是 **T/F + MCQ + 短计算**，不是证明题。上面 12 条 + AdaBoost + 公式表，覆盖了往年高频点；计算题一定要**先写公式，再代数字**，注意平方损失是否有 `1/2`、γ 是 XGBoost 还是 GBDT 语境。
