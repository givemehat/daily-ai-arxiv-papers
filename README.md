# 🤖 Daily AI Research Papers

*Automatically fetched on 2026-11-27*

This repository automatically fetches the latest top research papers in Artificial Intelligence, Machine Learning, and Computer Vision from arXiv every day.

---

## 1. AnyCam: Anything Can Represent Camera for Video Generation
**Authors:** Weijie Lyu, Zhixin Shu, Yuntian Ke, Ming-Hsuan Yang

**Summary:** Camera-controlled video generation re-renders a video along a target camera trajectory, yet moving the camera around an object, the most natural way to change the viewpoint of an object-centric scene, remains difficult. Existing methods condition either on camera parameters, which are scale-ambiguous in monocular video, or on explicit geometry such as warped point clouds or depth, which breaks down under large viewpoint changes. We present AnyCam, a method that represents the camera with an anchor object in the scene: we reconstruct it in 3D and render it along the target trajectory, a camera signal that is scale-aware, view-complete and easy to specify relative to the object. A video diffusion model transfers the content and dynamics of the source video to the new viewpoint. Its H-Concat layout aligns source and target frames in time, so the model can be distilled into AnyCam-AR, a streaming few-step generator for on-the-fly camera control. Both models are trained on paired videos with pixel-aligned anchor renderings from multi-camera videos and static-scene captures. Experiments on diverse datasets and trajectories show that AnyCam performs favorably against camera-controlled video generation and 3D reconstruction methods in camera control and visual quality.

