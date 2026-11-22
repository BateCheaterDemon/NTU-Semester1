# EE6222 Machine Vision — Final Exam Review（期末复习）

> **考试**：2026-11-24（周二），**3 小时**，**closed-book**，**4 道题、每题等分（25 分）、全部必答**。
>
> **命题地图（老师 Week 9 亲口公布）**：见下表。
>
> **明确不考**：Topic **1、2、4、6、7、8**（含 PCA / dimensionality reduction、统计估计、特征选择）。
>
> **老师的原话**："I will never test your skills, but I test your **understanding**." —— 考的是**原理与推导**，不是 corner case。Q4 更是 **"more on the concept, more on how you understand the questions"**，**千万不要留空**。

| 题号 | 来源 | 说明 |
|---|---|---|
| Q1 | Topic 3（Image Denoising and Enhancement） | 更偏 **enhancement**，不是 denoising |
| Q2 | Topic 5（MAP Decision and Classifiers） | MAP rule + 分类器设计 / 推导 |
| Q3 | Topic 9 + 10（Neural Network / CNN / Transformer） | 计算 + 矩阵形式 + 概念 |
| Q4 | Topic 11–14（Cheng Jun：Video + 3D） | 概念题，不考复杂计算 |

---

## 目录

1. 六套往年卷的命题规律（必读）
2. Q1 — Topic 3：Image Enhancement（图像增强）
3. Q2 — Topic 5：MAP Decision and Classifiers（MAP 决策与分类器）
4. Q3 — Topic 9+10：MLP / CNN / Transformer
5. Q4 — Topic 11–14：Video 与 3D（概念题）
6. 公式速查表（考前 30 分钟看这一页）
7. 最后 3 天复习计划
8. 模拟卷（4 题）＋ 答案要点

---

# 1. 六套往年卷的命题规律

> 6 套卷子（2023-24 S1/S2、2024-25 S1/S2、2025-26 S1/S2）的题目已逐页核对。**题型高度稳定**：Q1 算图像、Q2 推导概率/统计、Q3 算网络、Q4 答概念。

| 试卷 | Q1（图像） | Q2（概率/统计） | Q3（网络） | Q4（Cheng Jun） |
|---|---|---|---|---|
| 2023-24 S1 | histogram 由 δ 函数给出 → 求 c、γ 校正、直方图均衡 | 最小加权距离分类器 → 线性分类器 → 复杂度 | FC 层（参数量/乘加次数/矩阵形式）＋ CNN 层 | MEI/MHI、optical flow、cross-ratio、E/F 矩阵 |
| 2023-24 S2 | 8/4-connected component 提取算法 | 身高判性别：先验 + 高斯 → 决策与错误率 | 3×3 patch → FC 层 → 输出图像 | cross-ratio 计算、stereo 深度误差传播、LLVM |
| 2024-25 S1 | 由 impulse response 写 filter mask → 输出图像 → 语义 | 类条件均值/协方差 → 1D 特征方差推导 | MLP（画图/表达式/矩阵形式/反向传播） | ReID vs JDE、stereo pipeline、PSMNet cost volume |
| 2024-25 S2 | connected component（8/4） | 鱼的大小 PDF → 最小错误率决策 | 1×1 conv → 参数量 → 矩阵形式 | 生成模型（GAN/VAE）、stereo 概念 |
| 2025-26 S1 | 3×3 图像 2-bit → histogram / 幂变换 / 均衡化 | PCA 重构误差（今年不考） | 卷积核 → feature map + ReLU、Transformer attention | SIFT vs SuperPoint、stereo 步骤与挑战 |
| 2025-26 S2 | impulse response → mask → 横线/竖线响应 | PCA 方差/协方差/特征值（今年不考） | 1×1 conv → 矩阵形式 → CNN 与 Transformer 的关系 | GAN 目标/训练、stereo 系统设计 |

**三条结论**：

1. **每题内部都是 3–4 个小问、分数 4–13 分**——小问之间**层层递进**：先写公式，再代数字，再解释意义。
2. **"写出来"比"算出来"更重要**：Q2/Q3 大量要求 *derive / express in matrix form / show every step*，只给最终答案会丢过程分。
3. **2025-26 两套卷的 Q2 是 PCA**，那是**旧考纲**（当时 Topic 8 也在 Q2）；**今年老师已明确 Q2 = Topic 5，Topic 8 不考**——所以本文**不安排 PCA 主线**（只在 3.9 做一页对照，防止看旧卷时误解）。

## 1.1 评分点（从旧卷反推）

| 题型 | 必须写到的内容 |
|---|---|
| 直方图/变换 | 先写 $h(f)$ 表，再写累积 $c(f)$，再写映射 $g=T(f)$，最后写 $h_g(g)$ |
| 滤波器 | 先写 mask，再写 $g(x,y)=\sum\sum h f$，逐点算（写中间过程），最后解释语义 |
| MAP | 写 prior、class-conditional、posterior，再比较 joint；求错误率要写积分区间 |
| 网络 | 写维度、矩阵形状、参数量公式、乘加次数；反向传播写链式法则每一步 |
| 概念题 | 定义 → 原理/步骤 → 优缺点或对比 → 一句总结 |

---

# 2. Q1 — Topic 3：Image Enhancement

> **考法**：给一个小图像（3×3、6×6、9×9）或解析形式的 histogram / impulse response，让你**算并画**输出。
> **高频**：histogram、histogram equalization、power/gamma 变换、filter mask、卷积输出、平滑/锐化。

## 2.1 点处理（Point Processing）

点处理是**逐像素**的灰度映射 $g = T(f)$，与邻域无关。

| 变换 | 公式 | 作用 | 参数 |
|---|---|---|---|
| Negative（反相） | $g = L - f$ | 反转明暗 | $L$ = 最大灰度 |
| Log transformation | $g = c\,\log(1+f)$ | 压缩高灰度、拉伸低灰度 | $c = L/\log(1+L)$ |
| Power / Gamma correction | $g = c\,f^{\gamma}$ | $\gamma<1$ 提亮暗部；$\gamma>1$ 压暗 | 常取 $c=1$ |
| Piecewise linear | 分段线性（见下） | 拉伸关心的灰度区间 | $a,b,\alpha,\beta,\gamma$ |

**Contrast stretching（分段线性）**：

$$
g = T(f) =
\begin{cases}
\alpha f, & 0 \le f < a \\[2pt]
\beta (f-a) + T(a), & a \le f < b \\[2pt]
\gamma (f-b) + T(b), & b \le f \le L
\end{cases}
$$

**考试写法**：先写 $g=T(f)$，再把 $f$ 的所有可能取值**列成表**逐个映射，最后按新值**重画 histogram**。

## 2.2 Histogram 与 Histogram Equalization（重点）

### 2.2.1 定义

- **Histogram** $h(f)$：灰度级 $f$ 出现的**像素个数**；
- **Normalized histogram**：

$$
p_f(f) = \frac{h(f)}{n}, \qquad n = \text{总像素数}
$$

- 性质：$\sum_f h(f) = n$，$\sum_f p_f(f) = 1$。

### 2.2.2 均衡化算法（课件原式，务必按这个写）

$$
c(f) = \sum_{t=0}^{f} p_f(t) = \frac{1}{n}\sum_{t=0}^{f} n_t
$$

$$
g = T(f) = \operatorname{round}\!\left(\frac{c(f)-c_{\min}}{1-c_{\min}}\,L\right)
$$

- $c_{\min}$ = 所有 $c(f)$ 中的**最小值**（对应图像里最小的灰度级）；
- $L$ = **最大灰度级**（8-bit 图 $L=255$；2-bit 图 $L=3$；归一化图 $L=1$）；
- $\operatorname{round}[\cdot]$ 取整；这样得到的 $g$ **近似均匀分布**在 $[0,L]$。

**为什么能均匀**（连续情形，考点）：

$$
g = T(f) = \int_0^f p_f(t)\,dt \quad (\text{即 CDF})
$$

$$
p_g(g) = p_f(f)\left|\frac{df}{dg}\right|,
\qquad
\frac{dg}{df} = p_f(f)
\;\Longrightarrow\;
p_g(g) = \frac{p_f(f)}{p_f(f)} = 1
$$

> **结论**：CDF 作为变换函数，把任意分布变成均匀分布。

### 2.2.3 例题 A（2025-26 S1 Q1 原题）：3×3、2-bit

图像（灰度 0–3）：

$$
F =
\begin{bmatrix}
1 & 2 & 0 \\
1 & 3 & 1 \\
0 & 2 & 1
\end{bmatrix}
$$

**Step 1：histogram**

| $f$ | 0 | 1 | 2 | 3 | 合计 |
|---|---|---|---|---|---|
| $h(f)$ | 2 | 4 | 2 | 1 | 9 |
| $p_f(f)$ | 2/9 | 4/9 | 2/9 | 1/9 | 1 |

**Step 2：CDF**

$$
c(0)=\frac{2}{9},\quad
c(1)=\frac{6}{9},\quad
c(2)=\frac{8}{9},\quad
c(3)=1,
\qquad c_{\min}=\frac{2}{9},\ L=3
$$

