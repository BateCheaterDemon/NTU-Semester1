---
name: ee6497-course-info
description: EE6497 模式识别与深度学习的考核结构、关键日期与任课教师（以官方课件 PDF 为准）
metadata:
  type: project
---

EE6497 Pattern Recognition and Deep Learning（NTU，AY26-27 Semester1）。

**任课（以官方课件 PDF 为准，非转写）**：前 7 周（Week 1–7）**Tay Wee Peng**（wptay@ntu.edu.sg）讲模式识别/概率建模；recess week 后 Week 8–13 **Wang Lipo**（elpwang@ntu.edu.sg；办公室 **S1-B1C-98**，电话 6916 3162 ext.3013，随时可 drop by，约时间更保险）讲深度学习。

**考核占比（PG 研究生 EE6497）**：
- Final Exam 期末 60%（可带一张双面 A4 reference sheet，手写或打印均可，无便利贴；无有效 LOA/MC 缺考记 0）
- Quiz ×2 各 10%，共 20%（同样可带 A4 reference sheet；Quiz 1 在 Week 7 覆盖 Week 1–4，Quiz 2 在 Week 12 覆盖 Week 8–11；线上题但需到 lecture theater 现场自带 laptop 完成，经 NTULearn）
- Homework ×2 各 5%，共 10%（不允许迟交，提交单个 PDF；**Homework 1 已于 2026-09-11 23:59 截止并批改**；**Homework 2 已在 Week 11 前后发布，due date 推迟到 Week 12 末**（老师 Week 10 原话 "end of week 12"，以 NTULearn 为准））
- ⭐ **Quiz 2（Week 12）具体安排（Week 11 亲述）**：Week 12 课上 **21:00 左右**开始；老师说已发 **practice quiz**，题量/难度与真题相似；范围 **Week 8–11**；可带 A4 reference sheet；线上题但需到 lecture theater 用自带 laptop 经 NTULearn 完成。
- Class Participation 5%（PG；UG 为 10%）—— **Wooclap** 答题，13 次讲座参加 ≥9 次且 attempt 即满分，答错不扣分；必须经 NTULearn 登录进 Wooclap 才能记录出勤
- Survey Report 5%（仅 PG，约 Week 13）

**Wang Lipo 部分（Week 8–13）要点（Week 8 亲述）**：
- 课程分三块：NN/DL 导论 → 训练（shallow + deep）→ CNN；**其他网络结构放在 supplementary folder 作选读**（课上不覆盖）。
- **Python 编程不考**（"not in the final exam or in the quiz"），但作业**会包含编程**；**用 ChatGPT/AI 写程序他不禁止**。
- ⭐ **HW2 内容（Week 9 亲述）**："We're going to give you a homework that you're going to **train on your network to approximate a function**"——即用神经网络逼近一个函数，并借此说明"不需要很多 neuron"。预计 Week 11 前后发布。
- 考试形式补充（Week 9）：final exam 允许**笔 + 计算器手算**（"You just use your pen… maybe a calculator"），会有需要逐步计算 forward/backward 的题。
- 讲座 19:30–21:30 档（3×50 min），中途休息 10 分钟；**Week 8 忘记开 Wooclap**，**Week 9 已恢复正常**（课后 Wooclap 答题："if you get it wrong, you also get attendance… record the participation, not the score"——只记参与、不记分数）。
- Week 8 内容 = Part 2.1 Introduction to NN & DL（神经元模型、线性可分性、XOR 需多层 → universal approximation）。
- **Week 9 = Part 2.1 续**（多层网络设计、forward propagation、universal approximation）；**Week 10–11 = Part 2.2 Training Deep Networks**：
  - Week 10 前半：MLP forward、softmax、sigmoid/tanh/ReLU/Leaky ReLU、cross-entropy/MSE、gradient descent、backprop、mini-batch/SGD、momentum、Adam、learning rate/scheduling、vanishing gradient；
  - **Week 11 后半**：generalization（under/overfitting）、L2/L1/elastic net、dropout、early stopping、batch normalization、hyperparameter tuning（grid/random/Bayesian）、K-fold CV、deep vs shallow；然后进入 **CNN 导论**（MLP 不适合图像 / translation；Hubel & Wiesel；Neocognitron/LeNet/AlexNet；convolution 与 cross-correlation；local receptive field、parameter sharing、pooling、ResNet/DenseNet）。
  - ⚠️ CNN 部分在 `week11.txt` 转写中，**`Part 2.2_Training(1).pdf` 未包含 CNN slides**。