[📄 Read PDF](https://arxiv.org/pdf/2611.34944v1)

---

## 2. Tracking Any Point with Agentic Visual Reasoning
**Authors:** Xuweiyi Chen, Jin Yao, Linzhan Mou, Lei Gong, Di Liu, Cheng Zhang, Ziqiao Ma, Sihan Xu, Adam W. Harley, Shengyi Qian, Zezhou Cheng

**Summary:** A general-purpose Vision-Language Model (VLM) has surpassed expert vision models in many domains such as object detection and video recognition. However, point correspondence is known to be challenging for VLMs since it goes beyond object-level recognition: it requires pixel-level localization of the same physical surface point across observations, even when appearance changes or the point disappears and later reappears. In this paper, we introduce AgenTAP, a VLM-based agent that directly predicts point coordinates and visibility and actively reasons over videos. Starting from its own estimate, the agent autonomously chooses what to inspect and uses the resulting evidence to verify point identity and refine its predictions. With GPT-6 Astra, it surpasses expert vision models in both point localization and visibility prediction, without correspondence-specific fine-tuning. We further use AgenTAP to re-identify physical points after disappearance and reconnect fragmented tracks, constructing EgoTAP-4D, a dataset of 3D point trajectories in long real-world egocentric videos. On sampled reappearing points, its predictions approach human agreement, and adding EgoTAP-4D to D4RT training improves average 3D tracking performance.

[📄 Read PDF](https://arxiv.org/pdf/2611.34943v1)

---

## 3. Spectrum Adaptation of AI-Native Autoencoder Communications with Transfer Learning
**Authors:** Yalin E. Sagduyu, Tugba Erpek

**Summary:** End-to-end physical-layer learning replaces separate modulation, coding, and detection operations with an autoencoder (AE) that consists of a jointly trained encoder-decoder pair at the transmitter and the receiver. This paper studies AI-native communications with AEs and quantifies the sensitivity to training-test mismatch in channel models. Models trained only on an AWGN channel achieve low bit error rates (BERs) under matched conditions but degrade severely on Rayleigh fading with practical front-end impairments. To reduce the time and energy required to adapt to new channel conditions, we propose a low-latency transfer-learning procedure that starts from an AWGN-pretrained system and fine-tunes only a small subset of transmitter and receiver layers while freezing the remainder. We further formulate layer selection as a budget-constrained optimization problem that identifies the most informative parameters to update during adaptation. This preserves the learned signal geometry and the deep decision structure while adapting lightweight front ends to fading- and impairment-induced mixing. For AE communications, we show that partial updates remove the mismatch-induced error floor and approach the BER of fully retrained models. We provide a layer-wise study and quantify resource-performance trade-offs, showing that modest adaptation substantially reduces BER while cutting training time, multiply-accumulate (MAC) operations, energy consumption, and the fraction of updated parameters for resource-efficient implementation.

[📄 Read PDF](https://arxiv.org/pdf/2611.34942v1)

---

## 4. Improving and Expanding Video Editing Capabilities Without Videos
**Authors:** Ji Xie, Yanhao Jia, Xiangpeng Yang, Martin Q. Ma, Sihan Xu, Erik Cambria, Louis-Philippe Morency

**Summary:** Image editing models can follow a wide range of instructions, but video editing models still lag behind, limited in part by the difficulty of collecting paired source and edited videos. Is it possible to transfer advanced image editing capabilities to video editors without new paired videos? We introduce Image-to-Video Transfer (I2VT), which improves pretrained video editors and expands them to new editing tasks using an image editor. It enables efficient post-training with no architectural changes and no new videos, using only individual images. Our key idea is to let the video editor role-play as an image editor: it edits an image as a one-frame video, with the image editor guiding the video editor's predictions at each denoising step. Although the video editor sees only single images during training, at test time it applies the improved and expanded capabilities to whole video clips while preserving temporal consistency. To push the boundaries of video editing, we introduce OpenVE++, an extension of OpenVE-Bench that adds four new editing tasks useful for video production, including action changes, expression changes, body movements, and scene relighting. Our experiments across three different video editors show that I2VT improves existing editing capabilities and expands them to new tasks, and our models achieve state-of-the-art (SOTA) performance on both OpenVE-Bench and OpenVE++.

[📄 Read PDF](https://arxiv.org/pdf/2611.34941v1)

---

## 5. LuxAvatar: Real-Time Relightable Head Avatars via Causal Neural Shading of 3D Intrinsic Proxies
**Authors:** Yipengjing Sun, Chenyang Wang, Boyao Zhou, Jiapeng Zhu, Ka Leong Cheng, Shengping Zhang

**Summary:** We present LuxAvatar, a feed-forward framework for real-time head avatar animation and relighting from a single portrait. To achieve both 3D controllability and complex facial light transport, we factorize avatar synthesis into an animatable 3D intrinsic Gaussian proxy and a causal autoregressive neural shader. This proxy disentangles canonical geometry and reflectance attributes, rapidly rasterizing deformed Gaussians into view- and motion-consistent PBR buffers. Conditioned on these buffers, our neural shader formulates forward rendering as a conditional video diffusion process, bypassing explicit PBR computation to synthesize realistic shading effects under target illumination. We achieve real-time streaming through heterogeneous distillation from a pretrained multi-step bidirectional relighting teacher to a two-step causal autoregressive neural shader, inheriting broad synthetic lighting priors while minimizing conditioning and decoding latency. To further specialize these priors to human heads, we construct a hybrid relighting dataset for domain-specific fine-tuning, capturing authentic facial dynamics and physically grounded light transport. Extensive experiments show that our framework enables 3D-controllable, real-time portrait animation and relighting, outperforming state-of-the-art methods in visual fidelity, motion control, and lighting accuracy.

[📄 Read PDF](https://arxiv.org/pdf/2611.34940v1)

---

## 6. A Mesh for Every Moment
**Authors:** Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman

**Summary:** We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing dynamic Gaussian splatting methods either model appearance alone or target isolated objects segmented by foreground masks, and all of them recover meshes by TSDF fusion or Poisson reconstruction, whose fixed grids limit the detail they can capture. At the core of MEMO is a per-Gaussian motion model inspired by Gaussian processes, which represents each Gaussian's position and rotation over time as a combination of temporal Gaussian kernels. The model keeps every Gaussian a valid surface element throughout the sequence and carries an implicit representation of the dynamic geometry, so a mesh can be derived at any time from a field defined by the Gaussians. Although common in real captures, large and fast motion poses a challenge that dynamic Gaussian splatting methods usually overlook. To account for it, we design a track-based initialization scheme that fits each Gaussian's initial trajectory to point tracks in closed form. We evaluate MEMO on Blender-Moments, a new benchmark of nine animated scenes with ground-truth meshes at every frame, and on two real-world datasets. MEMO reconstructs the most accurate geometry among state-of-the-art methods, and remains competitive in novel-view synthesis and training time. Project page: https://memo-4d.github.io

[📄 Read PDF](https://arxiv.org/pdf/2611.34939v1)

---

## 7. Tokenisation is not in APX
**Authors:** Violeta Kastreva, Philip Whittington, Dennis Komm, Tiago Pimentel

**Summary:** In this paper, we prove that, unless P=NP, no polynomial-time algorithm can find a tokeniser whose objective is within any constant factor of the optimum, meaning that tokenisation is not in the APX complexity class. We prove this for direct and bottom-up tokenisation, under both a compression or unigram log-likelihood objectives, and for binary or larger alphabets. We further show that, even over unary alphabets, direct tokenisation is APX-hard, and thus admits no polynomial-time approximation scheme.

[📄 Read PDF](https://arxiv.org/pdf/2611.34938v1)

---

## 8. Can image generation help visual reasoning? An empirical study
**Authors:** Xueyang Yu, Yifan Jing, Taiming Lu, Linrong Cai, Zhipeng Cai, Yunyang Xiong, Gabriel Sarch, Zhuang Liu

**Summary:** Language models think in words; then multimodal models might think in images. We test whether a generated helper improves the answer to a visual question. A model describes the helper it needs and then answers using the original and generated images together. Across 13 vision-language model and generator pairs, generation lowers mean accuracy by 3.7 percentage points, with declines on nine of ten tasks. Two unified models, BAGEL and Janus-Pro-7B, each lose accuracy on eight tasks. On VSTAR, adding a generated image to the same planning hint lowers accuracy by 10.47 points. Repeated image edits yield different outcomes across tasks. ChartQAPro and MathVista stay below their no-generation baselines, while ERQA gains three points after ten edits.

[📄 Read PDF](https://arxiv.org/pdf/2611.34935v1)

---

## 9. Attack Policy Selection can Mislead Monitor Evaluators
**Authors:** Charlie Griffin, Oliver Makins, Asa Cooper Stickland, Alessandro Abate, Yarin Gal, Abby D'Cruz, Xander Davies

**Summary:** AI monitors, classifiers that flag dangerous behaviour by AI agents, are often evaluated against transcripts generated by attack policies acting as proxies for dangerous behaviour in deployment. We evaluate an ex-production OpenAI monitor as a case study and find that measured false negative rate is highly sensitive to both the method used to generate attack policies and the level of optimisation applied within that method. This rate ranged from 0.5\% to 20.8\% across optimisation levels of a single method (reinforcement learning), and from 6.4\% to 23.0\% across methods at their best observed optimisation level (optimised prompting vs.\ transcript editing). Every attack policy was developed against proxy monitors only: all reported results show attacks transferring to the held-out GPT-5.4 target monitor. Our results suggest that monitor evasion evaluations can easily mislead: an evaluation using only basic attack methods may give false confidence that a monitor is strong.
  The sensitivity to attack-policy choice raises a problem: interpreting any particular result as evidence about deployment performance requires justification. The transcripts produced by attack policies are proxies for the dangerous behaviour a monitor must flag in deployment. These proxies can introduce visible artefacts, such as reasoning about a ``side task'' absent from the instructions shown to the monitor, that affect monitor judgements. Given the sensitivity above, the choice of proxy can change an evaluation's conclusion. Reading these results as evidence about deployment therefore requires a separate legitimacy argument for why the proxies are informative, including any justification of conservativeness. Making convincing arguments remains an open problem.

[📄 Read PDF](https://arxiv.org/pdf/2611.34934v1)

---

## 10. DynMF2: Rigid Motion Factorization by Expectation-Maximization for Monocular 4D Reconstruction and Motion Segmentation
**Authors:** Agelos Kratimenos, Yile Hua, Kostas Daniilidis

**Summary:** A single casual video leaves a moving scene under-determined: a point seen once from each place can slide toward or away from the camera and still match every frame. We constrain the reconstruction with the structure of the motion itself. Building on DynMF, we model a scene's motion as a handful of SE(3) trajectories, each rigid, and let every point follow one of them alone, never a blend. DynMF2 computes this factorization directly from 3D point trajectories, with no rendering, by Expectation-Maximization (EM). Its M-step fits, in closed form, every rigid motion to the points assigned to it, and its E-step reassigns every point to the motion that explains it with the least error. The background is simply one more motion, the camera's, so no masks are needed. Three tools then revise the factorization: requery adds trajectories where the rendering shows parts the tracker missed, merge joins motions that move together, and split separates those that do not. Thus the number of motions follows the scene. Without masks, DynMF2 clearly outperforms the mask-based baselines in view synthesis on iPhone and NVIDIA and in 3D tracking on iPhone. It recovers what masks leave out, from thin parts and details to small movers far in the background. Its motions segment the moving parts of MOVi-F and iTACO scenes competitively, although DynMF2 is never trained to segment. What moves in a scene is not decided in advance: it emerges from the rigid motions themselves.

[📄 Read PDF](https://arxiv.org/pdf/2611.34931v1)

---

