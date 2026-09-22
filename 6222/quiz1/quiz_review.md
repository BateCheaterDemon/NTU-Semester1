# EE6222 Quiz 1 复习笔记

> **Quiz 1 信息**（权威，取自 Week 1 考核表 + Week 6 转写）
> - **时间**：Week 7 课堂内（下半节；上半节继续讲 AdaBoost）
> - **时长**：30 分钟
> - **占比**：10%（CA 40% 的一部分；另 30% 是两次 Assignment 各 15%）
> - **范围**：**Week 1–6 已讲内容**（Topic 1–6 + Topic 8 feature extraction + Topic 7 开场）
> - **形式**：课堂完成
> - **老师强调的考试原则**：**不要求死记无物理意义的公式**；记有物理意义的（Mahalanobis distance、MAP rule、histogram equalization 累加式等）

---

## ⭐ 老师明确提示的考试陷阱（必看）

1. **Histogram equalization 只用归一化公式 → 零分**：真正的 HE 是累加 histogram：`c(f)=Σ_{t=0}^f p_f(t)`；`g=round[(c(f)-c_min)/(1-c_min)·L]` 只是普通归一化，与 HE 无关。**必须先算累加**。
2. **Quiz 中 histogram 会用 impulse 形式给出**：`P_f(f)=a₁δ(f-b₁)+a₂δ(f-b₂)+…`，其中 **b 是灰度位置、a 是高度（像素比例）**。不认识这个写法 → 整题答不出。
3. **离散图像 HE 后 histogram 不是严格均匀**：point transform 不改变竖线**高度**，只改**位置**。
4. **数字图像频域相乘 ≠ 普通卷积**：是 circular convolution，**必须先 zero padding**。
5. **共享 Σ ≠ covariance 无用**：common Σ 仍决定最优边界方向与位置；边界**不一定**过两 mean 连线（仅 Σ=σ²I 时才过）。
6. **Minimum distance classifier 只在四条件全满足时 optimal**：Gaussian + 共享 covariance + Σ=σ²I + 等先验。任一不满足则非最优。
7. **PCA 对分类不一定好**：最大化 total variance ≠ 最大化 discriminative information；最大 variance 方向投影后两类可能完全重叠。
8. **降维提升 accuracy 的真正原因是去除 misleading information**，而非保留 discriminative info。

---

## 一、Topic 1：Image Fundamentals

### 1.1 数字图像
- 图像 = 3D 场景在 2D 上的投影 = 二维函数 `f(x,y)` = m×n 矩阵，每个元素是一个 pixel。
- 数字化两步：**spatial sampling**（空间采样）+ **gray-level quantization**（灰度量化）。
- 灰度分辨率 `g=2^b`，8 bit → 256 级；2 级 → binary image。

### 1.2 图像形成三要素
- **Light source**：光是 waveform，可见光 350–780 nm。
- **Object**：reflectivity ρ(λ) 是频率函数 → 白光下物体仍显色。
- **Lens + Sensor array**：透镜确保"一点对一点"聚焦；无透镜则一个传感器收到四面八方的光无法成像。

### 1.3 亮度公式
- 物体一点：`I(λ)=ρ(λ)·L(λ)`
- 传感器：`f(x,y)=∫₀^∞ I(x,y,λ)·V(λ)dλ`，V(λ) 是 relative spectral sensitivity function（频率响应）。
- 单个传感器只输出一个值（光能量总量），无频率信息。

### 1.4 颜色感知
- 人眼三类 cone（L红/M绿/S蓝），各输出 `f_k(x,y)=∫I(x,y,λ)V_k(λ)dλ`，三个**相对值**决定 color。
- Color 是 3D 空间中一点：`c=a·p₁+b·p₂+c·p₃`。
- 常见 color space：RGB（硬件）、CMY（打印）、HSI/HSV（颜色操作）、YIQ（电视）、CIE-Lab。

### 1.5 ⭐ Image Histogram
- `p_f(f)=n_f/n`，f 为 gray level，n_f 为该灰度像素数，n 为总像素数。性质：`p_f≥0, Σp_f=1`。
- **本质**：gray-level 出现的频率，是 PDF 的 estimate（非 PDF 本身——PDF 是理论值，histogram 是统计值）。
- **形状解读**：
  | 形状 | 图像特征 |
  |---|---|
  | 窄分布 | 低对比度 |
  | 集中低灰度端 | 暗图像（under-exposure） |
  | 集中高灰度端 | 亮图像（over-exposure） |
  | 双峰（bimodal） | 物体+背景，峰大小反映面积 |
  | 展布全范围近似均匀 | 理想清晰图像 |
