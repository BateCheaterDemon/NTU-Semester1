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

## Week 5 — Topic 5 续：Scalar Covariance 特例 + Topic 6 起：Statistical Estimation / Machine Learning

> 本周两堂课：上半场收尾 Topic 5（特殊情况最优分类器），下半场进入 Topic 6（Statistical Estimation and Machine Learning），从"已知 PDF 如何做最优分类"转向"未知 PDF 如何从 training data 估计 PDF/参数"。

### 1. 回顾：上一周的 linear classifier

上周在 shared covariance $\boldsymbol{\Sigma}_i=\boldsymbol{\Sigma}$（所有类同一 covariance，不同 mean）假设下，最优 discriminant function 化简为 $\mathbf{x}$ 的**一次函数**：

$$
g_i(\mathbf{x})=\mathbf{w}_i^T\mathbf{x}+w_{i0},\qquad \mathbf{w}_i=\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_i
$$

- 二次项 $\mathbf{x}^T\boldsymbol{\Sigma}^{-1}\mathbf{x}$ 对所有类相同 → 移除 → linear classifier。
- ⚠️ 关键（上周已强调）：**共享 $\boldsymbol{\Sigma}$ ≠ covariance 无用**，common $\boldsymbol{\Sigma}$ 仍决定最优边界方向与位置。

### 2. ⭐ Special Case 2：Scalar covariance $\boldsymbol{\Sigma}=\sigma^2\mathbf{I}$

本周进一步**收紧假设**——不止所有类共享同一 covariance，而且该 covariance 是 **scalar matrix**（对角且对角元相同）：

$$
\boldsymbol{\Sigma}_i=\boldsymbol{\Sigma}=\sigma^2\mathbf{I}\qquad\text{（all classes）}
$$

- 即一个标量 variance $\sigma^2$ 乘 identity matrix。
- 此时 $\boldsymbol{\Sigma}^{-1}=\tfrac{1}{\sigma^2}\mathbf{I}$，$|\boldsymbol{\Sigma}|=\sigma^{2D}$（$D$ 为数据维数），计算极大简化。

代入 shared-covariance 的 discriminant function：

$$
g_i(\mathbf{x})=\tfrac{1}{\sigma^2}\boldsymbol{\mu}_i^T\mathbf{x}-\tfrac{1}{2\sigma^2}\boldsymbol{\mu}_i^T\boldsymbol{\mu}_i+\ln p(\omega_i)
$$

- 二次项 $\tfrac{1}{2\sigma^2}\mathbf{x}^T\mathbf{x}$ 对所有类相同 → 仍可移除 → 仍是 linear classifier。

### 3. ⭐ Decision boundary：过两 class mean 连线（与上周的区别）

两类 $i,k$ 的 decision boundary 由 $g_i(\mathbf{x})=g_k(\mathbf{x})$ 给出：

$$
\mathbf{w}^T\mathbf{x}+w_0=0,\qquad \mathbf{w}=\tfrac{1}{\sigma^2}(\boldsymbol{\mu}_i-\boldsymbol{\mu}_k)
$$

**关键观察**：边界 hyperplane 的法向量 $\mathbf{w}\propto(\boldsymbol{\mu}_i-\boldsymbol{\mu}_k)$，即**类均值差向量方向**。因此：

- 2D：边界是一条**过两 class mean $\boldsymbol{\mu}_i,\boldsymbol{\mu}_k$ 连线**的直线。
- 3D：边界是一个过两 mean 连线的 plane。
- 高维：hyperplane 过两 mean 连线。

> ⭐⚠️ **与上周对比**：上周仅 shared $\boldsymbol{\Sigma}$ 时，边界方向由 $\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_i-\boldsymbol{\mu}_k)$ 决定，**不一定过两 mean 连线**。只有当 $\boldsymbol{\Sigma}=\sigma^2\mathbf{I}$（scalar matrix）时，$\boldsymbol{\Sigma}^{-1}$ 是标量乘 $\mathbf{I}$，不改变方向，边界才**必然过两 mean 连线**。这是比上周更严格的条件带来的额外简化。

### 4. 降维到 1D：投影到类均值差向量

由于边界法向量就是 $\boldsymbol{\mu}_i-\boldsymbol{\mu}_k$（单一方向），整个最优分类**只依赖数据在此方向上的投影**：

$$
\text{scalar projection}=\frac{(\boldsymbol{\mu}_i-\boldsymbol{\mu}_k)^T\mathbf{x}}{\|\boldsymbol{\mu}_i-\boldsymbol{\mu}_k\|}
$$

- 无论原始数据多少维，在此特例下**最优分类只需一维信息**——沿类均值差向量方向的投影。
- 这一点与 between-class scatter / Fisher LDA 的思想一致：分类信息集中在 class mean 差所张成的方向。老师提到有研究据此认为"classification 可只在 cluster centers 张成的子空间进行"——但**这只在 scalar covariance 成立**，一般 shared $\boldsymbol{\Sigma}$ 下不成立（回应上周对 Direct LDA 的批评）。
- $\sigma^2$ 在此特例中只决定 **threshold 的位置（平移）**，不改变边界方向；方向完全由 class mean 差决定。

### 5. Prior 的影响：移动 threshold

- 若两类 prior 相同 $p(\omega_i)=p(\omega_k)$，threshold 位于两 mean 中点附近（对称情形）。
- 若 prior 不等（如 $p(\omega_i)>p(\omega_k)$），边界向 prior 较小的类一侧**平移**——prior 大的类"地盘"扩大。
- 若 prior 悬殊，threshold 可**移出两 mean 连线区间**，落在某一侧之外。

### 6. ⭐⭐ Minimum Distance Classifier（Template Matching）

当**进一步假设所有类 prior 相同** $p(\omega_i)=$ const，则 $\ln p(\omega_i)$ 项可移除，discriminant 简化为：

$$
g_i(\mathbf{x})=-\frac{1}{2\sigma^2}\|\mathbf{x}-\boldsymbol{\mu}_i\|^2\;\propto\;-\|\mathbf{x}-\boldsymbol{\mu}_i\|^2
$$

即最优分类 = **minimum Euclidean distance classifier**：把 $\mathbf{x}$ 分到**欧氏距离最小的 class mean（cluster center）所在的类**。

$$
\omega^*=\arg\min_i\|\mathbf{x}-\boldsymbol{\mu}_i\|^2
$$

- 这就是 **template matching**：每类用一个 class mean（template / 原型点）代表，分类即比较输入到各 template 的距离。
- ⚠️ **极重要**：minimum distance classifier 虽直观易懂，但**只在极严格条件下才 optimal**：
  1. 各类 class-conditional PDF 为 Gaussian；
  2. 所有类共享同一 covariance；
  3. 该 covariance 还是 scalar matrix $\sigma^2\mathbf{I}$；
  4. 所有类 prior 相同。
  - **任一条件不满足，minimum distance classifier 不再是最优分类器**。这正是上周提到的"直观方法需数学条件背书"的体现。

### 7. 能否把任意分布变换成 Gaussian？（一个延伸讨论）

- 理论上，若能把任意分布的数据变换到 Gaussian，就可在新空间解析地设计最优分类器。
- 类比 histogram equalization（把任意灰度分布变换成 uniform 分布），能否类似地变换成 Gaussian？
- 结论：**仅对一维数据可行**；高维数据一般找不到这样的变换。但对某些特定分布（如 chi-square 类，常见于 LBP histogram 这类特征）可找到高维变换并发表在 IEEE Trans. on Image Processing。
- 实践意义有限——大多数高维真实数据无法简单 Gaussian 化，因此需要 Topic 6 的 estimation 方法。

### 8. Topic 6 开场：Statistical Estimation = Machine Learning

至此 Topic 5（分类/预测的最终决策）结束。接下来转入 **Topic 6: Statistical Estimation and Machine Learning**——回答"若不知道 PDF，只有 training data，如何估计 PDF / 参数"。

**核心论点：statistical estimation 就是 machine learning。**

- 最优预测（minimum error rate）需要 posterior $p(\omega_i|\mathbf{x})$，而 posterior = prior × class-conditional PDF / $p(\mathbf{x})$。
- 实践中**不知道 PDF**，只有一组 training data → 必须从数据**估计** prior、class-conditional PDF。
- "用 training data 估计随机变量的某些固定量" = statistical estimation；"用 training data 学一个 model 代表输入特性" = machine learning —— **两者本质相同**。
- PDF 是随机变量的**完备信息**（no more information beyond PDF），所以"学 PDF"= 学到关于输入的一切；理论上学全 PDF 即得最优分类。但实践中样本有限、需选参数，常退而直接优化预测输出（如 cost function），不精确估计 PDF。

### 9. 估计 prior：最简单情形

若只有 training data（已知每个样本的类标签）：

$$
\hat p(\omega_k)=\frac{N_k}{N}
$$

- $N_k$：类 $\omega_k$ 的训练样本数；$N$：总训练样本数。
- 不同类 $N_k$ 不同 → prior 估计不同。
- 老师认为：若仅有 training data、无其他信息，这是**最好也是最自然**的 prior 估计。

### 10. Topic 6 两大方法路线

| 路线 | 假设 | 本课覆盖 |
|---|---|---|
| **Non-parametric approach** | 不假设 PDF 形式，直接从数据估计 PDF 数值 | Parzen window、k-nearest neighbor |
| **Parametric approach** | 假设 PDF 形式（如 Gaussian），估计其参数 | Maximum Likelihood Estimation (MLE)；Gaussian mixture（本课 skip） |

### 11. Non-parametric：Parzen window 方法（本周已开始）

**核心直觉**：概率密度 × 体积 ≈ 概率（density × volume ≈ mass，类比物理）。

$$
p(\mathbf{x})\approx\frac{k/N}{V}
$$

- 以 $\mathbf{x}$ 为中心取一个区域 $R$，体积 $V$；
- 数落入 $R$ 内的训练样本数 $k$；
- 概率 $\approx k/N$，密度 $\approx (k/N)/V$。

**实现**：用 kernel function（窗口函数）把"计数"写成可计算求和：

$$
p(\mathbf{x})=\frac{1}{N}\sum_{i=1}^{N}\frac{1}{h^D}\,K\!\left(\frac{\mathbf{x}-\mathbf{x}_i}{h}\right)
$$

- $h$：窗口宽度（kernel bandwidth），$D$：维数，$h^D$：归一化体积。
- 矩形窗（hypercube）→ $K(u)=1$ 当 $|u|<\tfrac12$，否则 $0$。

**问题与改进**：
- 矩形窗 → 估计 PDF 为**阶梯函数**，不光滑、不平滑（训练样本处突变跳变）。
- 改用 **Gaussian kernel**：光滑、物理意义合理（样本处贡献最大，远处平滑衰减）。
- **核函数条件**：$K(u)\ge0$，$\int K(u)\,du=1$（任何 PDF 函数都满足）。
- ⚠️ **带宽 $h$ 是关键超参数**：$h$ 大 → 过度平滑（极端：含全部样本 → uniform）；$h$ 小 → 过度尖锐（极端：仅在训练点处冲激、其余为零）。不同 $h$ 结果天差地别——机器学习的不确定性来源之一。

**IID 假设**：训练样本须 **independent and identically distributed (IID)** ——独立抽取、同分布。若按"先采男性、再采女性"有目的性地采，则不独立，估计失效。

**与信号处理的类比**：Parzen window 是**采样过程的逆**——采样把连续函数变离散点，Parzen window 把离散训练点变回连续函数（每个样本放一个连续 kernel 再叠加）。机器学习本质是这个逆过程，但有不确定性（带宽/参数选择），故称"learning"而非确定性"feed-forward"。

### 12. ⭐ Parametric：Maximum Likelihood Estimation (MLE)

Parametric approach 假设 PDF 形式已知（如 Gaussian），只需估计参数（Gaussian 的 mean vector、covariance matrix）。

**Likelihood**：参数 $\theta$ 下训练数据出现的联合概率 $p(\mathbf{x}_1,\dots,\mathbf{x}_N|\theta)$，称为参数对数据的 **likelihood**（"可能性"）。

**MLE 原则**：选使 likelihood 最大的参数：

$$
\hat\theta=\arg\max_\theta\prod_{i=1}^{N}p(\mathbf{x}_i|\theta)
$$

取 log（乘积变求和）：

$$
\hat\theta=\arg\max_\theta\sum_{i=1}^{N}\ln p(\mathbf{x}_i|\theta)
$$

再对参数求导 $\nabla_\theta\sum\ln p(\mathbf{x}_i|\theta)=0$ 解出。

**一维 Gaussian 的 MLE 结果**（老师推导）：

$$
\boxed{\hat\mu=\frac{1}{N}\sum_{i=1}^{N}\mathbf{x}_i=\text{样本均值}}
$$

$$
\boxed{\hat\sigma^2=\frac{1}{N}\sum_{i=1}^{N}(\mathbf{x}_i-\hat\mu)^2=\text{样本方差}}
$$

- ⭐ **Gaussian mean 的 MLE = 样本均值；Gaussian variance 的 MLE = 样本方差。**
- 多维情形：covariance matrix 的 MLE = data covariance matrix（样本协方差矩阵）。
- 这是"常识性"公式，但本周从 MLE 推导**证明**它们就是 Gaussian 参数的最大似然估计。
- 非 Gaussian 模型：可用 Gaussian mixture 拟合（本课 skip）；deep network 也属 parametric approach（参数化模型，用数据训练）。

### 13. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| **scalar covariance $\sigma^2\mathbf{I}$** | 比 shared $\boldsymbol{\Sigma}$ 更严；$\boldsymbol{\Sigma}^{-1}=\tfrac1{\sigma^2}\mathbf{I}$，方向不变 |
| **边界过两 mean 连线** | 仅 $\sigma^2\mathbf{I}$ 时成立（上周 shared $\boldsymbol{\Sigma}$ 不一定） |
| **降维到 1D** | 法向量 $\propto\boldsymbol{\mu}_i-\boldsymbol{\mu}_k$，分类只需沿此方向投影 |
| **prior 移动 threshold** | prior 不等 → 边界平移；悬殊可移出两 mean 区间 |
| **minimum distance classifier** | $\omega^*=\arg\min_i\|\mathbf{x}-\boldsymbol{\mu}_i\|^2$，= template matching |
| **min distance 严格条件** | Gaussian + 共享 $\sigma^2\mathbf{I}$ + 等四条件全满足才 optimal |
| **estimation = ML** | statistical estimation 本质即 machine learning；PDF = 完备信息 |
| **prior 估计** | $\hat p(\omega_k)=N_k/N$ |
| **Parzen window** | $p(\mathbf{x})=\frac1N\sum\frac1{h^D}K(\frac{\mathbf{x}-\mathbf{x}_i}{h})$；kernel 光滑化；$h$ 关键 |
| **IID** | 训练样本须独立同分布 |
| **MLE Gaussian** | $\hat\mu=$ 样本均值，$\hat\sigma^2=$ 样本方差，covariance = data covariance matrix |
| **non-parametric vs parametric** | 前者不假设 PDF 形式（Parzen/K-NN），后者假设形式估参数（MLE） |

### 14. 本周要点小结

- **Topic 5 收尾**：scalar covariance $\boldsymbol{\Sigma}=\sigma^2\mathbf{I}$ 特例下，linear classifier 进一步简化——边界法向量 $\propto$ 类均值差，**必然过两 mean 连线**，分类只需沿类均值差方向的一维投影。
- **Minimum distance classifier**：等 prior + $\sigma^2\mathbf{I}$ 时，最优分类退化为"分到最近 class mean"= template matching。直观但**仅在四条件全满足时 optimal**。
- **Topic 6 开场**：未知 PDF、只有 training data 时，estimation = machine learning。先估 prior（$N_k/N$），再估 class-conditional PDF。
- **Non-parametric（Parzen window）**：density × volume ≈ probability；用 kernel 求和估 PDF；矩形窗→阶梯不光滑，改 Gaussian kernel；带宽 $h$ 是关键超参。
- **Parametric（MLE）**：假设 PDF 形式，最大化 likelihood；Gaussian 的 MLE = 样本均值/样本方差/data covariance matrix。
- **哲学**：PDF 是随机变量的完备信息；理论上学全 PDF 即最优，实践样本有限需选参数、常直接优化预测输出。

---

> **下一周（Week 6）预告**：老师末尾明确——分类/预测不能直接作用于 raw data，需先做 **feature selection / extraction** 预处理。**未来两周先讲 feature selection**（从高维数据选有用 component 作 feature），之后 Topic 8 讲 **feature extraction**（组合 raw data 各 component 生成新 feature，如 CNN feature map / Transformer token 变换）。feature selection/extraction 在整个系统中起极关键作用。具体以 Week 6 课件为准。

---

> **笔记约定**：本课英文授课、英文考试，核心术语保留英文（machine vision, image, pixel, convolution, impulse response, LSI/LTI, filter, filter mask, histogram, gray level, color space, RGB, HSI, LBP, HOG, Fourier transform, DFT, DTFT, sinusoid, sinc function, impulse train, magnitude/phase, conjugate symmetry, convolution theorem, zero padding, translation/rotation invariant, sampling, Nyquist, aliasing, band-limited, low-pass/high-pass filter, point processing, gamma correction, log transform, piecewise linear, histogram equalization, cdf, feature extraction, template matching, Euclidean distance, norm, normalization, correlation coefficient, nearest neighbor classifier, K-NN, order-statistic filter, median filter, alpha-trimmed mean, root signal, prior probability, posterior probability, class-conditional probability, likelihood, chain rule, law of total probability, mixture PDF/PMF, MAP decision rule, Bayes rule, decision region, decision boundary/threshold, error rate, discriminant function, Mahalanobis distance, covariance matrix, Gaussian/multivariate Gaussian, quadratic classifier, linear classifier, hyperplane, within-class scatter, Direct LDA, statistical estimation, machine learning, training data, non-parametric approach, parametric approach, Parzen window, kernel function, bandwidth, k-nearest neighbor, IID (independent and identically distributed), maximum likelihood estimation / MLE, likelihood, sample mean, sample variance, data covariance matrix, Gaussian mixture, feature selection, feature extraction, PCA, principal component analysis, LDA, linear discriminant analysis, eigenvector, eigenvalue, total scatter matrix, within-class scatter matrix, between-class scatter matrix, reconstruction error, variance, projection, dimensionality reduction, unsupervised, supervised, integral image, Haar-like feature, AdaBoost, Viola-Jones, boosting, feature generation, feature pool, sliding window, object detection 等）。中文用于组织句意与补充释义。

---

## Week 6 — Topic 8：Feature Extraction（PCA / LDA 维度缩减）＋ Topic 7 起：Feature Selection（Viola-Jones / AdaBoost 预告）

> **权威来源说明**：本周**没有官方 PDF 课件**，仅由 `week6.txt` 转写整理。转写噪声极大，以下笔记基于转写内容 + 已有 Week 1–5 笔记的上下文推断。无法确认的术语标注"待课件确认"。本周典型 ASR 错拼修正：
> - "road data" → **raw data**（原始数据）
> - "clasph / classp / classer / clasp" → **classifier**
> - "fue / full year transform" → **Fourier transform**
> - "cores magics / comet metrics / cosmetri / corns matrix / co matrix" → **covariance matrix**
> - "sycto matrix / scyt matrix / skate matrix" → **scatter matrix**
> - "ichenvector / ien vector / eichen vector / chen vector / i vector" → **eigenvector**
> - "ichenvalue / ichen vue / ien value / numbda / Nanda" → **eigenvalue**
> - "lacung / granger optimization" → **Lagrangian / Lagrange optimization**
> - "meniar / miniar / ninear / menial" → **linear**
> - "discrepant / discrepant analyses / discrettive" → **discriminant / discriminant analysis**
> - "ADA / ALDA" → **LDA**（linear discriminant analysis）
> - "precar / pretty car / pretty clear" → "pretty clear"（老师口头禅）
> - "recontraction / recontraction era / recontraction arrow" → **reconstruction error**
> - "g value / ge value / grid value / gi value" → **gray value**
> - "Vela / Vela Jones" → **Viola-Jones**
> - "adder boost" → **AdaBoost**
> - "IGCV" → **IJCV**（International Journal of Computer Vision）
> - "face titan / facial phase" → **Fisherfaces**

### 1. 本周主线与课程安排

老师开课即说明：

- **Assignment 已发布**，主题是 **dimensionality reduction for classification**（用 PCA / LDA 降维后做分类，比较不同降维方法与不同维度数下的 classification accuracy）。
- 本周先讲 **Topic 8（feature extraction / 维度缩减）**，再开始 **Topic 7（feature selection）**——因为下周只有半节课，下半节用于 **quiz**（Week 1 公布的 Week 7 课堂 quiz 30 分钟）。
- Topic 8 对应 Assignment，故本周讲解中会穿插 assignment 要求。

**承接 Week 5**：Week 5 结束于 Topic 6（statistical estimation / MLE），回答了"未知 PDF 如何从 training data 估计参数"。本周进入 Topic 7–8：**classifier 不能直接作用于 raw data，需先做 feature extraction 或 feature selection**。即便 deep learning / Transformer 的核心也是 feature extraction——最终 classification layer 只是一个简单 linear classifier。

### 2. Feature Extraction 的概念框架

#### 2.1 为什么需要 feature extraction

- Raw data 维度极高。例：300×200 灰度图像 → 展平为 **60,000 维向量**。
- 直接用 60,000 维做分类计算量过大，且大量信息与分类任务无关。
- 需把 60,000 维降维到例如 60 维（缩减 1000 倍），再做 classification。

#### 2.2 ⭐ Feature extraction vs Feature selection（核心区分）

| | Feature Extraction | Feature Selection |
|---|---|---|
| **方式** | **组合所有** raw component 生成新 feature（每个新 feature = 全部输入的加权和） | 从原始 component 中**选取子集**，不组合 |
| **数学形式** | $\mathbf{y}=\boldsymbol{\Phi}^T\mathbf{x}$，$\boldsymbol{\Phi}$ 为 $n\times m$ 矩阵 | 选取 $\mathbf{x}$ 的某些分量，其余丢弃 |
| **计算量** | 每个新 feature 需全部输入参与 → **较慢** | 训练时确定选哪些，预测时只算被选的 → **很快** |
| **本周归属** | Topic 8（PCA / LDA） | Topic 7（Viola-Jones / AdaBoost） |
| **对应课程编号** | Topic 8: Visual Data Dimensionality Reduction as Feature Extraction | Topic 7: Handcrafted Feature Generation and Feature Selection |

> ⭐ **Feature extraction**：每个新 feature 是**所有**原始数据的 combination（不同权重），故每个 feature 都 depends on all inputs。**Feature selection**：直接从原始数据中选一部分 component 作 feature，不组合，计算快。

#### 2.3 线性维度缩减的一般形式

所有 **linear method** 的维度缩减都可表示为矩阵乘法：

$$
\mathbf{y}=\boldsymbol{\Phi}^T\mathbf{x}
$$

- $\mathbf{x}\in\mathbb{R}^n$：$n$ 维原始数据（列向量）；$\boldsymbol{\Phi}\in\mathbb{R}^{n\times m}$：权重矩阵；$\mathbf{y}\in\mathbb{R}^m$：$m$ 维降维后数据（$m<n$）。
- Fourier transform、wavelet transform 等也是此形式，只是 $\boldsymbol{\Phi}$ 的元素**由人类预定义**（如 Fourier 的 $e^{-j2\pi u_i n/N}$）。
- 本课关注**由 training data 学习 $\boldsymbol{\Phi}$** 的方法（machine learning），而非人定义的 transform。

**矩阵乘法的两个效果**：
1. **Feature scaling**：每个输出 = 全部输入的 weighted sum，不同权重对输入做不同缩放。重要 component 赋大权重，不重要的赋小权重。
2. **Dimensionality reduction**：$\boldsymbol{\Phi}$ 为矩形（非方阵）时，$n$ 维 → $m$ 维。

### 3. ⭐⭐ PCA（Principal Component Analysis）— 本周核心之一

#### 3.1 问题设定

给定 $Q$ 个 training samples $\mathbf{x}_1,\dots,\mathbf{x}_Q$，每个 $\mathbf{x}_i\in\mathbb{R}^n$。目标：找最优降维。

#### 3.2 第一步：找最佳代表点（mean）

用一个点 $\mathbf{x}_0$ 代表所有 training data，最小化 mean squared error：

$$
\mathbf{x}_0=\arg\min_{\mathbf{x}_0}\sum_{i=1}^{Q}\|\mathbf{x}_i-\mathbf{x}_0\|^2
$$

- 对 $\mathbf{x}_0$ 求导令零，得 $\mathbf{x}_0=\frac{1}{Q}\sum_{i=1}^{Q}\mathbf{x}_i$，即**样本均值（sample mean）**。
- ⭐ 与 Week 5 呼应：mean 是使 mean squared error 最小的点，也是 Gaussian PDF 中心的最大似然估计（MLE）。
- **Centralize**：所有训练样本减去 mean，$\tilde{\mathbf{x}}_i=\mathbf{x}_i-\mathbf{x}_0$，组成中心化数据矩阵。

#### 3.3 第二步：找最佳一维方向（第一主成分）

在 $n$ 维空间中找一个**单位长度向量** $\boldsymbol{\phi}$（代表一个方向/坐标轴），将所有数据投影到该方向：

$$
a_i=\boldsymbol{\phi}^T\tilde{\mathbf{x}}_i\quad(\text{标量投影})
$$

用 $a_i$ 重建原始数据：$\hat{\mathbf{x}}_i=a_i\boldsymbol{\phi}$。重建误差为：

$$
\epsilon=\sum_{i=1}^{Q}\|\tilde{\mathbf{x}}_i-a_i\boldsymbol{\phi}\|^2
$$

展开化简（利用 $\boldsymbol{\phi}^T\boldsymbol{\phi}=1$）：

$$
\epsilon=\sum_{i}\|\tilde{\mathbf{x}}_i\|^2-\sum_{i}(\boldsymbol{\phi}^T\tilde{\mathbf{x}}_i)^2
$$

- 第一项与 $\boldsymbol{\phi}$ 无关 → 最小化 $\epsilon$ 等价于**最大化** $\sum_i(\boldsymbol{\phi}^T\tilde{\mathbf{x}}_i)^2$。

#### 3.4 ⭐ 识别出 covariance / scatter matrix

将最大化目标改写：

$$
\sum_{i=1}^{Q}(\boldsymbol{\phi}^T\tilde{\mathbf{x}}_i)^2=\sum_{i=1}^{Q}\boldsymbol{\phi}^T\tilde{\mathbf{x}}_i\tilde{\mathbf{x}}_i^T\boldsymbol{\phi}=\boldsymbol{\phi}^T\left(\sum_{i=1}^{Q}\tilde{\mathbf{x}}_i\tilde{\mathbf{x}}_i^T\right)\boldsymbol{\phi}
$$

$$
\mathbf{S}_T=\sum_{i=1}^{Q}\tilde{\mathbf{x}}_i\tilde{\mathbf{x}}_i^T\quad\text{（total scatter matrix / covariance matrix）}
$$

- $\mathbf{S}_T$ 即训练数据的 **total scatter matrix**（或 covariance matrix，差一个 $1/Q$ 因子）。
- 最大化目标变为 $\boldsymbol{\phi}^T\mathbf{S}_T\boldsymbol{\phi}$，约束 $\|\boldsymbol{\phi}\|=1$。

#### 3.5 ⭐ Lagrangian 推导 → 特征方程

条件优化：最大化 $\boldsymbol{\phi}^T\mathbf{S}_T\boldsymbol{\phi}$，约束 $\boldsymbol{\phi}^T\boldsymbol{\phi}=1$。

用 **Lagrangian method**（拉格朗日乘子法）转化为无条件优化，对 $\boldsymbol{\phi}$ 求导令零：

$$
\mathbf{S}_T\boldsymbol{\phi}=\lambda\boldsymbol{\phi}
$$

⭐ **这正是 eigenvector / eigenvalue 的定义方程**。最优投影方向 $\boldsymbol{\phi}$ 是 $\mathbf{S}_T$ 的 **eigenvector**，对应的 $\lambda$ 是 **eigenvalue**。

#### 3.6 ⭐⭐ PCA 的物理意义（老师重点，务必理解）

**Eigenvector 的物理意义**：

$$
\boldsymbol{\phi}^T\mathbf{S}_T\boldsymbol{\phi}=\boldsymbol{\phi}^T\left(\sum_i\tilde{\mathbf{x}}_i\tilde{\mathbf{x}}_i^T\right)\boldsymbol{\phi}=\sum_i(\boldsymbol{\phi}^T\tilde{\mathbf{x}}_i)^2=\sum_i a_i^2
$$

- $a_i=\boldsymbol{\phi}^T\tilde{\mathbf{x}}_i$ 是数据投影到 $\boldsymbol{\phi}$ 方向后的标量值。
- $\sum a_i^2$（中心化后 $a_i$ 均值为 0）就是数据沿 $\boldsymbol{\phi}$ 方向投影的 **variance（方差）**。
- ⭐ **Eigenvector = 使投影后方差最大的方向**。对应的 **eigenvalue = 该方向上的方差值**。

> **一句话**：PCA 的 eigenvector 是数据投影后方差最大的方向；eigenvalue 就是该方向的 variance。第一主成分（largest eigenvalue 对应的 eigenvector）方向方差最大，第二主成分次之，依此类推。

#### 3.7 推广到 $m$ 维：PCA 算法

取 $\mathbf{S}_T$ 的 **$m$ 个最大 eigenvalue 对应的 eigenvector** $\boldsymbol{\phi}_1,\dots,\boldsymbol{\phi}_m$，组成 eigenvector matrix $\boldsymbol{\Phi}=[\boldsymbol{\phi}_1,\dots,\boldsymbol{\phi}_m]$：

$$
\mathbf{y}=\boldsymbol{\Phi}^T\tilde{\mathbf{x}}\in\mathbb{R}^m\quad\text{（降维后 feature）}
$$

重建：

$$
\hat{\mathbf{x}}=\boldsymbol{\Phi}\mathbf{y}+\mathbf{x}_0
$$

⭐ **重建误差**等于**未被选取的 eigenvalue 之和**：

$$
\epsilon=\sum_{j=m+1}^{n}\lambda_j\quad\text{（剩余 eigenvalue 之和）}
$$

- 取最大的 $m$ 个 eigenvalue → 剩余 eigenvalue 之和最小 → **重建误差最小**。
- 若取所有非零 eigenvalue 对应的 eigenvector，重建误差可为 **零**（信息无损）。

#### 3.8 ⭐ Scatter matrix 的秩与无损降维

- $\mathbf{S}_T$ 由 $Q$ 个训练样本构成，其秩 $\text{rank}(\mathbf{S}_T)\le Q-1$（减 mean 后损失一个自由度）。
- 若 $Q-1\ll n$（训练样本远少于数据维度），则 $\mathbf{S}_T$ 最多有 $Q-1$ 个非零 eigenvalue。
- → 可将 $n$ 维数据无损降至 $Q-1$ 维（重建误差为零），因为其余 $n-(Q-1)$ 个 eigenvalue 为零。

> **直觉**：所有训练点在高维空间中实际只分布在一个低维子空间（如 3D 中所有点恰在一个平面上 → 垂直于该平面的方向 variance 为零 → eigenvalue 为零 → 该方向可丢弃）。

