# 🤖 Daily AI Research Papers

*Automatically fetched on 2026-08-28*

This repository automatically fetches the latest top research papers in Artificial Intelligence, Machine Learning, and Computer Vision from arXiv every day.

---

## 1. UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City
**Authors:** Tianjie Ju, Zheng Wu, Yueqing Sun, Yuhan Cui, Bobo Li, Shengqiong Wu, Pengzhou Cheng, Haodong Zhao, Zongru Wu, Xinbei Ma, Doris Zhang, Kunling Li, Mong-Li Lee, Wynne Hsu, Hao Fei, Qi Gu, Gongshen Liu, Zhuosheng Zhang

**Summary:** Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investigate how far current MLLM agents can turn local urban perception into reliable action in a complicated real-scale city. We propose UrbanGround, the first sandbox to make this question testable in a physically constrained replica of Hong Kong built from territory-wide 3D geospatial data. UrbanGround supports closed-loop interaction from a first-person view and provides an interactive map for navigation. Agents can directly enter the 3D city and explore from a first-person view. Our analysis follows the growth of the spatial problem through three research questions. We first test whether an agent can ground a local scene well enough to answer spatial questions after active observation. Then we ask whether that grounding supports navigation as destinations become farther away and less explicit. Finally, we examine whether the resulting behavior survives changes in route availability and pedestrian motion. Contemporary MLLM agents usually show useful atomic abilities in visual recognition and short-range spatial reasoning, while orientation and pedestrian-aware movement remain unreliable. Their central failure emerges over extended exploration, where local abilities do not compose into sustained goal-directed behavior and errors accumulate without effective correction. We hope UrbanGround will support broader study of how far current MLLM agents can explore reliably in complex, open-ended urban environments.

