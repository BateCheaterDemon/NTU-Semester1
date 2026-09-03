# EE6222 — Machine Vision（机器视觉）

> 课程学习笔记总览。每周一节，按周总结重点内容。
> 第一周（开课周）特别关注考核要求、任课教师、课程结构等行政性信息。
>
> **权威来源说明**：本笔记先由各周录播转写（`week1.txt`、`week2.txt`…）整理，再以 `EE6222_lecturenote1to9.pdf`（官方讲义，Jiang Xudong，2026-08-11）核对修正。转写有大量语音识别噪声（如 "Ji Shi Dong" 实为 Jiang Xudong、"19/night" 实为 light、"cner/nel" 实为 color、"st g/quam" 实为 histogram、"ninear/menia" 实为 linear、"ATI" 实为 LTI、"compion" 实为 convolution、"fear/fuel" 实为 Fourier），均以 PDF 为准修正。

---

## Week 1 — 开课周：课程介绍 + Image Fundamentals + 卷积入门

### 1. 课程基本信息

- **课程名称**：EE6222 **Machine Vision**（机器视觉）。注意用词是 Machine Vision 而非单纯 Computer Vision——本课隶属 School of EEE（电气与电子工程学院），强调"机器"理解视觉信息。
- **任课教师**：
  - **前 9 周（Week 1–9，Topic 1–10）**：**Jiang Xudong**（exdjiang@ntu.edu.sg，IEEE Fellow，办公室 S1-B1c-105，个人页 personal.ntu.edu.sg/exdjiang）。Course coordinator，本课主导。背景：电子科大（UESTC）本科+硕士，德国汉堡大学 PhD，先后在 I2R 与 NTU（2004 起）工作。教学经历：C 编程、Signals & Systems、DSP、Image Processing & Computer Vision、Intelligent System Design、EE7401 Probability & Random Process、Machine Vision、EE7403 Image Analysis & Pattern Recognition。研究：fingerprint recognition → face recognition → pedestrian detection 等计算机视觉，近年转向 AI/深度学习。
  - **后 4 周（Week 10–13，Topic 11–14）**：**Dr. Cheng Jun**，负责 Video Analysis、Video Recognition、3D Machine Perception、3D Machine Vision。

#### 教学理念（老师反复强调，贯穿全课）

- 研究生学习不应停留在 **superficial understanding（表面理解）**，要追求 **in-depth understanding（深入理解）**——这是人类相对 AI 的优势所在。
- 老师对 AI 的观点：AI 本质是 **memory-based（记忆 + 插值/外推）**，靠海量数据记忆与内插；人类胜在 **understanding** 与创造。机器能在记忆/计算上超人（飞机飞得快不代表整体超人），但 in-depth understanding 难以被 AI 取代。
- 深入理解的两个方面：
  1. **把复杂技术直观化（intuition）**：真正理解后会发现复杂方法其实简单、自然、straightforward。第一步是找到复杂技术背后的 idea/intuition，而非死记复杂数学公式。
  2. **深入内部找关键因素**：在众多因素中找出起 major role 的关键少数。对已有信号系统/图像处理背景的同学，老师希望帮他们"看到本来看不见的东西、想到本来没想过的东西"。
- 考试**不要求死记（memorize）**，要求理解概念与方法。老师不"填鸭（spoon-feeding）"已知知识——那些 Google/AI 都能查到；老师的作用是启发理解。

#### 与 EE7403 的区别

EE7403（Image Analysis and Pattern Recognition，研究生课）与本课高度相似，但：
- EE7403 **不讲 3D / Video**，只聚焦 2D 图像；省下的 4 周用于更深入的传统机器学习与深度学习。
- 本课覆盖面更广（含 Video + 3D），但相应部分深度略浅。

### 2. ⭐ 考核要求（重要）

| 成分 | 占比 | 说明 |
|---|---|---|
| **Final Exam 期末** | **60%** | — |
| **CA（Continuous Assessment）** | **40%** | 见下方明细 |
| ┗ Quiz | 10% | **Week 7**，课堂内 30 分钟 |
| ┗ Assignment ×2 | 30%（各 15%） | take-home mini-project，写 report（论文形式）。一份来自 Jiang Xudong 部分，一份来自 Cheng Jun 部分 |

#### Assignment 规则（重点）

- 是 **mini-project**，要"做点东西"并写 report。
- **允许使用 generative model（AI）生成报告**，但学生须**对报告完全负责**：必须逐字审阅、理解、**纠正 AI 的错误**。AI 生成的句子有独特格式与隐藏错误，老师能识别——若原样照搬不改，判为 **wrong/作弊**。
- 关键原则：**用 AI 可以，但必须 go through details, understand, and correct the errors**。

#### 先修知识（Prerequisites）

- **Probability Theory 概率论**：预测不可能 100% 正确，需用概率度量不确定性；生成模型生成图像也基于训练数据的概率分布。只需掌握**基本概念**（PDF、概率分布等），后续多为这些基本概念的简单延伸。不用怕——只需 fundamental concepts。
- **Linear Algebra 线性代数**：极其重要。图像是海量数据，需用向量/矩阵表示与处理；要理解 high-dimensional space、projection（两向量相乘）。Transformer 的核心操作**全是矩阵乘法**——不懂线性代数会混淆"乘了几次到底得到什么、物理意义是什么"。线性代数不仅用于计算，更用于理解与表示方法。
- **Signals & Systems 信号与系统**：所有信号/图像处理的基础。其中：
  - **convolution（卷积）** 是 CNN（Convolutional Neural Network）的起源——不懂卷积就无法理解 CNN 如何彻底改变机器从数据中学习的方式。
  - Transformer 中最重要的 **attention 本质是 correlation（相关）**，相关也在信号系统与概率论中学过。
  - 无此背景者（如软工/CS 部分同学未学过信号系统）需自行复习基本概念。

### 3. 课程内容总览（14 Topics，权威，取自 PDF Course Content 页）

| Topic | 内容 | 主讲 |
|---|---|---|
| 1 | Image Fundamentals and Human Perception | Jiang |
| 2 | LSI Systems and Transforms | Jiang |
| 3 | Image Denoising and Enhancement | Jiang |
| 4 | Intuitive Understanding of Object Recognition: from Matching to Classification | Jiang |
| 5 | MAP Decision and Classifiers | Jiang |
| 6 | Statistical Estimation and Machine Learning | Jiang |
| 7 | Handcrafted Feature Generation and Feature Selection | Jiang |
| 8 | Visual Data Dimensionality Reduction as Feature Extraction | Jiang |
| 9 | Neural Networks and Deep Machine Learning: from MLP to CNN | Jiang |
| 10 | Deep Learning: from CNN to Transformer | Jiang |
| 11 | Video Analysis | Cheng Jun |
| 12 | Video Recognition | Cheng Jun |
| 13 | Three-dimensional Machine Perception | Cheng Jun |
| 14 | Three-dimensional Machine Vision | Cheng Jun |

> **课程脉络**：
> - Topic 1–3：图像处理基础（image processing 基础）——机器视觉的"地基"。
> - Topic 4–5：识别/决策理论入门（从 matching 到 classification、MAP decision）。
> - Topic 6–8：传统机器学习（统计估计 → 手工特征生成 → 特征选择/降维提取）。
> - Topic 9–10：深度学习（MLP → CNN → Transformer）。
>
> 老师强调：现代 AI 的强大在于 **feature extraction（特征提取）**——CNN/Transformer 都在特征提取上极强，因而最终分类层只需一个简单 **linear classifier**。本课先讲传统手工特征，再讲深度学习如何自动学到远胜手工的特征。

### 4. 教材

- **Davies E. R.**, *Computer Vision: Principles, Algorithms, Applications, Learning*, Elsevier, 2017.
- **Gonzalez & Woods**, *Digital Image Processing*, Prentice Hall.（图像处理最佳教材）
- **Duda, Hart & Stork**, *Pattern Classification*, Wiley, 2001.（模式分类最佳教材）
- 可能补充近期 research papers。

---

### 5. Topic 1 — Image Fundamentals & Human Perception（详细讲解）

#### 5.1 图像是什么

- **物理定义**：image 是 **3D 场景/物体在 2D 上的投影**（a two-dimensional projection of a three-dimensional scene），是对物体或场景的视觉表征。
- **数学定义**：单通道（灰度）image 是**二维空间坐标的函数** `f(x, y)`——在不同空间位置 (x, y) 处取不同的亮度/灰度值。x, y 指定平面上一点，f 的值表示该点的 intensity / brightness / gray level（同一概念不同名字）。
- **数字图像（digital image）**：对连续 2D 光强函数做两步离散化得到：
  1. **Spatial sampling（空间采样）**：把连续空间坐标 (x, y) 在等距矩形网格上离散化。
  2. **Gray-level quantization（灰度量化）**：把幅度 f 也离散化为有限级数。
  - 结果：x, y, f 全是有限离散值。x, y 取整数；f 理论/计算机中可为任意值（0.1, 0.2…），存文件时才转整数。
- **矩阵表示**：数字图像 = 一个 `m×n` 矩阵，每个元素是一个 **pixel（像素）**，元素值为该位置的 gray level。
  ```
  F = [f(1,1) ... f(1,n); ...; f(m,1) ... f(m,n)]
  ```
- **一句话**：研究图像 = 研究一个 2D 函数 = 研究一个矩阵，没有更多。

#### 5.2 图像形成（Image Formation）三要素

图像由三个 component 形成：

1. **Light source 光源**：
   - 在信息处理意义上，light 是 **waveform（波形）**（物理上也是粒子，但此处按波处理）。
   - 可见光有频率/波长范围（约 **350–780 nm**）。频率与波长互为倒数关系（×光速）。
   - **太阳光（sunlight / white light）**：含许多频率成分，且各频率强度**几乎均匀** → 人眼感知为 **白色（white color）**。
   - 可用 **optical prism（棱镜）** 验证：光从一种介质进入另一种介质会 **bend（弯折）**，因为不同介质密度不同、光速不同；不同频率弯折角不同 → 棕色分解出不同频率成分 → 人眼看到不同颜色。光的弯折遵循"最短时间原则"（光总走时间最短的路径）。
   - 一般光源的强度是频率的函数：不同频率强度可能不同。

2. **Object 物体**：
   - 物体反射光。**reflectivity（反射率）ρ(λ) 也是频率的函数**——不同材料/物体对不同频率反射率不同。
   - 即使白光（各频率均匀）照射，因反射率随频率不同，反射出的光也会呈现不同 **color**。这是"白光下物体仍显色"的根本原因。

3. **Lens + Sensor array 透镜与传感器阵列**：
   - **Sensor array**：在空间平面上排布大量传感器，不同位置传感器接收不同强度的光 → 形成图像。
   - **Lens 透镜**的作用（关键理解）：确保 sensor 平面上**一个位置只接收来自物体一个对应位置的光**（聚焦），防止其他位置的光混入。
     - 若无透镜，一个传感器会收到来自四面八方的光 → 无法成像。
     - 透镜让"一点对一点"成为可能，这是成像的必要条件。
   - **替代方案：小孔成像（pinhole）**——极小（近零直径）孔径也能成像，原理与透镜相同（一点对一点）。
   - ⭐ **老师留给学生的思考题**：透镜 vs 小孔的优缺点对比？
     - 小孔缺点：进光量极小（孔径太小）。
     - 透镜优势：能汇聚更多光（大孔径 + 聚焦）。
     - 小孔的相对优点：（留作思考——例如无焦距/景深问题，成像几何最简单）。
     - 找到答案 = 真正理解透镜在成像系统中的作用。

#### 5.3 亮度公式（Luminance / Intensity）

- 物体一点反射的光：
  - **`I(λ) = ρ(λ) · L(λ)`**
  - ρ(λ)：物体 reflectivity；L(λ)：光源光谱能量分布（spectral energy distribution）；λ：波长（可见光谱 350–780 nm）。
- 传感器接收的空间分布亮度：
  - **`f(x, y) = ∫₀^∞ I(x, y, λ) · V(λ) dλ`**
  - **V(λ)**：视觉系统的 **relative spectral sensitivity function（相对光谱灵敏度函数）**，钟形曲线（bell-shaped）。
- **V(λ) 本质上是一种 frequency response（频率响应）**：
  - "response"=output。对不同频率的**相同**输入，V(λ) 决定输出大小不同——某频率处输出接近 1（不抑制），另一频率处输出接近 0（抑制）。
  - 即使输入在各频率上是常数，传感器输出也因 V(λ) 而随频率变化。
- **关键点**：单个传感器对所有频率积分累加，**只输出一个值**，本身**没有频率信息**——单个传感器收到的只是光的能量总量。那么颜色从何而来？→ 见下节。

#### 5.4 颜色感知（Human Perception of Color）

- **人眼有三类 cone（视锥细胞）**，形状像 cone，分别记为：
  - **L（red 红）、M（green 绿）、S（blue 蓝）**——对应视网膜中不同比例的三类 sensor。
  - 每类有不同的 spectral sensitivity function V₁(λ), V₂(λ), V₃(λ)。
- 给定一束光，三类 cone 各输出一个值：
  - **`f_k(x, y) = ∫₀^∞ I(x, y, λ) · V_k(λ) dλ`**，k = 1, 2, 3.
- 这三个**相对值** (f₁, f₂, f₃) 的不同组合 → 人脑感知为不同 **color**。
  - 例：某频率光使三个 sensor 输出 (强, 弱, 强) → 感知为某色；若第二个 sensor 输出是另两个的两倍、另两个接近 → 感知为绿色。
  - 即：颜色不是单由"光的频率"决定，而是由三类 sensor 输出的**相对值**决定。