- **丢失空间信息**：只统计"某灰度有多少像素"，不记录位置。
- **重要原则**：任何信息处理系统只能减少信息，不能增加信息。
- **作为特征**：LBP、HOG 最终都转化为 histogram。

---

## 二、Topic 2：LSI Systems & Transforms

### 2.1 两大支柱
- **Convolution**：信号分解为 **impulse** 之和。
- **Fourier transform**：信号分解为 **sinusoid** 之和。
- 两者同源于 **signal decomposition（信号分解）**。

### 2.2 Impulse 与图像分解
- 离散：`δ(x,y)=1 if x=y=0 else 0`。
- ⚠️ 连续 impulse 必须为**无穷大**（否则积分面积为零无意义），积分为 1。
- 任意图像 = 移位缩放 impulse 之和：`f(x,y)=Σ_{i,j} f(i,j)·δ(x-i,y-j)`。

### 2.3 ⭐ 2-D Convolution（推导四步）
1. 代入图像分解
2. 系统线性 → T 移入求和
3. 定义 impulse response `h(x,y)≜T{δ(x,y)}`
4. 系统移不变 → `T{δ(x-i,y-j)}=h(x-i,y-j)`

$$g(x,y)=f(x,y)*h(x,y)=\sum_i\sum_j f(i,j)\,h(x-i,y-j)$$

- LSI 系统**完全由 impulse response h(x,y) 刻画**。
- h 的别名：spatial representation of filter / filter mask / filter coefficients。
- 卷积本质 = **weighted sum（加权求和）**，输出在 mask 中心。
- 性质：交换律、结合律、分配律。
- CNN 中翻转与否不影响结果（参数学到的，训练推理一致即可）。

### 2.4 ⭐ Fourier Transform
- 正变换：`F(u)=∫f(x)·exp(-j2πux)dx`；逆变换：`f(x)=∫F(u)·exp(j2πux)du`。
- **lossless（无损）**：有逆变换，不丢信息。
- **物理意义**：任意信号 = 不同频率 sinusoid 之和；|F(u)|=amplitude，∠F(u)=initial phase。
- **为何用 complex exponential**：相乘 = 指数相加，远比 cos·cos 简洁。
- **正变换如何提取频率**：u=u₀ 时被积函数为常数 → ∞；u≠u₀ 时为 sinusoid → 积分 0。F(u) 只在信号真实含有的频率处非零。

### 2.5 2-D Fourier Transform
- `F(u,v)=∫∫f(x,y)exp[-j2π(ux+vy)]dxdy`
- **Separable**：2-D FT = 做两次 1-D FT。⚠️ `F(u,v)=F_x(u)·F_y(v)` **只在 f(x,y)=f₁(x)f₂(y) 时成立**。

### 2.6 ⭐ DFT 与"为何除以 m、n"
- `F(u,v)=ΣΣf(x,y)exp[-j2π(ux/m+vy/n)]`
- **为何除以 m、n**：离散信号 period ≥ 1 ⇒ frequency ≤ 1（DTFT 的 u,v 连续 ∈[0,1)）；除以 m 把 [0,1) 拉伸到 [0,m) 使 u 可取整数 → DFT。
- 常数 `1/mn` 不重要，可放正/逆变换任意位置。

| | x,y | u,v |
|---|---|---|
| 连续 FT | 连续 | 连续 (−∞,∞) |
| DTFT | 离散 | 连续 ∈[0,1) |
| DFT | 离散 | 离散整数 0…m−1 |

### 2.7 ⭐ DFT 性质

| 性质 | 要点 |
|---|---|
| **Periodicity** | `F(u,v)=F(u+m,v)=F(u,v+n)`，频率超过范围只重复自身 |
| **Conjugate symmetry**（实图像） | `F(u,v)=F*(-u,-v)`；m×n 实数→m×n 复数信息 2 倍冗余；magnitude 偶对称、phase 奇对称 |
| **Linearity** | FT 是线性变换 |
| **Scaling** | 一个域拉伸 ⇔ 另一域压缩 |
| **⭐ Convolution theorem** | `f*g ⇔ F·G`；⚠️ 离散情形是 **circular convolution**，**须先 zero padding** |
| **Translation** | 平移只乘 `exp(-j2π(x₀u/m+y₀v/n))`，**magnitude 不变**（只改 phase） |
| **Rotation** | 空间旋转 ⇒ 频谱同角度旋转；DFT **不是** rotation invariant → Polar Harmonic Transform 才是 |