#### 3.9 ⭐ Symmetric matrix 的性质

- $\mathbf{S}_T$（covariance / scatter matrix）是 **symmetric matrix（对称矩阵）**。
- 对称矩阵的 eigenvector 对应**不同 eigenvalue** 的彼此 **orthogonal（正交）**。
- 取 unit length 后即为 **orthonormal（正交归一）**：$\boldsymbol{\Phi}^T\boldsymbol{\Phi}=\mathbf{I}$，$\boldsymbol{\Phi}\boldsymbol{\Phi}^T=\mathbf{I}$。
- → eigenvector 可作为新坐标系的正交轴。

⭐ 由此得两个重要关系：

$$
\boldsymbol{\Phi}^T\mathbf{S}_T\boldsymbol{\Phi}=\boldsymbol{\Lambda}\quad\text{（对角化：对角元为 eigenvalue）}
$$

$$
\mathbf{S}_T=\boldsymbol{\Phi}\boldsymbol{\Lambda}\boldsymbol{\Phi}^T\quad\text{（谱分解）}
$$

- 投影到 eigenvector 后，新数据 $\mathbf{y}$ 的 covariance matrix 为**对角矩阵**（各分量 uncorrelated / 去相关）。
- ⭐ **与 Transformer 的联系**（老师提示）：Transformer 的 attention 本质是 covariance matrix 的运算；理解 covariance matrix 的物理意义有助于理解最先进的 AI 模型。

#### 3.10 二维可视化示例

- 2D 数据散点呈椭圆形云（cloud），沿长轴方向 variance 最大 → $\boldsymbol{\phi}_1$（第一主成分）沿长轴方向。
- $\boldsymbol{\phi}_2$ 沿短轴方向，与 $\boldsymbol{\phi}_1$ 正交。
- 投影到 $(\boldsymbol{\phi}_1,\boldsymbol{\phi}_2)$ 后只是**旋转坐标系**，数据本身不变，但新坐标下 covariance matrix 变为对角矩阵（两分量 uncorrelated）。
- Covariance matrix 的对角元 $\sigma_{11},\sigma_{22}$ 决定椭圆的长短轴（variance），非对角元 $\sigma_{12}$ 决定椭圆的倾斜程度（correlation）：
  - $\sigma_{12}=0$：椭圆轴与坐标轴对齐（uncorrelated）。
  - $|\sigma_{12}|$ 大：椭圆很扁、倾斜（强相关）。
  - 完全 linear correlated：椭圆退化为一条直线（短轴为零）。

### 4. ⭐⭐ LDA（Linear Discriminant Analysis）— 本周核心之二

#### 4.1 PCA 的问题：unsupervised，不利用 class membership

- PCA 只最大化**总体 variance**，不关心类别信息（**unsupervised**）。
- ⭐ **关键反例**（老师详讲）：两类数据（黑点与十字），沿最大 variance 方向（PCA 选的红线）投影后两类**完全重叠** → classification error ≈ 50%。而沿另一方向（绿线，variance 较小但两类分离好）投影后 error ≈ 5–10%。
- **结论**：PCA 对 classification **不一定好**——最大化 general information（variance）≠ 最大化 discriminative information。

#### 4.2 LDA 的核心思想

LDA 是 **supervised**（利用 class membership），目标：找投影方向使得
- **Between-class variance 最大化**（不同类中心尽量分开）；
- **Within-class variance 最小化**（同类数据尽量紧凑）。

#### 4.3 ⭐ 两个 scatter matrix

**Within-class scatter matrix** $\mathbf{S}_W$：

- 对每个类 $\omega_k$ 计算 class-conditional covariance matrix $\mathbf{S}_k=\sum_{i\in\omega_k}(\mathbf{x}_i-\boldsymbol{\mu}_k)(\mathbf{x}_i-\boldsymbol{\mu}_k)^T$。
- $\mathbf{S}_W=\sum_{k=1}^{c}P_k\mathbf{S}_k$（按类先验/样本数加权平均）。
- $\mathbf{S}_W$ 反映**各类内部**数据的 variation（average of class-conditional covariance）。

**Between-class scatter matrix** $\mathbf{S}_B$：

$$
\mathbf{S}_B=\sum_{k=1}^{c}P_k(\boldsymbol{\mu}_k-\boldsymbol{\mu})(\boldsymbol{\mu}_k-\boldsymbol{\mu})^T
$$

- $\boldsymbol{\mu}_k$：类 $k$ 的 mean；$\boldsymbol{\mu}$：全局 mean。
- $\mathbf{S}_B$ 反映**各类中心之间**的差异。

⭐ **重要关系**：

$$
\mathbf{S}_T=\mathbf{S}_W+\mathbf{S}_B
$$

- Total variation = within-class variation + between-class variation。这与 Week 4–5 的 discriminant function 中 covariance 的角色一致。

#### 4.4 ⭐ LDA 的优化目标与求解

最大化 **Fisher criterion**（投影后 between-class variance / within-class variance）：

$$
\boldsymbol{\phi}=\arg\max_{\boldsymbol{\phi}}\frac{\boldsymbol{\phi}^T\mathbf{S}_B\boldsymbol{\phi}}{\boldsymbol{\phi}^T\mathbf{S}_W\boldsymbol{\phi}}
$$

- 最大化 $\mathbf{S}_B$ 的同时最小化 $\mathbf{S}_W$ → 用 $\mathbf{S}_W^{-1}\mathbf{S}_B$。
- 与 PCA 同理，解变为 **eigenvector / eigenvalue 问题**：

$$
\mathbf{S}_W^{-1}\mathbf{S}_B\boldsymbol{\phi}=\lambda\boldsymbol{\phi}
$$

- LDA 取 $\mathbf{S}_W^{-1}\mathbf{S}_B$ 的 **largest eigenvalue** 对应的 eigenvector。

⭐ **PCA vs LDA 求解对比**：

| | PCA | LDA |
|---|---|---|
| **矩阵** | $\mathbf{S}_T$（total scatter） | $\mathbf{S}_W^{-1}\mathbf{S}_B$ |
| **监督** | Unsupervised（不用 class label） | Supervised（用 class membership） |
| **最大化** | Total variance | Between-class / within-class ratio |
| **求解** | Eigenvector of $\mathbf{S}_T$ | Eigenvector of $\mathbf{S}_W^{-1}\mathbf{S}_B$ |
| **对分类** | 不保证好（最大化 general variance） | 更好（最大化 discriminative information） |

#### 4.5 ⭐ LDA 的实际问题：$S_W$ 不满秩

- $\text{rank}(\mathbf{S}_W)=Q-c$（$Q$：总训练样本数，$c$：类数；每类减 mean 损失一个自由度）。
- 20 年前常见情形：$Q$ 远小于数据维度 $n$（如每人仅 2–3 张人脸图像，维度上百万）→ $\mathbf{S}_W$ **不满秩** → $\mathbf{S}_W^{-1}$ 不存在 → 无法直接做 LDA。
- ⭐ **解决方案：PCA + LDA**（先 PCA 降维到 $\mathbf{S}_W$ 满秩的维度，再 LDA）。人脸识别中称为 **Fisherfaces**。
- 这是当年数千篇论文的研究热点。

#### 4.6 ⭐⭐ 老师的批判性思考（重点理解，与 assignment 相关）

老师提出一个**根本性问题**，指出大量研究者忽视了它：

> 原始高维数据应该含有**最多**的 discriminative information。LDA 降维后**丢失**一部分信息，却声称保留"最 discriminative"的信息。如果"最 discriminative"信息意味着最好的分类结果，那为什么不在原始高维空间直接分类？为什么要降维？

**老师的洞察**：

- 降维能**提高** classification accuracy 的真正原因，不是"保留了最 discriminative 的信息"（LDA 只能**尽量不丢** discriminative 信息，但不能**新增**信息），而是**去除了 misleading information（误导信息）**。
- **Misleading information**：训练数据中某些信息虽然是 discriminative 的（能区分类别），但实际上是**噪声/虚假的 discriminative 信息**，会误导 classifier。
  - 例：人脸图像含表情、光照等信息，这些信息虽然能"区分"训练样本，但对**识别身份**是 misleading 的。
- **关键**：真正提升 accuracy 的关键是**识别并去除 misleading information**，而非单纯保留 discriminative information。
- 去除 misleading information → accuracy 可超过原始高维数据。
- 但识别 misleading information 非常困难（难以区分 real discriminative vs misleading discriminative）。

**Assignment 要求**：

- 用 PCA 和 LDA 降维到不同维度，画出 **classification accuracy vs. dimension** 曲线。
- 观察并解释曲线形状：一般 dimension 减少时 accuracy 下降；但若降维方法好（去除了 misleading info），低维可能不降甚至略升。
- 老师给了 3 篇参考论文（已确认，见 §9 官方要求）。
- ⚠️ 老师批评：很多研究者在低维下比较 PCA vs LDA 得出"LDA 更好"的结论，但若只看低维段，结论可能错误——LDA 只是让 accuracy 下降慢，真正提升来自去除 misleading info 的步骤。

### 5. 降维后的分类流程总结

1. 用 training data 计算 scatter matrix（$\mathbf{S}_T$ for PCA，$\mathbf{S}_W,\mathbf{S}_B$ for LDA）。
2. 求 eigenvector / eigenvalue，取 top-$m$ eigenvector 组成 $\boldsymbol{\Phi}$。
3. 对所有数据（训练+测试）投影：$\mathbf{y}=\boldsymbol{\Phi}^T(\mathbf{x}-\boldsymbol{\mu})$。
4. 在 $m$ 维 feature space 中做分类：
   - 计算 feature space 的 mean $\boldsymbol{\mu}_{k,F}$ 和 covariance $\boldsymbol{\Sigma}_{k,F}$（或 pooled covariance）。
   - 用 Mahalanobis distance / minimum distance classifier 分类。
5. ⭐ 实践中常用 **pooled covariance**（$\mathbf{S}_W$）而非每类各自的 covariance——样本少时更可靠（average over all classes），且共享 covariance → linear classifier。

### 6. Topic 7 开场：Feature Selection 与 Viola-Jones 方法

#### 6.1 为什么需要 feature selection

- Feature extraction（PCA / LDA）每个新 feature 需**全部**原始数据参与计算 → 计算量大。
- 某些应用需**极快**的 feature 计算 → **feature selection**：直接选取原始数据的部分 component，不组合。
- 训练时确定选哪些 component，预测时只算被选的 → 极快。

#### 6.2 ⭐ 应用驱动：Object Detection（物体检测）

以 **face detection** 为例（老师详讲）：

- 输入图像中，目标（face）位置和大小未知。
- 方法：用固定大小窗口（如 24×24）**扫描（sliding window）**所有位置，每个位置做一次 binary classification（face / non-face）。
- 还需尝试不同 window size 以检测不同 scale 的 face。
- → 需在每个位置提取 feature + 分类，执行次数可达**数万甚至百万级**。
- → 极需快速 feature 计算与快速分类。

**三大挑战**：
1. 如何**快速计算** feature（避免重复计算，如 FFT vs DFT）？
2. 如何用**少量 feature** 就能代表整个 raw data？
3. 如何在少量 feature 下仍获得好的 classification accuracy？

#### 6.3 ⭐ Viola-Jones 方法（face detection 经典方法，IJCV 发表）

- **Viola 和 Jones**（来自—in the transcript—待课件确认机构）提出，发表于 **IJCV**（International Journal of Computer Vision）。
- 深度学习前最流行的 face detection 方法，被各大公司采用。

**核心组件**：

1. **Haar-like feature（矩形特征）**：两个矩形区域 average gray value 的**差值**。
   - 差值反映**对比度（contrast）**，能捕捉图像结构。例：鼻部两侧亮度差大，眼部上下亮度差大。
   - 用矩形是因为矩形内像素之和可**极快计算**（利用 integral image）。

2. **⭐ Integral Image（积分图）**：预处理一步，之后任意矩形内像素之和只需 **3 次加减法**。
   - 定义：$I(x,y)=\sum_{x'\le x,\,y'\le y}f(x',y')$，即左上角到 $(x,y)$ 的所有像素之和。
   - **快速计算**：利用已算出的相邻位置的 integral image 值，递推只需 2 次加法/像素。
   - **任意矩形 D 的像素和**：$\text{Sum}(D)=I(4)-I(2)-I(3)+I(1)$，其中 $1,2,3,4$ 是矩形四个角点（3 次加减法，与矩形大小无关）。
   - → 任意大小、任意位置的 Haar-like feature 都可在常数时间算出。

3. **Feature pool 巨大**：24×24 检测窗口可生成约 **180,000** 种不同 Haar-like feature（不同矩形形状、大小、位置组合）。

4. **Feature selection**：从 180,000 个 feature 中选约 **100 个**最有效的 → 预测时只算这 100 个 → 极快。

5. **AdaBoost（Adaptive Boosting）**：用于从大 pool 中选取最有效的少量 feature。具体算法**下周讲**（半节课）。

#### 6.4 Feature selection 的流程

| 阶段 | 操作 |
|---|---|
| **离线训练** | 用 training data 生成全部 feature（如 180,000 个），用 AdaBoost 选出最有用的约 100 个 |
| **在线预测** | 只计算被选中的 100 个 feature + 分类 → 极快 |

- Viola-Jones 原始实验：4,900 张 face + 10,000 张 non-face 训练数据（20 年前已算大规模）。
- 关键：feature selection 后预测阶段无需计算未选 feature，计算量大幅降低。

### 7. ⭐ 本周考点速查

| 考点 | 要点 | 节号 |
|---|---|---|
| **feature extraction vs selection** | extraction 组合全部输入；selection 选取子集；后者更快 | §2.2 |
| **线性降维一般形式** | $\mathbf{y}=\boldsymbol{\Phi}^T\mathbf{x}$，$\boldsymbol{\Phi}$ 可人定义或从数据学习 | §2.3 |
| **PCA：最佳代表点 = mean** | mean 最小化 MSE，也是 Gaussian 中心的 MLE | §3.2 |
| **PCA：最佳方向 = 最大 variance 方向** | 投影后方差最大的方向 = eigenvector of $\mathbf{S}_T$ | §3.3–3.6 |
| **PCA：Lagrangian → 特征方程** | $\mathbf{S}_T\boldsymbol{\phi}=\lambda\boldsymbol{\phi}$ | §3.5 |
| **⭐ eigenvector 物理意义** | 投影后方差最大的方向 | §3.6 |
| **⭐ eigenvalue 物理意义** | 该方向的 variance 值 | §3.6 |
| **PCA 重建误差** | 未被选取的 eigenvalue 之和 | §3.7 |
| **无损降维条件** | 取所有非零 eigenvalue；$\text{rank}(\mathbf{S}_T)\le Q-1$ | §3.8 |
| **对称矩阵性质** | eigenvector orthonormal；$\boldsymbol{\Phi}^T\mathbf{S}_T\boldsymbol{\Phi}=\boldsymbol{\Lambda}$（对角化去相关） | §3.9 |
| **PCA 是 unsupervised** | 不用 class label，最大化 total variance | §4.1 |
| **PCA 对分类不好** | 最大 variance 方向可能两类重叠（error ≈ 50%） | §4.1 |
| **LDA：Fisher criterion** | $\max\,\boldsymbol{\phi}^T\mathbf{S}_B\boldsymbol{\phi}/\boldsymbol{\phi}^T\mathbf{S}_W\boldsymbol{\phi}$ | §4.4 |
| **LDA 求解** | eigenvector of $\mathbf{S}_W^{-1}\mathbf{S}_B$ | §4.4 |
| **$\mathbf{S}_T=\mathbf{S}_W+\mathbf{S}_B$** | total = within + between | §4.3 |
| **LDA：$S_W$ 不满秩** | $Q\ll n$ 时 $S_W$ 奇异 → PCA+LDA（Fisherfaces） | §4.5 |
| **⭐⭐ 降维提升 accuracy 的原因** | 去除 misleading information，非保留 discriminative info | §4.6 |
| **pooled covariance** | 样本少时更可靠 → 共享 $\Sigma$ → linear classifier | §5 |
| **Viola-Jones** | Haar-like feature + integral image + AdaBoost feature selection | §6.3 |
| **Integral image** | 任意矩形像素和只需 3 次加减法 | §6.3 |
| **Feature pool 大小** | 24×24 窗口 → ~180,000 feature | §6.3 |

### 8. 本周要点小结

- **Feature extraction**（Topic 8）组合全部原始数据生成新 feature，每个 feature = 全部输入的加权和；**feature selection**（Topic 7）直接选取原始 component 子集，计算更快。
- **PCA**：unsupervised，找 covariance matrix $\mathbf{S}_T$ 的 eigenvector，投影后方差最大；eigenvalue = variance；重建误差 = 未选 eigenvalue 之和；取 top-$m$ 个 → 最小重建误差。对称矩阵 eigenvector orthonormal → 投影后去相关。
- **LDA**：supervised，利用 class membership，最大化 $\mathbf{S}_B/\mathbf{S}_W$ 比，解 $\mathbf{S}_W^{-1}\mathbf{S}_B$ 的特征方程。$\mathbf{S}_T=\mathbf{S}_W+\mathbf{S}_B$。$S_W$ 不满秩时用 PCA+LDA（Fisherfaces）。
- **PCA vs LDA for classification**：PCA 最大化 total variance，不保证分类好；LDA 最大化 discriminative information。但老师强调：降维提升 accuracy 的真正原因是**去除 misleading information**，而非保留 discriminative info——很多研究者未深究此问题。
- **Viola-Jones**：face detection 经典。Haar-like feature（矩形 average gray value 差）+ integral image（任意矩形和 3 次运算）+ AdaBoost（从 ~180,000 feature 中选 ~100 个）→ 极快检测。
- **Assignment**：用 PCA / LDA 降维到不同维度，画 classification accuracy vs dimension 曲线，观察并解释。

### 9. ⭐⭐ Assignment 1 官方要求（权威：`assignment1/Assignment.pdf`）

> 标题：**Assignment 1: Dimensionality Reduction for Classification（15%）**。以下是官方 PDF 的完整要求（2026-09-14 版），与老师课上的口头说明一致。

**任务**：

- 写一个 **mini-computer program**：实现 dimensionality reduction + classification + classification accuracy / error rate 计算。
- 画出 **classification accuracy（或 error rate） vs. dimensionality** 曲线（降维到不同维数分别做 classification 后绘图）。
- 编程语言不限（**Python、Matlab 或其他均可**）。

**数据**：

- 任选**公开高维数据集**（images or others，从网上下载），或用程序生成的 **synthetic data**。
- 可能需要 **pre-processing**：alignment、normalization，使数据适合 classification。
- ⭐⭐ **必须正确划分 training / testing dataset**；**dimensionality reduction 与 classification 的所有参数只能由 training data 确定**；testing data **只能**用于生成 classification accuracy / error rate（不得参与任何调参）。

**方法**：

- 可用 **PCA、LDA、两者结合、或任何其他方法**，把数据降到多个不同 dimensionality 分别做 classification，画 accuracy vs. dimensionality 曲线。
- 推荐分类器：**minimum Mahalanobis distance classifier**、linear classifier、**nearest neighbor classifier**。

**报告**：

- **4–5 页**（含 figures、tables、references，但**不含**程序代码）。
- 须记录：experimental process / settings、results、analysis and comparison of results、conclusions drawn from the experiments。
- 程序代码作为 **appendix** 放在报告末尾。

**提交**：

- **PDF 提交到 NTULearn**，截止 **Week 10 结束：2026 年 10 月 25 日**。
- 文件名 = 学生证上的姓名 + matric number，例如 `HOEJIUNTIAN-U2203856C`。

**3 篇参考论文（Reference）**：

1. X. Jiang, "Linear Subspace Learning-Based Dimensionality Reduction," *IEEE Signal Processing Magazine*, vol. 28, no. 2, pp. 16–26, March 2011.
2. X. Jiang, "Asymmetric Principal Component and Discriminant Analyses for Pattern Classification," *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)*, vol. 31, no. 5, pp. 931–937, May 2009.
3. X. Jiang, B. Mandal and A. Kot, "Eigenfeature Regularization and Extraction in Face Recognition," *IEEE TPAMI*, vol. 30, no. 3, pp. 383–394, March 2008.

> ⚠️ AI 使用规则（Week 1 声明）：允许用 generative model 生成报告，但须逐字审阅、理解并**纠正 AI 的错误**；原样照搬会被判 wrong。

---

> **下一周（Week 7）预告**：老师明确说明下周只有**半节课**（下半节用于 **quiz**，Week 1 公布的 30 分钟课堂 quiz，占 10%）。上半节将继续 Topic 7 的 **AdaBoost（Adaptive Boosting）算法**——如何从巨大的 feature pool 中用 boosting 方法选出最有效的少量 feature。Viola-Jones 的 feature selection 具体算法将在下周完成。AdaBoost 是 ensemble learning 的经典方法，也可视为 embedded feature selection 的代表（feature selection 与 classifier 训练同时进行）。具体以 Week 7 课件/转写为准。

## Week 7 — AdaBoost Feature Selection 与 Cascade Classifier（Quiz 1 周）

> 本周上半节课讲完 Topic 7 的核心算法 **AdaBoost（Adaptive Boosting）**，完成 Viola-Jones feature selection 的算法部分；下半节为 **Quiz 1**（25 题 / 30 分钟，占 10%）。本笔记聚焦 AdaBoost 部分与 cascade classifier；Quiz 1 的行政/考务信息在末尾简述。

### 1. 回顾：Feature Extraction vs Feature Selection

- **Feature extraction**（PCA / LDA）：每个新 feature = **全部**原始数据的线性组合 → 预测时计算量大（如 30,000 像素 → 100 feature，每个 feature 都需对全部 30,000 做加权和）。
- **Feature selection**：从预先生成的大 feature pool 中**选子集**，预测时只算被选中的 feature → 极快。
  - 不能直接从原始 pixel 中选（少量 pixel 不是好 feature）；需先生成合理的 feature pool（如 Haar-like feature）。
  - 训练阶段：计算所有候选 feature + 用 AdaBoost 选出最有用的少量 feature。
  - 在线预测阶段：只计算被选中的 ~100 个 feature + 分类。

| 阶段 | 操作 | 计算量 |
|---|---|---|
| **离线训练** | 生成全部 feature（如 ~180,000 个 Haar-like feature），用 AdaBoost 选出 ~100 个 | 大，但只做一次 |
| **在线预测** | 只计算被选中的 ~100 个 feature + 分类 | 极快 |

### 2. ⭐ Boosting 思想：从 Weak Learner 到 Strong Learner

#### 2.1 Ensemble Learning 与 Boosting 动机

- **Boosting**（提升方法）属于 **ensemble learning（集成学习）**：组合多个 weak learner → 一个 strong learner。
- 在 Viola-Jones 中，每个 **weak classifier** 只使用 **一个 single feature**（一个 Haar-like feature 对应一个 weak classifier）。
  - 1 维 feature（单个 Haar-like feature 值）→ 用一个 threshold 分类为两类 → 极简单。
  - 选 feature = 选 weak classifier（一一对应）。
- **Weak learner**：error rate 略好于随机猜（binary classification 最大 error rate = 0.5，weak learner 只需 error rate < 0.5）。
- **Strong learner**：组合多个 weak learner 后，error rate 可极小。

#### 2.2 ⭐ 为什么不能贪心选"各自最优"的 feature

- 若每次独立选当前 error rate 最低的 feature，第二个 feature 可能与第一个**高度相似** → 组合后 accuracy 几乎不提升。
- **关键需求**：所选 feature 应**互相补偿（compensate each other）**——后续 feature 应修正前序 feature 的错误，而非重复其能力。
- AdaBoost 的核心智慧：通过**调整样本权重**实现 compensating selection——让后续 feature 重点关注前序 feature 分错的样本。

#### 2.3 为什么不直接联合搜索最优 feature 子集

| 选 feature 数 | 组合数（从 10,000 个中选） | 可行性 |
|---|---|---|
| 1 | 10,000 | 可行（逐一测试） |
| 2 | ≈ 10,000² = 10⁸ | 勉强可行 |
| 100 | ≈ 10,000¹⁰⁰ | 完全不可行 |

- 联合搜索 100 个 feature 的最优组合是 NP-hard 级别。
- AdaBoost 退而求其次：**逐个选**（每轮只测 ~10,000 次），但通过权重更新保证所选 feature 互补。

### 3. ⭐⭐ AdaBoost 算法详解

#### 3.1 记号

| 符号 | 含义 |
|---|---|
| $x_1, x_2, \ldots, x_N$ | $N$ 个 training sample（训练图像） |
| $y_1, y_2, \ldots, y_N$ | class label，$y_i \in \{+1, -1\}$（+1 = positive，-1 = negative） |
| $g$ | feature 池中某个 feature 的 index |
| $f_g$ | 第 $g$ 个 feature 的值 |
| $h_g(x)$ | 用 feature $g$ 构建的 weak classifier（threshold classifier） |
| $t$ | 迭代轮次，$t = 1, 2, \ldots, T$（$T$ = 要选的 feature 总数） |
| $w_t(i)$ | 第 $t$ 轮中 training sample $i$ 的权重 |
| $\varepsilon_t$ | 第 $t$ 轮选中的 weak classifier 的（加权）error rate |
| $\alpha_t$ | 第 $t$ 个 weak classifier 在 strong classifier 中的组合权重 |

#### 3.2 Weak Classifier 设计（单 feature threshold）

每个 feature $g$ 对应一个最简单的 1-D threshold classifier：

$$
h_g(x_i) = \begin{cases} +1 & \text{if } f_g(x_i) > \theta_g \\ -1 & \text{if } f_g(x_i) \le \theta_g \end{cases}
$$

- $\theta_g$：feature $g$ 的最优 threshold，通过扫描所有 training sample 的 feature 值、取相邻样本间的值来确定（使 error rate 最小）。
- 每个 feature 都可独立构建一个 weak classifier → 选 feature = 选 weak classifier。

#### 3.3 ⭐ 算法步骤

**初始化**：所有 training sample 权重均等

$$
w_1(i) = \frac{1}{N}, \quad i = 1, 2, \ldots, N
$$

**For** $t = 1, 2, \ldots, T$：

1. **训练 weak classifier**：对每个候选 feature $g$，用其 weak classifier $h_g$ 分类所有 training sample，计算加权 error rate：

$$
\varepsilon_g = \sum_{i=1}^{N} w_t(i) \cdot \mathbf{1}[h_g(x_i) \neq y_i]
$$

2. **选择最小 error rate 的 feature**：

$$
\varepsilon_t = \min_g \varepsilon_g, \quad h_t = h_{g^*} \text{（对应最小 error rate 的 feature } g^*）
$$

   - ⭐ 注意：error rate 必须满足 $\varepsilon_t < 0.5$（binary classification 最大 error rate = 0.5，否则该 weak classifier 无意义；实际中总能满足）。

3. **计算 weak classifier 的组合权重 $\alpha_t$**：

$$
\boxed{\alpha_t = \frac{1}{2} \ln\!\left(\frac{1 - \varepsilon_t}{\varepsilon_t}\right)}
$$

   - $\varepsilon_t \to 0$（极好 feature）→ $\frac{1-\varepsilon_t}{\varepsilon_t} \to \infty$ → $\alpha_t \to \infty$（该 classifier 在 strong classifier 中占主导）。
   - $\varepsilon_t \to 0.5$（最差 weak learner）→ $\frac{1-\varepsilon_t}{\varepsilon_t} \to 1$ → $\alpha_t \to 0$（几乎无贡献）。
   - 取 logarithm 的原因：后续权重更新用 exponential 函数，log 与 exp 可相互抵消，避免数值范围剧烈变化；乘 $\frac{1}{2}$ 为常规缩放（非严格必需）。

4. **更新 sample 权重**：

$$
\boxed{w_{t+1}(i) = \frac{w_t(i) \cdot \exp\!\left(-\alpha_t \, y_i \, h_t(x_i)\right)}{Z_t}}
$$

   - $Z_t$：normalization factor，使 $\sum_i w_{t+1}(i) = 1$。
   - **分类正确**（$y_i = h_t(x_i)$）→ $y_i \cdot h_t(x_i) = +1$ → $\exp(-\alpha_t) < 1$ → 权重**减小**。
   - **分类错误**（$y_i \neq h_t(x_i)$）→ $y_i \cdot h_t(x_i) = -1$ → $\exp(+\alpha_t) > 1$ → 权重**增大**。
   - ⭐ 核心：被前序 feature 分错的 sample 权重变大 → 下一轮选 feature 时若仍分错这些 sample，加权 error rate 会很大 → 不会被选中 → 迫使下一轮选能修正前序错误的 feature。

**输出**：Strong classifier（加权投票）

$$
\boxed{H(x) = \begin{cases} +1 & \text{if } \displaystyle\sum_{t=1}^{T} \alpha_t \, h_t(x) \geq \frac{1}{2}\sum_{t=1}^{T} \alpha_t \\ -1 & \text{otherwise} \end{cases}}
$$

- 即所有 weak classifier 的**加权投票**，超过权重总和一半 → positive，否则 → negative。
- 若 $h_t(x) \in \{0, 1\}$（而非 $\{-1, +1\}$），则判据为 $\frac{\sum \alpha_t h_t(x)}{\sum \alpha_t}$ 与 $\frac{1}{2}$ 比较（归一化加权平均与 0.5 比）。

#### 3.4 ⭐ 权重更新的直观理解（3 轮可视化示例）

转写中老师用 2D 可视化讲解了 3 轮 AdaBoost 的过程（11 个 training sample，positive "+" / negative "−"）：

| 轮次 | 权重状态 | 选 feature 行为 | 分错样本处理 |
|---|---|---|---|
| **Round 1** | 均匀权重（所有样本等高） | 选全局 error rate 最低的 feature | 2 个 negative 样本被分错 → 权重增大 |
| **Round 2** | 分错样本权重高 | 不选与 Round 1 相似的 feature（分错高权重样本会产生大 error rate）→ 选能修正 Round 1 错误的 feature | 另一组样本被分错 → 权重增大 |
| **Round 3** | 被前两轮都分错的样本权重最高 | 选能分对高权重样本的 feature | 3 个 feature 组合后形成分段分类边界 → 100% 正确 |

- 关键：若无权重更新，Round 2 会选与 Round 1 相似的 feature（因为全局 error rate 最低），组合后 accuracy 不提升。权重更新使 Round 2 **被迫**关注 Round 1 分错的样本。

### 4. ⭐ Overfitting 风险：Feature 数量的权衡

- 增加 feature 数量 $T$ → training data 上 error rate 可降至 0（甚至 100% accuracy）。
- ⚠️ 但 **training accuracy ≠ test accuracy**：feature 过多 → **overfitting**，对未知数据 generalization 下降。
- 选 feature 的目的是用于**未知数据**（test data / future data），而非追求 training data 上的 100%。
- 需选择适当数量的 feature，平衡 accuracy 与 generalization。

### 5. ⭐ Cascade Classifier（级联分类器）

#### 5.1 动机：利用检测问题的类别不平衡

