# Raw AI Proposal — Part 2 Record

- Date: 9 November 2026
- Tool: Claude Code (Anthropic), fresh session
- Prompt: see Appendix A of `Report.md`
- Note: This is the AI's output, preserved for transparency. It has not been edited. The student's verification of its claims is in §2.4 of the report.

---

# Proposal: Identity-Consistent Synthetic Video Generation for Labelled Research Demonstrations

## Data

We require three corpora. (1) Target-identity footage: approximately 35 hours of publicly available, rights-cleared video of the subject from 2011–2024 — about 18 h of public-domain C-SPAN and White House pool feeds, 10 h of Creative-Commons news clips, and 7 h of licensed archival interviews. (2) A generic face/speech corpus for pretraining: VoxCeleb2 (~1M clips, 6,112 identities), LRS3 (400 h), and HDTF (410 videos). (3) Driving audio: 6 hours recorded by a consenting voice actor under a written release, rather than a cloned copy of the subject's voice.

After filtering we expect ~22 h usable, segmented into ~128,000 clips of 4–12 s at ≥1080p, 25–30 fps. Preprocessing: PySceneDetect shot segmentation (threshold 27, discard shots <2 s); RetinaFace detection with ByteTrack tracking, retaining tracks with ≥90% frame coverage and face height ≥180 px; ArcFace verification (cosine ≥0.45 to a reference centroid) to reject crowd shots and impersonators; FLAME 3DMM fitting and head-pose estimation, keeping |yaw| ≤45°; quality filtering (Laplacian variance >100, CLIP aesthetic ≥4.5, exposure and motion-blur checks); face crops aligned to 512×512 with 2.5× expansion; RVM matting for hair/background compositing; Whisper-large-v3 transcripts and BLIP-2 captions; deduplication at CLIP cosine >0.95.

Splitting is by event date, not by frame, to prevent leakage from near-duplicate footage of the same speech: train 2011–2019 (17 h, ~98k clips), validation 2020–2021 (2.5 h, ~15k), test 2022–2024 (2.5 h, ~15k clips from 30 held-out events). Data are stored as WebDataset shards: 5 TB raw, 1.2 TB decoded crops, 400 GB precomputed latents.

## Network Architecture

A two-stage latent video diffusion system.

Stage 1 is a 3D causal VAE (8× spatial, 4× temporal compression, 16 channels) feeding a Diffusion Transformer with 1.4B parameters (28 blocks, hidden 1536, 24 heads, 2×2 latent patches, 3D RoPE). A 512×512, 121-frame clip becomes 64×64×31 latents, tokenised to 31,744 tokens. Four conditioning paths enter through cross-attention and adaptive normalisation: text (T5-XXL); audio (Whisper-large encoder at 50 Hz, resampled and injected per frame for lip sync); identity (a 512-d ArcFace embedding plus four reference frames through decoupled IP-Adapter cross-attention, rank 128); and expression/pose (FLAME coefficients predicted from audio by a 6-layer transformer).

Stage 2 upsamples to 1024×1024 with a 180M-parameter 3D U-Net super-resolution model conditioned on the low-resolution latent and identity embedding.

Outputs are 5–10 s clips at 25 fps with synchronised audio, an invisible VideoSeal watermark, and signed C2PA provenance metadata.

Temporal and identity consistency rest on five mechanisms: full 3D self-attention over the clip; re-injection of reference and first frames at every autoregressive chunk (8-frame overlap); shared fixed noise and cosine-masked latent blending across chunk boundaries; an identity loss (1 − cos(ArcFace)) plus LPIPS on face crops; and a RAFT optical-flow warp loss. Total loss is diffusion MSE + 0.2·LPIPS + 0.1·identity + 0.1·warp + 0.05·SyncNet, with classifier-free guidance of 4.5 (text) and 3.0 (identity).

## Resources

Training uses 48× NVIDIA H100 80GB SXM nodes for six weeks, about 48,000 GPU-hours: 2k VAE fine-tuning, 22k Stage-1 base training (1.4B × 31.7k tokens × 6 ≈ 2.7×10^14 FLOPs per sample; batch 512, 300k steps ≈ 4.1×10^22 FLOPs, ~33k GPU-hours at 35% MFU), 6k identity-adapter training, 8k super-resolution, and 10k ablations. Storage is 11 TB plus 2 TB checkpoints. Cloud cost is roughly US$110,000 at $2.30/GPU-hour; an owned cluster amortises to about $45,000.

Software: PyTorch 2.4, FSDP, FlashAttention-3, Diffusers, xFormers, WebDataset, FFmpeg, Hydra, Weights & Biases. Pretrained components: Open-Sora/SVD VAE, T5-XXL, Whisper-large-v3, wav2vec2, InsightFace ArcFace, FLAME, RAFT, VideoSeal, C2PA SDK. Team: four researchers over 16 weeks (data 5, modelling 8, evaluation 3).

## Evaluation

Automatic metrics on the 30-event test set: FVD (I3D) <400; frame FID <12; ArcFace identity cosine ≥0.65 against the reference; SyncNet LSE-C ≥6.0 and LSE-D ≤8.0; LPIPS ≤0.12; RAFT warp error ≤0.02; CLIP text alignment ≥0.28; aesthetic score ≥5.0. Each is reported with 95% bootstrap confidence intervals over three training seeds.

Human evaluation: 40 participants rate 200 clips (100 generated, 100 real) on 5-point Likert scales for identity fidelity, photorealism, temporal coherence, and lip-sync, with inter-rater Krippendorff's α reported. A two-alternative forced-choice real/fake task should yield ~75% detection accuracy — realistic enough for research, yet still distinguishable. A separate check verifies that participants notice and correctly interpret the "synthetic" label and watermark.

Safety evaluation: watermark bit accuracy >95% after H.264 compression and 0.9× rescaling; 100% C2PA validation; and DeepfakeBench detectors should retain AUC >0.90 on our outputs, since detectability is a design goal, not a failure. Ablations remove identity conditioning, 3D attention, audio conditioning, and the warp loss to quantify each component's contribution.

## Design Rationale and Limitations

Diffusion was chosen over GANs for training stability, mode coverage, and controllability via classifier-free guidance; a DiT over a U-Net for cleaner scaling; and a two-stage pipeline because full 1024p video diffusion would roughly quadruple compute. Event-level splitting is essential: frame-level splits leak the same outfit, lighting, and speech across sets and inflate every metric. Identity is conditioned separately from motion so appearance and behaviour can be varied independently. The voice actor deliberately avoids biometric voice cloning and makes outputs easier to distinguish from genuine recordings.

Assumptions: one identity, mostly frontal upper-body framing, English speech, podium or studio lighting, and clips under 10 s.

Limitations: identity drift and texture flicker beyond ~15 s; artefacts on hands, teeth, occluded faces, and fast head turns; bias toward the subject's dominant appearance (suits, podium backgrounds, particular decades), so off-distribution prompts degrade; audio-driven mouth shapes may not match a different voice's prosody; human evaluation is small-sample and culturally variable. Compute estimates carry ±30% uncertainty.

Legal and ethical constraints are integral to the design. The subject's consent is unobtainable, so outputs remain internal, access-logged, watermarked, and C2PA-signed; a visible "SYNTHETIC" overlay is burned in for demonstrations; an output filter blocks generated statements about real political topics, endorsements, or elections; and any release requires ethics-review approval and compliance with publicity-rights and AI-transparency law (e.g., the EU AI Act's disclosure duties). The system is not intended, and will not be licensed, for redistribution.