- **三原色（Color Primaries）**：
  - **Additive primaries（加色三原色）**：Red(R)、Green(G)、Blue(B)——用于发光设备。
  - **Subtractive primaries（减色三原色）**：Cyan、Magenta、Yellow——用于打印。
- **Color 是 3D 空间中的一点**：
  - 任意 color 可由三原色按量组合：`c = a·p₁ + b·p₂ + c·p₃`，其中 (p₁,p₂,p₃) 是某组 primaries。
  - 以 RGB 为坐标轴，一个 color = 3D color space 中一个点。
  - 指定同一点可用**不同坐标系**（旋转轴即可），因此有不同 **color space**。
- **常见 color space**（PDF p.15）：
  | Color space | 含义/用途 |
  |---|---|
  | **RGB** | hardware oriented，用于 monitors、video cameras |
  | **rgb** | Normalized RGB（归一化） |
  | **CMY** (Cyan-Magenta-Yellow) | 彩色打印机 |
  | **YIQ** (luminance, in-phase, quadrature) | 彩色电视广播 |
  | **HSI / HSV** (Hue-Saturation-Intensity/Value) | 便于颜色操作 |
  | **CIE-Luv, CIE-Lab** (lightness, red-green, yellow-blue) | 颜色区分 |
  | **sRGB** | 设备无关的数字图像显示 |
- **历史注**：deep learning 前，传统方法多只处理**单通道 gray-level image**（无颜色）；deep learning 后算力允许直接处理 **3 通道 RGB** 输入。老师相关研究：color channel fusion（融合多通道提升识别，IEEE SPL 2015）、color space construction（优化亮度/色度分量，PR 2018）。
- 本课后续只研究单通道（更简单），彩色只是单通道扩展到三通道，无本质区别。

#### 5.5 空间分辨率 vs 灰度分辨率

- **Spatial resolution（空间分辨率）**：指采样所得 m×n 阵列的尺寸。同一物体用更大尺寸表示 → 高分辨率 → 图像 **sharp / clear**；小尺寸 → 低分辨率 → **blurred**。
  - 注意：低分辨率图若显示在小区域看起来也清楚（因为没放大）；放大到与高分辨率图相同显示面积时才明显模糊。
  - PDF 例：600×408 / 300×204 / 150×102。
- **Gray-level resolution（灰度分辨率）**：量化级数 **`g = 2^b`**，b 为每像素比特数。
  - 8 bit → 256 级（常见最高）；级数减少：128/64/32/16/8/4/2 级。
  - 2 级 → **binary image**（只有黑白）。

#### 5.6 ⭐ Image Histogram（图像直方图）— 本周重点之一

##### 定义
- 数字图像 f(x,y) 灰度范围 [0, L] 的 histogram 是离散函数：
  - **`p_f(f) = n_f / n`**
  - f = 0,1,2,…,L 为某 gray level；n_f 为该灰度的像素数；n 为处理区域内总像素数（归一化）。
- 性质：**`p_f(f) ≥ 0`，且 `∑_{f=0}^{L} p_f(f) = 1`**（因为 n_f 对所有灰度求和 = n）。

##### 本质：频率分布 / 概率估计
- histogram 是 gray-level f 出现的**频率**。
- 若把像素灰度视为 random variable，histogram 是其概率的一个 **estimate（估计）**。

##### ⚠️ Histogram 与 PDF 的概念区分（老师强调学生易混淆）
- **PDF / 概率**：是**理论值**，描述一整类图像（如"人脸图像的灰度分布"）的客观可能性，用于期望未来。男性人脸与女性人脸的 PDF 会不同。
- **Histogram**：是**统计值**，由**一张**实际图像算出，是 PDF 的一个 estimate。真实概率未必恰好等于这张图算出的 histogram。
- 关系类比：**probability vs statistics**——statistics 用实际可得数据计算，probability 是理论值用于期望未来；用样本（population）去估计概率以期望未来。
- 有些教材/老师直接把 histogram 叫"图像的 PDF"，但**概念不同**，要分清。

##### 直方图的形状解读图像特征
| 直方图形状 | 图像特征 |
|---|---|
| **窄分布**（集中在小灰度范围） | **低对比度（low contrast）**——像素间差异小 |
| 集中在低灰度端 | 暗图像（曝光不足 under-exposure） |
| 集中在高灰度端 | 亮图像（曝光过度 over-exposure） |
| **双峰（bimodal）** | 含一个物体（窄灰度范围）落在不同灰度背景上；峰的大小反映面积，可据此判断物体/背景 |
| **展布全范围、各级近似均匀** | 理想清晰图像（人眼最舒服） |

- 双峰例：大峰（多像素、高灰度）= 大面积亮背景；小峰（少像素、低灰度）= 小面积暗物体。但背景内部灰度仍有小差异（非单一值）。

##### 直方图丢失空间信息
- histogram 只统计"某灰度有多少像素"，**不记录像素在哪**——spatial information 完全丢失。
- 但**信息减少未必是坏事**：很多任务需要去除与目的无关的冗余信息、保持对某类图像的不变性（invariance）。
- **重要原则**：**任何信息处理系统只能减少信息，不能增加信息**。系统若人为创造输入中没有的信息 = fake information = wrong。所有处理系统的目标都是为特定任务**减少冗余信息**。

##### Histogram 作为特征（deep learning 前的经典手工特征）
传统手工特征最终常转化为 histogram：
- **LBP（Local Binary Pattern）**：把每个像素与其邻域比较生成二进制码，用该码的 **histogram**（每种码有多少像素）作识别特征。
- **HOG（Histogram of Oriented Gradients）**：计算图像梯度方向，对不同方向/朝向统计 **histogram** 作特征。
- 老师课题组在 IEEE TIP 等期刊发表了大量基于 histogram 特征的工作（LBP 编码方案、HOG 子空间等）。

##### Histogram Equalization（直方图均衡化）— 预告
- 给定图像，变换为直方图更均匀的输出图像以增强对比度。
- 难点：变量从空间函数 f(x,y) 转为灰度的函数 p_f，学生常在此处困惑（这本身就是一种 transform）。后续会详细讲。

#### 5.7 Image Processing 及其应用

- **定义**：对数字图像（2D 函数/矩阵）进行一系列机器/计算机操作得到期望结果；操作须用数学描述。所用数学很简单（integration、differentiation、summation），关键是理解**物理意义**。
- **为什么需要**：visualization、image understanding、自动导引车、机器人视觉伺服、安防、信息检索等。
- **典型应用举例**（PDF p.29–43）：
  | 任务 | 说明 |
  |---|---|
  | **Contrast enhancement 对比度增强** | 暗区增对比度，代价是亮区对比度降低；因大区域在暗部，整体收益大于损失 |
  | **Deblurring 去模糊** | 模糊输入→锐化输出，代价是产生 artificial structures |
  | **Denoising 去噪** | 中值/非线性滤波可去除**幅度大但空间稀疏（spatially sparse）**的噪声 |
  | **Beautifying 美化** | 平滑细节 |
  | **Restoration & retouching 修复** | 老照片增强、补色 |
  | **Segmentation 分割** | 分离不同物体/器官/肿瘤（生物医学） |
  | **Digital watermarking 数字水印** | 在图像中隐藏不可见信息，可程序检索 |
  | **Content tampering detection 篡改检测** | 检测合成/篡改图像（含深伪）；LA Times 摄影师因合成照片被辞退案例 |
  | **Object/Face detection & recognition** | 检测与识别 |
  | **Signature verification** | 笔迹识别/验证 |
  | **Biometrics 生物识别** | fingerprint、face、signature、palmprint、iris、gait、ear 等 |

---

### 6. Topic 2 — LSI Systems & Transforms（本周讲到卷积为止）

> 转写结尾明确："下周讲 Fourier transform"。故本周覆盖 Topic 2 的 **image decomposition + 2-D convolution**，**Fourier transform 与 image sampling 留到 Week 2**。

#### 6.1 为什么学 LSI 系统

- 图像在**空间域（spatial domain）**，对应时域信号的 **LTI（Linear Time-Invariant）系统**；图像处理用 **LSI（Linear Shift-Invariant，线性移不变）系统**。
- **卷积（convolution）+ Fourier transform 是所有信号/图像处理的两大支柱**。两者都建立在 **signal decomposition（信号分解）** 这一核心思想上：把任意信号/图像分解为基本函数之和。理解分解，卷积和 Fourier 都顺理成章。
- 即便神经网络/CNN/Transformer 是非线性的，其**可学习参数部分都是线性的**——非线性来自**固定的、不可学习的 activation function**。人类能设计、能大规模计算的只有线性部分；非线性只能针对特定任务设计。因此**线性系统至关重要**。
- 本 Topic 还讲 **image sampling（图像采样）**，因为采样**桥接连续域与数字域**：虽然现在媒体都是数字的，但连续函数有丰富的数学工具（微分、积分、闭式结果），离散域工具贫乏；理论分析常在连续域做，再通过采样回到数字域。

#### 6.2 基本元素：Impulse（冲激）

- 数字图像的基本元素是 **impulse**：
  - **`δ(x, y) = 1 if x=y=0, else 0`**（离散情形，值为 1）。
- ⚠️ **连续情形 impulse 必须为无穷大**——这是学生常困惑处，老师专门澄清：
  - 连续函数中若只有"单一点非零"，该点值不能是有限的，必须为 **infinity**，否则积分（面积）为零、没有意义。
  - 离散情形则可以是有限值 1（一个点取 1 即可）。
  - 采样理论中会进一步讨论连续 impulse。
- 利用 impulse 可表示**任意单像素**：位置 (i, j)、灰度 c 的像素 = **`c · δ(x−i, y−j)`**（x=i, y=j 时 δ(0,0)=1，乘 c 得 c；其余位置为 0）。
- **1 和 0 的优良性质**（impulse 作为分解基的好处的根源）：
  - 1 乘任何数不变（保留该值）。
  - 0 乘任何数为 0；无穷多个 0 求和仍为 0（不干扰其他点）。
  - → 用 impulse 叠加表示图像时，各点互不干扰。

#### 6.3 Image Decomposition（图像分解）

- 任意图像可表示为**移位、缩放的 impulse 之和**：
  - **`f(x, y) = ∑_{i,j} f(i, j) · δ(x−i, y−j)`**（有限图像则求和范围为图像尺寸）。
- **例**：以 (0,0) 为中心、灰度 215、大小 11×11 的方块：
  - `f(x,y) = ∑_{j=−5}^{5} ∑_{i=−5}^{5} 215 · δ(x−i, y−j)`。
- 这是卷积推导的起点：把图像分解为 impulse 的加权和，再让系统对每个 impulse 响应并叠加（线性）。

#### 6.4 ⭐ 2-D Convolution（二维卷积）— 本周重点之二（完整推导）

设处理系统把输入 f(x,y) 映射为唯一输出 g(x,y)：`g(x,y) = T{f(x,y)}`。

**第一步：代入图像分解**
```
g(x,y) = T{ ∑∑ f(i,j) · δ(x−i, y−j) }
```

**第二步：若系统是线性的**（可把 T 移入求和）
```
g(x,y) = ∑∑ f(i,j) · T{δ(x−i, y−j)}
```

**第三步：定义 impulse response（冲激响应）**
```
h(x,y) ≜ T{δ(x,y)}     （输入 impulse 时的输出图像）
```

**第四步：若系统是 shift-invariant 的**（输入移多少、输出也移多少）
```
T{δ(x−i, y−j)} = h(x−i, y−j)
```

**结果：LSI 系统的输出 = 输入与冲激响应的卷积**
```
g(x,y) = f(x,y) * h(x,y)
       = ∑∑ f(i,j) · h(x−i, y−j)
       = ∑∑ h(i,j) · f(x−i, y−j)      （交换律形式）
```

- **核心结论**：一个 LSI 系统**完全由其 impulse response h(x,y) 刻画**。
- h(x,y) 的别名：**spatial representation of a filter / filter mask / filter coefficients / filter parameters**。
- 为加速处理，h 通常是**小尺寸图像**（3×3, 5×5, …, 11×11），而普通图像是 256×256 量级。
- 当 h 仅在 −3 < x,y < 3 非零时，求和范围缩小到 3×3 窗口。

#### 6.5 卷积性质

- **Commutative 交换律**：`f*h = h*f`。
- **Associative 结合律**：`f*(h₁*h₂) = (f*h₁)*h₂`。
- **Distributive 分配律**：`f*(h₁+h₂) = f*h₁ + f*h₂`。

#### 6.6 理解卷积的例子（老师重点示范）

**需求**：抑制随机噪声 / 平滑图像，使图像"soft"——做局部平均：输出像素 = 该像素 + 4 邻域像素之和。

**数学表达**：
```
g(x,y) = f(x,y) + f(x−1,y) + f(x+1,y) + f(x,y−1) + f(x,y+1)
```

**对应 impulse response**：
```
h(x,y) = δ(x,y) + δ(x−1,y) + δ(x+1,y) + δ(x,y−1) + δ(x,y+1)
```

**filter mask 表示**（3×3）：
```
0 1 0
1 1 1
0 1 0
```
（四连通邻域 + 中心，各权重 1）

#### 6.7 卷积数值例（PDF p.52）

3×3 卷积核 h 与图像 f 卷积，求 g(4,4)：
```
g(4,4) = ∑_{j=−1}^{1} ∑_{i=−1}^{1} h(i,j) · f(4−i, 4−j)
```
PDF 中 h 为 [[1,2,3],[4,5,6],[7,8,9]]，f 对应窗口为相应像素，则：
```
g(4,4) = 7·1 + 5·2 + 3·3 + 9·4 + 8·5 + 7·6 + 9·7 + 6·8 + 5·9
```
- **物理意义**：在每点 (x,y)，滤波器响应 = filter coefficients 与滤波窗口内对应像素的**乘积之和**。

