# EE6406 Quiz 1 复习与精讲

> 课程：EE6406 Analytic Methods for Pattern Recognition
> 材料来源：`6406/Quiz1/` 下 8 个文件
> 覆盖范围：教材 "Analytic Learning Methods for Pattern Recognition"（Toh Kar-Ann et al., Springer 2025）**第 2–4 章**课后习题 30 题，逐题精读两天冲刺版。
> 性质：这是 **Quiz 1（CA1）复习材料**，即教材课后题的逐题精读，覆盖 Week 2–4 内容，不是新周课件——不进 `Learning_note.md`，作为独立 quiz 复习文档。

---

## 〇、材料结构与使用方式

`6406/Quiz1/` 内 8 个文件分两类：

| 文件 | 内容 | 用途 |
|---|---|---|
| `05_逐题精读两天冲刺.pdf` | **核心**：第 2–4 章 30 题逐题精读（两天冲刺版），每题六段：①英文原题+重点等级 ②中文翻译 ③词汇+读音 ④知识点梳理 ⑤英文答案 ⑥中文答案+解题提示 | 主复习材料，本 .md 据此整理 |
| `EE6204_Quiz1_练习题含解析(1).pdf` | EE6204 Systems Analysis 的 Linear Programming 练习题（graphic/simplex/sensitivity），含答案 | **另课程（EE6204）的 LP 题**，与 6406 pattern recognition 无关，略过 |
| `978-981-96-2151-4.pdf` | 教材 "Analytic Learning Methods for Pattern Recognition" 全书 | 原书，查证用 |
| `PDF合并.pdf` | 教材 + 解答手册合并（4737 行） | 原题与答案的原始出处 |
| `Analytic Learning Methods_41-42.pdf` | 教材第 2 章练习节选 | 查证 |
| `Analytic Learning Methods_80-82.pdf` | 教材第 3 章线性参数模型节选 | 查证 |
| `Analytic Learning Methods_104-106.pdf` | 教材第 4 章评分函数节选 | 查证 |
| `Analytic Learning Methods_341-389.pdf` | 教材解答手册节选 | 查证 |

> 注意：`EE6204_Quiz1_练习题含解析(1).pdf` 是 **EE6204 Systems Analysis**（Linear Programming）的练习题，与 EE6406 不属同一课程，本复习文档不涵盖其 LP 内容。

---

## 一、重点等级与两天冲刺计划

### 三个重点等级

| 等级 | 标记 | 两天内的任务 |
|---|---|---|
| ★★★ | 必会 | 第一轮学透，第二轮遮住答案独立做 |
| ★★ | 补强 | 先达到题头最低学习目标，再补详细步骤 |
| ★ | 后置 | 先认术语和构造思路，时间不足最后再看（如 3.10 代码） |

> 等级是**复习建议，不是老师确认考题**。

### 两天复习顺序（每天约 5–6 小时）

| 时间 | 内容 | 完成标准 |
|---|---|---|
| 第1天 35min | 读 3.1 的矩阵/det/代入法；读 4.2、4.3 | 能区分 loss/cost/error，能算二阶 det |
| 第1天 100min | 第2章 2.1–2.10，先三星 | 能认数据类型、距离、缩放与中位数 |
| 第1天 100min | 3.1–3.4、3.6 | 能判系统类型和次数，能解释 x₁x₂ 作用 |
| 第1天 60min | 4.1–4.4、4.6、4.7 | 能读概念题，辨别验证误差与不平衡 |
| 第1天 30min | 遮答案重做当天不会的三星题 | 把错因记为：词不认识/条件漏看/计算错 |
| 第2天 100min | 4.5、4.8、4.9、4.10 | 独立数图、算五种指标、写 Gini 和 MCE |
| 第2天 60min | 3.5、3.7–3.9；3.10 只看最低目标 | 会展开一行，知道最小范数与秩条件 |
| 第2天 50min | 做模拟卷 A | 计时完成，不中途查答案 |
| 第2天 30min | 按错题回查本册对应题 | 必须能说出为什么错 |
| 第2天 50min | 做模拟卷 B | 再次练英文读题和计算 |
| 第2天 25min | 背保底清单 | 睡前只巩固，不扩展新章节 |

