<div align="center">

# Thrilok Manjunath

**MSc Data Science · Christ University, Bengaluru**

*Building intelligent, mathematically rigorous, and production-grade systems across AI/ML, Generative AI, Quantum Computing, and Full-Stack Engineering.*

[![Portfolio](https://img.shields.io/badge/Portfolio-thrilok--portfolio-6366f1?style=flat-square&logo=vercel&logoColor=white)](https://thrilok-portfolio-ruby.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-thrilokmanjunath-0A66C2?style=flat-square&logo=linkedin)](https://in.linkedin.com/in/thrilokmanjunath)
[![Email](https://img.shields.io/badge/Email-thrilokmanjunath@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:thrilokmanjunath@gmail.com)
[![Audit](https://img.shields.io/badge/Engineering%20Audit-Verified%20%26%20Reproducible-success?style=flat-square&logo=checkmarx)](https://github.com/thrilokmanjunath)

</div>

---

## 👨‍💻 About

I am a Data Science and Research Engineer committed to shipping real, scalable, production systems — not just prototypes and exploratory notebooks. My work bridges **empirical deep learning**, **generative AI verification**, **quantum-classical optimization**, and **cloud-native full-stack microservices**.

Currently pursuing my **MSc in Data Science at CHRIST University, Bengaluru**, where I serve as **President of the Quantum Club**, coordinating student researchers in quantum circuit design, QAOA formulations, and NISQ-era algorithms.

```
BCA / Data Analytics  ──►  Data Science Internship (Prodigy InfoTech)
                       ──►  MSc Data Science, CHRIST University
                       ──►  President, CHRIST Quantum Computing Club
                       ──►  Frontier AI · TDA · Quantum ML · Distributed Systems
```

---

## 📊 Flagship Systems & Engineering Benchmarks

| Project | Primary Focus & Innovation | Core Benchmark / Metric | Tech Stack |
| :--- | :--- | :---: | :--- |
| **[Synthetic Silence 2.0](https://github.com/thrilokmanjunath/SyntheticSilence2.0)** | Evidence insufficiency detection & manifold shift in LLMs | **AUROC 0.5463 (E0) → 0.2754 (E1)** (proven signal inversion) | Python, PyTorch, Conformal Prediction |
| **[TerraScope](https://github.com/thrilokmanjunath/TerraScope)** | Living digital twin of Earth & cosmos; real physics | **18,000 SDSS DR17 galaxies** 3D WebGL (60 FPS) | Next.js, Three.js, WebGL, Python |
| **[EV Battery Quantum](https://github.com/thrilokmanjunath/EV_Battery_Quantum)** | Hybrid Quantum-Classical battery pack design optimization | **100% convergence rate** (QAOA + QKSVM) | Qiskit, QAOA, FastAPI, Celery, Prometheus |
| **[Eyes on Tigers](https://github.com/thrilokmanjunath/Eyes-on-Tigers)** | Habitat integrity & Tiger Success Index (TSI) from orbit | **YOLOv8 mAP@0.5 = 0.842** (64ms CPU p95) | GEE Telemetry, YOLOv8 CV, Streamlit |
| **[PaperMate AI](https://github.com/thrilokmanjunath/PaperGraph)** | Research intelligence & interactive citation graph traversal | **3,450 req/s** (Project Loom audit), **18.4ms** graph p95 | Java 17/21 (Loom), Spring Boot 3, Next.js 16 |
| **[BLR Resilience AI](https://github.com/thrilokmanjunath/bengaluru-resilience-ai)** | Spatial flood, AQI, and gridlock resilience forecasting | **94.2% spatial precision**, **<42ms** alert latency | FastAPI, Next.js 15, MapLibre, Docker |
| **[CareerMatch AI](https://github.com/thrilokmanjunath/career-match-ai)** | Hybrid dense-semantic vector retrieval & skill-gap graph | **NDCG@10 = 0.6136** (vs. 0.0614 Keyword Jaccard) | FAISS, MiniLM, spaCy, Streamlit |
| **[E-Commerce Churn](https://github.com/thrilokmanjunath/ecommerce-churn-analysis)** | Leak-free customer churn prediction & TreeSHAP analytics | **98.05% Acc, 90.53% Recall, 0.9979 ROC-AUC** | Scikit-learn Pipeline, XGBoost, Streamlit |
| **[ToothCare](https://github.com/thrilokmanjunath/ToothCare)** | 3D Dental digital twin & clinical NLP treatment planner | **60-120 FPS** PBR, **<8.5ms** local NLP | Swift 5.9, SwiftUI, SceneKit, USDZ |
| **[Nexus-One](https://github.com/thrilokmanjunath/Nexus-One)** | Unified enterprise multi-agent & ML orchestration platform | **Multi-provider failover**, **<120ms** routing | Next.js, FastAPI, LiteLLM, Docker |
| **[RepoBase](https://github.com/thrilokmanjunath/RepoBase)** | Developer command-palette repository workspace SPA | **<14ms API p95**, **0 KB JS framework bloat** | Django 5, Django Ninja, Vanilla ES6+ |

---

## 🌟 Featured Projects

### 🧠 [Synthetic Silence 2.0](https://github.com/thrilokmanjunath/SyntheticSilence2.0)
*Evaluating Claim-Space Density for Evidence Insufficiency Under Construction and Reference-Manifold Shift.*  
An empirical investigation proving that representation-space density does not provide a robust, construction-invariant signal for hallucination detection across real-world claim manifolds.
- **Empirical Findings**: Evaluated on frozen benchmarks (FEVER synthetic vs. AVeriTeC real). On synthetic claims, kNN density achieves **AUROC = 0.5463** (95% CI `[0.5366, 0.5564]`, prevalence baseline `0.2403`). On real-world claims lacking evidence, density drops to **AUROC = 0.2754**, establishing a severe **signal inversion** where unverified claims cluster closer to encyclopedic reference embeddings than verified facts.
- **Reproducibility**: Single-command deterministic reproduction via `python scripts/reproduce_benchmark.py`.
- **Interactive UI**: Streamlit research demo with conformal uncertainty indicators and separation of model heuristic vs. ground truth.  
`Python` `PyTorch` `AI Safety` `Conformal Prediction` `Bootstrap CIs` `LLMs`

---

### 🛒 [E-Commerce Churn Analysis](https://github.com/thrilokmanjunath/ecommerce-churn-analysis) · [Live Dashboard ↗](https://thrilokmanjunath.github.io/ecommerce-churn-analysis/)
*Leak-Free Predictive Retention Pipeline & Explainable Risk Factor Analytics.*  
A scientifically grounded customer retention platform built on 5,630 customer profiles (Kaggle CC0).
- **Leak-Free ML Pipeline**: Implemented with `sklearn.pipeline.Pipeline` and `ColumnTransformer` fitted strictly post-split, preventing preprocessing leakage.
- **Model Performance**: Outperforms the 83.16% majority baseline with **98.05% Accuracy**, **90.53% Recall**, **93.99% F1**, and **0.9979 ROC-AUC** (XGBoost).
- **Behavioral Insights**: Empirically verified that customer complaints exhibit a **2.90× relative risk** of churn (31.67% churn rate with complaints vs. 10.93% without; Odds Ratio = 3.75).
- **Interpretability**: TreeSHAP feature attribution identifying tenure, complaints, and device count as primary drivers. Includes an interactive Streamlit what-if simulator.  
`Python` `Scikit-learn` `XGBoost` `SHAP` `Streamlit` `Pandas`

---

### 🐯 [Eyes on Tigers](https://github.com/thrilokmanjunath/Eyes-on-Tigers) · [Live Demo ↗](https://eyes-on-tigers-7mtepkv8ruq3aaulgr7ves.streamlit.app)
*AI-Powered Conservation Analytics & Anti-Poaching Telemetry.*  
Synthesizes Computer Vision, Google Earth Engine satellite telemetry, and spatial ML to evaluate Project Tiger reserves and compute the Tiger Success Index (TSI).
- **Computer Vision**: YOLOv8 camera-trap detection achieving **mAP@0.5 = 0.842** (Precision: 88.6%, Recall: 81.4%, 64ms CPU latency).
- **Telemetry & Hardened Paths**: Automated GeoJSON reserve boundaries and multi-layer GIS analytics.
- **Scientific Transparency**: Explicit high-visibility banners labeling synthetic patrol tracks to distinguish simulation demonstrations from tactical operations.  
`Python` `PyTorch` `YOLOv8` `Google Earth Engine` `Streamlit` `GeoPandas`

---

### 📚 [PaperMate AI (PaperGraph)](https://github.com/thrilokmanjunath/PaperGraph) · [Live Demo ↗](https://paper-graph-wine.vercel.app)
*Enterprise Research Intelligence Platform & Citation Knowledge Graph.*  
Transforms academic literature into dynamic citation graphs, discovers seminal works via graph centrality, and generates grounded literature reviews.
- **Interactive SVG Engine**: Client-side knowledge graph supporting pan, zoom, directed citation edges, and node selection with expandable metadata drawers.
- **High-Throughput Architecture**: Built with Java 17/21 Virtual Threads (Project Loom) and Spring Boot 3; verified via automated load test harness (`scripts/load_test.py`) auditing the **3,450 req/sec** throughput and **18.4ms p95** latency under high-concurrency keep-alive conditions and pre-warmed Redis cache buffers.
- **Modern Full-Stack**: Next.js 16 (React 19) frontend with dynamic search across topics, authors, and DOIs.  
`Java 17/21 (Loom)` `Spring Boot 3` `Next.js 16` `PostgreSQL` `Redis` `Knowledge Graphs`

---

### 🎯 [CareerMatch AI](https://github.com/thrilokmanjunath/career-match-ai)
*Two-Stage Hybrid Job Retrieval & Deterministic Skill-Gap Ontology Engine.*  
Replaces opaque keyword-matching Applicant Tracking Systems (ATS) with a multi-signal retrieval framework.
- **Empirical IR Benchmark**: Evaluated 5 retrieval architectures across 50 candidate profiles and 1,000 real job postings (`evaluation/run_benchmark.py`). Dense embeddings achieve **NDCG@10 = 0.6136** (vs. 0.0614 for naive keyword Jaccard and 0.5951 for BM25).
- **Skill-Gap Explainability**: CareerMatch Hybrid pairs dense semantic retrieval with explicit JSON ontology set-theoretic analysis to isolate exact missing prerequisites and generate actionable upskilling recommendations.
- **Transparent Methodology**: Ground truth relevance is explicitly disclosed as synthetic/proxy domain rules rather than subjective human hiring decisions.
- **Interactive Demo**: Streamlit app supporting resume PDF upload, text pasting, and 1-click candidate personas.  
`Python` `Sentence-Transformers` `FAISS` `spaCy` `Streamlit` `Scikit-learn` `BM25`

---

### 🌌 [TerraScope](https://github.com/thrilokmanjunath/TerraScope) · [Live Demo ↗](https://terrascope-three.vercel.app)
*A living digital twin of Earth and the cosmos. Real physics, real satellite telemetry, no fake numbers.*  
Renders 18,000 real SDSS DR17 galaxies in 3D, exact general-relativity Schwarzschild black hole gravitational lensing matching Event Horizon Telescope shadows, real pulsar audio synthesis at true spin periods, and real orbital mechanics.  
`TypeScript` `Next.js` `Three.js` `WebGL Shaders` `Orbital Mechanics` `Astrophysics`

---

### ⚡ [EV Battery Quantum](https://github.com/thrilokmanjunath/EV_Battery_Quantum)
*Hybrid Quantum-Classical ML framework for multi-objective EV battery pack design optimisation.*  
Uses QAOA for Pareto-optimal structural configurations and QKSVM for predictive electro-thermal performance modelling. Features Celery task workers, Redis caching, WebSocket streaming, and Prometheus telemetry.  
`Python` `QAOA` `QKSVM` `Qiskit` `FastAPI` `Celery` `Redis` `Docker` `Prometheus`

---

### 🦷 [ToothCare](https://github.com/thrilokmanjunath/ToothCare)
*3D Dental Digital Twin & AI Treatment Planner built with SwiftUI and SceneKit.*  
Translates unstructured clinical natural language dictation into localized 3D disease markers with physically-based rendering (PBR), automated procedural treatment synthesis, and HIPAA-compliant on-device processing (<8.5ms latency).  
`Swift 5.9` `SwiftUI` `SceneKit` `USDZ` `NLP` `iOS 17+`

---

### 🏙️ [BLR Resilience AI](https://github.com/thrilokmanjunath/bengaluru-resilience-ai)
*Real-time urban resilience intelligence platform for Bengaluru.*  
Multi-hazard spatial forecasting across flood risk, stormwater surge, AQI, and traffic gridlock across 198+ BBMP wards with conformal confidence bounds.  
`FastAPI` `Next.js 15` `MapLibre GL` `Spatial ML` `Docker`

---

### 🚀 [Nexus-One](https://github.com/thrilokmanjunath/Nexus-One)
*Unified full-stack AI platform for Data Science, ML, GenAI, and Multi-Agent Orchestration.*  
Next.js frontend, FastAPI backend, LiteLLM multi-provider intelligent routing, and Docker microservices.  
`Next.js` `FastAPI` `Python` `TypeScript` `LiteLLM` `Docker` `MLOps`

---

### 🗄️ [RepoBase](https://github.com/thrilokmanjunath/RepoBase) · [Live Demo ↗](https://repo-base-iota.vercel.app)
*Premium developer workspace SPA for repository management.*  
Features a Command Palette (⌘K), deterministic visual cryptographic color identities, and high-performance asynchronous Django Ninja backend.  
`Python` `Django 5` `Django Ninja` `Vanilla JavaScript` `PostgreSQL` `SPA`

---

## 📈 Data Science Portfolio & Analytical Studies

| Project | Focus | Key Outcome / Benchmark | Dataset |
|---|---|---|---|
| [E-commerce Churn Analysis](https://github.com/thrilokmanjunath/ecommerce-churn-analysis) | Leak-free retention modeling | **98.05% Acc, 90.53% Recall, 0.9979 ROC-AUC** (Complaints: 2.90× Risk) | 5,630 customer profiles (CC0) |
| [Karnataka Universities EDA](https://github.com/thrilokmanjunath/karnataka-universities-data-analysis) | Higher education landscape analysis | Comprehensive institutional distribution report | 100+ Karnataka universities |
| [Twitter Sentiment Analysis](https://github.com/thrilokmanjunath/PRODIGY_DS_04) | NLP, TextBlob polarity scoring | Polarity & subjectivity distribution mapping | twitter_training.csv |
| [US Traffic Accidents EDA](https://github.com/thrilokmanjunath/PRODIGY_DS_05) | Temporal & geographic pattern analysis | Weather & severity correlation analysis | US Accidents dataset |
| [Titanic EDA](https://github.com/thrilokmanjunath/PRODIGY_DS_02) | Survival analysis, demographic correlations | Interaction & family-size survival dynamics | Titanic dataset |
| [Bank Marketing Classifier](https://github.com/thrilokmanjunath/PRODIGY_DS_03) | Decision Tree classification | Cost-sensitive term-deposit conversion prediction | Bank marketing dataset |
| [Karnataka Crime Data](https://github.com/thrilokmanjunath/KarnatakaGovData) | Government data analysis | Spatial district-level crime variance analysis | Karnataka Govt open data |

---

## 🛠️ Technology Stack & Tooling

- **Languages:** Python (Core), Java 17/21, TypeScript, Swift 5.9, JavaScript (ES6+), SQL, C/C++
- **Machine Learning & Deep Learning:** PyTorch, scikit-learn, XGBoost, FAISS, Sentence-Transformers, spaCy, NumPy, Pandas
- **AI & Generative AI:** LiteLLM, Multi-Agent Systems, Sparse Autoencoders, Topological Data Analysis (TDA), Conformal Prediction
- **Backend & Cloud Services:** FastAPI, Spring Boot 3 (Project Loom), Django Ninja, Celery, Redis, PostgreSQL
- **Frontend & Spatial/3D UI:** Next.js 16, React 19, Tailwind CSS, Three.js, SceneKit (USDZ), MapLibre GL
- **Quantum Computing:** Qiskit, QAOA, QKSVM (NISQ algorithms)
- **DevOps, MLOps & Telemetry:** Docker, Docker Compose, GitHub Actions, Prometheus, Vercel

---

## 🌐 Live Deployments

| Platform | Production URL | Core Stack |
|---|---|---|
| **Portfolio** | [thrilok-portfolio-ruby.vercel.app](https://thrilok-portfolio-ruby.vercel.app) | Next.js · TypeScript · Tailwind |
| **TerraScope** | [terrascope-three.vercel.app](https://terrascope-three.vercel.app) | Next.js · Three.js · Astrophysics Engine |
| **PaperMate AI** | [paper-graph-wine.vercel.app](https://paper-graph-wine.vercel.app) | Next.js 16 · Spring Boot 3 · Redis |
| **Eyes on Tigers** | [eyes-on-tigers-7mtepkv8ruq3aaulgr7ves.streamlit.app](https://eyes-on-tigers-7mtepkv8ruq3aaulgr7ves.streamlit.app) | Streamlit · PyTorch · GEE |
| **RepoBase** | [repo-base-iota.vercel.app](https://repo-base-iota.vercel.app) | Django 5 · Django Ninja · Vanilla JS |
| **E-Commerce Churn**| [thrilokmanjunath.github.io/ecommerce-churn-analysis](https://thrilokmanjunath.github.io/ecommerce-churn-analysis/) | Streamlit · Scikit-learn · XGBoost |

---

<div align="center">

**[GitHub Profile](https://github.com/thrilokmanjunath)** · **[LinkedIn](https://in.linkedin.com/in/thrilokmanjunath)** · **[Portfolio](https://thrilok-portfolio-ruby.vercel.app)** · **[Email](mailto:thrilokmanjunath@gmail.com)**

*Bengaluru, Karnataka, India*

</div>