#### 6.8 学生难点 + CNN 翻转问题（老师剖析）

**为什么卷积看似简单却让学生觉得难？**
- 公式中 **(x, y) 是变量，(i, j) 是求和下标（running index）**——这是关键区别。
- 为算**一个**输出值 g(x,y)，需要 (i,j) 遍历整个范围，即用到**全部**输入像素与**全部**滤波器系数，却只产生**一个**输出值。
- 这种"输入全用、输出一个"的不对称让人觉得反直觉。但概念其实 straightforward。

**CNN 中卷积核要不要翻转（flip）？**
- 老师：**翻转与否不影响结果**——只要**训练与推理过程一致**即可。因为滤波器值是从数据**学到的**：
  - 训练翻转、推理也翻转 → 没问题。
  - 训练不翻、推理也不翻 → 没问题。
  - 训练不翻、推理翻转 → 全错。
- 严格数学卷积需翻转 h（用 f(x−i)），但 CNN 实践中"相关（correlation）"与"卷积"效果等价，因为参数是学出来的。

**卷积的革命意义**（预告）：
- 若没有卷积被引入机器学习，就不会有今天的 AI 模型。**卷积借入机器学习是革命性改变**——彻底改变了机器从数据中学习的方式。
- Week 8/9 会讲它为何如此重要、CNN 如何在哪些方面超越所有传统机器学习方法（CNN 发明者 Hinton 因此获 Nobel Prize）。

### 7. 本周与下周衔接

- **本周实际进度**：Topic 1（Image Fundamentals）全讲完 + Topic 2 讲到 image decomposition 与 2-D convolution。
- **下周（Week 2）预告**：继续 Topic 2，讲 **Fourier transform（傅里叶变换）**——2-D Fourier / DFT 及其性质（periodicity、conjugate symmetry、linearity、convolution theorem、translation、rotation）、image sampling 与 Nyquist 采样定理。

---

## Week 2 — Topic 2 续：Fourier Transform / DFT / Image Sampling ＋ Topic 3 起：Point Processing 与 Histogram Equalization

> **本周权威来源说明**：由 `week2.txt` 转写整理，以 `EE6222_lecturenote1to9.pdf` 第 53–83 页核对修正。本周转写噪声尤其严重，典型错拼对照：
>
> | 转写错拼 | 实际术语 |
> |---|---|
> | fear / fue / fuel / fluid / full year / free / fi / fid transform | **Fourier transform** |
> | full year theory | **Fourier series** |
> | same wave / say / cos and say | **sine wave / sinusoid**（cosine and sine） |
> | impasse / impulse tr / impasse ray / array / string | **impulse / impulse train** |
> | sync function | **sinc function** |
> | no pass / no path / no puss filter | **low-pass filter** |
> | Niclie rate / cse rate | **Nyquist rate** |
> | st gram / hestogram / se qui / squa / hem / HQ / cystogram / scram | **histogram** |
> | gama / comma correction | **gamma correction** |
> | no garism / ngithm / no go transform | **log transform** |
> | environment / enviart / vari / v | **invariant**（⭐ 如 "rotation environment" 实为 rotation invariant） |
> | grid value / gvalue / qui value / ge value | **gray value / gray level** |
> | AI system / T system / SI system | **LSI system** |
> | snope / nine | **slope / line** |
> | poredic / potic | **periodic** |
> | congugate | **conjugate** |
> | z padding | **zero padding** |
> | 19 strengths | **light strength（光照强度）** |
> | TJ Palm Master | **IEEE TPAMI** |
> | pica / pratica / pritic / predicon | "pretty clear"（老师口头禅） |

### 1. 承上：为什么还要学 Fourier transform

- 上周结论：空间域处理 = 输入与 impulse response 的 **convolution**。老师再次强调：**整个 signal processing 只有两根支柱**——**convolution** 与 **transform**。
- 两者同源于一个核心思想 **signal decomposition（信号分解）**：
  - **Convolution**：把信号分解为 **impulse** 之和 → 得到卷积。
  - **Fourier transform**：把信号分解为 **sinusoid（正弦波）** 之和 → 得到频谱。
  - 抓住"分解"这一点，两者都顺理成章。
- **为什么不能只学 deep learning？**（老师回应学生提问）
  - 有学生问："计算机视觉现在都用 deep learning 和 Transformer，还需要 Fourier transform 吗？传统理论是不是过时了？"→ **不是**。
  - 老师 2025 年发表于 **IEEE TPAMI** 的工作（*Revisiting One-stage Deep Uncalibrated Photometric Stereo via Fourier Embedding*）就是例子：对图像做 Fourier transform 后分离 **magnitude 与 phase**——
    - **magnitude** 与**光照强度（light strength）**密切相关；
    - **phase** 与**物体的结构（structure）**密切相关。
  - 借此可从**单张 2-D 图像**估计 **3-D 信息**（photometric stereo），当然还要配合 deep model。
- **为什么学过那么多种 transform？** Fourier series → 连续 Fourier transform → **DTFT** → **DFT** → **FFT** → 及其他变换。老师：**它们全部来自同一个 idea**；彻底理解其中一个，其余都是简单扩展，不必分别死记。

### 2. 1-D 连续 Fourier Transform：定义与物理意义

#### 2.1 定义（PDF p.53）

```
正变换：  F(u) = ℑ{f(x)} = ∫_{−∞}^{∞} f(x)·exp(−j2πux) dx
逆变换：  f(x) = ℑ⁻¹{F(u)} = ∫_{−∞}^{∞} F(u)·exp(j2πux) du

其中  exp(j2πux) = cos(2πux) + j·sin(2πux)，  j = √(−1)
u 为 frequency variable，x 为时间/空间变量
```

- 存在逆变换 ⇒ **Fourier transform 是 lossless transform（无损变换）**：变换后不丢失任何信息，可由 F(u) 完全恢复 f(x)。

#### 2.2 ⭐ 从逆变换读出物理意义（老师的讲法：先看逆变换）

- 把积分理解成求和（**integration 与 summation 完全等价**，只是一个用于连续、一个用于离散；离散信号"可数"故用 Σ，连续信号"不可数"故用 ∫）。
- 于是逆变换在说：**任意信号 f(x) = 许多 sinusoid 之和**。
  - 求和的"基函数"是 `exp(j2πux)`——它的实部是 cosine、虚部是 sine，**本质就是一个 sine wave**。
  - `F(u)` 不是 x 的函数，只是每个频率上的**缩放因子（复数）**。
- ⭐ **F(u) 的物理意义**：
  - **|F(u)|（magnitude）** = 频率 u 处那个 sinusoid 的 **amplitude（幅度）**；
  - **∠F(u)（phase）** = 该 sinusoid 的 **initial phase（初相位）**。
  - 因为 F(u) = |F(u)|·exp(jφ(u))，与 exp(j2πux) 相乘时**指数相加**，φ 自然落进 cos/sin 的相角里。
- **一句话**：任意信号 = 不同频率的 sinusoid 之和，每个频率的幅度与初相位由 F(u) 这个复数给出。

#### 2.3 为什么用 complex exponential 而不直接用 cos / sin？

老师专门澄清（学生最怕复数）：**引入复指数是为了带来方便，不是为了增加难度**。

- 复指数相乘 = **指数直接相加**：`e^{jα}·e^{jβ} = e^{j(α+β)}`，极其简洁。
- 若用实函数：`cos α · cos β = ½[cos(α+β) + cos(α−β)]`，非常繁琐。
- 相位的处理也因此变得 straightforward（相位就在指数里，相乘即相加）。

#### 2.4 ⭐ 正变换为什么"挑得出"某个频率（关键直觉）

设 f(x) 只含单一频率 u₀（写成 `exp(j2πu₀x)`），代入正变换：

```
F(u) = ∫ exp(j2πu₀x) · exp(−j2πux) dx = ∫ exp[j2π(u₀−u)x] dx
```

- **若 u = u₀**：指数相消 → 被积函数 = 常数 1 → `∫_{−∞}^{∞} 1 dx = ∞`（极大值）。
- **若 u ≠ u₀**：被积函数仍是一个 sinusoid → 在整个周期上积分 = **0**（半个周期给出 ±1，与无穷相比可忽略）。

⭐ **结论**：`F(u)` 只在信号真实含有的频率处非零，其余处为零。若 f(x) 含多个频率成分，改变 u 就能**逐个提取**各频率成分的幅度与相位。这正是 Fourier transform 的工作原理，也再次体现复指数的便利（相乘只需看指数和是否为常数 0）。

### 3. 复数与复函数（老师专门复习的部分）

学生对复函数的恐惧其实源于对复数本身不清楚。老师的观点：**复函数的所有性质与复数完全一样**。

- **复数本质 = 把两个数放在一起研究**。很多场景本就需要同时研究两个数（如地图上指定一个位置必须用两个数）。用 `j` 把两个数隔开而已。
- 两种坐标系表示同一个点：
  - **Cartesian（直角）**：`c = a + jb`，横轴 real part、纵轴 imaginary part。
  - **Polar（极坐标）**：`c = r·e^{jφ}`，r 为 magnitude、φ 为 phase/angle。
  - 互换（PDF p.55）：`a = r cos φ`，`b = r sin φ`；`r = √(a²+b²)`，`φ = tan⁻¹(b/a)`。
- 对 Fourier transform：
  ```
  F(u,v) = R(u,v) + jI(u,v) = |F(u,v)|·exp[jφ(u,v)]
  |F(u,v)| = √(R² + I²),    φ(u,v) = tan⁻¹(I/R)
  R = |F|cos φ,             I = |F|sin φ
  ```
- 需要额外记的只有一件事：**j = √(−1)**。除此之外没有别的。

### 4. 2-D Fourier Transform 与 Separability

#### 4.1 定义（PDF p.53）

图像是二元函数，2-D FT 只是 1-D 的**简单扩展**：

```
F(u,v) = ∫∫ f(x,y)·exp[−j2π(ux + vy)] dx dy
f(x,y) = ∫∫ F(u,v)·exp[ j2π(ux + vy)] du dv
```
u 是沿 x 方向的频率，v 是沿 y 方向的频率。

#### 4.2 ⭐ Separable（可分离性，PDF p.54）

利用复指数的良好性质 `exp[−j2π(ux+vy)] = exp(−j2πux)·exp(−j2πvy)`：

```
F(u,v) = ∫ [ ∫ f(x,y)·exp(−j2πux) dx ] · exp(−j2πvy) dy
       = ∫ F_x(u,y) · exp(−j2πvy) dy
```

- **含义**：2-D Fourier transform = **做两次 1-D Fourier transform**——先把 x 当变量做一次，再把 y 当变量做一次。可同理推广到 N 维。
- ⚠️ **PDF 上的问号（易错）**：`F(u,v) = F_x(u)·F_y(v)` **只有在 f(x,y) = f₁(x)·f₂(y) 时才成立**（即图像本身可分离）。"变换可分离计算"与"结果可写成乘积"是两回事，不要混淆。
- 若用 cosine/sine 实函数则无法轻易拆成两个因子相乘——这又一次体现了复指数的优势。

### 5. DFT（Discrete Fourier Transform）

#### 5.1 定义（PDF p.56）

对 m×n 的离散图像 f(x,y)：

```
F(u,v) = Σ_{x=0}^{m−1} Σ_{y=0}^{n−1} f(x,y)·exp[−j2π(ux/m + vy/n)]

f(x,y) = (1/mn) Σ_{u=0}^{m−1} Σ_{v=0}^{n−1} F(u,v)·exp[ j2π(ux/m + vy/n)]
```

- **与连续 FT 相比，唯一的区别是把 integration 换成 summation**——没有别的区别。
  - 连续定义用 −∞ 到 ∞ 是为了通用；对具体数字图像，求和只需覆盖图像范围（图像外视作 0，加零不改变结果）。
- **常数 `1/mn` 不重要**：可放在正变换、可放在逆变换，有的教材两边各放 `1/√(mn)`。老师用绿色标注它、明确说**不必记忆**——因为图像处理关心的是变换域内的**相对值**，统一乘常数不影响任何结论。

#### 5.2 ⭐⭐ 为什么定义里要除以 m、n？（老师花最多时间讲的"为什么"，重点理解）

推理链条如下：

1. **frequency = period 的倒数**（连续、离散都一样）。
2. **离散信号的 period 是什么？** 连续信号的周期是一段"时间长度"（可以是 1 毫秒、1 小时，任意实数）；但离散信号只有采样点，其周期只能是**一个周期内包含多少个点**。
3. 于是 **离散信号的 period 必须 ≥ 1**（不可能是 0.5 个点；最短周期是 2 个点，即 `1, −1, 1, −1, …`）。
4. **period ≥ 1 ⇒ frequency ≤ 1**。所以离散信号的频率**不可能大于 1**；若取 1.5，它等价于 0.5（`cos(2π·1.5·x)` 与 `cos(2π·0.5·x)` 在整数 x 上完全相同，可自行验证）。
5. 这正是 **DTFT（Discrete Time Fourier Transform）** 的情形：x, y 离散（整数），但 u, v **连续**且只取 [0, 1) 内的值。
6. **但我们希望 u, v 也是离散整数** 0, 1, 2, …, m−1，好逐点计算。离散值来自对连续量采样 → 需要把 [0, 1) 这段区间采成 m 个点。
7. **办法就是在指数里除以 m、n**：`ux/m` 中，当 u 取 0…m−1 时，`u/m` 恰好落在 [0, 1) 内。

⭐ **一句话**：`/m`、`/n` 的唯一作用，是把频率变量的取值范围从 [0,1) **拉伸**到 [0, m)、[0, n)，从而让 u, v 也能取整数。这就是 DTFT 与 DFT 的全部差别。