### 保底清单

- **最优先**：3.1、3.2、3.3、4.2、4.3、4.9
- **随后补**：2.2–2.6、2.8–2.10、3.4、3.6、4.5–4.8、4.10

### 临考检查词（英文读题易错点）

| 英文措辞 | 含义 | 陷阱 |
|---|---|---|
| `incorrect` | 选**错误**的 | 容易看成"选正确" |
| `select one or more` | 多选 | 不要只选一个 |
| `respectively` | 分别（按前后顺序对应） | 对应错位 |
| `thus` | 因此（可能是**错误推论**） | 不能盲信 |
| `at least` | 至少 | 边界条件 |
| `count` | 数量（不除总数） | 与 rate 混淆 |
| `rate` | 率（需除总数） | 与 count 混淆 |

> **不要只背选项字母**：原题会改数字、交换选项或换矩阵方向，记住公式和判断条件才有用。

---

## 二、第 2 章 — Data, Distance & Scaling（数据、距离与缩放）

| 题 | 主题 | 重点 | 答案要点 |
|---|---|---|---|
| 2.1 | Data vs Information | ★★ | **False**。Data 是原始记录；Information 是经处理/解释后有意义的数据。 |
| 2.2 | One-hot encoding | ★★★ | **True**。任意数字赋值会引入 artificial order/distance/unequal influence；one-hot 避免此问题。 |
| 2.3 | Ordinal data 特征 | ★★★ | **(a)(b)(c)(d)** 全选。Ordinal 有序、有 median、等级间隔未知、衡量非数值特征、建立 relative rank。 |
| 2.4 | Interval vs Ratio | ★★★ | (a) ratio (b) ratio (c) interval (d) ratio (e) ratio (f) ratio (g) ratio (h) ratio。Ratio 有真零点；interval 无真零点（如温度/智商）。 |
| 2.5 | Metric 四性质 | ★★★ | **(c) incorrect**。相同向量距离应为 0 而非非零。(a)(b)(d) 是 valid metric property。 |
| 2.6 | Hamming distance | ★★★ | **(d) Hamming**。统计等长向量对应位置**不同**的个数。 |
| 2.7 | Missing value | ★★ | 补强：认术语（imputation 等）。 |
| 2.8 | Standardization 选择 | ★★★ | **True**。z-score 用 mean+std，min-max 用 boundary values。 |
| 2.9 | Feature scale | ★★★ | **(b)**。大数值特征会 overshadow 小数值特征，需 min-max 或 z-score。 |
| 2.10 | Median | ★★★ | **Median = $5000**。9 个收入排序后第 5 个，robust to outlier（对 $800000 离群值稳健）。 |

### 2.1 知识点
- **Data**：recorded facts or values（原始记录）。
- **Information**：data processed or interpreted to be meaningful（处理后有意义的数据）。
- 记忆句：data 是原料，information 是从原料中读出的意义。

### 2.2 知识点
- Nominal categories 无自然数值顺序；数字 1/2/3 会让算法把"芒果3"看成比"橙子1"大，凭空引入 order/distance。
- One-hot encoding 为每类设独立指示位置：橙子[1,0,0]、苹果[0,1,0]、芒果[0,0,1]。
- `preferred over A` = "比 A 更推荐"，不是"更喜欢 A"。

### 2.3 知识点
- Ordinal data 能排序（establish order），可取 median。
- **能排顺序 ≠ 相邻差距相等**：等级间隔数值未知（value of interval is unknown）。
- 衡量 satisfaction/happiness 等非数值特征。

### 2.5 知识点 — Metric 四性质
- (a) 非负性：距离 ≥ 0 ✓
- (b) 对称性：d(x,y)=d(y,x) ✓
- (c) **相同向量距离应为 0**（题说"非零"，故 incorrect）
- (d) 三角不等式 ✓
- 一句话记忆：相同=距离0；不同≠距离0。