- ⭐ **Translation invariance**：平移只改 phase 不改 magnitude → |F| 可作 object recognition 特征（无论物体在哪都能认出）。
- **变换对**：rectangle ⇔ 2-D sinc。

### 2.8 ⭐ Image Sampling 与 Nyquist
- 采样：`f_d(m,n)=f_c(mΔx,nΔy)`，简单替换；难在分析连续与离散的关系。
- **Band-limited**：`F_c(u,v)=0 for |u|>U₀`；bandwidth = **2U₀**（本课采用，因负频率/调制后范围）。
- **Sampling function**（impulse train）：FT 仍是 impulse train，间隔 1/Δx, 1/Δy。
- **核心结论**：采样后 `F_d` 是 `F_c` 以 (1/Δx,1/Δy) 为间隔的**周期复制**。
- **Nyquist rate**：`1/Δx ≥ 2U₀`；低于则 **aliasing（混叠）**，不可逆丢失。
- **抗混叠**：采样前 low-pass filtering，代价是丢失高频细节。
- **重建**：用 low-pass filter 离散像素值加权连续 h(x,y) 求和 → 恢复连续图像。
- ⭐ **采样定理**：band-limited 且满足 Nyquist → 连续与离散图像信息完全等价，可放心用连续数学分析。

---

## 三、Topic 3：Image Enhancement

### 3.1 Point Processing
- `g=T(f)`，**memoryless**（与位置无关）。
- **三种变换**：
  | 变换 | 公式 | 用途 |
  |---|---|---|
  | Power / gamma | `g=c·f^γ` | gamma correction |
  | Log | `g=c·log(1+f)` | 形似 γ<1 |
  | Piecewise linear | 分段直线 | contrast stretching |
- ⭐ **守恒思想**：总范围 [0,L] 不变，增强一段必压缩另一段。
  - **γ>1**：拉伸亮部、压缩暗部 → 修过亮图
  - **γ<1**：拉伸暗部、压缩亮部 → 修过暗图
- Piecewise：斜率>1 增强对比，<1 压缩；极端中间段 ∞ → binary image（对比度最高）。

### 3.2 ⭐⭐ Histogram Equalization（最重要考点）
- **目标**：输出 histogram 尽量均匀 → 对比度最大。
- **算法**：
  ```
  ① c(f) = Σ_{t=0}^{f} p_f(t)    ← ⭐ 这才是 HE 本体
  ② g = round[(c(f)-c_min)/(1-c_min) · L]   ← 只是归一化，与 HE 无关
  ```
- ⚠️ **只用公式②作答 → 零分**。必须先算累加 c(f)。
- **连续证明**：取 `g=T(f)=∫₀^f p_f(t)dt`（cdf），则 `dg/df=p_f`，`p_g(g)=p_f·(df/dg)=p_f·(1/p_f)=1`（uniform）。
- **直观**：像素集中处累加快→大幅拉开；无像素处累加不变→压缩。自适应。
- ⭐ **离散不能严格均匀**：point transform 不改竖线**高度**，只改**位置**（同一灰度的像素变换后仍同一灰度）。
- ⭐ **考试形式**：histogram 用 **impulse 形式**给出 `P_f(f)=a₁δ(f-b₁)+a₂δ(f-b₂)+…`，a=高度、b=位置。不认识 → 失分。

### 3.3 Linear Filtering
- 卷积本质 = weighted sum。频率域设计、空间域实现（`G=F·H`）。

**Image Smoothing（low-pass）**：
| Filter | 公式/特点 |
|---|---|
| Ideal low-pass (ILPF) | 圆内 1 圆外 0；有 **ringing**（sinc 负瓣产生 artificial structure）→ 实践不用 |
| Gaussian low-pass (GLPF) | `H=(1/2πσ²)exp(-(u²+v²)/2D₀)`；平滑过渡无突变，FT 仍 Gaussian，无 ringing → **实践总是用** |

**Image Sharpening（high-pass）**：
- `H_hp=1-H_lp`，提取 edge。
- Ideal high-pass 同样 ringing；Gaussian high-pass 无。
- **High-boost filter**：`f_hb=A·f-f_lp=(A-1)f+f_hp`，保留低频+增强 edge。

### 3.4 ⭐⭐ Mean vs Median Filter（重点）

