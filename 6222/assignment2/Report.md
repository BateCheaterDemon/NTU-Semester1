# Designing a Video Generation Network: My Solution versus an AI Solution

**EE6222 Machine Vision — Assignment 2**

Name: [Your Name]　Matric: [Your Matric No.]　Date: 9 November 2026

> **AI-use statement.** Part 1 was completed before the Part 2 AI session was opened, and the Part 2 tool was given only the assignment prompt (Appendix A), not Part 1. I used Claude Code (Anthropic) to help draft and check the report; I verified the quantitative and factual claims attributed to the AI against the course notes, primary papers, official documentation and simple calculations (§2.4). I revised the design myself and take responsibility for all content.

## Part 1 — My Proposal (written before the Part 2 AI session)

### 1.1 Task and scope

The system generates short, **clearly labelled synthetic videos of Donald Trump** for educational and research demonstrations. Inputs are (i) a text script, (ii) a target speech track (a recording or TTS voice), and (iii) 3–5 identity reference portraits. The output is a 15–30 s, 25 fps, 720p MP4 clip with a persistent visible watermark (“AI-GENERATED — NOT REAL”), a visible/audible disclaimer, and C2PA provenance metadata. I assume a single English speaker, frontal-to-mid head pose, ordinary indoor/outdoor settings, and a research demonstration rather than a product. The system is access-controlled and is never used for political persuasion, endorsement or public release.

### 1.2 Data

**Sources and legal basis.** I would use only footage with a clear legal basis: official White House videos (US federal works are generally public domain), C-SPAN material under its non-commercial educational terms (to be confirmed by the institution’s legal office), and licensed interviews or debates. Scraping arbitrary YouTube clips is excluded because uploaders, not the platform, own the copyright. Because the subject is a public figure and the output is a political likeness, the protocol also requires ethics-review approval, a documented public-interest justification, and no redistribution of the raw corpus.

**Composition and scale.** About 20 h of raw video should yield 8–10 h of clean speech footage: roughly 2,000 clips of 5–20 s, covering 200+ sessions with different outfits, backgrounds, lighting and speaking styles; 50–100 high-resolution reference stills; about 10 h of aligned audio; and about 100k words of transcripts.

**Preprocessing pipeline.** (1) Shot-boundary detection and duplicate removal (PySceneDetect + perceptual hash). (2) Face detection and tracking (RetinaFace + ByteTrack), then identity verification with ArcFace so that only the target identity is retained. (3) Quality filtering: reject motion blur, occlusion, extreme pose, poor exposure and non-frontal faces; keep a balanced distribution of yaw, pitch, expression and lighting. (4) Alignment and cropping to 512×512 with a five-point similarity transform. (5) Audio extraction, denoising (Demucs) and loudness normalisation. (6) ASR with word timestamps (Whisper large-v3) and phoneme alignment (Montreal Forced Aligner). (7) 3DMM/FLAME fitting (EMOCA or Deep3DFaceRecon) for identity, expression, jaw and pose coefficients, plus face-parsing masks and landmarks. (8) Captioning and metadata (transcript, emotion, pose, source, licence).

**Organisation and splits.** Data are stored as WebDataset shards with a JSON metadata index and a datasheet. I split **by source event/date, not by random frame**, in an 80/10/10 ratio so that the same event never appears in two splits. The held-out test set contains 100 clips from unseen backgrounds and lighting, 20 unseen scripts, and 10 unseen reference images. It is fixed before training and never used for model selection.

### 1.3 Network architecture

The design, **ID-Vid**, is an **audio- and text-conditioned latent video diffusion model with an identity reference branch and a 3DMM control branch**. It combines the course’s video-diffusion architecture (a 3D UNet with spatial–temporal attention and relative positional embeddings along time) with an identity-preserving conditioning path.