- **Week 12 = Part 2.3 Convolutional Neural Networks（CNN 详解）**：MLP 不适合图像（translation）、Hubel & Wiesel、Neocognitron/LeNet-5/AlexNet、convolution（数学 flip vs 深度学习 cross-correlation）、local receptive field/parameter sharing、pooling、输出尺寸 `(W-F+2P)/S+1`、参数量 `F*F*C*K+K`、Flatten/FC、ResNet；Pytorch `Conv2d` shape `[N,C,H,W]`。**Quiz 2 在本周课后进行**（覆盖 Week 8–11，CNN 本周新内容不考）；本周是最后一次 face-to-face，Week 13 改 online。
- **Week 13 = Part 2.4 Examples & Reviews（online）**：`6497/week13/Part 2.4_Examples_Reviews.pdf`（37 页）。⚠️ `week13/week13.txt` 只有 191 字节且全是 ASR 乱码，**不可用**，笔记完全据 PDF。老师给出**考试范围准则**："All materials that I went through in lectures may be subject to exam, unless otherwise noted. Materials that I did not go through in lectures will not be examed."（⇒ supplementary folder 里未讲的网络结构**不考**）。内容全是 Final 题型样板：perceptron OR/AND 设计（`W=(1,1)`，b 分别 −0.5/−1.5）、3 层网络（4 隐藏神经元画 4 条边 + 输出 AND，0 权重屏蔽）、GD 四步、表达能力（线性+阶跃**不能**表示 hinge loss / 二次多项式，**能**表示分段常数）、训练曲线诊断（gap 大=overfit，两边都低=underfit）、linear regression 手算（`y=4/3`，MSE `2/9`）、basis function 覆盖问题、CNN shape/参数量表（**BN 有 2C 个参数**；FC 参数 `(输入+1)×输出`）。

**HW1 反馈（来自 Quiz 1 review session）**：批改时把 "EM algorithm" 当作 Baum-Welch 的写法**没有扣分**，但 Tay 明确提醒 **Quiz/Final 里必须具体写 Baum-Welch，只写 EM 会扣分**。

**⭐ Final 具体形式（据 `6497/final/` 三套往年卷 IE4497/EE6497 2023-24 S2、2024-25 S2、2025-26 S2）**：**2 小时、4 题 × 25 分、全部必答、restricted open book**（一张双面 A4 reference sheet，不能贴便签）；试卷附 **Appendix A（常见分布）** 与 **Appendix B（DL 公式）**。题型高度稳定：Q1 = MLE/MAP/EM（Bernoulli/Exponential/截断几何 + 共轭先验），Q2 = HMM（joint/likelihood/Baum-Welch）或 Sampling/MCMC（rejection/importance/MH/Gibbs），Q3 = CNN shape/参数量/softmax/卷积手算，Q4 = ReLU 网络理论（kink/|x|/万能逼近）。旧卷有 PyTorch/NumPy 代码题，但 **Wang Lipo 明确说编程不考**，可跳过。复习资料：`6497/final/EE6497_Basics_Review.pdf`（21 页基础）与 `6497/final/EE6497_Final_Review.pdf`（22 页真题题型）。

**权威来源**：`6497/week1/1_Introduction.pdf`（官方课件，57 页）、`6497/week1/Week 1.pdf`（标注讲义，AY26-27-S1）。笔记见 `6497/Learning_note.md`。

相关：[[semester1-repo-purpose]]、[[transcript-quality-noise]]