| 情形 | Mean（线性） | Median（非线性） |
|---|---|---|
| 图像细节/细线 | **blurs** detail | **preserves** detail |
| edge（阶跃） | **blurs** → ramp | **preserves** step edge |
| impulsive noise（强幅度稀疏） | 降低幅度且**扩散**，无法去除 | **完全去除**（噪声像素<非噪声时） |
| Gaussian dense noise（小幅密集） | **最优**（mean 是 L2 最小估计） | 能抑制但不如 mean |

- **median 稳健性**：异常值多大都不影响 median；mean 被拉偏。
- **median 缺点**：丢失 corner/细线等小细节（窗口内多数是背景→corner 被当噪声抹掉）。
- **root signal**：对 median 不变的信号；constant、单调信号是任意窗口 median 的 root。
- median 非线性，无成熟频域理论。

### 3.5 其他 Order-Statistic Filters
- Max / Min / Midpoint filter。
- **Alpha-trimmed mean**：排序去 d 个极端值再平均剩余 n-d 个。
  - d=0 → mean；d=n−1 → median。
  - 需排序（CPU 贵）、d 难选；老师改用 truncate（截断非删除）。
- **mean = L2 min**（闭式解），**median = L1 min**（需迭代）。ITM 用算术迭代逼近 median。

---

## 四、Topic 4：Object Recognition / Template Matching

### 4.1 Template Matching
- 机器不能"理解"，只能**比较**：gallery $\{g_1,…,g_G\}$，找最接近的。
- `k*=argmin_k ‖A-g_k‖`，取 **argmin（类索引）**非最小值本身。

### 4.2 Euclidean Distance 与向量化
- `d(A,g)=‖A-g‖₂=√(ΣΣ(A(x,y)-g(x,y))²)`
- 图像展平为列向量：`d(a,g)=√((a-g)ᵀ(a-g))`。

### 4.3 ⭐ Normalization
- Euclidean distance 不够：内容相同但 brightness/contrast 不同的图距离巨大。
- **零均值单位方差**：`f̃=(f-μ_f)/σ_f` 或 `f̃=(f-μ_f)/‖f-μ_f‖`（unit length）。
- 归一化后仅 brightness/contrast 不同的同一内容 → distance=0。
- ⭐ **normalization 是 recognition/ML 的核心**：消除 variation，把同一物体的不同表现映射到同一表示。

### 4.4 Correlation Coefficient
- `ρ=(f-μ_f)ᵀ(g-μ_g)/(‖f-μ_f‖·‖g-μ_g‖)`，内含归一化。
- 相似 → |ρ|→1。用 correlation 取**最大** = 归一化 Euclidean distance 取**最小**。

### 4.5 Nearest Neighbor Classifier
- 一物多 template → class。
- **1-NN**：`k*=argmin_i(min_{g∈class ω_i}‖A-g‖)`，取最近样本所属 class。
- **K-NN**：取 K 个最近，多数投票。
- **问题**：计算量大、overfit（只依赖少数训练样本）。

---

## 五、Topic 5：MAP Decision and Classifiers

### 5.1 ⭐ MAP Decision Rule
- 从 common sense 到数学化：选 posterior 最大的类。
$$\omega_k=\arg\max_{\omega_i} p(\omega_i|x)$$
- 同时**最小化 error probability** `p(e_k|x)=1-p(ω_k|x)`。

### 5.2 Bayes 公式
$$p(\omega_i|x)=\frac{p(\omega_i)\,p(x|\omega_i)}{p(x)}$$
- prior `p(ω_i)`、class-conditional / likelihood `p(x|ω_i)`。
- `p(x)=Σ_i p(x|ω_i)p(ω_i)`（law of total probability）。
- ⭐ **p(x) 对所有类相同 → 移除**：决策只需比较 `p(ω_i)·p(x|ω_i)`。

### 5.3 Error Rate
- 特定 x：`p(e_k|x)=1-p(ω_k|x)`。
- 全系统：`p(e)=∫p(e_k|x)p(x)dx`（probability-weighted average）。
- 两类可视化：两曲线交点处决策边界 → 阴影面积最小。
- **增加特征维度一般降低 error rate**。