**Step 3：映射** $g=\operatorname{round}\!\left(\dfrac{c-c_{\min}}{1-c_{\min}}\cdot 3\right)$

| $f$ | $c(f)$ | $\dfrac{c-c_{\min}}{1-c_{\min}}$ | $\times 3$ | $g$ |
|---|---|---|---|---|
| 0 | 2/9 | 0 | 0 | 0 |
| 1 | 6/9 | 4/7 | 12/7 ≈ 1.71 | 2 |
| 2 | 8/9 | 6/7 | 18/7 ≈ 2.57 | 3 |
| 3 | 1 | 1 | 3 | 3 |

**Step 4：输出图像与 histogram**

$$
F \;\longrightarrow\; G =
\begin{bmatrix}
2 & 3 & 0 \\
2 & 3 & 2 \\
0 & 3 & 2
\end{bmatrix}
$$

新 histogram：$h_g(0)=2,\ h_g(2)=4,\ h_g(3)=3$（原来集中在 1，现在被"摊开"到 2、3）。

### 2.2.4 例题 B（同题 (b)）：幂变换 $T(f)=\tfrac{1}{3}f^2$

逐灰度映射（再量化到 2 bit，即 0–3）：

| $f$ | $\tfrac{1}{3}f^2$ | round | $g$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 1 | 1/3 ≈ 0.33 | 0 | 0 |
| 2 | 4/3 ≈ 1.33 | 1 | 1 |
| 3 | 3 | 3 | 3 |

$$
G =
\begin{bmatrix}
0 & 1 & 0 \\
0 & 3 & 0 \\
0 & 1 & 0
\end{bmatrix},
\qquad
h_g(0)=6,\ h_g(1)=2,\ h_g(3)=1
$$

**观察**：$\gamma=2>1$ 把**低灰度压得更低**（1→0），这是 gamma 校正"压暗"的典型效果；而均衡化是把 histogram **拉平**，两者目的不同。

### 2.2.5 例题 C（2023-24 S1 Q1）：histogram 用 δ 函数给出

$$
P_{of}(f) = 0.2\,\delta[f-0.7] + 0.1\,\delta[f] + 0.3\,\delta[f-0.8]
+ c\,\delta[f-1] + 0.2\,\delta[f-0.9]
$$

| 小问 | 做法 |
|---|---|
| (a) 求 $f_{\min}$、$f_{\max}$、灰度级个数 | δ 的位置就是出现过的灰度级：0, 0.7, 0.8, 0.9, 1 ⇒ $f_{\min}=0$，$f_{\max}=1$，共 **5** 个 |
| (b) 求 $c$ 并画 histogram | 概率和 = 1：$0.2+0.1+0.3+c+0.2=1$ ⇒ $c=0.2$ |
| (c) $\gamma$ 校正 $g=f^2$ 后的 histogram | 每个 δ 搬到 $f^2$：0→0，0.7→0.49，0.8→0.64，0.9→0.81，1→1；概率质量不变 |
| (d) 均衡化后的 histogram | $c(f)$ 是阶梯累积；$g=\dfrac{c-c_{\min}}{1-c_{\min}}L$；把每个灰度的概率质量整体搬到新灰度 |

> **关键理解**：变换直方图就是**把每个灰度的概率质量整体搬到新灰度**；多个 $f$ 映射到同一个 $g$ 时，概率**相加**。

## 2.3 线性滤波（LSI / Convolution）

### 2.3.1 公式（课件写法）

$$
g(x,y) = f(x,y) * h(x,y) = \sum_{j}\sum_{i} h(i,j)\,f(x-i,\,y-j)
$$

- $h$ 是 **filter mask（kernel）**，尺寸通常 3×3、5×5；
- 对每个像素，把 mask **翻转后**与邻域**逐点相乘再求和**（数学卷积要翻转；CNN 里实际用 cross-correlation，**不翻转**）；
- 频域：$G(u,v) = F(u,v)\,H(u,v)$。

### 2.3.2 常见 mask

| 类型 | Mask | 说明 |
|---|---|---|
| 平均（box）滤波 | $\frac{1}{9}\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}$ | 平滑、去噪，但模糊边缘 |
| 高斯滤波 | 权重按距离衰减，总和为 1 | 平滑更自然，无振铃 |
| Laplacian（锐化） | $\begin{bmatrix}0&1&0\\1&-4&1\\0&1&0\end{bmatrix}$ 或 $\begin{bmatrix}1&1&1\\1&-8&1\\1&1&1\end{bmatrix}$ | 二阶微分，响应边缘 |
| Sobel（x 方向） | $\begin{bmatrix}-1&0&1\\-2&0&2\\-1&0&1\end{bmatrix}$ | 一阶微分，检测竖直边缘 |
| Sobel（y 方向） | $\begin{bmatrix}-1&-2&-1\\0&0&0\\1&2&1\end{bmatrix}$ | 检测水平边缘 |

**High-boost（unsharp masking）**：

$$
f_{hb} = A f - f_{lp} = (A-1)f + (f-f_{lp}) = (A-1)f + f_{hp},
\qquad A \ge 1
$$

### 2.3.3 从 impulse response 写 mask（2024-25 S1、2025-26 S2 题型）

**规则**：$h(x,y)=\sum_k a_k\,\delta(x-x_k,\,y-y_k)$ 中，**每个 δ 的系数 $a_k$ 就填在 mask 的对应位置**（mask 坐标以中心为 $(0,0)$）。

**例 1（2024-25 S1）**：

$$
h(x,y) = 2\delta(x,y) - \delta(x,y-1) - \delta(x-1,y)
$$

- $2\delta(x,y)$ → 中心 $(0,0)=2$；
- $-\delta(x,y-1)$：$y-1=0\Rightarrow y=1$ → 位置 $(0,1)=-1$（下方一格）；
- $-\delta(x-1,y)$：$x=1$ → 位置 $(1,0)=-1$（右方一格）。

$$
H =
\begin{bmatrix}
0 & 0 & 0 \\
0 & 2 & -1 \\
0 & -1 & 0
\end{bmatrix}
$$

**语义**：这是一个**方向性边缘检测器**——对上方/左方的灰度跳变有响应（减的是 $y+1$、$x+1$ 方向）。所以对"constant background 上的方块"，输出是**方块的右上边界**（一条 L 形边缘）；取绝对值或加偏移可让边缘更清楚。

**例 2（2025-26 S2）**：

$$
\begin{aligned}
h ={}& 4\delta(x,y) + 2\delta(x-1,y) + 2\delta(x+1,y) \\
&- 2\delta(x,y-1) - 2\delta(x,y+1) \\
&- \delta(x-1,y-1) - \delta(x+1,y-1) - \delta(x-1,y+1) - \delta(x+1,y+1)
\end{aligned}
$$

$$
H =
\begin{bmatrix}
-1 & -2 & -1 \\
2 & 4 & 2 \\
-1 & -2 & -1
\end{bmatrix}
$$

- 系数和 $=4+2+2-2-2-1-1-1-1=0$ ⇒ **zero-sum = high-pass**；
- 对**水平亮线**：上下两行为负、中间行为正 ⇒ 亮线处**正响应**、两侧**负响应**；
- 对**竖直亮线**：同理，方向转 90°。

### 2.3.4 卷积输出怎么算（逐点写，别跳步）

以 3×3 mask 为例：

$$
g(x,y)=\sum_{m=-1}^{1}\sum_{l=-1}^{1} h(l,m)\,f(x-l,\,y-m)
$$

**考试技巧**：

1. 先把 mask 写整齐，**标出中心**；
2. 对每个输出位置，把 3×3 邻域**抄成一个 3×3 小表**；
3. 对应位置相乘再相加（**写出乘加式**，便于拿过程分）；
4. 边界处理：题目若说 "out of the image is constant $c$"，就用 $c$ 补边；若说 zero padding，就补 0。

## 2.4 平滑 vs 锐化 vs 非线性

| 类别 | 代表 | 作用 | 缺点 |
|---|---|---|---|
| Low-pass（平滑） | 均值、Gaussian | 去噪、模糊 | 边缘也模糊；对椒盐噪声效果差 |
| High-pass（锐化） | Laplacian、Sobel、high-boost | 增强边缘/细节 | 放大噪声 |
| Order-statistic | Median filter | 去椒盐噪声、保边 | 对高斯噪声不如均值 |

**Median 例题**（课件）：邻域 $(10,15,20,20,20,20,20,25,100)$ 排序后中位数 $20$ ⇒ 把中心像素 $15$ 替换为 $20$。

> **一句话解释**：线性滤波的输出是邻域的加权平均，所以强噪声（如 100）会被"平均"进结果，且边缘被抹平；中值滤波取排序中间值，离群点直接被丢掉。

## 2.5 Q1 答题模板

1. 写变换/滤波公式，定义所有符号（$f,g,h,L,c(f)$）；
2. 列表算 $h(f)$、$p(f)$、$c(f)$（或写 mask）；
3. 逐点/逐灰度求 $g$（写出算式，保留分数）；
4. 画输出图像 / 新 histogram（标清坐标轴）；
5. 一句话解释结果（均匀化 / 增强暗部 / 检出某方向边缘 / 去椒盐噪声）。

