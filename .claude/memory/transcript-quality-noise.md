---
name: transcript-quality-noise
description: 录播转写 txt 有大量语音识别噪声，整理笔记时需还原正确术语
metadata:
  type: feedback
---

录播转写文本（`<课程编号>/weekN/weekN.txt`）由语音识别生成，噪声很多：术语被错拼（"Bas"→Bayes、"Bui/Bai/Burdi/Berdi"→Bernoulli、"gaucin/galcin/gcusm"→Gaussian、"pyro/viral"→prior、"posture/posior"→posterior、"livelihood"→likelihood、"data"→θ 等），人名也被错拼（"Tang"→Tay Wee Peng、"Depo"→Wang Lipo），平台名错拼（"CLAP"→Wooclap、"NTM/anti"→NTULearn），且有大量重复填充词。

**Why:** 直接照抄转写会产出无法阅读、且事实错误的笔记（人名/平台名/占比都可能错）。
**How to apply:** 整理 `Learning_note.md` 时，**优先对照同周文件夹内的官方课件 PDF 修正**，以 PDF 为准；还原正确的数学/ML 术语与人名平台名，不要照抄转写错字；保留术语英文原名。

相关：[[semester1-repo-purpose]]、[[ee6497-course-info]]
