# 🤖 Daily AI Research Papers

*Automatically fetched on 2026-10-30*

This repository automatically fetches the latest top research papers in Artificial Intelligence, Machine Learning, and Computer Vision from arXiv every day.

---

## 1. Hybrid AI Patterns: Thirteen Ways to Couple Language Models with Rules, and How to Choose Among Them
**Authors:** Siegfried Handschuh, Götz-Henrik Wiegand, Lorena Raichle

**Summary:** Language models handle text well, and rule engines give conclusions with proofs. Systems that combine the two are usually described by example, and the same coupling turns up under different names in agent frameworks, guardrail toolkits and neuro-symbolic research. This document defines thirteen patterns for coupling a language model with an executable rule language, in the catalogue form introduced for object-oriented design: intent, motivation, applicability, participants, collaborations, consequences, implementation, known uses and related patterns. Four patterns concern what crosses the boundary between model and rules, five who controls whom, three how the model takes part in the reasoning, and one how knowledge is kept over time. Five invariants hold for every combination, and five failure patterns name the couplings that break them. We relate the catalogue to published pattern catalogues and taxonomies of hybrid and neuro-symbolic systems and show where they overlap with it. A decision guide leads from a problem to a pattern. It rests on our measurements, including the cases in which a model alone did as well as the hybrid or better, and it reports what each design cost.