| | x, y | u, v | 说明 |
|---|---|---|---|
| 连续 FT | 连续 | 连续，(−∞, ∞) | 数学工具最丰富 |
| **DTFT** | 离散（整数） | **连续，但必须 ∈ [0,1)** | 不除以 m、n |
| **DFT** | 离散（整数） | **离散整数，0…m−1 / 0…n−1** | 除以 m、n 才能实现 |

#### 5.3 DFT 的 separability

与连续情形完全一样（求和与积分具有相同性质）：给定图像，**先对每一行做 1-D DFT，再对每一列做 1-D DFT**，即得 2-D DFT（PDF p.57 的 Row Transforms → Column Transforms 示意图）。

### 6. ⭐ DFT 的性质（PDF p.58–59）

| 性质 | 表达式 | 理解 |
|---|---|---|
| **Periodicity** | `F(u,v) = F(u+m,v) = F(u,v+n) = F(u+m,v+n)` | 源于离散信号频率只能落在 [0,1)（除 m 后为 [0,m)），超出范围只是**重复自身** |
| **Conjugate symmetry**（实图像） | `F(u,v) = F*(−u,−v)`，`\|F(u,v)\| = \|F(−u,−v)\|` | m×n 个**实数**变换后得到 m×n 个**复数**（信息量 2 倍）→ 必然冗余，只有一半是真信息。含义：**magnitude 偶对称、phase 奇对称** |
| **Linearity** | `ℑ{αf₁ + βf₂ + …} = αF₁ + βF₂ + …` | 由定义直接可得，FT 是线性变换 |
| **Scaling** | `ℑ{f(αx, βy)} = (1/\|αβ\|)·F(u/α, v/β)` | 一个域**拉伸** ⇔ 另一个域**压缩**。例：常数（极平坦）↔ impulse（只含零频）；impulse（变化极快、含丰富频率）↔ 极平坦的谱 |
| ⭐ **Convolution theorem** | `f(x,y)*g(x,y) ⇔ F(u,v)·G(u,v)`<br>`f(x,y)·g(x,y) ⇔ F(u,v)*G(u,v)` | 一个域的卷积 = 另一个域的相乘。见下方⚠️ |
| **Translation** | `f(x−x₀, y−y₀) ⇔ F(u,v)·exp[−j2π(x₀u/m + y₀v/n)]` | 见下方⭐ |
| **Rotation** | `f(r, θ+θ₀) ⇔ F(ω, φ+θ₀)`（极坐标下） | 空间旋转 ⇒ 频谱同角度旋转 |

#### 6.1 ⚠️ Convolution theorem 的陷阱（老师特别强调，很多教材忽略）

- 这条性质**严格来说只对连续函数成立**。
- 对**离散**信号/图像，频域相乘对应的不是普通卷积，而是 **circular convolution（循环卷积）**。
- **解决办法：zero padding（补零）**。把信号/图像补零扩展到约两倍尺寸后，circular convolution 就等价于 linear convolution。
  - **为什么？** circular convolution 把整个信号首尾相接成一个"圈"，移位是 **circular shift**；补零使圈内一半是信号、一半是零，此时循环移位的效果与线性移位相同。
- ⭐ 考点：**要在数字图像上使用"频域相乘代替卷积"，两个信号都必须先做 zero padding**（PDF p.58 明确写着 "Apply zero padding!"）。

#### 6.2 ⭐ Translation ⇒ magnitude 是 translation invariant

- 平移只让频谱乘上一个 `exp(−j2π(x₀u/m + y₀v/n))` 因子，而**这个因子的模为 1**——它**只改变 phase，不改变 magnitude**。
- 即：常数背景上的一个物体，**移到任何位置，|F(u,v)| 完全相同**，变的只是相位。
- **为什么重要**：object recognition 要求"无论车停在画面哪里都能认出是车"，因此需要 **translation invariant 的 feature**。取 Fourier transform 的 **magnitude** 就天然具备这一不变性。

#### 6.3 Rotation ⇒ DFT **不是** rotation invariant → Polar Harmonic Transform

- 物体旋转，频谱同角度旋转（用极坐标表示最容易看出）。所以 DFT magnitude **不具备**旋转不变性。
- 原因：DFT 是沿 x、y **两条直角轴**做变换。
- **解决思路**：改用 **polar coordinate (r, θ)** 表示图像，沿 r 与 θ 两个轴做变换 → **Polar Harmonic Transform**，其 magnitude 即为 **rotation invariant**。
  - 老师工作：P. Yap, X. Jiang, A. Kot, *"Two Dimensional Polar Harmonic Transforms for Invariant Image Representation," IEEE TPAMI*, vol. 32, no. 7, 2010。

#### 6.4 频谱示例与画法

- ⭐ **经典变换对**：图像中一个 **rectangle / square** ⇔ 其频谱是 **2-D sinc function**（信号处理中著名的"矩形 ↔ sinc"对）。
  - PDF 例图中 sinc 的水平与垂直宽度**不相等**：因为整幅图像本身不是正方形，**相对整幅图像归一化后**那个方块并非正方形。
- 旋转物体 → 频谱同步旋转（示例图）。
- **两种画法表示同一个函数**：
  - **3-D plot**：三条轴，高度表示函数值；
  - **2-D image**：两条轴是坐标（图像域为空间坐标、频域为频率坐标），**用亮度表示函数值**。
- PDF 另附 FT 性质表与常用 **FT pairs 表**（p.63–64），老师说不逐条讲，需要时查表即可。

### 7. ⭐ Image Sampling（图像采样理论，PDF p.65–71）

#### 7.1 为什么要学采样理论

- 数字图像本来就是离散的，但**连续函数的数学工具远比离散丰富**（微分、积分、闭式解）。图像处理/分析中常把图像**当作连续函数**来推导。
- 因此必须搞清楚：**连续函数与离散函数究竟是什么关系**？采样理论正是连接两者的桥梁。
- 老师另一个动机：很多人被采样理论里"连续 impulse 的值是无穷大"吓住，这一节专门澄清。

#### 7.2 采样在数学上极其简单

```
f_d(m,n) = f_c(mΔx, nΔy) = f_c(x,y)|_{x=mΔx, y=nΔy}
```
- 就是把连续变量 x, y **替换**为 mΔx, nΔy（m, n 为整数，Δx 为采样间隔）。仅此而已。
- **难的不是采样，而是分析关系**：`f_d = f_c` 只在采样点上成立；**两个采样点之间 f_d 是 undefined（未定义）**，而 f_c 处处有值。
- 真正要回答的问题（PDF p.65）：**f_d(m,n) 是否包含与 f_c(x,y) 相同的信息？在什么条件下是？** 这才需要更抽象的数学工具。

#### 7.3 前提：Band-limited（带限）假设

```
F_c(u,v) = 0,   for |u| > U₀, |v| > V₀
```
- **bandwidth = 2U₀ 与 2V₀**（x、y 两个方向）。
- ⭐ **PDF 的思考题"Why 2U₀ and 2V₀?"**——老师给了两条理由，并**建议采用"2 倍最高频率"这个定义**：
  1. Fourier transform 有**负频率**部分，非零区间实际从 −U₀ 到 U₀，长度为 2U₀。
  2. 若对信号做 **modulation（调制）** 搬移到高频，非零频率范围确实变成 2U₀ 宽。
  - （有些教材把 bandwidth 定义为最高频率 U₀ 本身，注意区分。）
- **实际图像总能近似为 band-limited**：真实世界虽连续，但传感器（以及人眼）分辨率有限，变化过快的高频成分要么感知不到、要么信息量极小；能量主要集中在某个频带内。

#### 7.4 Sampling function（impulse train）

```
s(x,y) = Σ_{m=−∞}^{∞} Σ_{n=−∞}^{∞} δ(x − mΔx, y − nΔy)

其 Fourier transform：
S(u,v) = (1/ΔxΔy) Σ_m Σ_n δ(u − m/Δx, v − n/Δy)
```
- **impulse train 的 FT 仍是 impulse train**，间隔从 Δx, Δy 变为 **1/Δx, 1/Δy**（互为倒数）。

⭐ **老师对"impulse = ∞"的澄清（重要且常令人困惑）**：
- 连续域中，impulse 的值**必须是无穷大**（否则积分即面积为零、没有意义），积分为 1。图上用带箭头的竖线表示，箭头意即"其实是无穷"。
- **不要被这个无穷吓到**——它只是一个想象出来的数学工具。**实际中我们从不使用 impulse 本身，只使用 impulse response**（系统/滤波器对 impulse 的输出，是有限值）。impulse 只是定义 impulse response 的跳板。
- ⭐ **impulse train 的妙处**：它是一个**连续函数**（不是离散函数），却**只在离散采样点上非零**——正好是连接连续与离散的桥梁。

#### 7.5 ⭐ 核心推导：采样后频谱是原频谱的周期复制

**第一步（空间域）**：连续图像乘以 impulse train

```
f_d(x,y) = f_c(x,y)·s(x,y) = Σ_m Σ_n f_c(mΔx, nΔy)·δ(x − mΔx, y − nΔy)
```
- 依据：**函数 × impulse = 该 impulse 位置上的函数值 × impulse**（因为 impulse 在别处为 0，0 乘任何数仍为 0）。
- ⚠️ 注意：**f_d(x,y) 仍是连续函数**（x, y 连续），只是只在采样点非零。

**第二步（频域）**：相乘 ⇔ 卷积（convolution theorem）

```
F_d(u,v) = F_c(u,v) * S(u,v)
         = (1/ΔxΔy) Σ_m Σ_n F_c(u,v) * δ(u − m/Δx, v − n/Δy)
         = (1/ΔxΔy) Σ_m Σ_n F_c(u − m/Δx, v − n/Δy)
         = (1/ΔxΔy) Σ_m Σ_n F_c(u − m·f_xs, v − n·f_ys)
```
- 依据：**函数与 impulse 卷积 = 函数本身，且被搬移到该 impulse 的位置**（卷积的 shift-invariance）。
- 记号：`f_xs = 1/Δx`、`f_ys = 1/Δy` 为采样频率。

⭐ **结论**：`F_d(u,v)` 是 `F_c(u,v)` 在频率平面上、以 **(1/Δx, 1/Δy) 为间隔**、在矩形网格上的**周期复制（periodic replication）**。

#### 7.6 无混叠条件与重建

**条件（PDF p.69）**：只要各份复制品**不重叠**——

```
f_xs = 1/Δx ≥ 2U₀   且   f_ys = 1/Δy ≥ 2V₀
等价于  Δx ≤ 1/(2U₀)  且  Δy ≤ 1/(2V₀)
```

**恢复方法**：用 **low-pass filter** 只保留中心那一份、滤掉其余复制品

```
H(u,v) = { ΔxΔy,  (u,v) ∈ ℜ
         { 0,     otherwise

F_c(u,v) = F_d(u,v)·H(u,v)      （频域相乘）
f_c(x,y) = f_d(x,y) * h(x,y)    （空间域卷积）
```

**重建公式的推导（PDF p.70）**：

```
f_c(x,y) = h(x,y) * f_d(x,y)
         = h(x,y) * Σ_m Σ_n f_c(mΔx, nΔy)·δ(x − mΔx, y − nΔy)
         = Σ_m Σ_n f_c(mΔx, nΔy)·h(x − mΔx, y − nΔy)
         = Σ_m Σ_n f_d(m,n)·h(x − mΔx, y − nΔy)
```

⭐⭐ **老师的点睛之笔**：推导**从 impulse（无穷大）开始，却以 impulse response（有限、就是滤波器 mask）结束——impulse 中途消失了**。最终公式里没有任何无穷，只有：
- **离散的像素值 f_d(m,n)**（蓝色部分）；
- 一个**连续的 low-pass filter 的 impulse response h(x,y)**，且对任何图像都是同一个滤波器。

即：**用离散像素值去加权一个连续的低通滤波器并求和，就能得到连续图像**。这样一来，两个采样点之间"未定义"的值也被恢复了——**对所有 x, y 都建立起了连续与离散的关系**。

#### 7.7 Sampling Theorem（PDF p.71）

> 带宽为 (2U₀, 2V₀) 的 band-limited 图像 f_c(x,y)，若以间隔 (Δx, Δy) 在矩形网格上均匀采样，且**采样率 (f_xs, f_ys) 大于 Nyquist rates**，则可由采样值 f_d(m,n) **无误差地完全恢复** f_c(x,y)。

- **Nyquist rate（奈奎斯特率）/ Nyquist frequency**：所需采样率的下界，即带宽本身；其倒数称 **Nyquist interval**。
- **Aliasing（混叠）**：采样率低于 Nyquist rate 时，`F_c(u,v)` 的周期复制品会**重叠**，`F_d(u,v)` 被扭曲，`F_c(u,v)` **不可逆地丢失**——重建出的图像与原图不同。
- **抗混叠**：采样**之前**先做 **low-pass filtering**，把带宽压到采样频率以下。
  - ⭐ **PDF 留的思考题："at the expense of what?"**（代价是什么？）→ 代价是**主动丢弃高频细节**，图像变模糊；但这好过让混叠把整个频谱污染。

#### 7.8 ⭐ 采样理论的最终意义

只要图像是 band-limited 且满足采样定理，**连续图像与离散（数字）图像在信息上完全等价**。因此我们可以放心地把数字图像当作连续函数来做微分、积分等数学分析——**连续用 ∫、离散用 Σ，效果完全相同，没有区别**。

---

### 8. Topic 3 — Image Enhancement：Point Processing（本周进入）

> 课间休息后进入 Topic 3。Topic 3 outline（PDF p.72）：Simple Point Processing → **Histogram Equalization** → Image Smoothing → Image Sharpening → Nonlinear Image Processing。本周讲到 histogram equalization 为止。

#### 8.1 什么是 point processing

