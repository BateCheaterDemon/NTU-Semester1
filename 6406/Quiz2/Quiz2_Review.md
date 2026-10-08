# EE6406 Quiz 2（CA2）复习与精讲

> 课程：EE6406 Analytic and Ensemble Machine Learning（Part 1 主讲：Toh Kar-Ann）
> 材料来源：`6406/Quiz2/` 下 4 份 Cornell Notes PDF + `week5–week7/` 官方课件
> 覆盖范围：**Lecture 5–7**（analytic regression → advanced analytic classification → penalized learning）
> 性质：这是 **Quiz 2（CA2）复习材料**，覆盖 Week 5–7 内容——不进 `Learning_note.md`，作为独立 quiz 复习文档，与 `Quiz1/Quiz1_Review.md` 同一套规范。

---

## 〇、材料结构与使用方式

`6406/Quiz2/` 内 4 份 PDF：

| 文件 | 内容 | 用途 |
|---|---|---|
| `EE6406_Week1-4_to_Week5-7_Bridge_Review.pdf` | **前置**：Week 1–4 主线回顾，只保留 L5–L7 会直接调用的概念、公式、shape 与判断方法 | **开始前先读这 16 页**（约 35–45 分钟） |
| `EE6406_L5_Analytic_Regression_Cornell_Notes.pdf` | **核心 1**：超定与欠定解析回归（19 页） | 主复习材料 |
| `EE6406_L6_Advanced_Analytic_Classification_Cornell_Notes.pdf` | **核心 2**：TER / AUC / 统一框架（18 页） | 主复习材料 |
| `EE6406_L7_Penalized_Learning_Cornell_Notes.pdf` | **核心 3**：惩罚学习、系数收缩、bridge（17 页） | 主复习材料 |

对应官方课件（本册页码索引以此为准）：

| 讲次 | 课件文件 | 页数 | 关键页码 |
|---|---|---|---|
| L5 | `week5/EE6406-Lecture5-TKA-v1.pdf` | 59 | p.5–20 超定 · p.21–28 欠定 · p.29–40 ridge · p.41–53 kernel · p.54–57 分类决策 |
| L6 | `week6/EE6406-Lecture6-TKA-v1.pdf` | 59 | p.5–25 TER · p.26–36 AUC · p.37–48 统一框架 · p.49–55 贝叶斯联系 |
| L7 | `week7/EE6406-Lecture7-TKA-v1.pdf` | 68 | p.4–20 动机 · p.21–27 三种 penalty · p.28–34 ridge · p.35–44 bridge · p.45–65 三个实验 |

> 注：Cornell Notes 内文引用的是 `materials/EE6406-Lecture5-TKA-v2.pdf`，与仓库内 `week5/` 的 v1 为同一份课件，页码已逐页核对一致。课件每页右下角的 `NN / 58` 是**幻灯片序号**，PDF 页码 = 幻灯序号 + 1。

---

## 一、三讲主线总图（先看这张）

三讲不是三个独立知识点，而是层层递进地回答**同一个问题**：

> **能不能不做迭代，直接一步把参数解出来？**

```
L5  用 SSE 直接解回归参数         → 产出：primal / dual 两套闭式解
      ↓  但"数错了几个"这个分类指标不可导啊
L6  把 TER / AUC 改写成能解的二次式 → 产出：TER / AUC 两套闭式解（与 L5 同构）
      ↓  但一味拟合训练集会过拟合
L7  在 objective 里加惩罚项         → 产出：ridge / lasso / bridge
```

**贯穿三讲的因果链**（背这条比背公式有用）：

```
选 feature map p(x) → 拼出 P → 看 P 的 shape → 决定在哪个空间求逆
   → 需要就加 λI → 求逆得 w 或 α → 预测 score → threshold / argmax 得类别
```

做题顺序（三讲通用）：

> **写 shape → 判断 task → 选择 objective → 判断 primal/dual → 检查 inverse/rank → 求参数 → 用 train-consistent representation 预测 → 再 threshold、argmax 或算 metric**

> ⚠️ **第一原则**（老师反复强调）：写公式前先把 `P` 的 rows 与 columns 写出来。只背公式而不检查 inverse 的 shape，极易把 primal 与 dual 用反。

---

## 二、符号与 shape 速查

| 符号 | Shape | 含义 |
|---|---|---|
| `X` | $m \times d$ | $m$ 个原始输入样本，每个 $d$ 个 features |
| $p(x_i)$ | $(D+1) \times 1$ | 含 intercept 的 transformed feature column |
| `P` | $m \times (D+1)$ | **第 $i$ 行为 $p^T(x_i)$**；行 = 样本，列 = 特征 |
| `y` | $m \times 1$ | 单输出 target vector |
| `Y` | $m \times C$ | $C$ 类 one-hot / indicator targets |
| `w` | $(D+1) \times 1$ | primal parameter vector |
| `W` | $(D+1) \times C$ | 多输出参数矩阵 |
| `α` | $m \times 1$ | dual coefficients |
| `K = PPᵀ` | $m \times m$ | training Gram / kernel matrix |
| `Kt` | $n \times m$ | $n$ 个 test samples 对 $m$ 个 training samples 的 kernels |
| `PᵀP` | $(D+1) \times (D+1)$ | **feature space**，在参数空间求逆 |
| `PPᵀ` | $m \times m$ | **sample space**，在样本空间求逆 |

### 三个容易混淆的对象（用具体数字固定住）

设 $m = 3$ 个样本、每个样本 $D+1 = 2$ 个特征、$C = 2$ 类：

$$
P = \begin{bmatrix} 1 & 0.2 \\ 1 & 1.1 \\ 1 & -0.4 \end{bmatrix},
\qquad
Y = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 0 \end{bmatrix}
$$

- `P` 的第 $i$ 行 = 第 $i$ 个样本的 transformed features；
- `Y` 的第 $i$ 行 = **同一个样本**的 target；
- `W` 的第 $k$ 列负责产生第 $k$ 类 score；
- `PW` 的第 $i$ 行给出第 $i$ 个样本对所有类别的 scores。

> 样本可按任意顺序排列（课件为画图方便常按类别分块堆叠，**这不是算法要求**）。真正不能改变的是：**`P` 与 `Y` 的相同行必须指向同一个样本**（row correspondence）。

---

## 三、重点等级与复习计划

### 三个重点等级

| 等级 | 标记 | 含义 |
|---|---|---|
| ★★★ | 必会 | 第一轮学透，第二轮遮住答案独立做 |
| ★★ | 补强 | 先达到最低学习目标，再补细节 |
| ★ | 后置 | 先认术语和构造思路，时间不足最后再看 |

> 等级是**复习建议，不是老师确认考题**。

### 三轮复习顺序

| 轮次 | 时间 | 做什么 | 完成标准 |
|---|---|---|---|
| **第 0 轮** | 40 min | 读 `Bridge_Review.pdf`，只看 §2–§4 的公式表与 shape | 能说出 `PᵀP` / `PPᵀ` 各多大、什么时候用哪个 |
| **第 1 轮** | 40 min | 只读本册 §一、§二，以及每讲最后的「考试点」 | 能口述三讲的关系和各自产出 |
| **第 2 轮** | 2 h | 逐讲精读，**每读到一个公式先自己写出它的 shape**，再看推导 | 能不看笔记写出 L5/L6/L7 的核心闭式解 |
| **第 3 轮** | 1 h | 遮住答案做 §八 的手算演练 + §十 的自测清单 | 错题能说出"为什么错" |

### 保底清单（时间不够时只看这些）

- **最优先**：L5 的 primal/dual 选择逻辑、L6 的 shifted one-arm quadratic、L7 的 L1 vs L2
- **随后补**：TER/AUC 两个闭式解、ridge primal/dual、coefficient profile 解读
- **可后置**：bridge 长推导、TAUC 参数表、贝叶斯联系

### CA2 考试定位

| 项目 | 内容 |
|---|---|
| **范围** | Lecture 5–7（Week 5–7），recess 前全部内容 |
| **占比** | **15%**（CA1 = 10%，CA2 = 15%，CA3 = 15%，Final = 60%） |
| **时间** | **Week 8**（recess week 后） |
| **形式** | online quiz，**in-class**，lockdown browser，**closed-book** |
| **题型** | **concept 为主 + basic calculation**，课件 examples 与简单练习足够，不做书末复杂计算 |

> 老师原话："concept holds more mass than calculations, similar to CA one."

---

## 四、Lecture 5 — Over-/Under-determined Analytic Regression

> 📄 `Quiz2/EE6406_L5_Analytic_Regression_Cornell_Notes.pdf`
> 📄 课件 `week5/EE6406-Lecture5-TKA-v1.pdf`

**本讲主线**：选择 feature map $p(x)$ → 形成 `P` 与目标 → 由 `P` 的 shape 选择 primal 或 dual 空间 → 用 SSE 或 ridge 求闭式解 → 用 `Pt` 或 kernel matrix 预测 → threshold / argmax 得到类别。

### 4.1 模型长什么样

$$
g(x_i, w) = w^T p(x_i), \qquad p(x_i) = [1, p_1(x_i), \ldots, p_D(x_i)]^T
$$

**关键理解**：$p(x)$ 可以是线性的，也可以是非线性的（$x^2$、$x_1x_2$、$\sin x$ 都行），**但模型对 $w$ 必须保持线性**——这才谈得上闭式解。这就是 "linear-in-parameter" 的含义。

### 4.2 SSE：什么叫"学得好"

$$
J_{SSE}(w) = \sum_{i=1}^{m} \big(y_i - g(x_i, w)\big)^2 = \|y - Pw\|_2^2
$$

翻译成普通话：

1. `Pw` 一次算出全部 training predictions；
2. `y - Pw` 的第 $i$ 个元素是第 $i$ 个样本的 residual；
3. $\|y - Pw\|_2^2$ 把所有 residual 平方后相加；
4. 学习就是寻找使这笔总误差最小的 $w$。

### 4.3 为什么先检查 shape

真正要求逆的矩阵取决于把问题放在哪个空间：