### 5.4 ⭐ Discriminant Function
- `g_i(x)=ln p(x|ω_i)+ln p(ω_i)`，与 posterior 单调成比例（取 ln 把乘变加、指数变线性）。
- Gaussian 假设 `p(x|ω_i)=N(μ_i,Σ_i)` 下：
$$g_i(x)=-\frac{1}{2}(x-μ_i)^TΣ_i^{-1}(x-μ_i)+\ln p(ω_i)-\frac{1}{2}\ln|Σ_i|-\frac{d}{2}\ln2\pi$$
- 末项对所有类相同 → 移除。记 `b_i=ln p(ω_i)-½ln|Σ_i|`：
$$g_i(x)=-\frac{1}{2}d_{Σ_i}(x,μ_i)+b_i$$

### 5.5 ⭐ Mahalanobis Distance
$$d_Σ(x,μ)=(x-μ)^TΣ^{-1}(x-μ)$$
- = **Euclidean distance 被 covariance 归一化**。
- Gaussian 下 minimum Mahalanobis classifier = optimal。
- mean 决定位置，covariance 决定形状（contour/ellipse）。
- 椭圆等距线上 Mahalanobis 相同但 Euclidean 不同。

| | Mahalanobis | Euclidean |
|---|---|---|
| 1D | (x-μ)²/σ² | (x-μ)² |
| 等距线 | 椭圆 | 圆 |

### 5.6 ⭐ 分类器三种情形

| 假设 | 分类器 | 边界 | 关键 |
|---|---|---|---|
| 一般 Gaussian（各 Σ_i 不同） | **Quadratic classifier** | 二次曲线/曲面 | 可为 ellipse/hyperbola/抛物线 |
| 共享 Σ（Σ_i=Σ） | **Linear classifier** `g=w_iᵀx+w_{i0}`，w_i=Σ⁻¹μ_i | hyperplane | ⚠️ 边界**不一定过两 mean 连线**；Σ 仍关键（反 Direct LDA） |
| Σ=σ²I（scalar）+ 等 prior | **Minimum distance classifier** | 过两 mean 连线 | argmin‖x-μ_i‖² = template matching |

- ⭐ **Minimum distance classifier 的四条件**：Gaussian + 共享 covariance + Σ=σ²I + 等先验。任一不满足则非最优。
- scalar Σ=σ²I：边界法向量 `w∝(μ_i-μ_k)` → 必然过两 mean 连线 → 分类只需沿类均值差方向一维投影。
- **prior 影响**：不等 prior → 边界平移（prior 大的类地盘扩大）；悬殊可移出两 mean 区间。

---

## 六、Topic 6：Statistical Estimation / Machine Learning

### 6.1 核心论点
- **Statistical estimation = machine learning**：用 training data 估计 PDF/参数。
- PDF 是随机变量的**完备信息**，学全 PDF 即得最优分类；实践样本有限需选参数。

### 6.2 Prior 估计
$$\hat p(ω_k)=N_k/N$$

### 6.3 两大路线
| 路线 | 假设 | 方法 |
|---|---|---|
| Non-parametric | 不假设 PDF 形式 | Parzen window、K-NN |
| Parametric | 假设 PDF 形式（如 Gaussian） | MLE |

### 6.4 ⭐ Parzen Window（Non-parametric）
$$p(x)=\frac{1}{N}\sum_{i=1}^N\frac{1}{h^D}K\!\left(\frac{x-x_i}{h}\right)$$
- 核心：density × volume ≈ probability，`p(x)≈(k/N)/V`。
- 矩形窗 → 阶梯不光滑；改 **Gaussian kernel** → 光滑。
- 核函数条件：K≥0，∫K=1。
- ⭐ **带宽 h 是关键超参**：h 大→过度平滑（极端 uniform）；h 小→过度尖锐（极端仅训练点冲激）。
- **IID**：训练样本须独立同分布。

### 6.5 ⭐ MLE（Parametric）
$$\hat\theta=\arg\max_\theta\sum_{i=1}^N\ln p(x_i|\theta)$$
- Gaussian MLE 结果：
$$\hat\mu=\frac{1}{N}\sum x_i=\text{样本均值},\quad \hat\sigma^2=\frac{1}{N}\sum(x_i-\hat\mu)^2=\text{样本方差}$$
- 多维：covariance matrix 的 MLE = data covariance matrix。

---

## 七、Topic 8：Feature Extraction（PCA / LDA）

### 7.1 Feature Extraction vs Feature Selection

| | Feature Extraction | Feature Selection |
|---|---|---|
| 方式 | 组合全部 raw component 生成新 feature | 选取子集，不组合 |
| 数学 | `y=Φᵀx` | 选 x 的某些分量 |
| 计算 | 每个 feature 需全部输入 → 较慢 | 预测只算被选的 → 很快 |
| 归属 | Topic 8（PCA/LDA） | Topic 7（Viola-Jones/AdaBoost） |