- **定义**：把输入图像灰度按 `g = T(f)` 映射为输出灰度。
- ⭐ **又称 memoryless operation（无记忆操作）**：系统不需要记忆——输出像素值**只取决于该点自身的输入灰度**，与**位置 (x,y) 无关**。
  - 因此可以把 x, y 省略，直接写 `g = T(f)`：给定同一个 f 值，无论它在图像哪个位置，输出都是同一个 g。

#### 8.2 三种简单变换（PDF p.73–76）

| 变换 | 公式 | 别名/用途 |
|---|---|---|
| **Power Transformation** | `g = c·f^γ` | 又称 **gamma correction**，Photoshop 等传统图像处理工具中的经典操作 |
| **Log Transformation** | `g = c·log(1 + f)` | 形状与 γ<1 的 power transform 相似 |
| **Piecewise Linear Transformation** | 见下 | 又称 **contrast stretching** |

**Piecewise Linear（PDF p.73/76 完整公式）**：

```
        ⎧ αf,                      0 ≤ f < a
g = T(f)⎨ β(f − a) + T(a),         a ≤ f < b
        ⎩ γ(f − b) + T(b),         b ≤ f < L
```
分段直线、各段斜率不同，整体是**非线性**函数。

#### 8.3 ⭐ Gamma correction 的效果分析（老师讲得最细的部分）

**曲线形状**：
- **γ = 1**：直线（恒等映射）。
- **γ > 1**：曲线在直线**下方**（如 γ=2 即 `g = f²` 的形状）。
- **γ < 1**：曲线在直线**上方**。

⭐ **为什么必须用非线性变换？**
- 有人想："要提高对比度，把每个像素乘 100 不就行了？原来差 1 现在差 100。"——**这不是对比度增强**。因为**人眼的敏感范围有限**，只能在某个范围内感知差异。
- 所以 power transform 里的常数 **c 就是用来把输出范围归回与输入相同的 [0, L]**——**总范围不变**。
- ⭐⭐ **核心守恒思想**：既然总范围不变，**要增强某段灰度的对比度，就必须牺牲（压缩）另一段的对比度**。所有 point processing 都遵循这个"此消彼长"的原则。

**两种情形（考点）**：

| 情形 | 曲线 | 效果 | 适用图像 |
|---|---|---|---|
| **γ > 1** | 在直线下方 | **拉伸亮部（bright range）对比度**，压缩暗部 | **过亮 / over-exposed** 的图像（大部分像素在高灰度，牺牲暗部无所谓） |
| **γ < 1**（≈ log transform） | 在直线上方 | **拉伸暗部（dark range）对比度**，压缩亮部 | **过暗** 的图像（大部分像素在低灰度） |

- **从 histogram 角度理解**（老师用暗图举例）：暗图的 histogram 密集堆在低灰度端、高灰度端稀疏。γ<1 的变换把**密集分布拉成稀疏分布**（不同像素灰度差变大 = 对比度增强），代价是把原本稀疏的亮部**压得更密集**。整体灰度范围前后不变。

**Piecewise linear 的效果**：
- **斜率 > 1 的段** → 输入的小范围映射到输出的大范围 → **对比度增强**；
- **斜率 < 1 的段** → 输入的大范围映射到输出的小范围 → **对比度压缩**。
- 适用于 **low contrast image**（不太亮也不太暗，但灰度差都很小）：中间段斜率设 > 1，两端设 < 1。
- ⭐ **极端情形**：若中间段斜率设为 **∞（竖直线）**，两端为水平线 → 变成**阶跃函数** → 输出只有 0 与最大值两种取值 → 得到 **binary image**，此时**对比度最高**（像素非最小即最大）。

#### 8.4 承上启下：自适应的需求

上述变换都需要**事先知道图像"病"在哪**（太亮？太暗？低对比度？）才能选对。**若不知道呢？** → 需要一种能**自适应于输入图像问题**的方法 → **Histogram Equalization**。

### 9. ⭐⭐ Histogram Equalization（本周最重要考点，PDF p.77–83）

#### 9.1 目标

把输入图像的灰度 f 变换为输出灰度 g，使**输出图像的 histogram 尽可能均匀（uniform）**。此时所有像素均匀分布在最小到最大灰度之间，**对比度达到最大**。

#### 9.2 算法（PDF p.77）—— ⚠️ 两个公式必须分清

```
① c(f) = Σ_{t=0}^{f} p_f(t) = Σ_{t=0}^{f} n_t / n        ← ⭐ 这才是 histogram equalization

② g = T(f) = round[ (c(f) − c_min) / (1 − c_min) · L ]   ← 只是把 [0,1] 线性归一化到 [0,L] 再取整
```
- `p_f(t)`：输入图像的 histogram（灰度 t 的像素数 n_t 除以总像素数 n）；`t` 是求和的 dummy variable；`c_min` 是所有 c(f) 中的最小值。

**做法一句话**：给定输入灰度 f，**把输入 histogram 从 0 累加到 f，这个累加和就作为输出灰度**。

#### 9.3 ⭐⭐⭐ 老师的考试警告（原话强调，务必记住）

> 教科书介绍 histogram equalization 时总是给出两个公式（上面的①和②）。但在老师看来，**公式②与 histogram equalization 毫无关系**——它只是一个**简单的归一化**（任何图像处理之后都可以做：减最小值、除以范围、乘 L、取整），可用于任何处理场合。
>
> ⚠️ **往年考试中，不止个别学生**在遇到 histogram equalization 的题目时，**只背了公式②并用它作答，完全忽略公式①** ——这种答案**判零分（zero mark）**。
>
> **真正的 histogram equalization 来自公式①（累加 histogram）**。

#### 9.4 ⭐ 连续情形的严格证明（PDF p.78–79，考点）

**前提条件**：
- 设 f 为归一化到 [0,1] 的连续灰度；
- 变换 `g = T(f)` 是 **single-valued（单值）** 且 **monotonically increasing（单调递增）**，`0 ≤ T(f) ≤ 1`；
- 其逆变换 `f = T⁻¹(g)` 也是单值、单调递增的。

**第一步：概率论关系**

```
p_g(g) = p_f(f)·|df/dg|
```
- **为什么？** 把 f、g 看作 random variable。`p_f(f)·df` 是"随机变量落在小区间 df 内"的**概率**（PDF 是概率密度，密度 × 区间 = 概率）。由于 **g 完全由 f 决定**，f 落在 df 内的概率必然等于 g 落在对应区间 dg 内的概率：
  ```
  p_f(f)·df = p_g(g)·dg   ⟹   p_g(g) = p_f(f)·df/dg
  ```
- ⭐ 老师说明：histogram 概念上虽不是 PDF（见 Week 1 的辨析），但它满足 PDF 的一切性质、是 PDF 的 estimate；连续图像情形下可直接当 PDF 用。

**第二步：取变换为 cdf**

```
g = T(f) = ∫₀^f p_f(t) dt        （f 的 cumulative distribution function，cdf）
```
- cdf 天然是**单值且单调递增**的，满足前提条件。

**第三步：代入**

```
∵ dg/df = p_f(f)                （积分的导数就是被积函数）
∴ p_g(g) = p_f(f)·(df/dg) = p_f(f)·(1/p_f(f)) = 1
```

⭐ **结论**：变换后的灰度服从 **uniform distribution**。∎

**离散版本**就是把积分换成求和，即公式①：`c(f) = Σ_{t=0}^{f} p_f(t)` 是 `∫₀^f p_f(t)dt` 的离散版。

#### 9.5 ⭐ 直观理解：为什么这么简单的式子就能均衡？

老师用**暗图**举例（histogram 密集堆在低灰度端）：

- 输出灰度 = **累计到该灰度为止的像素比例**。
- **某灰度区间像素很多** → 累加和上升很快 → 该区间被**大幅拉开（放大）**。
  - 例：若某点之前已累计 50% 的像素，则该输入灰度被映射到输出的 0.5（最大值为 1）。
- **某灰度区间几乎没有像素** → 累加和几乎不变 → 该区间被**压缩到几乎一点**。
  - 例：暗图中最亮的那一小段几乎没有像素，这一整段输入都被映射到接近最大值 1 的同一处。
- ⭐ 所以它**自适应**：像素集中在哪里，就把哪里拉开；哪里没像素，就把哪里压掉。**输入实际占据的灰度范围被拉伸到几乎整个输出范围**。

#### 9.6 ⭐ 离散情形无法严格均匀（重要洞察）

- 连续情形可严格证明得到 uniform；**但离散图像做不到严格均匀**，只能"尽量接近"。
- **为什么？** ⭐ **任何 point transform 都不能改变 histogram 中每根竖线的高度，只能改变它的位置**。
  - 因为同一灰度的像素，经过同一个变换后**必然仍是同一灰度**——不可能把它们拆散到不同灰度去。若某灰度有 50 个像素，变换后这 50 个像素仍然共享同一个新灰度值。
  - 所以竖线的**高度（像素数）永远不变**，变的只是**横轴上的位置**：某些区间被压缩、某些被拉伸（重新分布），但**纵轴上什么也不会发生**。
- ⭐ **用途**：这条可以用来判断教材插图的对错。老师指出 PDF 中"均衡化前后彩色图 + histogram"那张图里的 histogram **并非真实计算所得**，只是示意——因为真实的均衡化不可能改变每根线的高度。

#### 9.7 ⭐ 考试形式提示（老师主动透露）

- 考 histogram equalization 时，若给出完整图像的 histogram，计算量太大。因此题目通常只给**几根线**。
- **数学上会用 impulse function 来表示这几根线**（PDF p.80）：
  ```
  P_f(f) = a₁·δ(f − b₁) + a₂·δ(f − b₂) + a₃·δ(f − b₃)
  ```
  - 每个 impulse 代表一根线：**b₁, b₂, b₃ 是线的位置（灰度值）**，**a₁, a₂, a₃ 是线的高度（像素比例）**。
- ⚠️ **往年不止个别学生**看到这种写法**不认识 impulse、不明白它表示什么**，因而整道题答不出来。老师专门提醒了这一点。

#### 9.8 其他

- **Local histogram equalization**（PDF p.83）：在局部窗口内做均衡化，效果更强，老师本周只作展示。
- 相关工作：J. Ren, X. Jiang, J. Yuan, *"A Chi-Squared-Transformed Subspace of LBP Histogram for Visual Recognition," IEEE TIP*, vol. 24, no. 6, 2015。
- 老师**跳过**了 PDF 上的一小节（"不是主流内容"），并把 **low-pass / high-pass filter 设计**留到下周。

### 10. ⭐ 本周考点速查

| 考点 | 关键结论 | 节号 |
|---|---|---|
| Fourier transform 物理意义 | 信号 = sinusoid 之和；\|F\|=amplitude，∠F=initial phase | §2.2 |
| 为何用 complex exponential | 相乘 = 指数相加，远比 cos·cos 简洁 | §2.3 |
| 正变换如何提取频率 | u = u₀ 时被积函数为常数 → ∞；u ≠ u₀ 时为 sinusoid → 积分 0 | §2.4 |
| 2-D FT separable | 做两次 1-D FT；`F=F_x·F_y` 仅当 `f=f₁(x)f₂(y)` | §4.2 |
| ⭐ DFT 为何除以 m、n | 离散信号 period ≥ 1 ⇒ frequency ≤ 1；除以 m 把 [0,1) 拉成 [0,m) 使 u 可取整数 | §5.2 |
| DTFT vs DFT | DTFT 的 u,v 连续∈[0,1)；DFT 的 u,v 离散整数 | §5.2 表 |
| Periodicity 由来 | 频率超过 1 只是重复自身 | §6 |
| Conjugate symmetry 由来 | m×n 实数 → m×n 复数，信息 2 倍，必有冗余 | §6 |
| ⚠️ Convolution theorem | 离散情形对应 circular convolution，**须先 zero padding** | §6.1 |
| ⭐ Translation invariance | 平移只改 phase 不改 magnitude ⇒ \|F\| 可作识别特征 | §6.2 |
| Rotation | DFT 非旋转不变；Polar Harmonic Transform 的 magnitude 才是 | §6.3 |
| 变换对 | rectangle ⇔ 2-D sinc | §6.4 |
| Bandwidth 定义 | 取 **2U₀**（因有负频率 / 调制后范围） | §7.3 |
| 采样频域结论 | `F_d` 是 `F_c` 以 (1/Δx, 1/Δy) 为间隔的周期复制 | §7.5 |
| Sampling theorem | `1/Δx ≥ 2U₀`；低于则 aliasing 且不可逆 | §7.6–7.7 |
| 抗混叠代价 | 采样前低通滤波 → 丢失高频细节 | §7.7 |
| Point processing | memoryless，`g=T(f)` 与位置无关 | §8.1 |
| ⭐ Gamma 守恒原则 | 总范围不变 ⇒ 增强一段必压缩另一段 | §8.3 |
| γ>1 / γ<1 | γ>1 增强亮部（修过亮图）；γ<1 增强暗部（修过暗图） | §8.3 表 |
| ⭐⭐ Histogram equalization | **`c(f)=Σp_f(t)` 才是本体**；归一化式与它无关 | §9.2–9.3 |
| HE 连续证明 | 取 g=cdf ⇒ dg/df=p_f ⇒ p_g=1（uniform） | §9.4 |
| ⭐ 离散不能严格均匀 | point transform 不改变竖线**高度**，只改**位置** | §9.6 |

### 11. ⚠️ 本周易错点清单