---

# 3. Q2 — Topic 5：MAP Decision and Classifiers

> **考法**：给 prior + class-conditional PDF（高斯或分段线性）→ 求**决策规则**与**错误率**；或给一个 discriminant function → 推导它等价于 MAP / 最小距离；或推导**加权距离分类器**。
> **核心**：MAP 最小化错误率；高斯假设下判别函数 → Mahalanobis 距离 → 线性分类器。

## 3.1 基本概率量

| 量 | 记号 | 含义 |
|---|---|---|
| Prior | $P(\omega_i)$ | 未看数据前，类 $i$ 的概率 |
| Class-conditional density | $p(x \mid \omega_i)$ | 类 $i$ 中观测到 $x$ 的密度（likelihood） |
| Posterior | $P(\omega_i \mid x)$ | 看了 $x$ 后，属于类 $i$ 的概率 |
| Evidence / mixture | $p(x)=\sum_i p(x\mid\omega_i)P(\omega_i)$ | $x$ 的总密度（对所有类相同） |

**Bayes 公式**：

$$
P(\omega_i \mid x) = \frac{p(x \mid \omega_i)\,P(\omega_i)}{p(x)}
$$

## 3.2 MAP 决策规则

$$
\omega_k = \arg\max_i P(\omega_i \mid x)
= \arg\max_i \big[\,p(x\mid\omega_i)\,P(\omega_i)\,\big]
= \arg\max_i \big[\,\ln p(x\mid\omega_i) + \ln P(\omega_i)\,\big]
$$

（分母 $p(x)$ 与类无关，可去掉；取对数单调不变。）

**为什么最优（必背三行）**：

$$
P(\text{correct}\mid x)=P(\omega_k\mid x),
\qquad
P(\text{error}\mid x)=1-P(\omega_k\mid x)
$$

选 posterior 最大的类 ⇒ 每个 $x$ 上的 error 最小 ⇒ **积分后的总错误率也最小**。

**总错误率**：

$$
p(e) = \int p(e\mid x)\,p(x)\,dx
= 1 - \sum_i P(\omega_i)\int_{\mathcal{R}_i} p(x\mid\omega_i)\,dx
$$

其中 $\mathcal{R}_i$ 是判为类 $i$ 的**决策区域**。二类时：

$$
p(e) = P(\omega_1)\int_{\mathcal{R}_2} p(x\mid\omega_1)\,dx
+ P(\omega_2)\int_{\mathcal{R}_1} p(x\mid\omega_2)\,dx
$$

> 直观：**类 1 的样本落进类 2 的区域 + 类 2 的样本落进类 1 的区域**，各自乘 prior。

## 3.3 判别函数（Discriminant Function）

定义 $g_i(x) = \ln p(x\mid\omega_i) + \ln P(\omega_i)$，判给 $\arg\max_i g_i(x)$。

### 3.3.1 多维高斯情形（课件推导）

$$
p(x\mid\omega_i) =
\frac{1}{(2\pi)^{d/2}\,|\Sigma_i|^{1/2}}
\exp\!\left[-\frac{1}{2}(x-\mu_i)^{T}\Sigma_i^{-1}(x-\mu_i)\right]
$$

取对数：

$$
g_i(x) = -\frac{1}{2}(x-\mu_i)^{T}\Sigma_i^{-1}(x-\mu_i)
-\frac{1}{2}\ln|\Sigma_i| + \ln P(\omega_i) - \frac{d}{2}\ln(2\pi)
$$

去掉与 $i$ 无关的常数项：

$$
g_i(x) = -\frac{1}{2}\,d_{\Sigma_i}(x,\mu_i) + b_i,
\qquad
b_i = \ln P(\omega_i) - \frac{1}{2}\ln|\Sigma_i|
$$

其中

$$
d_{\Sigma_i}(x,\mu_i) = (x-\mu_i)^{T}\Sigma_i^{-1}(x-\mu_i)
$$

是 **Mahalanobis 距离的平方**。

**Mahalanobis vs Euclidean**：

$$
d_{Eu}(x,\mu) = (x-\mu)^{T}(x-\mu),
\qquad
d_{\Sigma}(x,\mu) = (x-\mu)^{T}\Sigma^{-1}(x-\mu)
$$

1D 时：$d_{Eu}=(x-\mu)^2$，$d_{\Sigma}=(x-\mu)^2/\sigma^2$。

### 3.3.2 特例 1：所有类协方差相同 $\Sigma_i=\Sigma$ → 线性分类器

$$
\begin{aligned}
g_i(x) &= -\frac{1}{2}(x-\mu_i)^{T}\Sigma^{-1}(x-\mu_i) + \ln P(\omega_i) \\
&= \mu_i^{T}\Sigma^{-1}x - \frac{1}{2}\mu_i^{T}\Sigma^{-1}\mu_i + \ln P(\omega_i)
\end{aligned}
$$

（丢掉与 $i$ 无关的 $x^{T}\Sigma^{-1}x$ 项。）

$$
g_i(x) = w_i^{T}x + w_{i0},
\qquad
w_i = \Sigma^{-1}\mu_i,
\quad
w_{i0} = -\frac{1}{2}\mu_i^{T}\Sigma^{-1}\mu_i + \ln P(\omega_i)
$$

两类边界 $g_i=g_j$：

$$
(\mu_i-\mu_j)^{T}\Sigma^{-1}x
-\frac{1}{2}\left(\mu_i^{T}\Sigma^{-1}\mu_i-\mu_j^{T}\Sigma^{-1}\mu_j\right)
+\ln\frac{P(\omega_i)}{P(\omega_j)} = 0
$$

⇒ **超平面**；当先验相等且 $\Sigma$ 相同时，它**垂直于两类均值连线**。

### 3.3.3 特例 2：$\Sigma_i=\sigma^2 I$ → 最小距离分类器

$$
g_i(x) = -\frac{1}{2\sigma^{2}}(x-\mu_i)^{T}(x-\mu_i) + \ln P(\omega_i)
$$

若**先验全部相等**，$\ln P(\omega_i)$ 相同 ⇒ 等价于**最小化欧氏距离**：

$$
g_i(x) = -\|x-\mu_i\|^{2}
\quad\Longrightarrow\quad
\text{decide the nearest mean}
$$

这就是 **template matching** 的理论基础：把每个类的均值当作"模板"，看输入离谁最近。

## 3.4 例题 1：鱼的尺寸（2024-25 S2 Q2）

设定：类 $\omega_1$ 有 40 条、$\omega_2$ 有 60 条，即

$$
P(\omega_1)=0.4,\qquad P(\omega_2)=0.6
$$

两个 PDF 是**分段直线**（图给出）。

**决策规则（最小错误率）**：比较 **joint**：

$$
P(\omega_1)\,p(x\mid\omega_1)
\quad\text{vs.}\quad
P(\omega_2)\,p(x\mid\omega_2)
$$

- 两条曲线的交点 $x^{*}$ 就是**阈值**；
- **注意先验**：若只比较 $p(x\mid\omega)$ 而忽略先验，阈值会偏——这是最常见的失分点。

**错误率**：

$$
p(e) = P(\omega_1)\int_{x>x^{*}} p(x\mid\omega_1)\,dx
+ P(\omega_2)\int_{x<x^{*}} p(x\mid\omega_2)\,dx
$$

分段直线 PDF 的积分 = **三角形/梯形面积**：

$$
\int p(x)\,dx = \tfrac{1}{2}\times\text{底}\times\text{高}
$$

> 考试时把面积算式写清楚（底、高各是多少），比只写数字更稳。

## 3.5 例题 2：身高判性别（2023-24 S2 Q2）

| 小问 | 做法 |
|---|---|
| (a) 只知道 300 男 / 700 女 | $P(\omega_1)=0.3,\ P(\omega_2)=0.7$，**只比 prior** ⇒ 判女；错误率 $=\min(0.3,0.7)=0.3$ |
| (b) 男女各半，均值 1.7 / 1.62 | 先验相同 ⇒ 比较 $p(x\mid\omega_1)$ 与 $p(x\mid\omega_2)$；方差相同则阈值 $=(1.7+1.62)/2=1.66$；$x=1.67$ ⇒ 判男 |
| (c) 300 男 / 700 女，$\sigma_1=0.2,\ \sigma_2=0.3$ | 解 $P(\omega_1)N(x;1.7,0.2^2)=P(\omega_2)N(x;1.62,0.3^2)$；方差不同 ⇒ 二次方程，取合理根作阈值；再积分求错误率 |

**等方差时的闭式阈值**（必背）：

$$
x^{*} = \frac{\mu_1+\mu_2}{2}
+ \frac{\sigma^{2}}{\mu_2-\mu_1}\ln\frac{P(\omega_2)}{P(\omega_1)}
$$

- 先验相等 ⇒ 第二项为 0 ⇒ 阈值 = **均值中点**；
- 若 $P(\omega_2)>P(\omega_1)$（女多）⇒ 阈值**往男那边移**，更容易判女。

**错误率（等方差、用 Q 函数）**：