| 矩阵 | Shape | 空间 |
|---|---|---|
| $P^T P$ | $(D+1) \times (D+1)$ | feature space（parameter space） |
| $P P^T$ | $m \times m$ | sample space |

**应优先在较小空间求解**，同时必须满足相应的 rank / nonsingularity 条件。

### 4.4 超定系统（$m > D+1$）：样本比参数多

对 SSE 求 gradient：

$$
\nabla_w J_{SSE}(w) = -2P^T (y - Pw)
$$

令 gradient 为零，得到 **normal equation**：

$$
P^T P w = P^T y
\quad\Longrightarrow\quad
\boxed{\ \hat{w} = (P^T P)^{-1} P^T y\ } \qquad (m > D+1)
$$

前提：$P^T P$ nonsingular（等价于 $P$ 的列线性无关）。

> ⚠️ 课件写 over-determined 时**同时要求 observations independent 且 $P^T P$ nonsingular**——后一个条件才真正保证 inverse 存在。

**手算演练：用 3 个点拟合一条直线**

$$
P = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{bmatrix},
\qquad y = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}
$$

$P$ 有 3 行 2 列，表示用 3 个 observations 估计截距与斜率两个参数。于是：

$$
P^T P = \begin{bmatrix} 3 & 3 \\ 3 & 5 \end{bmatrix},
\qquad P^T y = \begin{bmatrix} 5 \\ 6 \end{bmatrix}
$$

$$
(P^T P)^{-1} = \frac{1}{15-9}\begin{bmatrix} 5 & -3 \\ -3 & 3 \end{bmatrix} = \frac{1}{6}\begin{bmatrix} 5 & -3 \\ -3 & 3 \end{bmatrix}
$$

$$
\hat{w} = \frac{1}{6}\begin{bmatrix} 5 & -3 \\ -3 & 3 \end{bmatrix}\begin{bmatrix} 5 \\ 6 \end{bmatrix}
= \frac{1}{6}\begin{bmatrix} 7 \\ 3 \end{bmatrix}
= \begin{bmatrix} 7/6 \\ 1/2 \end{bmatrix}
$$

因此拟合直线为 $\hat{y} = 7/6 + (1/2)x$。**三个预测值并不逐点等于 $y$**——3 条约束一般无法由 2 个参数全部满足；least squares 选择的只是总体 squared residual 最小的折中解。

### 4.5 Training 与 test prediction

$$
\hat{g}(X) = P\hat{w}, \qquad \hat{g}(X_t) = P_t \hat{w}
$$

$P_t \in \mathbb{R}^{n \times (D+1)}$ **必须使用与 training 完全相同的 feature map 和列顺序**。

### 4.6 多类别扩展

把每一类的 indicator target 作为 `Y` 的一列：

$$
J_{SSE}(W) = \mathrm{trace}\big[(Y - PW)^T (Y - PW)\big]
$$

每一列共享同一个 `P`，因此可一次写成：

$$
\boxed{\ \hat{W} = (P^T P)^{-1} P^T Y\ }
$$

> **这不是新的求解原理**，只是把 $C$ 个独立的 least-squares problems 横向堆叠。

课件把 `Y` 画成 category blocks（同类样本连续堆叠）只是为了作图方便。样本顺序为 class 2、1、3、2 时完全可以写成：

$$
Y = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}
$$

只要 `P` 的四行也按同一顺序排列，`PW` 与 `Y` 就能逐行比较。**需要的是 row correspondence，不是按类别排序。**

### 4.7 欠定系统（$m < D+1$）：参数比样本多

#### 为什么 primal inverse 直接失败

若 $m < D+1$，则 `P` 最多只有 $m$ 个 independent rows，故 $P^T P$ 的 rank 不超过 $m$，**通常 singular**。此时未知参数多于独立约束，一致系统一般有**无穷多 exact solutions**。

#### 解的结构：row space + null space

任意一个解都可以写成：

$$
w = w_{row} + w_{null}
$$

其中 $w_{null}$ 位于 `P` 的 null space，所以 $P w_{null} = 0$——**它不改变 training output，却会增大参数 norm**。

因此 minimum-norm solution 令 $w_{null} = 0$，只保留 `P` 的 row space 中的部分：

$$
w = P^T \alpha, \qquad \alpha \in \mathbb{R}^m
$$

这里的 $\alpha$ 给每个 training row 一个组合权重；$P^T\alpha$ 把这 $m$ 个 row directions 组合成 feature-space 参数 $w$。代入 SSE 后转到 sample space 调整 $\alpha$：

$$
\min_\alpha \|y - PP^T\alpha\|_2^2
$$

若 $PP^T$ full rank：

$$
\hat{\alpha} = (PP^T)^{-1} y
$$

所以：

$$
\boxed{\ \hat{w} = P^T (PP^T)^{-1} y\ } \qquad (m < D+1)
$$

#### 为什么叫 least-norm solution（Lagrangian 完整推导）

同一个结果也可由 constrained problem 得到：

$$
\min_w \|w\|_2^2 \quad \text{subject to} \quad y - Pw = 0
$$

它不是说原系统只有一个解，而是在**所有 exact solutions 中选 Euclidean norm 最小的一个**。

**Step 1 — 把约束放进 Lagrangian**（为每条约束引入 multiplier $\alpha$）：

$$
L(w, \alpha) = \|w\|_2^2 + (y - Pw)^T \alpha
$$

> $\alpha$ **不是新的模型参数**，而是帮助强制执行 $y - Pw = 0$ 的 Lagrange multiplier vector。

**Step 2 — 对 $w$ 求导**：

$$
(y - Pw)^T\alpha = y^T\alpha - w^T P^T \alpha
\quad\Longrightarrow\quad
\frac{\partial L}{\partial w} = 2w - P^T\alpha
$$

令一阶条件为零：

$$
2w - P^T\alpha = 0 \quad\Longrightarrow\quad w = \tfrac{1}{2}P^T\alpha
$$

> 这一步解释了**为什么最小范数解必然能写成 $P^T\alpha$ 的形式**。

**Step 3 — 代回原约束，先求 $\alpha$**：

$$
y = Pw = P\big(\tfrac{1}{2}P^T\alpha\big) = \tfrac{1}{2}PP^T\alpha
\quad\Longrightarrow\quad
\hat{\alpha} = 2(PP^T)^{-1}y
$$

**Step 4 — 代回 $w$**：

$$
\hat{w} = \tfrac{1}{2}P^T\hat{\alpha} = \tfrac{1}{2}P^T\big[2(PP^T)^{-1}y\big] = P^T(PP^T)^{-1}y
$$

**手算演练：一个方程、两个未知数**

$$
P = [1 \quad 1], \qquad y = 2
$$

约束是 $w_1 + w_2 = 2$。$(0,2)$、$(1,1)$、$(3,-1)$ 都能 exact fit，但 norms 不同：

$$
\hat{w} = P^T(PP^T)^{-1}y = \begin{bmatrix} 1 \\ 1 \end{bmatrix}\Big([1\ 1]\begin{bmatrix}1\\1\end{bmatrix}\Big)^{-1} \cdot 2 = \begin{bmatrix}1\\1\end{bmatrix}\cdot\frac{1}{2}\cdot 2 = \begin{bmatrix}1\\1\end{bmatrix}
$$

它在直线 $w_1 + w_2 = 2$ 上**离原点最近**，因此 norm 最小。

### 4.8 Ridge Regression：加一个 $\lambda I$ 买稳定

当 large coefficients 使输出对小输入扰动过度放大时，在 SSE 后加入 weight decay：

$$
J_{SSEr}(w) = \|y - Pw\|_2^2 + \lambda\|w\|_2^2, \qquad \lambda > 0
$$

令 gradient 为零：

$$
-2P^T(y - Pw) + 2\lambda w = 0
\quad\Longrightarrow\quad
(P^T P + \lambda I)w = P^T y
$$

$$
\boxed{\ \hat{w}_{primal} = (P^T P + \lambda I)^{-1} P^T y\ }
$$

Dual 形式：

$$
\boxed{\ \hat{w}_{dual} = P^T (PP^T + \lambda I)^{-1} y\ }
$$

| 形式 | 求逆矩阵 | 适合的相对规模 |
|---|---|---|
| Primal ridge | $(D+1) \times (D+1)$ | $D+1$ 较小，常见于 over-determined |
| Dual ridge | $m \times m$ | $m$ 较小，常见于 under-determined |

> **`λI` 干什么**：给 covariance / Gram matrix 的 diagonal 加正数，**把 eigenvalues 向正方向平移**，减少接近零的 eigenvalue 在求逆时造成的数值放大。
> **权衡**：$\lambda$ 增大通常使参数更小、variance 更低，但 bias 更大。
> 两式描述**同一类** regularized solution；"dual" 不是另一种 loss，而是换到 sample-coordinate $\alpha$ 中求解。

### 4.9 Kernel Regression

#### 从 dual inner product 到 kernel

在 dual form 中，预测只通过 training features 的 inner products 使用 `P`：

$$
w = P^T\alpha, \qquad g(x) = \alpha^T P p(x)
$$

定义 training kernel matrix 与 test kernel matrix：

$$
K = PP^T \in \mathbb{R}^{m \times m}, \qquad K_t = k(P_t, P) \in \mathbb{R}^{n \times m}
$$

若 kernel function 可直接计算 $k(x_i, x_j) = p(x_i)^T p(x_j)$，就**无需显式构造可能极高维的 $p(x)$**。例如 polynomial kernel：

$$
k(x_i, x) = (1 + x_i^T x)^r
$$

**把矩阵按"谁和谁比较"来读**：

- `K` 的第 $i$ 行、第 $j$ 列是 training sample $x_i$ 与 $x_j$ 的相似度；
- `Kt` 的第 $r$ 行、第 $j$ 列是 test sample $x_{t,r}$ 与 training sample $x_j$ 的相似度；
- 因此 `Kt` **必须有 $m$ 列**，才能与长度为 $m$ 的 $\alpha$ 相乘。

> Kernel trick 省掉的是**显式 feature expansion**，不是省掉 training samples 之间的 pairwise comparisons。

#### Kernel regression（未正则化）

