# 🤖 Daily AI Research Papers

*Automatically fetched on 2026-11-25*

This repository automatically fetches the latest top research papers in Artificial Intelligence, Machine Learning, and Computer Vision from arXiv every day.

---

## 1. OmniAct: One Policy, One Million Embodiments
**Authors:** Xiang Fan, Yuheng Wang, Jiayuan Yan, Bohan Fang, Wisdom Oluchi Ikezogwo, Ainaz Eftekhar, Max Argus, Jason Ren, Jiafei Duan, Ranjay Krishna

**Summary:** A single policy that controls diverse robots must not only transfer task knowledge across embodiments, but also adapt its behavior to each robot's capabilities. Existing approaches facilitate transfer through shared action representations, but these representations do not necessarily capture how differences in robot morphology should shape manipulation strategies. We introduce OmniAct, a cross-embodiment manipulation policy that conditions directly on each robot's kinematics in a specific scene to produce embodiment-specific behavior. This kinematic graph represents the robot's joint positions, motion axes, and connectivity to its visual observation, allowing the policy to account for how its embodiment related to objects and surfaces in the scene. A flow-matching policy predicts relative joint motions for each node, enabling control across robots with different degrees of freedom and kinematic configurations. To learn how physical structure shapes behavior at scale, we procedurally design and filter one million physically feasible robot embodiments; next, we develop algorithms to generate robot trajectories in simulation for all embodiments; finally, we train across diverse simulated manipulation tasks. On 2,000 embodiment-scene-held-out evaluation episodes, OmniAct achieves 63.0% success, compared to 17.8% for pi 0.5 and 57.9% for the strongest baseline; on the task families GPT-6 Astra was evaluated on, it achieves 64.7% against GPT-6 Astra's 41.1%. On a previously unseen real-world robot, it achieves nearly twice the success rate of the next best method, MolmoAct2. Beyond task success, we observe that OmniAct learns distinct manipulation strategies that exploit the capabilities and accommodate the limitations of different morphologies. Project: https://omniact.github.io/