- Object detection（如 face detection）用 sliding window 扫描整幅图像：
  - 10,000 个窗口中可能只有 ~10 个是 face，9,990 个是 non-face → **极度类别不平衡**。
- 串行使用全部 ~200 个 feature 分类每个窗口 → 仍不够快，无法 real-time。

#### 5.2 Cascade 思路

- **不一次性用全部 feature**，而是 feature **逐级**使用：
  - **Stage 1**：只用 1 个（或少数几个）feature 做初步分类。设置 threshold 使**所有 face 必定正确分类**（保证不漏检），同时大量 non-face 被快速拒绝。
    - 10,000 个窗口中 ~9,000 个在此阶段被判定为 non-face → 立即结束。
  - **Stage 2**：只有通过 Stage 1 的窗口（少量）进入下一级，用更多 feature 进一步分类。
  - **Stage 3, ...**：依此类推，只有极少数"疑似 face"的窗口走完全部 stage。

| 阶段 | 通过窗口比例 | 累计 feature 计算量 |
|---|---|---|
| Stage 1（1 feature） | ~90% 被拒绝 → ~10% 通过 | 极低 |
| Stage 2（少量 feature） | 大部分通过者被拒绝 | 低 |
| Stage T（全部 feature） | 极少窗口到达 | 少数窗口算全部 feature |

- ⭐ 绝大多数窗口在早期 stage 被快速拒绝 → 总体检测速度极快。
- 只有极少数"疑似 face"窗口需走完全部 stage。
- 利用 detection 问题的 **unbalanced** 性质（background 远多于 object）→ cascade 是自然加速方案。

#### 5.3 Viola-Jones 的完整 pipeline

| 组件 | 作用 |
|---|---|
| **Haar-like feature + Integral image** | 快速 feature 计算（任意矩形 3 次加减法） |
| **AdaBoost feature selection** | 从 ~180,000 feature 中选 ~100 个互补 feature |
| **Cascade classifier** | 逐级拒绝 non-face，极少量窗口走完全部 feature → real-time |

- Viola-Jones 是**第一个 real-time face detection 系统**（深度学习之前，甚至早于 neural network 在 CV 中的广泛应用）。
- 曾被各大公司广泛采用，OpenCV 中仍可调用。
- 虽然现已被 deep learning 超越，但作为 traditional CV 的经典方法，其 feature selection + cascade 思想仍有重要意义。

### 6. Weak Learner vs Strong Learner 对比

| 属性 | Weak Learner | Strong Learner |
|---|---|---|
| 使用 feature 数 | 1 个 | $T$ 个（如 ~100） |
| Error rate | 略低于 0.5（仅比随机猜好一点） | 可极小 |
| 结构 | 1-D threshold classifier | 加权投票组合 |
| 角色 | AdaBoost 每轮选一个 | 最终输出 |
| 构建方式 | 逐轮选择 + 权重更新 | $\sum \alpha_t h_t(x)$ 加权组合 |

### 7. ⭐ 本周考点速查

| 考点 | 要点 | 节号 |
|---|---|---|
| **feature extraction vs selection** | extraction 组合全部输入；selection 选子集；后者预测更快 | §1 |
| **boosting 思想** | 组合 weak learner → strong learner；weak classifier = 1 feature | §2.1 |
| **compensating feature** | 所选 feature 互补，不重复；非各自最优 | §2.2 |
| **联合搜索不可行** | 100 feature 从 10,000 选 ≈ 10,000¹⁰⁰ → 逐个选 | §2.3 |
| **⭐⭐ AdaBoost 权重更新公式** | $w_{t+1}(i) \propto w_t(i)\exp(-\alpha_t y_i h_t(x_i))$；分错↑分对↓ | §3.3 |
| **⭐⭐ $\alpha_t$ 公式** | $\alpha_t = \frac{1}{2}\ln\frac{1-\varepsilon_t}{\varepsilon_t}$；$\varepsilon \to 0$ 则 $\alpha \to \infty$ | §3.3 |
| **strong classifier 判据** | $\sum \alpha_t h_t(x)$ 与 $\frac{1}{2}\sum\alpha_t$ 比较 | §3.3 |
| **权重更新直观** | 分错样本权重↑ → 下一轮被迫关注 | §3.4 |
| **overfitting** | feature 过多 → training 100% 但 test 下降 | §4 |
| **⭐ cascade classifier** | 逐级拒绝 non-face，利用类别不平衡加速 | §5 |
| **cascade 保证** | Stage 1 设 threshold 保证 face 不漏检 | §5.2 |
| **Viola-Jones 三组件** | Haar-like + integral image + AdaBoost + cascade | §5.3 |

### 8. 本周要点小结

- **AdaBoost** 是 ensemble learning 的经典 boosting 方法，在 Viola-Jones 中用于 feature selection：从 ~180,000 个 Haar-like feature 中逐轮选出 ~100 个互补 feature。
- **核心机制**：每轮选当前权重下加权 error rate 最低的 feature → 计算 classifier 权重 $\alpha_t$ → 更新 sample 权重（分错的样本权重增大，分对的减小）→ 迫使下一轮选能修正前序错误的 feature。
- **Strong classifier** = 所选 weak classifier 的加权投票，权重 $\alpha_t$ 由 error rate 决定（error rate 越小 → $\alpha_t$ 越大 → 该 classifier 话语权越大）。
- **Overfitting 警告**：feature 数量过多会导致 training accuracy = 100% 但 test accuracy 下降，需适量。
- **Cascade classifier** 利用 detection 问题的类别不平衡（non-face 远多于 face），逐级用少量 feature 快速拒绝多数 non-face 窗口，只有极少数"疑似 face"窗口走完全部 feature → real-time 检测。
- **Viola-Jones** = Haar-like feature + integral image + AdaBoost + cascade，是深度学习前最经典的 real-time face detection 方法。

### 9. Quiz 1 考务信息（本周课堂）

- **Quiz 1**：25 题，30 分钟，占 10%。通过 NTULearn 进入，老师现场给 password。
- 不使用 lockdown browser，但**严禁打开其他程序**（10 个 invigilator 监考，违规记零分）。
- 只能开 NTULearn；**21:00 前不得离开教室**。
- 题目随机推送（每次只看到 1 题，相邻同学题目不同；选择题选项也随机排列）。
- 可多次 attempt，但**每次从头开始**，且只记最后一次成绩 → 建议只做一次。
- 计分：最终只看到 letter grade（不知道 raw score）；及格线 40%；75% 对应 A-（GPA 4.5）；若最高分 < 100% 会做 normalization。

### 10. 下一周预告

转写末尾老师明确说明：**recess week 后还有两周课**，内容为：
1. **Traditional neural network（MLP，多层感知机）**
2. **Convolutional Neural Network（CNN）**——如何 revolutionize machine learning；CNN 发明者 Professor Hinton 因此获 Nobel Prize（待课件确认具体奖项表述）。
3. 之后再讲 **Transformer**——聚焦 transformer 解决了什么 limitation、为何现代大模型（GPT 等）都基于 transformer。

> ⚠️ 由于本周是 Quiz 1 + recess week 前，下周（recess week 后）将进入 neural network / deep learning 部分。具体从 MLP 还是 CNN 开始、详细进度待课件确认。

## Week 8 — Topic 9：Neural Networks and Deep Machine Learning（MLP → CNN 主线 + Transformer 预告）

> **本周主线**（转写开场原话）："This week we will start neural networks... we will start from the traditional neural networks MLP, to the revolution of the machine learning, it is a CNN convolutional neural network, and finally go to the foundations of the current AI system, the large model AI system, the Transformer."
> 即 **三代神经网络**：① MLP（传统 neural network）→ ② CNN（deep learning 的 revolution）→ ③ Transformer（当前 large model / ChatGPT 的基础）。
> ⚠️ 本周课堂**实际只讲到 CNN 为止**（转写末句：*"after next week, I will first [cover] further development of the CNN and then based on that, further go to the current state of the art module of the AI model, it is a Transformer. That's all for today."*）。**Transformer 属于 Topic 10 / 下一周**，本笔记 §12 依据 PDF Topic 10 幻灯片 + 老师本周的口头预告整理，并已明确标注。

> **权威来源说明**：本周官方讲义为 `EE6222_lecturenote1to9.pdf` **第 263–341 页**（**Topic 9** "Neural Networks and Deep Machine Learning: from MLP to CNN" = 第 263–317 页；**Topic 10** "Deep Learning: from CNN to Transformer" = 第 318–341 页）。转写 `week8.txt` 是截至目前**噪声最严重**的一周（"neural" 几乎每次都被错拼），以下内容一律以 PDF 的公式与结构为准。本周典型 ASR 错拼对照（⚠️ **本周新特例**：`nel / nail / nay / nes / neler / yer / mayer / ayer / Myer` 在本周指 **layer（层）**，而非 Week 2–3 中的 color）：

| 转写噪声 | 正确术语 |
|---|---|
| near / neon / neo / new network、ner rate work、neontwork、nay | **neural network** |
| nel / nail / nay / nes / neler / yer / mayer / Mayor / Myer / ayer / el | **layer**（本周特例） |
| arg model AI system | **large model**（大模型） |
| fed / fit forward / ft forward | **feedforward** |
| wed / waged / wet / weak / which sum | **weighted sum** |
| tris / triso / tic / tre | **threshold** $\theta$ |
| choice（"a network must have a choice... must have a bias"） | **bias / threshold** |
| syncod / sycod / schmit / mot / mode function | **sigmoid** |
| redo / renew / red / anar / n function | **ReLU** |
| nose / north / moss function | **loss function**（损失函数） |
| arrow / er / ro / ero / aro / ao | **error** |
| change / chain zoo / zoos | **chain rule**（链式法则） |
| greatly / grid / great / gent / cog decent | **gradient descent** |
| ata / ta / Data（学习率系数） | **$\eta$（eta，learning rate）** |
| back publication / by prorogation / bipgion / bprolgation | **backpropagation** |
| pulling / p | **pooling** |
| fit / field / fetal window、fit size | **filter**（卷积核） |
| china / china dimension | **channel**（通道） |
| special size / special index | **spatial**（空间） |
| phase recognition | **face recognition** |
| taste data / twining / trending / turning data | **test data / training data** |
| crotic / atic / aquatic / logic function | **quadratic function** |
| reganization / regnation / reorganization | **regularization** |
| overfating / overfting / over fading / al fitting | **overfitting** |
| under faking / undating | **underfitting** |
| H O transection on new networks | **IEEE Transactions on Neural Networks** |
| CPA / IW PAM | **CVPR / TPAMI** |
| image, minions of the real images | **ImageNet / 数百万张真实图像** |
| CN / C / the N / the s | **CNN** |
| L P / ALP / MP / Mop | **MLP** |
| 1 bar / one by one convolution | **1×1 convolution** |
| CAT GPT / chat GPT | **ChatGPT** |

### 1. 三代神经网络的地位（本周要回答的问题）

| 代际 | 代表 | 关键问题 | 本课结论 |
|---|---|---|---|
| 第 1 代 | **MLP**（multilayer perceptron，多层感知机） | 能学任意非线性映射，但**只对 training data 有效** → overfitting | 传统 neural network，理论上万能，实践中崩 |
| 第 2 代 | **CNN**（convolutional neural network） | 为什么 CNN 比 MLP 表现好？ | 不是"local structure"，而是 **parameter sharing = 强 regularization**（§10） |
| 第 3 代 | **Transformer** | 为什么 Transformer 又超过 CNN？ | **attention** 用 test input 生成权重，捕捉 global information（§12 预告） |

- 老师反复强调的**唯一主线**：machine learning 的成败在于**学到 general rule，而非 overfit 到 training data 的 specific details**。三代网络的演进，本质上是**逐步解决 overfitting 问题**的历史。
- ⚠️ 老师的核心观点（贯穿全周、也是他自己的研究贡献）：很多人认为 "CNN 优于 MLP 是因为 convolution 只捕捉 local information，而图像有 local structure"——**老师明确说"this is not the reason"**。真正的理由是 **参数共享带来的强正则化**（详见 §10）。

### 2. ⭐ Neuron Model（神经元模型）

#### 2.1 结构：weighted sum + threshold + activation

一个 neuron（神经元）做两件事，顺序固定：

1. **weighted sum（加权求和）**：把输入数据 $\mathbf{x}$ 的每个分量乘以对应 weight，再求和。
2. **减去 threshold**（或加 bias），再送入 **activation function（激活函数）** 得输出。

⚠️ 老师特别强调的两点：

- **weighted sum 是神经网络里唯一"可学习"的部分**。"In this weighted sum, this weight is a network parameter. It is learnable, it is learned from the training data. **Machine learning or training a neural network is just to update these weights.**"
- **activation function 是固定的、不可学习的（fixed, non-learnable）**，只是一个简单的非线性函数。
- **网络必须有 bias/threshold**："A network must have a bias. Without the bias, the network cannot work."即使公式里看不出来，也永远不要忘记。

#### 2.2 数学表达（scalar 形式）

$$
u_k = \sum_{j=1}^{p} w_{kj} x_j, \qquad y_k = f(u_k - \theta_k)
$$

| 符号 | 含义 |
|---|---|
| $x_1, x_2, \ldots, x_p$ | 输入信号（input signals） |
| $w_{k1}, w_{k2}, \ldots, w_{kp}$ | neuron $k$ 的 synaptic weights（突触权重） |
| $u_k$ | linear combiner output（加权和） |
| $\theta_k$ | threshold（阈值，external parameter） |
| $f(\cdot)$ | activation function |
| $y_k$ | neuron $k$ 的输出 |

#### 2.3 把 threshold 吸收进输入（bias 技巧）

令**额外输入** $x_0 = 1$，其权重取 $w_{k0} = -\theta_k$，则上式可写成"纯 weighted sum"：

$$
v_k = \sum_{j=0}^{p} w_{kj} x_j, \qquad y_k = f(v_k)
$$

- 求和从 $j=1$ 变成 $j=0$，多出来的 $x_0=1$ 项就是 **bias 项**（$-\theta_k$）。
- ⚠️ 老师提醒："$j$ 从 1 到 $p$ 写，**不代表没有 threshold**"——只是被吸收了。这一技巧后面在 **least square**（§5.2，要求 $\mathbf{x}$ 含一个常数分量 1）与 **CNN 的 bias $b_k$**（§9）中反复出现。

### 3. ⭐ Activation Functions（激活函数）对比

PDF（第 268–269 页）给出四类 activation function：

| 名称 | 表达式 | 特点 | 使用时期 |
|---|---|---|---|
| **Binary function**（阶跃） | $f(v)=1\ (v\ge 0),\ 0\ (v<0)$ | 就是 step function，0/1 突变，不可导 | 早期 NN |
| **Piecewise-linear function** | $f(v)=1\ (v\ge 0.5);\ v\ (-0.5<v<0.5);\ 0\ (v\le -0.5)$ | 在 0 附近加了一段**过渡区**（transition region），让输出从 0 逐渐升到 1 而不是突然跳变 | 早期 NN |
| **Sigmoid function** | $f(v)=\dfrac{1}{1+\exp(-av)}$ | **光滑、处处可导**（smooth, differentiable everywhere），且 $0\le f\le 1$ | **CNN 之前的 MLP 主力** |
| **ReLU function** | $f(v)=\max(0,v)=\begin{cases}v & v\ge 0\\ 0 & v<0\end{cases}$ | 正半轴是**恒等（线性）**，负半轴输出 0；计算最简单 | **CNN / Transformer 时代** |

- 为什么 sigmoid 是 MLP 的绝配（老师原话）："This function is very nice. It is smooth and can be differentiable everywhere. **Everywhere we can compute its differentiation.**"——backpropagation 需要对 $f$ 求导（§6.4），sigmoid 的导数可以用**输出本身**表示，计算极省。
- 为什么 CNN/Transformer 改用 ReLU：深层网络要**从最后一层把 error 逐层 back-propagate 回第一层**；若用复杂的非线性函数，梯度会**越来越弱、几乎变 0**（vanishing gradient）。ReLU 是最简单的非线性函数（正半轴近似线性），因此"facilitates the deep layers' learning"（PDF 原话）。详见 §10.7。
- ⚠️ 现代网络里 "almost all NN and Transformer use the ReLU function"（老师原话）。

### 4. ⭐ MLP 的三种数学表达（scalar / vector / matrix）

老师用三种等价写法描述网络，**用哪种取决于后续推导哪种更方便**。

#### 4.1 Scalar 形式（两层网络）

**第一层（hidden layer，隐含层）**，$j=1,\ldots,d$：

$$
z_j = f\!\left(\sum_{i=1}^{n} w_{ji} x_i\right) = f\!\left(\mathbf{w}_j^{T}\mathbf{x}\right)
$$

**第二层（output layer）**，$k=1,\ldots,c$：

$$
y_k = f\!\left(\sum_{j=1}^{d} v_{kj} z_j\right) = f\!\left(\mathbf{v}_k^{T}\mathbf{z}\right) = f\!\left(\sum_{j=1}^{d} v_{kj}\, f\!\left(\sum_{i=1}^{n} w_{ji} x_i\right)\right)
$$

#### 4.2 Vector / Matrix 形式

$$
\mathbf{z} = f(\mathbf{W}^{T}\mathbf{x}), \qquad \mathbf{y} = f(\mathbf{V}^{T}\mathbf{z}) = f\!\left(\mathbf{V}^{T} f(\mathbf{W}^{T}\mathbf{x})\right)
$$

记号（PDF 第 270 页）：

- $\mathbf{x} = (x_1,\ldots,x_n)^{T}$：input vector（列向量）
- $\mathbf{z} = (z_1,\ldots,z_d)^{T}$：hidden layer 输出
- $\mathbf{y} = (y_1,\ldots,y_c)^{T}$：network 输出
- $\mathbf{t} = (t_1,\ldots,t_c)^{T}$：**target output / ground truth**（监督训练必须有）
- $\mathbf{w}_j$ = 第 $j$ 个隐含神经元的 weight **vector**；把 $d$ 个 $\mathbf{w}_j$ 并排 → 矩阵 $\mathbf{W} = [\mathbf{w}_1\ \mathbf{w}_2\ \cdots\ \mathbf{w}_d]$（**一列 = 一个神经元的权重**）
- 同理 $\mathbf{V} = [\mathbf{v}_1\ \mathbf{v}_2\ \cdots\ \mathbf{v}_c]$

#### 4.3 ⭐⭐ 为什么 activation function 必须非线性

设 $f$ 是线性函数 $f(r)=r$，则

$$
\mathbf{y} = f\!\left(\mathbf{V}^{T} f(\mathbf{W}^{T}\mathbf{x})\right) = \mathbf{V}^{T}\mathbf{W}^{T}\mathbf{x} = (\mathbf{W}\mathbf{V})^{T}\mathbf{x} = \mathbf{U}^{T}\mathbf{x}, \qquad \mathbf{U} = \mathbf{W}\mathbf{V}
$$

- ⚠️ **两个 layer 的权重矩阵可以合并成一个** $\mathbf{U}$ → **多层网络完全等价于单层网络**（"Multilayer network will be just the same as a single layer network"）。
- 结论：**hidden neuron 的 activation function 必须是非线性函数**，否则层数没有意义。这是"为什么要有 activation function"的根本答案。
- 补充（老师口述）：**单层网络连 activation function 都不需要**——即使加了非线性 $f$，$f(\mathbf{w}^T\mathbf{x})$ 也只是"标量函数的非线性"，输入输出关系仍是线性的，仍只能形成**线性决策边界**。**非线性的作用是"separate two different layers"**，让多层不等价于单层。

### 5. ⭐ 单层网络的学习：MSE → 闭式解 → Gradient Descent

#### 5.1 Error 与 loss function

单层、单输出：$y = \mathbf{w}^{T}\mathbf{x}$，则

$$
e = t - y = t - \mathbf{w}^{T}\mathbf{x}
$$

**Mean square error（均方误差）作为 loss function**（老师称"loss function"是目前最流行的叫法，另有 objective/cost function 等名称）：

$$
J(\mathbf{w}) = E\{e^{2}\} = E\{(t-y)^{2}\} = E\{(t-\mathbf{w}^{T}\mathbf{x})^{2}\}
= \overline{t^{2}} - 2\mathbf{w}^{T}E\{\mathbf{x}t\} + \mathbf{w}^{T}E\{\mathbf{x}\mathbf{x}^{T}\}\mathbf{w}
$$

- 为什么要平方：error 有正有负，**平方后恒非负**，最小值 0 才有意义（"then the smallest error is zero"）。
- 为什么取 $E\{\cdot\}$：期望在训练中就是**对所有 training data 求平均**。
- ⭐ $J(\mathbf{w})$ 是 $\mathbf{w}$ 的**二次函数（quadratic function，二阶）→ 只有一个 minimum point**（1D 情形是抛物线，最小值在 $w=t/x$）。因此可以**直接求导置零**。

#### 5.2 ⭐ 闭式解：Least Square Method

$$
\frac{\partial E\{e^{2}\}}{\partial \mathbf{w}} = 0 \;\Longrightarrow\; E\{\mathbf{x}\mathbf{x}^{T}\}\mathbf{w} = E\{\mathbf{x}t\}
$$

用样本平均近似期望（$q$ 个样本）：

$$
E\{\mathbf{x}\mathbf{x}^{T}\} \cong \frac{1}{q}\sum_{i=1}^{q}\mathbf{x}_i\mathbf{x}_i^{T}, \qquad E\{\mathbf{x}t\} \cong \frac{1}{q}\sum_{i=1}^{q}\mathbf{x}_i t_i
$$

把所有样本排成数据矩阵 $\mathbf{X} = [\mathbf{x}_1\ \mathbf{x}_2\ \cdots\ \mathbf{x}_q]$，$\mathbf{t} = [t_1\ t_2\ \cdots\ t_q]$，则 $q\,E\{\mathbf{x}\mathbf{x}^{T}\} \cong \mathbf{X}\mathbf{X}^{T}$，$q\,E\{\mathbf{x}t\} \cong \mathbf{X}\mathbf{t}^{T}$，于是

$$
\boxed{\;\mathbf{w} = (\mathbf{X}\mathbf{X}^{T})^{-1}\mathbf{X}\mathbf{t}^{T}\;}
$$

- 这就是 **least square method（最小二乘法）**。
- ⚠️ 需要求**逆矩阵** $(\mathbf{X}\mathbf{X}^{T})^{-1}$，形式上与 **Mahalanobis distance** 中的 $\boldsymbol{\Sigma}^{-1}$ 极为相似：若 $\mathbf{X}$ 换成"减去均值的数据矩阵"，$\mathbf{X}\mathbf{X}^{T}$ 就是 covariance matrix。
- 老师提出的**思考题（他本人也未做的研究）**：这个 least square 解**乘上输入产生分类输出**的形式，与 **Mahalanobis distance classifier** 的解几乎一模一样。区别在于：Mahalanobis 的解在 "data 是 Gaussian PDF" 时才是最优；而 least square 解在**任意分布**下都最优（**但最优指的是"最小化 mean square error"，不是"最小化分类错误率"**）。两者最终结果可能非常接近，值得比较。
- ⚠️ 用此解做分类时：$\mathbf{x}$ 必须**含一个常数分量 1**（bias，§2.3）；两类时常用 target = $+1$ / $-1$，决策边界取输出为零处。

#### 5.3 ⭐ Gradient Descent（梯度下降）

$J(\mathbf{w})$ 单层时是二次的，但**多层非线性时没有解析解**（§6.1）。通用做法是迭代：

$$
\mathbf{w} \leftarrow \mathbf{w} + \Delta\mathbf{w}, \qquad \Delta\mathbf{w} = -\eta \nabla J(\mathbf{w})
$$

其中

$$
\nabla J(\mathbf{w}) = \frac{\partial E\{(t-\mathbf{w}^{T}\mathbf{x})^{2}\}}{\partial \mathbf{w}}
= -2E\{(t-\mathbf{w}^{T}\mathbf{x})\mathbf{x}\} = -2E\{e\mathbf{x}\} \cong -2e_i\mathbf{x}_i
$$

- 梯度指向 loss **增大**最快的方向，所以沿**反方向**更新（$-\eta$）能让 loss 下降。老师原话："gradient will point out the direction the loss function will increase... modify the W in the opposite direction of the gradient."
- 用**单个样本**近似期望 $E\{\cdot\}$，得到经典的 **LMS / delta rule**：

$$
\boxed{\;\mathbf{w} \leftarrow \mathbf{w} + \eta\, e_i \mathbf{x}_i = \mathbf{w} + \eta\,(t_i - y_i)\mathbf{x}_i\;}
$$

  迭代下去会收敛到与解析解 $\mathbf{w}=(\mathbf{X}\mathbf{X}^{T})^{-1}\mathbf{X}\mathbf{t}^{T}$ **相同的结果**。

#### 5.4 ⭐ Learning Rate $\eta$ 的取舍

| $\eta$ | 收敛速度 | 结果 |
|---|---|---|
| **大** | 快 | 靠近 minimum 时会**来回振荡（oscillate）**，收敛到误差较大的值，无法非常接近 minimum |
| **小** | 慢 | 需要**很多次迭代**，但能收敛得非常接近 minimum |

- 常用做法（现代 deep learning 仍在用）：**先用较大 learning rate，若干轮后改小**（learning rate schedule）。
- 老师自述：他**硕士期间**就研究过如何计算/选取 adaptive signal processing 中的**最优 learning rate / step size**——那时还没有 neural network 和 deep learning，但"参数从数据中学习"的思想已经存在，且与 gradient descent 完全同构。这是他"早期研究"的起点。

#### 5.5 ⭐ Batch 的三种极端：SGD / Mini-batch / Full-batch

期望 $E\{e\mathbf{x}\}$ 如何用样本实现，对应三种做法：

| 方式 | 更新频率 | 说明 |
|---|---|---|
| **单样本（SGD）** | 每个样本更新一次 | 一个极端：用 1 个 sample 就算 gradient 并更新 |
| **Mini-batch** | 每个 batch 更新一次 | **中间方案**：把 training data 分成若干 batch，batch 内求平均后更新一次 |
| **Full-batch** | 每轮（epoch）更新一次 | 另一个极端：在**全部** training data 上求平均后更新一次 |

- ⚠️ 老师强调："**the size of the batch is very important to make the learning more effective**"——这就是今天 deep learning 里 batch size 这个超参的由来。

#### 5.6 Learning Curve 与线性决策边界

- 把 loss 对 iteration 数作图 → **learning curve（学习曲线）**。
- **training data 上的 loss 曲线必然单调下降**（因为更新规则就是为减小 loss 设计的）；但 **test data 上的 loss 不一定下降，可能上升**——因为 test data 从不参与训练，网络"学不到"它。两条曲线的**差距（gap）**就是问题所在。
- 单层网络 → 输入输出是**线性关系** → 分类时只能形成**线性决策边界**：

$$
\mathbf{w}^{T}\mathbf{x} = 0
$$

  即一条直线 / 一个平面 / 一个 hyperplane。两类 target 取 $\pm 1$ 时，边界就是输出等于 0 的位置。**这正是必须研究多层网络的原因**。

### 6. ⭐⭐ Backpropagation（反向传播，本周最核心）

#### 6.1 动机：为什么必须有 backprop

两层网络的 loss：

$$
J(\mathbf{w},\mathbf{v}) = E\{e^{2}\} = E\{\|\mathbf{t}-\mathbf{y}\|^{2}\} = E\!\left\{\left\|\mathbf{t} - f\!\left(\mathbf{V}^{T} f(\mathbf{W}^{T}\mathbf{x})\right)\right\|^{2}\right\}
$$

- 令 $\nabla J(\mathbf{w},\mathbf{v}) = 0$ —— ⚠️ **由于非线性函数 $f$ 的存在，这个方程组没有解析解（no analytical solution）**，无法像单层那样解出 $\mathbf{w}, \mathbf{v}$ 的显式表达式。
- 这就是 1940s–1970s（**30 多年**）神经网络研究**只能停留在单层**的原因："people just stop here. For more than 20, 30 years, people research on the neural network just on the single layer."
- 突破点（老师说他当年觉得很惊讶，因为解法"并不难"）：**既然 gradient 可算，就不必解方程**。只要能得到 $\nabla J$ 的**数学表达式**（哪怕解不出 $=0$），代入数值就能迭代更新：

$$
\mathbf{w} \leftarrow \mathbf{w} - \eta\nabla J(\mathbf{w}), \qquad \mathbf{v} \leftarrow \mathbf{v} - \eta\nabla J(\mathbf{v})
$$

#### 6.2 ⭐ 链式法则推导（scalar 形式）

记 $\mathbf{z} = f(\mathbf{q})$，$\mathbf{y} = f(\mathbf{q}_k)$ 式的中间量：

- $q_j = \sum_i w_{ji} x_i$：隐含神经元 $j$ 的 weighted sum，$z_j = f(q_j)$
- $q_k = \sum_j v_{kj} z_j$：输出神经元 $k$ 的 weighted sum，$y_k = f(q_k)$

取带 $\frac{1}{2}$ 的平方误差（**取 $1/2$ 只是为了求导后系数变简洁**，老师原话）：

$$
J(\mathbf{w},\mathbf{v}) = \frac{1}{2}\sum_{k=1}^{c}(t_k - y_k)^{2}
= \frac{1}{2}\sum_{k=1}^{c}\left(t_k - f(q_k)\right)^{2}
= \frac{1}{2}\sum_{k=1}^{c}\left(t_k - f\!\left(\sum_{j=1}^{d} v_{kj} z_j\right)\right)^{2}
$$

**① 对输出层权重 $v_{kj}$ 求导**（chain rule 一次）：