$$
\hat{\alpha} = K^{-1}y, \qquad \hat{y}_t = K_t K^{-1}y
$$

条件是 `K` nonsingular——**这在实际数据中不总能保证**。

#### Kernel ridge regression

把 $\|w\|_2^2 = \alpha^T K\alpha$ 写进 dual objective：

$$
J(\alpha) = \frac{\lambda}{2}\alpha^T K\alpha + \frac{1}{2}(y - K\alpha)^T(y - K\alpha)
$$

课件推导得到：

$$
\boxed{\ \hat{\alpha} = (K + \lambda I)^{-1} y\ }, \qquad
\boxed{\ \hat{y}_t = K_t (K + \lambda I)^{-1} y\ }
$$

多输出时只需以 `Y` 代替 `y`：

$$
\hat{G}_t = K_t (K + \lambda I)^{-1} Y
$$

#### Gaussian kernel 与 $\sigma$

$$
K_{ij} = \exp\Big(-\frac{\|x_i - x_j\|_2^2}{2\sigma^2}\Big)
$$

- $\sigma$ **小**：相似度衰减快，prediction 更局部、更容易起伏；
- $\sigma$ **大**：相似度衰减慢，曲线更平滑，也可能抹去局部结构。

> 课堂特别强调：$\sigma$ **会直接改变 kernel fit**，它不是无关的作图参数。

#### 课件 kernel 例题

| 例题 | 做法 | 要点 |
|---|---|---|
| **Example 5.3**（Gaussian kernel） | ①由 training inputs 形成 `K` → ②$\hat{\alpha} = (K+\lambda I)^{-1}y$ → ③training output = $K\hat{\alpha}$ → ④对 test inputs 形成 `Kt` → ⑤test output = $K_t\hat{\alpha}$ | 五步固定流程 |
| **Example 5.4**（五阶 polynomial kernel） | $K = (1 + XX^T)^{\circ 5}$，$\circ 5$ 表示逐元素取五次幂 | 重点：**不用枚举五阶 polynomial expansion 的全部 monomials** |

### 4.10 从回归输出到分类

#### Binary threshold

若 targets 为 $\{0, 1\}$，常在 normalized score 上用 $\tau = 0.5$；若 targets 为 $\{-1, +1\}$，常用 $\tau = 0$：

$$
\mathrm{cls}(g(x,w)) = \begin{cases} 1, & g(x,w) > \tau \\ 0, & g(x,w) < \tau \end{cases}
$$

> ⚠️ 课件公式只写了严格大于与严格小于，**等号落在哪一类必须在实现中明确**。

#### Multi-category winner-takes-all

对第 $j$ 个 test sample，取 $C$ 个 outputs 中最大的一个：

$$
\mathrm{cls}(g(x_j, W)) = \arg\max_{k \in \{1, \ldots, C\}} g(x_j, w_k)
$$

课件称为 one-versus-all / winner-takes-all，输出为 one-hot vector。

### 4.11 课件例题汇总

| 题目 | 设置 | 答案 / 要点 |
|---|---|---|
| **Example 5.1(a)** | 10 samples、二维、二阶 full polynomial，$P: 10 \times 6$，用 primal LS | test scores $\hat{G}_t = \begin{bmatrix} 0.3080 & 0.6892 & 0.0028 \\ -0.5763 & 1.4049 & 0.1714\end{bmatrix}$ |
| **Example 5.2(a)** | 6 samples、三阶 full polynomial（含 $\binom{2+3}{3} = 10$ terms），$P: 6 \times 10$，用 dual least-norm | 与 5.1 用**相同两个 test points**，差别是训练样本更少、feature expansion 更高 |
| **Examples 5.1(b), 5.2(b)** | 分别用 primal / dual ridge，$\lambda = 0.001$ | 预测类别相同、score 数值不同 → **regularization 改变的是 fitted surface，不是预先保证某个 label** |
| **Examples 5.1(c), 5.2(c)** | 对两行 test scores 做 row-wise argmax | 均得第一个 test point → class 2，第二个 → class 3 |
| 课件问题 | 不显式形成 `P`，怎样得到 polynomial `K`？ | 直接按 $K_{ij} = (1 + x_i^T x_j)^r$ 计算 pairwise kernels |

### 4.12 L5 考试点

> 老师原话：**L5 是把 L3 的 over- / under-determined systems 应用到 learning。**

- ✅ 必须会**先看 `P` 的 shape，再选 primal 或 dual formula**
- ✅ **simple hand calculation 与课件 examples 要会**（如 §4.4 的三点拟合直线）
- ✅ kernel 的关键是**直接算 training-training 与 test-training similarities**，不必显式求 $p(x)$
- ⚠️ **长篇 primal-to-dual manipulation 用于理解来源**，应用最终式与检查维度更重要
- ⚠️ 矩阵 theoretically invertible **不代表数值计算一定可靠**：若 eigenvalues 跨越很大尺度，floating-point inversion 仍可能放大误差，$\lambda I$ 能改善 conditioning。实际代码宜用 linear solve 而非显式 `inv`，但**考试推导仍按课件 inverse 形式书写**

---

## 五、Lecture 6 — Advanced Analytic Classification

> 📄 `Quiz2/EE6406_L6_Advanced_Analytic_Classification_Cornell_Notes.pdf`
> 📄 课件 `week6/EE6406-Lecture6-TKA-v1.pdf`

**本讲主线**：classification counting objective 不可导 → 用 shifted quadratic 只工作在单侧区间 → TER 得到 class-balanced closed form → AUC 把所有正负样本组成 pairs 并优化 ranking → data scaling / translation 把 TER、AUC、FLD、weighted LS 与 LSE 放进同一框架。

**两条主线一句话**：

> TER 问"**固定 threshold 下两类各错多少**"；AUC 问"**任取一正一负，正样本是否排在负样本前面**"。

### 5.1 核心矛盾：counting loss 不可导

| 层级 | 处理对象 | 是否依赖单一 threshold |
|---|---|---|
| **TER** | FPR + FNR，分别对两类归一化 | 是 |
| **ROC** | threshold 扫描产生的一组 operating points | 扫描全部 thresholds |
| **AUC** | 正样本 score 高于负样本 score 的 pairwise fraction | 否 |
| **AAC** | $1 - \mathrm{AUC}$ 对应的错误排序 fraction | 否 |

Zero-one / counting loss **在 threshold 处跳变，其他位置几乎处处 gradient 为 0**。它准确表达最终计数目标，却不能给 gradient method 提供连续的局部方向。

#### 为什么 sigmoid approximation 仍不理想

$$
\sigma(\theta) = \frac{1}{1 + e^{-\theta}}, \qquad \theta > 0
$$

它可导，但有两个问题：

1. $\sum\sigma(w)$ 对 $w$ **仍是 nonlinear**，可能有 local solutions，结果依赖 initialization；
2. sigmoid 饱和区形成 **local plateaus**，gradient 很小，搜索可能缓慢。

### 5.2 TER：Total Error Rate

$$
\mathrm{TER} = \mathrm{FPR} + \mathrm{FNR}
$$

展开为：

$$
\mathrm{TER} = \frac{1}{m^-}\sum_{j=1}^{m^-} \mathrm{cls}\big(g(x_j^-, w) > \tau\big) + \frac{1}{m^+}\sum_{i=1}^{m^+} \mathrm{cls}\big(g(x_i^+, w) < \tau\big)
$$

**每类先除以自己的 class size**，所以两类在 objective 中**等权**。

#### 为什么类别不平衡时要分别归一化

假设 90 个 negative、10 个 positive，某分类器把 90 个 negative 全部判对，却把 10 个 positive 全部判错：

$$
\mathrm{FPR} = \frac{0}{90} = 0, \qquad \mathrm{FNR} = \frac{10}{10} = 1
$$

普通 accuracy 是 **90%**（看起来很高），但：

$$
\mathrm{TER} = 0 + 1 = 1, \qquad \mathrm{HTER} = \frac{\mathrm{TER}}{2} = 0.5
$$

> TER 没有让 90 个多数类样本淹没 10 个少数类样本，而是**先在每个 class 内计算错误率，再把两类等权相加**。

补充指标：

$$
\mathrm{TER} = \mathrm{FPR} + \mathrm{FNR}, \qquad \mathrm{HTER} = \frac{\mathrm{FPR} + \mathrm{FNR}}{2}, \qquad \mathrm{Balanced\ Accuracy} = 1 - \mathrm{HTER}
$$

### 5.3 ⭐ 核心技巧：Shifted One-Arm Quadratic

> **这是整个 L6 最重要的思想**，务必理解，不能只背闭式解。

#### Step 1 — 把两类错误统一成"变量大于 0"

$$
\epsilon_j = g(x_j^-, w) - \tau, \qquad \eta_i = \tau - g(x_i^+, w)
$$

（其中 $\to 0$ 用于表示 strict inequality，实践中忽略。）

这样 false positive 与 false negative 都可写为**某个变量大于 0 时 loss 为 1**：

$$
\mathrm{TER} = \frac{1}{m^-}\sum_j L(\epsilon_j > 0) + \frac{1}{m^+}\sum_i L(\eta_i > 0)
$$

**直觉**：无论原样本属于哪一类，都把"犯错方向"翻到数轴正侧，之后才能使用同一种 surrogate。

**用一个 $\tau = 0.5$ 的例子检查符号**：

| 样本 | score | 原判定 | 统一后的变量 | 是否 $> 0$ |
|---|---|---|---|---|
| negative | 0.8 | 高于 threshold，false positive | $\epsilon = 0.8 - 0.5 = +0.3$ | 是，错误 |
| negative | 0.2 | 低于 threshold，正确 | $\epsilon = 0.2 - 0.5 = -0.3$ | 否，正确 |
| positive | 0.1 | 低于 threshold，false negative | $\eta = 0.5 - 0.1 = +0.4$ | 是，错误 |
| positive | 0.9 | 高于 threshold，正确 | $\eta = 0.5 - 0.9 = -0.4$ | 否，正确 |

因此，后面的统一 loss **只需判断一个量是否大于 0**。