1. **只用归一化公式②做 histogram equalization 题 → 零分**。必须先算累加 `c(f) = Σ p_f(t)`。
2. **不认识 `P_f(f)=a₁δ(f−b₁)+…` 的 impulse 表示法**（a=高度、b=位置）→ 整题失分。
3. 认为离散图像做完 HE 后 histogram **严格**均匀 → 错。只能近似；竖线高度永远不变。
4. 在数字图像上直接用"频域相乘 = 空间域卷积" → 错，那是 circular convolution，**必须 zero padding**。
5. 把 `F(u,v) = F_x(u)·F_y(v)` 当作普遍成立 → 错，只在 `f(x,y)=f₁(x)f₂(y)` 时成立。
6. 认为 DFT magnitude 也是 rotation invariant → 错，只有 translation invariant。
7. 混淆 bandwidth 是 U₀ 还是 2U₀ → 本课**采用 2U₀**。
8. 认为"每个像素乘以一个大常数"就是 contrast enhancement → 错，人眼感知范围有限，且总范围应保持。
9. 忘记连续域 impulse 的值是 **∞**（离散域才是 1）。
10. 把 DFT 定义中的常数 `1/mn` 当作必须记忆的要点 → 老师明确说它不重要、可任意放置。

### 12. 行政信息（回答"本周有无签到/考勤/quiz"）

- ⭐ **本周录播中没有任何签到、考勤或 quiz 安排的通知**。全程为知识讲授，无平台点名（无 Wooclap/NTULearn 互动环节）。
- 转写中出现的 "quiz" 全部是**出题方式的提示**，而非考试通知，共两处，均已记入上文：
  - §9.3：往年考试中只用归一化公式作答 histogram equalization 者判**零分**；
  - §9.7：quiz 中会用 **impulse 形式**给出 histogram，往年有学生不认识该写法。
- 已知考核安排仍以 Week 1 为准：**Quiz 10%（Week 7 课堂内 30 分钟）+ Assignment ×2 共 30% + Final 60%**。

---

> **下一周（Week 3）预告**：继续 Topic 3 Image Enhancement——用 LSI 系统设计 **low-pass filter 与 high-pass filter**（image smoothing 与 image sharpening），随后进入 **nonlinear image processing / rank filter**（如 **median filter**）。老师本周明确表示："这部分今晚做不完，下周讲。"

---

## Week 3 — Image Enhancement 续：Linear Filtering（smoothing/sharpening）＋ Nonlinear Filtering（median/order-statistic）＋ 进入 Machine Vision（template matching / nearest neighbor）

> **权威来源说明**：本周官方讲义为 `EE6222_lecturenote1to9.pdf` 第 83–113 页（Topic 3 "Image Enhancement" 续：image smoothing / sharpening / nonlinear processing / order-statistic filters），以及第 114 页起 Topic 4 machine vision 引言。转写 `week3.txt` 噪声较大，以 PDF 为准。本周典型转写噪声："fue/fequin/Finkst/fnqust/frequdj"→Fourier/frequency；"menial"→linear；"comvolution/conv"→convolution；"spoons/spoon"→response；"glen/gal/gaucin/gausin/Gusel"→Gaussian；"ck tank/k tangle/reck tangle"→rectangle；"no ps/no puss/no path/no pas/no paster/no pop"→low-pass；"hyposphea/high posphaa/high pasaor/high pasha"→high-pass；"meting/medium/medi"→median；"menial/men filter/minar"→mean/linear；"age"→edge；"st equation/Hc"→histogram equalization；"Zod/loot/zu"→root（root signal）；"tile/tole"→tolerance；"tuncate/trancate/tcate/trancated"→truncate；"equis/UC/uc/equity/ukV/UCD"→Euclidean；"euch"→Euclid；"merest/nes nestable/nes/first nestable"→nearest（nearest neighbor）；"classph/classfh/classer/clasp/classp"→classifier；"ation"→variation。
> 本周分两大块：**Part A** 完成 Topic 3 Image Enhancement 的线性滤波（low-pass/high-pass、image smoothing/sharpening）与非线性滤波（median filter、order-statistic filters、alpha-trimmed mean、ITM）；**Part B** 进入 Topic 4 Machine Vision——从 template matching、Euclidean distance、normalization 到 nearest neighbor classifier，为后续 classification 与机器学习铺垫。

### Part A：Image Enhancement 续 — 线性与非线性滤波

### 1. 卷积回顾与滤波本质

- 所有 linear processing 都用 **LSI 系统**描述：输出 = 输入与 impulse response 的卷积。
$$
g(x,y)=f(x,y)*h(x,y)=\sum_i\sum_j h(i,j)\,f(x-i,y-j)
$$
- 利用 Fourier transform 的 **convolution property**：spatial domain 卷积 ⇔ frequency domain 相乘 $G(u,v)=F(u,v)H(u,v)$，相乘比卷积简单，故**滤波器通常在 frequency domain 设计**，但**实现在 spatial domain**（卷积）。
- ⭐ **卷积的物理意义（老师重点）**：output pixel = filter mask 内 input pixels 的 **weighted sum（加权求和）**，权重即 filter coefficient / impulse response，输出位于 mask 中心。理解这一点极重要——CNN、neural network、transformer 本质都在做某种 weighted summation。不必逐点死算定义，抓住"加权求和"即可快速算卷积。
- 若 filter mask 为有限大小（如 $3\times3$），mask 外 $h(x,y)=0$，求和限自然收窄到 mask 覆盖范围。

### 2. Image Smoothing（低通滤波）

- **smoothing filter** 用于 blurring 与 noise reduction，又称 **averaging filter** 或 **low-pass filter**：低频通过、高频抑制。

#### 2.1 Ideal low-pass filter（ILPF）

$$
H(u,v)=\begin{cases}1,&D(u,v)\le D_0\\0,&D(u,v)>D_0\end{cases},\qquad D(u,v)=\sqrt{u^2+v^2}
$$
- 频域中一个半径 $D_0$ 的圆内为 1、圆外为 0。digital image 的频率范围归一化到 $[-0.5,0.5]$（中心为零频），故圆心是零频，离中心越远频率越高。
- ⚠️ **ideal filter 在实践有问题**：$H$ 从 1 到 0 有**突变**（sharp transition），含极高频率成分，其 inverse Fourier transform 是 **sinc function**，在 spatial domain 从 $-\infty$ 到 $+\infty$ 都非零。实际只能用有限窗口截断，导致：
  - **ringing（振铃）**：对单个 impulse 输入，ILPF 不只把它"抹开成 blur"，还产生一圈圈明暗相间的环（sinc 的负瓣所致）——这些环是**输入图像里不存在的虚假结构**（artificial structure）。
  - 真实图像经 ILPF 后会出现原图没有的条纹/结构，这是 undesirable 的。
- 结论：**实践中不要用 ideal low-pass filter**。

#### 2.2 ⭐ Gaussian low-pass filter（GLPF）

$$
H(u,v)=\frac{1}{2\pi\sigma^2}\exp\!\left(-\frac{u^2+v^2}{2D_0}\right)
$$
- 从最大值**平滑过渡**到 0（无突变），故 inverse Fourier transform 仍是 Gaussian（**Gaussian 的 FT 仍是 Gaussian**），无 sinc 负瓣、无 ringing，不产生 artificial structure。
- 对 impulse 输入，GLPF 只把它平滑成一个 Gaussian blob，无环——这是 Gaussian 在图像处理中"非常 nice"的原因。**实践总是用 Gaussian low-pass，不用 ideal low-pass**。

### 3. Image Sharpening（高通滤波）

- **high-pass filter** 抑制低频、通过高频，提取 edge/细节。由 low-pass 反推：
$$
H_{hp}(u,v)=1-H_{lp}(u,v)
$$
- **Ideal high-pass filter**：圆内（低频）= 0、圆外（高频）= 1，与 ILPF 相反，同样有 ringing 问题。
- **Gaussian high-pass filter（GHPF）**：$G(u,v)=1-\exp\!\bigl(-\frac{u^2+v^2}{2D_0}\bigr)$，无 artificial structure。
- 直觉：constant region（无论亮或暗）是零频，经 high-pass 后变 0（近黑）；只有 edge 处灰度突变（高频）输出非零 → **high-pass 提取 edge pattern**。

#### 3.1 High-boost filter（高频增强）

- 纯 high-pass 会丢掉所有低频信息，不利于人眼观察（看不出原本是亮 constant 还是暗 constant）。**high-boost filter** = 原图放大 $A$ 倍（$A\ge1$）减去 low-pass 输出：
$$
f_{hb}(x,y)=A\,f(x,y)-f_{lp}(x,y)=(A-1)f(x,y)+\underbrace{[f(x,y)-f_{lp}(x,y)]}_{f_{hp}(x,y)}
$$
- 即"原图 + edge"：edge 被增强，其余信息保留。可再配合 histogram equalization 进一步增强对比度。

### 4. 为什么需要非线性滤波（linear filter 的局限）

- **所有 linear filter 输出都是输入像素的 weighted average**（加权平均）。average 有固有缺陷：
  1. **blurs the image**（模糊图像、丢失 sharpness/细节）；
  2. **难以抑制强噪声**：若噪声值极大，average 后该强值仍残留，无法完全去除，还会把噪声**扩散**到更多像素。
- 老师举例：一幅被强噪声污染的图像——噪声**幅度极大**（能把最暗像素变最亮、反之亦然），但**空间上稀疏**（spatially sparse，多数像素未被污染）。low-pass 只能降低噪声幅度、并把它扩散开，无法彻底清除。
- 由此引出**基于 order statistic（排序统计）的非线性滤波**。

### 5. ⭐ Median Filter（中值滤波，本周核心）

#### 5.1 定义

$$
\hat f(x,y)=\operatorname*{median}_{(s,t)\in S_{xy}} f(s,t)
$$
- 把 filter window 内所有像素灰度**排序**（升/降序），取**中间位置**的值作为输出。例：$\{10,15,20,20,20,20,20,25,100\}$，median = 20（15 被替换为 20）。

#### 5.2 ⭐⭐ Mean vs Median 对比（老师详讲，重点考点）

| 情形 | Mean filter（均值/线性） | Median filter（中值/非线性） |
|---|---|---|
| **图像细节（pulse/细线）** | **blurs** detail（2 像素脉冲被抹成 4 像素、幅值减半） | **preserves** detail（window 内多数是背景时，median = 背景值，输出不变） |
| **edge（阶跃）** | **blurs** sharp step edge → ramp edge（均值拉平两侧） | **preserves** step edge（两侧 median 分别等于各自灰度） |
| **impulsive/salt-and-pepper noise（强幅度、稀疏）** | 只能**降低**幅度且**扩散**噪声，无法完全去除 | **完全去除**（只要窗口内噪声像素数 < 非噪声像素数，median 取多数值）|
| **Gaussian dense noise（小幅、密集）** | **最优**（mean 是 Gaussian noise 下最小平方估计） | 能抑制但**不如 mean filter**（dense 噪声下 median 略逊） |

- ⭐ **median 的稳健性直觉**：无论异常值多大（哪怕 1 百万），median 不受影响（一组数里加个极大值，中位数几乎不动）；mean 则被拉偏。这是 median filter 能完全去除强 impulsive noise 的根本原因。
- ⚠️ **median filter 的代价**：会**丢失小细节**（corner、细线/曲线等少数像素构成的结构），因为 corner 处窗口内多数是背景，corner 被当成噪声抹掉。这是 median 的主要缺点，引出 image detail-preserving filter 研究。

#### 5.3 Median Filter 的性质

- **root signal（根信号）**：对 median filter **不变**的信号（再施加 median filter 输出仍不变）。反复施加 median filter，信号最终收敛到某个 root signal。
  - constant（常数）信号、monotonically increasing/decreasing（单调）信号是任意窗口 median 的 root signal。
  - PDF 示例：长度 3 的 median 反复作用于 `0001212121000` → `0001121211000` → `0001112111000` → `0001111111000`（root）。
- ⚠️ median filter **是非线性**的，难以像 linear filter 那样在 frequency domain 做理论分析（没有成熟的频域理论工具），这是其理论难点。

### 6. 其他 Order-Statistic Filters

| Filter | 定义 |
|---|---|
| **Max filter** | $\hat f=\max_{(s,t)\in S_{xy}} f(s,t)$（取窗口最大值） |
| **Min filter** | $\hat f=\min_{(s,t)\in S_{xy}} f(s,t)$（取窗口最小值） |
| **Midpoint filter** | $\hat f=\tfrac12[\max f+\min f]$（最大+最小的平均） |

- Max pooling 在神经网络中类似 max filter。

### 7. ⭐ Alpha-Trimmed Mean Filter（α 修正均值滤波，教材必出现）

- **结合 mean 与 median 思想**：先排序，去掉 $d$ 个极端值（最大 $d/2$ 个、最小 $d/2$ 个），对剩下 $n-d$ 个像素求平均：
$$
\hat f=\frac{1}{n-d}\sum_{(s,t)\in S_{xy}^{\text{trimmed}}} f(s,t)
$$
- 两个极端：
  - $d=0$：不修剪，退化为 **mean filter**；
  - $d=n-1$：只留中位数，退化为 **median filter**。
- 介于二者之间即"mean 与 median 的折中"。
- ⚠️ 局限（老师指出，思考题）：
  1. **如何选 $d$**？太大趋近 median，太小趋近 mean，无定论。
  2. 实现上即便叫"mean"，仍需**排序**才能去掉极端值——排序与加减乘除是不同操作，CPU 实现麻烦，大规模/多级处理成本高。
  3. 完全"去掉"极端值可能不稳定；老师的研究改用 **truncate（截断而非删除）**——把极端值 clamp 到某个 bound，而非丢弃。

### 8. ⭐ Mean 与 Median 的数学本质（老师的研究延伸，理解性内容）