$$
\boxed{\;\frac{\partial J(\mathbf{w},\mathbf{v})}{\partial v_{kj}} = \frac{\partial J}{\partial q_k}\cdot\frac{\partial q_k}{\partial v_{kj}} = -(t_k - y_k)\,f'(q_k)\,z_j\;}
$$

**② 对隐含层权重 $w_{ji}$ 求导**（chain rule 三次，逐层"回传"）：

$$
\boxed{\;\frac{\partial J(\mathbf{w},\mathbf{v})}{\partial w_{ji}} = \frac{\partial J}{\partial z_j}\cdot\frac{\partial z_j}{\partial q_j}\cdot\frac{\partial q_j}{\partial w_{ji}} = -\sum_{k=1}^{c}(t_k - y_k)\,f'(q_k)\,v_{kj}\,f'(q_j)\,x_i\;}
$$

⚠️ **这两个式子的关键差别**：$\partial J/\partial w_{ji}$ 中出现了 $\sum_k (t_k-y_k)f'(q_k)v_{kj}$ —— 正是**输出层的误差项**经过权重 $v_{kj}$ 传回第 $j$ 个隐含神经元的结果。也就是说：

- 输出层：**error 乘上该层输入的 derivative**
- 隐含层：**把输出层的 error 沿权重"反向"传回来**，再乘本层 activation 的 derivative

⛔ 这正是算法得名 **back-propagation（误差反向传播）** 的原因。

#### 6.3 更新公式（最终形式）

$$
v_{kj} \leftarrow v_{kj} - \eta\frac{\partial J}{\partial v_{kj}}
= v_{kj} + \eta\,(t_k - y_k)\,f'(q_k)\,z_j
$$

$$
w_{ji} \leftarrow w_{ji} - \eta\frac{\partial J}{\partial w_{ji}}
= w_{ji} + \eta\sum_{k=1}^{c} v_{kj}\,(t_k - y_k)\,f'(q_k)\,f'(q_j)\,x_i
$$

- 注意符号：$\partial J/\partial v_{kj}$ 带负号，所以 $-\eta\frac{\partial J}{\partial v_{kj}}$ 变成 **$+\eta$**。
- 直觉：weight 的更新量 ∝ **误差 × 该 weight 对应输入信号 × activation 斜率**。

#### 6.4 ⭐ Sigmoid 的导数（为什么 backprop 选 sigmoid）

$$
f(q) = \frac{1}{1+\exp(-aq)}, \qquad 0 \le f(q) \le 1
$$

$$
f'(q) = \frac{a\exp(-aq)}{\left[1+\exp(-aq)\right]^{2}} = a\,f(q)\left[1 - f(q)\right]
$$

- ⚠️ **极其重要的计算优势**：$f'(q)$ 可以用**已经算出的输出 $f(q)$ 直接表示**，不必重新计算 exp。老师原话："This is why this mode function is very nice. It is smooth, differentiable everywhere, and **we can just use the output of this activation function to get its differentiation.**"
- sigmoid 的导数最大值只有 $a/4$（$a=1$ 时 = 0.25）→ 这正是深层网络 **vanishing gradient** 的根源（§10.7）。

#### 6.5 ⭐ Backpropagation 训练流程（PDF 第 288–290 页，5 步）

给定 $n$ 个 training sample $\{\mathbf{x}(1),\mathbf{t}(1)\},\ldots,\{\mathbf{x}(n),\mathbf{t}(n)\}$：

| 步骤 | 名称 | 内容 |
|---|---|---|
| **(1)** | **Initialization** | 无先验信息时，weight 取**均匀分布**随机值（mean = 0）；**方差要选得让 activation signal 的标准差落在 sigmoid 的"线性区与饱和区交界处"** |
| **(2)** | **Presentation** | 向网络呈现一个 **epoch（一轮）** 的 training samples |
| **(3)** | **Forward computation** | 把 $\mathbf{x}(i)$ 送入输入层，**逐层前向**计算各神经元的 activation signal 与 function signal |
| **(4)** | **Backward computation** | 计算 local gradient，**逐层反向**调整 synaptic weights |
| **(5)** | **Iteration** | 呈现新的 epoch，重复 (3)(4)，直到满足 **stopping criterion** |

- ⚠️ **每个 epoch 都要重新随机打乱样本顺序**（"the order of presentation of training samples should be randomized from epoch to epoch"）。
- **Stopping criterion**：迭代次数上限，或 **average error 的变化率足够小**。
- 两种信号（PDF 第 287 页）：forward 传的是 input/function signal，backward 传的是 error signal。**训练 = forward + backward 交替；预测 = 只做 forward。**
- ⚠️ 老师的历史评价：backprop **数学上只是链式法则**（"We just use the chain rule, we don't need specific skills"），但意义重大——"even now the deep learning and the transformer also use this backpropagation"，是 **Hinton 获 Nobel Prize 的贡献之一**（⚠️ 老师原话：主要贡献是 convolutional network，backpropagation 也被诺奖提及；Nobel Prize 于 2024 年颁给 University of Toronto 的 Hinton，具体奖项表述以官方为准）。

### 7. ⭐ 训练的两大根本困难

#### 7.1 Problem of Local Minima（→ underfitting）

- loss 作为 network parameter 的函数是**高度非线性（highly nonlinear）**的，且参数多达数百上千个 → loss surface 极其复杂。
- gradient descent **只依赖局部信息**，只能沿梯度下降 → 一旦到达某个 **local minimum**，gradient = 0，**无法再更新**（它不接受 loss 先升后降的策略）。
- 从不同的初始点出发，会收敛到**不同的 local minimum** → 训练结果，理论上有 global minimum（可让 training error → 0）但**不保证能找到**。
- 后果：训练停在某个 loss 值远高于目标的点 → **underfitting（欠拟合）**：网络没能学到 training data 中的规律。
- ⚠️ 老师的博士论文工作：提出一种**构造网络结构 + 初始化参数**的方法以保证得到解 —— *X.D. Jiang and A. Kam, "Constructing and Training Feed-Forward Neural Networks for Pattern Classification," Pattern Recognition, vol. 36, no. 4, pp. 853–867, April 2003*（PDF 第 290、299 页引用）。

#### 7.2 ⭐⭐ Overfitting（比 local minima 更严重，老师称"the most important problem in all machine learning"）

- 设定：machine learning 的目标是找到**未知的连续函数** $f$，使 $\mathbf{y} = f(\mathbf{x})$ 对**整个 population** $\mathbf{x}\in\mathbb{R}^{n}$ 成立；但我们只有**有限的离散训练样本** $\{\mathbf{x}_i,\mathbf{y}_i\}$，只能求出近似 $\hat{f}$。

$$
\min_{\hat{f}} e^{2} = \min_{\hat{f}} \sum_{\forall i}\left\|\mathbf{y}_i - \hat{f}(\mathbf{x}_i)\right\|_{2}^{2} \;\Rightarrow\; 0
\quad\text{但只会得到}\quad \mathbf{y}_i = \hat{f}(\mathbf{x}_i)\ \text{（训练点）而非}\ \mathbf{y} = f(\mathbf{x})\ \text{（全体）}
$$

- ⚠️ 老师的**核心论断**："Compared to the continuous, uncountable infinite different values, a set of **finite discrete samples, whatever large in size, is always negligible**!"（有限样本相对连续无限总体，永远可以忽略不计）→ **overfitting / poor generalization 是 machine learning 的根本困难。**
- **典型案例：double spiral problem（双螺旋问题）**（PDF 第 299 页）：
  - 二维输入，两类样本（黑/白）各自形成一条螺旋，**两条螺旋完全重叠**（fully overlapped）→ 需要**高度非线性**的决策边界。
  - 线性分类边界 → 错误率最高约 **50%**（等于乱猜）。
  - **两层 MLP** 训练后 → **training data 上 100% 正确**，形成极复杂的非线性边界。
  - ⚠️ 但画出的 decision region 显示：边界**极度扭曲（wiggly/funding）**，某些训练点被"孤立地"包进正确的区域；**输入只要与该点略有不同，立刻分类错误**。
  - 用更多层（5 层）训练 → 边界几乎一样，仍然处处是 overfitting 的痕迹 —— **更多层并不能解决 overfitting**。
- ⚠️ 老师用这个例子说明："although the network is powerful in terms of machine learning — it can learn the training data perfectly — it cannot work for the [new] data. Sometimes just very slightly different from the training data."
- 历史代价（老师亲历的 research history）：正因为 overfitting，神经网络研究在 1990s–2000s 中期**跌入谷底**——"in that year, nobody cared about neural networks. Even top conferences such as **CVPR** and **TPAMI** would reject all submissions if your paper topic is neural network."

#### 7.3 ⭐ Regularization（正则化：解决 overfitting 的唯一思路）

⚠️ 老师的根本逻辑：**仅靠 machine learning 原理上无法解决 overfitting**（因为它就是从 training data 学）。唯一出路是**用 human knowledge 去限制/约束 $\hat{f}$**，这就是 **regularization**。PDF（第 300–301 页）给出三种做法：

| 做法 | 数学形式 | 说明 |
|---|---|---|
| **限制函数类** | $\min_{\hat{f}\in\Omega}\sum_{\forall i}\|\mathbf{y}_i - \hat{f}(\mathbf{x}_i)\|^{2}$ | 约束学到的函数只能是"简单的/经典的"一类函数，复杂度不超过某个程度 |
| **先降维再学习** | 先 reduce data 到低维，再在低维空间最小化 loss | 这就是 **dimensionality reduction（PCA/LDA）能提高 test accuracy 的原因**——它提供了一条克服 overfitting 的途径 |
| **加正则项** | $\min_{\hat{f}}\sum_{\forall i}\|\mathbf{y}_i-\hat{f}(\mathbf{x}_i)\|^{2} + \lambda\Phi(\hat{f})$ | 在 loss 中追加 regularization term，例如约束参数**稀疏（sparse）**→ sparse coding / sparse representation |

#### 7.4 Validation Set 与 Early Stopping

- 把 training data 划出一部分**不参与训练**，作为 **validation data**，用来"validate 训练后的 loss 值"。
- 训练在 **validation data 上 loss 最小处停止**，而不是在 training data 上 loss 最小处停止。
- ⚠️ 老师明确指出这**只能部分解决问题**："even if the network is trying to work well on the validation data, the test data is also different from the validation data. It cannot [completely] solve the problem of overfitting."

### 8. ⭐⭐ 神经网络发展史（老师亲历的研究曲线）

| 时期 | 状态 | 原因 |
|---|---|---|
| **1940s 起** | 研究起步（比 1950s 更早） | 但**只能做单层**——多层没有解法 |
| **1980s** | **backpropagation 出现** → 多层可训练 | 发现"两层 MLP 就能实现任意非线性关系" → 研究热情爆发；新期刊涌现：*IEEE Trans. on Neural Networks*、*Neural Computation* 等，大量 PhD 以此毕业（老师本人也是） |
| **1980s–1990s** | 第一个**高峰** | 人们相信神经网络无所不能 |
| **1990s → 2000s 中期** | **跌入极深的谷底（AI winter）** | ⚠️ 因为**只对 training data 有效**：真实数据的 variation 巨大，test 图像与训练集差异很大 → "people found the neural network is useless"；CVPR/TPAMI 直接拒掉 neural network 的投稿 |
| **2006 前后 → 2010s** | **CNN / deep learning 复兴** | 用**极大规模真实数据集**（如 ImageNet，数百万张真实图像）训练 CNN → 真实图像识别率从约 **60% 提升到 90% 以上** |
| **2010s → 现在** | Transformer → **large model（ChatGPT）** | 这次的推动力**主要来自工业界**（industry，因为能直接产生 revenue），而非大学学术界 |

- ⚠️ **DNN / CNN 是"第三代神经网络"**（PDF 第 295 页）。
- ⚠️ 老师对 "deep learning" 一词的**祛魅**：**"Deep learning does not mean the network can learn knowledge deep inside. Deep learning just means we have deep layers — many layers, a huge number of layers."**（现代 CNN 可达 100 层甚至数百层、上千层。）
- 深刻学习 = **progressive learning**（PDF 原话）：复杂的非线性 input-output relation 是**逐层、渐进**学出来的。

### 9. ⭐ CNN 的结构：Convolution + Pooling + ReLU

#### 9.1 CNN 与 MLP 的五大差异（PDF 第 303 页）

1. **Network architecture**（网络结构，二维排布，直接面向图像）
2. **Convolution**（卷积替代 weighted sum）
3. **Simple nonlinear activation function ReLU**（最简非线性激活）
4. **Pooling**（池化）
5. **Deep, large number of layers**（层数很多）

以 **VGG-Face CNN**（人脸识别网络）为例：

- 输入图像 → 用 **3×3 的 filter window** 卷积 → 输出多张 output image（**feature map**，也叫 channel）。
- 第一层用 **64 个不同的 filter → 生成 64 张 output image**（64 channels）。
- 卷积后接 **ReLU**，再接 **pooling layer**：以 2×2 窗口为例，4 个像素中只留 1 个、丢掉另外 3 个 → **空间尺寸长宽各减半，像素数只剩 1/4**。
- 反复 "convolution → ReLU → pooling" 堆叠后，最后得到一个 **spatial size 为 7×7、channel 数超过 500** 的 feature map。
- 这个 7×7×500 的 feature map 就是**最终特征**，用于分类/预测（识别输入图像是哪个人的人脸）。
- 演化规律：**空间尺寸（spatial size）不断减小，channel 数（number of feature maps）不断增大**。

⚠️ 老师对 pooling 的**个人观点**（与主流教材不同，且他明确说 "pooling does not make much role"）：

- pooling **只是减小 spatial size**，本身不提供什么能力；
- 如果 pooling 是 **sub-sampling（下采样）**型而非 **max pooling**，那么"在部分像素上算卷积"和"算完之后 pooling"是**等价的**——**去掉 pooling 层，效果差不多**；
- 真正的主角是 **convolution**。

#### 9.2 ⭐ Convolution 的数学定义（含 bias 与 channel 求和）

训练数据：输入 feature maps 空间尺寸 $P\times Q$、$C$ 个 channel，记为 $x_{i,j,k}$；输出 feature maps 空间尺寸 $P\times Q$、$D$ 个 channel，记为 $y_{i,j,k}$。则（PDF 第 304 页，以 3×3 filter 为例）：

$$
\boxed{\;y_{i,j,k} = \sum_{n=1}^{C}\ \sum_{m=-1}^{1}\ \sum_{l=-1}^{1} w_{l,m,n,k}\, x_{i-l,\, j-m,\, n} \;+\; b_k\;}
$$

$$
1\le i\le P,\quad 1\le j\le Q,\quad 1\le k\le D
$$

逐项解读（老师原话的整理）：

| 部分 | 含义 |
|---|---|
| $\sum_{l=-1}^{1}\sum_{m=-1}^{1}$ | **卷积本身**：以 $(i,j)$ 为中心的 3×3 邻域**空间加权求和**（$l,m$ 取 $-1,0,1$ 即 3×3；换成 $-\infty..\infty$ 就是传统卷积定义） |
| $\sum_{n=1}^{C}$ | ⚠️ **CNN 特有**：把 **所有输入 channel（输入图像）** 上同一 spatial position 的结果**再加总**——"convolution in CNN includes a bias term; along the channel dimension, all inputs of different channels are **fully connected**, same as MLP" |
| $w_{l,m,n,k}$ | 第 $k$ 个 filter 的权重（$n$ = 输入 channel 索引，$k$ = 输出 channel 索引） |
| $b_k$ | 每个输出 feature map（每个 filter）**一个 bias** |
| 下标 $k$ | 不同 filter → 不同输出 channel |

- ⚠️ 与图像处理课里的传统 convolution 的区别：传统卷积只对**单张图**做空间加权求和；CNN 的卷积**还必须在 channel 维上求和**（因为输入天然是多张图，RGB 就有 3 个 channel）。
- 老师提醒：PPT 上 $\sum_{m=-1}^{1}$ 的上下限有时显示成 $\pm 1$ 有时显示别的东西，是 PowerPoint 的显示 bug，"this sign is just here, same as this one"，不影响含义。

#### 9.3 ⭐ CNN vs MLP（1D 形式的严格对照）

这是本周**最关键的一段推导**——把 CNN 写成 MLP 的形式，两者差异一目了然（PDF 第 306–309 页）。

**MLP**：

$$
o_j = \sum_{\forall i} w_{ji}\,x_i = \mathbf{w}_j^{T}\mathbf{x}, \qquad \mathbf{o} = \mathbf{W}\mathbf{x}
$$

**CNN（1D 卷积）**：

$$
o_j = w_j * x_j = \sum_{\forall i} w_i\, x_{j-i} = \mathbf{w}^{T}\mathbf{x}_j = \mathbf{w}\mathbf{x}_j
$$

把 CNN 的每个输出 $o_j$ 也写成 MLP 的 $\mathbf{w}_j^{T}\mathbf{x}$ 形式：

- $\mathbf{x}$：**整个输入**（长向量，含所有位置）
- $\mathbf{x}_j$：**以像素 $j$ 为中心、filter 窗口内**的**短向量**（低维）
- ⚠️ **关键差别**：
  - MLP 的 $\mathbf{w}_j$ **随 $j$ 变化**（每个输出位置有自己**各自独立**的权重）；
  - CNN 的 $\mathbf{w}$ **与 $j$ 无关**——**对所有输出位置用同一个 filter**。

若坚持用"全长度向量"写法，则 CNN 的权重矩阵

$$
\mathbf{W} = (\mathbf{W}_1,\ \ldots,\ \mathbf{W}_q,\ \ldots,\ \mathbf{W}_p)
$$

$$
\mathbf{W}_q = \left(\ \cdots,\ 0,\ \mathbf{g}_1,\ \mathbf{g}_2,\ \ldots,\ \mathbf{g}_p,\ 0,\ \cdots\ \right)^{T}
$$

- 即：**每个 $\mathbf{W}_q$ 只有 filter 窗口覆盖的那一小段 $(\mathbf{g}_1,\ldots,\mathbf{g}_p)$ 非零，其余分量全部补 0**；filter $\mathbf{g}$ 被"搬"到第 $q$ 个输出位置（这也是"zero padding 视角"——把 filter 参数补零到与输入等长）。

$$
\boxed{\;\text{CNN is a regularized MLP（CNN 是一种被强正则化的 MLP）}\;}
$$

| 对比项 | MLP | CNN |
|---|---|---|
| 基本运算 | weighted sum | convolution（**也是 weighted sum**） |
| 权重自由度 | $\mathbf{W}$ 中**所有元素**都自由地从训练数据学 | $\mathbf{W}$ 中**大量元素被强制为 0**；非零元在**所有列上取值完全相同** |
| 每个输出位置的参数 | $\mathbf{w}_j$ 各不相同 | 共用同一个 filter $\mathbf{w}$ |
| 参数量 | 巨大（$p\times p$ 级） | 只有 filter 大小（如 3×3） |
| 学习方式 | 各自为政地学 | "把一组参数移到不同位置去产生输出" |
| 本质 | 自由学习 | **强正则化**的 MLP |

- ⚠️ 老师对这条结论的评价：**这是 CNN 优于 MLP 的"真正原因"**——不是因为 local structure，而是因为**强正则化 = 抑制 overfitting = 提升 generalization**。

### 10. ⭐⭐ CNN 为什么更好：Parameter Sharing 的深层含义

#### 10.1 ⭐ 核心机制：each learnable parameter goes through all pixels

- CNN 的 filter 参数**被所有输入像素和输出像素共享（shared by all input and output pixels）**。
- 最关键的一步推理：**在机器学习过程中，共享意味着这个参数是由所有像素共同决定的，而不是只由某个特定像素决定**。
- ⚠️ 老师的经典表述（PDF 第 308 页原句）：

  > "**Each learnable parameter goes through all pixels. Convert one image as a training sample to every pixel as a training sample?**"

  即：本来一张图像是**一个** training sample；而在 CNN 中，每一个像素位置都相当于一个 training sample，**所有像素一起训练每一个 filter 参数**。
- 于是参数学到的是**覆盖整个输入的 general rule**，而不是 overfit 到某个 specific component。这就是 CNN **robust to novel unseen data**、能克服 overfitting 的原因。

#### 10.2 ⭐ 由此可解释"为什么 filter 只用 3×3 或 1×1"（PDF 第 307 页）

- 如果只想"捕捉大面积信息"，直觉上应该用**大 filter**；但现代 CNN 反而**只用最小的 3×3（甚至 1×1）**。早期模型还用过 7×7、9×9 甚至更大，越到后来越小。
- 理由：**要让每个可学习参数都能"走过"图像的每一个位置（尤其是边界处）**。
  - 用 **1×1** 卷积，参数自然能覆盖每一个像素；
  - 用 **大 filter**（比如 100×100）时，滑到边界就会**有一部分 filter 落在图像之外**，filter 的参数无法访问所有位置 → 学到的不是"全局通用规则"。
- 结论：**filter 越小，越能保证"所有像素共同训练同一个参数"这一正则化优势**。

#### 10.3 ⭐ 由此可解释"为什么 CNN 需要很多层"（receptive field）

- 单个 3×3 卷积层的输出**只依赖输入的 3×3 局部区域**。
- 但多层堆叠后，**感受野（receptive field）逐层扩大**：

| 层数 | 有效覆盖原始输入的窗口 |
|---|---|
| 1 层 3×3 | **3×3** |
| 2 层 3×3 | **5×5** |
| 3 层 3×3 | **7×7** |
| ⋮ | ⋮ |
| 深层（配合尺寸缩减） | 可覆盖**整幅图像** |

- ⚠️ 老师的关键反驳：**"很多人说 CNN 优于 MLP 是因为它利用 local structure。可是层数一多，CNN 的输出能捕捉到几乎整幅图像的信息，不只是一个小窗口。"**——所以"local"不是理由（详见 §10.5）。
- ⚠️ 另一处细节：因为每层还配合 spatial size 缩减（pooling/stride），3×3 在高层的"有效覆盖"相对于**原始输入**更大。

#### 10.4 ⭐ 由此可解释"为什么 CNN 用 ReLU 而不是漂亮的 sigmoid"（PDF 第 309 页）

- 因为 CNN **层数多**：训练时需要 back-propagate error **从最后一层一路传回第一层**。
- 若用复杂的非线性函数（如 sigmoid），梯度在逐层相乘中**越来越弱、几乎变成 0** → **vanishing gradient**，深层根本训不动。
- **ReLU 是最简单的非线性函数**（正半轴近似线性、负半轴置零），梯度为 1 或 0，不会累乘衰减 → 老师说这是 ReLU 之所以成为深度网络标配的**根本理由**（"**the simplest ReLU activation function facilitates the deep layers' learning**"，PDF 原话；CNN 的层数多正是为了配合小 filter 扩大覆盖，§10.3）。
- ⚠️ 但 ReLU **必须仍是非线性函数**（§4.3），否则多层退化为一层。

#### 10.5 ⭐ 老师的理论：驳斥 "local vs global" 说法

围绕 "为什么 CNN 比 MLP 好 / 为什么 Transformer 比 CNN 好"，流行的解释是：

| 流行说法 | 老师的反驳 |
|---|---|
| "CNN 好，因为 convolution 只捕捉 **local** 信息，而图像有 local structure" | ⚠️ **不是理由**。首先，CNN 的 convolution **包含 bias，且沿 channel 维做了全连接**（§9.2）——所以完全可以取 **1×1 卷积**，连空间局部性都不要，CNN 仍然 work；而 1×1 卷积在传统图像滤波里根本不能算 filter（单像素无法滤波）。其次，层数一多，CNN 的输出**已经捕捉到接近整幅图像的信息**（§10.3） |
| "Transformer 好，因为 Transformer 捕捉 **global** 信息，而 CNN 只是 local" | ⚠️ **同样不是理由**。如果"global 就是好"，那么 **MLP 本来就是 fully connected（全连接 = 完全 global）**，理应最好——可 MLP 恰恰表现最差 |
| — | ⚠️ 老师的正面回答：**CNN 的优势来自 parameter sharing 的强正则化**（§10.1）；**global information 并不是靠局部/全局这个维度区分的**。PDF（第 320 页）另有一句关键补充：**"Global information learnt by CNN is on the whole training dataset."**（CNN 的"全局性"体现在它从**整个训练集**学规则）—— 这与 Transformer 用 test input 生成权重的机制有本质区别（§12） |

#### 10.6 ⭐ 1×1 Convolution 为什么有意义（PDF 第 305 页）

- 传统图像处理里，filter 必须是**局部区域**的加权和——**单像素无法"滤波"**。
- 但 CNN 中 **1×1 卷积完全合理**，因为除了空间维，CNN 的卷积还要**沿 channel 维求和**，而沿 channel 维的求和**本身就是一次 fully-connected 的 weighted sum（与 MLP 相同）**。
- 所以 1×1 convolution = **对每个像素位置，做一次跨 channel 的加权求和**（pointwise 操作），可用来升/降 channel 数。
- ⚠️ 老师埋了个伏笔："Later, I will show what is the role of this 1×1 convolution."——**答案在 Transformer**：Transformer 里的 **pointwise feed-forward network** 正是 "each learnable parameter goes through all inputs" 的 1×1 卷积思想（§12）。

#### 10.7 ⭐ 深层网络的整体图景（progressive learning）

```
y = h(W_m^T ... h(W_2^T h(W_1^T x)))     ⇒     y = f(x)
```

| 论断 | 内容 |
|---|---|
| 理论上 | **$m=2$ 就足够**（universal approximator：任意非线性连续函数都能被两层 perceptron + sigmoid 任意逼近，只要节点足够多） |
| 实际上 | 两层**很难找到解**（§7.1 local minima）；$m \gg 2$ 反而**更容易找到解** |
| 因此 | **Deep learning：$m \gg 2$**（现代网络可达上百层） |
| 学到的内容 | 复杂的非线性 input-output 关系被**逐层、渐进（progressive, layer by layer）**地学出来 |
| 层的递推写法 | $\mathbf{x}_{k+1} = h(\mathbf{W}_k^{T}\mathbf{x}_k),\ k=1,2,\ldots,m$，$\mathbf{x}_1 = \mathbf{x}$，$\mathbf{y} = \mathbf{x}_{m+1}$ |

- ⚠️ PDF 第 297–298 页把 supervised learning 写成一个统一的优化问题：给定有限离散样本 $\{\mathbf{x}_i,\mathbf{y}_i\}$，求 $\hat{f}$ 使 $\min_{\hat{f}} e^{2} = \min_{\hat{f}}\sum_{\forall i}\|\mathbf{y}_i - \hat{f}(\mathbf{x}_i)\|_2^{2}$；neural network 的解法就是上面的 $h$-复合形式。
- 老师也在此**公开质疑**了"human knowledge 是否无用"：看上去 raw data 直接进网络就能出结果，"our human knowledge is useless"——但这只是印象，真正的关键仍是 regularization 与 generalization（§7.3、§10.1）。

### 11. ⭐ 深层学习成功的官方总结（PDF 第 341 页 "Conclusion of Deep Learning"）

按 PDF 原文逐条：

1. **The success of AI lies in Machine Learning.**
2. **The success of Machine Learning lies in learning general rules, not overfitting to specific details of training data.**
3. 这一点靠 **learning in convolution with minimum filter size ⇒ CNN** 实现。
4. **因此需要很多 convolutional layers 来捕捉大面积信息 ⇒ Deep learning。**
5. **Deep learning is facilitated by the simplest nonlinear activation function ReLU.**
6. **CNN 中每个学到的参数都走过所有输入，极大增强了 generalization**；但它是**靠从 training data 学到的权重**去捕捉信息，**这也限制了它的能力**（cannot capture what is not learnable from the training set）。
7. **Transformer 用 non-learnable 的 attention module 捕捉 global information**：与 MLP / CNN 都不同，**捕捉 global information 的方式不是从训练集学出来的，而是由具体的 test input 决定的**。
8. **Transformer 所有可学习的模块，用的仍然是 convolution 的思想！**（§12：Q/K/V 投影与 feed-forward 都是 1×1 convolution / pointwise）

### 12. ⭐ Transformer 预告（Topic 10，本周未展开，下周正式讲）

> ⚠️ 本节内容来自 **PDF Topic 10（第 318–341 页）** 与老师本周的口头预告，**本周课堂未讲授**，仅供预习。老师原话："after next week, I will first [cover] further development of the CNN and then based on that, further go to the current state of the art module of the AI model. It is a Transformer."

#### 12.1 Transformer 的定位（PDF 第 319 页）

- 输入 **sequence**（序列）→ 输出 sequence：speech（语音）、text（文本）、time series（时间序列）。
- **RNN（recurrent neural network）** 及其发展 **LSTM（long short-term memory）** 天然处理序列/列表，但 **Transformer 通过把序列操作并行化（parallelization）而胜过它们**。
- 最初为 **NLP（natural language processing）** 而生，如今在 **computer vision** 中也比 CNN 更强。
- 力量的来源是 **Attention module（注意力模块）**：捕捉序列中**每个 word/token 与其余所有 token 的关系**。原始论文标题：***"Attention Is All You Need"***。
- PDF 提出的三个**待答问题**（下周展开）：
  1. Transformer 到底怎么工作？**attention 真是一切吗？**
  2. 与 CNN 有什么关系？
  3. 能否简单地说 "CNN 只捕捉 local information，而 Transformer 捕捉 global information，所以 Transformer 更强"？——⚠️ **不能**（见 §10.5 的反驳）。

#### 12.2 结构：Encoder + Decoder（PDF 第 321–329 页）

- **一叠结构相同的 encoders + 一叠结构相同的 decoders**。
- 机器翻译示例：输入一句英文，输出另一语言的译文；**所有 word/token（或图像的 patch）并行地（parallelly）送入** transformer；输出是 decoder 输出上的**线性分类**。
- 每个 token 先 **embedding** 成一个 feature vector。
- **Attention layer 与 feed-forward layer 都带 residual skip-connection（残差跳连）**。
- 每个 encoder/decoder 中都有 **multi-head attention（多头注意力）**。
- 两类 attention：**self-attention**（源序列自己关注自己）与 **encoder-decoder attention**。

#### 12.3 ⭐ Attention 的计算（PDF 第 330–335 页）

以英译西为例：源句 "The ball is blue" → 目标句 "La bola es azul"。

**Step 1：三个可学习的线性投影（Query / Key / Value）**

$$
\mathbf{Q} = \mathbf{X}\mathbf{W}_q,\qquad \mathbf{K} = \mathbf{X}\mathbf{W}_k,\qquad \mathbf{V} = \mathbf{X}\mathbf{W}_v
$$

$$
\mathbf{q}_i = \mathbf{x}_i\mathbf{W}_q,\quad \mathbf{k}_i = \mathbf{x}_i\mathbf{W}_k,\quad \mathbf{v}_i = \mathbf{x}_i\mathbf{W}_v,\qquad i = 1,2,\ldots,N
$$

- ⚠️ **所有 token 共享同一套可学习参数**——"any single learnable parameter goes through all tokens or is learned from all tokens"。PDF 明确标注：**这就是 CNN 的 1×1 convolution！**（§10.6 的伏笔在此揭晓）

**Step 2：Attention score = Q 与 K 的点积**

$$
\mathbf{R} = \mathbf{Q}\mathbf{K}^{T}
$$

- 点积度量**两个 token 之间的相似度**（similarity）。
- ⚠️ PDF 标注：这个中间矩阵（"factor" matrix）的每个元素都是两个 word 的乘积 → **Covariance Matrix!!!**（与协方差矩阵同构）。

**Step 3：用 relevance 做 Value 的加权求和**

$$
\mathbf{Z} = \mathbf{Q}\mathbf{K}^{T}\mathbf{V}, \qquad \mathbf{z}_i = \sum_{j}\left(\mathbf{q}_i\cdot\mathbf{k}_j\right)\mathbf{v}_j
$$

- Q 与 K 的点积算出**每对 word 之间的 relevance**，再以此作为"factor"对所有 **Value** 做加权和，结果即 attention module 的输出。
- ⚠️ PDF 讲义中**未写出 softmax 与 $\sqrt{d_k}$ 缩放**，属简化表述；标准 self-attention 为 $\mathrm{softmax}(\mathbf{Q}\mathbf{K}^{T}/\sqrt{d_k})\mathbf{V}$。以老师课件写法为准。

**Step 4：Learnable feed-forward network（pointwise）**

$$
\mathbf{Y} = h\!\left(h\!\left(h\!\left(\mathbf{Z}\mathbf{W}_1\right)\mathbf{W}_2\right)\mathbf{W}_3\right),\qquad
\mathbf{y}_i = h\!\left(h\!\left(h\!\left(\mathbf{z}_i\mathbf{W}_1\right)\mathbf{W}_2\right)\mathbf{W}_3\right)
$$

- 每行 $\mathbf{z}_i$ 对应一个 token；**所有 token 共享同一套参数**。
- ⚠️ PDF 强调：Transformer 的 feed-forward network **是 pointwise 的，不是 MLP**——"Pointwise means that each single learnable parameter goes through all inputs. **It comes again from the key concept, 1×1 convolution of CNN.**"

#### 12.4 ⭐⭐ 与 MLP / CNN 的本质区别（PDF 第 334、341 页）

> **"Each output token is weighted sum of all input tokens, capturing global information. Different from MLP and CNN, weights are not learnt by training data. They are flexibly generated by specific test input. Attention itself is not learnable."**

| 属性 | MLP | CNN | Transformer |
|---|---|---|---|
| 权重来源 | 从 training data 学（**自由**） | 从 training data 学（**共享 + 大量置零**） | ⚠️ **不从 training data 学**——由**具体 test input** 动态生成（attention 本身 non-learnable） |
| 捕捉范围 | 全连接（global） | 小 filter 局部、**多层后覆盖整图**；从**整个训练集**学全局规则 | **输出 token 是所有输入 token 的加权和 → 天然 global** |
| 解决 overfitting 的方式 | 无（→ overfit） | **parameter sharing 强正则** | attention 由 test input 决定，**不依赖训练集学到的固定权重** |
| 可学习部分 | 全部权重 | convolution filter | 仅 **Q/K/V 投影 + feed-forward**（且都基于 **1×1 convolution / pointwise** 思想） |

- ⚠️ Encoder-decoder attention：最后一个 encoder 的输出 → 送入 **Key 与 Value**；其下方 self-attention module 的输出 → 送入 **Query**。即 $\mathbf{Z} = \mathbf{Q}\mathbf{K}^{T}\mathbf{V}$，$z_i = \sum_j (\mathbf{q}_i\cdot\mathbf{k}_j)\mathbf{v}_j$。

#### 12.5 Vision Transformer（ViT）vs CNN（PDF 第 339 页）

- **ViT** 在大规模数据上 pre-train 后，在**多项 computer vision benchmark 上超过 SOTA 的 convolutional network**，且训练所需算力更少。
- CNNs 在各类 CV 任务上有**经过验证的良好记录**，处理大规模数据集**高效**；而 **Vision Transformer 在需要 global dependencies 与 contextual understanding 的场景下有优势**。
- ⚠️ 注意 PDF 在 "global(?)" 处打了问号——与 §10.5、§12.4 的讨论呼应：老师**不认为** "local vs global" 是完整的解释。

### 13. ⭐ 本周考点速查

| 考点 | 要点 | 节号 |
|---|---|---|
| **neuron model** | $u_k=\sum_j w_{kj}x_j$，$y_k=f(u_k-\theta_k)$；weighted sum 可学，activation 固定 | §2 |
| **bias 技巧** | 令 $x_0=1,\ w_{k0}=-\theta_k$ → $v_k=\sum_{j=0}^{p}w_{kj}x_j$；**网络必须有 bias** | §2.3 |
| **四种 activation function** | binary（阶跃）/ piecewise-linear（带过渡区）/ **sigmoid**（光滑处处可导）/ **ReLU**（$\max(0,v)$） | §3 |
| **sigmoid 用于 MLP 的原因** | 处处可导，且 $f'(q)=a\,f(q)[1-f(q)]$——**用输出即可算导数** | §3, §6.4 |
| **ReLU 用于 CNN 的原因** | 最简单的非线性函数；深层 backprop 不会 vanishing gradient | §3, §10.4 |
| **MLP 三种写法** | scalar / vector $\mathbf{y}=f(\mathbf{V}^T f(\mathbf{W}^T\mathbf{x}))$ / matrix | §4 |
| **⭐ activation 必须非线性** | 线性时 $\mathbf{y}=\mathbf{V}^T\mathbf{W}^T\mathbf{x}=(\mathbf{W}\mathbf{V})^T\mathbf{x}$ → 多层 = 单层 | §4.3 |
| **单层 loss** | $J(\mathbf{w})=E\{(t-\mathbf{w}^T\mathbf{x})^2\}$，是 $\mathbf{w}$ 的**二次函数** → 唯一 minimum | §5.1 |
| **⭐ least square 闭式解** | 令梯度 = 0 → $\mathbf{w}=(\mathbf{X}\mathbf{X}^{T})^{-1}\mathbf{X}\mathbf{t}^{T}$；类似 Mahalanobis | §5.2 |
| **⭐ LMS / delta rule** | $\mathbf{w}\leftarrow\mathbf{w}+\eta(t_i-y_i)\mathbf{x}_i$ | §5.3 |
| **learning rate 取舍** | 大 → 快但振荡；小 → 慢但精确；常用"先大后小" | §5.4 |
| **SGD / mini-batch / full-batch** | 期望的实现方式；**batch size 很关键** | §5.5 |
| **learning curve** | training loss 必降；**test loss 可能升**（gap = 问题所在） | §5.6 |
| **单层决策边界** | $\mathbf{w}^{T}\mathbf{x}=0$，直线/平面/hyperplane | §5.6 |
| **⭐⭐ backprop 动机** | 多层 loss 求导方程**无解析解**（非线性 $f$）；但梯度可算 → 用 gradient descent | §6.1 |
| **⭐⭐ 链式法则结果** | $\frac{\partial J}{\partial v_{kj}}=-(t_k-y_k)f'(q_k)z_j$；$\frac{\partial J}{\partial w_{ji}}=-\sum_k (t_k-y_k)f'(q_k)v_{kj}f'(q_j)x_i$ | §6.2 |
| **⭐ 为什么叫 backprop** | 隐含层的 error = 输出层 error 经 $v_{kj}$ **反向传回** | §6.2 |
| **⭐ sigmoid 导数** | $f'(q)=a f(q)[1-f(q)]$ | §6.4 |
| **backprop 5 步** | init / present epoch / forward / backward / iterate；**每轮打乱样本顺序** | §6.5 |
| **⭐ local minima** | 梯度只含局部信息，停在 local minimum → **underfitting** | §7.1 |
| **⭐⭐ overfitting** | double spiral：training 100% 正确但 decision boundary 扭曲，略变即错；**加层不能解决** | §7.2 |
| **double spiral 数字** | 线性边界错误率 ≈ **50%**；两层 MLP 训练集 **100%** 正确 | §7.2 |
| **⭐ regularization 三种** | 限制函数类 $\hat{f}\in\Omega$ / 先降维 / 加正则项 $\lambda\Phi(\hat{f})$（如 sparse） | §7.3 |
| **validation set** | 在 validation loss 最小处停训（**只能部分解决** overfitting） | §7.4 |
| **⭐ 发展史** | 1940s 单层 → 1980s backprop 高峰 → 1990s–2000s 谷底（CVPR/TPAMI 拒稿）→ 2006+ CNN 复兴（60%→90%+）→ Transformer/large model | §8 |
| **deep learning 定义** | **只是层数多（$m\gg 2$）**，不是"学到内部深处知识"；理论 $m=2$ 就够但难找解 | §8, §10.7 |
| **CNN 五大特征** | architecture / convolution / ReLU / pooling / deep many layers | §9.1 |
| **VGG-Face 例子** | 第一层 64 filters → 64 feature maps；最终 7×7×(**>500**) 特征图 | §9.1 |
| **⭐⭐ CNN 卷积公式** | $y_{i,j,k}=\sum_{n=1}^{C}\sum_{m=-1}^{1}\sum_{l=-1}^{1}w_{l,m,n,k}x_{i-l,j-m,n}+b_k$ | §9.2 |
| **⭐ 与 MLP 的差别** | MLP：$o_j=\sum_i w_{ji}x_i$（$w_{ji}$ 随 $j$ 变）；CNN：$o_j=\sum_i w_i x_{j-i}$（**$w$ 与 $j$ 无关**） | §9.3 |
| **⭐⭐ CNN is a regularized MLP** | CNN 的 W 有大量 **0**，且非零元在各列**取值相同**（filter 挪到不同位置） | §9.3 |
| **⭐ parameter sharing 的意义** | 每个参数走过**所有像素** → 由**所有像素共同训练** → **一个像素 = 一个 training sample** → 抗 overfitting | §10.1 |
| **为什么 filter 用 3×3 / 1×1** | 保证参数能覆盖**每个位置**（大 filter 在边界会露出图像外） | §10.2 |
| **为什么需要很多层** | 3×3 → 5×5 → 7×7…**感受野随层数扩大**，最终覆盖整图 | §10.3 |
| **为什么用 ReLU** | 层多 → backprop 路径长 → ReLU 梯度不衰减 | §10.4 |
| **1×1 convolution 为何有意义** | 沿 channel 维的 weighted sum = fully connected（同 MLP） | §10.6 |
| **⚠️ 驳斥 local/global 说法** | MLP 全连接（global）却最差；CNN 高层也覆盖整图；Transformer 更不是靠 global | §10.5 |
| **⭐ Transformer 预告** | Encoder+Decoder；$\mathbf{Q}=\mathbf{X}\mathbf{W}_q,\mathbf{K}=\mathbf{X}\mathbf{W}_k,\mathbf{V}=\mathbf{X}\mathbf{W}_v$；$\mathbf{R}=\mathbf{Q}\mathbf{K}^T$（类似协方差）；$\mathbf{Z}=\mathbf{Q}\mathbf{K}^{T}\mathbf{V}$ | §12.3 |
| **⭐⭐ attention 的独特性** | **权重不由 training data 学得**，而由 **specific test input 灵活生成**；attention 本身 non-learnable | §12.4 |
| **Q/K/V 与 feed-forward 的实质** | 都是 **1×1 convolution / pointwise**——Transformer 可学习部分仍用 convolution 思想 | §12.3, §11 |

### 14. 本周要点小结

- **Neuron model**：neuron = weighted sum → 减 threshold → activation function。**weighted sum 是唯一可学习的部分**，machine learning 就是更新这些 weight；**bias 必须有**，只是可以吸收进输入（$x_0=1$）。
- **Activation function**：MLP 时代用 **sigmoid**（光滑处处可导，$f'=af(1-f)$ 计算极省）；CNN/Transformer 时代用 **ReLU**（最简非线性，避免深层 vanishing gradient）。**activation 必须非线性**，否则多层网络退化为单层。
- **单层网络**：loss 是 $\mathbf{w}$ 的二次函数，有**闭式解** $\mathbf{w}=(\mathbf{X}\mathbf{X}^{T})^{-1}\mathbf{X}\mathbf{t}^{T}$（least square），也可用 **gradient descent**（$\mathbf{w}\leftarrow\mathbf{w}+\eta(t_i-y_i)\mathbf{x}_i$）迭代得到同一结果；learning rate、batch size 都在此埋下伏笔。
- **Backpropagation**：多层网络的 loss 导数方程**无解析解**（非线性 $f$），但**梯度表达式可以用 chain rule 算出** → 用 gradient descent 迭代。其精髓是把输出层的 error 经权重**反向传回**隐含层，故得名 backpropagation。训练 = forward 计算 output + backward 更新权重，逐 epoch 迭代、每轮打乱样本顺序。
- **两大困难**：**local minima**（→ underfitting，梯度只含局部信息）与 **overfitting**（→ 训练完美但 test 崩，老师视为 machine learning 最核心的问题）。**regularization**（限制函数类 / 降维 / 加正则项）与 **validation set + early stopping** 是缓解手段，但都不能彻底解决。
- **发展史**：1940s 起只能做单层 → 1980s backprop 带来第一个高峰 → 1990s–2000s 因 overfitting 跌入谷底（CVPR/TPAMI 拒稿）→ 2006 年后 CNN + 大数据集复兴（真实图像识别率 60% → 90%+，主要由工业界推动）→ Transformer → large model（ChatGPT）。**DNN/CNN 是第三代神经网络。**
- **CNN** = convolution + ReLU + pooling + deep layers。卷积公式 $y_{i,j,k}=\sum_{n}\sum_{m}\sum_{l}w_{l,m,n,k}x_{i-l,j-m,n}+b_k$ 比传统卷积多了**沿 channel 维的求和**（与 bias）。
- **⭐ CNN 优于 MLP 的真正原因（老师观点）**：不是"local structure"，而是 **CNN is a regularized MLP**——权重矩阵被强制"局部非零 + 所有位置共享同一组非零值"。由此**每个可学习参数走过所有像素，由所有像素共同训练**（一张图 = 每像素一个 training sample），学到 general rule 而非 overfit；也由此解释了**为什么 filter 只用 3×3/1×1**（保证参数能到每个位置）、**为什么需要很多层**（感受野 3×3→5×5→7×7 逐层扩大）、**为什么用 ReLU**（层多、梯度不能衰减）、**1×1 卷积为何有意义**（channel 维本来就是全连接）。
- **Transformer（预告）**：Encoder + Decoder 堆叠，靠 **attention** 捕捉 token 之间的相互关系；$\mathbf{Q}=\mathbf{X}\mathbf{W}_q$、$\mathbf{K}=\mathbf{X}\mathbf{W}_k$、$\mathbf{V}=\mathbf{X}\mathbf{W}_v$ 都是 **1×1 convolution**；$\mathbf{R}=\mathbf{Q}\mathbf{K}^{T}$ 度量相似度（类比 covariance matrix），$\mathbf{Z}=\mathbf{Q}\mathbf{K}^{T}\mathbf{V}$。⚠️ 与 MLP/CNN 的**本质不同**：**attention 的权重不是从 training data 学出来的，而是由具体的 test input 动态生成**，attention 本身 non-learnable——这可能正是它超越 CNN 的关键；而 **Transformer 所有可学习的模块，用的仍是 convolution 的思想**。

### 15. 下一周预告

老师在转写末尾明确说明："**After next week, I will first [cover] further development of the CNN, and then based on that, further go to the current state of the art module of the AI model. It is a Transformer.**"

1. **CNN 的进一步发展（Further Development of CNN）**：PDF 第 310–317 页列出的是**老师本人的研究工作**，预计下周展开：
   - **Image Segmentation**（逐像素的场景理解，pixel-wise scene understanding）；
   - **Context Contrasted Local (CCL) features**（把局部信息与其 context/surroundings 做对比）：H. Ding, X.D. Jiang et al., "Context contrasted feature and gated multi-scale aggregation for scene segmentation," **CVPR Oral 2018**；H. Ding, X. Jiang et al., "Semantic Segmentation with Context Encoding and Multi-Path Decoding," IEEE TIP 2020；
   - **Gated Multi-scale Aggregation**（skip layer 输出选择性融合）；
   - **Boundary Refinement**（multi-scale Gaussian diffusions）；
   - **Shape-Variant Convolution**（spatial-dependent vs semantic-dependent context）：H. Ding, X. Jiang et al., "Semantic Correlation Promoted Shape-Variant Context for Segmentation," **CVPR'19 Oral**。
2. **Transformer（Topic 10 正式讲授）**：重点回答 PDF 第 319–320 页提出的三个问题——Transformer 如何工作？attention 是否真是一切？它与 CNN 有何关系？**"local vs global" 是否足以解释 Transformer 优于 CNN？**（老师已提前给出否定性论证，见 §10.5。）
3. 后续还会讲 Transformer 在 CV 中的落地：**Vision Transformer (ViT)** 及老师团队的 **Vision-Language Transformer**（H. Ding, C. Liu, S. Wang, X. Jiang, "Vision-Language Transformer and Query Generation for Referring Segmentation," **ICCV'21**；扩展版 **IEEE TPAMI**, vol. 45, no. 6, pp. 7900–7916, Jun. 2023）。

> ⚠️ 具体以 Week 9 课件/转写为准。

---

## Week 9 — Topic 9 续：Further Development of CNN（Image Segmentation）＋ Topic 10：Deep Learning from CNN to Transformer

> **本周主线**（转写开场原话，已按 PDF 修正 ASR）："Last week we studied CNN. In my opinion, the key role of the CNN is to make the **kernel learning go through all positions of the input data**, so that in the learning process, the kernel is learned from all points — for example, in the image, from all pixels, not fixed to a particular pixel. Because of that, the parameters are very robust and reliable. I believe this is the key difference from all past machine learning. This is why I think this point is some kind of **revolution** in machine learning."
>
> 本周分两大块：
> 1. **Topic 9 续：Further Development of CNN**——老师用自己的 **image segmentation（图像分割）** 研究，说明如何在 CNN 之上做"further development"：**Context Contrasted Local (CCL) features → Gated Multi-scale Aggregation → Boundary Refinement**，以及 **Shape-Variant Convolution**。这些工作的共同思想是：**权重不再只由 training data 学定，而由具体 input 生成**——这正是本节后半 **Transformer attention** 的伏笔。
> 2. **Topic 10：from CNN to Transformer**——正式讲 Transformer 的 **encoder-decoder** 结构、**self-attention**、**multi-head attention**、**pointwise feed-forward network**、**residual/skip connection**，以及 **ViT / Vision-Language Transformer**。
>
> ⚠️ 本周是 **Jiang Xudong 老师主讲部分（Topic 1–10）的最后一课**；Week 10–13 的 Topic 11–14 由 **Dr. Cheng Jun** 讲授。老师还在本周末尾**明确公布了 final exam 的题型与范围**（见 §19，极重要）。

> **权威来源说明**：本周官方讲义为 `EE6222_lecturenote1to9.pdf` **第 310–341 页**：**Further Development of CNN（image segmentation）= p.310–317**；**Topic 10 "Deep Learning: from CNN to Transformer" = p.318–341**。Week 8 笔记 §12 的 Transformer 内容是"预告版"；**本周是正式讲授版**，新增了 **multi-head attention、embedding + positional encoding、residual connection、generative decoding、ViT、Vision-Language Transformer、期末考试范围** 等内容。转写 `week9.txt` 噪声仍然很重（尤其 `C n / SN / the N / arn` 都指 CNN，`prime` 同时可能是 kernel 或 pre-trained），以下一律以 PDF 的公式、结构图与老师课堂讲解为准。本周典型 ASR 错拼对照：

| 转写噪声 | 正确术语 |
|---|---|
| C n / SN / the N / CN / arn / the s | **CNN**（convolutional neural network） |
| near / neon / nel / nail / nals / nyls / nyer / ayer / mal / nay | **layer**（层；本周仍高频） |
| prime / prim / prin（"prime learning"） | **kernel**（卷积核）；⚠️ "prin trend / prim trained" 则是 **pre-trained**（预训练），需按上下文区分 |
| fit forward / ft forward / fd network / fit fd network | **feedforward（network）** |
| nose / north / moss function | **loss（function）** |
| arrow / ero / ro | **error** |
| pulling | **pooling** |
| china / chins | **channel** |
| redo / renew / reno | **ReLU** |
| greatly / grid / cog decent | **gradient descent** |
| taste / ta / tasted data | **test / test data** |
| twining / trending / turning data | **training data** |
| correnation / crenation / corre | **correlation**（相关） |
| mutate / match attention / mutate attention | **multi-head attention**（多头注意力） |
| venue / V | **Value**（注意力中的 V） |
| gauge sum / gaged sum | **gated sum**（门控求和） |
| dint kernel | **dilated kernel**（空洞卷积核） |
| impasse | **impulse**（冲激） |
| gu / guine / gazing / gausin | **Gaussian**（高斯） |
| pit convolution | **1×1 convolution** |
| rent 101 / rent of 101 ayers | **ResNet-101**（101 层残差网络） |
| bel / beling / enable / abeling | **label / labeling**（标注） |
| objector recognition | **object recognition** |
| neck / ak / train / ska | **lake / lake / terrain / sky**（分割示例中的类别） |
| pur effect | **blur effect**（平均/模糊效应） |
| sweeten our humans | **surpass humans**（超越人类） |
| marching learning | **machine learning** |
| quits / equations（"four quits"） | **questions**（题目） |
| zoo of MAP | **theory of MAP** |
| class designed | **classifiers**（分类器） |
| A T GP | **ChatGPT** |
| V IT / Vs transformer / IT | **ViT**（Vision Transformer） |
| T P / P | **TPAMI**（IEEE Trans. on Pattern Analysis and Machine Intelligence） |
| 1918 / 2070 | **2018 / 2017**（年份） |
| single mold function | **sigmoid function** |
| nnnar / nn linear | **nonlinear**（非线性） |
| AARP / M ALP / MP | **MLP** |
| compute / computation / compilation | **computer vision / computation**（按上下文） |

### 1. 本周定位：从 "CNN 的进一步发展" 到 Transformer

| 阶段 | 核心机制 | 权重从哪里来？ | 本周对应 |
|---|---|---|---|
| **MLP** | 全连接 weighted sum | 从 **training data** 学，训练后固定 | Week 8 |
| **CNN** | convolution（卷积；parameter sharing，参数共享） | 从 **training data** 学，所有位置共享，训练后固定 | Week 8 + 本周前半 |
| **CNN 的进一步发展** | gated sum / shape-variant convolution | ⚠️ **由具体 input 生成**（不是训练后固定） | 本周 §4–§7 |
| **Transformer** | **attention（注意力）** | ⚠️ **attention 权重由具体 test input 生成**；只有 Q/K/V 投影与 FFN 的参数是学出来的 | 本周 §8–§18 |

- 老师用一句话贯穿全课：**machine learning 的成功在于学到 general rule，而不是 overfit 到 training data 的 specific details**。CNN 用 **parameter sharing** 做到这一点；Transformer 则进一步让**加权求和的权重随 input 自适应**。
- ⚠️ 老师特别强调：**"attention 的权重不是从 training data 学出来的"** 并不是说 Transformer 没有可学习参数——**Q/K/V 的线性投影矩阵、feed-forward 网络的矩阵仍然是可学习的**；不可学的是**由 Q 与 K 的点积算出来的那组 attention weights**。这一点是本周最容易混淆、也最常考的地方（§12.5、§16）。

### 2. 回顾：CNN 的关键——kernel 走过所有位置

#### 2.1 老师开场原话的逻辑链

1. CNN 的 **kernel（卷积核 / filter）** 在**所有空间位置**上滑动 → 同一个 kernel 参数被**所有像素**使用。
2. 因此这个参数不是由某一个特定像素决定的，而是由**所有像素共同训练**出来的。
3. 所以学到的参数**非常 robust、reliable**，学到的是覆盖整个输入的 **general rule**，而不是 overfit 到某个局部细节。
4. 这就是 CNN 相对过去 machine learning 的 **revolution**。
5. 但也因为 CNN 是在**超大规模通用数据集**（如 ImageNet）上训练的，**具体应用**（如医学图像、特定场景分割）还需要用该应用的数据做 **fine-tune（微调）**，让网络 specific for your task。

#### 2.2 三个必须记住的卷积尺寸公式

**① 输出空间尺寸**（输入 $I\times I$，kernel $K\times K$，padding（填充）$P$，stride（步幅）$S$）：

$$
O=\left\lfloor\frac{I+2P-K}{S}\right\rfloor+1
$$

- **same padding**：$P=(K-1)/2$ 且 $S=1$ 时，$O=I$（空间尺寸不变）。
- **pooling（池化）/ stride > 1**：空间尺寸按比例缩小。Week 8 的 VGG-Face 例子中，2×2 pooling 让长宽各减半、像素数只剩 $1/4$。

**② 一个卷积层的参数量**（输入 $C_{in}$ 个 channel，输出 $C_{out}$ 个 channel）：

$$
\#\text{params}=(K_h K_w C_{in}+1)\times C_{out}
$$

- $+1$ 是每个输出 channel 的 **bias**。
- ⚠️ 对比 MLP：若输入是 $P\times Q\times C_{in}$、输出 $P\times Q\times C_{out}$，全连接层参数量是 $(PQC_{in}+1)C_{out}$，约为 CNN 的 $PQ/(K_hK_w)$ 倍——这就是 **parameter sharing** 带来的正则化。

**③ 感受野（receptive field）递推**：

$$
r_L=r_{L-1}+(K_L-1)\prod_{i=1}^{L-1}S_i,\qquad r_0=1
$$

- 对连续堆叠的 **3×3、stride 1** 卷积：$r_L=r_{L-1}+2=2L+1$，即 **3×3 → 5×5 → 7×7 → …**（Week 8 §10.3 的结论）。
- 对 **1×1** 卷积：$K=1$，感受野**不增加**，只做跨 channel 的 weighted sum（Week 8 §10.6）。
- ⚠️ 这解释了为什么"单层只看局部"不等于"CNN 只看局部"：层数一多，输出可以覆盖几乎整幅图像。

#### 2.3 一句话复习 CNN 的本质

$$
\boxed{\;\text{CNN is a regularized MLP（CNN 是一种被强正则化的 MLP）}\;}
$$

- MLP：$o_j=\sum_i w_{ji}x_i$，每个输出位置有**各自独立**的权重。
- CNN：$o_j=\sum_i w_i x_{j-i}$，**所有输出位置共享同一个 filter** $\mathbf{w}$。
- 写成大矩阵时，CNN 的 $\mathbf{W}$ 有大量 **0**，且非零元在各列上**取值完全相同**（filter 被"搬到"不同位置）。

### 3. Further Development of CNN：Image Segmentation（逐像素场景理解）

#### 3.1 什么是 image segmentation

- **Image segmentation（图像分割）** = **pixel-wise scene understanding（逐像素场景理解）**：把图像中的**每一个像素**分类到不同类别（人、建筑、天空、道路、草地……）。
- 输出是一张 **segmentation map（分割图）**：不同颜色代表不同类别；颜色只是为了可视化，本身没有语义。
- 与 **object recognition / image classification（物体识别 / 图像分类）** 的区别：

| 任务 | 输入 | 输出 | 标注成本 |
|---|---|---|---|
| **Object recognition** | 一张图像 | **一个** class label（这张图是猫/狗/车） | 低：一张图一个 label |
| **Image segmentation** | 一张图像 | **每个像素**一个 class label（$P\times Q$ 个 label） | 极高：需要逐像素人工标注 |

- ⚠️ 老师强调：分割的标注**非常昂贵**，所以能拿到的分割训练集通常**很小**；用小数据集从零训练一个很深的网络**不够**。解决办法是 **transfer learning（迁移学习）**：
  1. 先用**大规模分类数据集**（ImageNet，数百万张带 label 的真实图像）训练一个强大的 **pre-trained network（预训练网络）**；
  2. 再在分割数据集上 **fine-tune（微调）**，并在网络顶部**加一些专门为分割设计的小网络/卷积层**。

#### 3.2 例子：ResNet-101 + 分割头

- 老师以 **ResNet-101**（101 层的 residual network，残差网络）为例：
  - 输入：$200\times200\times3$ 的 RGB 图像；
  - 经过许多 **convolution + pooling** block 后，最后的 feature map 空间尺寸变为 **16×16**，channel 数约 **2000**（转写数字；ResNet-101 标准最后一 stage 是 **2048** 个 channel）；
  - 这个 16×16×2048 的 feature map 是在 ImageNet 上预训练得到的，**非常可靠**。
- ⚠️ ResNet 的两个关键组件（背景补充）：
  - **batch normalization（批归一化）**：对每个 mini-batch 的激活做归一化，稳定训练、允许更深网络；
  - **skip connection / residual connection（残差跳连）**：$\mathbf{y}=\mathbf{x}+F(\mathbf{x})$，让梯度有直接通路（详见 §11）。
- 问题：预训练网络是为 **object recognition** 训练的——它用**整张 16×16 feature map** 去预测**一个** class。而分割要预测**每个像素**的 class，不能只看一个像素，必须看它的 **neighborhood / context（邻域 / 上下文）**。
- 因此需要在预训练网络之上**再加卷积层**，让每个输出位置收集**更大范围**的信息。这就引出三个必须解决的问题（外加另一项工作处理的 kernel 形状问题）→ 老师这几项工作的**核心贡献**：

| 问题 | 现象 | 解决方法（§） |
|---|---|---|
| **① Context / average blur** | 只用大区域卷积 → 输出是大区域的"平均"，不同物体的特征不够 distinct | **Context Contrasted Local (CCL) features**（§4） |
| **② Scale variation** | 物体有大有小；哪个尺度的特征更重要**因位置而异** | **Gated Multi-scale Aggregation**（§5） |
| **③ Boundary ambiguity** | 边界两侧像素用大区域看"几乎一样"，无法准确定位边界 | **Boundary Refinement**（§6） |
| **④ Kernel shape mismatch** | 固定方形 kernel 与物体形状不匹配 | **Shape-Variant Convolution**（§7） |

> 前三条来自 **CVPR Oral 2018** 与 **IEEE TIP 2020** 的 segmentation 工作；第四条来自 **CVPR'19 Oral 2019**。三者的共同点：**加权求和的权重由具体 input 生成，而不是训练后固定**——这就是老师反复强调的"further development on top of CNN"。

### 4. 贡献一：Context Contrasted Local (CCL) Features

#### 4.1 动机：大区域卷积的 "average / blur effect"

- 为了让每个像素看到更大的 **context（上下文）**，最直接的做法是在 16×16 feature map 上继续堆 **更大的卷积核 / 更深的卷积层**。
- ⚠️ 但老师指出：如果输出**只**来自一个很大的区域，那么输出本质上是该区域信息的**平均（average）** → 产生 **blur effect（模糊效应，转写 "pur effect"）**。不同物体的特征会变得**不够 distinctive（可区分）**。
- 直觉：只看一大片区域的平均颜色，很难区分"人"和"背景"；需要把**局部细节**与**周围环境**做**对比（contrast）**。

#### 4.2 做法：local 与 context 的差值

在预训练网络的最后一层（16×16 feature map）之上，接两个 **3×3** 卷积分支：

| 分支 | 卷积类型 | 看到的信息 | 作用 |
|---|---|---|---|
| **Local branch** | 标准 **3×3 convolution** | 中心像素附近的小区域 | 保留**局部细节** |
| **Context branch** | **dilated 3×3 convolution（空洞卷积）** | 9 个采样点散布在更大区域 | 收集**周围 context / surroundings** |

- 然后把两个分支的输出**相减**：

$$
\boxed{\;\mathbf{F}_{CCL}(p)=\underbrace{\sum_{q\in\mathcal{N}_{d}(p)}w^{ctx}_{q}\mathbf{x}_q}_{\text{context (dilated)}}
\;-\;\underbrace{\sum_{q\in\mathcal{N}_{3}(p)}w^{loc}_{q}\mathbf{x}_q}_{\text{local (3×3)}}\;}
$$

其中 $\mathcal{N}_{3}(p)$ 是以 $p$ 为中心的 3×3 邻域，$\mathcal{N}_{d}(p)$ 是 dilated kernel 覆盖的、范围更大但更稀疏的邻域。

- ⚠️ **为什么相减有用**：大区域与小区域共享的那部分"平均/背景"成分会被**抵消**，剩下的正是**局部相对于周围的差异（contrast）**——这正是区分物体边界、纹理、显著区域的关键。
- 老师的人眼类比：**"To identify a point, we need to compare this point with its surroundings."** 人类视觉判断一个点是什么，从来不是孤立地看这个点，而是把它与周围环境比较。这个"比较"在数学上就是**差值**。

#### 4.3 Multi-level CCL

- 一个 CCL block 只能提供一个尺度的对比；把**多个 CCL block 串联（chained）**，就得到 **multi-level context contrasted local features**。
- 浅层 block 的 context 范围小，深层 block 的 context 范围大 → 多尺度、多层次的对比特征。
- PDF p.311 的原话："Several blocks are chained to make multi-level context contrasted local features."

| 层次 | 感受野 | 对比的"周围"范围 | 适合识别的结构 |
|---|---|---|---|
| 浅层 CCL | 小 | 近邻纹理 | 边缘、细纹理、小物体 |
| 中层 CCL | 中 | 局部区域 | 物体部件 |
| 深层 CCL | 大 | 大范围场景 | 物体整体、场景类别 |

### 5. 贡献二：Gated Multi-scale Aggregation（门控多尺度聚合）

#### 5.1 动机：不同位置需要不同尺度

- 图像中的物体**尺度变化很大**：近处的人占大面积，远处的车只占很小面积。
- CNN 的浅层感受野小、深层感受野大 → 不同层的 feature / classification score 天然代表**不同尺度**。
- 一个自然的想法：把**多个尺度的 classification score** 聚合起来。**之前的工作**通常是把各层的 score **直接相加（simple sum）**：

$$
\mathbf{S}_{\text{old}}(p)=\sum_{l=1}^{L}\mathbf{s}_l(p)
$$

- ⚠️ 老师指出：**简单相加没有 selection（选择）功能**。对某些位置（如近处大物体）应该更信任**大尺度**；对另一些位置（如远处小物体）应该更信任**小尺度**。权重应该**因位置而异**。

#### 5.2 信息图（information map）与自顶向下连接

老师的设计分三步：

1. **每个尺度层的所有 channel → 一张 information map**：
   对第 $l$ 层的 feature map（$C_l$ 个 channel）做一次 **1×1 convolution**，把 $C_l$ 个 channel 压成**一张** map：

   $$
   \mathbf{g}_l(p)=\mathbf{w}_l^{T}\mathbf{f}_l(p)\in\mathbb{R}
   $$

   这张 map 在每个空间位置 $p$ 上的值，表示"**该位置应该更偏向大尺度还是小尺度**"。

2. **加入自顶向下（top-down / reverse）连接**：
   原来的信息流是 bottom-up（低层 → 高层）。老师额外把**高层的信息反向传回低层**，使高层语义与低层细节**平衡（balanced）**，而不是只让低层信息单方向流向高层。

3. **归一化生成权重图**：
   对每个位置 $p$、每个尺度 $l$，生成一个非负权重 $\alpha_l(p)$，并归一化：

   $$
   \sum_{l=1}^{L}\alpha_l(p)=1,\qquad \alpha_l(p)\ge 0
   $$

#### 5.3 Gated Sum 的定义

> PDF p.312 只给出结构示意图；下面的公式是按老师课堂讲解整理的数学表达。

$$
\boxed{\;\mathbf{S}(p)=\sum_{l=1}^{L}\alpha_l(p)\,\mathbf{s}_l(p)\;}
$$

- $\mathbf{s}_l(p)$：第 $l$ 层（第 $l$ 个尺度）在位置 $p$ 的 **classification score map**；
- $\alpha_l(p)$：由 input 生成的 **gate（门控权重）**；
- $\mathbf{S}(p)$：融合后的最终 classification score map。

#### 5.4 ⭐ 为什么叫 "gated sum" 而不是普通的 "weighted sum"

老师先列出三种传统的权重确定方式，再给出本工作的第四种：

| 方式 | 权重来源 | 特点 |
|---|---|---|
| **① 全 1** | 不设定 | 就是 simple sum，没有选择 |
| **② 人工设计** | 人根据先验知识设定 | 不同输入、不同位置的最优尺度未知，人工很难设计 |
| **③ 从 training data 学习** | MLP / CNN 的权重，训练后**固定** | 对所有 input 都用同一组权重，不能自适应 |
| **④ 由具体 input 生成（本工作）** | **每个 input image 自己生成** | 不同图像、不同位置的权重都不同；**训练后不固定** |

- ⚠️ 本工作用的是 ④：**权重 $\alpha_l(p)$ 由 individual input 生成，而不是从 training data 学出来的固定值**。
- 因此老师把它命名为 **gated sum（门控求和）**：gate 的作用就是**根据当前输入选择/调节**不同尺度的贡献。
- 关键卖点（也是论文被 CVPR Oral 接收的原因）：**不同图像中，大物体和小物体的位置完全不同，固定权重无法处理；只有 input-dependent 的权重才能自适应。**

$$
\boxed{\;\text{普通 weighted sum：权重 learned \& fixed；gated sum：权重 generated by input}\;}
$$

- ⚠️ 这与 Transformer 的 **attention** 在思想上是**同构的**：attention 也是"用 input 生成权重，再对所有 token 做 weighted sum"。老师特别说明：**他的 gated sum 工作（CVPR 2018）在 ViT（2020/2021）之前**，并不是从 Transformer 借来的；两者是**独立地走到了同一个 idea**。

### 6. 贡献三：Boundary Refinement（边界细化，Multi-scale Gaussian Diffusions）

#### 6.1 问题：边界像素与内部像素需要不同尺度

- **内部像素（远离边界）**：它属于哪一类很明确，用**大尺度**信息更可靠——看得越多，判断越稳。
- **边界像素（靠近两类交界）**：如果用一个大的方形窗口，窗口会**同时覆盖边界两侧**；两侧像素收集到的信息**几乎一样**，因此**无法准确判断边界到底在哪一侧**。
- 结论：**边界附近必须用很小的尺度（small scale）**，才能区分两侧的细微差异；**远离边界才用大尺度**。
- 问题变成：**如何自动地、逐像素地决定"用哪个尺度"？** 不能人工设计，因为边界位置随每张输入图像而变。

#### 6.2 Multi-scale Gaussian Diffusion 的做法

> PDF p.313 只给出示意图；下面的公式是按老师课堂讲解整理的数学表达。

1. **先得到粗略分割结果（rough segmentation）**：网络先输出一个大致的分割图。
2. **从粗分割提取粗略边界（rough boundary）**：两类标签交界处的像素即为边界。
3. **把边界看成冲激（impulse）**：沿一条**穿过边界**的直线采样，边界位置的值是 1，其他位置是 0——这是一个 **1D impulse**。
4. **用不同标准差 $\sigma$ 的 Gaussian 核去平滑这个 impulse**：

   $$
   g_\sigma(d)=\frac{1}{\sqrt{2\pi}\,\sigma}\exp\!\left(-\frac{d^{2}}{2\sigma^{2}}\right)
   $$

   其中 $d$ 是到粗略边界的距离。不同 $\sigma$ 得到**不同宽度的扩散曲线**（PDF p.313 的蓝/中/黄三条曲线）。
5. **用曲线值作为不同尺度的权重**：

   $$
   w_s(d)=\frac{g_{\sigma_s}(d)}{\sum_{s'}g_{\sigma_{s'}}(d)},\qquad
   \mathbf{S}(p)=\sum_{s}w_s\!\left(d_p\right)\mathbf{s}_s(p)
   $$

   - 靠近边界（$d$ 小）：小 $\sigma$ 的曲线值相对大 → **small scale 权重大**；
   - 远离边界（$d$ 大）：大 $\sigma$ 的曲线衰减慢、值相对大 → **large scale 权重大**。

