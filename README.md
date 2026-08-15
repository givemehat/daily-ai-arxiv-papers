# 🤖 Daily AI Research Papers

<div align="center">
  <img src="https://img.shields.io/github/repo-size/givemehat/daily-ai-arxiv-papers?style=for-the-badge&color=blue" alt="Repository Size" />
  <img src="https://img.shields.io/github/license/givemehat/daily-ai-arxiv-papers?style=for-the-badge&color=green" alt="License" />
  <img src="https://img.shields.io/github/commit-activity/m/givemehat/daily-ai-arxiv-papers?style=for-the-badge&color=orange" alt="Commit Activity" />
  <img src="https://img.shields.io/github/last-commit/givemehat/daily-ai-arxiv-papers?style=for-the-badge&color=red" alt="Last Commit" />
</div>

*Automatically fetched on 2026-08-10*

This repository automatically fetches the latest top research papers in Artificial Intelligence, Machine Learning, and Computer Vision from arXiv every day.

---

## 1. SimWAM: A Simple World Action Model for End-to-End Autonomous Driving
**Authors:** Zongchuang Zhao, Xin Zhou, Tianyang Xu, Zhengyang Sun, Kaixuan Zhou, Honglin Li, Dingkang Liang, Xiang Bai

**Summary:** World-Action Models (WAMs) improve end-to-end autonomous driving by transferring video dynamics priors to action prediction, but existing methods require costly future generation at inference. We present SimWAM, a simple yet effective WAM that uses video generation purely as a training signal. It co-trains a pretrained video expert and a lightweight action expert with joint flow matching. An isolated attention mask keeps action prediction independent of future frames, allowing the video branch to be discarded after training and leaving a self-contained planner that directly predicts trajectories. Since the two experts share no parameters and interact only through a unified attention interface, the video backbone could be replaced and the action expert scaled independently without modifying the learning objective or inference pipeline. We further apply reinforcement learning to optimize a compositional driving reward beyond trajectory imitation. Our SimWAM achieves $91.5$ PDMS on NAVSIM, surpasses state-of-the-art WAM-based planners with substantially lower latency, and transfers zero-shot to nuScenes. These results position SimWAM as a simple yet solid baseline that could readily benefit from advances in video generation for efficient autonomous driving. The code and model weights are available at https://github.com/H-EmbodVis/SimWAM/