### 2.6 知识点 — Hamming distance
- 统计两个等长向量对应位置**不同**的个数。
- 例：[1,0,1,1] 与 [0,0,1,0]，第1、4位不同 → 距离 2。
- 可用于等长离散序列，不限于 binary。
- Minkowski 是 Lp 距离：p=1 是 Manhattan，p=2 是 Euclidean。

### 2.8 知识点 — 缩放公式
- **min-max normalization**：$\frac{x - \min}{\max - \min}$
- **z-score standardization**：$\frac{x - \mu}{\sigma}$
- z-score 用 mean+std；min-max 需要 boundary values。

### 2.9 知识点
- 大数值特征会 overshadow 小数值特征 → 缩放解决 scale 差异。
- 注意：response −13 不是自动 invalid。

### 2.10 知识点 — Median
- 排序后取中间值；对 outlier 稳健（robust to outlier）。
- 极端收入 $800000 会拉偏 mean，但 median 不受影响。

---

## 三、第 3 章 — Linear Parametric Model（线性参数模型）

| 题 | 主题 | 重点 | 答案要点 |
|---|---|---|---|
| 3.1 | 方阵与行列式 | ★★★ | (a) even-determined (b) 可逆，det=1 (c) w=[−1,1]ᵀ |
| 3.2 | 超定但有精确解 | ★★★ | **False**。Over-determined but **consistent**，精确解 w=[0,0.5]ᵀ。rank(X)=rank([X\|y])=2。 |
| 3.3 | 欠定与最小范数 | ★★★ | **(d)(e)**。Consistent under-determined，无穷多精确解（minimum-norm 解）。 |
| 3.4 | 多项式次数 | ★★★ | **(a)(c)(d)**。含二阶项；(b) 5 个变量但全一阶，下标≠指数。 |
| 3.5 | 三次回归 | ★★ | 补强。 |
| 3.6 | 交互特征 x₁x₂ | ★★★ | 含 x₁x₂ 交互项。 |
| 3.7 | 完整三维三阶 | ★★ | 最小范数解唯一。 |
| 3.8 | 简化多项式 | ★★ | 修正重复 x₃。 |
| 3.9 | 固定隐藏层与秩 | ★★ | 伪逆结果经数值复核。 |
| 3.10 | 倒数 Sigmoid 代码 | ★ | 后置：先认术语和构造思路，时间不足最后看。 |

### 3.1 知识点 — 系统类型与行列式（⚠️ 往次例题直接考过）

给定 $Xw=y$，$X=\begin{bmatrix}1&1\\5&6\end{bmatrix}$，$y=\begin{bmatrix}0\\1\end{bmatrix}$。

- **(a) 系统类型**：2 方程 2 未知数 → **even-determined**。
- **(b) 可逆性**：二阶行列式 $\det(X)=ad-bc=1\times6 - 1\times5 = 1 \neq 0$ → 可逆。$X^{-1}=\begin{bmatrix}6&-1\\-5&1\end{bmatrix}$。
- **(c) 求解**：$w = X^{-1}y = \begin{bmatrix}-1\\1\end{bmatrix}$。
- 验证：$-1+1=0$ ✓；$5(-1)+6(1)=1$ ✓。

> ⚠️ 往次例题若只问 determinant，填 **1**，不用继续求 w。

### 3.2 知识点 — Over-determined 但 consistent
- Over-determined（方程 > 未知数）≠ 必然无解。
- **精确解存在的判据是 rank**：$\text{rank}(X)=\text{rank}([X|y])$ → consistent，有精确解。
- 本题 $w=[0,0.5]^T$ 精确解，不能只看形状判"无解"。

### 3.3 知识点 — Under-determined
- Under-determined（方程 < 未知数）→ 若 consistent 则有**无穷多**精确解。
- 选 **minimum-norm solution**（最小范数解）作为唯一代表。