[📄 Read PDF](https://arxiv.org/pdf/2608.27456v1)

---

## 2. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution
**Authors:** Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu

**Summary:** Agent skills package specialized knowledge and workflows into reusable resources that extend AI agent capabilities. Recent work automatically discovers such skills from agent experience, which enables agents to progressively adapt through interaction. However, the insights that guide skill development typically remain scattered across optimization histories, limiting their systematic reuse across iterations. We introduce WikiSkill, a framework that co-evolves agent skills with a persistent knowledge base (wiki). At a high level, WikiSkill separates raw execution experience, accumulated knowledge, and executable skills, while continuously consolidating experience into the wiki, which subsequent skill updates can build on. Across diverse benchmarks and models, WikiSkill consistently outperforms state-of-the-art skill-evolution methods and improves over no-skill baselines in most model-benchmark settings. We find that skill evolution complements model scaling: larger models generally benefit more from evolved skills, while smaller models with skills can outperform substantially larger models without them. We also find that evolved skills transfer effectively across models and model families, and skills evolved by other models can outperform self-evolved skills. Finally, our ablation studies confirm that persistent knowledge accumulation in the wiki is critical for effective skill evolution. These results demonstrate the benefits of systematically accumulating and refining agent experience for developing reusable and transferable skills.

[📄 Read PDF](https://arxiv.org/pdf/2608.27454v1)

---

## 3. SWE-Prime: Fewer Trajectories, Better Performance
**Authors:** Dewu Zheng, Ruizhe Ye, Yanlin Wang, Yang Ye, Hongyu Zhang, Ensheng Shi, Xilin Liu, Yuchi Ma, Jianxing Yu, Zibin Zheng

**Summary:** To improve large language models' ability to resolve real-world software issues, prior work has focused on constructing large-scale agent trajectory datasets and performing supervised fine-tuning (SFT) on successful trajectories. However, task success does not guarantee high-quality supervision: successful trajectories may still contain ineffective, redundant, or risky steps. Directly using such trajectories for SFT can introduce noisy supervision and encourage models to imitate undesirable problem-solving behaviors. Therefore, we propose SWE-Prime, a multi-granularity, two-stage SFT data selection method that progressively filters training data at the trajectory and segment levels. Specifically, the first stage performs trajectory-level screening based on process quality, result quality, and data representativeness, selecting a high-quality and representative subset of successful trajectories. The second stage performs segment-level selection by grouping consecutive steps into semantic segments and assessing each segment based on its contribution to the final solution, learnability, and potential risks. During SFT, all segments remain in the sequence to preserve context, while only selected segments contribute to the loss computation. Experiments on SWE-Bench Pro and SWE-Bench Verified show that training on the 10% trajectory subset selected by SWE-Prime outperforms training on the full resolved dataset, yielding relative performance gains of up to 12.2% and 24.2%, respectively.

[📄 Read PDF](https://arxiv.org/pdf/2608.27449v1)

---

## 4. From Static to Dynamic: Benchmarking Real-World Code Review with MCR-Bench
**Authors:** Dewu Zheng, Yanlin Wang, Xiwen Wang, Kefeng Duan, Hongyu Zhang, Xilin Liu, Yuchi Ma, Zibin Zheng

**Summary:** In real-world software development, code review typically involves iterative interactions between developers and reviewers to improve software quality, making the process costly and time-consuming. Although recent work explores large language models (LLMs) for automated code review, most approaches oversimplify code review into a single-round, static decision task, which fails to capture the multi-round interactive nature and the complex problem-solving processes inherent in realistic review scenarios. To bridge this gap, we introduce MCR-Bench, the first defect state-aware benchmark designed for realistic multi-round code review. MCR-Bench covers five commonly-used programming languages and consists of 2,269 real-world multi-round code review tasks, each of which is annotated with fine-grained defect information and cross-round state labels. Each task in MCR-Bench is equipped with fine-grained defect metadata (e.g., description, type, severity) alongside dynamic state annotations, capturing the complete evolutionary trajectory of a defect throughout the multi-round process. We obtain several findings through extensive experiments on MCR-Bench with mainstream LLMs. (1) Limited overall capability: experiments reveal that mainstream LLMs exhibit limited overall performance in defect detection and defect lifecycle state tracking, with performance degrading significantly as the number of interaction rounds increases; (2) Defect-sensitive performance: LLMs' performance varies substantially across different defect types and severity levels, with semantically complex or low-salience defects being significantly more likely to be missed; (3) Underlying Failure Mechanisms: our in-depth error analysis dissects the distinct drivers of false positives and false negatives, revealing critical weaknesses such as cross-round temporal misalignment and inadequate long-range memory.

[📄 Read PDF](https://arxiv.org/pdf/2608.27442v1)

---

## 5. RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution
**Authors:** Junjie Zhang, Hui Liu, Kecheng Chen, Xianbo Mo, Changsheng Chen, Haoliang Li

**Summary:** LLM-based agents are increasingly deployed in product-level execution harnesses, where jailbreaks can trigger harmful tool use and persistent state changes, creating greater risks than unsafe text generation alone. Existing automatic red-teaming methods often rely on fixed attacks, while recent agentic attackers coordinate multiple jailbreak tools and show stronger potential through trajectory-based retrieval. However, such retrieval can reuse misleading experiences due to retrieval bias and unclear tool credit, and full trajectories add context overhead while reducing interpretability. We propose RedEvoAgent, a black-box red-teaming agent that distills cross-case attack trajectories into a concise, human-readable attack skill. The attack skill adaptively evolves through tool-effectiveness profiling and Deciding-Tool Attribution for skill updates, and a validation ratchet that retains only updates improving validation performance. Experiments on multiple benchmarks, target models, and target execution harnesses show that RedEvoAgent outperforms fixed and agentic baselines, improves tool efficiency, and transfers across attacker models and target execution harnesses.

[📄 Read PDF](https://arxiv.org/pdf/2608.27439v1)

---

## 6. Mechanistic Reaction Prediction via Discrete Flow Matching on Graph-Structured Electron Occupation
**Authors:** Nguyen Xuan-Vu, Octavian Susanu, Daniel Armstrong, Philippe Schwaller

**Summary:** Chemical reactions are fundamentally transformations in electron space, yet most machine learning approaches model them either through \textit{de novo} generation of product molecules or through heuristic graph edits that operate directly on molecular topology.
  We introduce MAELLE (\textbf{M}ech\textbf{A}nistic \textbf{E}dit f\textbf{L}ow-matching on e\textbf{L}ectron r\textbf{E}arrangements), which instead models reactions as discrete flow matching over electron occupation vectors.
  Concretely, we formulate the reactant-to-product mapping as a Continuous-time Markov Chain (CTMC) over the graph-structured integer-valued electron occupation space defined on all bonding, non-bonding, and hydrogen sites.
  To construct the intermediate edit trajectories, we generalize the discrete flow matching mixture path to discrete electron rearrangements using Optimal Transport, yielding a sequence of mechanistically interpretable edit moves without requiring elementary step annotations.
  MAELLE achieves competitive performance on the USPTO-480K benchmark compared with leading reaction prediction models.
  Beyond in-distribution accuracy, we evaluate robustness across two out-of-distribution settings - structural complexity and reaction type - and find that MAELLE maintains strong performance where existing methods degrade.
  Finally, because the learned flow operates over the full electron redistribution, MAELLE naturally recovers mechanistic trajectories that align with known chemistry and can predict side products of a reaction.

[📄 Read PDF](https://arxiv.org/pdf/2608.27429v1)

---

## 7. Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Audit
**Authors:** Yisen Xi

**Summary:** Large language model (LLM) agents in governed organizations must let the persona (instructions, tone, self-presentation) evolve freely, while keeping execution (stateful, audited work) traceable. A single trust domain does not satisfy both cheaply. We present Persona-Execution Separation (PES): persona and execution reside in different trust domains, connected by a governed contract bridge. The persona is singly-homed and may drift; execution is faceless and audited. Status summaries may return; data bodies remain in the restrictive domain except a graded data-loss-prevention (DLP) exception; identity stays continuous. An approval matrix, DLP, and audit enforce the crossing. PES follows from three goals---free drift, execution traceability, and decoupling. Under LLM representational indistinguishability, any single-domain mechanism that meets all three must re-introduce typed change objects, an external gate, and a stable audit anchor: PES rebuilt at higher coupling cost. A development/pilot case in a regulated digital-employee platform records five decisions over one month, each with a rejected alternative. A mechanism check on the shipped implementation found no execution-side re-validation under persona perturbation (five model configurations) and no persona fingerprint on hard-asserted fields. A probe of a recovered pre-separation build found the governed execution path decoupled from the persona by omission, not by construction; a later wiring change could reverse that isolation, which PES makes an audited architectural rule. The pattern applies when multi-user deployment, execution audit, and expected persona churn hold jointly.

[📄 Read PDF](https://arxiv.org/pdf/2608.27427v1)

---

## 8. Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners
**Authors:** Qianlong Lan, Vinothini Pandurangan, Anuj Kaul, Indranil Sanyal

**Summary:** Static scanners are increasingly used to identify executable or otherwise unsafe content in machine- learning artifacts, yet conventional evaluation metrics characterize only cases where a scanner yields a usable security judgment. We evaluate ModelScan, ModelAudit, and Fickling using a controlled, artifact-backed benchmark on a synthetic corpus of 170 Pickle and PyTorch focused artifacts across 145 specimen families, 135 of which have binary security ground truth and 10 of which are intentionally malformed without labels. We explicitly distinguish non-N/A coverage, analysis completion, definitive security decisions, non-security findings, and unsupported outcomes. On labeled families, ModelAudit produced definitive security decisions for all 135 families (100%), Fickling for 110 (81.5%), and ModelScan for 67 (49.6%). Conditional on making a definitive judgment, ModelScan achieved 100% precision, recall, and F1. Fickling identified no unique true- positive families beyond those found by the combination of ModelAudit and ModelScan. Furthermore, for the 48 malicious families where ModelScan failed to complete its analysis, both ModelAudit and Fickling generated detections consistent with ground truth. These findings underscore the need to separate judgment accuracy from judgment availability, as well as incremental detection coverage from tool-level redundancy.

[📄 Read PDF](https://arxiv.org/pdf/2608.27424v1)

---

## 9. Learning a Continuous Sepsis Severity Score Without Hour-by-Hour Supervision: A Two-Site Retrospective Study
**Authors:** Kevin Zhu, Ryan Zhang, Baraa Abed, Tilendra Choudhary, Malvern Madondo, Mehak Arora, Yixuan Yang, Alasdair Gent, Aditya Nagori, Omer T. Inan, Krista L. Haines, Patrick Georgoff, Suresh M. Agarwal, Vijay Krishnamoorthy, Tetsu Ohnuma, Mihai V. Podgoreanu, Michael R. Pinsky, Gilles Clermont, Craig M. Coopersmith, Craig S. Jabaley, Rishikesan Kamaleswaran

**Summary:** Currently used sepsis severity indices rely on fixed variables and weights established decades ago, which are coarsely discretized and calibrated to a cohort that no longer reflects contemporary critical care. No alternative learned directly from patient trajectories is in routine use. We conducted a retrospective two-cohort study on a total of 29,116 and 7,691 adult patients meeting Sepsis-3 criteria from two hospital systems in Massachusetts and Georgie, respectively.
  We developed a sepsis index using 43 routinely charted variables over a 72-hour treatment window. Unlike previous studies, we use mortality as a treatment-level ranking signal rather than a per-state target, allowing credit to be redistributed non-uniformly across timesteps. Evaluation was done on a permanent 20% test holdout, using clinical vignettes and Spearman correlation. Uncertainty intervals were obtained by bootstrap resampling of whole patients. Under this ranking scheme, non-survivors scored 1.19-1.64 points higher than survivors on a 0-10 scale within all strata of baseline SOFA-2, with similar results stratifying within lactate, mean arterial pressure (MAP), and creatinine. Within-patient change in the index correlated with change in lactate (Spearman rho = 0.39; n = 1,854). Similar, weaker correlations were found for MAP and creatinine. On a cohort level, cross-institutional agreement measured by Spearman correlation between models trained on different sites, were 70-77% of same-site correlation. External within-patient correlations were 0.54 and 0.59 against ceilings of 0.92 and 0.90. Our index also correlated with established indices, while null controls stayed near zero.
  Our index demonstrated hourly prognostic information that meaningfully separates patient outcomes and is consistent with clinical expectation, indicating potential as a decision support tool complementing clinical judgement.

[📄 Read PDF](https://arxiv.org/pdf/2608.27421v1)

---

## 10. Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information
**Authors:** Chanho Park, Daehyeon Choi, Jihyun Lee, Minhyuk Sung

**Summary:** Vision-language models (VLMs) can locate an image region referred to by a text prompt and route the corresponding visual evidence to the output, yet the internal mechanism behind this behavior is not understood. Inspired by retrieval heads in large language models, we ask whether VLMs contain an analogous mechanism for visual retrieval. We answer affirmatively by introducing Visual Retrieval Heads (VRHs), a small subset of attention heads (about 1.7-2.6%) that are causally responsible for grounding text descriptions to image regions. To find them, we recast existing head-scoring methods under a unified design space over query tokens, key aggregation, and cross-sample aggregation. We then show that scoring attention from output prediction tokens with a sum over the ground-truth referent region most reliably identifies causal heads. Across eleven VLMs and five referring-expression benchmarks, masking only the top 20 VRHs reduces grounding accuracy by up to 80 percentage points, while masking the same number of random heads has little effect. Beyond replicating the causal-sparse-universal triad established for text retrieval heads, VRHs exhibit several properties not previously reported: they generalize across visual reference tasks, remaining causal on attribute, spatial, counting, and visual-math benchmarks despite being discovered through bounding-box prediction; they are functionally specific, preserving output format while corrupting localization; and they are architecturally shared, transferring causally across VLMs that share an LLM backbone but differ in vision encoder, projector, and instruction tuning.

[📄 Read PDF](https://arxiv.org/pdf/2608.27417v1)

---

