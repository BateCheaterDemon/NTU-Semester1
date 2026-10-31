---
name: ee6222-course-info
description: EE6222 Machine Vision 的考核结构、任课教师分工与课程布局（以官方讲义 PDF 为准）
metadata:
  type: project
---

EE6222 Machine Vision（NTU，AY26-27 Semester1，School of EEE）。注意用词是 Machine Vision（强调"机器"理解视觉信息）。

**任课分工（以官方讲义 PDF 为准）**：
- 前 9 周（Week 1–9，Topic 1–10）**Jiang Xudong**（exdjiang@ntu.edu.sg，IEEE Fellow，S1-B1c-105，personal.ntu.edu.sg/exdjiang），course coordinator。背景：UESTC 本硕、德国汉堡大学 PhD，I2R 后 2004 起 NTU。研究 fingerprint→face→pedestrian detection，近年转 AI/深度学习。
- 后 4 周（Week 10–13，Topic 11–14）**Dr. Cheng Jun**，讲 Video Analysis / Video Recognition / 3D Machine Perception / 3D Machine Vision。

**考核占比**：
- Final Exam 期末 **60%**：**4 题 / 3 小时**。其中 **3 题来自 Jiang Xudong 部分（Topic 1–10）**，第 4 题来自 Cheng Jun 部分（Topic 11–14，纯英文简答）。
  - ⭐ **Jiang Xudong 亲口公布的命题范围（Week 9，2026-10）**：
    | 题 | 来源 | 备注 |
    |---|---|---|
    | Q1 | **Topic 3**（image noise and enhancement） | 更偏 **enhancement** 而非 denoising |
    | Q2 | **Topic 5**（MAP rule 与基于 MAP 的分类器设计） | — |
    | Q3 | **Topic 9 + 10**（Neural Network / CNN / Transformer） | — |
  - **不考**：Topic **1、2、4、6、7、8**。
  - 老师强调："I will never test your skills, but I test your **understanding**"——考的是 fundamentals，不是具体 corner case。
- Continuous Assessment (CA) **40%**：
  - Quiz **10%**：**Week 7**，课堂内 **30 分钟**。
  - Assignment ×2 共 **30%**（各 15%）：take-home mini-project + report（论文形式）；一份来自 Jiang Xudong 部分、一份来自 Cheng Jun 部分。
  - ⭐ Assignment 允许用 generative model（AI）生成报告，但学生须**完全负责**：逐字审阅、理解、**纠正 AI 的错误**；原样照搬不改判为 wrong/作弊。
  - ⭐ **Assignment 1（Jiang 部分，15%）：Dimensionality Reduction for Classification**。主题 = 降维 + 分类，可用任意公开高维数据集或合成数据、任意语言（Python/Matlab/…），**降维与分类的参数只能由训练数据确定**；报告 4–5 页（含图表与参考文献），程序代码放附录。
    - **提交**：把报告 PDF 上传 **NTULearn**，**截止 2026-10-25（Week 10 末）**。
    - **文件名规则**：学生证姓名 + 学号，例如 `HOEJIUNTIAN-U2203856C`。
    - 原文见 `6222/assignment1/Assignment.pdf`；工作目录 `/home/qwx/NTU/6222assignment1/`（手写 PCA/LDA 人脸识别 pipeline + report）。
  - **Assignment 2（Cheng Jun 部分，15%）**：**Week 10 课堂发布**（"available online tonight"）；主题 = **video generation network proposal + 与 AI proposal 比较**。Week 11 更正：**不需要 revised design**；Part 1 写自己的设计，Part 2 按四个 points 比较 AI proposal（差异、AI 弱点等）。**在线提交系统截止约 2026-11-23 23:59**（转写 "November 23 … 59 seconds" 略含糊，以 NTULearn 公告为准）。

**课程进度（Cheng Jun 部分）**：
- **Week 10 = Video (Part I)**；**Week 11 = Video (Part II)**：object detection & tracking、Re-ID / JDE、action recognition（LRCN / C3D / two-stream / Hidden Two-Stream）、video enhancement（motion blur / PSF / blind deconvolution / turbulence）、optical flow（brightness constancy、aperture problem）、video segmentation（FCN / U-Net / temporal consistency）。
- ⭐ **Week 11 考试说明**：Final 4 题 × 25 分；Cheng Jun 的 **Q4 是概念题，不考计算**（往年题偏计算，但本学期他的部分考 concept/understanding）；不要战略放弃 Q4。
- **Week 12–13 = 3D**（Topic 13–14：3D Machine Perception / Machine Vision；VLA、Vision-Language Navigation 等前沿）。

**课程布局**：14 Topics。Topic 1–3 图像处理基础（image fundamentals / LSI & transforms / enhancement），4–5 识别决策（matching→classification、MAP decision），6–8 传统机器学习（统计估计→手工特征→特征选择/降维），9–10 深度学习（MLP→CNN→Transformer），11–14 Video + 3D（Cheng Jun）。

**权威来源**：`6222/EE6222_lecturenote1to9.pdf`（Jiang Xudong 官方讲义 1–9，约 83+ 页，覆盖 Topic 1–9 前段）。笔记见 `6222/Learning_note.md`。

**6222 特有的转写噪声**（整理笔记时按 PDF 修正）："Ji Shi Dong"→Jiang Xudong、"19/night"→light、"cner/nel"→color、"st g/quam"→st-gram→histogram、"ninear/menia"→linear、"ATI"→LTI、"compion"→convolution、"fear/fuel/fue"→Fourier、"impasse"→impulse、"no pass filter"→low-pass filter、"Niclie rate"→Nyquist rate、"gama/comma"→gamma、"environment"→invariant。

相关：[[semester1-repo-purpose]]、[[transcript-quality-noise]]、[[note-language-english-terms]]、[[coursework-notes-skill]]