### 3.4 知识点 — 多项式次数判断（⚠️ 高频考点）
- 单项式总次数 = 各变量**指数之和**。
- **下标是"第几个变量"，不是幂**：$x_5$ 是第 5 个变量（一阶），$x_1^2$ 才是平方（二阶）。
- $x_1x_2 = x_1^1 x_2^1$，总次数 $1+1=2$（二阶）。
- (d) $x_1(x_1-x_2)=x_1^2 - x_1x_2$，展开后可见二阶项。
- (b) 有 5 个变量但每项一阶 → 一阶模型。
- 口诀：**次数看右上角；多变量相乘，指数加起来**。

### 3.6 知识点 — 交互特征
- $x_1x_2$ 是 interaction term（交互项），总次数 2，引入变量间的协同效应。

---

## 四、第 4 章 — Score Functions / Loss / Metrics（评分函数与指标）

| 题 | 主题 | 重点 | 答案要点 |
|---|---|---|---|
| 4.1 | 回归 vs 分类损失 | ★★ | Regression loss 罚数值偏差；classification loss 评离散类错误或 surrogate penalty。 |
| 4.2 | Error vs Loss | ★★★ | Error 测偏差本身；Loss 把偏差量化为惩罚。 |
| 4.3 | Loss vs Cost | ★★★ | **Loss 单样本；Cost 总体汇总**（可能含正则化）。 |
| 4.4 | 常见损失 | ★★ | Regression: squared/absolute error (MSE/MAE)；Classification: 0-1, cross-entropy, hinge, logistic, exponential loss。 |
| 4.5 | 从图读混淆矩阵 | ★★★ | 数图：行=预测，列=真实；[[6,1],[1,3]]，11 点 9 对。 |
| 4.6 | 按验证误差选参 | ★★★ | 选 **θ=0.5**（Va 最小 0.18 并列，用 Tr 打破并列）。 |
| 4.7 | 类别不平衡选指标 | ★★★ | **(b)(c)(d)**：cost-sensitive accuracy、precision/recall、Type-I/II error。普通 accuracy 会误导。 |
| 4.8 | Gini 与 AUC | ★★★ | **Gini = 2AUC − 1**。 |
| 4.9 | 混淆矩阵计算 | ★★★ | TPR=0.99, TNR=0.95, Acc=0.9786, Acc(s=1)=0.97, Precision=0.9802 |
| 4.10 | 用 margin 计 MCE | ★★★ | MCE = Σ𝟙[yᵢg(xᵢ)<0]；数负间隔。 |

### 4.2 知识点 — Error vs Loss（⚠️ 往次例题直接考过）
- **Error function**：测量预测与真实观测的**偏差**（deviation）。
- **Loss function**：把这种偏差量化为**惩罚**（penalty/negative consequence）。
- 例：真实 $y=5$，预测 $\hat{y}=3$，若 $e=\hat{y}-y$，则 $e=-2$（error）；$L(e)=e^2=4$（squared-error loss）。
- 同一个 error 可对应不同 loss。
- ⚠️ "negative consequences" 不要机械理解为"损失值必须是负数"——平方损失当然非负。

### 4.3 知识点 — Loss vs Cost（⚠️ 往次例题直接考过）
- **Loss function**：**单个样本**的惩罚。
- **Cost function**：汇总多个样本的 loss 形成优化目标，可含正则化：
  $$J(w) = \sum_i L_i(w) + \lambda R(w)$$
- 最短记忆：**Loss is per sample; cost is aggregate.**
- ⚠️ 往次例题把 loss 和 cost 对调过，正确记法：**loss 单样本，cost 汇总**。

### 4.4 知识点 — 常见损失
- **Regression**：squared error、absolute error（汇总为 MSE、MAE）。
- **Classification**：0-1 loss、cross-entropy、hinge loss（SVM）、logistic loss（LogitBoost）、exponential loss（AdaBoost）。

### 4.5 知识点 — 从图读混淆矩阵
- 行 = 预测类别，列 = 真实类别；对角线 = 正确分类。
- 本题：预测 Class1 区域（左）6 蓝星+1 红三角；预测 Class2 区域（右）1 蓝星+3 红三角。
- 矩阵 $\begin{bmatrix}6&1\\1&3\end{bmatrix}$，共 11 点，9 对。
- 选 Class1 为正类：TP=6, FP=1, FN=1, TN=3。
- 检查：四格相加 = 总样本数。