- ⚠️ 这套权重同样是 **input-dependent** 的：每张图的粗分割不同 → 边界位置不同 → $d_p$ 不同 → 权重不同。**不是训练后固定的参数。**

| 像素位置 | 到边界距离 $d$ | 主导尺度 | 原因 |
|---|---|---|---|
| 物体内部 | 大 | **large scale** | 大窗口信息更可靠，不易受噪声影响 |
| 边界附近 | 小 | **small scale** | 大窗口会跨过边界，两侧信息混在一起，无法定位 |

### 7. Shape-Variant Convolution（形状可变卷积，CVPR'19 Oral）

#### 7.1 固定方形 kernel 的根本问题

- 传统 convolution 的 kernel 是**固定的方形窗口**（3×3、5×5、7×7……）。
- 考虑两个像素 $A$ 与 $B$：它们**空间上离得很远**，但**分别位于边界两侧**（例如 $A$ 在湖里，$B$ 在陆地上）。
- 如果用一个**很大的方形 kernel**，$A$ 的窗口与 $B$ 的窗口会**大量重叠** → 两个输出**几乎一样** → 网络无法区分 $A$ 与 $B$ 属于不同类别。
- 这不是靠"再加几层"就能解决的：只要 kernel 是固定方形，边界两侧的大窗口就必然重叠。