- **Condition encoders.** A text encoder (T5 or CLIP) encodes the script; a speech encoder (wav2vec 2.0 or Whisper) produces frame-aligned audio features; an identity encoder (ArcFace/AdaFace) plus a reference network encodes 3–5 portraits; a small audio-to-3DMM transformer predicts expression, jaw and head-pose coefficients from the speech.
- **Latent video generator.** A pretrained open video-diffusion backbone (e.g., Stable Video Diffusion or CogVideoX) is fine-tuned with LoRA. A 3D causal VAE compresses pixels by 8×8 spatially and 4× temporally, so denoising happens in a compact latent space; the backbone keeps its spatial–temporal attention and relative temporal positional embeddings.
- **Conditioning paths.** Audio enters through cross-attention in the temporal/mid blocks; the script enters through text cross-attention; identity enters through reference-frame cross-attention (IP-Adapter style); predicted 3DMM/landmark/depth maps enter through a ControlNet-style branch, so mouth shape, jaw motion and head pose are explicitly controlled rather than left to the prompt.
- **Output and provenance.** The VAE decoder produces frames; RIFE interpolation raises the rate to 25 fps; a watermark and C2PA manifest are applied last.

At inference, the pipeline is: script + speech + references → encoders → 50-step classifier-free-guided denoising → VAE decode → interpolation → watermark. Long videos are generated as 4–8 s overlapping windows, each anchored on the last frame of the previous window and blended in latent space.

**Identity consistency.** Identity is a global attribute, so I enforce it at three levels: (i) an ArcFace identity loss on sampled generated frames against the reference set; (ii) reference-image cross-attention that injects appearance into every denoising step; (iii) fixed 3DMM identity coefficients, so only expression and pose vary. I select checkpoints by held-out identity similarity, not only by FVD.

**Temporal consistency.** Temporal consistency is local, so it uses different mechanisms: 3D temporal attention; shared latent noise across frames; relative time embeddings; a flow-warping loss that penalises changes inconsistent with RAFT optical flow; and overlap-and-blend plus first-frame anchoring for long clips.

**Training objective.** The model minimises *L = E[||ε − ε_θ(z_t, t, c_text, c_audio, c_id)||²] + λ_id·L_id + λ_sync·L_sync + λ_flow·L_flow + λ_lm·L_lm*, where *z_t* is the noisy latent, the *c* terms are the conditions, *L_id* is the ArcFace cosine loss, *L_sync* is a SyncNet-style audio–lip contrastive loss, *L_flow* is the flow-warping error, and *L_lm* is a landmark loss. The weights are tuned on the validation split.

### 1.4 Resources

| Item | Specification | Estimated cost |
|---|---|---|
| Data and annotation | 3–5 TB raw + processed + backup; 150–200 person-hours for quality/transcript checks | ~US$3–4k + US$200/month |
| Audio→3DMM predictor | 1×A100 80 GB, 2–3 days | ~70 GPU-hours |
| Video-diffusion LoRA | 8×A100 80 GB, 7–10 days | ~1,500–2,000 GPU-hours |
| Identity/sync adapters | 4×A100 80 GB, 3–5 days | ~300–500 GPU-hours |
| Inference | 1×A100; 5–10 min per 30 s clip at 50 steps, 1–2 min with 4-step distillation | ~0.2 GPU-hours/clip |

Software: PyTorch, Hugging Face Diffusers, xFormers/FlashAttention, DeepSpeed/FSDP, FFmpeg, InsightFace, MediaPipe, Whisper, Montreal Forced Aligner, PySceneDetect and Weights & Biases. Pretrained models: SVD/CogVideoX (video diffusion), wav2vec 2.0/Whisper (speech), ArcFace/AdaFace (identity), EMOCA/Deep3DFaceRecon (3DMM) and RIFE (interpolation); all licences require review.

The total training budget is about **2,000–2,600 A100 GPU-hours**, or roughly **US$5k–8k** at US$2–3 per GPU-hour; on the university cluster the monetary cost is lower but queue time is longer. I would first run a one-day, one-GPU pilot on 1 h of data. The target is 720p, not 1080p, because native 1080p diffusion multiplies compute by roughly 2–2.5× for a modest perceptual gain; super-resolution is optional and must preserve identity.