### 4.6 知识点 — 按验证误差选参
- 训练数据学参数；**验证数据选设置**。
- 步骤：①看 Va 最小 → 0.18 对应 θ=0.3 和 0.5；②并列时用 Tr 打破 → θ=0.5（Tr=0.16 < 0.21）。
- ⚠️ 不能选 θ=0.1（Tr 最低 0.08，但 Va=0.23 高）→ 过拟合。
- ⚠️ "仅凭 Tr>Va 证明 underfitting"不普遍成立，本题为答案册口径。

### 4.7 知识点 — 类别不平衡（9900 vs 100）
- 全猜多数类：accuracy=9900/10000=99%，但少数类**一个都没找出**（recall=0）。
- 故普通 accuracy 会误导 → 选 **(b) cost-sensitive accuracy、(c) precision & recall、(d) Type-I & Type-II errors**。
- 一句核心：全猜多数类也能 99%，但少数类召回为 0。

### 4.8 知识点 — Gini 与 AUC 关系（⚠️ 必背公式）
- ROC 图：纵轴 TPR，横轴 FPR，都从 0 到 1，正方形面积 1，对角线下三角形面积 0.5。
- $\text{Gini} = \frac{A}{A+B} = \frac{A}{0.5} = 2A$；$\text{AUC} = A + 0.5$。
- 代入：
  $$\boxed{\text{Gini} = 2\text{AUC} - 1 \quad\Longleftrightarrow\quad \text{AUC} = \frac{\text{Gini}+1}{2}}$$
- 例：AUC=0.8 → Gini=0.6；AUC=0.5 → Gini=0；AUC=1 → Gini=1。
- ⚠️ 这是 **ROC 相关的 Gini**，不是决策树的 Gini impurity，不要混用。

### 4.9 知识点 — 混淆矩阵五指标计算（⚠️ 本章计算核心）

混淆矩阵（行=预测，列=真实）：

| | 真实 +1 | 真实 −1 |
|---|---|---|
| 预测 +1 | TP=990 | FP=20 |
| 预测 −1 | FN=10 | TN=380 |

- $n_+ = TP+FN = 1000$，$n_- = TN+FP = 400$，总 $N=1400$，$s=n_-/n_+ = 0.4$。
- **(a) TPR** = $\frac{TP}{n_+} = \frac{990}{1000} = 0.99$（= recall = sensitivity）
- **(b) TNR** = $\frac{TN}{n_-} = \frac{380}{400} = 0.95$（= specificity）
- **(c) Accuracy** (s=0.4) = $\frac{TP+TN}{n_+ + n_-} = \frac{1370}{1400} \approx 0.9786$
- **(d) Accuracy at s=1** = $\frac{TPR+TNR}{2} = \frac{0.99+0.95}{2} = 0.97$（balanced accuracy）
- **(e) Precision** = $\frac{TP}{TP+FP} = \frac{990}{1010} \approx 0.9802$

本课公式：
$$\text{Acc}(s) = \frac{TPR + s\cdot TNR}{1+s}, \qquad \text{Prec}(s) = \frac{TPR}{TPR + s\cdot FPR}$$
其中 $FPR = FP/n_-$。s=0.4 还原普通 accuracy/precision；s=1 为 balanced accuracy。

> ⚠️ 易错：不要把 TPR 与 TNR 的分母对调；Precision 分母是 1010（TP+FP），不是 1000。

### 4.10 知识点 — 用 margin 计 MCE
- 标签 $\{+1,-1\}$，margin $\mu_i = y_i g(x_i)$。
- **margin > 0** → 同号 → 分类正确；**margin < 0** → 异号 → 错分。
- $\text{MCE} = \sum_i \mathbf{1}[y_i g(x_i) < 0]$（数负间隔的个数）。
- 等价：$-\sum_i \min\{0, \text{sgn}(\mu_i)\}$ 或 $\sum_i \frac{1-\text{sgn}(\mu_i)}{2}$（非零 margin 时）。
- ⚠️ MCE 是 **count（数量）**，不除总数；错误率 = MCE/m 才除。
- 例：margin $[2,-0.3,1,-4]$ 有 2 个负数 → MCE=2；错误率=2/4=0.5。
- ⚠️ $\mu=0$ 是边界，按题目规定处理，不要套 AUC 计半对规则。