#### Step 2 — 为什么普通 quadratic 不行

Linear link $g(x,w) = w^T p(x)$ 与 quadratic loss 可形成 convex problem 和 closed form；**但 $z^2$ 关于 0 对称，正负两侧都会随 $|z|$ 增大**，无法保证"错误侧 loss 高、正确侧 loss 低"。

#### Step 3 — Shifted one-arm quadratic

解决办法**不是**让整个 quadratic 近似 step，而是**先移动 data / residual，使所有需要比较的值落在 quadratic 的同一个 monotonic arm**：

$$
\min_w \Big\{ \frac{1}{2m^-}\sum_{j=1}^{m^-}(\epsilon_j + \eta)^2 + \frac{1}{2m^+}\sum_{i=1}^{m^+}(\eta_i + \eta)^2 \Big\}
$$

其中 $\eta$ 是 offset。加入 weight decay 后：

$$
\min_w\ \frac{b}{2}\|w\|_2^2 + \frac{1}{2m^-}\sum_j \big[w^T p(x_j^-) - \tau + \eta\big]^2 + \frac{1}{2m^+}\sum_i \big[\tau - w^T p(x_i^+) + \eta\big]^2
$$

**取 $\eta = 1$ 验证**：

- 正确侧 residual 为 $-0.8$ 时：$(-0.8 + 1)^2 = 0.04$ ← 小 ✓
- 错误侧 residual 为 $+0.4$ 时：$(0.4 + 1)^2 = 1.96$ ← 大 ✓

> **核心机制**：TER 与 AUC 都使用"**offset 后只落在 quadratic 的一个 arm**"这一技巧。
> 若同时使用 parabola 的左右两臂，就可能出现"**离 threshold 很远但分类正确的样本反而被重罚**"，因此课件强调 **one-arm matching**。

### 5.4 TER Closed-Form Learning

先对 objective 求导并令其为零（记 $p_j^- = p(x_j^-)$、$p_i^+ = p(x_i^+)$）：

$$
0 = bw + \frac{1}{m^-}\sum_j p_j^-\big(p_j^{-T}w - \tau + \eta\big) + \frac{1}{m^+}\sum_i p_i^+\big(p_i^{+T}w - \tau - \eta\big)
$$

把所有含 $w$ 的项放在左边，其余常数项放在右边，得 $Aw = c$：

$$
A = bI + \frac{1}{m^-}\sum_j p_j^- p_j^{-T} + \frac{1}{m^+}\sum_i p_i^+ p_i^{+T}
$$

$$
c = \frac{\tau - \eta}{m^-}\sum_j p_j^- + \frac{\tau + \eta}{m^+}\sum_i p_i^+
$$

若 $A$ nonsingular，则 $\hat{w} = A^{-1}c$：

$$
\boxed{\
\hat{w} = \Big[ bI + \frac{1}{m^-}\sum_j p_j^- p_j^{-T} + \frac{1}{m^+}\sum_i p_i^+ p_i^{+T} \Big]^{-1}
\Big[ \frac{\tau-\eta}{m^-}\sum_j p_j^- + \frac{\tau+\eta}{m^+}\sum_i p_i^+ \Big]
\ }
$$

#### 怎么读这个式子

- **inverse 内部的 `A`** 汇总 regularization 与两类样本的 outer products，描述"**数据沿哪些 feature directions 分布**"；
- **右侧的 `c`** 汇总两类希望靠近的 target levels，描述"**参数应朝哪个方向移动**"；
- **$1/m^-$ 与 $1/m^+$** 使两类贡献**不由样本数量决定**。

#### 符号解释

| 符号 | 含义 |
|---|---|
| $b$ | weight-decay strength |
| $\tau$ | classification threshold |
| $\eta$ | quadratic offset |
| $m^-, m^+$ | 两类的样本数，用于 class-wise normalization |
| $p_j^- p_j^{-T}$ | negative sample 的 outer product（positive 同理） |

#### Compact matrix form

将 negative / positive rows 分别堆成 $P^-$、$P^+$，$1$ 是相应长度的 all-ones vector：

$$
\hat{w} = \Big(bI + \frac{1}{m^-}P^{-T}P^- + \frac{1}{m^+}P^{+T}P^+\Big)^{-1}
\Big( \frac{\tau-\eta}{m^-}P^{-T}1^- + \frac{\tau+\eta}{m^+}P^{+T}1^+ \Big)
$$

> 这就是**把两类分别加权的 ridge-like least squares**。

#### Weighted-LS form

若 data rows 按 negative 再 positive 排列，构造 diagonal class weights $M = M^- + M^+$（negative block 为 $1/m^-$，positive block 为 $1/m^+$），target vector 的两类常数分别是 $\tau - \eta$ 与 $\tau + \eta$。于是：

$$
\boxed{\ \hat{w} = (bI + P^T MP)^{-1}P^T M y\ }
$$

#### Dual TER

令 $w = P^T M\alpha$：

$$
\hat{\alpha} = (bI + P^T P M)^{-1} y, \qquad \hat{w} = P^T M (bI + P^T P M)^{-1} y
$$

多类别时是 $C$ 个 one-versus-all TER problems；每个 class-specific $P_k, M_k, y_k$ 的 **row order 必须一致**。

### 5.5 AUC-Based Learning

#### 为什么从 ROC 改成 AUC

**ROC 是 threshold 扫描得到的一条 curve，不是单一 scalar objective。** AUC 把 curve 汇总成 scalar，并有清楚的 pairwise ranking interpretation。

令：

$$
\xi_{ij} = g(x_i^+) - g(x_j^-)
$$

若 $\xi_{ij} > 0$，这对 positive–negative samples 排序正确。采用 tie 计 0.5 的 Heaviside function：

$$
u(\xi) = \begin{cases} 1, & \xi > 0 \\ 0.5, & \xi = 0 \\ 0, & \xi < 0 \end{cases}
$$

$$
\boxed{\ \mathrm{AUC} = \frac{1}{m^+ m^-}\sum_{i=1}^{m^+}\sum_{j=1}^{m^-} u(\xi_{ij})\ }
$$

**手算演练：四个 pairs 手算 AUC**

positive scores $\{0.9, 0.4\}$，negative scores $\{0.6, 0.2\}$，共 $2 \times 2 = 4$ 对：

| Pair | 比较 | 结果 |
|---|---|---|
| 0.9 vs 0.6 | positive 更高 | 1 |
| 0.9 vs 0.2 | positive 更高 | 1 |
| 0.4 vs 0.6 | positive 更低 | 0 |
| 0.4 vs 0.2 | positive 更高 | 1 |

$$
\mathrm{AUC} = \frac{1+1+0+1}{4} = 0.75
$$

> 这就是"**随机抽一个 positive 和一个 negative，positive score 更高**"的经验概率。

#### AUC 与 AAC

Maximize AUC 等价于 minimize Area Above the ROC Curve（AAC）：

$$
\mathrm{AAC} = \frac{1}{m^+ m^-}\sum_{i,j} u(-\xi_{ij})
$$

对 linear-parametric predictor，课件使用 **pairwise difference**：

$$
d_{ij} = p_j^- - p_i^+ \qquad (\text{注意：negative 减 positive})
$$

Quadratic approximation 加 offset 与 regularization：

$$
\min_w \Big\{ \frac{b}{2}\|w\|_2^2 + \frac{1}{2m^+m^-}\sum_{i,j}(d_{ij}^T w + \eta)^2 \Big\}
$$

> 当 normalized score differences 落在 $[-1, 1]$ 时，**$\eta = +1$ 才使 wrongly ranked pairs 的 quadratic output 高于 correctly ranked pairs**；$\eta = -1$ 会反向。

#### AUC / AAC closed form

令：

$$
A_{pair} = bI + \frac{1}{m^+m^-}\sum_{i,j} d_{ij} d_{ij}^T, \qquad
c_{pair} = -\frac{1}{m^+m^-}\sum_{i,j} d_{ij}
$$

一阶条件仍是 $A_{pair}w = c_{pair}$，因此：

$$
\boxed{\
\hat{w} = \Big[ bI + \frac{1}{m^+m^-}\sum_{i,j} d_{ij} d_{ij}^T \Big]^{-1}
\Big[ -\frac{1}{m^+m^-}\sum_{i,j} d_{ij} \Big]
\ }
$$

它**一次求得在 pairwise ranking sense 下的 least-squares optimum，不需要在训练式中先选 threshold**。

#### ⭐ TER 与 AUC 的对照（本讲最漂亮的地方）

| | 累积什么 | 训练单位 |
|---|---|---|
| **TER** | single-sample **outer products** $p\,p^T$ | 每个**样本** |
| **AUC** | positive-negative **difference outer products** $d\,d^T$ | 每个**正负对** |

> **公式外形相似，但训练单位不同。** 理解这一点，两个公式只需记一个。

#### 训练无 threshold，部署仍要 threshold

AUC 对所有 operating thresholds 的排序表现负责，但实际 binary decision 必须选一个 operating point。课件用 approximated TER 给出：

$$
\boxed{\ \tau = \frac{1}{2m^-}\sum_{j=1}^{m^-}\hat{w}^T p_j^- + \frac{1}{2m^+}\sum_{i=1}^{m^+}\hat{w}^T p_i^+\ }
$$

它是**两类平均 scores 的中点**。

> ⚠️ 若应用代价不对称（银行、安防），实际 threshold 仍可能按安全、医疗或商业要求调整。**AUC 高表示整体排序好，不替代具体 operating threshold 的代价分析。**

### 5.6 Generalized Learning by Data Transformation

#### Transformation 的对象

对 raw feature 或 generalized feature：

$$
\tilde{x} = Tx + a, \qquad \tilde{p}(x) = Tp(x) + a
$$

$T$ 做 scaling / rotation / linear transformation，$a$ 做 translation。若有 $K$ 组 $(T_k, a_k)$，每个 original sample 可产生 $K$ 个 transformed samples，代价是 computation 增加。

**先把 transformation 看成"换一套比较数据的方式"**：