- 线性降维一般形式：`y=Φᵀx`，Φ 可人定义（Fourier）或从数据学习（ML）。

### 7.2 ⭐⭐ PCA（Principal Component Analysis）

**推导链**：
1. **最佳代表点** = sample mean（最小化 MSE，也是 Gaussian 中心 MLE）。
2. Centralize：`x̃_i=x_i-x₀`。
3. **最佳一维方向**：投影 `a_i=φᵀx̃_i`，重建 `x̂=a_iφ`，最小化重建误差 ⇔ **最大化投影后方差** `Σ(φᵀx̃_i)²`。
4. 识别出 **total scatter matrix** `S_T=Σx̃_i x̃_iᵀ`。
5. **Lagrangian**（约束 ‖φ‖=1）→ **特征方程**：
$$S_T\phi=\lambda\phi$$

**⭐ 物理意义**：
- **Eigenvector = 投影后方差最大的方向**。
- **Eigenvalue = 该方向的 variance 值**。
- 第一主成分（largest eigenvalue）方差最大，第二次之…

**m 维 PCA**：取 top-m eigenvalue 的 eigenvector 组成 Φ，`y=Φᵀx̃`。
- **重建误差 = 未被选取的 eigenvalue 之和** `ε=Σ_{j=m+1}^n λ_j`。
- 取所有非零 eigenvalue → 无损降维。
- `rank(S_T)≤Q-1`（Q 个样本减 mean 损一个自由度）→ 可无损降至 Q−1 维。

**对称矩阵性质**：
- Eigenvector 对应不同 eigenvalue 彼此 **orthogonal**，unit length 后 **orthonormal**（ΦᵀΦ=I）。
- `ΦᵀS_TΦ=Λ`（对角化，投影后去相关）。
- `S_T=ΦΛΦᵀ`（谱分解）。

**2D 可视化**：椭圆云，φ₁ 沿长轴（variance 最大），φ₂ 沿短轴。对角元 σ₁₁,σ₂₂ = 长短轴（variance），非对角元 σ₁₂ = 倾斜（correlation）。

### 7.3 ⭐⭐ LDA（Linear Discriminant Analysis）

**PCA 的问题**：unsupervised，不利用 class membership → 最大 variance 方向投影后两类可能完全重叠（error ≈ 50%）。

**LDA 思想**（supervised）：
- **Between-class variance 最大化**（类中心分开）。
- **Within-class variance 最小化**（类内紧凑）。

**两个 scatter matrix**：
- `S_W=Σ_k P_k S_k`，`S_k=Σ_{i∈ω_k}(x_i-μ_k)(x_i-μ_k)ᵀ`（类内 covariance 平均）。
- `S_B=Σ_k P_k(μ_k-μ)(μ_k-μ)ᵀ`（类中心间差异）。
- ⭐ **`S_T=S_W+S_B`**（total = within + between）。

**Fisher criterion**：
$$\phi=\arg\max_\phi\frac{\phi^T S_B\phi}{\phi^T S_W\phi}$$
- 解为 **eigenvector of `S_W^{-1}S_B`**：`S_W^{-1}S_B φ=λφ`，取 largest eigenvalue。

**PCA vs LDA**：
| | PCA | LDA |
|---|---|---|
| 矩阵 | S_T | S_W⁻¹S_B |
| 监督 | Unsupervised | Supervised |
| 最大化 | Total variance | Between/within ratio |
| 对分类 | 不保证好 | 更好 |

**S_W 不满秩问题**：`rank(S_W)=Q-c`；Q≪n 时奇异 → **PCA+LDA（Fisherfaces）**：先 PCA 降维到 S_W 满秩，再 LDA。

### 7.4 ⭐⭐ 降维提升 accuracy 的真正原因（老师批判性思考）
- LDA 降维**丢失**信息，却声称保留"最 discriminative"——但 LDA 只能**尽量不丢** discriminative info，不能**新增**。
- 真正提升 accuracy 的原因是**去除了 misleading information（误导信息）**：训练数据中虽能区分类别但是噪声/虚假的 discriminative 信息。
- 去除 misleading info → accuracy 可超过原始高维数据。
- **Assignment**：用 PCA/LDA 降维到不同维度，画 accuracy vs dimension 曲线，观察并解释。