#### 7.2 理想情况：kernel 形状随物体形状自适应

- 理想的 kernel 应该**贴合物体的形状（shape-adaptive）**：
  - 对湖里的像素 $A$，kernel 主要覆盖**湖面**；
  - 对陆地上的像素 $B$，kernel 主要覆盖**陆地**。
- 这样 $A$ 与 $B$ 的输出就会**完全不同**，边界两侧才能被正确区分。
- PDF p.314 把 context 分成两类：
  - **Spatial-Dependent Context**：用**预定义窗口**（如红色矩形）收集固定邻域；
  - **Semantic-Dependent Context**：窗口形状**随语义相关性变化**（variant shapes according to the semantic correlation）。

#### 7.3 如何生成形状掩码（shape mask）

> PDF p.314–316 主要是示意图；下面的公式是按老师课堂讲解整理的数学表达。

老师的做法：

1. **先用 1×1 convolution 生成每个像素的 feature**（不改变空间位置，只做跨 channel 融合）。
2. **计算中心像素与所有其他像素的 correlation（相关）**：
   对中心像素 $p$ 和任意像素 $q$，计算它们 feature 的**点积**：

   $$
   c(p,q)=\mathbf{f}(p)^{T}\mathbf{f}(q)
   $$

   这得到一个 **correlation map / attention map**：值越大，说明 $q$ 与 $p$ 越相关（越可能属于同一物体）。
3. **由 correlation map 生成 shape mask** $\mathbf{M}(p,q)$：把相关性高的像素保留在 kernel 内，相关性低的排除在外。
4. **用 shape mask 去加权一个大方形 kernel**：

   $$
   \mathbf{W}_{\text{eff}}(p,q)=\mathbf{M}(p,q)\odot\mathbf{W}_{\text{sq}}(q-p),
   \qquad
   y(p)=\sum_{q}\mathbf{W}_{\text{eff}}(p,q)\,x(q)+b
   $$

   等价地，也可以把 mask 直接乘在输入上——数学上是一样的。
5. **效果**：等效 kernel 的形状不再固定为方形，而是**随输入图像中物体的形状变化**。PDF p.316 的 "Four Visual Examples Shape Mask" 展示了车、道路、草地等不同区域生成的 mask：同一物体的像素权重高，不相关区域权重低。

#### 7.4 审稿人的质疑与老师的 rebuttal

- **质疑**：卷积本身就是 weighted sum；你现在再乘一个 mask，不过是**又加了一层 weight**。这有什么本质区别？
- **老师 rebuttal**：
  - **convolution 的权重**：从**整个 training data** 学出来，训练后**固定**；对所有 input 都一样。
  - **shape mask**：由**individual input image** 生成；不同图像 → 不同 mask → 不同权重。
  - 所以两者**完全不同**：一个是 **learned & fixed**，一个是 **input-generated & adaptive**。
- ⚠️ 这个 rebuttal 与 §5 的 gated sum 完全一致，也是理解 Transformer attention 的钥匙。

#### 7.5 ⭐ 与 attention 的关系：shape mask 就是 attention map

- 老师原话（转写修正）：**"The attention and the correlation are exactly the same, no difference, only different name."**
- 在这个工作中：
  - **correlation map** = 像素之间的相关；
  - **shape mask** = 用相关生成的权重图；
  - 这两者在 Transformer 里就叫 **attention map**。
- 所以老师把 §4–§7 放在 Transformer 之前讲，是**刻意铺垫**：
  1. **gated sum**：用 input 生成多尺度融合权重；
  2. **boundary refinement**：用 input 的粗分割生成尺度权重；
  3. **shape-variant convolution**：用 input 的像素相关生成 kernel mask；
  4. **Transformer attention**：用 input 的 Q/K 相关生成 token 权重。
- 四者共享同一个核心：**weighted sum 的权重由具体 input 生成，而不是训练后固定**。

> ⚠️ PDF p.317 还有一页 **"Labeling De-noising in Decoding Process"**（高层 error 偏位置不准、低层 error 偏类别噪声；用不同层的分类结果去噪），但老师课堂明确说 **"This one I skip"**，本周未展开；考试也不在重点范围内。

**本部分参考文献**（PDF p.310、p.314）：

- H. Ding, X.D. Jiang, B. Shuai, A. Liu, G. Wang, "Context Contrasted Feature and Gated Multi-scale Aggregation for Scene Segmentation," **CVPR Oral 2018**.
- H. Ding, X. Jiang, B. Shuai, A. Liu, G. Wang, "Semantic Segmentation with Context Encoding and Multi-Path Decoding," **IEEE Transactions on Image Processing (TIP), 2020**.
- H. Ding, X. Jiang, B. Shuai, A. Liu, G. Wang, "Semantic Correlation Promoted Shape-Variant Context for Segmentation," **CVPR'19 Oral, 2019**.

### 8. 从 CNN 到 Transformer：Topic 10 的三个问题

#### 8.1 Transformer 的定位

- **Transformer** 是一个 **sequence-to-sequence** 的神经网络结构：输入一个 **sequence（序列）**，输出另一个 sequence。
  - 序列可以是 **speech（语音）**、**text（文本）**、**time series（时间序列）**，也可以是图像的 **patch/token 序列**。
- 在 Transformer 之前，处理序列的主流模型是 **RNN（recurrent neural network，循环神经网络）** 及其改进 **LSTM（long short-term memory，长短期记忆网络）**。
  - RNN/LSTM 必须**一个 token 一个 token 顺序处理**（sequential），难以并行。
  - Transformer 的关键优势：**把所有 token 并行（parallelly）处理** → 训练更快、效果更好。
- Transformer 最初为 **NLP（natural language processing，自然语言处理）** 发明；现在也被引入 **computer vision**，并在很多任务上超过 CNN。
- 力量来源：**Attention module（注意力模块）**——捕捉序列中**每个 word/token 与其余所有 token 的关系**。
- 原始论文：**"Attention Is All You Need"**（Google 团队，NeurIPS 2017）。

#### 8.2 PDF p.319 提出的三个问题

1. **Transformer 到底怎么工作？Is attention really everything?**（真的只需要 attention，别的都不需要？）
2. **它与 CNN 有什么关系？**
3. **能否简单地说："CNN 只捕捉 local information，而 Transformer 捕捉 global information，所以 Transformer 更强"？**

⚠️ 老师对第 3 个问题的回答是**明确的"不能"**（详见 §8.3）。这也是 Week 8 §10.5 已经埋下的伏笔。

#### 8.3 ⭐ 驳斥 "local vs global" 的解释

| 流行说法 | 老师的反驳 |
|---|---|
| "CNN 只捕捉 local information，所以有局限" | ⚠️ **错**。单层 convolution 确实只看局部，但 CNN 可以有**几百层**；每层感受野逐层扩大（§2.2），最后输出**已经覆盖几乎整幅输入图像**。所以"CNN 只看局部"只在单层意义下成立，对深层 CNN 不成立。 |
| "Transformer 捕捉 global information，所以更强" | ⚠️ **不充分**。如果真的"global 就一定好"，那么 **MLP 本来就是 fully connected（全连接 = 完全 global）**，理应最强；但 MLP 恰恰**表现最差**（overfitting）。 |
| — | ⚠️ 老师的正面解释：**CNN 的 global information 是从整个 training dataset 学出来的**（PDF p.320 原话："Global information learnt by CNN is on the whole training dataset."）；而 **Transformer 的 global information 是由具体 test input 动态生成的**。两者的差别不在 "local vs global"，而在 **权重是否随 input 自适应**。 |

#### 8.4 ⭐ 三种 weighted sum 的本质对比（本周最核心的一张表）

| 模型 | 输出形式 | 权重来源 | 训练后权重是否固定？ | 能否适应不同 input？ |
|---|---|---|---|---|
| **MLP** | $o_j=\sum_i w_{ji}x_i$ | 从 **training data** 学 | ✅ 固定 | ❌ 对所有 input 用同一组权重 |
| **CNN** | $o_j=\sum_i w_i x_{j-i}$ | 从 **training data** 学，空间共享 | ✅ 固定 | ❌ 对所有 input 用同一组 filter |
| **Transformer attention** | $z_i=\sum_j a_{ij}\mathbf{v}_j$ | **由当前 input 的 Q/K 计算** | ❌ **不固定** | ✅ 不同 input → 不同 $a_{ij}$ |

- ⚠️ 老师把这一点称为 Transformer 的 **revolution**：**"The weighted sum is performed with weights generated by the individual input, not learned from the training data."**
- 也正因如此，Transformer 能**adapt to the input**：即使 test input 有很多 variation，它仍能表现良好，因为每次都会**重新生成**一组适合当前输入的权重。

### 9. Transformer 总体结构：Encoder + Decoder

#### 9.1 整体架构

- Transformer = **一个 encoder stack（编码器堆叠）** + **一个 decoder stack（解码器堆叠）**。
- 每个 stack 内的 encoder/decoder **结构完全相同**；可以有几个、几十个甚至上百个。因此**只需要研究一个 encoder 和一个 decoder**。
- 数据流：
  1. 输入 sequence 的所有 token **并行**送入第一个 encoder；
  2. 第一个 encoder 的输出送入第二个 encoder……直到最后一个 encoder；
  3. **最后一个 encoder 的输出**作为 **Key 与 Value**，送入**每一个 decoder**；
  4. decoder 还接收**前一个 decoder 的输出 / 已生成的 token**；
  5. 最后一个 decoder 的输出经过一个**简单的 linear classification**，得到下一个 token。

- PDF p.321 的机器翻译例子：输入一句英文，输出另一种语言的译文；所有 word/token **parallelly** 输入，输出是 decoder 输出的**线性分类**。

#### 9.2 Encoder 内部结构

一个 encoder block 只有两个主函数（PDF p.323、p.327）：

| 顺序 | 模块 | 作用 |
|---|---|---|
| 1 | **Self-attention（自注意力）** | 让每个 token 关注**同一序列中的所有 token**，捕捉上下文关系 |
| 2 | **Add & Norm（残差 + 归一化）** | $\mathbf{x}\leftarrow\mathrm{Norm}(\mathbf{x}+\mathrm{SelfAttn}(\mathbf{x}))$ |
| 3 | **Pointwise feed-forward network（逐点前馈网络）** | 对每个 token **独立**做非线性变换 |
| 4 | **Add & Norm** | $\mathbf{x}\leftarrow\mathrm{Norm}(\mathbf{x}+\mathrm{FFN}(\mathbf{x}))$ |

- ⚠️ **self-attention 的 Q、K、V 都来自同一个输入序列**——所以叫 "self"（自己关注自己）。
- ⚠️ 每个子层（attention / FFN）外面都包着 **residual skip-connection（残差跳连）**，后面接 **normalization**（PDF 原话："Both the Attention and Feed-forward layers have a residual skip-connection."）。

#### 9.3 Decoder 内部结构

一个 decoder block 比 encoder 多一个 attention（PDF p.323、p.328）：

| 顺序 | 模块 | Q 来自 | K, V 来自 | 作用 |
|---|---|---|---|---|
| 1 | **Self-attention** | decoder 当前输入（已生成的 token） | 同左 | 让已生成的部分互相看 |
| 2 | **Add & Norm** | — | — | — |
| 3 | **Encoder-Decoder attention（交叉注意力）** | decoder self-attention 的输出 | **最后一个 encoder 的输出** | 让 decoder 在生成时"查询"输入序列 |
| 4 | **Add & Norm** | — | — | — |
| 5 | **Pointwise feed-forward network** | 每个 token 独立 | — | 非线性变换 |
| 6 | **Add & Norm** | — | — | — |

- ⚠️ 三种 attention（encoder self-attention、decoder self-attention、encoder-decoder attention）的**内部计算完全相同**；**唯一的区别是 Q/K/V 的来源不同**。
- 老师原话："Although the names are different, the structure of this attention is also identical to self-attention. The difference is only the input."

#### 9.4 Encoder vs Decoder 对比

| 对比项 | Encoder | Decoder |
|---|---|---|
| attention 数量 | 1 个 self-attention | 2 个：self-attention + encoder-decoder attention |
| Q/K/V 来源 | 全部来自 encoder 输入 | self-attention：全来自 decoder；cross-attention：Q 来自 decoder，K/V 来自 encoder |
| 是否生成输出 | 否，只编码 | 是，逐个生成 token |
| 是否使用位置编码 | 是 | 是 |
| 输出用途 | 送入所有 decoder 的 K/V | 经 linear classifier 得到下一个 token |

### 10. 输入表示：Token → Embedding → Matrix

#### 10.1 从 token 到 feature vector

- **Token**：序列中的一个基本单位。NLP 中是一个 word / sub-word；CV 中可以是图像的一个 **patch**。
- 最朴素的做法：给每个 token 一个**不同的整数编号**。⚠️ 老师指出这**不够好**：整数编号无法表达语义相似性——"cat" 和 "dog" 的编号可能相差很远，但语义很近；编号大小也没有物理意义。
- 正确做法：**embedding（嵌入）**——把每个 token 映射成一个**feature vector（特征向量）**：

  $$
  \mathbf{x}_i=\mathrm{Embed}(w_i)\in\mathbb{R}^{K}
  $$

  - 语义相近的 token，其 feature vector 在空间中**距离近**；语义远的距离远。
  - 标准 Transformer 中 $K=512$（老师课堂举例；实际模型可不同）。
  - 这样"距离"才有意义，后续的 dot product / attention 才有物理含义。

#### 10.2 Positional encoding（位置编码）

- 只有 token 的 embedding 还不够：不加 positional encoding 时，attention 对 token 顺序是 **permutation-equivariant（置换等变）** 的——把 token 打乱，输出只跟着同样打乱，模型**无法区分谁在前谁在后**。
- 因此要给每个位置 $i$ 再加一个 **positional encoding vector（位置编码向量）** $\mathbf{p}_i$：

  $$
  \mathbf{x}_i=\mathrm{Embed}(w_i)+\mathbf{p}_i
  $$

- 这样 feature vector 同时包含**语义信息**（word meaning）与**位置信息**（第几个 token）。
- ⚠️ 老师课堂没有展开正弦/余弦位置编码的公式，只强调"**位置也要用 feature vector 表示，再与词义 vector 相加**"。

#### 10.3 矩阵表示（贯穿 Transformer 的核心）

把所有 token 的 feature vector 按行排成矩阵：

$$
\mathbf{X}=
\begin{bmatrix}
\mathbf{x}_1\\
\mathbf{x}_2\\
\vdots\\
\mathbf{x}_N
\end{bmatrix}
\in\mathbb{R}^{N\times K}
$$

- **一行 = 一个 token**；$N$ 个 token，每个 $K$ 维。
- ⚠️ 老师反复强调：**"In this matrix, one row is one token. This is very, very important — never be confused."**
- Transformer 内部所有运算都是**矩阵乘法**；**这个矩阵的大小（$N\times K$）在整个 Transformer 中保持不变**（除非显式做投影改变特征维，但 token 数 $N$ 不变）。
- 因此理解 Transformer 的关键，就是理解**每一步矩阵乘法到底对"行（token）"和"列（feature）"做了什么**。

| 表示 | 形状 | 含义 |
|---|---|---|
| 一个 token | $1\times K$ 行向量 | 一个 word / patch 的特征 |
| 整个输入 $\mathbf{X}$ | $N\times K$ | $N$ 个 token 的 feature 矩阵 |
| $\mathbf{Q},\mathbf{K},\mathbf{V}$ | $N\times K$ | 每个 token 的三个投影向量，仍是一行一个 token |
| attention 输出 $\mathbf{Z}$ | $N\times K$ | 每个 token 的新 feature，一行一个 token |

### 11. Residual Connection（残差连接 / Skip Connection）

#### 11.1 定义

Transformer 的**每一个** attention / feed-forward 子层都使用 **residual connection**：

$$
\boxed{\;\mathbf{y}=\mathbf{x}+F(\mathbf{x})\;}
$$

- $\mathbf{x}$：子层的输入；
- $F(\mathbf{x})$：子层（attention 或 FFN）学到的变换；
- $\mathbf{y}$：子层输出（再过 normalization）。

#### 11.2 为什么残差连接重要

- 把上式改写：

  $$
  F(\mathbf{x})=\mathbf{y}-\mathbf{x}
  $$

  即：**子层只需要学习"输出相对于输入的差异（residual，残差）"，而不是从头学习整个输出。** 老师原话："The output of this unit is just the difference between the final output and the input. This makes the training easier."

- **梯度视角**（为什么能训练很深）：

  $$
  \frac{\partial\mathbf{y}}{\partial\mathbf{x}}
  =\mathbf{I}+\frac{\partial F(\mathbf{x})}{\partial\mathbf{x}}
  $$

  反向传播时，梯度中永远包含一个 **identity term（恒等项）$\mathbf{I}$**，可以直接从深层流回浅层，**不会因为连乘而消失** → 缓解 **vanishing gradient（梯度消失）**。

- **集成视角**：残差连接让网络可以"跳过"某些层；如果某一层没用，网络可以把 $F(\mathbf{x})$ 学成 0，等价于**恒等映射**，不会变差。

#### 11.3 与 ResNet 的关系

- 这个思想来自 **ResNet（residual network，残差网络）**。
- ResNet 用 **skip connection** 把输入直接加到卷积输出上，使 100+ 层的网络可以稳定训练；Transformer 把同一思想用在 attention / FFN 子层上。
- ⚠️ 注意区分：
  - **ResNet 的 skip connection**：连接的是**同一个 block 的输入与输出**；
  - **Transformer 的 residual connection**：连接的是**同一个子层的输入与输出**；
  - 两者数学形式相同，都是 $\mathbf{y}=\mathbf{x}+F(\mathbf{x})$。

### 12. ⭐⭐ Self-Attention 的计算（本周最核心）

#### 12.1 第一步：Q / K / V 线性投影

给定输入矩阵 $\mathbf{X}\in\mathbb{R}^{N\times K}$，用**三个可学习的权重矩阵**做线性投影：

$$
\boxed{\;\mathbf{Q}=\mathbf{X}\mathbf{W}_q,\qquad
\mathbf{K}=\mathbf{X}\mathbf{W}_k,\qquad
\mathbf{V}=\mathbf{X}\mathbf{W}_v\;}
$$

逐 token 写：

$$
\mathbf{q}_i=\mathbf{x}_i\mathbf{W}_q,\qquad
\mathbf{k}_i=\mathbf{x}_i\mathbf{W}_k,\qquad
\mathbf{v}_i=\mathbf{x}_i\mathbf{W}_v,\qquad i=1,2,\ldots,N
$$

| 符号 | 名称 | 含义 |
|---|---|---|
| $\mathbf{Q}$ | **Query（查询）** | 当前 token "想找什么" |
| $\mathbf{K}$ | **Key（键）** | 每个 token "能被什么找到" |
| $\mathbf{V}$ | **Value（值）** | 每个 token "实际提供的内容" |
| $\mathbf{W}_q,\mathbf{W}_k,\mathbf{W}_v$ | 可学习投影矩阵 | 从 training data 学出来 |

- ⚠️ **所有 token 共享同一套 $\mathbf{W}_q,\mathbf{W}_k,\mathbf{W}_v$**：第 $i$ 个 token 的 $\mathbf{q}_i$ 只由 $\mathbf{x}_i$ 与**同一个** $\mathbf{W}_q$ 决定。
- 这正是 PDF p.331 的原话："**All tokens share the same learnable parameter: any single learnable parameter goes through all tokens or is learned from all tokens. 1×1 Convolution of CNN!**"
- 换句话说：Q/K/V 投影就是**对每个 token 做一次 1×1 convolution**——Transformer 的可学习部分仍然沿用 CNN 的 parameter sharing 思想。

#### 12.2 第二步：Attention score = Q 与 K 的点积

$$
\boxed{\;\mathbf{R}=\mathbf{Q}\mathbf{K}^{T}\;}
$$

- $\mathbf{R}\in\mathbb{R}^{N\times N}$，第 $(i,j)$ 个元素：

  $$
  r_{ij}=\mathbf{q}_i\cdot\mathbf{k}_j=\sum_{d=1}^{K}q_{i,d}\,k_{j,d}
  $$

- **物理意义**：$\mathbf{q}_i$ 与 $\mathbf{k}_j$ 的**点积 = 相似度 / 相关性（similarity / correlation）**。值越大，说明 token $i$ 与 token $j$ 越相关，$j$ 对 $i$ 越重要。
- ⚠️ **与 covariance matrix 的类比**（PDF p.332 原话："Covariance Matrix!!!"）：
  - $\mathbf{Q}\mathbf{K}^{T}$ 的形状与 $\mathbf{X}\mathbf{X}^{T}$ 一样，都是 $N\times N$ 的 **Gram / correlation matrix**；
  - 区别在**求和的维度语义**：covariance 通常对**样本**求和，而 attention 是对**同一对 token 的 feature 维**求和；
  - 老师强调："Attention is just the same as correlation. Nothing new."——**attention 没有发明新的数学，只是给"相关矩阵"换了个名字。**

#### 12.3 第三步：归一化（softmax + scaling）

- 老师课堂明确说：在 $\mathbf{Q}\mathbf{K}^{T}$ 之后、乘 $\mathbf{V}$ 之前，要做**归一化**；但"**this normalization is very simple, it does not change any physical meaning**"，所以没有展开。
- 标准写法是 **softmax（归一化指数函数）** 加 **$\sqrt{d_k}$ 缩放**：

  $$
  \mathbf{A}=\mathrm{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^{T}}{\sqrt{d_k}}\right),
  \qquad
  a_{ij}=\frac{\exp\!\left(r_{ij}/\sqrt{d_k}\right)}{\sum_{j'=1}^{N}\exp\!\left(r_{ij'}/\sqrt{d_k}\right)}
  $$

  - softmax 让每行的权重**非负且和为 1** → 成为真正的"加权平均"；
  - $\sqrt{d_k}$ 防止 $d_k$ 很大时点积数值过大、softmax 饱和。
- ⚠️ **PDF 的写法省略了 softmax 与 scaling**，直接写 $\mathbf{Z}=\mathbf{Q}\mathbf{K}^{T}\mathbf{V}$；这是**简化表述**，考试若要求严格公式，应写 softmax 版本，并注明老师课件的简化形式。

#### 12.4 第四步：用 attention 权重对 Value 加权求和

$$
\boxed{\;\mathbf{Z}=\mathbf{Q}\mathbf{K}^{T}\mathbf{V}\quad\text{（PDF 简化式）}\;}
$$

严格写法：

$$
\mathbf{Z}=\mathbf{A}\mathbf{V},\qquad
\mathbf{z}_i=\sum_{j=1}^{N}a_{ij}\,\mathbf{v}_j
$$

逐项展开（PDF p.335）：

$$
\mathbf{z}_i=\sum_{j=1}^{N}\left(\mathbf{q}_i\cdot\mathbf{k}_j\right)\mathbf{v}_j
\quad\text{（未归一化版本）}
$$