$$
p(e) = P(\omega_1)\,Q\!\left(\frac{x^{*}-\mu_1}{\sigma}\right)
+ P(\omega_2)\,Q\!\left(\frac{\mu_2-x^{*}}{\sigma}\right),
\qquad
Q(z)=1-\Phi(z)
$$

## 3.6 例题 3：最小加权距离分类器（2023-24 S1 Q2）

题目给的判别函数：

$$
g_i(x) = -\sum_{j=1}^{n}\frac{(x_j-\mu_{ij})^{2}}{\sigma_{ij}^{2}} + c_i
$$

**理解**：这是**各特征独立、方差不同**的高斯情形（$\Sigma_i$ 为对角阵 $\operatorname{diag}(\sigma_{i1}^{2},\dots,\sigma_{in}^{2})$）。代入高斯判别函数：

$$
g_i(x) = -\frac{1}{2}\sum_j\frac{(x_j-\mu_{ij})^{2}}{\sigma_{ij}^{2}}
-\frac{1}{2}\sum_j\ln\sigma_{ij}^{2} + \ln P(\omega_i)
$$

题目把 $-\tfrac{1}{2}$ 缩放、把常数并入 $c_i$，就得到题给形式。**它等价于 MAP（在高斯 + 独立假设下）**。

**(a) 什么时候它最小化错误率？** 当 $p(x\mid\omega_i)$ 确实是**独立高斯**、且 $c_i$ 取 $-\tfrac{1}{2}\sum\ln\sigma_{ij}^{2}+\ln P(\omega_i)$ 时，$g_i$ 就是对数 posterior（差一个常数），$\arg\max$ 即 MAP。

**(b) 推导线性分类器**：若**所有类的方差相同** $\sigma_{ij}^{2}=\sigma_j^{2}$（与 $i$ 无关），则

$$
g_i(x) = -\sum_j\frac{x_j^{2}-2x_j\mu_{ij}+\mu_{ij}^{2}}{\sigma_j^{2}} + c_i
$$

$-\sum_j x_j^{2}/\sigma_j^{2}$ 与 $i$ 无关，丢掉后：

$$
g_i(x) = \sum_j \frac{\mu_{ij}}{\sigma_j^{2}}x_j
- \sum_j \frac{\mu_{ij}^{2}}{2\sigma_j^{2}} + c_i'
= w_i^{T}x + w_{i0}
$$

$$
w_i = \left[\frac{\mu_{i1}}{\sigma_1^{2}},\ \dots,\ \frac{\mu_{in}}{\sigma_n^{2}}\right]^{T}
$$

⇒ **线性判别函数**（超平面边界）。

**(c) 复杂度对比**：

| 方法 | 训练阶段 | 分类阶段 |
|---|---|---|
| 加权距离（二次） | 只需估 $\mu_{ij},\sigma_{ij}$，$O(nc)$ | 每个样本 $O(nc)$ 乘加，无矩阵求逆 |
| 线性（等方差） | 同样估 $\mu,\sigma$，$O(nc)$ | $O(nc)$，更快（少一次平方） |
| 全协方差高斯 | 估 $\Sigma_i$ 并求逆，$O(n^3)$ | 每个样本 $O(n^2)$ |

## 3.7 补充：如果题目给的是 joint 而不是 posterior

- **比较 posterior**：$P(\omega_i\mid x)$；
- **比较 joint**：$p(x,\omega_i)=P(\omega_i)\,p(x\mid\omega_i)$；
- 两者**只差分母 $p(x)$**（与类无关）⇒ **决策结果完全相同**；
- 计算时**优先用 joint**，避免算 $p(x)$。

## 3.8 错误率的三种算法（按题目给的形式选）

| 题目给的形式 | 算法 |
|---|---|
| 离散 PDF（表格/δ） | 求和：$p(e)=\sum$ 落在错误区域的概率 |
| 分段直线 PDF | 求交点 → 算三角形/梯形面积 |
| 高斯 PDF | 化作 Q 函数：$Q(z)=1-\Phi(z)$；等方差用 3.5 的闭式 |

## 3.9 对照：2025-26 卷子的 PCA 题（今年不考，但别被旧卷误导）

旧卷 Q2 考过 PCA：

$$
y = W^{T}x,
\qquad
\hat{x} = Wy = WW^{T}x
$$

$$
e^{2} = \|\hat{x}-x\|^{2} = x^{T}(I-WW^{T})x
$$

以及 $b=w^{T}x$ 的方差 $\sigma^{2}=w^{T}\Sigma w$、协方差 $\Sigma=\frac{1}{n}\sum(x-\mu)(x-\mu)^{T}$、特征方程 $\Sigma\phi=\lambda\phi$。

> **今年不考 Topic 8**（老师明确列为不考）；这一小节只用于**看懂旧卷**，不要花时间。

## 3.10 Q2 答题模板

1. 写 $P(\omega_i)$ 与 $p(x\mid\omega_i)$，写出 Bayes 公式；
2. 写 MAP 规则（$\arg\max$ posterior = $\arg\max$ joint）；
3. 求阈值：令两个 joint 相等，解 $x^{*}$（高斯要开方/配方，注意先验项）；
4. 写错误率积分（标清区域），代 PDF 算面积或 Q 函数；
5. 若要求推导分类器：写判别函数 → 取对数 → 丢常数 → 写成 $w^{T}x+w_0$；
6. 一句话说明假设（等方差？先验相等？独立？）。

---

# 4. Q3 — Topic 9+10：MLP / CNN / Transformer

> **考法**：给网络结构（层数、神经元数、卷积核、输入尺寸），要求 ① 写前向表达式 ② 写成矩阵形式 ③ 算参数量/乘加次数 ④ 推导反向传播 ⑤ 解释 CNN/Transformer 的关系。
> **技巧**：所有答案都先写**维度**，再写**矩阵形状**，最后代入数字。

## 4.1 MLP 前向传播

### 4.1.1 标量形式（两层，2 输入、2 隐层、1 输出）

$$
\begin{aligned}
h_1 &= f(w_{11}x_1 + w_{12}x_2 + b_1)\\
h_2 &= f(w_{21}x_1 + w_{22}x_2 + b_2)\\
y &= g(v_1h_1 + v_2h_2 + c)
\end{aligned}
$$

sigmoid：

$$
f(s) = \frac{1}{1+e^{-s}}
$$

### 4.1.2 矩阵形式（必考）

$$
o = W^{T}x + b,
\qquad
h = f(W^{T}x+b),
\qquad
y = g(V^{T}h+c)
$$

- $x\in\mathbb{R}^{n_{in}}$，$W\in\mathbb{R}^{n_{in}\times n_{hidden}}$，$V\in\mathbb{R}^{n_{hidden}\times n_{out}}$；
- 加深：$x^{(k+1)}=f(W_k^{T}x^{(k)}+b_k)$，$y=g(W_m^{T}x^{(m)}+b_m)$。

### 4.1.3 参数量与计算量

$$
\text{参数} = (n_{in}+1)\,n_{out},
\qquad
\text{乘法} \approx n_{in}n_{out},
\qquad
\text{加法} \approx (n_{in}-1)n_{out}+n_{out}
$$

**例（2023-24 S1 Q3a）**：$x\in\mathbb{R}^{100}\to y\in\mathbb{R}^{98}$，线性层：

- 参数 $W$：$98\times100=9800$，bias $98$ ⇒ 共 **9898**；
- 乘法 $100\times98=9800$；加法 $99\times98+98=9800$；
- 输出数/参数数 $=98/9898\approx0.0099$。

## 4.2 反向传播（Backpropagation）

### 4.2.1 平方误差 + 链式法则

$$
E=\tfrac{1}{2}(t-y)^{2},
\qquad
y=g(s),\quad s=V^{T}h+c,
\qquad
h=f(u),\quad u=W^{T}x+b
$$

**输出层**：

$$
\frac{\partial E}{\partial y}=-(t-y),
\qquad
\frac{\partial E}{\partial s}=-(t-y)\,g'(s)
$$

$$
\frac{\partial E}{\partial V}=\frac{\partial E}{\partial s}\,h,
\qquad
\frac{\partial E}{\partial c}=\frac{\partial E}{\partial s}
$$

**隐藏层**：

$$
\frac{\partial E}{\partial h}=\frac{\partial E}{\partial s}\,V,
\qquad
\frac{\partial E}{\partial u}=\frac{\partial E}{\partial h}\odot f'(u)
$$

$$
\frac{\partial E}{\partial W}=\frac{\partial E}{\partial u}\,x^{T},
\qquad
\frac{\partial E}{\partial b}=\frac{\partial E}{\partial u}
$$

**更新**：

$$
V \leftarrow V-\eta\frac{\partial E}{\partial V},
\qquad
W \leftarrow W-\eta\frac{\partial E}{\partial W}
$$

**只要求更新输出层权重**时（2024-25 S1 Q3d）：

$$
\Delta v_j = \eta\,(t-y)\,g'(s)\,h_j,
\qquad
\Delta c = \eta\,(t-y)\,g'(s)
$$

其中 $g'(s)=1$（线性输出），或 $g'(s)=y(1-y)$（sigmoid 输出）。