### 7.5 降维后分类流程
1. 计算 scatter matrix（S_T for PCA，S_W/S_B for LDA）。
2. 求 eigenvector/eigenvalue，取 top-m 组成 Φ。
3. 投影：`y=Φᵀ(x-μ)`。
4. 在 m 维 feature space 分类（Mahalanobis / minimum distance）。
5. ⭐ 常用 **pooled covariance**（S_W）→ 共享 Σ → linear classifier。

---

## 八、Topic 7 开场：Feature Selection / Viola-Jones

### 8.1 为什么需要 feature selection
- Feature extraction 每个新 feature 需全部输入 → 计算量大。
- 某些应用需极快 feature 计算 → feature selection 选取子集，预测时只算被选的。

### 8.2 Object Detection（face detection）
- sliding window 扫描所有位置+不同 scale，每位置 binary classification（face/non-face）。
- 执行次数可达数万~百万级 → 极需快速 feature + 快速分类。
- **三大挑战**：快速计算 feature、少量 feature 代表 raw data、少量 feature 下好 accuracy。

### 8.3 ⭐ Viola-Jones 方法（IJCV，深度学习前最流行 face detection）
1. **Haar-like feature**：两个矩形区域 average gray value 的差值（反映 contrast，捕捉结构）。用矩形因可极快计算。
2. **⭐ Integral Image（积分图）**：`I(x,y)=Σ_{x'≤x,y'≤y}f(x',y')`。
   - 任意矩形 D 像素和 = `I(4)-I(2)-I(3)+I(1)`（四角点，**3 次加减法**，与矩形大小无关）。
3. **Feature pool**：24×24 窗口 → 约 **180,000** 种 Haar-like feature。
4. **Feature selection**：从 180,000 选约 **100** 个最有效 → 预测只算这 100 个 → 极快。
5. **AdaBoost**：从大 pool 选最有效少量 feature（具体算法 Week 7 讲）。

---

## 九、考点速查表（全范围）