- ⚠️ **核心解读**（老师反复讲）：
  1. **每个输出 token $\mathbf{z}_i$ 都是所有输入 token 的 weighted sum** → 从第一层开始就**捕捉 global information**（不是像 CNN 那样逐层扩大感受野）。
  2. **权重 $a_{ij}$ 是 token $i$ 与 token $j$ 的相关性**：$j$ 与 $i$ 越相关，$j$ 的 Value 对 $i$ 的输出贡献越大。
  3. 因此 attention 的输出是**所有 token 的线性组合（linear combination）**，组合系数由当前输入决定。

#### 12.5 ⭐⭐ 最关键的区别：attention 权重不是学出来的

> **PDF p.334 原话**："Each output token is weighted sum of all input tokens, capturing global information. **Different from MLP and CNN, weights are not learnt by training data. They are flexibly generated by specific test input. Attention itself is not learnable.**"

这句话要拆成两层理解，**考试极易混淆**：

| 成分 | 是否可学习？ | 说明 |
|---|---|---|
| $\mathbf{W}_q,\mathbf{W}_k,\mathbf{W}_v$ | ✅ **可学习** | 从 training data 学，训练后固定；所有 token 共享 |
| attention weights $\mathbf{A}$（即 $a_{ij}$） | ❌ **不可学习** | 由当前 input 的 $\mathbf{Q}\mathbf{K}^{T}$ **现场计算**出来；不同 input → 不同 $\mathbf{A}$ |
| feed-forward 的 $\mathbf{W}_1,\mathbf{W}_2,\mathbf{W}_3$ | ✅ **可学习** | 从 training data 学，所有 token 共享 |

- 所以"**attention itself is not learnable**"指的是：**没有一组"attention 参数"被训练出来**；attention 权重是**前向计算时由 Q/K 现算的**。
- ⚠️ 但要注意：$\mathbf{A}$ 依赖可学习的 $\mathbf{W}_q,\mathbf{W}_k$，所以训练会**间接影响** $\mathbf{A}$ 的分布；老师强调的是 **$\mathbf{A}$ 没有自己独立的、训练后固定的参数**，而不是"训练对 $\mathbf{A}$ 完全没影响"。
- ⚠️ 这与 MLP/CNN 的本质区别：
  - MLP/CNN：权重在**训练时**确定，**推理时对所有 input 都一样**；
  - Transformer：Q/K/V 投影在训练时确定，但**最终的加权系数在推理时由每个 input 重新生成**。
- 老师把这一点视为 Transformer 的 **revolution**：网络可以 **adapt to the input**，因此对输入的变化（different variations）更 robust。

#### 12.6 一个直观例子

- 输入 "Hi how are you?"，输出 "I am fine."（PDF p.337 的 generative 示例）。
- attention 会发现：
  - 输入中的 "how" 与输出中的 "fine" 高度相关（问候 → 回答）；
  - 输入中的 "you" 与输出中的 "I" 高度相关（问答双方对应）。
- 虽然 "you" 在输入中是**最后一个 token**，"I" 在输出中是**第一个 token**，attention **不受位置限制**——它会计算**所有 token 对**的相关性。这正是 attention 相对 RNN 的优势：**不需要按顺序一步步传递信息**。

### 13. Multi-head Attention（多头注意力）

#### 13.1 做法

- 只做一次 attention 可能只捕捉一种"关系"；**multi-head attention** 用**多组不同的投影矩阵**并行做多次 attention：

$$
\mathrm{head}_m=\mathrm{Attention}\!\left(\mathbf{X}\mathbf{W}_q^{(m)},\mathbf{X}\mathbf{W}_k^{(m)},\mathbf{X}\mathbf{W}_v^{(m)}\right),
\qquad m=1,2,\ldots,h
$$

$$
\mathrm{MultiHead}(\mathbf{X})=\mathrm{Concat}\left(\mathrm{head}_1,\ldots,\mathrm{head}_h\right)\mathbf{W}_o
$$

- 每组 $\mathbf{W}_q^{(m)},\mathbf{W}_k^{(m)},\mathbf{W}_v^{(m)}$ 都从 training data 学；**不同 head 学到不同的"关注方式"**（例如一个 head 关注语法关系、一个关注语义相似、一个关注位置邻近……）。
- 最后把所有 head 的输出 **拼接（concatenate）**，再用 $\mathbf{W}_o$ 投影回一个矩阵。

#### 13.2 老师的课堂表述

- 转写中的 "mutate / match attention" = **multi-head attention**。
- 老师原话大意："Given a single input matrix, we can generate **three copies** (Q/K/V); of course we can generate **six copies, nine copies, twelve copies**. Then each three copies perform one attention; finally we merge the outputs into one matrix."
- PDF p.329："Multiple attention heads in each encoder and decoder."
- ⚠️ 每个 head 的 Q/K/V 仍然是 **1×1 convolution**（所有 token 共享该 head 的投影参数）。

### 14. Pointwise Feed-forward Network（逐点前馈网络）

#### 14.1 结构

attention 输出 $\mathbf{Z}$ 之后，接一个**逐 token 独立**的前馈网络：

$$
\boxed{\;\mathbf{Y}=h\!\left(h\!\left(h\!\left(\mathbf{Z}\mathbf{W}_1\right)\mathbf{W}_2\right)\mathbf{W}_3\right)\;}
$$

逐 token 写：

$$
\mathbf{y}_i=h\!\left(h\!\left(h\!\left(\mathbf{z}_i\mathbf{W}_1\right)\mathbf{W}_2\right)\mathbf{W}_3\right),
\qquad i=1,2,\ldots,N
$$

- $h(\cdot)$ 是**非线性激活函数**，PDF 明确说中间使用 **ReLU**。
- 通常有两层线性变换 + 一个 ReLU（PDF 写三层矩阵，是为了强调"可以堆多层"；标准 Transformer 是两层 linear + 一层 ReLU）。

#### 14.2 ⭐ 为什么叫 "pointwise"，为什么不是 MLP

| 特性 | MLP | Transformer 的 pointwise FFN |
|---|---|---|
| 输出与输入的关系 | 每个输出是**所有输入**的 weighted sum | 每个输出 token **只依赖自己的输入 token** |
| 是否跨 token 混合 | ✅ 是（全连接） | ❌ 否（逐 token 独立） |
| 参数共享 | ❌ 无共享（每个输出有自己的权重行） | **所有 token 共享同一套 $\mathbf{W}_1,\mathbf{W}_2,\mathbf{W}_3$** |
| 等价操作 | 全连接 | **1×1 convolution**（沿 token 维逐点） |

- ⚠️ PDF p.336 原话："**Feed-forward network of the transformer is Pointwise, which is not MLP. Pointwise means that each single learnable parameter goes through all inputs. It comes again from the key concept, 1×1 convolution of CNN.**"
- ⚠️ 老师特别批评 ViT 原论文：**"This paper calls this feed-forward network as MLP. In my opinion, it is wrong. It's not MLP."** 原因就是：MLP 的输出混合所有输入，而这里每个 token 独立处理，只是参数共享——本质是 **1×1 convolution**。

### 15. Encoder-Decoder Attention 与生成过程

#### 15.1 Encoder-Decoder Attention（交叉注意力）

- 在 decoder 的 cross-attention 中：
  - **Query** 来自 decoder 下方的 **self-attention 输出**；
  - **Key 与 Value** 来自**最后一个 encoder 的输出**。
- 公式与 self-attention **完全相同**：

  $$
  \mathbf{Z}=\mathbf{Q}\mathbf{K}^{T}\mathbf{V}
  \qquad\text{（简化式）}
  $$

  $$
  \mathbf{z}_i=\sum_{j}\left(\mathbf{q}_i\cdot\mathbf{k}_j\right)\mathbf{v}_j
  $$

- 物理意义：decoder 在生成每个 token 时，用当前的 Query 去**查询输入序列的所有 token（Key/Value）**，从而决定"现在应该关注输入的哪一部分"。
- 机器翻译例子：生成西班牙语 "La bola es azul" 时，生成 "bola" 的 Query 会去关注英文输入 "The ball is blue" 中的 "ball"。

#### 15.2 生成过程（Transformer is a generative model）

- Transformer 是**自回归（autoregressive）**的生成模型：**一次生成一个 token**，然后把新生成的 token **追加到 decoder 输入**，再生成下一个。
- 流程：
  1. 输入 sequence 送入 encoder，得到固定不变的 encoder 输出；
  2. decoder 先根据 encoder 输出 + 起始 token，生成**第一个**输出 token；
  3. 把第一个输出 token 作为 decoder 的新输入，生成**第二个** token；
  4. 重复，直到生成结束符或达到最大长度。
- ⚠️ **encoder 的输出在每一步都相同**；变化的只是 decoder 已经生成的 token 序列。
- PDF p.337 把整体写成：

  $$
  \mathbf{Y}=f\!\left(f\!\left(f\!\left(\mathbf{Z}\mathbf{W}_1\right)\mathbf{W}_2\right)\mathbf{W}_3\right)
  $$

  其中 $\mathbf{Z}=\mathbf{Q}\mathbf{K}^{T}\mathbf{V}$，$\mathbf{Q}=\mathbf{X}\mathbf{W}_q,\ \mathbf{K}=\mathbf{X}\mathbf{W}_k,\ \mathbf{V}=\mathbf{X}\mathbf{W}_v$。

| 阶段 | 输入 | 输出 | 说明 |
|---|---|---|---|
| **Training** | 完整输入序列 + 完整目标序列（teacher forcing） | 每个位置的预测 | 可并行计算所有位置的 loss |
| **Inference** | 输入序列 + 已生成的前缀 | 下一个 token | 逐个生成，不能并行 |

### 16. ⭐⭐ MLP vs CNN vs Transformer：三代模型的本质对比

#### 16.1 总表

| 对比维度 | **MLP** | **CNN** | **Transformer** |
|---|---|---|---|
| **基本运算** | fully-connected weighted sum | convolution（local weighted sum + channel 求和） | **attention（global weighted sum）** + pointwise FFN |
| **权重来源** | 从 training data 学 | 从 training data 学，空间共享 | Q/K/V 投影与 FFN 从 training data 学；**attention 权重由 test input 现算** |
| **训练后权重是否固定** | ✅ 固定 | ✅ 固定 | ⚠️ **投影/FFN 固定，attention 权重不固定** |
| **能否适应不同 input** | ❌ | ❌ | ✅ **不同 input → 不同 attention 权重** |
| **感受野 / 范围** | 全连接（global） | 单层 local；**多层后覆盖整图** | **第一层就覆盖所有 token（global）** |
| **参数共享** | 无（每个输出位置独立权重） | **filter 在所有空间位置共享** | **投影/FFN 在所有 token 上共享** |
| **正则化方式** | 无 → 容易 overfit | **parameter sharing 强正则** | parameter sharing + **input-adaptive attention** |
| **位置信息** | 无显式位置概念 | 由空间结构隐式表示 | 需要 **positional encoding** |
| **典型 overfitting 表现** | 最严重（double spiral） | 被 parameter sharing 抑制 | attention 随 input 变化，泛化更强 |
| **典型应用** | 传统分类/回归 | 图像分类、检测、分割 | NLP、ViT、多模态 |

#### 16.2 三代模型的演进逻辑

$$
\text{MLP（自由权重 → overfit）}
\;\longrightarrow\;
\text{CNN（parameter sharing → 强正则）}
\;\longrightarrow\;
\text{Transformer（input-adaptive attention → 自适应）}
$$

- **MLP**：每个输出位置有独立权重，自由度最大，但最容易 overfit；理论上是 universal approximator，实践中崩。
- **CNN**：用 **parameter sharing** 强制所有位置共享同一组 filter，大幅减少自由度 → 强正则 → 学到 general rule。这是 CNN 成功的真正原因（Week 8 §10）。
- **Transformer**：在保留 parameter sharing（Q/K/V、FFN 都是 1×1 convolution）的同时，让**加权系数由 input 动态生成** → 既能学 general rule，又能**适应每个具体输入**。

#### 16.3 "Is attention really everything?" 的答案

- **attention 是 Transformer 的力量来源**：它让每个输出 token 成为所有输入 token 的加权和，权重由 input 的相关性决定。
- **但 attention 不是"全部"**：
  1. **Q/K/V 投影、FFN** 仍然是可学习的，而且本质上都是 **1×1 convolution**；
  2. **residual connection** 保证深层可训练；
  3. **positional encoding** 提供顺序信息；
  4. **multi-head** 让模型同时关注多种关系；
  5. **encoder-decoder 结构** 支持 sequence-to-sequence 生成。
- 老师更准确的说法是：**"Attention 是 Transformer 区别于 MLP/CNN 的关键，但 Transformer 的可学习模块仍然沿用 CNN 的 convolution 思想。"**（PDF p.341 最后一条）

### 17. ViT 与 Vision-Language Transformer

#### 17.1 Vision Transformer (ViT)：把图像变成 token 序列

- Transformer 的输入必须是 **sequence of tokens**；图像是 **2D 网格**，所以第一步是**把图像转成序列**。
- ViT 的做法非常直接：
  1. 把图像**切成固定大小的 patch**（例如 $16\times16$）；
  2. 把每个 patch 内的所有像素**展平（flatten）**成一个向量；
  3. 每个 patch 的向量 = 一个 **token**；
  4. 加上 **positional encoding**；
  5. 送入 **Transformer encoder**；
  6. 最后接一个 **linear classifier**，输出图像类别。
- 公式：

  $$
  \mathbf{x}_i=\mathrm{Flatten}(\text{patch}_i)\in\mathbb{R}^{P^2 C},
  \qquad
  \mathbf{X}=[\mathbf{x}_1;\ldots;\mathbf{x}_N]\in\mathbb{R}^{N\times P^2C}
  $$

  其中 $P\times P$ 是 patch 大小，$C$ 是 channel 数，$N$ 是 patch 数。
- ⚠️ **图像分类只需要 encoder，不需要 decoder**：因为输入是图像、输出是**一个类别**，不是另一个序列。decoder 是用来生成序列的（翻译、问答等）。

#### 17.2 ViT vs CNN（PDF p.339）

| 对比项 | **CNN** | **Vision Transformer (ViT)** |
|---|---|---|
| 输入 | 图像 / feature map | patch 序列 |
| 核心运算 | convolution（local → global by depth） | self-attention（global from layer 1） |
| 大数据集表现 | 有长期验证的良好记录，处理大规模数据高效 | **在大规模数据上 pre-train 后，多个 benchmark 超过 SOTA CNN** |
| 训练算力 | 相对高效 | 原论文称**所需算力更少**（after large-scale pre-training） |
| 优势场景 | 各类 CV 任务，成熟稳定 | **需要 global dependencies 与 contextual understanding 的场景** |
| 位置信息 | 由卷积/空间结构隐式提供 | 必须显式加 positional encoding |

- ⚠️ PDF 在 "global(?)" 处**打了问号**——这与 §8.3 的讨论呼应：老师**不认为** "local vs global" 是 Transformer 优于 CNN 的完整解释。
- ⚠️ 老师对 ViT 的**个人评价**：
  - ViT 把图像简单切成 patch、展平成 token 的做法**很粗糙**；"**In my opinion, this is not a good way to generate tokens from the image. We should have some other better way.**"
  - 但即便如此简单的 tokenization，Transformer 已经能超过 CNN——这更说明 **attention 机制的强大**。
  - 老师还批评 ViT 原论文把 pointwise FFN 叫作 **MLP** 是**错误的**（§14.2）。

#### 17.3 Vision-Language Transformer（VLT）：referring segmentation

- 老师的另一项工作：**Vision-Language Transformer（视觉-语言 Transformer）**，用于 **referring segmentation（指代分割）**。
- 任务：给一张图像 + 一句自然语言指令（如 "the small elephant on the left"），分割出语言所指的物体。
- 需要同时处理**视觉信息**与**语言信息**：

| 模态 | 处理方式 |
|---|---|
| **Image** | 先过 **CNN** 提取 visual features（得到 image token 序列） |
| **Language** | 先做 **embedding**，得到 language token 序列 |
| **Fusion** | 在 language tokens 与 image tokens 之间做 **cross-attention（交叉注意力）** |
| **Query generation** | 用 cross-attention 的输出生成一个 **query**，它同时包含语言语义与图像信息 |
| **Decoder** | 用该 query 去查询 image transformer decoder，输出分割结果 |

- 核心公式仍是 attention：

  $$
  \mathbf{z}_i=\sum_j\left(\mathbf{q}_i\cdot\mathbf{k}_j\right)\mathbf{v}_j
  $$

  只是这里的 $i$ 可能来自 language，$j$ 来自 image（或反之），所以叫 **cross-attention**。
- 发表：**ICCV 2021**；扩展版 **IEEE TPAMI**, vol. 45, no. 6, pp. 7900–7916, Jun. 2023；老师课堂称已被引用 **700+** 次。

### 18. ⭐ Deep Learning 的官方总结（PDF p.341）

PDF 最后一页 "Conclusion of Deep Learning" 给出 8 条，是**整个 Topic 9–10 的收束**，也是期末复习的纲领：

| # | 结论 | 解读 |
|---|---|---|
| 1 | **The success of AI lies in Machine Learning.** | 当前 AI 的成功本质上依赖 machine learning，而不是手工规则 |
| 2 | **The success of Machine Learning lies in learning general rules, not overfitting to specific details of training data.** | 学 general rule 才是关键；overfit 细节必然失败 |
| 3 | **This is realized by learning in convolution with minimum filter size ⇒ CNN.** | 用**最小 filter（3×3、1×1）**做 convolution，让每个参数走过所有位置 → CNN |
| 4 | **Hence, many convolutional layers are required by capturing large area of information ⇒ Deep learning.** | 小 filter 要覆盖大区域，只能靠**很多层** → deep learning |
| 5 | **Deep learning is facilitated by the simplest nonlinear activation function ReLU.** | 层多 → backprop 路径长 → 必须用最简单的非线性 ReLU 防止 vanishing gradient |
| 6 | **Every single learned parameter of CNN going through all inputs greatly enhances the learning generalization.** It captures information by weights learned from training data, however, **limits its capability**. | parameter sharing 提升泛化；但权重**从 training data 学、训练后固定**，无法适应每个具体 input → 这是 CNN 的**能力上限** |
| 7 | **Transformer captures global information by non-learnable attention modules.** Different from MLP and CNN, the way to capture global information is **not learned from the training data set. It is specified by the specific test input.** | attention 权重由 test input 生成；这是 Transformer 相对 CNN 的**革命性区别** |
| 8 | **All learnable modules of transformer exploits the concept of convolution!** | Q/K/V 投影、FFN 都是 **1×1 convolution / pointwise**；Transformer 的可学习部分仍然沿用 CNN 思想 |

- ⚠️ 第 6–8 条是老师整个课程的**核心观点**，也是 Week 8–9 的主线：
  - CNN 用 **parameter sharing** 解决 overfitting；
  - 但 CNN 的权重**固定**，不能随 input 自适应；
  - Transformer 用 **input-generated attention weights** 解决这一点；
  - 同时 Transformer 的**可学习部分仍然是 convolution**（1×1）。
- 一句话总结：

$$
\boxed{\;\text{CNN 的 revolution = parameter sharing；Transformer 的 revolution = input-adaptive attention。}\;}
$$

### 19. ⭐⭐ 期末考试范围与题型（Week 9 末公布，极重要）

#### 19.1 课程考核构成（PDF p.3）

| 成分 | 占比 | 说明 |
|---|---|---|
| **Final Examination** | **60%** | 期末笔试 |
| **CA（Continuous Assessment）** | **40%** | 见下 |
| ┗ Quiz | **10%** | Week 7，课堂内 30 分钟 |
| ┗ Assignment 1 | **15%** | take-home mini-project + report（Jiang 部分） |
| ┗ Assignment 2 | **15%** | take-home mini-project + report（Cheng Jun 部分） |

#### 19.2 Final exam 的题型（老师原话整理）

- **4 道题，3 小时**。
- 其中 **3 道题来自 Jiang Xudong 部分（Topic 1–10）**，**第 4 题由另一位老师出**。
- **前 3 题**：用**数学表达式 / 数值计算**来回答，**不要求英文 essay**；考的是**理解（understanding）**，不是**记忆（memorization）**。
  - 老师原话："I will never test your skills, but I test your understanding. Based on your understanding, you should be able to figure out how to solve the question."
  - 即使题目看起来是数值计算，也不是考"算术"，而是考"**你是否知道该怎么算、为什么这样算**"。
- **第 4 题**：用**英文句子**回答；不要求漂亮英文，**踩到 key points 就给分**。

#### 19.3 前 3 题的来源（明确）

| 题号 | 来源 Topic | 内容 | 备注 |
|---|---|---|---|
| **Q1** | **Topic 3** | **Image denoising and enhancement** | 老师明确说："**more on the enhancement part than the denoising part**" |
| **Q2** | **Topic 5** | **MAP decision and classifiers** | 基于 MAP 理论的各种 classifier |
| **Q3** | **Topic 9 + Topic 10** | **Neural networks, CNN, Transformer** | 重点在 **deep learning 部分**（MLP → CNN → Transformer 的核心概念与公式） |
| **Q4** | 另一位老师 | 英文简答 | 用 English sentences 答 key points |

#### 19.4 不考的 Topic（按老师课堂宣布）

- 老师原话（转写整理）："**The first topic and the second topic, both are not in the final exam. The third topic, image noise and enhancement, will be in the final exam, where the fourth topic, sixth topic ... also not in the final exam. The MAP rule and different classifiers designed based on the theory of MAP is within the scope of the final exam. And then the next few topics, two topics are not in the final exam.**"
- 结合"Q1=Topic 3、Q2=Topic 5、Q3=Topic 9+10"可以确定：
  - ✅ **考**：Topic 3、Topic 5、Topic 9、Topic 10；
  - ❌ **不考**：Topic 1、Topic 2、Topic 4、Topic 6、Topic 7、Topic 8。
- ⚠️ 转写在这段有重复/漏词（"fourth topic six topic and six topic"），但**三道题的来源是老师逐题点名说的**，以上表为准。若老师之后在 NTULearn 发布正式范围，以官方通知为准。

#### 19.5 复习建议（按老师原话）

1. **不要背公式**：要理解公式**怎么来的、每一项的物理意义**；考试时能**自己写出来**。
2. **重点深入**：Topic 3 的 **enhancement**、Topic 5 的 **MAP/classifier**、Topic 9–10 的 **NN/CNN/Transformer**。
3. **练习用数学表达**：能写出 convolution、backprop、attention 等关键公式，并说明符号含义。
4. **Q4 用英文答 key points**：不需要长篇大论，踩点即可。
5. **Assignment 不要逾期**：老师特别提醒 "don't forget to submit your assignment before the deadline."

### 20. ⭐ 本周考点速查

| 考点 | 要点 | 节号 |
|---|---|---|
| **CNN 的核心** | kernel 走过所有位置；所有像素共同训练同一参数 → robust、general rule、revolution | §2 |
| **卷积输出尺寸** | $O=\lfloor(I+2P-K)/S\rfloor+1$；same padding $P=(K-1)/2,S=1$ → $O=I$ | §2.2 |
| **卷积参数量** | $(K_hK_wC_{in}+1)C_{out}$；远小于同尺寸 MLP | §2.2 |
| **感受野递推** | $r_L=r_{L-1}+(K_L-1)\prod_{i<L}S_i$；3×3 stride 1 → $2L+1$ | §2.2 |
| **Image segmentation** | 逐像素分类；标注昂贵；用 pre-trained network（ResNet-101）+ fine-tune | §3 |
| **ResNet-101 例子** | 输入 200×200×3；最终 16×16×约 2000 channel；ImageNet 预训练 | §3.2 |
| **CCL** | local 3×3 与 dilated 3×3 的**差值** = 局部与周围的 contrast；多层 chained → multi-level | §4 |
| **Gated sum** | $\mathbf{S}(p)=\sum_l\alpha_l(p)\mathbf{s}_l(p)$；$\alpha_l(p)$ 由 **input** 生成，不是训练后固定 | §5 |
| **为什么叫 gated** | 权重随 input/位置变化，起"选择尺度"的门控作用；普通 weighted sum 权重固定 | §5.4 |
| **Boundary refinement** | 粗分割 → 边界 impulse → 不同 $\sigma$ 的 Gaussian 扩散 → 小/中/大尺度权重；边界附近用小尺度 | §6 |
| **Shape-variant convolution** | 1×1 conv 算像素相关 → shape mask → 加权大方形 kernel；mask 随 input 变化 | §7 |
| **Shape mask = attention** | correlation map 就是 attention map；"attention and correlation are exactly the same" | §7.5 |
| **Transformer 定位** | sequence-to-sequence；RNN/LSTM 顺序处理，Transformer 并行 | §8.1 |
| **三个问题** | 怎么工作？attention 是否一切？local vs global 能否解释？ | §8.2 |
| **驳斥 local/global** | CNN 多层可覆盖整图；MLP 全连接却最差；CNN 的 global 是从整个 training set 学的 | §8.3 |
| **三种 weighted sum** | MLP/CNN 权重 learned & fixed；Transformer attention 权重 input-generated | §8.4 |
| **Encoder/Decoder** | 同构 stack；last encoder → 所有 decoder 的 K/V；decoder 还接收已生成 token | §9 |
| **Encoder block** | self-attention → add & norm → pointwise FFN → add & norm | §9.2 |
| **Decoder block** | self-attention → cross-attention（Q 来自 decoder，K/V 来自 encoder）→ FFN | §9.3 |
| **Token/Embedding** | token → feature vector（标准 512 维）；语义相近 → 距离近 | §10.1 |
| **Positional encoding** | $\mathbf{x}_i=\mathrm{Embed}(w_i)+\mathbf{p}_i$；否则 attention 不知道顺序 | §10.2 |
| **输入矩阵** | $\mathbf{X}\in\mathbb{R}^{N\times K}$，一行一个 token；大小在 Transformer 中不变 | §10.3 |
| **Residual** | $\mathbf{y}=\mathbf{x}+F(\mathbf{x})$；子层只学残差；梯度含 $\mathbf{I}$，缓解 vanishing gradient | §11 |
| **Q/K/V** | $\mathbf{Q}=\mathbf{X}\mathbf{W}_q,\mathbf{K}=\mathbf{X}\mathbf{W}_k,\mathbf{V}=\mathbf{X}\mathbf{W}_v$；所有 token 共享 → **1×1 convolution** | §12.1 |
| **Attention score** | $\mathbf{R}=\mathbf{Q}\mathbf{K}^{T}$；$r_{ij}=\mathbf{q}_i\cdot\mathbf{k}_j$；相似度/相关；类比 covariance | §12.2 |
| **Softmax** | $\mathbf{A}=\mathrm{softmax}(\mathbf{Q}\mathbf{K}^{T}/\sqrt{d_k})$；PDF 简化省略 | §12.3 |
| **Attention 输出** | $\mathbf{Z}=\mathbf{Q}\mathbf{K}^{T}\mathbf{V}$（简化）；$\mathbf{z}_i=\sum_j a_{ij}\mathbf{v}_j$；所有输入 token 的加权和 → global | §12.4 |
| **⭐ attention 权重** | **不由 training data 学**；由 test input 的 Q/K 现算；attention itself non-learnable | §12.5 |
| **可学习部分** | Q/K/V 投影、FFN 的 $\mathbf{W}$ 是可学习的；attention weights 不是 | §12.5 |
| **Multi-head** | 多组 Q/K/V 并行 attention，concat 后 $\mathbf{W}_o$ 融合 | §13 |
| **Pointwise FFN** | $\mathbf{Y}=h(h(h(\mathbf{Z}\mathbf{W}_1)\mathbf{W}_2)\mathbf{W}_3)$；逐 token 独立，参数共享；**不是 MLP，是 1×1 conv** | §14 |
| **Cross-attention** | Q 来自 decoder，K/V 来自 encoder；公式同 self-attention | §15.1 |
| **Generative** | 一次生成一个 token，输出反馈为下一步输入；encoder 输出不变 | §15.2 |
| **ViT** | 图像切 patch → flatten → token 序列 → encoder → classifier；只需 encoder | §17.1 |
| **ViT vs CNN** | ViT 大规模预训练后超过 CNN、算力更少；CNN 成熟高效；"global(?)" 存疑 | §17.2 |
| **VLT** | image tokens + language tokens → cross-attention → query → decoder 分割；ICCV'21/TPAMI'23 | §17.3 |
| **Deep learning 总结** | 8 条结论：AI→ML→general rule→CNN→deep→ReLU→parameter sharing→Transformer attention | §18 |
| **考试范围** | 4 题 3 小时；Q1 Topic 3、Q2 Topic 5、Q3 Topic 9+10；Q4 英文简答；Topic 1/2/4/6/7/8 不考 | §19 |
| **考试形式** | 前 3 题数学表达/数值计算，考理解不考记忆；Q4 英文踩点 | §19.2 |

### 21. 本周要点小结

- **CNN 的进一步发展**：老师用自己的 image segmentation 研究（三项主要贡献 + Shape-Variant Convolution）说明，在 CNN 之上还可以做**input-adaptive weighting**：
  - **CCL**：local 与 dilated context 的**差值**，突出局部与周围的 contrast，避免大区域平均导致的 blur；
  - **Gated multi-scale aggregation**：不同位置需要不同尺度；权重 $\alpha_l(p)$ 由**当前 input** 生成，而不是训练后固定，故称 **gated sum**；
  - **Boundary refinement**：用粗分割边界 + **multi-scale Gaussian diffusion** 自动给边界附近小尺度、远离边界大尺度；
  - **Shape-variant convolution**：用像素间 **correlation** 生成 **shape mask**，让 kernel 形状随物体形状变化；mask 就是 **attention map**。
- **共同主线**：这四项工作的权重都**由具体 input 生成**，不是从 training data 学完就固定——这正是 Transformer **attention** 的思想先声。
- **Transformer 结构**：**encoder stack + decoder stack**；encoder 是 self-attention + pointwise FFN，decoder 多一个 encoder-decoder attention；每个子层都有 **residual connection** 与 normalization。
- **输入表示**：token → **embedding**（标准 512 维）→ 加 **positional encoding** → 排成 $N\times K$ 矩阵，一行一个 token；整个 Transformer 中矩阵大小不变。
- **Self-attention**：
  - $\mathbf{Q}=\mathbf{X}\mathbf{W}_q,\ \mathbf{K}=\mathbf{X}\mathbf{W}_k,\ \mathbf{V}=\mathbf{X}\mathbf{W}_v$，所有 token 共享 → **1×1 convolution**；
  - $\mathbf{R}=\mathbf{Q}\mathbf{K}^{T}$ 是 token 两两相关（类比 covariance）；
  - $\mathbf{A}=\mathrm{softmax}(\mathbf{Q}\mathbf{K}^{T}/\sqrt{d_k})$，$\mathbf{Z}=\mathbf{A}\mathbf{V}$；PDF 简化为 $\mathbf{Z}=\mathbf{Q}\mathbf{K}^{T}\mathbf{V}$；
  - **每个输出 token 是所有输入 token 的加权和 → global information**。
