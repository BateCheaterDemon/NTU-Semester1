---
name: past-paper-summary-workflow
description: quiz/往年题/final 的逐题详解学习文档工作流与存放约定
metadata:
  type: feedback
---

用户希望把每门课的 **quiz / 往年题 / 期末往年题** 单独整理成**逐题详解学习文档**（不只是转写笔记），用于考前学习。

**Why**：考核题是考点最集中的材料，逐题给出"题目+答案+详解+映射回 Learning_note.md 考点"比单纯看笔记更能抓重点；且用户明确说"以后其他 quiz 往年题或期末往年题可以给我总结，我们来学习"。

**How to apply**：
- 用户在某课程下添加 `quizN/`、`final/` 等文件夹并放入题目图片/扫描时触发。
- 产出：在该文件夹下写 `<QuizN_详解.md>` 或 `<Final_详解.md>`。
- 格式：逐题（题目精简 + 答案 + 详解 + 考点映射）；T/F 题用表格；计算题（PMX/OX/CX/编码等）**手算验证**并校验合法性；论述题给要点清单。
- 图片用 Read 读取（视觉模型会分析）。
- 拿不准处标【存疑】并说明，**不编造官方答案**。
- 文末附"考点速查表"映射回 Learning_note.md 的 Week 节号 + "易错点清单"。
- 末尾留"下次更新"占位，便于后续 quiz/final 追加。

首份产出：`6407/quiz1/Quiz1_详解.md`（现题 25-26 S1 + 往年 24-25 S2，含 PMX/OX/CX 三种 crossover 手算、trinary 编码、NFL 论述、fitness proportional 阶段性）。

相关：[[ee6407-course-info]]、[[coursework-notes-skill]]、[[semester1-repo-purpose]]