### 4.2.2 为什么要非线性激活

- 若 $f$ 是线性，多层复合仍是**线性变换** ⇒ 等价于单层；
- 非线性（sigmoid/ReLU）才使 MLP 能逼近任意连续函数（universal approximation）。

## 4.3 CNN 前向与计算（高频）

### 4.3.1 卷积层公式（课件原式）

输入 $P\times Q\times C$，输出 $P\times Q\times D$（same padding，stride 1，3×3 核）：

$$
y_{i,j,k} = \sum_{n=1}^{C}\sum_{m=-1}^{1}\sum_{l=-1}^{1}
w_{l,m,n,k}\,x_{i-l,\,j-m,\,n} + b_k
$$

- $w_{l,m,n,k}$：第 $k$ 个 filter、通道 $n$、偏移 $(l,m)$ 的权重；
- $b_k$：第 $k$ 个 filter 的 bias；
- **每个输出通道 $k$ 都对所有输入通道 $n$ 求和** ⇒ 通道间全连接（这是 1×1 卷积有意义的根本原因）。

### 4.3.2 输出尺寸与参数量

**Valid convolution（无 padding）**：

$$
W_{out} = \frac{W_{in}-F}{S}+1,
\qquad
H_{out} = \frac{H_{in}-F}{S}+1
$$

**Same padding（stride 1）**：$P=(F-1)/2$ ⇒ 输出尺寸不变。

**参数量**：

$$
F\cdot F\cdot C\cdot D + D
$$

（$F\times F$ 核、$C$ 输入通道、$D$ 输出通道；$+D$ 是 bias。）

**乘加次数**（每个输出点）：

$$
F\cdot F\cdot C \ \text{次乘法} + (F\cdot F\cdot C-1)\ \text{次加法},
\quad \text{再乘 } D\,H_{out}W_{out}
$$

### 4.3.3 例题 A（2025-26 S1 Q3）：6×6 图像 + 3×3 核

核（**中心对称**，所以 convolution 与 cross-correlation 结果相同）：

$$
K =
\begin{bmatrix}
-1 & 1 & -1\\
1 & 1 & 1\\
-1 & 1 & -1
\end{bmatrix}
$$

图像：

$$
F =
\begin{bmatrix}
2&2&2&0&2&0\\
2&2&2&0&2&0\\
2&2&2&0&0&0\\
0&0&0&0&2&0\\
2&2&0&2&2&2\\
2&2&0&0&2&0
\end{bmatrix}
$$

**(a) bias = 0：先算 4×4 卷积，再 ReLU**

$$
\text{conv} =
\begin{bmatrix}
2 & 4 & -2 & 4\\
4 & 4 & -4 & 4\\
-2 & -4 & 0 & 0\\
4 & 2 & 0 & 10
\end{bmatrix}
\qquad
\xrightarrow{\text{ReLU}}
\qquad
\begin{bmatrix}
2 & 4 & 0 & 4\\
4 & 4 & 0 & 4\\
0 & 0 & 0 & 0\\
4 & 2 & 0 & 10
\end{bmatrix}
$$

手算示范（左上角输出，窗口为图像左上 3×3）：

$$
(-1)2+(1)2+(-1)2 = -2,
$$
$$
(1)2+(1)2+(1)2 = 6,
$$
$$
(-1)2+(1)2+(-1)2 = -2
\;\Longrightarrow\; -2+6-2 = 2
$$

再举一个**跨过亮暗边界**的例子（输出第 1 行第 3 列，窗口为第 1–3 行、第 3–5 列）：

$$
\begin{bmatrix}2&0&2\\2&0&2\\2&0&0\end{bmatrix}
\;\Longrightarrow\;
-4+4-2=-2 \;\xrightarrow{\text{ReLU}}\; 0
$$

> **教训**：先把 3×3 窗口**完整抄下来**（看清边界处取 0 还是 2），再逐行乘加。

**(b) bias = −5：先加 bias 再 ReLU**

$$
\text{conv}+(-5)=
\begin{bmatrix}
-3&-1&-7&-1\\
-1&-1&-9&-1\\
-7&-9&-5&-5\\
-1&-3&-5&5
\end{bmatrix}
\qquad
\xrightarrow{\text{ReLU}}
\qquad
\begin{bmatrix}
0&0&0&0\\
0&0&0&0\\
0&0&0&0\\
0&0&0&5
\end{bmatrix}
$$

> **重要特征**：绝大多数输出被压成 0 ⇒ **ReLU 的稀疏性（sparsity）**：只有少数强响应通过，减少计算、抑制噪声、让特征更稀疏可分。也可答：**bias 相当于阈值，控制神经元的激活门槛**。

### 4.3.4 例题 B（2023-24 S1 Q3）：FC vs Conv 参数量

| 指标 | FC（100→98） | Conv（20 个 3×3 filter，输入 3 通道） |
|---|---|---|
| 参数量 | $(100+1)\times98=9898$ | $20\times(3\cdot3\cdot3+1)=560$ |
| 乘法 | $100\times98=9800$ | 每个输出点 $3\cdot3\cdot3=27$ 次 |
| 输出/参数比 | $98/9898\approx0.0099$ | $(20HW)/560$ |

> **结论**：卷积用参数共享把参数量降了约 18 倍，且对平移鲁棒。

### 4.3.5 1×1 卷积 = 通道间的矩阵乘法（高频）

对每个空间位置 $(i,j)$，把所有通道的像素排成向量 $x_{ij}\in\mathbb{R}^{C}$：

$$
y_{ij} = W^{T}x_{ij}+b,
\qquad
W\in\mathbb{R}^{C\times D}
$$

- 参数量：$C\cdot D+D$；
- **等价于对每个像素做一次 FC**（通道维度全连接，空间维度共享权重）；
- 把整幅图拉平成矩阵 $X\in\mathbb{R}^{(HW)\times C}$，则 $Y=XW+\mathbf{1}b^{T}$，$Y\in\mathbb{R}^{(HW)\times D}$。

**例题（2024-25 S2 Q3）**：$p$ 个输入通道、$q$ 个输出通道、1×1 卷积：

$$
y_{i,j,k} = \sum_{n=1}^{p} w_{n,k}\,x_{i,j,n}+b_k
$$

$$
\text{参数} = pq+q,
\qquad
\text{乘法} = pq\,(mn),
\qquad
\text{加法} = (p-1)q\,(mn)+q\,(mn)
$$

矩阵形式：$Y=XW+\mathbf{1}b^{T}$，$X\in\mathbb{R}^{(mn)\times p}$，$W\in\mathbb{R}^{p\times q}$。

### 4.3.6 CNN 为什么是"正则化的 MLP"（课件观点）

- 把卷积写成矩阵：$W$ 是**稀疏 + 每行权重相同**（Toeplitz/循环结构）；
- 每个可学习参数**经过所有像素** ⇒ 学到的是**全局通用规则**，不是局部细节 ⇒ **泛化好、抗过拟合**；
- 这也是为什么 filter 用 **3×3 或 1×1**（保证参数覆盖所有位置），并且要 **deep**（堆叠扩大感受野）。

## 4.4 Transformer 与 Attention

### 4.4.1 Q/K/V 的生成（课件原式）

输入矩阵 $X\in\mathbb{R}^{N\times d}$（$N$ 个 token，每行一个 token）：

$$
Q=XW_q,
\qquad
K=XW_k,
\qquad
V=XW_v
$$

$$
q_i = x_iW_q,
\qquad
k_i = x_iW_k,
\qquad
v_i = x_iW_v
$$

- $W_q,W_k,W_v$ 是**可学习**的线性投影；
- **所有 token 共享同一组 $W$** ⇒ 等价于 **1×1 卷积**（pointwise）。

### 4.4.2 Attention 计算

$$
R = QK^{T},
\qquad
A = \operatorname{softmax}\!\left(\frac{R}{\sqrt{d_k}}\right),
\qquad
Z = AV
$$

- $r_{ij}=q_i\cdot k_j$：token 间相似度；
- softmax **按行**归一化：每个 token 对所有 token 的权重和为 1；
- $z_i=\sum_j a_{ij}v_j$：每个输出是所有 value 的加权和；
- $\sqrt{d_k}$ 缩放：防止点积过大导致 softmax 饱和、梯度消失。

**多头（Multi-head）**：

$$
\text{head}_h = \operatorname{Attention}(XW_q^{h}, XW_k^{h}, XW_v^{h}),
\qquad
Z = \operatorname{Concat}(\text{head}_1,\dots,\text{head}_H)\,W_O
$$

**残差 + LayerNorm + FFN**：

$$
Z' = \operatorname{LayerNorm}\big(Z+\operatorname{Attention}(X)\big),
\qquad
Y = \operatorname{LayerNorm}\big(Z'+\operatorname{FFN}(Z')\big)
$$

$$
\operatorname{FFN}(z) = \operatorname{ReLU}(zW_1)\,W_2
\quad(\text{pointwise，即 1×1 卷积})
$$

### 4.4.3 Attention 的"物理意义"（答题要点）