### 1.5 Design rationale, assumptions, limitations and trade-offs

**Why diffusion rather than a GAN?** GANs sample quickly and produce sharp faces, but adversarial training on a single identity is prone to mode collapse and artefacts, and control is indirect. Diffusion gives broader mode coverage, stable training and clean conditioning through cross-attention and ControlNet; its slow sampling can be reduced by distillation. I would keep a GAN-based talking-head model (e.g., Wav2Lip/SadTalker) as a **baseline**, not as the final system.

**Why a pretrained backbone plus LoRA?** Training a video diffusion model from scratch on 10 h of data is infeasible and would overfit. Fine-tuning reuses learned appearance and motion priors; LoRA reduces trainable parameters and memory and lowers the risk of catastrophic forgetting. The domain gap between generic video and formal speech is handled by the identity and 3DMM branches trained on the target data.

**Why a hybrid 3DMM branch?** A pure end-to-end model must discover the phoneme-to-mouth mapping from limited data. A 3DMM predictor supplies an explicit low-dimensional motion prior, improving lip sync and head motion. The risk is error propagation, so 3DMM is a **soft control signal** in a ControlNet branch rather than a hard rendering constraint, letting the diffusion model correct small errors.

**Assumptions.** English speech; mostly frontal faces; short clips; enough public-domain footage; ethics approval; minutes-per-clip latency. **Limitations.** Extreme poses, occlusion, strong emotion, singing and unusual prosody are under-represented; long videos may drift; TTS audio differs from real speech; the corpus over-represents formal speeches; identity metrics can be fooled by a static face; and realism is not appropriateness.

**Trade-offs.** I use moderate classifier-free guidance to balance fidelity and diversity; soft 3DMM control to balance realism and controllability; 720p plus a 4-step distilled sampler to balance compute and latency; 8–10 h of curated data to favour quality over quantity; and identity loss plus reference attention rather than face swapping to avoid a “pasted face” look and reduce deception risk.

### 1.6 Evaluation protocol

On the held-out split I would measure: **visual quality** by FVD and FID; **identity** by mean ArcFace cosine similarity plus human identity-recognition accuracy; **audio–visual sync** by SyncNet confidence and LSE-C/LSE-D plus phoneme–viseme accuracy; **temporal consistency** by RAFT flow-warping error, a flicker metric on static regions, and DINO/CLIP subject consistency; and a **20-person human study** rating realism, identity, lip sync and appropriateness in a randomised A/B test against Wav2Lip, SadTalker, LivePortrait and a generic text-to-video model. Ablations remove the identity branch, ControlNet branch, temporal attention and LoRA one at a time. Target criteria (to be confirmed on validation data) are ArcFace cosine > 0.55, SyncNet confidence > 0.8, human identity accuracy > 90%, and FVD below the strongest baseline; a clip that fails the identity or safety check is not released.

## Part 2 — AI-Assisted Proposal and Critical Comparison

### 2.1 How the AI proposal was obtained

I used **Claude Code (Anthropic)** in a fresh session on 9 November 2026 and gave it only the assignment task, without showing it my Part 1. The exact prompt is in Appendix A. This separation is deliberate: it gives an independent proposal rather than a paraphrase of my design. I then checked the AI’s claims against the course notes, primary papers, official documentation and arithmetic (§2.4).

### 2.2 Summary of the AI proposal

The AI returned a detailed proposal for a two-stage latent video diffusion system. The table condenses its main claims; the full response is retained in my project records.