| 操作 | 作用 |
|---|---|
| **Scaling** | 改变不同类别或方向的相对权重 |
| **Translation** | 把数据移到新的参考中心 |
| **Centering** | 令 $a$ 与 class mean 有关，使公式关注**类内散布**而不是原始坐标 |
| **多组 transformation** | 让同一原始样本以多种视角参与 objective |

#### TAUC 为什么能统一其他方法

Transformed AUC（TAUC）在每个 pair difference 上再累加 $K$ 组 transformations。改变 class-dependent scaling parameters $\beta_k, \gamma_k$ 和 translations $u_k, v_k$，可让某些 terms 保留、消失或变成 class-centering：

| 设置变化 | 得到的关系 | 直觉 |
|---|---|---|
| 所有 class scalings 都为 1、无 translation | **TAUC → AUC** | 不再改变 pairwise data |
| $\beta_1 = \gamma_2 = 0$，$\beta_2 = \gamma_1 = 1$ | **TAUC → TER-like** | pairwise double sum 分解为 class-wise single sums |
| 加 class mean translations | **TAUC → FLD-like** | 把每类 data 中心化后比较 mean separation |
| 写成 $P^T MP$ 与 $P^T My$ | **TER → weighted LS** | class-normalized weights 进入 LS |

#### FLD 与 TER 的中心化差别

课件的特殊设置得到：

$$
\hat{w} = \Big[ \frac{1}{m^-}\sum_j (p_j^- - \mu^-)(p_j^- - \mu^-)^T + \frac{1}{m^+}\sum_i (p_i^+ - \mu^+)(p_i^+ - \mu^+)^T \Big]^{-1}(\mu^+ - \mu^-)
$$

与 TER 相比，FLD-like form **明确减去 class means**：

> **FLD 是 centered，TER 是 non-centered。**

> ⚠️ **学习边界**：generalized framework 的长式用于展示方法间的结构关系。课堂明确说**不要求记住整张复杂参数表**；应掌握 scaling、translation、class-centering 如何把一个 formulation 化为另一个。

### 5.7 与贝叶斯推断的联系（概念即可）

#### Regression likelihood

若 $y_i = x_i^T w + e_i$，$e_i \sim \mathcal{N}(0, \sigma^2)$，且 samples independent，则：

$$
p(y \mid X, w) = (2\sigma^2)^{-m/2}\exp\Big[-\frac{1}{2\sigma^2}(y - Xw)^T(y - Xw)\Big]
$$

**Maximizing this likelihood 等价于 minimizing SSE。** 若再给 Gaussian prior，posterior mean 会出现 covariance term 加 prior precision 的 **ridge-like structure**。

#### TER 的 dual-Gaussian interpretation

TER quadratic approximation 把 negative 与 positive 分别拉向两个 constant targets：

$$
y^- = \tau - \eta, \qquad y^+ = \tau + \eta
$$

两类可分别看作**不同 Gaussian error groups**，再将 likelihood 相乘。若两类 variances 不同，它们**自然产生不同 class weights**——这解释了 TER closed form 为什么像 two-group weighted regression。

#### AUC 的 pairwise Gaussian interpretation

AUC/AAC 的"输入"不是单个 $x$，而是 pairwise difference $x_j^- - x_i^+$；因此其 quadratic approximation 可视为**在 pairwise differences 上做 Gaussian regression**。TAUC 则对应这些 differences 的 scaled / translated version。

### 5.8 高频对比题总表

| 方法 | 优化对象 | 数据单位 | Threshold | Class imbalance 处理 |
|---|---|---|---|---|
| **LSE** | residual magnitude | single samples | 训练式无；分类后加 | 默认按 samples 加权 |
| **TER** | FPR + FNR | class-separated samples | **显式** $\tau$ | 每类除以 $m$，两类等权 |
| **AUC/AAC** | pairwise ranking | positive-negative pairs | **训练式无** | 每对等权；由 $m^+m^-$ 归一化 |
| **FLD-like** | within-class scatter 与 mean separation | centered class samples | 后续决定 | 显式使用 class means |
| **Weighted LS** | weighted residual magnitude | weighted samples | 后续决定 | 权重矩阵 $M$ 决定 |

### 5.9 L6 考试点

**需要较详细掌握**：

- ✅ TER、AUC 的**目标**（各回答什么问题）
- ✅ **one-arm shifted quadratic**（为什么必须加 offset $\eta$）
- ✅ 核心 closed forms + 简单计算

**需要概念掌握**：

- ✅ generalized framework 中 **scaling / translation / centering 如何连接方法**

**不要求死背**：

- ❌ TAUC 展开的长 double / triple sums
- ❌ 整张参数设置表

---

## 六、Lecture 7 — Penalized Learning

> 📄 `Quiz2/EE6406_L7_Penalized_Learning_Cornell_Notes.pdf`
> 📄 课件 `week7/EE6406-Lecture7-TKA-v1.pdf`

**本讲主线**：只压低 training error 会过拟合 → 在 objective 中加入 coefficient penalty → $L_2$ 得 ridge、$L_1$ 得 lasso、一般 $L_p$ 得 bridge → primal regularization 适合 over-determined，dual least-norm 适合 under-determined → 通过 coefficient profiles 检查 stability、compression 与 feature selection。

> **本讲只抓一个权衡**：data-fit term 希望模型贴近训练数据，penalty 希望参数更小或更稀疏；**$\lambda$ 决定两种要求谁更重要，penalty 的形状决定"大家一起缩小"还是"把部分系数压成 0"。**

### 6.1 为什么需要惩罚学习

高复杂度模型能追随 training noise，使 training error 持续下降，但 unseen-data error 在某一后果反而上升：

```
model complexity ↑
    training error ↓ monotonically
    test error     ↓ then ↑
                     ↑
             optimal complexity
```

把模型复杂度从低到高分成三个阶段：

| 阶段 | Training error | Test error | 原因 |
|---|---|---|---|
| **太简单** | 高 | 高 | 连主要规律也表达不了（underfitting） |
| **适中** | 较低 | **最低附近** | 抓住主要规律，同时没有追随太多 noise |
| **太复杂** | 很低甚至 0 | 重新升高 | 开始把 training noise 当规律（overfitting） |

> Penalization **不直接保证**最优 generalization，但通过限制模型可用的 coefficient magnitude / complexity，减少过度拟合自由度。

#### 通用形式

$$
\hat{w} = \arg\min_w \Big[ \sum_{i=1}^{m} L\big(g(x_i, w), y_i\big) + \lambda R(w) \Big]
$$

| 部件 | 回答的问题 |
|---|---|
| $L$ | 要求模型**解释 training data** |
| $R(w)$ | 惩罚过大、过多或不符合先验结构的 coefficients |
| $\lambda$ | 控制 **fit 与 simplicity 的权衡** |

#### $\lambda$ 的作用

| $\lambda$ | 状态 | Objective 更在意什么 | 常见结果 |
|---|---|---|---|
| $= 0$ | 无正则 | 只在意 training fit | 回到 unregularized solution |
| 较小 | 轻度限制 | fit 为主 | coefficients 略缩小 |
| 较大 | penalty 更重要 | 明显缩小 | 可能 underfit |
| $\to \infty$ | 几乎只想让参数最小 | 非截距系数趋近 0 | 模型失去表达能力 |

#### 为什么 large coefficients 可能不稳定

对 $g(x, w) = w^T p(x)$，输入 perturbation $\delta p$ 引起 $\delta g = w^T \delta p$。**若 $\|w\|$ 很大，即使 $\delta p$ 很小，输出也可能大幅变化。**

> Coefficient shrinkage 因此**既是 complexity control，也是 numerical / prediction stability control**。

#### 三类应用

1. **Penalized linear regression**：ridge、lasso；
2. **Feature selection**：high-dimensional genomics、text、finance 中用 sparsity 保留少数 variables；
3. **Neural networks / inverse problems**：weight decay 防过拟合，penalty 引入 stability 或 prior knowledge。

### 6.2 Coefficient Shrinkage：三种 penalty 的形状 ⭐

#### Ridge：$L_2^2$ penalty

课程用 half scaling 写：

$$
J_{SSEr}(w) = \frac{1}{2}\sum_{i=1}^{m}(y_i - p_i^T w)^2 + \frac{\lambda}{2}\|w\|_2^2
$$

它等价于在 SSE minimization 中加入约束 $\|w\|_2^2 \le t$。

> **$L_2$ 的圆形 / 球形 contour 平滑，通常同时缩小全部 coefficients，但不强迫许多元素恰好为 0。**

#### LASSO：$L_1$ penalty

LASSO（**L**east **A**bsolute **S**hrinkage and **S**election **O**perator）：

$$
J_{lasso}(w) = \sum_{i=1}^{m}(y_i - p_i^T w)^2 + \lambda\|w\|_1, \qquad \|w\|_1 = \sum_{j=0}^{D}|w_j|
$$

等价于约束 $\|w\|_1 \le c$。

> **$L_1$ constraint 有尖角；loss contour 与尖角相切时，某些 coordinates 正好为 0**，所以可做 **embedded feature selection**。

**"尖角"可以这样理解**：在 $w_j = 0$ 附近，$|w_j|$ 的斜率会从 $-1$ 突然变成 $+1$。优化时，**只要 data-fit term 提供的改善不足以克服这段 penalty，最优点就可以停在 $w_j = 0$**。相比之下 $w_j^2$ 在 0 附近的斜率连续趋近 0，更常把系数缩得很小，**而不是恰好压成 0**。

#### Bridge regression：一般 $L_p$ penalty

$$
\|w\|_p = \Big(\sum_{j=0}^{D}|w_j|^p\Big)^{1/p}, \qquad
J_{bridge}^{SSE}(w) = \sum_{i=1}^{m}(y_i - p_i^T w)^2 + \lambda\|w\|_p^p
$$

课件关注 $0 \le p < 2$：

| $p$ 范围 | 典型效果 | 优化性质 |
|---|---|---|
| $p = 2$ | ridge-like smooth shrinkage | convex、smooth |
| $p = 1$ | lasso-like sparsity | convex、**在 0 不可导** |
| $0 < p < 1$ | 更强 subset selection / compression | ⚠️ **non-convex**，优化更困难 |
| $1 < p < 2$ | compression 为主 | smooth，通常较少 exact zeros |