- **mean** = 最小化**平方距离**的值：$\bar x=\arg\min_c\sum_i(x_i-c)^2$，即 **L2 norm** minimization（有闭式解 $\bar x=\frac1n\sum x_i$）。
- **median** = 最小化**绝对距离**的值：$\text{med}=\arg\min_c\sum_i|x_i-c|$，即 **L1 norm** minimization（一般无闭式解，需迭代逼近）。
- 二者关系：mean 和 median 之差**有上界**，老师证明该差小于三种统计量（标准差、绝对偏差、两半均值差之半），其中"两半均值差之半"（将数据按 mean 分成大小两组各求均值，差的一半）是**最紧的上界**。

#### 8.1 Iterative Truncated Mean（ITM）算法

- 利用上述紧上界 $T$，迭代地用**算术运算逼近 median**，避免昂贵的排序：
  1. 算 mean；
  2. 以 mean ± $T$ 为界，把超出范围的值 **truncate（截断/clamp）**到边界；
  3. 对截断后的数据重新算 mean；
  4. 重复，truncated mean 会**逐步逼近 median**。
- 数学保证：对任何数据集，总有至少一个值在界外（保证每步都改变数据、bound 持续缩小），且 mean 与 median 始终在 bound 内 → truncated mean 收敛到 median。
- 实践只需 2–3 次迭代即非常接近 median；甚至不必收敛到 median，停在中间状态可能**比 mean 和 median 都好**。
- **Olympic average（奥林匹克平均）**类比：评分时去掉最高/最低再平均——介于 mean 与 median 之间，兼顾二者优点。这正是 alpha-trimmed mean 的思想。

### Part B：进入 Machine Vision — Template Matching 与 Nearest Neighbor

### 9. 从 Human Vision 到 Machine Vision

- 之前的技术（contrast enhancement、noise removal）面向**人眼**；接下来面向**机器**：让机器自动识别视觉信息。但传统方法（convolution、Fourier transform）在 machine vision 也很有用。

### 10. ⭐ Template Matching（模板匹配）

#### 10.1 机器如何识别物体

- 机器**不能"理解"输入**，只能**比较**：系统有 gallery/database $\{g_1,\dots,g_G\}$，对未知输入 $A$，逐一比较、找最接近的 gallery 样本，判定 $A$ 属于该样本代表的物体。

#### 10.2 比较的数学：difference → norm → argmin

- 两图像比较：先做 difference $A-g$，再把差异（可能上百万个像素值）压缩成**一个数**——**norm（范数）**。
- 识别 = 最小化该 norm：
$$
k^*=\arg\min_k \lVert A-g_k\rVert
$$
- 结果取 **argument（argmin，使函数取最小的自变量值 $k$）**，而非最小值本身——即"哪个 gallery 样本最像"。
- 这种"找最相似（最小差异）"的方法叫 **template matching**：$g_k$ 是物体的 template。

#### 10.3 Euclidean Distance 与向量化

- 取 **2-norm**（平方差求和）即 **Euclidean distance**：
$$
d(A,g)=\lVert A-g\rVert_2=\sqrt{\sum_x\sum_y(A(x,y)-g(x,y))^2}
$$
- 把图像（矩阵）按行展开成 **column vector**（列向量）$\mathbf{a},\mathbf{g}\in\mathbb{R}^{n}$（$n=pq$），则距离可写成向量内积：
$$
d(\mathbf{a},\mathbf{g})=\lVert\mathbf{a}-\mathbf{g}\rVert_2=\sqrt{(\mathbf{a}-\mathbf{g})^T(\mathbf{a}-\mathbf{g})}
$$
- 向量 = $n$ 维空间中一个点；Euclidean distance = 两点的几何距离，直观可视。

### 11. ⭐ Normalization（归一化，核心概念）

#### 11.1 为什么 Euclidean distance 不够

- 老师反例：两幅内容**完全相同**的 triangle pattern 图，仅 brightness/contrast 不同 → Euclidean distance 巨大，但实为同一物体。直接用 Euclidean distance 会误判。
- 解决：先对每幅图像做 **normalization**，再做 template matching。

#### 11.2 零均值单位方差归一化

- 把图像每个像素减去其 mean、再除以 standard deviation（或向量长度）：
$$
\tilde f=\frac{f-\mu_f}{\sigma_f}\quad(\text{zero mean, unit variance})\qquad\text{或}\qquad \tilde f=\frac{f-\mu_f}{\lVert f-\mu_f\rVert}\quad(\text{unit length})
$$
- 归一化后，仅 brightness/contrast 不同的同一内容图像 → Euclidean distance = 0，正确判为相同物体。
- ⭐ **normalization 是 recognition/machine learning 的核心概念**：识别之所以难，是因为同一物体有巨大 **variation**（brightness、scale、position、rotation 等）；recognition 的本质就是**消除这些 variation**，把不同表现的同一物体映射到同一表示。AI/deep learning 中大量 normalization 都为此。

#### 11.3 Correlation Coefficient（相关系数）

- 不必显式归一化，直接用 **correlation coefficient**：
$$
\rho=\frac{(f-\mu_f)^T(g-\mu_g)}{\lVert f-\mu_f\rVert\,\lVert g-\mu_g\rVert}
$$
- 其定义**已内含归一化**（减均值、除长度）。相似 → $|\rho|\to1$；不相似 → $|\rho|$ 小。
- 用 correlation 取**最大**，等价于用归一化后 Euclidean distance 取**最小**（二者互为反面：distance 最小 = similarity 最大）。

### 12. ⭐ 从 Matching 到 Classification（Nearest Neighbor Classifier）

#### 12.1 一物多模板 → class

- 一个物体（如 car）在 gallery 中应有**多个 template**（正面/侧面、不同 size/contrast…），单个 template 无法代表。于是**一个 object 对应一组 samples = 一个 class**。
- 识别"未知输入是 car 还是 bicycle"变成：把它**分类**到某个 class——从 matching 升级为 **classification**。

#### 12.2 Nearest Neighbor Classifier（1-NN）

$$
k^*=\arg\min_i\Bigl(\min_{g\in\text{class}\,\omega_i}\lVert A-g\rVert\Bigr)
$$
- 对所有 class 的所有 sample 算距离，取最小者所属 class 为结果（外层 argmin 取 class 索引 $i$，内层 min 找该 class 中最近 sample）。
- 这是最经典的 classifier 之一，deep learning 前广泛使用。

#### 12.3 K-Nearest Neighbor（K-NN）

- 取 $K$ 个最近训练样本，在这 $K$ 个里**多数投票**（majority vote）决定 class。如 5-NN：取最近 5 个，看哪 class 占多数。
- 1-NN 的自然推广。

#### 12.4 Nearest Neighbor 的问题（引向后续）

1. **计算量大**：每个未知输入都要与全部训练样本算距离（detection 问题中尤其严重）。
2. **overfit / 性能受限**：决策只依赖离未知最近的少数几个训练样本，其余大量训练数据未被利用 → 易 overfit。
- → 下周将从 probability theory 出发，**理论推导**出最优 classifier（揭示 nearest neighbor 的理论根源）。

### 13. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| 卷积本质 | weighted sum，输出在 mask 中心；频率域设计、空间域实现 |
| Ideal vs Gaussian low-pass | ideal 有 ringing（sinc 负瓣）→ 实践用 Gaussian，无 ringing |
| High-pass = 1 − low-pass | 提取 edge；high-boost = (A−1)f + high-pass，保留低频 |
| Linear filter 局限 | average 必模糊、强噪声无法彻底去除且会扩散 |
| ⭐⭐ Mean vs Median | median 保 edge/细节、完全去除 impulsive noise；mean 适合 Gaussian dense noise 但模糊 edge |
| median 完全去噪条件 | 窗口内噪声像素数 < 非噪声像素数 |
| median 缺点 | 丢失 corner/细线等小细节 |
| Alpha-trimmed mean | 去极端值再求平均；$d=0$→mean，$d=n-1$→median；需排序、$d$ 难选 |
| mean = L2 min，median = L1 min | mean 闭式解、median 需迭代 |
| template matching | argmin‖A−g‖，取 argument（类索引）非最小值 |
| normalization 核心 | 消除 brightness/contrast 等 variation；同一物体不同表现归一后距离=0 |
| correlation coefficient | 内含归一化，取最大；等价归一化 Euclidean distance 取最小 |
| Nearest Neighbor | 1-NN 取最近样本所属 class；K-NN 多数投票；问题：计算量大、overfit |

### 14. 本周要点小结

- **线性滤波**：low-pass（smoothing/blurring）与 high-pass（sharpening/edge）互为 1−H；ideal filter 有 ringing，实践用 Gaussian（FT 仍 Gaussian，无 ringing）；high-boost 保留低频同时增强 edge。
- **非线性滤波**：linear = average，必然模糊且难去强噪声。median filter 基于 order statistic，**保 edge、完全去除稀疏强 impulsive noise**，但难做频域理论分析、会丢小细节。Gaussian dense noise 下 mean filter 最优。
- **alpha-trimmed mean** 介于 mean 与 median 之间（$d=0$→mean，$d=n-1$→median），需排序、$d$ 难定；ITM 用算术迭代逼近 median，Olympic average 同理。
- **machine vision 入口**：机器只能比较 → template matching = argmin‖A−g‖；Euclidean distance（向量化、内积）直观但受 brightness/contrast 干扰 → **normalization 消除 variation**（recognition 的本质）；可用归一化 Euclidean distance 或 correlation coefficient。
- **classification**：一物多模板 → class；1-NN 取最近样本所属 class，K-NN 多数投票；问题：计算量大、overfit → 下周理论推导最优 classifier。

---

> **下一周（Week 4）预告**：老师明确预告将从 **probability theory 出发理论推导 optimal classifier**，揭示 nearest neighbor classifier 的理论根源（"how this nearest neighbor classifier comes from the theoretic study, from the probability theory to get the optimal classifier"）。预计涉及 Bayes decision rule / MAP decision / classification 的概率论推导。本周已引出 nearest neighbor 的两大问题（计算量大、overfit），下周给出最优解法。

---

## Week 4 — Topic 5：MAP Decision and Classifiers（从概率论推导最优分类器）

> **权威来源说明**：本周官方讲义为 `EE6222_lecturenote1to9.pdf` 第 152–170 页（Topic 5 "MAP Decision and Classifiers"），转写 `week4.txt` 噪声极大，以 PDF 为准。本周典型 ASR 错拼修正：
> - "a postal / apo / apostrop / post probability" → **a posteriori probability / posterior probability**
> - "prior / pyro / P or mega / P omega" → **prior probability** $p(\omega_i)$
> - "cha / chain / chain rule" → **chain rule**（联合概率分解 $p(A,B)=p(A)p(B|A)=p(B)p(A|B)$）
> - "null of the total probability" → **law of total probability**
> - "equity / equiv / QD / euclid distance" → **Euclidean distance**
> - "Mov / Mab / homo base / man distance" → **Mahalanobis distance**
> - "cons / conse / co metric / cosmetics / nsmetri" → **covariance matrix**
> - "g / gal / galcan / gusin / gaucin / guan / sulfin" → **Gaussian**
> - "dit / discreminant / disc / decriminal / decree man" → **discriminant function**
> - "atic / aquatic / crotic / roogic" → **quadratic**
> - "mimiar / meniar / aia" → **linear**
> - "tris / choice / trigo / twice" → **threshold**（决策阈值/边界点）
> - "Chinese sample" → **training sample**（训练样本）
> - "school of the trouble E / trouble E" → **school of EEE**
> - "higher / nuns of the higher" → **hair**（头发长度，第二特征示例）

### 1. 本周主线

上周结束于 nearest neighbor classifier 的两大问题（计算量大、overfit）。本周回答一个更根本的问题：**在不确定下如何做最优决策？** 老师从一个直观例子（在 EEE 学院猜学生性别）出发，从 common sense 一步步抽象出 **MAP decision rule**，再用 chain rule 与 law of total probability 把 posterior 拆成 prior × likelihood，最终在 Gaussian 假设下推出 **discriminant function = quadratic function of x**，其核心项正是 **Mahalanobis distance**。这就从概率论给出了 optimal classifier 的理论根源，并解释了上周 Mahalanobis distance 为何出现。

### 2. 从 common sense 到 MAP decision rule

#### 2.1 直觉例子：在 EEE 学院看一个学生

- 在 EEE 学院，男生 70%、女生 30% → 看到一个模糊身影，**最佳决策是判 male**，因为 $p(\omega_1)=0.7>p(\omega_2)=0.3$。
- 换到会计学院（male 30% / female 70%）→ 决策反过来。
- 这就是 **maximum probability decision**：选 $p(\omega_i)$ 最大的类。
- 决策不一定对，但**没有更好的决策**：error rate = 0.3 是最小的。

#### 2.2 引入观测值：posterior probability

- 若已知身高 $x=1.75$ m，最佳决策**仍是比较两类概率**，只是现在概率变成 **posterior probability** $p(\omega_i|x)$。
- **prior probability** $p(\omega_i)$：未观测 $x$ 前的概率；**posterior probability** $p(\omega_i|x)$：观测到 $x$ 后的概率。
- 老师强调：posterior 本质就是 **conditional probability**，所有概率本质上都是 conditional，只是研究 scope 不同。不必被术语吓到。

#### 2.3 ⭐ MAP decision rule

$$
\text{Decide } \omega_k = \arg\max_{\omega_i} p(\omega_i|x)
$$

- 选 posterior 最大的类。
- 由于选了最大的 $p(\omega_k|x)$，错误概率 $p(e_k|x)=1-p(\omega_k|x)$ 同时被**最小化**。

$$
\text{Decide } \omega_k = \arg\max_{\omega_i} p(\omega_i|x) = \arg\min_{\omega_i} p(e_i|x)
$$

> ⭐ **MAP decision rule 最小化 decision error probability**——这是其"最优"的含义。

### 3. 从 posterior 到 prior × likelihood：Bayes 公式