| Aspect | AI proposal (condensed) |
|---|---|
| Data | 35 h of “rights-cleared” video: 18 h “public-domain C-SPAN and White House pool feeds”, 10 h Creative-Commons news, 7 h licensed archival interviews; VoxCeleb2, LRS3 and HDTF for pretraining; 6 h from a consenting voice actor. After filtering, “~22 h usable” and “~128,000 clips of 4–12 s”; split by event date (train 2011–2019, val 2020–2021, test 2022–2024). |
| Architecture | 3D causal VAE (8× spatial, 4× temporal, 16 channels) + 1.4B-parameter DiT (28 blocks, hidden 1536, 24 heads, 2×2 latent patches, 3D RoPE). Conditions: T5-XXL text; Whisper-large audio at 50 Hz; 512-d ArcFace embedding + 4 reference frames via IP-Adapter (rank 128); FLAME coefficients from audio. Stage 2: 180M 3D U-Net super-resolution to 1024×1024; 5–10 s at 25 fps; VideoSeal + C2PA. |
| Resources | 48× H100 80GB for six weeks, ~48,000 GPU-hours, ~US$110k at US$2.30/GPU-hour; 11 TB storage + 2 TB checkpoints; four researchers over 16 weeks. |
| Evaluation | FVD(I3D) < 400, FID < 12, ArcFace ≥ 0.65, SyncNet LSE-C ≥ 6.0 / LSE-D ≤ 8.0, LPIPS ≤ 0.12, RAFT warp ≤ 0.02, CLIP ≥ 0.28, aesthetic ≥ 5.0; 40-person human study with 2AFC (~75% detection); watermark > 95% after H.264/0.9×; DeepfakeBench AUC > 0.90; ablations. |
| Rationale and safety | Diffusion over GAN; DiT over U-Net; two-stage to control 1024p compute; event-level split; identity separated from motion; voice actor avoids voice cloning; internal-only, visible “SYNTHETIC” overlay, C2PA, political-content filter, EU AI Act. |

### 2.3 Similarities and differences

Both proposals use a **3D VAE + video diffusion backbone**, condition on text, audio, identity and 3DMM/FLAME motion, use reference-frame cross-attention plus an ArcFace identity loss, combine temporal attention with shared noise and a flow-warping loss, and evaluate with FVD/FID, identity similarity, SyncNet and a human study. The differences are mainly **scale and training strategy**: the AI trains a 1.4B DiT from scratch with 48 H100s and adds 1024p super-resolution; I fine-tune a pretrained backbone with LoRA on 8–10 h and stay at 720p. The AI’s data scale is larger on paper, but its clip counts and training schedule are internally inconsistent (§2.4). Its evaluation is stronger on safety and provenance, which I adopt; mine is stronger on legal data sourcing and on matching compute to data scale.

| Dimension | My proposal | AI proposal | Assessment |
|---|---|---|---|
| Data | 10–20 h public-domain/licensed; legal review; 8–10 h clean, ~2,000 clips; event split | 35 h “rights-cleared”; 22 h usable, “128k clips”; date split 2011–2024 | AI larger but internally inconsistent and misclassifies licences |
| Preprocessing | Face tracking, ArcFace filter, pose/quality filtering, 3DMM, ASR + phoneme alignment | Same core + RVM matting, CLIP aesthetic score, CLIP dedup | Convergent; AI adds useful filters |
| Backbone and conditioning | Pretrained SVD/CogVideoX + LoRA, 720p; text/audio/identity/3DMM ControlNet | 1.4B DiT from scratch + 1024p SR; T5/Whisper/ArcFace IP-Adapter/FLAME | Convergent design; AI is data-inefficient |
| Consistency | 3D attention, shared noise, flow loss, overlap, ArcFace loss | Same + cosine-masked blending, LPIPS on face crops | Convergent; AI’s blending detail is useful |
| Resources | 2,000–2,600 A100 GPU-hours, ~US$5–8k | 48,000 H100 GPU-hours, ~US$110k | AI is ~20× larger |
| Evaluation and safety | FVD/FID, ArcFace, SyncNet, RAFT/flicker, human study, ablations | Same + watermark, C2PA, detector AUC, label comprehension, 3 seeds | AI’s safety checklist is better; I adopt it |

### 2.4 Verification of weaknesses and unsupported claims

I checked the AI response by (i) unit and arithmetic checks; (ii) FLOPs and GPU-hour calculations; (iii) primary documentation (C-SPAN, C2PA, VideoSeal); and (iv) comparison with the course notes and published baselines. The four main findings follow.