| 说法 | 含义 |
|---|---|
| Q 是"查询" | 当前 token 想找什么信息 |
| K 是"键" | 每个 token 能提供什么信息 |
| V 是"值" | 每个 token 的实际内容 |
| $QK^{T}$ 是相似度 | 两个 token 的相关性（课件称 covariance matrix 式两两相关） |
| softmax 归一化 | 变成权重（和为 1） |
| $Z=AV$ | 按相关性加权求和所有 token ⇒ 全局信息 |

> 与 CNN 的关键区别（老师原话）：**CNN 的权重是训练学出来的；Attention 的权重是由"当前输入"现场算出来的（not learnable）**——所以 Transformer 能对任意输入动态建立全局依赖。

### 4.4.4 CNN 与 Transformer 的关系（2025-26 S2 Q3c 的核心答案）

| 维度 | CNN | Transformer |
|---|---|---|
| 可学习变换 | 卷积核（局部、共享） | $W_q,W_k,W_v$、FFN（pointwise 1×1 卷积） |
| 权重来源 | 训练数据学出来 | 投影权重学出来；attention 权重由输入算出来 |
| 感受野 | 局部，靠堆叠扩大 | 全局（每个 token 与所有 token 交互） |
| 参数共享 | 空间共享（同一 filter 滑全图） | token 共享（同一 $W$ 作用于所有 token） |
| 本质 | 稀疏 + 共享的 MLP | 1×1 卷积 + 数据相关的加权聚合 |

> **一句话**：Transformer 的所有可学习模块（Q/K/V 投影、FFN）本质上都是 1×1 卷积；区别在于 attention 的权重不是学出来的，而是由输入动态生成的。

### 4.4.5 ViT（Vision Transformer）

- 把图像切成 **patch**（如 16×16），每个 patch 拉平后线性投影成 token；
- 加 **position embedding**（否则没有位置信息）；
- 送入标准 Transformer encoder；
- 用 **CLS token** 或全局池化做分类；
- 优点：**全局建模**、大规模预训练后性能强；缺点：**需要大量数据**、计算量大。

## 4.5 Q3 答题模板

1. 写维度：$x\in\mathbb{R}^{n}$，$W\in\mathbb{R}^{n\times m}$，输出 $\in\mathbb{R}^{m}$；
2. 写标量式 → 再写矩阵式（题目通常两样都要）；
3. 算参数量：FC $(n+1)m$；Conv $F\cdot F\cdot C\cdot D+D$；
4. 反向传播：$E\to\partial E/\partial y\to\partial E/\partial s\to\partial E/\partial V\to\partial E/\partial h\to\partial E/\partial u\to\partial E/\partial W$；
5. 解释：为什么非线性、为什么参数共享、attention 权重从哪来。

---

# 5. Q4 — Topic 11–14：Video 与 3D（概念题）

> **考法**：概念解释 + 对比 + 步骤描述 + 挑战与对策。老师明确"不考记忆、不考计算"；但如果题目给公式（如 stereo 的 $Z=fB/d$），要会代符号推导。
> **范围**：Video generation / video analysis / video enhancement / 3D（ToF、LiDAR、SfM、stereo）。

## 5.1 生成模型（Video Generation）

### 5.1.1 Discriminative vs Generative

| 维度 | Discriminative | Generative |
|---|---|---|
| 学什么 | $P(y\mid x)$（决策边界） | $P(x)$ 或 $P(x,y)$（数据分布） |
| 输出 | 标签/数值 | 新样本 |
| 例子 | 分类器、回归 | GAN、VAE、diffusion |

### 5.1.2 GAN（Generative Adversarial Network）

两个网络**对抗训练**：

- **Generator $G$**：输入噪声 $z\sim p_z$，输出假样本 $G(z)$，目标是**骗过 $D$**；
- **Discriminator $D$**：输入样本，输出"真/假"概率，目标是**区分真假**。

**目标函数（minimax）**：

$$
\min_G\max_D\;
\mathbb{E}_{x\sim p_{data}}\big[\log D(x)\big]
+\mathbb{E}_{z\sim p_z}\big[\log(1-D(G(z)))\big]
$$

- $D$ 想最大化：真样本 $D(x)\to1$，假样本 $D(G(z))\to0$；
- $G$ 想最小化（等价于最大化 $\log D(G(z))$）：让 $D(G(z))\to1$。

**为什么能逼近真实分布**：固定 $G$ 时，最优 $D$ 为

$$
D^{*}(x) = \frac{p_{data}(x)}{p_{data}(x)+p_g(x)}
$$

代回目标函数 ⇒ 等价于最小化 **Jensen–Shannon divergence**：

$$
JSD(p_{data}\,\|\,p_g)
$$

当且仅当 $p_g=p_{data}$ 时取最小值 ⇒ **$G$ 的分布逼近真实分布**。

**训练难点**：mode collapse、训练不稳定、需要平衡 G/D。

### 5.1.3 VAE（Variational Autoencoder）

- **Encoder**：$x\to q(z\mid x)$（通常输出均值 $\mu$、方差 $\sigma^{2}$）；
- **Decoder**：$z\to p(x\mid z)$；
- **Latent space**：低维、连续、近似标准正态的隐空间；采样 $z$ 后可生成新样本；
- **Loss**：

$$
\mathcal{L} =
-\mathbb{E}_{q(z\mid x)}\big[\log p(x\mid z)\big]
+\operatorname{KL}\big(q(z\mid x)\,\|\,p(z)\big)
$$

- **Reparameterization trick**：

$$
z = \mu + \sigma\odot\varepsilon,
\qquad
\varepsilon\sim\mathcal{N}(0,I)
$$

### 5.1.4 GAN vs VAE（对比表，必背）

| 维度 | GAN | VAE |
|---|---|---|
| 结构 | G + D 两个网络 | Encoder + Decoder |
| 训练 | 对抗、minimax | 最大化 ELBO（重建 + KL） |
| 生成质量 | 更锐利 | 偏模糊 |
| 隐空间 | 无显式编码器（除非 BiGAN） | 结构化、连续，可插值 |
| 稳定性 | 难训练、mode collapse | 稳定、易训练 |
| 目标 | 隐式分布 | 显式近似 posterior |

### 5.1.5 Diffusion（简要）

前向逐步加噪：

$$
x_t = \sqrt{\alpha_t}\,x_0 + \sqrt{1-\alpha_t}\,\varepsilon
$$

反向学习去噪 $\varepsilon_\theta(x_t,t)$；采样从纯噪声逐步去噪。优点：训练稳定、质量高；缺点：采样慢。

## 5.2 Video Analysis（检测、跟踪、动作识别）

### 5.2.1 Detection & Tracking

- **Detection**：逐帧检测目标（YOLO/Faster R-CNN）；
- **Tracking**：跨帧关联（Kalman filter、Hungarian matching、Siamese tracker）；
- **Tracking-by-detection**：先检测再关联。

### 5.2.2 ReID vs JDE（2024-25 S1 原题）

| 维度 | ReID（Re-identification） | JDE（Joint Detection and Embedding） |
|---|---|---|
| 任务 | 给定一个人，跨摄像头找回同一个人 | 检测 + 重识别一起做 |
| 输入 | 裁剪好的行人图 | 整帧图像 |
| 输出 | 特征向量（用于匹配） | 检测框 + 每个框的 embedding |
| 流程 | 两阶段：检测 → 裁剪 → ReID | 单阶段：一个网络同时输出检测与特征 |
| 优点 | 特征专精、精度高 | 快（共享 backbone）、适合实时 |
| 缺点 | 慢（两次前向） | 检测与 ReID 目标冲突，需平衡 |

> **一句话**：ReID 是"给图找人"，JDE 是"边检测边提特征"。

### 5.2.3 Action Recognition

| 方法 | 思路 |
|---|---|
| Two-stream | 空间流（RGB 单帧，外观）+ 时间流（optical flow，运动），后期融合 |
| C3D | 3D 卷积直接处理时空 volume |
| LRCN | CNN 提特征 + LSTM 建模时序 |
| Hidden Two-Stream | 用网络实时生成 optical flow，省掉预计算 |

> 核心：**外观（spatial）+ 运动（temporal）** 两条信息缺一不可。

### 5.2.4 MEI / MHI（旧卷考过，了解即可）

- **MEI（Motion Energy Image）**：二值运动能量图，表示"哪里动过"；
- **MHI（Motion History Image）**：灰度随时间衰减，越近的运动越亮，表示"什么时候动"；
- 缺点：丢失方向/速度细节、对背景运动敏感、需要精确对齐。

## 5.3 Optical Flow（光流）

### 5.3.1 定义

光流 = 3D 运动在图像平面上的 2D 投影（像素位移场）。

### 5.3.2 三个假设

1. **Brightness constancy**：同一点在相邻帧亮度不变；
2. **Small motion**：位移足够小（可用一阶 Taylor 展开）；
3. **Spatial coherence**：邻域内像素运动相似（Lucas–Kanade 用）。

### 5.3.3 推导（必背）

$$
I(x,y,t) = I(x+u,\,y+v,\,t+1)
$$

一阶 Taylor 展开：

$$
I(x+u,y+v,t+1) \approx I(x,y,t) + I_x u + I_y v + I_t
$$