> ⚠️ 这里的 $p$（课件后文也写作 $k$）控制 **penalty 的形状，不是 polynomial order**。读公式时必须根据所在章节判断符号含义。

### 6.3 Regularization vs Least-Norm：两种写法的角色

| Approach | 主 objective | Constraint / secondary term | 常见系统 |
|---|---|---|---|
| **Primal regularization** | data-fit loss | 限制 / 惩罚 $\|w\|$ | **over-determined** |
| **Dual least-norm** | $\|w\|$ | **exact fit** $y = Pw$ | **under-determined** |

Least-norm $L_2$ problem：

$$
\min_w \|w\|_2^2 \quad \text{s.t.} \quad y = Pw
\quad\Longrightarrow\quad
\hat{w} = P^T(PP^T)^{-1}y
$$

（要求 $PP^T$ nonsingular。）一般化到 $L_p$ 后，每个 sample constraint 对应一个 Lagrange multiplier。

### 6.4 Ridge Regression Revisited

$$
\boxed{\ \hat{w}_{primal} = (P^T P + \lambda I)^{-1}P^T y\ }, \qquad
\boxed{\ \hat{w}_{dual} = P^T(PP^T + \lambda I)^{-1}y\ }, \qquad \lambda > 0
$$

- Primal inverse size 是 $(D+1) \times (D+1)$；dual inverse size 是 $m \times m$。**这也是选择 computational form 的直接依据。**

> ⚠️ 两式**不是**"超定只能用 primal、欠定只能用 dual"的绝对规则。更准确的判断是：**比较 feature dimension $D+1$ 与 sample size $m$，并检查 rank 与 numerical conditioning；通常选择较小且更稳定的 inverse space。**

#### Constrained view

Primal ridge 可写成 $\min_w \|y - Pw\|_2^2$ s.t. $\|w\|_2^2 \le c$；
Dual least-norm 的起点则是 $\min_w \|w\|_2^2$ s.t. $y = Pw$。

对后一式写 Lagrangian 并对 $w$ 求导，得到 $w = P^T\alpha$；再在 $\alpha$ space 加 regularization，得到 $(PP^T + \lambda I)^{-1}$。

#### Softening exact-fit constraint

若 exact fit $y = Pw$ 太严格，引入 residual $\epsilon$：

$$
\min_{w, \epsilon}\ \|w\|_2^2 + \gamma\|\epsilon\|_2^2 \quad \text{s.t.} \quad y = Pw + \epsilon
$$

课件推导出：

$$
\lambda = \frac{1}{\gamma}, \qquad \hat{w} = P^T(PP^T + \lambda I)^{-1}y
$$

> $\gamma$ 大表示 residual 更昂贵，对应 $\lambda$ 小；反之更强调小 coefficients。

#### Ridge 能做什么、不能做什么

- ✅ 能 shrink coefficients、改善 near-singular inverse 的 conditioning；
- ✅ 能降低 variance，但**会引入 bias**；
- ❌ **通常不会做 hard feature selection**，因为 coefficients 很少精确等于 0；
- ⚠️ $\lambda$ **应由 validation / cross-validation 选择，不能只看 training error**。

### 6.5 Proximal Bridge Regression

#### 为什么平滑 absolute value

$|w_j|$ 在 0 不可导。课件用：

$$
f(w_j) = \sqrt{w_j^2 + \epsilon}, \qquad \epsilon > 0 \text{ small}
$$

并定义 **smooth $k$-measure**：

$$
\||w|\|_k = \Big(\sum_j f(w_j)^k\Big)^{1/k}
$$

当 $\epsilon \to 0$ 时 $f(w_j) \to |w_j|$。

> ⚠️ 课件特别说明：这个 smooth operator **不严格构成 normed vector space**，因为它**违反 absolute homogeneity**；因此称 **$k$-measure，不能无条件叫 $L_k$ norm**。

#### Primal $p$-bridge

对 over-determined system：

$$
J(w) = (y - Pw)^T(y - Pw) + \lambda\||w|\|_k^k
$$

课件给出 **coefficient-dependent diagonal weighting form**：

$$
\hat{w} = \Big[ \frac{\lambda k}{2}\mathrm{diag}\big(|w|^{\circ(k-2)}\big) + P^T P \Big]^{-1} P^T y
$$

（要求 bracketed matrix nonsingular；$\circ$ 表示 element-wise operation。）

**直觉**：当 $k < 2$ 时，小 coefficient 在 $|w_j|^{k-2}$ 中对应**更大的 effective penalty weight**，因此被更强地压向 0；large coefficients 相对保留。

> ⚠️ **这不是一次代入即可得到的普通 closed form**——右侧 diagonal matrix **仍含未知的 $w$**，所以该式是 **implicit fixed-point equation**。实际求解常采用 **iterative reweighted ridge**：
>
> 1. 先给一个初值 $w^{(0)}$，通常可取 **ridge solution**；
> 2. 用当前 $w^{(t)}$ 计算每个 coefficient 的 effective penalty weight；
> 3. 固定这些 weights，解一次 weighted ridge 得到 $w^{(t+1)}$；
> 4. 重复直到 coefficients 或 objective 的变化足够小。
>
> 用平滑形式时，第 $j$ 个 weight 可理解为与 $\big((w_j^{(t)})^2 + \epsilon\big)^{\frac{k}{2} - 1}$ 成正比。$k < 2$ 时指数为 **负**，小 $|w_j|$ 产生更大权重，下一轮被压得更强。
>
> **读这个公式的顺序**：$P^T P$ 提供 data-fit curvature；diagonal term 为每个 coefficient 提供**不同强度**的 penalty；inverse 解出下一轮 parameters。**不要把含 $w$ 的 diagonal term 当作已知常数。**

#### Dual $p$-bridge

对 under-determined system：

$$
\min_w \||w|\|_k^k \quad \text{s.t.} \quad y = Pw, \qquad 1 < k \le 2
$$

课件最终解写为：

$$
\hat{w} = \mathrm{sgn}(\theta) \circ P^T (PP^T)^{-1} P \theta^{\circ \frac{1}{k-1}}
$$

其中：

$$
\theta = |P^T|^{\circ \frac{1}{k-1}} \Big[ P |P^T|^{\circ \frac{1}{k-1}} \Big]^{-1} y
$$

> ⚠️ **课堂边界**：Bridge regression 要理解**为什么需要**、$k$ 如何控制 compression / selection、primal 与 dual 各适合什么 shape，以及**会直接应用最终式**。老师明确说**不要求从头背诵整段推导**。

### 6.6 Multiple Outputs

若 $C$ 个 outputs 条件独立并共享同一个 regressor matrix `P`，分别估计：

$$
\hat{W} = [\hat{w}_1, \ldots, \hat{w}_C] \in \mathbb{R}^{(D+1) \times C}, \qquad \hat{G} = P\hat{W}
$$

> 这与 L5 的 multi-category stacking **相同**：算法对每个 target column 求一个 coefficient vector，再横向堆叠。若 outputs 之间存在结构依赖，简单独立堆叠则**没有利用这种依赖**。

### 6.7 Coefficient Profiles：怎么读图

Coefficient profile 以 regularization strength（或其 path index）为横轴、各 $w_j$ 为纵轴：

- 曲线**快速靠近 0**：该 variable 易被 penalty 抑制；
- **长时间保持较大 magnitude**：该 term 对 fit 更重要，或与其他 terms 共同承担解释；
- **精确落到 0**：表示该 method 做了 **variable selection**；
- ⚠️ **correlated variables 的系数路径可能互相替代，不能把 magnitude 直接当因果重要性。**

**建议按以下顺序读图**：

1. 先确认横轴是 $\lambda$、$\log\lambda$ 还是 path index，以及从左到右 penalty 是**增强还是减弱**；
2. 看 $\lambda \approx 0$ 时是否接近 unregularized coefficients；
3. 找哪些 curves **最先到 0**、哪些长期保留；
4. 再对照 validation / test error 选择 operating point，**不能只追求"留下的变量最少"**；
5. 最后检查 correlated variables 是否发生替代，避免把一次 path 当成稳定因果结论。

### 6.8 三个课件实验

#### Example 6.1 — 十阶多项式恢复二、三次项

Training inputs $x \in \{-5, -4, -3, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 10\}$，targets 由 $y = 10x^2 - x^3$ 生成。模型却使用含 intercept 的 **tenth-order polynomial**，共 11 个 coefficients。

课件用 $k = 1.1$、$\lambda = 1$ 的 p-bridge：

> **结果主要保留 $x^2$ 与 $x^3$ 对应的 coefficients，其余高阶 terms 被压缩**——说明 penalty 可从过度丰富的 basis 中恢复较简结构。

课件代码逻辑：

```
construct P = [1, x, x², …, x¹⁰]
construct dense test grid P_t
solve p-bridge(P, y, k=1.1, λ=1, primal=True)
predict y_t = P_t w
plot training samples and prediction curve
```

#### Prostate example — over-determined coefficient profiles

67 training samples、30 test samples、8 inputs 加 intercept，共 9 coefficients，属于 **over-determined** linear regression。

| Method | Tuned parameter(s) | Test MSE | Selected variables（不含 intercept） |
|---|---|---|---|
| OLS | - | 0.520 (0.174) | All |
| Ridge | $\lambda = 1$ | 0.516 (0.175) | All |
| Lasso | $\lambda = 0.02$ | 0.483 (0.160) | 1,2,3,4,5,6,8 |
| Elastic-net | $\lambda = 0.06$, $\alpha = 0.11$ | 0.492 (0.164) | 1,2,3,4,5,6,8 |
| p-bridge, $k = 1$ | $\lambda = 2$ | 0.494 (0.167) | 1,2,3,4,5,6,8 |

> 课件将 gleason coefficient 压到 0，而 lcavol 保持最大 magnitude。应把这理解为**该 fitted model / split 下的结果，不是变量的普遍因果结论**。

#### XOR example — under-determined sparse polynomial