[📄 Read PDF](https://arxiv.org/pdf/2608.07468v1)

---

## 2. MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation
**Authors:** Youjun Zhao, Alex Warren, Gary K. L. Tam, Rynson W. H. Lau

**Summary:** Recent advances in video diffusion models (VDMs) have enabled high-fidelity video synthesis. However, generating mirror reflections remains challenging because the content within a mirror must remain consistent with the surrounding scene. Existing VDMs are not specifically designed to model scene-to-mirror relationships, which can lead to reflections with incorrect content or inconsistent spatial arrangements. We observe that mirror reflection generation involves two complementary challenges: determining what scene content should be reflected and how the reflected content should be spatially arranged within the mirror region. Motivated by this observation, we propose MirrorWorld, a reflection-aware video inpainting framework that models scene-to-mirror relationships during generation. Specifically, we introduce Semantic Relation Distillation (SRD), which transfers relational information from a frozen visual foundation model to encourage semantic associations between visible scene content and mirror regions. We further propose Geometric Transformation Alignment (GTA), which learns a transformation that guides the spatial arrangement of reflected content. The two components play complementary roles, with SRD modeling what should be reflected and GTA modeling how it should be arranged. To facilitate research on this problem, we construct a benchmark for video mirror reflection generation by repurposing four existing video mirror datasets into a unified reflection reconstruction task. Experimental results show that MirrorWorld achieves improved reflection reconstruction quality over representative image-based reflection generation methods and strong video inpainting baselines.

[📄 Read PDF](https://arxiv.org/pdf/2608.07463v1)

---

## 3. CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity
**Authors:** Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin

**Summary:** While post-training improves the capabilities of large language models (LLMs), it generally lowers their output diversity and creativity, negatively impacting tasks that explicitly require creativity (e.g., story generation) as well as those that require it implicitly, e.g., reinforcement learning (RL). We instead propose CreativeInstruct, a scalable instruction-tuning method that teaches LLMs to balance creative, base-model-like generations with the quality of post-trained models, by learning to inject special [StartCreativity] spans that bias generation toward creativity. Furthermore, we introduce a structural diversity metric based on graph edit distance, which captures narrative level variation missed by purely lexical and semantic metrics. On narrative generation, CreativeInstruct matches or exceeds the diversity of both multi-model baselines and distilled variants of their outputs, without sacrificing quality or requiring multiple models at inference time. These results are mirrored in our human evaluation, where we find that annotators rate CreativeInstruct generations as more creative than the post-trained LLMs' generations in 70.3% of cases. We also show the benefits of creative models as a substrate for RL: GRPO applied to a CreativeInstruct checkpoint improves by ~4% on AMC and ~5% points on MATH over the same training applied to the post-trained checkpoint.

[📄 Read PDF](https://arxiv.org/pdf/2608.07460v1)

---

## 4. CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG
**Authors:** Gyuwan Kim, Cheoneum Park, Tao Yang

**Summary:** Recent optimization studies on Retrieval-Augmented Generation (RAG) have exploited chunk-level KV cache reuse to avoid processing long retrieved contexts for higher efficiency, while significant information redundancy and noise still remain in the coarse-grained chunks. This paper optimizes the Pareto frontier under low prefill latency constraints while maximizing accuracy by proposing CoinRAG (Contextualized Information Nugget KV Cache Reuse for Long-Context RAG). The name metaphorically reflects our core mechanism: much like assembling small tokens (or "coins") to accumulate a larger value, CoinRAG compositionally reuses offline-computed, fine-grained nugget caches to form a learned contextual representation efficiently in a more semantically relevant but compact manner. Specifically, instead of full-chunk encoding, CoinRAG identifies query-relevant semantic units within retrieved chunks through two-stage retrieval and seamlessly assembles their sliced KV representations with a chunk-level context. Extensive evaluations on LongBench multi-hop question answering tasks demonstrate that CoinRAG significantly reduces operational costs and outperforms the other baselines with a new Pareto frontier and an average 5.3% relative improvement in answer quality (F1) under a standard fast prefill latency budget.

[📄 Read PDF](https://arxiv.org/pdf/2608.07458v1)

---

## 5. Interaction Creates Dynamical AI Behavior Absent in Isolation
**Authors:** Bella Xinrui Li, Frank Yingjie Huo, Neil F Johnson

**Summary:** What will happen when AI agents interact in daily life, e.g. when one AI starts bossing another around? We find a counterintuitive answer that opens new avenues for out-of-equilibrium Physics. When a boss AI directs a stream of messages at the subordinate AI while ignoring its replies, it drives the subordinate into an alien behavioral state that it would never have exhibited alone. Although the two AIs share the same well-defined (decoding) temperature, the subordinate neither copies its boss nor returns to how it behaves on its own; instead, it adopts an entirely different behavior. The boss's added value is similar to a pre-recorded tape. When the boss listens, they both adopt a similar alien dynamical state. A simple kinetic theory captures the principal effects, such as why the way in which the same messages are delivered will matter in future AI-AI interactions.

[📄 Read PDF](https://arxiv.org/pdf/2608.07457v1)

---

## 6. Strategy-first synthesis planning for complex natural products
**Authors:** Daniel Armstrong, Xuan-Vu Nguyen, Octavian Susanu, Gabriel Gibberd, Théo A. Neukomm, Taddäus Strunden, Dan Forster, Morgane Delattre, Shawn Teh, Clément Rols, John Federice, Hayden Leatherwood, M. Lavelle Barnes, Maarten R. Dobbelaere, Peter Wipf, Jon T. Njardarson, Jieping Zhu, Philippe Schwaller

**Summary:** The total synthesis of a complex molecule is among the most demanding intellectual and experimental feats in chemistry: a chemist must plan many steps ahead for how to assemble simple building blocks into an intricate target, devise backup strategies, and anticipate procedural challenges. It is also a profoundly creative activity. For half a century, efforts to automate the retrosynthetic design of natural products and other complex molecules have drawn on catalogued reactions, and the resulting tools now report near-complete success on benchmarks built from that same source. But these tools were shaped to fit benchmarked chemistry, and they falter on many natural products, the frontier of the field, whose densely functionalized, polycyclic architectures demand precisely the inventive chemistry the record contains least. Whether a machine could reasonably design such syntheses like an expert chemist does has remained unclear. Here, we show that SynthEx, an agentic framework built on large language models, plans routes to complex natural products that lie beyond the reach of conventional design algorithms. SynthEx proposes competing strategies, assembles a sequence of routine and key steps into a cohesive route, and critiques and improves its own design; the chemistry it favours is more convergent than existing tools produce, and spans a region of reaction space that catalogue-based tools cannot match. Most notably, in blinded assessments, expert chemists judged its key steps comparable to those of published human syntheses and engaged with them as genuine synthesis plans, a response algorithmic route prediction has not previously accomplished. We release routes to more than a thousand natural products as SynthAtlas, an open, interactive database, and anticipate it will become a shared resource for a collection of complex target molecules that lack existing literature routes.

[📄 Read PDF](https://arxiv.org/pdf/2608.07454v1)

---

## 7. SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent
**Authors:** Mingxuan Zheng, Yujin Zhou, Chuxue Cao, Boqin Yin, Yuyao Zhang, Jiapeng Sun, Shuaishuai Gong, Sirui Han, Yike Guo

**Summary:** LLM agents increasingly adapt to recurring tasks by accumulating procedural knowledge in skills. These skills are lightweight, reusable textual artifacts that are loaded into the agent's context without weight updates. Recent methods refine skills through iterative task execution, failure diagnosis, and trajectory-guided text-space updates. However, existing frameworks lack explicit diagnosis--outcome feedback and treat deletion as a generic edit operation rather than a dedicated mechanism for consolidating accumulated knowledge. We introduce SkillProx, a proximal-gradient-inspired forward--backward framework that couples closed-loop diagnostic evolution with utility-aware proximal refinement. Motivated by a composite objective balancing task loss and skill complexity, the forward stage re-executes diagnosis-driven edits on the same task batch, rolls back regressions, and feeds measured outcomes into subsequent diagnoses. The backward stage decomposes the resulting skill into auditable knowledge units, estimates their contributions using a frozen leave-one-out utility audit, and applies validation-gated consolidation, demotion, or removal. Experiments on in-distribution and out-of-distribution benchmarks across multiple backbone LLMs show that SkillProx improves average accuracy by 3.0 percentage points over the strongest gradient-based baseline. Component ablations demonstrate the complementary effects of closed-loop diagnosis and proximal refinement.

[📄 Read PDF](https://arxiv.org/pdf/2608.07449v1)

---

## 8. Taxonomy-Driven Analysis of Open-Source AI Risk Mitigation Tools
**Authors:** Afreen Alam, Evgenija Popchanovska, Ana Gjorgjevikj, Maryan Rizinski, Lubomir T. Chitkushev, Irena Vodenska, Dimitar Trajanov

**Summary:** Rapid adoption of large language models (LLMs) in enterprise settings has introduced operational, security, and governance risks. As generative AI applications move from pilot to production, manual harm identification and mitigation are becoming difficult to scale. Although many tools support model evaluation, adversarial testing, runtime guardrails, and observability, the tooling landscape remains fragmented. Tools are typically designed for specific engineering tasks and described in technical terms that do not align with governance frameworks or risk taxonomies, making it difficult to determine which tools address which risks and where critical gaps remain. This paper proposes a structured protocol to automate AI risk mitigation through a taxonomy-driven analysis of open-source LLM evaluation and security tools. We map the capabilities of 21 prominent open-source tools to the 32 subcategories of the extended MIT AI Risk Mitigation and Response Taxonomy. An LLM-assisted retrieval-augmented generation pipeline analyzes source code and documentation to extract capabilities for each taxonomy category. Reliability assessment yielded moderate agreement (Fleiss' Kappa = 0.509) among three independent reviewers. The analysis reveals a highly skewed landscape in which tools cluster around technical and operational controls, while governance, legal and regulatory, and financial and market controls remain largely unaddressed. This motivates a layered risk-mitigation architecture combining tool-based controls with organizational and regulatory processes. The mapping protocol achieved an F1 score of 75.5% after majority voting. Overall, the study provides a practical mapping between enterprise AI risk categories and open-source mitigation capabilities, identifies where human oversight remains necessary, and presents a taxonomy-driven framework applicable to open-source and proprietary solutions.

[📄 Read PDF](https://arxiv.org/pdf/2608.07446v1)

---

## 9. RIS-Aided mmWave Localization Under Cross-Link Interference via Beam-Domain ML Fingerprinting
**Authors:** Md Tarek Hassan, Dmitry Zelenchuk, Muhammad Ali Babar Abbasi

**Summary:** Accurate user equipment (UE) localization is critical for beam management in reconfigurable intelligent surface (RIS)-assisted millimeter-wave (mmWave) based sixth-generation (6G) networks, especially if the direct base-station-UE links are unavailable. This paper proposes a beam-domain fingerprint framework that maps the received signal-to-noise ratio (SNR) across a small set of predefined RIS reflection states to the UE azimuth angle and range, without requiring channel state information (CSI). Crucially, we extend the framework to a realistic interference-impaired scenario in which a nearby cross-link interferer (CLI) corrupts the clean SNR fingerprint, yielding a signal-to-interference-plus-noise ratio (SINR) fingerprint; an interference-to-noise ratio (INR)-constrained calibration strategy keeps the interference level physically interpretable. Four machine-learning (ML) regressors are evaluated under both conditions. Simulation results at 28 GHz with a 20x20 RIS show that k-nearest neighbors (KNN) achieves the lowest angle MAE of 0.37 degrees and range MAE of 4 cm under clean conditions, rising to 1.4 degrees and 7.6 cm under interference. A key finding is that interference degrades angle estimation substantially more than range estimation across all models, a consequence of the asymmetric encoding of location information in the beam-domain fingerprint.

[📄 Read PDF](https://arxiv.org/pdf/2608.07444v1)

---

## 10. Blast Radius
**Authors:** MY Pitsane, Hope Mogale

**Summary:** Agentic coding faces growing problems of affordability and wasted tokens. We introduce Blast Radius, a predictive memory management layer that estimates an incoming prompt's reach through coupled context and code channels. NECROPHORESIS enables reversible eviction by archiving dead context verbatim, while Recurring Dead Matter (RDM) identifies and buries repeatedly occurring transcripts. We formulate reversible context eviction over a Polish context space, providing a measurable foundation for retention, recurrence, and eviction while connecting context entropy to resurrection probability. Across seven OpenAI models, Blast Radius reduced token consumption by 17-26%, achieved the lowest overflow rate among tested policies, and remained byte exact reversible. Of 450 buried bodies, 378 were recurring dead matter and zero were recalled. Blast Radius operates beneath HCRC, determining which records to bury and how far an incoming prompt may reach into the codebase. This work contributes to the broader goal of Algosophy: making large language models and agentic coding more reusable and sustainable.

[📄 Read PDF](https://arxiv.org/pdf/2608.07440v1)

---