[📄 Read PDF](https://arxiv.org/pdf/2610.40036v1)

---

## 2. Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information
**Authors:** Daniel Strauss, Nikolaos Sotirakis, Zhenshan Bing, Alois Knoll

**Summary:** Memory in reinforcement learning raises two problems. Attention finds the relevant item by scoring the whole store, which is costly for robots under latency and energy limits. When a retrieved memory pays off, credit for acquiring it must cross the whole sequence. We argue that both are governed by one quantity, the value of information, and propose to estimate it from archived rollouts with a learned world model. We obtain that, when read at the observation, it yields a provable lower bound on the optimal value of the acquiring action, which floors its TD target and attributes this floor to the observation that earned it. Read at the decision, it defines the optimal retrieval set. A pilot retrieval system, to be trained and improved with this signal, solves a memory task with reduced context.

[📄 Read PDF](https://arxiv.org/pdf/2610.40030v1)

---

## 3. Segment Anything Model Based Context Guided Mamba Unet for Medical Image Segmentation
**Authors:** Chenchen Wang, You Zhou

**Summary:** Medical image segmentation is crucial for clinical diagnosis and treatment planning, requiring both global contextual understanding and fine-grained structural precision. While the Segment Anything Model (SAM) demonstrates strong generalization capabilities, its direct application to medical images often lacks domain-specific adaptability. Meanwhile, State Space Models (SSMs)-based methods, such as Mamba, efficiently capture long-range dependencies but may struggle with preserving fine anatomical details. To address these challenges, we propose a segment anything model based context guided mamba unet, SAMBA-UNet, a novel framework that integrates SAM's context knowledge with Mamba's hierarchical feature learning to enhance both global representation and local detail refinement. Specifically, we introduce the Hierarchical Context Enhancement Module (HCEM), an attention-based fusion module that deeply incorporates the multi-level features of SAM and Mamba to improve detail perception and segmentation precision. Additionally, we employ LoRA and Adapter-based fine-tuning to adapt SAM to medical imaging tasks, further enhancing its domain-specific segmentation capability and robustness. We conducted a comprehensive study on several medical segmentation datasets, including Synapse, ISIC17, and ISIC18, evaluating our method across multiple metrics. Experimental results demonstrate that SAMBA-UNet achieves state-of-the-art performance, effectively balancing generalization, segmentation accuracy, and computational efficiency. Our code will be released upon acceptance.

[📄 Read PDF](https://arxiv.org/pdf/2610.40029v1)

---

## 4. HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization
**Authors:** Jianghan Zhu, Cong Zhang, Ni Zhang, Yifan Yang, Yew Soon Ong, Zhiguang Cao

**Summary:** Automatic operator design (AOD) has increasingly adopted large language models (LLMs) to generate problem-specific search and variation operators for multi-objective combinatorial optimization (MOCO). Yet most methods evolve the operators while leaving the process that discovers them fixed. This limits adaptation as new Pareto trade-offs and operator interactions change where and how the search should proceed. We introduce HEMO, which makes the AOD harness itself a self-evolving optimization target. HEMO maintains a persistent harness state and updates one module at a time, revising the logic that determines which experience to retrieve, which operators to improve, which parents to select, and how to formulate the orchestration of search steps. Downstream solution quality and runtime guide these updates, while a discounted UCB scheduler directs adaptation toward promising modules as their utility changes. A persistent memory filesystem preserves candidate outcomes and diagnostic feedback across harness states, enabling successive states to build on accumulated optimization experience. Experiments across eight MOCO tasks and two structurally distinct evolutionary backbones demonstrate strong performance against conventional evolutionary, neural, and LLM-based AOD baselines, together with effective transfer to related tasks. HEMO extends automatic operator design beyond evolving individual operators to improving the search process that discovers them.

[📄 Read PDF](https://arxiv.org/pdf/2610.40023v1)

---

## 5. DINOv2 for PET: A Pre-Training Domain Benchmark Across Classification, Segmentation, and Prognosis
**Authors:** Roxanne De Maeyer, Yannick Brackenier, Vicky De Ridder, Simon DeKeyser, Maarten Larmuseau, Jef Vandemeulebroucke

**Summary:** DINO (self-DIstillation with NO labels) has become a stan- dard for self-supervised pre-training, producing features that generalise across datasets and downstream tasks. In medical imaging it has been adopted mainly for radiology (X-ray, CT and MRI), where even natural- image DINO features transfer well. In the literature, these features have been reported to transfer worse to functional imaging such as PET. Yet PET-specific DINO models have barely been introduced, and even less validated across multiple tasks and datasets. We present PET-DINOv2-2D, the first DINOv2 model pre-trained on 2D PET, and benchmark it against open-source encoders: the origi- nal DINOv2 (pre-trained on the LVD-142M natural-image dataset) and OmniRad (pre-trained on CT, MRI and ultrasound). Using the same lightweight heads for every backbone, and despite far less pre-training data, PET-DINOv2-2D matches or outperforms both on three down- stream PET tasks: normal/abnormal classification, lesion segmentation and recurrence-free survival prognosis. Its advantage is largest when few labels are available, suggesting that PET pre-training gives more transferable, label-efficient features. Code is made available at https://github.com/nuclivision/pet-dinov2-2d/.

[📄 Read PDF](https://arxiv.org/pdf/2610.40018v1)

---

## 6. FIDE: Fiber-Informed Differentiable Experimental Design for Reference-Relative Law Dynamics
**Authors:** Pietro Zanotta, Ján Drgoňa

**Summary:** Aggregate measurements generally leave an evolving population law underdetermined, so different measurement systems can be equally adequate for a scientific task while constraining different aspects of the law. We study how to resolve this residual design freedom in baseline-preserving settings, where an existing dynamical model remains the working baseline outside quantities explicitly valued by the task. \textbf{F}iber-\textbf{I}nformed \textbf{D}ifferentiable \textbf{E}xperimental Design (\textbf{FIDE}) completes each candidate's aggregate constraints by information projection relative to a common frozen reference, then ranks scientifically adequate designs by the dynamical revision required to realize the resulting completed paths. The resulting \emph{Full action} is the minimum mean-squared velocity correction needed to realize a completed path; equivalently, its square root is the sharp reference-relative expectation-rate discrepancy over a gradient-normalized Sobolev class. This defines a conditional minimum-revision principle for baseline-preserving design rather than a generic truth-recovery objective. Experiments show that this preference changes sensor selection, can help or harm withheld downstream predictions depending on baseline reliability, can be used prospectively from aggregate predictions, and remains computationally usable for a $32$-dimensional configuration law.

[📄 Read PDF](https://arxiv.org/pdf/2610.40009v1)

---

## 7. Greenscapes: Optimized Vegetation Configurations in Cities
**Authors:** Patryk Bartkowiak, Marcin Marlewski, Paweł Wójcik, Jae Joong Lee, Dominik L. Michels, Bedrich Benes, Sören Pirk, Wojciech Pałubicki

**Summary:** Vegetation plays a central role in cities, serving functional roles such as balancing shade and sky exposure, shaping the microclimate, carbon sequestration, and providing acoustic screening. Furthermore, aesthetic choices in landscape styles (formal, modernist, picturesque) are important for citizens' well-being and should be considered in the design of urban landscapes. In this paper, we present a novel method for placing vegetation, ranging from shrubs to large trees, in 3D urban scenes. Our method uses individual lots as input and employs a conditioned Vision-Language Model (VLM) to generate a top-down rendering of vegetation, placing large trees, small trees, and shrubs on lawn areas. This rendering is then converted into a 3D scene by detecting individual plants and selecting appropriate 3D assets. To refine the proposed configurations, we define an optimization loop that keeps the VLM-generated positions fixed after a deterministic feasibility repair and uses CMA-ES to optimize per-instance scale transformations along with discrete vegetation asset substitutions. To define the objective function for the optimization, we evaluate the generated 3D scenes with efficient surrogate models of shade and path-based acoustic exposure. Furthermore, we render in-scene views at each optimization step to compute view-dependent perceptual descriptors, enabling the generation of both aesthetic and functional vegetation layouts for urban scenes.

[📄 Read PDF](https://arxiv.org/pdf/2610.40007v1)

---

## 8. Human--AI Interactions as First-Class Data: A Formal Interaction Model and Runtime for Explainable AI Collaboration
**Authors:** Michela Taufer, Kin Ng, Ian Lumsden, Aashish Pandey, Rajasi Gore, Angelina Ju, Sukanya Moudgalya, Ewa Deelman, Sai Swaminathan

**Summary:** AI assistants are increasingly embedded in computational notebooks, scientific workflows, software engineering tools, and learning systems, yet human-AI interactions are often treated as transient prompt-response exchanges rather than durable data products, hindering reproducibility, explainability, replay, behavioral analysis, and adaptive AI support. We argue that these interactions form a new data class requiring formal representation and introduce the Human-AI Interaction Description Language (HAIDL), a formal interaction model with a Backus-Naur Form-inspired concrete syntax. HAIDL encodes each interaction as a structured object capturing computational context, user request, prompt payload, AI response, feedback, problem context, provenance, and model metadata. We integrate this vision into HAIDL-X, a middleware for JupyterLab that instantiates HAIDL by capturing user-bot state, building contextualized prompts, interfacing with AI providers, collecting feedback, and storing interactions in a repository. We add a learning layer over HAIDL that maps interaction objects and notebook execution traces into reproducible measures of user behavior, including engagement, performance, help-seeking, error-oriented use, and learning personas. HAIDL-X provides a foundation for treating human-AI collaboration as structured, queryable, replayable, analyzable data.

[📄 Read PDF](https://arxiv.org/pdf/2610.40006v1)

---

## 9. Efficient Learning of Mechanism Designs and Compositionality
**Authors:** João Pedro Gandarela, Thiago Rios, Stefan Menzel, André Freitas

**Summary:** Learning mechanism behaviour requires a representation of how connected parts jointly constrain motion. We study whether exposing reusable constraint subassemblies improves prediction from limited data. Assur-KB represents planar mechanisms through irreducible modules, boundary interfaces, and solve dependencies while retaining source geometry. Our theoretical results characterize transfer through module interfaces and establish physical limits arising from missing interface information and accumulated sensitivity. To test the representation claim directly, the experimental design compares matched mechanism-curve pairs across training budgets within the same multilayer-perceptron family. This controlled comparison establishes the utility of the complete representation in the evaluated learning setting. Assur-derived features provide a geometric-mean $1.8\times$ advantage in sample efficiency over flattened adjacency and position inputs across budgets of 50-10,000 mechanisms. Separate experiments establish invariance under tested joint relabelings, higher valid-generation rates under dyadic composition, and a coarser structural index over 10.02 million mechanisms. In summary, the theory and experiments identify how physical constraint structure supports limited-data prediction and which interface conditions govern compositional reuse.

[📄 Read PDF](https://arxiv.org/pdf/2610.40005v1)

---

## 10. How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function
**Authors:** Dabin Seo, Eunhyek Joa

**Summary:** Reasoning vision-language-action (VLA) policies write a reasoning trace and then decode the action from it. A wrong trace yields a wrong action, and even a correct-looking trace can mislead the plan. Existing remedies ask whether the reasoning is right. We ask how strongly it should steer. CoC-CFG applies classifier-free guidance between the policy's context and the same context without the reasoning span. One weight per Euler step attenuates or amplifies the reasoning, and w=1 recovers the original policy. We treat the choice of this weight as a Markov decision process whose action values are measured, not bootstrapped. With the expert frozen and the noise fixed, applying a weight for one step and finishing the plan under the current controller returns that weight's value exactly. Q-adaptive guidance fits these values with small critics and improves the controller conservatively. In the Alpasim driving simulator it outperforms every fixed weight and online RL (SAC, GRPO) in open loop, and in closed loop it passes 262 of 300 scenes, against 252 for the original policy. On held-out frames of the Waymo end-to-end driving benchmark, its first three stages outperform every fixed weight, four adaptive-guidance methods, SAC and GRPO. On the hidden test set, a frozen Alpamayo 1.5 with rule-based camera and vehicle conversions and Q-adaptive guidance sets a new state of the art among published methods: 8.135159 rater feedback score, against 8.079 for the best published method.

[📄 Read PDF](https://arxiv.org/pdf/2610.40002v1)

---