**Finding 1 — the data counts do not add up.** The AI states “~22 h usable, segmented into ~128,000 clips of 4–12 s.” Check: 22 h is 79,200 s, so 4–12 s clips give **6,600–19,800 clips**, not 128,000; conversely, 128,000 clips of 4–12 s would require **142–427 h**. The split numbers confirm the error: “17 h, ~98k clips” implies 0.62 s per clip, and “2.5 h, ~15k” implies 0.6 s per clip. **Verdict:** internally inconsistent by roughly 6.5–19×. This matters because the clip count drives the number of training steps and the claimed compute.

**Finding 2 — the compute estimate is inconsistent and ignores attention cost.** The AI lists “22k Stage-1 base training … (~33k GPU-hours at 35% MFU)” and also itemises “48,000 GPU-hours: 2k VAE + 22k Stage-1 + 6k identity adapters + 8k super-resolution + 10k ablations.” Check: the itemised total is 48k, but if Stage 1 is 33k the total is 59k; 48 H100s × 6 weeks is only 48,384 GPU-hours, leaving no headroom for failed runs or evaluation. The phrase “48× H100 nodes” is also ambiguous: 48,000 GPU-hours corresponds to 48 GPUs, not 48 eight-GPU nodes (~387k GPU-hours). More importantly, the 6ND estimate (1.4B × 31,744 tokens × 6 ≈ 2.7×10¹⁴ FLOPs/sample) ignores the quadratic attention term. At 31,744 tokens, 28 blocks and d = 1536, attention adds about 12n²d per block ≈ 5.2×10¹⁴ FLOPs/sample, roughly **twice the linear term**, so the true total is about **three times** the 6ND estimate (~60–100k GPU-hours for Stage 1 at 35% MFU). **Verdict:** the budget is understated. I used the H100 SXM dense BF16 peak of ~989 TFLOPS and 35% MFU; the exact number depends on utilisation, but the order of magnitude is clear.

**Finding 3 — the data-licensing claim misclassifies C-SPAN and pool footage.** The AI claims “18 h of public-domain C-SPAN and White House pool feeds.” Check: C-SPAN’s own copyright policy says only **House and Senate floor proceedings** (shot with government cameras) are public domain; other C-SPAN-produced federal-event coverage is copyrighted and may be used for non-commercial educational purposes with attribution, not freely redistributed. White House “pool” footage is not automatically public domain either: it depends on who shot it, and network-owned pool footage remains copyrighted. **Verdict:** the “rights-cleared 18 h” is unsupported; legal review would likely reduce the usable public-domain hours and require licences for the rest. This is the kind of context an AI cannot verify on its own.

**Finding 4 — the watermark robustness claim is unsupported as stated.** The AI claims “watermark bit accuracy >95% after H.264 compression and 0.9× rescaling.” Check: the claim omits the CRF/bitrate, payload length and watermark strength; the 0.9× condition is milder than the 75% downscale used in published tests, but the missing CRF is decisive. The VideoSeal paper evaluates 64/128-bit payloads under H.264 at several CRF levels, and an independent benchmark of a 256-bit VideoSeal model reports ~0.99 bit accuracy on clean video but **~0.56–0.57 after H.264 CRF 23** and ~0.69 after 75% downscaling. **Verdict:** >95% may hold only for mild compression and short payloads; it cannot be stated as a general result. I would report a bit-accuracy-versus-CRF curve and specify the payload.

**Smaller issues.** (i) “95% bootstrap confidence intervals over three training seeds” conflates test-set sampling uncertainty with seed variance; with three seeds, report mean ± standard deviation and bootstrap the test clips. (ii) “100% C2PA validation” is a metadata check on the system’s own outputs, not evidence of misuse resistance, because C2PA can be stripped; pair it with the watermark and detector AUC. (iii) “output filter blocks statements about real political topics” has no mechanism; an audio-driven system needs ASR/transcript filtering plus human review, and semantic filters are bypassable. (iv) “the subject’s consent is unobtainable” is asserted, not demonstrated; the legal position depends on jurisdiction and purpose, so it should be a legal-review assumption.