[📄 Read PDF](https://arxiv.org/pdf/2611.33158v1)

---

## 2. PointX: Multi-View Consistent Intrinsics by Querying Surface Points
**Authors:** Miguel Farinha, Sam Sartor, Iliyan Georgiev, Giuseppe Vecchio, Ronald Clark, Michael Fischer

**Summary:** The appearance of a scene is determined by the albedo, roughness, metallicity and normal of every point on its surface, and by the light that reaches it, its irradiance. Recovering these intrinsics from images is ambiguous, and methods that predict them per pixel give the same surface point a different decomposition in every view. We introduce PointX, a simple feed-forward model that predicts intrinsics per 3D surface point instead. A multi-view transformer encodes a set of unposed images, and for any queried surface point, PointX pools the point's tokens across the views in which it appears and decodes the point's intrinsics once. Each point of a 3D reconstruction of the scene, such as a point cloud or a mesh, thus receives a single prediction, which is exactly consistent across views by construction and enables view-consistent relighting and editing. The same model also predicts per-view maps, from one image or many, by querying the point seen at every pixel. These maps agree across views up to the precision of the estimated geometry and correspondences. PointX is significantly more consistent than existing methods, while remaining competitive in accuracy from a single image and improving as views are added. Project page: https://pointx-paper.github.io/

[📄 Read PDF](https://arxiv.org/pdf/2611.33157v1)

---

## 3. DiaCap: Jointly Learning Who Speaks When for Audiovisual Dialogue Captioning
**Authors:** Binfei Ji, Zhiwen Cao, Anqi Yang, Prem Seetharaman, Shuo Yang, Ratheesh Kalarot, Yingyan Celine Lin, Mingze Xu

**Summary:** We present DiaCap, an audiovisual LLM for comprehensive dialogue captioning, which produces the transcript, timestamps, and a visual description of the speaker for every utterance in a video. Considering that utterance timing and audiovisual diarization are tightly coupled, DiaCap unifies the tasks in a single model, trained in two complementary stages. First, we train DiaCap on 225K curated clips, using synthetic captions that densely label every utterance in detail. Second, we further refine the model via reinforcement learning on 2.9K human-corrected clips, using fine-grained feedback that directly evaluates utterance timing, speaker grouping, and speaker binding. On DiaDemBench, which we extend with utterance-level timestamps and subtitle redaction, both DiaCap with off-the-shelf transcripts and its end-to-end variant DiaCap-E2E achieve strong results. Specifically, DiaCap performs on par with Gemini 4 Argon in audiovisual diarization while clearly outperforming it in timestamp accuracy (76.59 vs. 42.76 TIME). It also maintains strong diarization on multilingual and minute-long videos, and transfers to audiovisual question answering.

[📄 Read PDF](https://arxiv.org/pdf/2611.33153v1)

---

## 4. BioLoom: Scaling Biomedical Vision-Language Models by Learning from the Structure of Scientific Articles
**Authors:** Yuwei Yang, Xiaoxiao Sun, Alejandro Lozano, Yuan-Sen Ting, Yuhui Yuan, Liang Zheng, Serena Yeung-Levy

**Summary:** The development of biomedical vision-language models (VLMs) with contrastive image-text pretraining has been driven by scaling to increasingly large and diverse image-text datasets. Beyond scaling, further progress can come from learning richer representations from existing data. We hypothesize that the structure of scientific literature itself provides an additional source of supervision: figures, panels, captions, and accompanying article text encode rich relationships across modalities. Yet, treating these as independent image-text pairs overlooks their relationships. To address this limitation, we incorporate these structural relationships into contrastive image-text supervision. We preserve exact image-text matches while introducing weaker positive supervision for related pairs, such as a panel and the caption of a sibling panel. We upweight cross-article negatives of the same content type to encourage finer discrimination. We also enrich panel descriptions using visual content, original figure captions, and mentioning paragraphs. Pairing panels with these descriptions and whole figures with their original captions yields Loom52M, a dataset of 52.4 million image-text pairs spanning scientific charts and biomedical images. Using Loom52M, BioLoom (DFN-2B) achieves 56.82% domain-balanced mean accuracy across 67 zero-shot classification tasks from 43 datasets in 10 domains, compared with 48.77% for MedPMC-CLIP. On BioLoomBench with concise captions and BioMedFlickr, it achieves bidirectional mean Recall@1 of 63.20% and 10.59%, versus 46.37% and 7.55% for the respective strongest evaluated baselines, BiomedCLIP and MedPMC-CLIP. Code, datasets, benchmarks, and models are available at https://bioloom-clip.github.io/.

[📄 Read PDF](https://arxiv.org/pdf/2611.33151v1)

---

## 5. One Take, Many Cameras: Audio-Grounded Shot Synthesis for Dialogue Re-Cinematography
**Authors:** Anthony Chen, Naomi Ken Korem, Matan Ben-Yosef, Tavi Halperin, Urska Jelercic, Ofir Bibi, Daniel Cohen-Or, Or Patashnik, Maneesh Agrawala

**Summary:** Creating a dialogue scene typically requires cutting between multiple views (e.g., close-ups, medium shots, and over-the-shoulder shots) of the actors. Yet capturing such coverage is costly and in many settings unavailable. We study dialogue re-cinematography: synthesizing additional shots from a single wide-angle dialogue video. Existing video generators can synthesize new shots, but rely on visual cues alone, so when the source video barely shows the lips, the generated lip motion fails to match the speech. Our key observation is that the speech audio is view-invariant: it constrains lip motion in any target view. Building on this insight, we adapt a pretrained audio-visual diffusion model to generate the new shot from a target frame that specifies the view, a source video that contains the performance, and the speech audio that drives lip motion. In multi-person scenes, however, pretrained audio-visual models drive every visible face with the same speech, causing speech leakage, where silent listeners mouth the speaker's words. We therefore introduce speaker-aware audio gating, a training-free module that lets the audio drive only the faces that speak in the target shot. On a cinematic paired-view benchmark spanning diverse viewpoints and framings, our method lowers perceptual error by 59%, landmark error by 56%, and speech leakage by 97% relative to the strongest baseline, Wan 3.0. Our method also remains robust on in-the-wild scenes, highlighting its potential for film post-production.

[📄 Read PDF](https://arxiv.org/pdf/2611.33147v1)

---

## 6. Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild
**Authors:** Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng

**Summary:** Embodied Spatial Reasoning (ESR) is central to deploying Vision-Language Models (VLMs) in real-world embodied tasks, yet remains inadequately evaluated. Existing benchmarks primarily assess spatial reasoning in static images or synthetic indoor environments, where semantic shortcuts often suffice, making it difficult to faithfully evaluate spatial reasoning capabilities in the wild. In light of this, we present Lost on Campus, a benchmark for evaluating ESR in large-scale real-world outdoor 3D environments reconstructed by 3D Gaussian Splatting. Our benchmark introduces a unified reasoning-action evaluation framework that seamlessly integrates diagnostic QA for isolated reasoning with closed-loop interactive navigation for active reasoning under multimodal instructions. To enable fine-grained diagnosis, we evaluate six capability aspects of ESR: action grounding, spatial foresight, metric awareness, goal-directed planning, ego-allocentric localization, and spatio-temporal consistency. Extensive experiments reveal that: (i) Compared to indoor settings, real-world outdoor environments impose substantially higher demands on spatial reasoning, where existing models exhibit poor performance; (ii) VLMs still struggle with fine-grained visual alignment, with failures in spatial foresight and ego-allocentric localization emerging as primary bottlenecks; (iii) Improving multimodal interaction capabilities and long-term spatial reasoning is crucial for advancing embodied intelligence. These findings highlight that faithful evaluation of ESR demands benchmarks tightly coupling perception, reasoning and action within realistic and continuous environments.

[📄 Read PDF](https://arxiv.org/pdf/2611.33145v1)

---

## 7. ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification
**Authors:** Xingjian Ran, Xiaoye Mo, Sihao Liu, Li Luo, Taiqiang Wu, Ji Zhao, Wenqi Shao, Hongyang Li, Jiaqi Wang, Bo Dai

**Summary:** Embodied spatial intelligence requires agents to gather information through exploration and interaction, then use it to reason and act. Existing benchmarks insufficiently distinguish correct outcomes from completion of these task requirements. We introduce ROAM-Bench to evaluate these abilities under robot motion and collision constraints. Independent checks use simulation state and episode records to assess outcomes and task requirements, with stronger checks of geometry, coverage, or placement. It comprises 250 manually validated tasks across 11 types in five groups and 27 indoor environments, covering object and room search, counting, geometric judgments, direction reasoning, and relocation. Human evaluators achieve 84% strict task success on 100 sampled tasks, with every correct outcome satisfying the required checks. Across seven frontier vision-language models, we identify two complementary failure modes: correct outcomes with unmet task requirements, and incorrect outcomes despite passing stronger checks. Oracle-input diagnostics show that more complete target observations and calibrated feedback improve final spatial judgments.

[📄 Read PDF](https://arxiv.org/pdf/2611.33143v1)

---

## 8. iWAM: Efficient Action Prediction from World Models without Explicit Future Prediction
**Authors:** Vansh Kapoor, Max Sobol Mark, Sreyas Venkataraman, Max Simchowitz, Aviral Kumar

**Summary:** World-action models (WAMs) build policies on pretrained video-generation models, on the premise that predicting how a scene evolves helps determine how to act. However, generating future scenes is expensive for real-time control. This motivates efficient proxies for future imagination, but how to train such proxies without sacrificing action-prediction quality remains unclear. An effective proxy need not generate a high-resolution frame; it only needs to provide enough information to distinguish between possible futures. This leads to the design principle behind iWAM: rather than denoising an entire future frame, can we condition the action policy on intermediate features from a single video-model evaluation? We show that the answer is yes. Exploiting the reversible dynamics of flow-matching models, we invert each training future into the corresponding latent noise vector. However, a single velocity evaluation at this latent does not necessarily yield informative features for action prediction. We therefore learn a bidirectional flow map that amortizes future-generation computation, enabling a single model evaluation to provide effective conditioning features. At inference, we sample a latent noise vector from the prior and condition the policy using just one video-backbone forward pass. Across simulated benchmarks and real robots, iWAM recovers the generalization benefits of WAMs while substantially reducing its inference cost.

[📄 Read PDF](https://arxiv.org/pdf/2611.33141v1)

---

## 9. Physicl Scenes: An Artist-created 3D Dataset for Learning Perception and Action
**Authors:** Yueh-Cheng Liu, Snehal Jauhri, Matthias Nießner, Angela Dai

**Summary:** We present Physicl Scenes, a high-quality artist-created and curated dataset of 6,499 3D scenes spanning household rooms, public interiors, and outdoor spaces. The dataset combines detailed geometry, physically based materials, and carefully composed environments with object- and part-level semantic annotations, providing rich, joint supervision for visual and embodied learning. We demonstrate its value as training data across inverse rendering, 3D reconstruction, scene understanding, and mobile manipulation. Across these tasks, training state-of-the-art methods with our scenes improves performance over alternative synthetic datasets. In addition, we introduce a mobile manipulation benchmark, evaluating vision-language-action models performing physical pick and place in diverse 3D scenes with realistic layouts, and using our part annotations to also score where each object is grasped. Our dataset will be released publicly to facilitate research in visual and embodied AI.

[📄 Read PDF](https://arxiv.org/pdf/2611.33137v1)

---

## 10. BriConstrain: Geometrically Constrained Decoding for Autoregressive Brick Assembly Generation
**Authors:** Nadav Magar, Amir Hertz, Ariel Shamir, Or Patashnik

**Summary:** Language models can generate LEGO$^\circledR$ assemblies from text, but their builds often contain parts that collide or attach to nothing. The usual approach of rejecting and resampling invalid placements discards decoded tokens without guaranteeing a valid build. We present BriConstrain, a constrained decoding method that restricts a pretrained language model's next-token probabilities before sampling, steering it towards valid placements. Because the validity of a brick placement depends on the non-predetermined build state, it cannot be compiled into a fixed grammar and must be checked dynamically. However, checking the validity of a brick before sampling is challenging as the space of valid placements is combinatorially large and cannot be enumerated exhaustively. Our key idea is to narrow the search space by constraining how parts attach rather than which parts attach to each other. Concretely, given the model's predictions of the currently placed part, and the previously placed parent it wants to connect to, we constrain the model's choice of how they attach. This allows us to span the space of part attachments, using a precomputed geometric oracle, and to effectively filter out colliding options. With valid attachment candidates in hand, we bias the model's next-token distribution towards the remaining valid candidates. We evaluate our method on two LEGO$^\circledR$ formats and models: BrickNet, which annotates connectivity explicitly, and our proposed Implicit Connectivity LDraw Format (ICLF), which uses numeric values for placements and leaves connectivity implicit. Our method raises collision-free builds from 31% to 91% on BrickNet and from 15% to 65% on ICLF, and outperforms rejection sampling on both formats at about 60% of its decoding cost.

[📄 Read PDF](https://arxiv.org/pdf/2611.33135v1)

---