四个 training samples：$(x_1, x_2) \in \{(0,1), (2,1), (1,0), (1,2)\}$，$y \in \{0,0,1,1\}$。使用 third-order polynomial 的 10 terms，因此 $P: 4 \times 10$，属于 **under-determined** system。

| Method | Setting | Test MSE | Selected term indices |
|---|---|---|---|
| OLS | - | 0.513 (0.089) | All |
| Ridge | $\lambda = 6$ | 0.503 (0.047) | 0,1,2,3,4,6,7,8,9 |
| Lasso | $\alpha = 1$, $\lambda = 0.1$ | 0.225 (0.011) | 0,6,7 |
| p-bridge | $k = 1.05$, $\lambda = 30$ | 0.504 (0.040) | **6,7** |
| p-bridge baseline | $k = 2$, $\lambda = 0$ | 0.513 (0.089) | All |

> 课件的 p-bridge 在 $k = 1.05$ 时**只保留 indices 6、7，即 $x_1^3, x_2^3$**；decision contour 仍能完成 XOR separation。此例展示的是 **under-determined + nonlinear basis + sparse coefficient selection** 的组合。

#### ⚠️ 结果表不能单独证明某方法普遍更优

这些表只是在**指定 split、basis 与 tuned settings** 下的 empirical results。正确比较还需要相同 train/test protocol、同等 tuning budget 与重复试验；本讲用它们主要展示**不同 penalty 产生的 coefficient profiles**。

### 6.9 方法对比总表

| Method | Penalty | Sparse exact zeros? | 典型优点 | 主要代价 |
|---|---|---|---|---|
| **OLS** | 无 | 否 | unbiased fit under assumptions、简单 | 高 variance、ill-conditioning、overfitting |
| **Ridge** | $\lambda\|w\|_2^2$ | 通常否 | stable、处理 correlated features | 保留全部 variables、引入 bias |
| **Lasso** | $\lambda\|w\|_1$ | **是** | feature selection、interpretable | correlated features 下选择可能不稳定 |
| **Bridge** | $\lambda\|w\|_p^p$ | 取决于 $p$ | 连续控制 compression / selection | $p < 1$ 时 non-convex，求解与 tuning 更难 |
| **Elastic-net** | $L_1 + L_2$ | 是 | 兼顾 sparsity 与 grouped shrinkage | 多一个 mixing parameter |

### 6.10 L7 考试点

**必须掌握**：

- ✅ **penalization 的 how and why**
- ✅ 会区分 $L_2$ ridge、$L_1$ lasso 与一般 bridge
- ✅ 会按 `P` 的 shape 选 primal / dual ridge，并检查 inverse dimension
- ✅ 会读 coefficient profile

**重点是概念、最终形式与 coefficient behavior**：

- ⚠️ Bridge **不要求完整推导**
- ⚠️ 课堂将 bridge 称为**更重要的新内容**，但仍强调**应用与 interpretation 高于死背 derivation**
- ⚠️ **$\lambda$ 不是"越大越好"**：$\lambda$ 变大使 penalty 更重要、coefficients 更小，但过大时会 underfit。选择应依赖 validation / cross-validation，而非只看 training cost 或 coefficient 是否足够小

---

## 七、三讲对比总表

| | **L5** | **L6** | **L7** |
|---|---|---|---|
| **回答的问题** | 怎样直接求 regression 参数？ | 怎样让 TER/AUC 也能解析求解？ | 怎样抑制过拟合并选择变量？ |
| **Objective** | $\|y - Pw\|_2^2$ | shifted one-arm quadratic | loss $+ \lambda R(w)$ |
| **核心技巧** | shape 决定 primal/dual | offset 使 quadratic 只用一个 arm | penalty 形状决定 shrink vs select |
| **产出** | $(P^TP)^{-1}P^Ty$ / $P^T(PP^T)^{-1}y$ | TER / AUC closed forms | ridge / lasso / bridge |
| **逆的空间** | feature space 或 sample space | 同 L5（ridge-like） | 同 L5 |
| **Threshold** | 训练后加（分类时） | TER 显式 $\tau$；AUC 训练式无 | — |
| **与前一讲的关系** | 把 L3 的系统理论用于 learning | 把 L5 的 closed-form 逻辑搬到 classification | 在 L5/L6 的 objective 上加 penalty |

---

## 八、手算演练（CA2 就考这种）

### 演练 1 — 判断系统类型 + 选公式

**题**：10 个二维训练样本，用二阶 full polynomial。
**答**：$p(x) = [1, x_1, x_2, x_1^2, x_1x_2, x_2^2]^T$，$D+1 = 6$，$P: 10 \times 6$，$m > D+1$ → **over-determined** → 用 $\hat{W} = (P^TP)^{-1}P^TY$。

**变体**：6 个样本、三阶 full polynomial。含 intercept 的 monomial 数 $M = \binom{2+3}{3} = 10$，$P: 6 \times 10$ → **under-determined** → 用 $\hat{W} = P^T(PP^T)^{-1}Y$。

> ⚠️ 多项式特征数公式（$d$ 个变量、总次数不超过 $r$、含常数项）：$M = \binom{d+r}{r}$；**恰好 $r$ 次**则为 $\binom{d+r-1}{r}$。

### 演练 2 — 三点拟合直线（完整计算）

**题**：$P = \begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix}$，$y = [1,2,2]^T$，求 least-squares 解。

$$
P^TP = \begin{bmatrix}3&3\\3&5\end{bmatrix}, \quad P^Ty = \begin{bmatrix}5\\6\end{bmatrix}, \quad
\hat{w} = \frac{1}{6}\begin{bmatrix}5&-3\\-3&3\end{bmatrix}\begin{bmatrix}5\\6\end{bmatrix} = \begin{bmatrix}7/6\\1/2\end{bmatrix}
$$

**拟合直线** $\hat{y} = 7/6 + x/2$。⚠️ 三个预测值**不等于**原 $y$（3 条约束解不出 2 个参数）。

### 演练 3 — 欠定最少范数

**题**：$P = [1\ 1]$，$y = 2$，求 minimum-norm 解。

$$
\hat{w} = P^T(PP^T)^{-1}y = \begin{bmatrix}1\\1\end{bmatrix}\cdot\frac{1}{2}\cdot 2 = \begin{bmatrix}1\\1\end{bmatrix}
$$

**验证**：$w_1 + w_2 = 2$ ✓，且这是直线上离原点最近的点。

### 演练 4 — 手算 AUC

**题**：positive scores $\{0.9, 0.4\}$，negative scores $\{0.6, 0.2\}$，求 AUC。
**答**：4 对中 3 对排序正确 → $\mathrm{AUC} = 3/4 = 0.75$。

**变体**：若出现 tie（如 positive 0.6 vs negative 0.6）→ 该对记 **0.5**。

### 演练 5 — TER vs Accuracy

**题**：90 negative + 10 positive，模型把 negative 全判对、positive 全判错。
**答**：

$$
\mathrm{Accuracy} = \frac{90}{100} = 90\%, \quad
\mathrm{FPR} = \frac{0}{90} = 0, \quad
\mathrm{FNR} = \frac{10}{10} = 1
$$

$$
\mathrm{TER} = 0 + 1 = 1, \qquad \mathrm{HTER} = 0.5
$$

> 这题就是 CA2 最典型的概念计算题：**accuracy 高不代表 TER 好**。

### 演练 6 — Ridge 形式选择

**题**：$m = 5$，$D+1 = 20$，用 ridge，该用哪个形式？逆矩阵多大？
**答**：under-determined（样本少、参数多）→ 选 **dual ridge** $\hat{w} = P^T(PP^T + \lambda I)^{-1}y$，逆矩阵是 **$5 \times 5$**（不是 $20 \times 20$）。

### 演练 7 — Shifted one-arm quadratic 的数值验证

**题**：$\tau = 0.5$，$\eta = 1$。某 negative 样本 score = 0.8，某 positive 样本 score = 0.1，分别算 quadratic penalty。
**答**：

$$
\text{negative}: \epsilon = 0.8 - 0.5 = 0.3 \Rightarrow (0.3+1)^2 = 1.69 \ (\text{错误侧，重罚})
$$

$$
\text{positive}: \eta = 0.5 - 0.1 = 0.4 \Rightarrow (0.4+1)^2 = 1.96 \ (\text{错误侧，重罚})
$$

**对照正确侧**：negative score = 0.2 → $\epsilon = -0.3$ → $(-0.3+1)^2 = 0.49$（轻罚）✓

### 演练 8 — coefficient profile 解读

**题**：某 p-bridge 在 $k = 1.05$ 下只保留 $x_1^3, x_2^3$ 两项，其余为 0，说明什么？
**答**：penalty 形状（$k$ 接近 1）产生 **sparsity / subset selection**；模型从 10 个 term 的 over-complete basis 中选出 2 个必要项即可完成分类——说明 **under-determined + nonlinear basis + sparse selection** 可以共存。

---

## 九、核心公式速查表（最后一页汇总）

### L5

| 主题 | 公式 |
|---|---|
| 模型 | $g(x,w) = w^Tp(x)$ |
| SSE | $J_{SSE}(w) = \|y - Pw\|_2^2$ |
| Normal equation | $P^TPw = P^Ty$ |
| **Primal LS** | $\hat{w} = (P^TP)^{-1}P^Ty$（$m > D+1$） |
| **Dual least-norm** | $\hat{w} = P^T(PP^T)^{-1}y$（$m < D+1$） |
| Multi-output | $\hat{W} = (P^TP)^{-1}P^TY$ |
| **Primal ridge** | $\hat{w} = (P^TP + \lambda I)^{-1}P^Ty$ |
| **Dual ridge** | $\hat{w} = P^T(PP^T + \lambda I)^{-1}y$ |
| Kernel matrices | $K = PP^T \in \mathbb{R}^{m \times m}$，$K_t \in \mathbb{R}^{n \times m}$ |
| Kernel regression | $\hat{\alpha} = K^{-1}y$，$\hat{y}_t = K_tK^{-1}y$ |
| **Kernel ridge** | $\hat{\alpha} = (K+\lambda I)^{-1}y$，$\hat{y}_t = K_t\hat{\alpha}$ |
| Gaussian kernel | $K_{ij} = \exp(-\|x_i - x_j\|_2^2 / 2\sigma^2)$ |
| Polynomial kernel | $k(x_i, x) = (1 + x_i^Tx)^r$ |
| Binary decision | $\mathrm{cls} = \mathbb{1}[g > \tau]$（$\{0,1\}$ 用 0.5；$\{-1,+1\}$ 用 0） |
| Multi-class | $\arg\max_k g(x, w_k)$ |
| Polynomial feature 数 | $M = \binom{d+r}{r}$（含常数项，总次数 $\le r$） |