代入 ⇒ **brightness constancy equation**：

$$
I_x u + I_y v + I_t = 0
$$

- 1 个方程、**2 个未知数** $(u,v)$ ⇒ **aperture problem（孔径问题）**：只能确定沿梯度方向的分量（normal flow），切向分量未知；
- 数学表述：$\nabla I\cdot(u,v)^{T}=-I_t$，解空间是一条直线，不是唯一点。

### 5.3.4 Lucas–Kanade

- 假设**邻域内 $(u,v)$ 相同** ⇒ 用 $n$ 个像素建立 $n$ 个方程：

$$
\begin{bmatrix}
I_x(p_1) & I_y(p_1)\\
I_x(p_2) & I_y(p_2)\\
\vdots & \vdots
\end{bmatrix}
\begin{bmatrix}u\\v\end{bmatrix}
=
\begin{bmatrix}-I_t(p_1)\\-I_t(p_2)\\\vdots\end{bmatrix}
$$

- 最小二乘解：

$$
\begin{bmatrix}u\\v\end{bmatrix} = (A^{T}A)^{-1}A^{T}b
$$

- 要求 $A^{T}A$ **可逆**（有足够梯度、非平坦区域）。

## 5.4 3D Machine Vision

### 5.4.1 3D 获取方式

| 方法 | 主动/被动 | 原理 | 缺点 |
|---|---|---|---|
| ToF | 主动 | 测光/信号往返时间 | 多路径、背景光 |
| LiDAR | 主动 | 激光测距 | 贵、ghosting/blooming |
| Structured Light | 主动 | 投图案、看变形 | 室外强光失效 |
| SfM | 被动 | 多视图特征对应 + 光束法平差 | 计算量大、依赖纹理 |
| Stereo | 被动 | 双目视差 | 需标定、弱纹理难匹配 |

### 5.4.2 相机模型

$$
x = f\frac{X}{Z},
\qquad
y = f\frac{Y}{Z}
\qquad\text{(perspective projection)}
$$

$$
P_{camera} = R\,P_{world} + T
\qquad\text{(extrinsics)}
$$

> 除以 $Z$ ⇒ 非线性、信息丢失（单图无法唯一恢复深度）。

### 5.4.3 SIFT vs SuperPoint（2025-26 S1 原题）

| 维度 | SIFT（handcrafted） | SuperPoint（learned） |
|---|---|---|
| 检测 | DoG 尺度空间极值（blob） | CNN 输出 heatmap，取局部极大 |
| 描述 | 梯度方向直方图（128 维） | CNN 输出 descriptor map（如 256 维） |
| 不变性 | 尺度、旋转（金字塔 + 方向分配） | 从数据中学（需数据增强/训练） |
| 训练 | 无需训练 | 需要训练（合成数据 + 自监督） |
| 优点 | 可解释、无需数据 | 弱纹理/光照变化下更强、更快 |
| 缺点 | 对模糊/大视角变化弱 | 依赖训练分布、可解释性差 |

> **关键差异**：SIFT 用人工设计的规则找关键点、用梯度直方图描述；SuperPoint 用网络直接回归"哪里是点"和"点长什么样"。

### 5.4.4 Stereo Matching（最高频）

#### 几何与视差

$$
Z = \frac{f\,B}{d}
$$

- $B$ baseline，$d=x_{left}-x_{right}$（disparity）；
- $Z\propto 1/d$：视差大 ⇒ 近；视差小 ⇒ 远。

#### 步骤（必背四步）

1. **Feature extraction**：左右图提特征（共享权重）；
2. **Cost volume construction**：在视差维度上堆叠匹配代价，$H\times W\times D$；
3. **Cost aggregation**：3D CNN / hourglass 聚合上下文；
4. **Disparity regression**：soft argmin / 回归，得到视差图。

#### Cost volume

- 尺寸 $H\times W\times D$；$D$ = **最大视差搜索范围**（如 192、256）；
- **每个 voxel $(h,w,d)$ 的物理意义**：左图 $(h,w)$ 与右图 $(w-d,h)$ 在视差 $d$ 下的**匹配代价**（特征差的范数/相关性）；
- $D$ 太小 ⇒ 近处大视差被截断（深度范围受限）；$D$ 太大 ⇒ 显存/计算量暴涨、易受噪声干扰。

#### 误差传播（2023-24 S2 原题）

$$
Z = \frac{fB}{d}
\quad\Longrightarrow\quad
\Delta Z \approx \left|\frac{dZ}{dd}\right|\Delta d
= \frac{fB}{d^{2}}\Delta d
= \frac{Z^{2}}{fB}\Delta d
$$

> **结论**：深度误差随 $Z^{2}$ 增长——远处一点点视差误差，会造成很大的深度误差。

#### 三大挑战与对策（2025-26 S1 原题）

| 挑战 | 影响 | 对策（learning-based） |
|---|---|---|
| Textureless（弱纹理） | 匹配代价平坦，视差不确定 | 多尺度/大感受野聚合、edge-aware smoothing、active stereo 投图案 |
| Occlusion（遮挡） | 一点在另一图不可见 | 左右一致性检查（LR consistency）、遮挡 mask、robust loss |
| Repetitive patterns（重复纹理） | 多个相同匹配，歧义 | 全局上下文聚合（3D CNN/hourglass）、attention、位置先验 |

#### 系统设计（2025-26 S2 原题）

- **如何定 $D$**：由最近工作距离 $Z_{\min}$ 决定：

$$
d_{\max} = \frac{fB}{Z_{\min}}
$$

再考虑分辨率、视场角、显存；$D$ 取略大于 $d_{\max}$。

- **如何省算力**：① 降分辨率/多尺度（coarse-to-fine）；② 用 1×1 卷积/分组卷积压缩 cost volume；③ early exit / 只在 ROI 算精细视差；④ 稀疏/量化 cost volume；⑤ 轻量 backbone（MobileNet）。

### 5.4.5 Epipolar Geometry（旧卷考过）

$$
p'^{T}E\,p = 0,
\qquad
E = [t]_{\times}R
\qquad\text{(calibrated)}
$$

$$
x'^{T}F\,x = 0,
\qquad
F = K'^{-T}E\,K^{-1}
\qquad\text{(uncalibrated)}
$$

- 极线约束：左图一点，右图对应点必在极线上；
- **rectification**：把极线变成水平行 ⇒ 只需在一行内搜索。

### 5.4.6 Cross-ratio（交比，旧卷考过）

$$
[A,B,C,D] = \frac{|AC|/|BC|}{|AD|/|BD|}
$$

- **投影不变**：任意透视变换下交比不变；
- 用途：从图像中的 3 个已知距离 + 交比，反推第 4 个距离；误差会被放大（对点的定位精度敏感）。

## 5.5 Q4 答题模板

1. 定义：一句话说清"是什么"；
2. 原理/步骤：编号列出（如 stereo 四步、GAN 两网络）；
3. 公式（若题目给符号）：写出来并解释每个符号；
4. 对比/优缺点：表格或 2–3 条；
5. 挑战与对策：每条一句；
6. 总结：一句话点题。

---

# 6. 公式速查表（考前 30 分钟）

## 6.1 Image Enhancement

$$
g = T(f),
\qquad
g = c\,f^{\gamma},
\qquad
g = c\log(1+f)
$$

$$
p_f(f)=\frac{h(f)}{n},
\qquad
c(f)=\sum_{t\le f}p_f(t),
\qquad
g=\operatorname{round}\!\left(\frac{c(f)-c_{\min}}{1-c_{\min}}L\right)
$$

$$
g(x,y)=\sum\sum h(i,j)f(x-i,y-j),
\qquad
G(u,v)=F(u,v)H(u,v)
$$

$$
f_{hb}=(A-1)f+f_{hp},
\qquad
\hat{f}(x,y)=\operatorname{median}_{(s,t)\in S_{xy}} f(s,t)
$$

## 6.2 MAP

$$
P(\omega_i\mid x)=\frac{p(x\mid\omega_i)P(\omega_i)}{p(x)},
\qquad
\omega_k=\arg\max_i p(x\mid\omega_i)P(\omega_i)
$$

$$
p(e)=1-\sum_i P(\omega_i)\int_{\mathcal{R}_i}p(x\mid\omega_i)\,dx
$$

$$
g_i(x)=-\frac{1}{2}(x-\mu_i)^{T}\Sigma_i^{-1}(x-\mu_i)-\frac{1}{2}\ln|\Sigma_i|+\ln P(\omega_i)
$$

$$
d_{\Sigma}=(x-\mu)^{T}\Sigma^{-1}(x-\mu),
\qquad
\Sigma_i=\Sigma:\ g_i=w_i^{T}x+w_{i0},\ w_i=\Sigma^{-1}\mu_i
$$

$$
\Sigma_i=\sigma^{2}I,\ \text{equal priors}:\ \text{nearest mean}
$$

$$
x^{*}=\frac{\mu_1+\mu_2}{2}+\frac{\sigma^{2}}{\mu_2-\mu_1}\ln\frac{P(\omega_2)}{P(\omega_1)}
$$

