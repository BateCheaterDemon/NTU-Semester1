---
name: ee6407-course-info
description: EE6407 遗传算法与机器学习的考核结构、分工与关键日期（Assignment 1&2 合并 PDF 10/19 截止；Quiz 2 于 11/10）
metadata:
  type: project
---

EE6407 Genetic Algorithms and Machine Learning（NTU，AY26-27 Semester1）。

**课程分工**：前 4 周（Week 1–4）**A/P LIM Meng Hiot**（emhlim@ntu.edu.sg，S1-B1b-46）讲遗传算法/进化计算；**Week 5–13 由 Mao Kezhi 教授**讲机器学习部分（CA Part 2）。

**考核占比**：
- Continuous Assessment (CA) **40%**
  - CA Part 1（Lim 的 4 周内）：**仅一次 Quiz 占 10%**，**闭卷**、受控环境书面作答，在 **Week 4** 进行；**无作业、不考核出勤**（来否自便）。
    - ⭐ 具体细节（Week 2 末宣布）：**9 月 1 日 9:30–10:30**，约 15 分钟；三考场 **LT 19A / LT 2A / LT 5**（去哪个在 NTULearn 公布）；隔座就坐，带 ID+笔，**不需计算器**，禁手机/智能设备。
  - CA Part 2（后半 ML 部分，Mao Kezhi）：占 **30%** = **Assignment ×2 共 20%** + **Quiz 2 占 10%**。
- Final Exam **60%**（3 小时，覆盖全课程；4 题中约 3 题来自 ML 部分）。

**⭐ 两次 Assignment（合计 20%，ML 部分重点）**：
- **Assignment 1**（Week 7 发布）：同一 Iris 数据（120 训练 / 30 测试，4 连续特征），用 **normal/Gaussian 建 class-conditional density 的 Naïve Bayes**，预测测试集 class label。
- **Assignment 2**（**Week 8，约 10/12–13 发布**）：**同一数据集**，要求设计 **linear FDA（Fisher Discriminant Analysis / LDA）**分类器——可用闭式公式或解 eigenvalue problem，并提醒检查类别符号方向（投影后类 1 应在正侧）。
- 两份**合并为一个 PDF** 提交（**不含代码**），内容 = 设计说明 + 测试样本预测结果表（sample number → label），上传 NTULearn 的 Assignments 文件夹。
- **截止：2026-10-19（周一，Week 10）**。
- 工作目录 `/home/qwx/NTU/6407assigment1/`（含数据、Assignment 1.pdf 与我给出的 A1 解题方案）。

**⭐ Quiz 2**：**10%**，**2026-11-10（周二）9:30–10:30**（Week 13，紧接课后；因 ~800 人选大阶梯教室，否则改周六/晚上）。
（注：`Learning_note.md` 第 29 行写作"11 Nov 周二"，但 2026-11-11 是周三，**应以 11-10 周二为准**。）

**课程进度与收尾**：
- Week 8 = **Linear Discriminant Analysis / FDA**（Fisher criterion、within/between-class scatter、多类推广为 c−1 个判别函数）；**Week 9 = Linear SVM**；Week 10 = clustering 等。
- **教学于 2026-11-13（周五）结束**，其后 Week 14 为复习周（11/16–20），**期末考试随后开始**（转写提到"20 号那个周一"但含糊，实际以教务排期为准）。

**要点**：前 4 周只靠一次闭卷 Quiz（10%）评估；CA 40% 中 ML 部分占 30%（作业 20% + Quiz 10%）；期末 60% 中约 3/4 题来自 ML 部分。

**权威来源**：`6407/week1/L1(2-1).pdf`（官方课件，作者 Meng-Hiot Lim）、`6407/week8/ML-Slides4.pdf` + `week8/week8.txt`（LDA 与 Assignment 2 发布公告）。笔记见 `6407/Learning_note.md`。

相关：[[semester1-repo-purpose]]、[[ee6497-course-info]]、[[transcript-quality-noise]]