### L6

| 主题 | 公式 |
|---|---|
| TER | $\mathrm{TER} = \mathrm{FPR} + \mathrm{FNR}$ |
| HTER | $(\mathrm{FPR} + \mathrm{FNR})/2$ |
| Balanced Accuracy | $1 - \mathrm{HTER}$ |
| 错误统一 | $\epsilon_j = g(x_j^-) - \tau$；$\eta_i = \tau - g(x_i^+)$ |
| **TER closed form** | $\hat{w} = \big[bI + \frac{1}{m^-}P^{-T}P^- + \frac{1}{m^+}P^{+T}P^+\big]^{-1}\big[\frac{\tau-\eta}{m^-}P^{-T}1^- + \frac{\tau+\eta}{m^+}P^{+T}1^+\big]$ |
| TER weighted-LS | $\hat{w} = (bI + P^TMP)^{-1}P^TMy$ |
| AUC | $\mathrm{AUC} = \frac{1}{m^+m^-}\sum_i\sum_j u(g(x_i^+) - g(x_j^-))$ |
| AAC | $\mathrm{AAC} = 1 - \mathrm{AUC}$（同 tie 约定下） |
| Pairwise difference | $d_{ij} = p_j^- - p_i^+$ |
| **AUC closed form** | $\hat{w} = \big[bI + \frac{1}{m^+m^-}\sum d_{ij}d_{ij}^T\big]^{-1}\big[-\frac{1}{m^+m^-}\sum d_{ij}\big]$ |
| AUC 部署 threshold | $\tau = \frac{1}{2m^-}\sum_j \hat{w}^Tp_j^- + \frac{1}{2m^+}\sum_i \hat{w}^Tp_i^+$ |
| Heaviside（tie 0.5） | $u(\xi) = 1$ if $\xi>0$; $0.5$ if $\xi=0$; $0$ if $\xi<0$ |

### L7

| 主题 | 公式 |
|---|---|
| Penalized objective | $\hat{w} = \arg\min_w[\sum_i L(g(x_i,w),y_i) + \lambda R(w)]$ |
| Ridge | $J = \|y-Pw\|_2^2 + \lambda\|w\|_2^2$ |
| Lasso | $J = \|y-Pw\|_2^2 + \lambda\|w\|_1$ |
| Bridge | $J = \|y-Pw\|_2^2 + \lambda\|w\|_p^p$ |
| Primal ridge | $\hat{w} = (P^TP + \lambda I)^{-1}P^Ty$ |
| Dual ridge | $\hat{w} = P^T(PP^T + \lambda I)^{-1}y$ |
| Smooth measure | $f(w_j) = \sqrt{w_j^2+\epsilon}$，$\|\|w\|\|_k = (\sum_j f(w_j)^k)^{1/k}$ |
| Primal p-bridge | $\hat{w} = [\frac{\lambda k}{2}\mathrm{diag}(\|w\|^{\circ(k-2)}) + P^TP]^{-1}P^Ty$（implicit） |
| 软化约束 | $\lambda = 1/\gamma$ |
| Multi-output | $\hat{W} = [\hat{w}_1,\ldots,\hat{w}_C]$，$\hat{G} = P\hat{W}$ |

---

## 十、自测清单（Cornell Questions 精选）

### L5（12 问）

1. 为什么同一个 SSE objective 会产生 primal 与 dual 两种解？
2. $P \in \mathbb{R}^{m \times (D+1)}$ 的行、列各代表什么？
3. Over-determined SSE 的 normal equation 怎样得到？
4. Under-determined system 为什么把 $w$ 写成 $P^T\alpha$？
5. Least-norm solution 到底在无穷多解中选了什么？
6. Ridge 中的 $\lambda I$ 为什么改善稳定性？
7. Primal 与 dual ridge 应怎样按 inverse size 选择？
8. Gram matrix $K$ 与 test kernel matrix $K_t$ 的 shape 是什么？
9. Kernel trick 为什么不需要显式列出 polynomial features？
10. Kernel regression 与 kernel ridge 的差别是什么？
11. Binary threshold 与 multi-category argmax 怎样把 regression output 变成类别？
12. L5 的考试计算最先应检查什么？

### L6（12 问）

1. 为什么直接优化 classification count 会变成 nonlinear / non-differentiable problem？
2. TER 为什么比普通 error rate 更适合 class imbalance？
3. $\epsilon_j$ 与 $\eta_i$ 怎样把 FPR/FNR 写成同一方向的 loss？
4. Sigmoid approximation 有哪两个 optimization problems？
5. **Shifted quadratic 为什么必须只使用一个 arm？**
6. TER closed form 中 $m, \tau, \eta, b, P$ 各做什么？
7. AUC 与 AAC 的关系是什么？
8. AUC learning 为什么基于 $m^+m^-$ 个 sample pairs？
9. AUC solution 没有 threshold，实际决策怎样选择 $\tau$？
10. Data transformation 怎样把 AUC、TER、FLD 与 LSE 联系起来？
11. TER 为什么可解释为 weighted LS 与 dual-Gaussian regression？
12. 本讲哪些部分要会计算，哪些只需掌握概念？

### L7（12 问）

1. Training error 继续下降时，test error 为什么可能上升？
2. Penalized objective 中 loss、penalty 与 $\lambda$ 各负责什么？
3. Coefficient magnitude 为什么影响 stability 与 generalization？
4. Ridge、lasso 与 bridge 的 penalty 有何关系？
5. **为什么 $L_1$ 容易产生 exact zeros，而 $L_2$ 通常只 shrink？**
6. Primal regularization 与 dual least-norm 的优化角色有何不同？
7. Primal / dual ridge 的 inverse 分别在哪个空间？
8. Ridge 的 $\lambda$ 增大时，fit 与 coefficient norm 怎样变化？
9. Bridge 中 $p$ 或 $k$ 怎样控制 sparsity / compression？
10. Proximal bridge 为什么要用 smooth approximation $\sqrt{w_j^2+\epsilon}$？
11. Multiple outputs 怎样从单输出解堆叠得到？
12. Coefficient profile 图应该怎样读？

---

## 十一、应试提醒

1. **先写 shape 再动笔**：见到 `P`，第一件事写下 $m \times (D+1)$，判断 over-/under-determined，再选 $(P^TP)^{-1}$ 还是 $(PP^T)^{-1}$。
2. **$\lambda I$ 加在**你正在求逆的那个矩阵上——primal 加在 $P^TP$，dual 加在 $PP^T$，别加错。
3. **AUC 的 $d_{ij}$ 是 negative 减 positive**（$p_j^- - p_i^+$），符号搞反整个解就错。
4. **AUC 的 tie 记 0.5**，不要记 0 或 1。
5. **shifted quadratic 必须有 offset $\eta$**：概念题常问"为什么不能直接用 $z^2$"——答"$z^2$ 对称，无法区分正确与错误方向"。
6. **TER 的两类各自除以自己的 $m$**，这是它对抗 class imbalance 的机制。
7. **$L_1$ 有尖角 → exact zeros；$L_2$ 光滑 → 只 shrink**。这是 L7 最高频的概念对比。
8. **$\lambda$ 不是越大越好**：过大会 underfit；必须用 validation / cross-validation 选，不能只看 training error。
9. **Ridge 不做 hard feature selection**，因为系数很少精确为 0。
10. **Coefficient profile 的 magnitude 不是因果重要性**：correlated variables 会互相替代。
11. **Bridge 只需记最终形式与行为，不要求推长公式**——但要知道 primal bridge 是 **implicit fixed-point**，需要迭代。
12. **读题注意 `incorrect` / `select one or more`**（同 Quiz 1 的英文读题陷阱）。
13. **课件 examples 与简单练习足够**：CA2 不考书末复杂计算，把 §八 的 8 道演练做熟即可。

---

## 十二、材料处理说明

本册对材料与已知边界的处理：

- **页码对应**：Cornell Notes 内文引用 `materials/EE6406-Lecture5-TKA-v2.pdf`，仓库内为 `week5/…-v1.pdf`；已逐页核对为同一份课件，公告中统一按仓库路径索引。课件页码 = 幻灯序号 + 1。
- **符号冲突**：Week 1 的 Mitchell 定义中 $P$ = performance measure，Week 3 之后 $P$ = design matrix，**只是碰巧使用同一字母**。
- **符号 $p$ / $k$**：L7 中 $p$（或 $k$）控制 penalty 形状，**不是 polynomial order**；读公式须按章节判断。
- **Closed form ≠ 零计算**：不等于真的在程序中显式计算 inverse；实际数值实现通常使用 QR、SVD 或 linear solve。考试推导仍按课件的 inverse 形式书写。
- **$k$-measure 的严格性**：L7 的 smooth operator 违反 absolute homogeneity，**不构成 normed vector space**，课件称其为 measure。
- **实验表格口径**：Prostate / XOR 表格中的数值（含括号内标准差）按课件保留，属**特定 split 与 tuned setting** 下的结果，不构成方法优劣的普遍结论。
- **考试边界**：CA2 scope 为 Lectures 5–7，以 concept 为主；TAUC 长式、bridge 长推导均**不要求死背**。

**主要来源**：`Quiz2/` 下 4 份 Cornell Notes PDF；`week5/EE6406-Lecture5-TKA-v1.pdf`、`week6/EE6406-Lecture6-TKA-v1.pdf`、`week7/EE6406-Lecture7-TKA-v1.pdf`。
