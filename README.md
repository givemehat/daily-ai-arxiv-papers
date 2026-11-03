# 🤖 Daily AI Research Papers

*Automatically fetched on 2026-11-03*

This repository automatically fetches the latest top research papers in Artificial Intelligence, Machine Learning, and Computer Vision from arXiv every day.

---

## 1. Whitened Advantage Summation Policy Optimization: Correlation-Aware Aggregation for Multi-Reward Reinforcement Learning
**Authors:** Olaitan Olaleye, Jayson Meribe, Temidayo Olaleye

**Summary:** Reinforcement learning for language models often combines several rewards by normalizing each one and adding them with fixed weights. When the rewards are correlated, the variation they share is counted once for every reward that carries it. In terms of the ZCA-decorrelated components of the reward signal, the weighted sum applies weights $Σ^{1/2} w$ rather than the chosen weights $w$, where $Σ$ is the reward correlation matrix. We study WAS-PO, which whitens the normalized advantages with $Σ^{-1/2}$ before adding them, so that the chosen weights apply to those components. We derive the scalarized objective whose gradient it follows when normalization statistics are held fixed, show that its weights on the raw rewards can be negative, give an exact two-reward condition under which the lighter-weighted reward is reversed, and give a loose bound on the error from estimating $Σ$ during training. On tool calling with Qwen2.5-1.5B-Instruct, WAS-PO reached a higher mean training reward than GDPO in all seven seeds with three rewards (3.8% higher) and all three seeds with four (3.9% higher). WAS-PO also replaces GDPO's per-prompt normalization with batch-level normalization, and we did not separate the two changes with three or four rewards. The training-reward gains did not carry over to held-out accuracy, which was slightly lower than GDPO's with three rewards (not significant) and 0.03 lower in absolute terms with four (two seeds evaluated). With two rewards, WAS-PO trailed GDPO in training reward, and a three-seed control weakly suggests that the gap comes from batch-level normalization rather than whitening. In a math setting where the two rewards were nearly identical by construction, WAS-PO drove down the lighter-weighted reward, as the sign condition predicts.