---

## 五、核心公式速查表（最后一页汇总）

| 主题 | 公式 |
|---|---|
| 二阶行列式 | $\det\begin{bmatrix}a&b\\c&d\end{bmatrix} = ad-bc$；非零则可逆 |
| 系统类型 | $m$=方程数，$K$=未知数；$m=K$ 方阵，$m>K$ 超定，$m<K$ 欠定；精确解看 rank(X)=rank([X\|y]) |
| 多项式次数 | 单项式次数=指数和；完整 $d$ 维最高 $r$ 阶含偏置项数 $C(d+r,r)$ |
| min-max | $\frac{x-\min}{\max-\min}$ |
| z-score | $\frac{x-\mu}{\sigma}$ |
| loss/cost/error | loss 单样本；cost 汇总；error 偏差本身 |
| TPR | $\frac{TP}{TP+FN}$ |
| TNR | $\frac{TN}{TN+FP}$ |
| Precision | $\frac{TP}{TP+FP}$ |
| Accuracy | $\frac{TP+TN}{N}$ |
| Balanced accuracy | $\frac{TPR+TNR}{2}$ |
| FPR | $1 - TNR$ |
| FNR | $1 - TPR$ |
| TER | $FPR + FNR$ |
| HTER | $\frac{TER}{2}$ |
| Gini | $2\text{AUC} - 1$ |
| Margin | $y_i g(x_i)$ |
| MCE | $\sum \mathbf{1}[y_i g(x_i) < 0]$；错误率再除 $m$ |

---

## 六、材料处理说明

本册（`05_逐题精读两天冲刺.pdf`）对原题与答案的已知问题处理：
- 2.4 智力测验分数：保留答案册 ratio 与通常 IQ 的 interval 解释，不掩盖歧义。
- 2.6 Hamming：保留预期 Hamming 并说明原题措辞宽泛（Euclidean/Manhattan 对 binary 向量数学上也可用）。
- 3.7/3.8：明确唯一的是 minimum-norm 解；3.8 修正重复 $x_3$。
- 3.9：给出经数值复核的 pseudoinverse 结果。
- 4.4：并列说明课件前后损失定义差异。
- 4.6：保留答案册选 0.5 但限定并列处理口径。
- 4.10：明确零间隔需题设约定。

原题与答案主要来源：`PDF合并.pdf` 第 4–11 页和第 29–41 页。相关知识来自 `EE6406-Lecture2-LZP-v1.pdf`、`EE6406-Lecture2Suppl-LZP-v1.pdf`、`Lecture3-KA.pdf`、`EE6406-Lecture4-TKA-v2.pdf`。

---

## 七、应试提醒

1. **读题先看是否多选**：`select all` / `which of the following`（看是否给 `one or more`）。
2. **`incorrect` 选错的**，别看成选对的。
3. **下标 ≠ 指数**：$x_5$ 是第 5 个变量（一阶），$x_1^2$ 才是二阶。
4. **loss/cost/error 三者区分**：error 偏差、loss 单样本惩罚、cost 总体汇总。
5. **混淆矩阵行列**：行=预测，列=真实；TPR 分母是真实正类数 $n_+$，Precision 分母是预测正类数 $TP+FP$。
6. **Gini = 2AUC − 1** 是 ROC 的 Gini，不是 Gini impurity。
7. **MCE 是 count 不除总数**，错误率才除。
8. **选参看 Va 不是 Tr**：Tr 最低可能是过拟合。
9. **不要只背选项字母**：改数字、换矩阵方向后只有公式和判断条件可靠。
10. **2 天至少闭卷完整算两遍 4.9**：换一组数字也要会用同样分母。