**What this says about AI-generated proposals.** The AI is strong on standard architecture vocabulary and safety metrics, but its quantitative claims are not self-consistent. A reader who copied it would inherit a data scale, a compute budget and a legal position that do not survive arithmetic or a primary-source check.

### 2.5 Useful AI suggestions and my disposition

| AI suggestion | Disposition | Reason |
|---|---|---|
| Event/date split with a 2022–2024 hold-out | **Adopt** | My split was by event/source; a temporal hold-out also tests aging and appearance drift. |
| Consenting voice actor instead of a cloned voice | **Adopt** | Reduces biometric voice-cloning risk and makes the synthetic nature clearer; replaces “real or TTS” with “consenting voice actor or licensed TTS.” |
| Safety evaluation: watermark bit accuracy, C2PA, DeepfakeBench AUC, label comprehension | **Adopt with modification** | Good additions, but report watermark curves rather than a single >95% claim, and treat C2PA as provenance, not protection. |
| 1024p super-resolution conditioned on identity | **Modify / optional** | Keep 720p native; add SR only if ArcFace similarity is preserved, because SR can hallucinate identity details. |
| 1.4B DiT from scratch with full 3D attention | **Reject at this data scale** | 22 h cannot support 1.4B parameters; batch 512 × 300k steps is 153.6M samples, about 9,000 epochs over 22 h, a severe overfitting risk. Keep DiT/3D-RoPE only inside a pretrained backbone with LoRA and windowed attention. |
| Generic pretraining corpora (VoxCeleb2/LRS3/HDTF) | **Modify** | Useful for encoder pretraining, but licences and identity bias must be checked; do not fine-tune the identity branch on them. |
| Three seeds × 95% bootstrap and a 2AFC human study | **Adopt with corrected statistics** | Report mean ± standard deviation over seeds and bootstrap the test clips; the 2AFC and label-comprehension tests are valuable. |

### 2.6 Revised design after the comparison

The comparison changed my design in four places while confirming the core. I keep the **pretrained video-diffusion + LoRA backbone**, the identity reference branch, the 3DMM ControlNet, the event-level split and the watermark/C2PA pipeline. I adopt the **temporal hold-out**, the **consenting voice actor**, the **safety evaluation suite** and the **2AFC/label-comprehension study**. I modify the super-resolution stage to be optional and identity-checked, and I replace the vague content filter with a **script allow-list + ASR/transcript filter + human review**. I reject the 1.4B from-scratch DiT, the 48k H100 budget and the 128k-clip scale as inconsistent with the available data. The revised budget remains ~2,000–2,600 A100 GPU-hours and 8–10 h of curated data; the revised evaluation adds FVD/FID, ArcFace, SyncNet, RAFT/flicker, watermark bit-accuracy curves, detector AUC and a 40-person human study.

**Overall judgement.** The AI proposal is a useful reference for what a well-resourced lab might attempt, but it is not a drop-in plan. Its main value is the **evaluation and safety checklist** and the **temporal-split / voice-actor** ideas; its main risk is confident but inconsistent numbers. The human must own the feasibility calculation and the legal/ethical context.

## Part 3 — Conclusion: How AI Can Help Me Develop and Improve the Solution

AI is most useful to me as a **fast, broad design partner**, not as an authority. In this project it can (i) propose alternative architectures and baselines I might not recall, (ii) draft code scaffolding for data loading, training loops and evaluation, (iii) suggest metrics and ablations, and (iv) help me write and debug documentation. Its suggestions changed my design in concrete ways: I adopted the **temporal hold-out**, the **consenting voice actor**, the **watermark/C2PA/detector safety suite** and the **2AFC label-comprehension study**; I modified the **super-resolution stage** and the **content filter**; and I rejected the **1.4B from-scratch DiT** and the **48k H100 budget** as inconsistent with the available data and the assignment’s scope. The AI also produced four errors — inflated clip counts, an understated compute budget, a misclassified C-SPAN licence and an unsupported watermark claim — which I caught by arithmetic and primary sources. That mixed record is exactly why the assignment asks for verification rather than copying.