- **⭐⭐ 最核心的考点**：**attention 的权重不是从 training data 学出来的，而是由具体 test input 的 Q/K 现算的**；可学习的是 Q/K/V 投影与 FFN，attention 本身 non-learnable。这是 Transformer 相对 MLP/CNN 的 **revolution**。
- **Transformer 的可学习模块仍是 convolution**：Q/K/V 投影与 pointwise FFN 都是 **1×1 convolution**；pointwise FFN **不是 MLP**，因为每个 token 独立处理、参数共享。
- **ViT**：图像切 patch → token 序列 → Transformer encoder → classifier；大规模预训练后超过 CNN，但 tokenization 方式仍较粗糙。**VLT** 把 vision + language 结合，用于 referring segmentation。
- **期末考试**（极重要）：4 题 3 小时；Q1 Topic 3（enhancement 为主）、Q2 Topic 5（MAP/classifier）、Q3 Topic 9+10（NN/CNN/Transformer）；Q4 英文简答。Topic 1/2/4/6/7/8 不考。前 3 题考**理解 + 数学表达**，不考死记。

### 22. 下一周预告

- **本周是 Jiang Xudong 老师 Topic 1–10 的最后一课**。从 **Week 10** 起，课程进入 **Dr. Cheng Jun** 主讲部分（PDF p.2）：

| Week | Topic | 内容 |
|---|---|---|
| **Week 10** | **Topic 11** | **Video Analysis**（视频分析） |
| **Week 11** | **Topic 12** | **Video Recognition**（视频识别） |
| **Week 12** | **Topic 13** | **Three-dimensional Machine Perception**（三维机器感知） |
| **Week 13** | **Topic 14** | **Three-dimensional Machine Vision**（三维机器视觉） |

- **Week 9 没有新的录播预告内容**（老师只说 "from next week, another lecturer from the Research Institute will come to give you the lectures for Topic 11 to 14"）；上表来自 PDF 第 2 页的 Course Content，是权威课程安排。
- **期末复习建议**（按老师原话）：
  1. 重点复习 **Topic 3（enhancement）、Topic 5（MAP/classifier）、Topic 9–10（NN/CNN/Transformer）**；
  2. 不要背公式，要能**从理解出发写出数学表达式**；
  3. 用 Week 8–9 笔记中的公式表与对比表自测：卷积尺寸、感受野、backprop、Q/K/V、attention、softmax、residual；
  4. Q4 用英文答 **key points**，不需要漂亮英文；
  5. **Assignment 不要逾期**。
- ⚠️ 若 NTULearn 之后发布正式的 final exam scope / sample questions，以官方通知为准；本节 §19 是老师课堂口头宣布的整理。





---

## Week 11 — Topic 12：Video (Part II)（视频分析下半：检测/跟踪、动作识别、视频增强、光流、视频分割）

> **本周材料**：`week11/week11.txt`（录播转写）、`Lecture Notes Week 11.pdf`（Cheng Jun，*Video (Part II)*，49 页）。本周是 **Dr. Cheng Jun** 部分的第二讲，接 Week 10 的 Video (Part I)。
>
> **权威来源说明**：转写 ASR 噪声较大，典型错拼：
>
> | 转写 | 正确 |
> |---|---|
> | detection and checking | **detection and tracking** |
> | racking / ting | **tracking** |
> | re ID / GDE / GD | **Re-ID / JDE** |
> | temporary | **temporal** |
> | general A | **generative AI** |
> | sitation / semitation | **segmentation** |
> | optic flow | **optical flow** |
> | decolion | **deconvolution** |
> | unit | **U-Net** |
> | compolution / combolion | **convolution** |
> | MK | **MICCAI**（medical image conference） |
> | treaty / TD | **3D** |
> | post function | **point-spread function (PSF)** |
> | brightness considered equation | **brightness constancy equation** |
> | four positive / force positive | **false positive** |
> | ASF | **AI safety** |

### 1. 本周定位：Video (Part II)

Week 10 的 Video (Part I) 讲了视频的基础表示与视频理解的整体框架；本周进入**具体任务**：

| 任务 | 核心问题 |
|---|---|
| **Object Detection & Tracking** | 视频里有什么、每一帧在哪里、跨帧是不是同一个人/物 |
| **Re-ID** | 跨摄像头/跨时间匹配同一个人/物 |
| **Action Recognition** | 视频里的人在做什么动作 |
| **Video Enhancement** | 视频模糊/湍流怎么恢复 |
| **Optical Flow** | 每个像素在相邻帧之间怎么移动 |
| **Video Segmentation** | 每个像素属于什么类别，且帧间要一致 |

⭐ 老师的定位：Video (Part II) 是**相对成熟、商业化已久**的方向（object detection/tracking、action recognition 已在工业界广泛使用）；相比 Week 10 的生成式 AI，这个方向**研究热度较低**，但工业需求稳定。

### 2. Video vs Image：最核心的区别是 Temporal Continuity

- **Video**：a sequence of images with **correlations among the images**。
- **Image object detection**：每一帧独立处理。
- **Video object detection**：帧与帧之间有 **temporal continuity**；可以利用 temporal information 改善 detection、tracking。
- 人眼把连续帧"看成"视频；计算机看到的是**一帧一帧的静态图像**。

⭐ 典型流水线：

```
1. Detect / segment objects in each frame
2. Associate detections over time (tracking)
3. Assign consistent ID to each object
```

### 3. Object Detection & Tracking（目标检测与跟踪）

#### 3.1 基本概念

- **Detection**：在当前帧找出 object，给出 bounding box，并可做 segmentation 得到精确边界。
- **Tracking**：把不同帧中的 detection **关联**起来，判断是不是同一个 object。
- 每个 object 分配一个 **ID**；视频中不同颜色/编号的框就是 tracking 的结果。

#### 3.2 视频检测的挑战：Flicker（闪烁）

- 同一张脸在连续帧中**人眼明明看到**，但 detector 在某些帧漏检 → 框时有时无，称为 **flickering artifact**。
- 这是视频检测特有的问题：单帧检测器没有利用 temporal consistency。
- 评价一个 detector 在视频上的表现，**帧间一致性**本身就是一个指标。

#### 3.3 Re-ID（Re-identification，重识别）

> **Re-ID**：matching object/people across **disjoint camera views** in a multi-camera system.

- 可以跨不同摄像头，也可以同一摄像头不同时间。
- 传统做法：**detect → track → compare appearance**。
- 应用：多摄像头行人追踪、安防、无人店。

#### 3.4 JDE（Joint Detection and Embedding）

- **JDE**：把 detection 和 embedding **同时**做。
- 检测头通常包含：
  - **Regression**：预测 bounding box（左上/右下坐标）；
  - **Classification**：判断 object 类别（人/狗/车…）；
  - **Embedding**：输出一个固定维度的 feature，代表 object 的 appearance。
- 有了 embedding，就可以直接比较不同帧/不同摄像头的 object 是不是同一个，**不需要先检测再单独做 Re-ID**。
- 相比 "detect-then-compare" 的 Re-ID：
  - JDE 在**遮挡后重新出现**时更容易恢复（因为 embedding 一直保留）；
  - 速度更快、端到端。

⭐ 老师用 DGI 的视频展示：普通 detection+tracking 在 object 被树挡住后会丢失，无法恢复；JDE 因为有 embedding feature，object 再次出现时可以自动 re-associate。

#### 3.5 动作识别与事件检测的区别

- **Action recognition**：识别**单个动作**（走路、跳跃、挥手）。
- **Video event detection**：识别**复杂事件**（婚礼、进球、打架）。
- 复杂事件的时间边界（从哪一帧开始、到哪一帧结束）目前**仍不准确**；通常把长视频切成 clip，再对 clip 分类，只能粗略定位。

### 4. Action Recognition（动作识别）

#### 4.1 基本流程

```
raw video → sample frames into a clip → feature extraction → classifier
```

- 与 object recognition 类似，但输入从单张图变成 **clip（多帧）**。
- 关键新增：**video sampling / frame rate**。

#### 4.2 Frame rate 与实时性

- 视频可以是 60/30/15 fps；做实时系统时，每秒要处理所有帧。
- 例：10 fps → 每帧只有 **100 ms** 的处理预算；30 fps → 约 33 ms。
- 老师课堂提问：最低多少 fps 看起来仍像"视频"而不是"几张图"？答案大约 **7–15 fps**；10–15 fps 是很多人觉得"接近实时"的范围。
- 动作识别对 frame rate 的鲁棒性也是一个挑战：downsample 后分类结果可能变化。

#### 4.3 早期方法：LRCN（Long-term Recurrent Convolutional Network）

- 用 CNN 提每帧 feature，再用 **LSTM/RNN** 建模时间序列。
- 结构：CNN feature sequence → recurrent layer → classifier。
- 适合处理变长视频；但训练较慢。

#### 4.4 C3D（3D Convolutional Network）

- 把视频看成 **3D volume**（空间 2D + 时间 1D），用 **3D convolution** 同时提取空间和时间特征。
- 优点：直接捕获 spatiotemporal features；不需要显式 optical flow。
- 缺点：参数量大、计算贵；对长时序建模有限。
- 课件还提到用 **deconvolutional layers** 解释模型决策。

#### 4.5 Two-Stream / Hidden Two-Stream

- **Two-stream**：一路 RGB（spatial appearance），一路 optical flow（motion），最后融合。
- **Hidden Two-Stream**（Zhu et al., 2017）：用一个单独的网络**实时生成 optical flow**，不再需要预先计算 flow。
- 直觉：一张图看"我长什么样"，另一路看"我怎么动"。

#### 4.6 医学视频例子：Cine MRI

- 任务：判断心肌微血管阻塞（microvascular obstruction），healthy vs unhealthy。
- 数据：新加坡国家心脏中心约 600 个病人（小数据）。
- 方法：C3D 提取时空特征 + motion features + two-stream 融合。
- ⭐ 老师强调：**Transformer 虽然强，但需要大量数据**；医学数据小，所以用 C3D / two-stream 更实际。

#### 4.7 Transformer 的崛起

- 现在视频理解的主流逐渐转向 **Transformer**（时空 attention）。
- 但 Transformer 需要更多数据/算力；小数据场景仍可用 CNN/RNN/3D CNN。

### 5. Video Enhancement（视频增强）

#### 5.1 Motion Blur（运动模糊）

- 来源：**object motion**（物体动）或 **camera motion**（相机抖）。
- 模糊可以用 **point-spread function (PSF)** 描述：

$$g(n_1,n_2)=d(n_1,n_2)*f(n_1,n_2)+w(n_1,n_2)$$

其中 $d$ = PSF，$f$ = 真实图像，$w$ = 噪声，$*$ 是 2D convolution。

- PSF 的性质：
  - 非负（物理成像过程）；
  - 实值；
  - 不吸收/产生能量：$\sum_{n_1,n_2}d(n_1,n_2)=1$。
- **No blur**：PSF 是 unit pulse（delta function），$g=f+w$。

#### 5.2 Blind Image Deconvolution（盲反卷积）

- 目标：从 $g$ 恢复 $f$。
- 因为 $g=d*f+w$，逆过程是 **deconvolution**。
- **Blind**：PSF $d$ 未知（不同人手持相机的抖动不同）。
- ⭐ 需要**准确的 PSF**；PSF 不准，deconvolution 会引入新的噪声/伪影。
- 传统方法不展开；深度学习方法：**encoder-decoder**，输入 stacked nearby frames，输出 deblurred video（Deep Video Deblurring, Su et al., CVPR 2017）。

#### 5.3 Turbulence Removal（湍流去除）

- 场景：空气湍流（air turbulence）、水面（water turbulence）。
- 特点：
  - **local non-rigid deformation**（局部非刚性形变）；
  - **space-time-varying blur**（时空变化的模糊）。
- 处理框架：low-rank decomposition → non-rigid registration → spatial-temporal kernel regression → deblurring → superfast refinement（NLTV & TV）。
- 代表工作：Xie et al., IEEE T-IP 2016。

⭐ 老师观点：深度学习降低了进入门槛（不需要完全理解 PSF 也能训练 deblur 模型），但**理解成像模型**仍然重要，否则不知道模型为什么work、什么时候会失败。

### 6. Optical Flow（光流）

#### 6.1 定义

> **Optical flow**：the 2D projection of the physical movement of points relative to the observer to the 2D displacement of pixel patches on the image plane.

- 给定帧 $t$ 中的点 $p_1$，在帧 $t+1$ 中找到对应点 $p_2$，位移 $(u,v)$ 就是 flow。
- 由位移和帧间隔可算**速度**（方向 + 大小）。
- 应用：image tracking、motion analysis、two-stream action recognition、video stabilization。

#### 6.2 三个假设

| 假设 | 含义 |
|---|---|
| **Spatial coherence** | 相邻像素通常属于同一表面，因而有相近的 flow |
| **Temporal persistence** | 相邻帧之间物体移动有限（不会瞬间跳很远） |
| **Brightness constancy** | 同一个点在相邻帧中亮度不变：$I(x,y,t)=I(x+\Delta x,y+\Delta y,t+\Delta t)$ |

#### 6.3 Brightness Constancy Equation（推导）

对 $I(x+\Delta x,y+\Delta y,t+\Delta t)$ 在 $(x,y,t)$ 做一阶 Taylor 展开：

$$I(x+\Delta x,y+\Delta y,t+\Delta t)\approx I(x,y,t)+I_x\Delta x+I_y\Delta y+I_t\Delta t$$

由 brightness constancy，两边相等：

$$I_x\Delta x+I_y\Delta y+I_t\Delta t\approx0$$

除以 $\Delta t$，令 $u=\frac{dx}{dt},\ v=\frac{dy}{dt}$：

$$\boxed{I_x u+I_y v+I_t=0}\qquad\text{或}\qquad \nabla I^T\begin{bmatrix}u\\v\end{bmatrix}+I_t=0$$

这就是 **brightness constancy equation**（光流约束方程）。

#### 6.4 Aperture Problem（孔径问题）

- 每个像素只有 **1 个方程**，但有 **2 个未知数** $(u,v)$ → **underdetermined**。
- 几何解释：只能测出**沿梯度方向**的运动分量（normal flow）；**沿边缘方向**（垂直于梯度）的分量无法确定。
- 若 $(u,v)$ 满足方程，则 $(u+u',v+v')$ 只要 $\nabla I^T[u'\ v']=0$ 也满足 → 解不唯一。
- 解决需要额外约束（如 Lucas-Kanade 的局部平滑假设、Horn-Schunck 的全局平滑）——课件只讲到问题本身。

### 7. Video Segmentation（视频分割）

#### 7.1 Semantic Segmentation

- 输入图像，输出**每个像素的 class label**（人/车/路/背景…）。
- 与 classification 的区别：classification 输出一个 label；segmentation 输出**与原图同尺寸的 label map**。
- 相关任务：depth estimation、boundary prediction（输入输出都是 image-level）。

#### 7.2 从 Classification 到 Segmentation：FCN

- 分类网络：conv + pool + FC → 1000-dim vector → class。
- 分割网络：把 **FC 层换成 fully convolutional**，保留 spatial 信息；再 **upsampling** 回原图尺寸。
- **End-to-end, pixels-to-pixels**：输入像素，输出像素级 label + loss。
- 代表：R-CNN 做 detection；FCN 做 segmentation。

#### 7.3 U-Net

- 结构：**Contraction（encoder）+ Expansion（decoder）**。

| 阶段 | 作用 | 变化 |
|---|---|---|
| **Contraction** | 提取语义、"what" | 空间尺寸减小，channel 数增加；丢失部分 spatial info |
| **Expansion** | 恢复细节、"where" | 上采样，恢复分辨率 |
| **Skip connection** | 把 contraction 的高分辨率 feature **concatenate** 到 expansion | 帮助恢复 "where" 信息 |

- ⭐ 类比：contraction 是"压缩理解"，expansion 是"还原细节"；skip connection 把压缩前的细节抄近路送回去。

#### 7.4 Image Segmentation vs Video Segmentation

| | Image segmentation | Video segmentation |
|---|---|---|
| **处理方式** | frame-based，每帧独立 | frame-to-frame association |
| **问题** | **flicker artifact**：相邻帧 label 跳变 | 需要**temporal consistency** |
| **目标** | 单帧准确 | 帧间平滑、稳定 |

- 视频分割可以直接用 image segmentation 逐帧跑，但会有 flicker；更好的做法是利用帧间关联。
- 评价：除了 mIoU，还要看 **temporal consistency**（相邻帧相似度/感知特征）。
- 例子：OSDab（on-device learning）用 base network + tiny auxiliary network 提升时序一致性；在 Snapdragon 上把任务分到 DSP/GPU，推理时间降到 37 ms，达到 real-time。
- 应用：autonomous driving、smart cameras、XR。

#### 7.5 Face detection：image-based vs video-based

- 老师课堂投票：商用 face detection 是基于 image 还是 video？
- 答案：**image-based**（逐帧处理）更常见。
- 原因：video-based 需要等更多帧，延迟高；image-based 虽然精度可能略低，但**更实用、更快、更省资源**。

### 8. 3D 与 Vision-Language-Action（老师的前沿点评）

- 老师认为 **3D** 比 2D 视频更重要：机器人、自动驾驶都在 3D 世界。
- 当前热点：**Vision-Language-Action (VLA)**、**Vision-Language Navigation**——用自然语言给机器人/汽车下指令，模型把视觉 + 语言转成动作。
- 趋势：从"segmentation 输出"转向"直接输出动作/导航决策"；Tesla 等公司也在从 rule-based 后处理转向端到端学习。
- ⚠️ 老师明确说：**接下来两周（Week 12–13）讲 3D**。

### 9. 作业与考试信息（Week 11 课堂宣布）

#### 9.1 Assignment 2 更正

> **"You don't need to provide revised design."**

- Part 1：写自己的设计（own design），不需要参考/修改 AI；
- Part 2：拿到 AI proposal 后，**比较差异**，按四个 points 讨论；
- **不需要**给出"revised design"；
- 重点：**能够判断 AI 哪里对、哪里错**，而不是让 AI 代写。

#### 9.2 Final Exam（Cheng Jun 部分）

- 期末 **4 题，每题约 25 分**：
  - **3 题**来自 Jiang Xudong（Topic 1–10）；
  - **1 题**来自 Cheng Jun（Topic 11–14）。
- ⭐ Cheng Jun 明确说：**他这部分考 concept，不考 calculation**；不要只背公式，要理解原理、方法、limitation。
- 往年题可能以计算为主，但**本学期他的 Q4 是英文简答/概念题**；不要因为"往年题"而只准备计算。
- 他提到有学生战略性地放弃 Q4——他明确不鼓励：Q4 占 25 分，且是概念题，容易拿分。

### 10. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| **Video vs Image** | video 有 temporal continuity；image 每帧独立 |
| **Detection + Tracking** | detect → associate over time → assign ID |
| **Flicker** | 视频检测的帧间不一致；可用 temporal consistency 评价 |
| **Re-ID** | 跨摄像头/跨时间匹配同一 object |
| **JDE** | detection + embedding 同时做；embedding 用于 re-associate |
| **Action recognition** | clip → feature → classifier；与 object recognition 类似但多时间维 |
| **LRCN** | CNN + LSTM/RNN |
| **C3D** | 3D convolution 提 spatiotemporal features |
| **Two-stream / Hidden Two-stream** | RGB + optical flow；Hidden 用网络生成 flow |
| **Frame rate** | 10–15 fps 接近"实时感"；10 fps → 100 ms/frame |
| **Blur model** | $g=d*f+w$；PSF 非负、和为 1；无模糊时 PSF=delta |
| **Blind deconvolution** | PSF 未知；PSF 不准会引入伪影 |
| **Deep video deblur** | stacked frames → encoder-decoder |
| **Turbulence** | non-rigid deformation + space-time-varying blur；registration + kernel regression |
| **Optical flow** | 2D displacement of pixel patches |
| **三个假设** | spatial coherence、temporal persistence、brightness constancy |
| **Brightness constancy equation** | $I_xu+I_yv+I_t=0$ |
| **Aperture problem** | 1 equation, 2 unknowns；只能测 normal flow |
| **Semantic segmentation** | 每像素 class label |
| **FCN** | FC → fully convolutional + upsampling；pixels-to-pixels |
| **U-Net** | contraction + expansion + skip concatenation |
| **Image vs video segmentation** | frame-based 有 flicker；video 要 temporal consistency |
| **Face detection** | 商用多用 image-based（速度/资源） |
| **Final exam** | 4 题 × 25 分；Cheng Jun 1 题，概念为主，不考计算 |

### 11. 本周要点小结

- **Video 的本质**：带时间相关性的图像序列；视频任务的关键是 **temporal continuity**。
- **Detection & Tracking**：检测每帧 object，再跨帧关联；Re-ID 跨摄像头匹配；JDE 把 detection 与 embedding 合在一起，遮挡后更容易恢复。
- **Action recognition**：clip → feature → classifier；LRCN（CNN+RNN）、C3D（3D conv）、two-stream（RGB+flow）是早期主流；Transformer 现在更强但需要更多数据。
- **Video enhancement**：motion blur = PSF convolution + noise；blind deconvolution 需要准确 PSF；深度学习用 encoder-decoder；turbulence 需要 non-rigid registration + kernel regression。
- **Optical flow**：brightness constancy → $I_xu+I_yv+I_t=0$；1 equation / 2 unknowns → aperture problem，只能测 normal flow。
- **Video segmentation**：FCN / U-Net 做 pixel-level 预测；视频要额外保证 temporal consistency，避免 flicker。
- **考试**：Cheng Jun 的 Q4 是概念题（25 分），不考计算；理解原理、方法、limitation 比背公式重要。
- **一句话**：Video (Part II) 的主线是"**在时间维度上保持一致**"——检测要跨帧一致、动作要跨帧理解、分割要跨帧平滑、光流要跨帧对应；所有方法都在解决"单帧方法在视频上会抖/会丢"的问题。

### 12. 下一周预告

- **Week 12–13：3D**（Topic 13–14）——Three-dimensional Machine Perception / Machine Vision。
- 老师会讲 3D 的表示、感知、以及 Vision-Language-Action / Navigation 等前沿方向。
- **Final exam**：4 题 × 25 分；Cheng Jun 的 Q4 概念题；3 题来自 Jiang Xudong。
- **Assignment 2**：按更正后的要求，不需要 revised design；重点是 own design + AI proposal + 四点比较。

---

## Week 12 — Topic 13：3D Machine Perception（三维感知基础：ToF / LiDAR / Structured Light / SfM / 相机模型）

> **本周材料**：`week12/week12.txt`（录播转写）、`Lecture Notes Week 12-13.pdf`（Cheng Jun，*3D*，约 60+ 页；Week 12–13 共用）。
>
> **本周定位**：从 2D 视频进入 **3D**。老师先讲 3D 数据获取的几条路线（ToF、LiDAR、Structured Light、Structure from Motion、Stereo），再讲**相机模型 / 投影 / 旋转**，以及 **SfM + 特征点（Harris/SIFT）**。下周继续 **stereo images**。
>
> **ASR 错拼**：ta/treaty → **3D**；LDA → **LiDAR**；stretal → **stereo**；sift → **SIFT**；fitura → **feature**；Mobic → **Mahalanobis**；Euler → **Euler**；roll/pitch/yaw → **roll/pitch/yaw**。

### 1. 3D 数据获取的五条路线

| 方法 | 原理 | 优点 | 缺点 |
|---|---|---|---|
| **Time of Flight (ToF)** | 发射光/信号，测往返时间 → 距离 | 直接测深度、实时 | 背景光、多次反射、干扰 |
| **LiDAR** | 激光测距（ToF 的一种） | 高精度、远距离 | **LiDAR ghost**（反射/散射造成假读数）、**blooming**（高反物体使光束扩散） |
| **Structured Light** | 投射已知图案（网格/条纹），看变形 | 高精度、低成本 | **不适合室外**（强光干扰） |
| **Structure from Motion (SfM)** | 多张图像 + 特征点对应 → 同时恢复场景几何与相机运动 | 只需普通相机 | 计算复杂、依赖特征点/匹配 |
| **Stereo** | 两个相机（双目）→ 视差 → 深度 | 被动、密集 | 需要标定、纹理弱区域难匹配（下周讲） |

⭐ **ToF / LiDAR / Structured Light 是"主动"（发射信号）；SfM / Stereo 是"被动"（只用相机图像）**。

### 2. 相机模型与投影

#### 2.1 Perspective projection（透视投影）

1D 针孔模型：

```
x / f = X / Z      →      x = f * X / Z
```

- `X`：3D 点的横向坐标；
- `Z`：深度（到相机）；
- `f`：焦距；
- `x`：图像平面上的坐标；
- `Z` 越大 → `x` 越小（远处物体在图像上更小）。

⭐ 透视投影是**非线性**的（除以 Z）；这是 3D→2D 信息丢失的根源：单张图像无法唯一恢复深度。

#### 2.2 相机外参：Rotation + Translation

3D 世界点 `(U,V,W)` → 相机坐标 → 2D 图像 `(x,y)`：

```
P_camera = R * P_world + T
x = f * X_c / Z_c
y = f * Y_c / Z_c
```

- `R`：旋转矩阵（3×3）；
- `T`：平移向量（3×1）；
- 合称 **extrinsic parameters**；
- `f`（以及主点、像素尺寸）是 **intrinsic parameters**。

#### 2.3 Euler angles（欧拉角）

| 角 | 旋转轴 | 直觉 |
|---|---|---|
| **Roll** | z 轴 | 翻滚（左右倾斜） |
| **Pitch** | x 轴 | 俯仰（上下点头） |
| **Yaw** | y 轴 | 偏航（左右转头） |

- 方向：`R = Rz(roll) * Rx(pitch) * Ry(yaw)`（具体顺序取决于约定）；
- 绕 x 轴旋转 θ 的矩阵：

```
[1    0       0   ]
[0  cosθ  -sinθ  ]
[0  sinθ   cosθ  ]
```

- 绕 y、z 轴类似；三个矩阵相乘得到完整旋转。

⭐ 考试若考旋转：记住**绕哪个轴、sin/cos 的位置、旋转方向**；不同教材的 roll/pitch/yaw 定义可能不同，按课件约定。

### 3. Structure from Motion（SfM）

#### 3.1 问题定义

> 给定**两张或更多图像**，同时恢复：
> 1. **场景几何**（3D 点坐标）；
> 2. **相机运动**（每张图的 R, T）。

输入：图像间的**像素对应**（pixel correspondence），通常通过 **tracking** 得到。
输出：3D 结构 + 相机位姿。

#### 3.2 流程

1. 在图像中检测**关键点/特征**（corners、textured areas）；
2. 在帧间**跟踪/匹配**这些关键点；
3. 用对应点估计**相机参数**和**3D 点坐标**；
4. 优化（bundle adjustment）——课件只提概念，不展开。

#### 3.3 投影模型

- 经典方法：**orthographic（正交）**；
- 新方法：**perspective（透视）**；
- 近年：**deep learning** 端到端。

### 4. 特征点与跟踪

#### 4.1 什么是好的 keypoint

- **Corner（角点）**：两个方向都有明显梯度，容易定位；
- **Textured area（纹理区域）**：有丰富变化；
- 平坦区域/纯边缘：难以唯一匹配（aperture problem）。

#### 4.2 Harris corner

- 用图像梯度构造结构矩阵，检测"两个方向都变化大"的点；
- 对旋转较鲁棒，对尺度不鲁棒。

#### 4.3 SIFT（Scale-Invariant Feature Transform）

> Lowe, 2004；**scale/rotation invariant**；最著名的 hand-crafted feature descriptor。

三个步骤：

1. **Detection**：在**尺度空间**中检测可重复的关键点；
2. **Description**：给每个关键点分配方向，构造 descriptor；
3. **Matching**：用 descriptor 匹配两幅图像的关键点。

**尺度不变性**：

- **Image pyramid**：不断降采样（宽高各除以 2），在不同尺度上检测；
- **Scale space / DoG（Difference of Gaussians）**：金字塔 + 高斯模糊，取相邻高斯图像的差；在 DoG 中稳定出现的点 → scale invariant。

**旋转不变性**：

- 计算关键点邻域的**梯度方向直方图**（36 bins，每 10°）；
- 把主方向作为参考方向，旋转归一化。

**Descriptor**：

- 在关键点周围取 16 个 block，每个 block 一个 8-bin 梯度直方图 → 128 维 descriptor；
- 对光照、旋转、尺度、部分 affine 变化鲁棒。

**不变性类型**：illumination、scale、rotation、affine、full perspective（SIFT 主要覆盖前四者）。

#### 4.4 应用

- **Mosaicking**：匹配 SIFT → 估计 homography → 拼接图像；
- **Object recognition**：匹配特征点；
- **Robot localization**：用已知地图的特征匹配定位。

### 5. 本周与考试的关系

- 本周是 **Cheng Jun 部分 Topic 13**；下周 **Topic 14** 继续 3D（stereo images）。
- **Final Exam**：Cheng Jun 的 Q4 是**概念题**（25 分），3D 的**方法原理、优缺点、适用场景**是重点；不需要复杂计算。
- **Assignment 2**：Cheng Jun 部分；系统允许**无限次提交**；5 页是建议，不是硬性上限；**不需要 revised design**；重点是 own design + AI proposal + 四点比较。

### 6. ⭐ 本周考点速查

| 考点 | 要点 |
|---|---|
| **ToF** | 测往返时间；背景光/多反射/干扰 |
| **LiDAR** | ToF 的一种；ghost（假读数）、blooming（高反物体） |
| **Structured Light** | 投图案；不适合室外 |
| **SfM** | 多图 + 对应点 → 3D 结构 + 相机运动 |
| **Stereo** | 双目视差 → 深度；下周讲 |
| **Perspective projection** | `x = f X / Z`；非线性、深度丢失 |
| **Extrinsic** | `R, T`；世界→相机 |
| **Euler angles** | roll(z)、pitch(x)、yaw(y)；旋转矩阵相乘 |
| **SfM 输入/输出** | 输入 pixel correspondence；输出 3D points + camera poses |
| **Harris** | 角点检测；旋转鲁棒、尺度不鲁棒 |
| **SIFT** | scale/rotation invariant；detection/description/matching |
| **Scale space** | pyramid + DoG；找尺度不变关键点 |
| **SIFT descriptor** | 16 blocks × 8 bins = 128 维；梯度方向直方图 |
| **不变性** | illumination、scale、rotation、affine、perspective |
| **应用** | mosaicking、object recognition、robot localization |

### 7. 本周要点小结

- **3D 获取**：主动（ToF、LiDAR、Structured Light）vs 被动（SfM、Stereo）；各有优缺点。
- **相机模型**：透视投影 `x=fX/Z`；外参 `R,T`；内参 `f`；Euler angles 描述旋转。
- **SfM**：从多张图像 + 特征对应，同时恢复 3D 结构和相机运动；经典 orthographic、新法 perspective、近年 deep learning。
- **特征点**：Harris（角点，旋转鲁棒）；SIFT（scale/rotation invariant；pyramid + DoG + 梯度直方图 descriptor）。
- **考试**：Cheng Jun Q4 是概念题；重点记方法原理、优缺点、应用，不需要复杂推导。

---

> **下一周（Week 13）预告**：继续 **3D**（Topic 14），重点是 **stereo images / 双目视觉**：视差、深度恢复、极线几何等。Week 13 也是最后一周；Final Exam 的 Q4 来自 Cheng Jun 部分（概念题）。