[📄 Read PDF](https://arxiv.org/pdf/2611.02609v1)

---

## 2. StateFence: Task-State Protection Against Evidence-Chain Contamination in Blue-Team LLM Agents
**Authors:** Haowen Dai, Alejandro Guerra-Manzanares

**Summary:** Indirect prompt injection creates a distinctive risk for blue-team Large Language Model (LLM) agents in Security Operations Centers (SOCs). Malicious instructions can be embedded in telemetry, tickets, retrieval results, or memory and then propagate through alert triage, incident summarization, response recommendation, and Indicator of Compromise (IOC) extraction as locally plausible intermediate decisions. We characterize this failure mode as evidence-chain contamination of protected task state. The main challenge is task dependent: a suspicious string may be malicious control text for summarization but essential evidence for IOC extraction. To address this challenge, we propose StateFence, a task-aware evaluation and defense framework that treats severity labels, incident narratives, response policies, and IOC sets as protected states. StateFence maps indirect prompt-injection attacks into explicit, stealth, multi-hop, and persistent SOC evidence attacks, records observable propagation traces, and routes defenses according to the attacked state. Across controlled SOC cases and public-SOC validation cases, StateFence lowers attack success and reduces failures that appear only after evidence is poisoned, while preserving task utility and avoiding the indicator loss caused by task-mismatched filtering. Our findings indicate that robust blue-team LLM agents require mechanisms that preserve task-critical state under untrusted evidence.

[📄 Read PDF](https://arxiv.org/pdf/2611.02605v1)

---

## 3. BGD-SF PolySegNet: boundary-guided dynamic selective fusion network for robust polyp segmentation in colonoscopy images
**Authors:** Nishi Kanta Paul, Shamia Maherin, Morsheda Akter, Moinul Hossain, Md Kishor Morol

**Summary:** Effective polyp segmentation in colonoscopy images is crucial for early detection of colorectal cancer, a leading cause of cancer-related death worldwide. While current deep learning models perform well on traditional Dice benchmarks, border segmentation remains difficult. Most methods use boundary information only as an additional loss signal during training, which prevents the network from explicitly learning border-guided feature selection or mask refinement. This paper introduces BGD-SF PolySegNet, a boundary-guided encoder-decoder architecture that controls three phases of the segmentation pipeline: dynamic multi-scale context aggregation, selective skip-feature fusion, and final mask refinement. The architecture comprises a pretrained EfficientNet-B4 backbone and three proposed modules: Boundary-Guided Dynamic Cascaded Multi-Scale Context Aggregation (BGD-CMSCA), Boundary-Guided Selective Attention Fusion (BG-SAGF), and a Multi-Level Boundary Guidance Head (MBGH). The model is trained on 3,535 annotated images from Kvasir-SEG, BKAI-IGH NeoPolyp-Small, and PolypGen, and evaluated on four held-out benchmark datasets. On the internal test set, BGD-SF achieves a Dice of 0.887, IoU of 0.839, mask-derived Boundary F1 of 0.531, HD95 of 30.32, and ASSD of 18.10, improving Boundary F1, HD95, and ASSD by 15.7%, 27.5%, and 34.6% over the strongest CNN baselines. External validation on CVC-ClinicDB, CVC-ColonDB, ETIS-Larib, and CVC-300 yielded Dice scores of 0.891, 0.776, 0.863, and 0.885, respectively. The model runs at 35 FPS with 22.51M parameters. Wilcoxon signed-rank tests confirm statistically significant mask-derived Boundary F1 improvements over six of seven ablation variants (p < 0.001; small-to-moderate effect sizes, r = 0.215-0.434), demonstrating that integrating boundary guidance as an active architectural component measurably advances polyp boundary delineation.

[📄 Read PDF](https://arxiv.org/pdf/2611.02603v1)

---

## 4. Parallelism-Aligned Pruning and Round-Aware Context Reuse for On-Device Multimodal Agents
**Authors:** Peipei Jiao, Mingkang Liu, Weiming Meng, Lichen Pang, Tianyuan Liu, Junyan Li

**Summary:** On-device multimodal agents are limited by two deployment mismatches: pretrained attention structures may not divide evenly across the compute cores of an edge accelerator, causing irregular partitions; and standard prefix caching keeps historical visual tokens in the persistent KV cache, whose capacity grows with the number of rounds. We present PARC, which combines parallelism-aligned structured pruning with lifetime-aware KV-cache reorganization. At the model level, it uses first-order Taylor importance and grouped-query-attention-aware selection to make attention dimensions divisible by the target core count while preserving the query-to-key/value ratio and head dimension. At runtime, it separates the system prompt, persistent text history, and transient visual observations by lifetime, updating text history during tool execution so that historical images leave the persistent cache and more interaction rounds fit a fixed budget. On 2,062 GUI actions, the incremental interface shows no accuracy regression, and task-aware recovery training restores 98.7% of the action-type accuracy gap and the coordinate hit rate to the original level. Under seven-core deployment, hardware-aligned pruning reduces vision-encoder latency by 11.4%, improves decoding throughput by 23.8%, and lowers per-heap high-water memory by 12.7%; a parameter-matched control confirms that the speedup stems mainly from core alignment rather than parameter reduction.

[📄 Read PDF](https://arxiv.org/pdf/2611.02601v1)

---

## 5. Camera-Free Object Discovery and Interaction with GazeTags
**Authors:** Vimal Mollyn, Chris Harrison

**Summary:** We present GazeTags, a camera- and computer-vision-free approach for worn head-gaze object awareness. Our small electronic tags cost roughly \$2 each and can operate for more than a year on a coin cell battery. They work in concert with a user-worn device (smartglasses, hearables, etc.) that periodically emits a focused infrared signal aligned with the user's head direction. Only GazeTags within that narrow head-oriented beam wake and respond, providing their identity and optional payloads such as object state or live sensor readings. By avoiding cameras and computer vision pipelines, our approach is very energy efficient, able to operate continuously even in battery-constrained wearables, and sidesteps non-trivial privacy issues. We describe our hardware design, characterize our system performance and operating tradeoffs, and demonstrate how GazeTags can enable practical gaze-aware environments.

[📄 Read PDF](https://arxiv.org/pdf/2611.02599v1)

---

## 6. AVID: A 5T fMRI Dataset for Benchmarking Auditory-induced Visual Mental Imagery Decoding
**Authors:** Shiqi Shen, Shurui Li, Xilin Zhang, Yuanning Li

**Summary:** Visual mental imagery (VMI) decoding uses brain activity to reconstruct internally generated visual scenes, providing a potential pathway for externalizing internal experiences and developing neuroprosthetic communication interfaces. However, progress is limited by the lack of dedicated, training-scale VMI datasets. Current VMI paradigms often rely on visual prompts or short-term memory images, introducing visual and mnemonic confounds that make it difficult to disentangle neural activity associated with endogenous image construction from signals driven by prior or concurrent visual input. Furthermore, existing VMI datasets offer limited descriptive control over individual visual attributes, making it difficult to systematically assess fine grained visual details. To address these gaps, we introduce AVID, the first dedicated training-scale 5.0 Tesla functional magnetic resonance imaging (fMRI) resource for auditory-induced VMI decoding. AVID comprises approximately 67 hours of dense recordings from nine participants. The dataset is structured into two complementary splits: a scene-level complex split using naturalistic Mandarin descriptions and a controlled simple split with explicitly specified visual attributes. We further formalize a standardized evaluation protocol that decouples source-image consistency from semantic alignment, allowing for a more nuanced assessment of imagery reconstruction. Baseline qualitative and quantitative results show that current reconstruction pipelines remain limited on AVID, although the most successful reconstructions preserve recognizable scene level semantics from spoken descriptions. By combining dedicated training-scale neural recordings and standardized evaluation resources, AVID provides both a data foundation for imagery-specific model development and a benchmark for evaluating VMI decoding with substantially reduced sensory contamination.

[📄 Read PDF](https://arxiv.org/pdf/2611.02593v1)

---

## 7. They Know Where It Is, But Not What It Says: A Bilingual Hallucination Benchmark of Hadith Recall in Open LLMs
**Authors:** Dayam Nadeem, Safdar Mustafa, Ameen Ur Rehman, Shahab Saquib Sohail, Mohammad Nadeem, Usman Naseem

**Summary:** Large language models are increasingly consulted for religious knowledge, including the recall of specific Hadith (recorded sayings and actions of the Prophet Muhammad, peace be upon him). Unlike open-ended generation, Hadith recall is a high-stakes, verifiable task: a reference (collection, chapter, and Hadith number) has exactly one correct text, and any deviation from it constitutes a fabrication that can be mistaken for authentic scripture. This study introduces a bilingual (English/Arabic) benchmark that probes five open-weight, locally-deployable language models (Mistral-7B, Gemma3-4B, Jais-7B, ALLaM-7B, and Phi4-mini-3.8B) across all six canonical Sunni Hadith collections (Sahih al-Bukhari, Sahih Muslim, Sunan Abi Da'ud, Jami' al-Tirmidhi, Sunan an-Nasa'i, Sunan Ibn Majah), sampling 500 Hadith per collection (3,000 per model per language, 30,000 responses total). Each model is given only the bibliographic reference and asked to reproduce the exact Hadith text, with no retrieval augmentation, and is scored on lexical fidelity (BLEU) and semantic fidelity (multilingual cosine similarity), with refusals flagged separately. Across all five models and both languages, 0% of 30,000 responses achieve both high lexical and high semantic fidelity, i.e., an exact, verifiable match to the source text. Arabic responses fare uniformly worse than English. These findings suggest that current open-weight LLMs, used without retrieval grounding, are unreliable and potentially dangerous sources for exact religious-text recall, and that deployment for Islamic scholarship should mandate retrieval-augmented generation over a verified corpus rather than parametric memory. The complete code, prompts, evaluation pipeline, and scored outputs are publicly available at https://github.com/dayam8696/Hadith-Hallucination-Benchmark.

[📄 Read PDF](https://arxiv.org/pdf/2611.02587v1)

---

## 8. BasisKV: Value Latents for Communication and Key Routing
**Authors:** Lixun Zhang, Zishan Shao, Kangning Cui, Yu Liang, Fan Yang, Yiran Chen

**Summary:** Long-context large language model (LLM) inference is increasingly constrained by the cost of maintaining an ever-growing KV-cache. Low-rank K/V projections provide a promising way to compress the KV-cache with minimal quality loss, but prior work has largely optimized KV-cache compression in isolation, leaving distributed inference, especially with tensor parallelism where attention computation is partitioned across multiple GPUs, largely underexplored. We make two observations: (i) tensor-parallel communication is an important cost when deploying low-rank KV-cache compression in distributed inference; and (ii) Value compression can be associated with the output projection, allowing the same low-rank Value representation to reduce both Value-cache width and tensor-parallel communication. Based on these observations, we propose BasisKV, a low-rank KV-cache compression method for communication-intensive, long-context LLM inference. BasisKV jointly optimizes the low-rank factors across per-GPU attention partitions against the complete attention output, rather than fitting each partition in isolation. The compressed Value cache is further reused to help identify which Key pages should be accessed: it predicts part of the Key information needed for routing, while a Key-specific residual stores what cannot be recovered from Value. The original Keys are then retrieved only for the selected pages to compute exact QK scores. Across multiple LLM families and system settings, BasisKV achieves a better quality--efficiency tradeoff than existing low-rank baselines, reaching up to 1.42x end-to-end speedup under 8-GPU tensor-parallel inference. Our code is available at https://github.com/alexz949/BasisKV

[📄 Read PDF](https://arxiv.org/pdf/2611.02583v1)

---

## 9. SMILE: A Structured Multi-Agent Clinical Reasoning for Liver Ultrasound Understanding
**Authors:** Haris Ghafoor, Minjee Seo, Seonaeng cho, Keungmo Yang, Jaejun Lee, Kyungho Yoon

**Summary:** Automated liver ultrasound report generation improves the diagnosis of liver diseases by producing clinically structured descriptions of anatomical and disease-related findings. However, current generative vision-language models (VLMs) often rely on a single reasoning pathway that maps ultrasound appearance directly to textual descriptions. In addition to the inherent vision-language modality gap, this design is limited for liver ultrasound because disease interpretation is constrained by subtle visual evidence, heterogeneous disease patterns, and limited paired supervision. To address these limitations, we propose SMILE, a Structured Multi-agent clInicaL rEasoning framework that uses multiple complementary specialist agents to interpret ultrasound images and consolidates their outputs through a judge-guided consensus mechanism. Our approach employs three specialized agents: an image interpretation agent for morphological descriptions, a clinical-stage reasoning agent, and a visual question answering (VQA) agent for targeted queries. These agent responses are then aggregated and scrutinized by a judge VLM using a consensus filtering prompt to produce a unified, clinically coherent output. Across a public liver ultrasound dataset and an internal clinical dataset, SMILE consistently outperforms state-of-the-art VLMs, achieving up to 19.0\% improvement in ROUGE-1 and 18.8\% improvement in clinical F1-score, while reaching VQA F1-scores of 0.82 and 0.65 on public and internal datasets, respectively. These results demonstrate the potential of SMILE for data-scarce and limited-supervision clinical settings. Our models, datasets, and code are available \href{https://github.com/CMME-Lab/SMILE}{here}.

[📄 Read PDF](https://arxiv.org/pdf/2611.02581v1)

---

## 10. Probing Local Conditional Fit for Diffusion Model Membership Inference
**Authors:** ByungHee Cha, Naoki Murata, Yuhta Takida, Jong Chul Ye, Yuki Mitsufuji

**Summary:** Membership inference determines whether a candidate example was used to train a text-to-image diffusion model and is an important tool for auditing training-data use. We identify a directional membership signal in \emph{conditional prediction shifts}, the changes in predicted noise under alternative text conditions at a fixed noisy input: whether movement toward the alternative prediction initially lowers or raises the denoising loss from its value under the original caption. Members exhibit less room for such local improvement. To quantify this response, we propose \emph{LoFIT} (Local Conditional Fit), which measures the initial response of the denoising loss along normalized prediction shifts and aggregates it across multiple text conditions and diffusion states. LoFIT requires no target-model gradients and can be computed using only forward queries to the denoiser. Evaluations on four datasets show improved membership discrimination across fine-tuned and pretrained models. LoFIT distinguishes members early in fine-tuning, while the naive denoising-loss baseline remains near chance. Controlled comparisons show that the membership signal is concentrated in the first-order response, with little discrimination from prediction-shift magnitude alone.

[📄 Read PDF](https://arxiv.org/pdf/2611.02578v1)

---