This matches the course’s view of AI as **memory-based interpolation**: it retrieves and recombines standard patterns fluently, but it does not know my data, my legal constraints or my experimental results. The human contribution is the part that cannot be outsourced — framing the problem, checking feasibility, running the pilot, interpreting the metrics and taking responsibility for release. My workflow is therefore: **design independently → ask AI for an alternative → verify every claim (arithmetic, documentation, papers) → run a small pilot → revise → document the AI use transparently**. In future work I would use AI to widen the search space, generate ablation tables and write unit tests for preprocessing; I would not use it to estimate GPU budgets or licence footage without recomputing and checking the primary source myself. Used this way, AI shortens the path to a good design, but the judgement about whether the design is feasible, lawful and responsible remains human.

## References

- [1] J. Cheng, *EE6222 Machine Vision — Lecture Notes Week 10: Video (Part I)*, NTU, 2026.
- [2] J. Ho, T. Salimans, A. Gritsenko, W. Chan, M. Norouzi and D. J. Fleet, “Video Diffusion Models,” *NeurIPS*, 2022.
- [3] L. Zhang, A. Rao and M. Agrawala, “Adding Conditional Control to Text-to-Image Diffusion Models,” *ICCV*, 2023.
- [4] A. Blattmann et al., “Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets,” arXiv:2311.15127, 2023.
- [5] K. R. Prajwal, R. Mukhopadhyay, V. P. Namboodiri and C. V. Jawahar, “A Lip Sync Expert Is All You Need for Speech to Lip Generation in the Wild,” *ACM Multimedia*, 2020.
- [6] J. Deng, J. Guo, N. Xue and S. Zafeiriou, “ArcFace: Additive Angular Margin Loss for Deep Face Recognition,” *CVPR*, 2019.
- [7] J. S. Chung and A. Zisserman, “Out of Time: Automated Lip Sync in the Wild,” *ACCV Workshops*, 2016.
- [8] T. Unterthiner et al., “Towards Accurate Generative Models of Video: A New Metric and Challenges,” arXiv:1812.01717, 2018.
- [9] Coalition for Content Provenance and Authenticity, *C2PA Technical Specification*, 2024.
- [10] C-SPAN, “Copyright Policy,” https://www.c-span.org/classroom/copyright/, accessed 9 Nov 2026.
- [11] P. Fernandez, H. Elsahar, I. Z. Yalniz and A. Mourachko, “Video Seal: Open and Efficient Video Watermarking,” arXiv:2412.09492, 2024.
- [12] Y. Yan et al., “DeepfakeBench: A Comprehensive Benchmark of Deepfake Detection,” *NeurIPS Datasets and Benchmarks*, 2023.
- [13] NVIDIA, “NVIDIA H100 Tensor Core GPU Datasheet,” 2023.

## Appendix A — Prompt Given to the AI Tool

> “You are an AI assistant helping a student with a university assignment. Answer independently from your own knowledge. Do NOT use any tools, web search, or file access — just produce a proposal. Assignment prompt given to you: ‘Suppose you are tasked with developing a deep learning system that generates synthetic videos depicting Donald Trump for clearly labelled educational or research demonstrations. Develop a proposal covering: Data (what data, how to collect, preprocess, and organise the training and evaluation datasets); Network architecture (main components, inputs, outputs, how to maintain identity and temporal consistency across frames); Resources (hardware, software, pretrained models, computational budget); Design rationale (choices, assumptions, expected limitations, trade-offs); Evaluation (how to evaluate the generated videos).’ Write a complete, specific, quantitative proposal of 900–1400 words. Use section headings: Data, Network Architecture, Resources, Evaluation, Design Rationale and Limitations. Be concrete about dataset size, model components, training compute, and metrics. Do not ask clarifying questions. Output only the proposal.”