#### 3.1 chain rule

$$
p(x,\omega_i)=p(x)\,p(\omega_i|x)=p(\omega_i)\,p(x|\omega_i)
$$

由此得 Bayes 公式：

$$
p(\omega_i|x)=\frac{p(\omega_i)\,p(x|\omega_i)}{p(x)}
$$

- $p(\omega_i)$：**prior probability**（先验）。
- $p(x|\omega_i)$：**class-conditional probability / likelihood**（类条件概率）。
- $p(x)$：**mixture PDF/PMF**，由 **law of total probability** 给出：

$$
p(x)=\sum_{i=1}^{c} p(x|\omega_i)\,p(\omega_i)
$$

#### 3.2 ⭐ 去掉 $p(x)$：决策只需比较

- $p(x)$ 对所有类**相同**，在 argmax 中可**移除**。决策实际只用：

$$
\omega_k = \arg\max_{\omega_i} p(\omega_i)\,p(x|\omega_i)
$$

> 这是本周关键简化之一：**不必精确算出 posterior 的值，只需比较哪个类最大**。

#### 3.3 自动化系统需要整条 PDF

- 手动判断一个 $x=1.75$ 只需该点的概率；但**自动系统要对所有 $x$ 都能判**，故需整条 class-conditional PDF $p(x|\omega_i)$。
- PDF/PMF 须归一化：$\int p(x|\omega_i)\,dx=1$（continuous）或 $\sum p(x|\omega_i)=1$（discrete）。
- 离线用训练数据估计这两条曲线 → 预先算出 **class boundary（决策阈值）** → 在线只需比较 $x$ 与阈值，极快。

### 4. 系统性能：error rate 的计算与可视化

#### 4.1 特定 $x$ 的 error rate

$$
p(e_k|x)=1-p(\omega_k|x)=\sum_{i\neq k} p(\omega_i|x)
$$

#### 4.2 ⭐ 全系统 error rate：概率加权平均

- $x$ 是 random variable，不同 $x$ 出现概率不同 → 不能简单求和除以个数，要按 $p(x)$ **加权**：

$$
p(e)=\int_{-\infty}^{\infty} p(e_k|x)\,p(x)\,dx \quad (\text{continuous}),\qquad p(e)=\sum_x p(e_k|x)\,p(x)\ (\text{discrete})
$$

> 老师强调：common sense 的"平均"只是 uniform 分布下 probability-weighted average 的特例。

#### 4.3 推导到 decision region

- 不同 $x$ 区域决策的 $\omega_k$ 不同 → 把整个空间划分为 $c$ 个 **decision region** $\Re_i$：

$$
p(e)=1-\sum_{i=1}^{c} p(\omega_i)\int_{\Re_i} p(x|\omega_i)\,dx,\qquad p(\text{correct})=\sum_{i=1}^{c} p(\omega_i)\int_{\Re_i} p(x|\omega_i)\,dx
$$

#### 4.4 ⭐ 两类问题的 error rate 可视化（PDF p.161–162）

两类的 $p(\omega_i)p(x|\omega_i)$ 曲线画在一起，total error rate 是两块**阴影面积**之和：
- 类1的 PDF 在 $\Re_2$ 区域的积分（被错分到类2的类1样本）
- 类2的 PDF 在 $\Re_1$ 区域的积分（被错分到类1的类2样本）

**决策边界放在两条曲线的交点处时，阴影面积最小** → 这正是 MAP 决策（选 posterior 大者）的几何含义。

#### 4.5 ⭐ 增加特征维度降低 error rate

- 1D 用身高 $x_1$ → 2D 加头发长度 $x_2$，向量 $\mathbf{x}=[x_1,x_2]^T$。
- 原则上**无区别**，只是 scalar $x$ → vector $\mathbf{x}$，PDF 从曲线 → surface，阈值从点 → 曲线/直线。
- 老师给示例：两类在单一维度上严重重叠（error rate 大），但联合两维用一条斜线可几乎完美分开（error rate ≈ 0）。
- **增加信息/维度一般降低 error rate**——这是引入更多特征的动机。

### 5. ⭐ Discriminant Function（判别函数）

#### 5.1 定义

- 不必精确算 posterior，只要一个与 posterior **成比例**（monotonic）的函数即可比较：

$$
g_i(\mathbf{x}) = \ln p(\mathbf{x}|\omega_i) + \ln p(\omega_i)
$$

- 取 **natural logarithm ln**：单调递增不影响比较，且把乘法变加法、把指数变线性，简化计算。
- 决策：选 $g_i(\mathbf{x})$ 最大的类。

#### 5.2 Gaussian 假设下的 discriminant function（PDF p.165–166）

设 $p(\mathbf{x}|\omega_i)=\mathcal{N}(\boldsymbol{\mu}_i,\boldsymbol{\Sigma}_i)$：

$$
p(\mathbf{x}|\omega_i)=\frac{1}{(2\pi)^{d/2}|\boldsymbol{\Sigma}_i|^{1/2}}\exp\!\left[-\tfrac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_i)^T\boldsymbol{\Sigma}_i^{-1}(\mathbf{x}-\boldsymbol{\mu}_i)\right]
$$

代入取 ln：

$$
g_i(\mathbf{x}) = -\tfrac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_i)^T\boldsymbol{\Sigma}_i^{-1}(\mathbf{x}-\boldsymbol{\mu}_i) + \ln p(\omega_i) - \tfrac{1}{2}\ln|\boldsymbol{\Sigma}_i| - \tfrac{d}{2}\ln 2\pi
$$

- 末项 $-\tfrac{d}{2}\ln 2\pi$ 对所有类相同 → **移除**。
- 记 $b_i = \ln p(\omega_i) - \tfrac{1}{2}\ln|\boldsymbol{\Sigma}_i|$，则：

$$
g_i(\mathbf{x}) = -\tfrac{1}{2}d_{\Sigma_i}(\mathbf{x},\boldsymbol{\mu}_i) + b_i
$$

其中

$$
d_{\Sigma_i}(\mathbf{x},\boldsymbol{\mu}_i) = (\mathbf{x}-\boldsymbol{\mu}_i)^T\boldsymbol{\Sigma}_i^{-1}(\mathbf{x}-\boldsymbol{\mu}_i)
$$

就是 **(squared) Mahalanobis distance**。

### 6. ⭐ Mahalanobis distance vs Euclidean distance

| | Mahalanobis | Euclidean |
|---|---|---|
| 公式 | $d_{\Sigma}=(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})$ | $d_{Eu}=(\mathbf{x}-\boldsymbol{\mu})^T(\mathbf{x}-\boldsymbol{\mu})$ |
| 1D | $(x-\mu)^2/\sigma^2$ | $(x-\mu)^2$ |
| 几何 | 椭圆等距线（contour of Gaussian PDF） | 圆等距线 |
| 含义 | Euclidean distance 被 covariance **归一化** | 无归一化 |

- ⭐ **Minimum Mahalanobis distance classifier 在各类服从 Gaussian PDF 时即为 optimal classifier**（与上周 §11 的伏笔呼应）。
- Gaussian 的 **mean 决定位置**，**covariance matrix 决定形状（contour/ellipse）**。
- 椭圆上所有点到中心 Mahalanobis distance 相同但 Euclidean distance 不同。

### 7. ⭐ Quadratic Classifier（一般情形）

- Gaussian 假设下 $g_i(\mathbf{x})$ 是 $\mathbf{x}$ 的 **quadratic function（二次函数）**。
- decision boundary $g_i(\mathbf{x})=g_j(\mathbf{x})$ 是 **quadratic curve/surface**（二次曲线/曲面）。
- 2D 两类、不同 $\boldsymbol{\Sigma}$ → 边界可为 ellipse / hyperbola / 抛物线，**即使两类的 mean 相同**也可形成圆/椭圆。
- 高维或多类时 quadratic boundary 可很复杂。

### 8. ⭐ 特例：共享 covariance matrix → Linear Classifier

#### 8.1 推导

若所有类 $\boldsymbol{\Sigma}_i = \boldsymbol{\Sigma}$（相同 covariance，不同 mean）：

$$
g_i(\mathbf{x}) = -\tfrac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_i)^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_i) + \ln p(\omega_i) - \tfrac{1}{2}\ln|\boldsymbol{\Sigma}|
$$

展开后，**二次项 $\mathbf{x}^T\boldsymbol{\Sigma}^{-1}\mathbf{x}$ 对所有类相同 → 移除**，只剩 $\mathbf{x}$ 的一次项 → **linear function of $\mathbf{x}$**：

$$
g_i(\mathbf{x}) = \mathbf{w}_i^T \mathbf{x} + w_{i0},\qquad \mathbf{w}_i = \boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_i
$$

- decision boundary 为 **hyperplane**（高维）/ **straight line**（2D）/ **plane**（3D）。

#### 8.2 ⭐⚠️ 关键易错点（老师重点强调）

- **共享 $\boldsymbol{\Sigma}$ ≠ covariance matrix 无用！** common $\boldsymbol{\Sigma}$ 仍**参与决定**最优边界方向与位置。
- **decision boundary 不一定经过两 class mean 的连线**——边界方向由 $\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_i-\boldsymbol{\mu}_j)$ 决定，而非单纯由 mean 差决定。
- 老师点名批评 **Direct LDA** 方法：它把数据投影到"类中心差所张成的子空间"并声称其余维度无用——这与上述理论**矛盾**，因为 class-conditional covariance（within-class variation）仍影响最优分类。
- 记忆：**分类不只取决于 class mean 的差异，within-class covariance 同样关键**。

### 9. 老师的考试哲学（重要提示）

- 转写明确："I never require you to memorize any formula. Any formula without clear physical meaning, you don't need to memorize it."
- 应记的是**有物理意义的公式**：Mahalanobis distance $d_\Sigma=(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})$（= Euclidean distance 被 covariance 归一化）、MAP rule、discriminant function 与 posterior 的比例关系。
- 不必死记 discriminant function 的展开常数项——要知道它是 **Mahalanobis distance 的函数**，由 Gaussian PDF 的 shape 决定。

### 10. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| **MAP decision rule** | $\omega_k=\arg\max_i p(\omega_i\|x)$，最小化 error probability |
| **prior / posterior / likelihood** | posterior = prior × likelihood / $p(x)$；$p(x)$ 可移除 |
| **error rate** | $p(e)=\int p(e_k\|x)p(x)dx$；两类 = 两块阴影面积之和；边界在曲线交点处最小 |
| **discriminant function** | $g_i(\mathbf{x})=\ln p(\mathbf{x}\|\omega_i)+\ln p(\omega_i)$，与 posterior 单调成比例 |
| **Gaussian → quadratic** | $g_i=-\tfrac{1}{2}d_{\Sigma_i}+b_i$，二次函数，边界为二次曲线 |
| **Mahalanobis distance** | $d_\Sigma=(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})$，Gaussian 下 optimal |
| **共享 $\Sigma$ → linear** | 二次项抵消，边界为 hyperplane，**但不一定过两 mean 连线** |
| **维度↑ → error↓** | 更多特征一般降低 error rate |
| **共享 $\Sigma$ ≠ covariance 无用** | within-class covariance 仍决定边界（反 Direct LDA） |

### 11. 本周要点小结

- **最优决策的直觉**：在不确定下，选当前信息下概率最大的类——这就是 common sense，数学化即 MAP。
- **posterior 难算** → Bayes 公式拆成 prior × likelihood，再移除对所有类相同的 $p(x)$。
- **判别函数**：取 ln、移除公共项，得到与 posterior 成比例的函数；Gaussian 下核心项是 **Mahalanobis distance**。
- **Mahalanobis distance = 归一化的 Euclidean distance**，Gaussian 假设下 minimum Mahalanobis classifier 即 optimal。
- **一般 Gaussian**：quadratic classifier；**共享 $\Sigma$**：linear classifier，但 covariance 仍关键、边界不一定过 mean 连线。
- **性能评估**：error rate = probability-weighted average，两类可视化为两曲线交点处的阴影面积。
- **考试**：不死记无物理意义的公式，重点理解 Mahalanobis distance 的含义与 MAP 的最优性。

---

> **下一周（Week 5）预告**：老师末尾说 "we haven't completed all content… next week we study further special cases"。预计继续 Topic 5 的 special case（如 $\boldsymbol{\Sigma}_i=\sigma^2\mathbf{I}$ 的 nearest mean / Euclidean classifier、Naive Bayes 独立假设等），并可能进入 Topic 6（Statistical Estimation and Machine Learning）——如何从 training data 估计 prior 与 class-conditional PDF 的参数。具体以课件为准。

---

> **笔记约定**：本课英文授课、英文考试，核心术语保留英文（machine vision, image, pixel, convolution, impulse response, LSI/LTI, filter, filter mask, histogram, gray level, color space, RGB, HSI, LBP, HOG, Fourier transform, DFT, DTFT, sinusoid, sinc function, impulse train, magnitude/phase, conjugate symmetry, convolution theorem, zero padding, translation/rotation invariant, sampling, Nyquist, aliasing, band-limited, low-pass/high-pass filter, point processing, gamma correction, log transform, piecewise linear, histogram equalization, cdf, feature extraction, template matching, Euclidean distance, norm, normalization, correlation coefficient, nearest neighbor classifier, K-NN, order-statistic filter, median filter, alpha-trimmed mean, root signal, prior probability, posterior probability, class-conditional probability, likelihood, chain rule, law of total probability, mixture PDF/PMF, MAP decision rule, Bayes rule, decision region, decision boundary/threshold, error rate, discriminant function, Mahalanobis distance, covariance matrix, Gaussian/multivariate Gaussian, quadratic classifier, linear classifier, hyperplane, within-class scatter, Direct LDA 等）。中文用于组织句意与补充释义。