$$
p(e)=P(\omega_1)Q\!\left(\frac{x^{*}-\mu_1}{\sigma}\right)+P(\omega_2)Q\!\left(\frac{\mu_2-x^{*}}{\sigma}\right)
$$

## 6.3 NN / CNN / Transformer

$$
y=W^{T}x+b,
\qquad
\text{params}=(n_{in}+1)n_{out},
\qquad
y=g\big(V^{T}f(W^{T}x+b)+c\big)
$$

$$
\Delta v_j=\eta\,(t-y)\,g'(s)\,h_j,
\qquad
\delta=(V\delta_{out})\odot f'(u)
$$

$$
y_{i,j,k}=\sum_n\sum_m\sum_l w_{l,m,n,k}\,x_{i-l,j-m,n}+b_k
$$

$$
W_{out}=\frac{W_{in}-F+2P}{S}+1,
\qquad
\text{params}=F\cdot F\cdot C\cdot D+D
$$

$$
y_{ij}=W^{T}x_{ij}+b
\qquad(\text{1×1 conv})
$$

$$
Q=XW_q,\ K=XW_k,\ V=XW_v,
\qquad
A=\operatorname{softmax}\!\left(\frac{QK^{T}}{\sqrt{d_k}}\right),
\qquad
Z=AV
$$

## 6.4 Video / 3D

$$
Z=\frac{fB}{d},
\qquad
\Delta Z=\frac{Z^{2}}{fB}\Delta d,
\qquad
I_x u+I_y v+I_t=0
$$

$$
p'^{T}Ep=0,\ E=[t]_{\times}R,
\qquad
x'^{T}Fx=0,\ F=K'^{-T}EK^{-1}
$$

$$
[A,B,C,D]=\frac{|AC|/|BC|}{|AD|/|BD|}
$$

$$
\min_G\max_D\ \mathbb{E}[\log D(x)]+\mathbb{E}[\log(1-D(G(z)))]
$$

$$
\mathcal{L}=-\mathbb{E}[\log p(x\mid z)]+\operatorname{KL}(q(z\mid x)\,\|\,p(z))
$$

---

# 7. 最后 3 天复习计划

> 11-22（今天）→ 11-23 → **11-24 考试**。

| 时间 | 内容 | 目标 |
|---|---|---|
| 11-22 上午 | 读第 1–3 章（命题规律 + Q1 + Q2） | 能独立做完 3 道 Q1、2 道 Q2 |
| 11-22 下午 | Q1 手算：5 套卷子的 Q1 全部重做 | 直方图/卷积不看答案能算对 |
| 11-22 晚 | Q2 推导：MAP → 判别函数 → 阈值/错误率 | 闭卷写出 3.3、3.5 |
| 11-23 上午 | Q3：MLP 反向传播 + CNN 参数量 | 手推两层网络 |
| 11-23 下午 | Q3：Transformer + 1×1 卷积 + ViT | 能讲清 CNN vs Transformer |
| 11-23 晚 | Q4：背 5.1–5.4 的对比表与步骤 | 每题能写 5 行 |
| 11-24 考前 | 做第 8 章模拟卷（限时），再看第 6 章公式表 | 保持手感 |

**考场策略**：

1. **先做 Q1**（计算最确定，拿满 25）；
2. **Q2 先写公式再算**（过程分多）；
3. **Q3 先写维度/矩阵形状**，再代数；
4. **Q4 先写定义和步骤**，**绝不空题**——写 3 行就有分；
5. 时间：每题 **40–45 分钟**，留 10 分钟检查符号/单位。

---

# 8. 模拟卷（4 题）

> 按今年命题地图自编，难度与旧卷相当。建议限时 3 小时闭卷完成。

## Q1（Topic 3，25 分）

3×3 图像（灰度 0–3）：

$$
F=\begin{bmatrix}0&1&3\\2&3&3\\1&0&2\end{bmatrix}
$$

- (a) 写出 histogram $h(f)$ 与 normalized histogram $p_f(f)$。（5 分）
- (b) 做 histogram equalization（$L=3$），写出映射表与输出图像、输出 histogram。（10 分）
- (c) 若改用 $g=f^{2}/3$（再量化到 0–3），写出输出图像与 histogram，并与 (b) 比较效果。（10 分）

## Q2（Topic 5，25 分）

二类问题，$P(\omega_1)=0.4,\ P(\omega_2)=0.6$；$p(x\mid\omega_1)\sim\mathcal{N}(0,1)$，$p(x\mid\omega_2)\sim\mathcal{N}(4,1)$。

- (a) 写出 MAP 决策规则，求阈值 $x^{*}$。（8 分）
- (b) 求最小错误率（用 Q 函数表示）。（8 分）
- (c) 若两类的方差改为 $\sigma_1=1,\ \sigma_2=2$，阈值还是闭式吗？说明求解方法。（9 分）

## Q3（Topic 9+10，25 分）

输入 $8\times8\times3$，依次经过 CONV3-16（pad 1, stride 1）→ ReLU → POOL2（2×2, stride 2）→ CONV1-32。

- (a) 写出每层输出尺寸与参数量。（10 分）
- (b) 把 CONV1-32 写成矩阵形式，说明它与全连接层的区别。（8 分）
- (c) 解释 Transformer 的 attention 与 1×1 卷积的关系。（7 分）

## Q4（Topic 11–14，25 分）

- (a) 比较 GAN 与 VAE 的结构、训练目标与生成质量。（10 分）
- (b) 描述 stereo matching 的四个步骤；说明 cost volume 中 $D$ 的含义，以及弱纹理/遮挡/重复纹理各自的一种缓解方法。（15 分）

## 8.1 模拟卷答案要点

### Q1

$$
h(0)=2,\ h(1)=2,\ h(2)=2,\ h(3)=3,
\qquad
p=\frac{2}{9},\frac{2}{9},\frac{2}{9},\frac{3}{9}
$$

$$
c(0)=\frac{2}{9},\ c(1)=\frac{4}{9},\ c(2)=\frac{6}{9},\ c(3)=1,
\qquad c_{\min}=\frac{2}{9},\ L=3
$$

映射：

$$
0\to0,\qquad
1:\ \frac{2/9}{7/9}\times3=\frac{6}{7}\approx0.857\to1,
$$

$$
2:\ \frac{4/9}{7/9}\times3=\frac{12}{7}\approx1.71\to2,
\qquad
3:\ \frac{6/9}{7/9}\times3=\frac{18}{7}\approx2.57\to3
$$

⇒ 映射为恒等（本例已近似均匀），输出图不变，$h_g=h$。

(c) $g=f^{2}/3$：$0\to0$，$1\to1/3\to0$，$2\to4/3\to1$，$3\to3\to3$。

$$
G=\begin{bmatrix}0&0&3\\1&3&3\\0&0&1\end{bmatrix},
\qquad
h_g(0)=4,\ h_g(1)=2,\ h_g(3)=3
$$

对比：幂变换压暗低灰度、拉伸高灰度（非线性）；均衡化按累积分布重映射以拉平 histogram。

### Q2

$$
x^{*}=\frac{0+4}{2}+\frac{1}{4-0}\ln\frac{0.6}{0.4}
=2+\frac{1}{4}\ln1.5\approx2.101
$$

$$
p(e)=0.4\,Q(2.101)+0.6\,Q(1.899)
\approx0.4(0.0179)+0.6(0.0288)\approx0.0245
$$

(c) 方差不同 ⇒ 比较两个高斯，取对数后是 $x$ 的二次方程（判别函数为二次），阈值有两个根，取落在两类之间的那个；错误率用两个 Q 函数相加。

### Q3

$$
\text{Input}: 8\times8\times3
$$

$$
\text{CONV3-16, pad1, stride1}: 8\times8\times16,\quad
\text{params}=16(3\cdot3\cdot3+1)=448
$$

$$
\text{POOL2}: 4\times4\times16,\quad 0\ \text{params}
$$

$$
\text{CONV1-32}: 4\times4\times32,\quad
\text{params}=32(1\cdot1\cdot16+1)=544
$$

(b) 对每个空间位置：$y_{ij}=W^{T}x_{ij}+b$，$W\in\mathbb{R}^{16\times32}$。与 FC 区别：FC 每个位置独立权重；1×1 conv 所有位置共享同一 $W$，参数量从 $(16+1)\times32\times16$ 降到 $(16+1)\times32$。

(c) Q/K/V 投影 = 对每个 token 的 1×1 卷积；FFN 也是 pointwise 1×1 conv；区别：attention 权重由输入算出（非学习），CNN 权重由训练学出。

### Q4

(a) 见 5.1.4 对比表：GAN 用对抗损失、质量锐利但难训；VAE 用重建 + KL、稳定但偏模糊、隐空间连续。

(b) 四步见 5.4.4；$D$ = 最大视差范围；弱纹理 → 多尺度聚合/active stereo；遮挡 → 左右一致性检查；重复纹理 → 全局上下文/attention。

---

> **最后提醒**：Q4 是**概念题**，"if you attend all the lectures, you should be able to answer"——**写满、写清楚定义与步骤**，不要因为不确定就留空。祝考试顺利。