| # | 考点 | 关键结论 |
|---|---|---|
| 1 | 数字图像 | 2D 函数 f(x,y) = m×n 矩阵；sampling + quantization |
| 2 | Histogram | `p_f=n_f/n`；是 PDF 的 estimate，非 PDF 本身；丢失空间信息 |
| 3 | Convolution 推导 | 线性+移不变 → `g=f*h=Σf(i,j)h(x-i,y-j)` |
| 4 | LSI 系统 | 完全由 impulse response h 刻画；weighted sum |
| 5 | Fourier 物理意义 | 信号=sinusoid 之和；|F|=amplitude, ∠F=phase |
| 6 | 为何 complex exponential | 相乘=指数相加，简洁 |
| 7 | DFT 为何除 m,n | 离散 period≥1⇒freq≤1；除以 m 拉到 [0,m) |
| 8 | Convolution theorem | 离散是 circular，**须 zero padding** |
| 9 | Translation invariance | 平移只改 phase 不改 magnitude → |F| 可作识别特征 |
| 10 | DFT rotation | 非旋转不变；Polar Harmonic Transform 才是 |
| 11 | Sampling | F_d 是 F_c 的周期复制；Nyquist 1/Δx≥2U₀ |
| 12 | Aliasing | 低于 Nyquist 不可逆；抗混叠代价=丢高频 |
| 13 | ⭐⭐ Histogram equalization | `c(f)=Σp_f(t)` 才是本体；只用归一化→零分 |
| 14 | HE impulse 形式 | `P_f=Σa_iδ(f-b_i)`，a=高度 b=位置 |
| 15 | 离散 HE | 不严格均匀；不改竖线高度只改位置 |
| 16 | Gamma 守恒 | 总范围不变，增强一段必压缩另一段 |
| 17 | γ>1/γ<1 | γ>1 修过亮；γ<1 修过暗 |
| 18 | Ideal vs Gaussian filter | Ideal 有 ringing；Gaussian 无（FT 仍 Gaussian） |
| 19 | High-boost | `(A-1)f+f_hp`，保留低频+增强 edge |
| 20 | ⭐ Mean vs Median | median 保 edge/细节、完全去 impulsive noise；mean 适合 Gaussian dense |
| 21 | median 去噪条件 | 窗口内噪声像素<非噪声像素 |
| 22 | median 缺点 | 丢失 corner/细线小细节 |
| 23 | Alpha-trimmed | d=0→mean, d=n-1→median；需排序 |
| 24 | mean/median 本质 | mean=L2 min(闭式), median=L1 min(迭代) |
| 25 | Template matching | argmin‖A-g‖，取 argmin 非最小值 |
| 26 | Normalization | 消除 variation；同一物体不同表现归一后 distance=0 |
| 27 | Correlation coefficient | 内含归一化，取最大=归一化 Euclidean 取最小 |
| 28 | K-NN | K 个最近多数投票；问题：计算量大、overfit |
| 29 | ⭐ MAP rule | argmax p(ω_i\|x)，最小化 error probability |
| 30 | Bayes | posterior=prior×likelihood/p(x)；p(x) 可移除 |
| 31 | Discriminant function | g_i=ln p(x\|ω_i)+ln p(ω_i)，与 posterior 单调 |
| 32 | ⭐ Mahalanobis distance | (x-μ)ᵀΣ⁻¹(x-μ)，Euclidean 被 covariance 归一化 |
| 33 | Gaussian→quadratic | g_i=-½d_Σ+b_i，二次边界 |
| 34 | 共享 Σ→linear | 二次项抵消，w_i=Σ⁻¹μ_i；不一定过 mean 连线 |
| 35 | Σ=σ²I+等prior | min distance classifier，过 mean 连线，template matching |
| 36 | min distance 四条件 | Gaussian+共享Σ+σ²I+等prior 全满足才 optimal |
| 37 | 共享Σ≠covariance无用 | Σ 仍决定边界方向位置（反 Direct LDA） |
| 38 | prior 影响 | 不等→边界平移；悬殊可移出两 mean 区间 |
| 39 | estimation=ML | 用训练数据估 PDF/参数 |
| 40 | Parzen window | `p=(1/N)Σ(1/h^D)K((x-x_i)/h)`；h 关键 |
| 41 | MLE Gaussian | μ̂=样本均值, σ̂²=样本方差 |
| 42 | feature extraction vs selection | extraction 组合全部；selection 选子集更快 |
| 43 | PCA 推导 | 最佳代表点=mean→最大投影方差→S_T 特征方程 |
| 44 | ⭐ PCA eigenvector | 投影后方差最大方向 |
| 45 | ⭐ PCA eigenvalue | 该方向 variance |
| 46 | PCA 重建误差 | 未选 eigenvalue 之和 |
| 47 | PCA 无损降维 | 取所有非零 eigenvalue；rank≤Q-1 |
| 48 | 对称矩阵 | eigenvector orthonormal；对角化去相关 |
| 49 | PCA unsupervised | 不用 class label；对分类不一定好 |
| 50 | LDA Fisher criterion | max φᵀS_Bφ/φᵀS_Wφ；eigenvector of S_W⁻¹S_B |
| 51 | S_T=S_W+S_B | total=within+between |
| 52 | LDA S_W 不满秩 | Q≪n→PCA+LDA(Fisherfaces) |
| 53 | ⭐ 降维提升 accuracy | 去除 misleading info，非保留 discriminative |
| 54 | pooled covariance | 样本少更可靠→共享Σ→linear classifier |
| 55 | Integral image | 任意矩形和 3 次加减法 |
| 56 | Haar-like feature | 两矩形 average gray value 差 |
| 57 | Viola-Jones | Haar+integral image+AdaBoost；180k→100 feature |

---

## 十、应试策略

1. **Histogram equalization 题**：先认出 impulse 形式（a=高度、b=位置）→ 算累加 `c(f)=Σp_f(t)` → 再归一化到 [0,L] 取整。**千万别只写归一化公式**。
2. **卷积计算题**：用 weighted sum 思想，filter mask 翻转后与图像窗口对应相乘求和，输出在 mask 中心。
3. **Fourier 性质题**：记住 translation 只改 phase（magnitude 可作识别特征）、离散卷积需 zero padding、rectangle↔sinc。
4. **MAP / classifier 题**：写 discriminant function，Gaussian 下核心是 Mahalanobis distance；区分三种情形（quadratic/linear/min distance）的假设条件。
5. **PCA 题**：写推导链（mean→投影方差→S_T→Lagrangian→特征方程）；eigenvector=最大方差方向，eigenvalue=方差值，重建误差=未选 eigenvalue 之和。
6. **LDA 题**：Fisher criterion、S_W⁻¹S_B 特征方程、S_T=S_W+S_B、S_W 不满秩用 Fisherfaces。
7. **概念辨析题**：feature extraction vs selection、PCA vs LDA（unsupervised vs supervised）、mean vs median filter。
8. **不会的别空着**：写对公式与思路有过程分；尤其 HE 累加式、Mahalanobis distance、Fisher criterion 这些有物理意义的公式务必写上。
