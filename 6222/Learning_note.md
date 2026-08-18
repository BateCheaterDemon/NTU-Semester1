# EE6222 — Machine Vision（机器视觉）

> 课程学习笔记总览。每周一节，按周总结重点内容。
> 第一周（开课周）特别关注考核要求、任课教师、课程结构等行政性信息。
>
> **权威来源说明**：本笔记先由 `week1.txt` 录播转写整理，再以 `EE6222_lecturenote1to9.pdf`（官方讲义，Jiang Xudong，2026-08-11）核对修正。转写有大量语音识别噪声（如 "Ji Shi Dong" 实为 Jiang Xudong、"19/night" 实为 light、"cner/nel" 实为 color、"st g/quam" 实为 histogram、"ninear/menia" 实为 linear、"ATI" 实为 LTI、"compion" 实为 convolution、"fear/fuel" 实为 Fourier），均以 PDF 为准修正。

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

> **笔记约定**：本课英文授课、英文考试，核心术语保留英文（machine vision, image, pixel, convolution, impulse response, LSI/LTI, filter, filter mask, histogram, gray level, color space, RGB, HSI, LBP, HOG, Fourier transform, DFT, sampling, Nyquist, feature extraction 等）。中文用于组织句意与补充释义。
