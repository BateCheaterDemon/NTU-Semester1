---
name: ee6406-course-info
description: EE6406 Analytic and Ensemble Machine Learning 的考核结构、教学分工与 ASR 转写噪声（以官方讲义 PDF 为准）
metadata:
  type: project
---

EE6406 Analytic and Ensemble Machine Learning（NTU，AY2026-27 S1，School of EEE）。注意：SPM（Signal Processing 方向）2026.08 新生此课为 SE（必修性选修），其余 program 为 GE，但考核/考试/注册流程无差异。

**教学分工（2+6+5）**：
- Week 1–2 **Zhiping Lin**（ezplin@ntu.edu.sg，course coordinator，SPM program director）：Lecture 1 Introduction + Lecture 2 Data Preprocessing + Lecture 2 Supplement（Mathematics Review）。
- Week 3–8 **Kar-Ann Toh**（转写误为 "proto/Tok"；part-time，延世大学 emeritus，machine learning & pattern recognition，主教材主作者）：**Analytic Learning 主体** L3–L8。
- Week 9–13 **Simon Liu**（转写误为 "Simon Le/Dell"；part-time，Trust Decision 首席 DA/AI 官，多伦多 PhD；亦教 EE6405 NLP）：**Ensemble Learning** L9–L13。

**考核占比**：
- Final Exam **60%**：4 题，2.5 题来自 Part 1（Week 1–8）、1.5 题来自 Part 2（Week 9–13）。
- CA（仅 quiz）**40%**：CA1 10% **Week 5**、CA2 15% **Week 8**（recess 后）、CA3 15% **Week 12**。
- 三次 quiz 均 **online 但 in-class（必须到课）**、**closed-book**、需 **lockdown browser**（PC+Windows 最稳，Mac/Unix 可能有问题，iPad 可用但不稳）；计划 Week 4 开头 10–15 分钟 try-run 测设备。**无日常考勤**——平时不点名，仅在三次 quiz 日须到场。
- **Lecture 1 不进 quiz/exam；Lecture 2 起会进。**

**课程布局**：L1 Introduction → L2 Data Preprocessing（+数学复习补充）→ L3–L8 Analytic（linear parametric models→score functions→over/under-determined regression→advanced classification→penalized learning→performance evaluation & statistical inference）→ L9–L13 Ensemble（bagging/boosting→Random Forest/Adaboost/Gradient Boosting→XGBoost/LightGBM→RL+ensemble→工业应用）。

**主教材**：Toh, Zhuang, Liu, Lin, *Analytic Learning Methods for Pattern Recognition*, Springer 2025（NTU 图书馆免费电子版，每章有习题+解答）。

**权威来源**：`6406/weekN/EE6406-LectureN-LZP-v1.pdf` 与 `EE6406-Lecture2Suppl-LZP-v1.pdf`（Lin 讲义）。笔记见 `6406/Learning_note.md`。

**6406 特有的转写噪声**（整理时按 PDF 修正）："Dinger Ping/P L"→Zhiping Lin、"proto/Tok"→Toh Kar-Ann、"Simon Le/Dell"→Simon Liu、"seemal/on sample"→ensemble、"sample learning"→ensemble learning、"fear"→field、"etction"→extraction、"n by n/n to n dives"→end-to-end、"mean ski/Mosk/means co ski"→Minkowski、"humming"→Hamming、"matrix"常实为 metric、"lacung/lacungan/logngan"→Lagrange(Lagrangian)、"copian"→Jacobian、"fi"→affine、"S score/score stang"→z-score(standardization)、"packing lot"→log、"sikmoi"→sigmoid、"biliion/valian/variant"→variance、"neumic/neumatical"→numeric(numerical)、"Odiner"→ordinal、"chromo"→cofactor、"alg gate/adj gate"→adjugate、"atom"→codomain。

相关：[[semester1-repo-purpose]]、[[transcript-quality-noise]]、[[note-language-english-terms]]、[[coursework-notes-skill]]
