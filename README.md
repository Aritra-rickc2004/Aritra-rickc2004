<div align="center">

# Aritra Chowdhury

**Software Development & Applied AI Engineer**  
*Building resilient backend architectures, decoupled systems, and production-grade AI applications.*

Kolkata, West Bengal, India • [tchowdhury979@gmail.com](mailto:tchowdhury979@gmail.com) • [LinkedIn](https://linkedin.com/in/aritra-chowdhury-82201228b) • [LeetCode](https://leetcode.com/u/Aritra-RickC2004) • [GitHub](https://github.com/Aritra-rickc2004)

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/aritra-chowdhury-82201228b)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Aritra-rickc2004)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/u/Aritra-RickC2004)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:tchowdhury979@gmail.com)

</div>

---

## 📌 Executive Summary

Final-year **Computer Science and Engineering** undergraduate at the **Institute of Engineering & Management (IEM), Kolkata** (CGPA: **8.55/10**), targeting Software Development Engineer (SDE), Backend Engineering, and Applied AI/ML roles.

- **Defensive, Production-First Mindset**: Experienced in building end-to-end full-stack applications and event-driven backends. Strong emphasis on schema validation, typed API contracts (Zod/TypeScript), resilient fallback chains, and comprehensive test coverage (Vitest / Supertest).
- **Practical AI Systems & RAG**: Practical experience designing deterministic multi-agent state graphs (LangGraph), retrieval-augmented generation (FAISS), and background job orchestration (Inngest) with low-latency constraints.
- **Academic & Research Foundation**: Ex-**AI/ML Research Intern at IIT Patna** (PyTorch, hierarchical multi-label classification, hyperbolic embeddings; **88.57 Micro-F1** on WOS benchmark). Author of an agentic healthcare architecture presented at **ICDC 2026** (proceedings in progress with **Springer Nature**).

---

## 🛠️ Technical Competencies

| Domain | Technologies & Methodologies |
| :--- | :--- |
| **Languages** | C++, Python, TypeScript, SQL, C, JavaScript |
| **Backend & Systems** | Node.js, Express.js, RESTful APIs, Inngest (Durable Execution), Drizzle ORM, Event-Driven Architecture, Session Authentication (Argon2id) |
| **AI / Machine Learning** | LangChain, LangGraph (Multi-Agent Systems), PyTorch, FAISS Vector DB, Sentence-Transformers, Google Gemini API, RAG Pipelines |
| **Databases & Storage** | PostgreSQL, Supabase, MySQL, Firebase, MongoDB |
| **Testing & Tooling** | Vitest, Supertest, Git, GitHub, Postman, Linux/Bash, Vite, Streamlit |
| **Core Computer Science** | Data Structures & Algorithms, Object-Oriented Programming (OOP), DBMS, System Design Fundamentals |

---

## 🚀 Featured Engineering Projects

### 1. [Medi-AI-Agent](https://github.com/Aritra-rickc2004/Medi-AI-Agent) — Multi-Agent Clinical Coordination & Adherence System
*Autonomous healthcare framework orchestrating specialized agents for interaction detection and adherence monitoring.*
- **System Architecture**: Orchestrated a 3-agent hierarchy using **LangGraph** (*Monitor Agent* for deterministic safety checks, *Nurse Agent* for patient habit reminders, and *Medication Manager* for dosage resolution).
- **RAG & Knowledge Retrieval**: Integrated **top-$k$ FAISS vector retrieval** over clinical guideline knowledge bases, augmenting queries with patient-specific history (allergies, conditions, active schedules) to eliminate hallucinated advice.
- **Benchmarked Performance**: Validated across **100 patient profiles** (~15,000 schedule rows); achieved `<10ms` local monitor safety checks and `~2.5s` end-to-end multi-agent resolution.
- **Academic Publication**: Paper accepted and presented at the **4th ICDC 2026 Conference**; publication in **Springer Nature** proceedings currently in progress.
- **Stack**: `Python` • `LangGraph` • `LangChain` • `FAISS` • `Gemini 2.5 Flash` • `Streamlit` • `Pydantic`

---

### 2. [BugX](https://github.com/BlackClover-pvt/BugX) — Full-Stack AI Automated Code Review & Static Analysis Platform
*Production-grade static analysis platform analyzing source code across 17+ languages with multi-model fallback.*
- **Multi-Model Fallback Architecture**: Designed a cascading provider adapter (`Gemini 2.5 Flash` → `Flash-Lite` → `Flash-Latest`) validating all structured JSON outputs against strict **Zod** schemas, ensuring zero client parsing failures during upstream API timeouts.
- **Data Modeling & Analysis Engine**: Structured a **Drizzle ORM / PostgreSQL** schema capturing severity ratings (`CRITICAL` to `INFO`), impacted line ranges, root-cause analyses, and instant refactoring diffs.
- **Defensive Security & Auth**: Implemented stateful authentication using **Argon2id** password hashing, HTTP-only session cookies stored via `connect-pg-simple`, and tiered rate-limiting (`express-rate-limit`) against brute-force and token drainage attacks.
- **Testing & Quality Assurance**: Backed by a full test suite with **41/41 passing unit and integration tests** built using **Vitest** and **Supertest**.
- **Stack**: `TypeScript` • `React 19` • `Node.js` • `Express.js` • `Drizzle ORM` • `PostgreSQL` • `Vitest` • `Argon2id`

---

### 3. [Lysiq AI (Lycic AI)](https://github.com/Aritra-rickc2004/Lysiq-AI) — Autonomous Incident Triage & Specialist Routing Platform
*Event-driven incident management SaaS decoupling ticket submission from background AI classification.*
- **Decoupled Durable Pipeline**: Leveraged **Inngest durable step functions** to decouple HTTP ticket ingestion from downstream analysis, returning REST client acknowledgments in under **80ms**.
- **Resilient AI Classification**: Deployed `Gemini 3.5 Flash` to extract incident severity, tag categories, and suggested triage steps under an `AbortSignal.timeout(3500)` guard with an automated 4-domain heuristic fallback.
- **High-Throughput Specialist Matching**: Optimized routing queries using PostgreSQL **GIN-indexed array-overlap (`&&`)** operators to match required skill tags to active engineers in single-digit milliseconds, backed by a Super Admin failover queue.
- **Desktop-First DX**: Developed a keyboard-driven interface with an OS-aware `Ctrl+K` / `Cmd+K` command palette and centralized Axios request/response interceptors for global auth lifecycle handling.
- **Stack**: `TypeScript` • `React 18` • `Node.js` • `Express 5` • `Supabase (PostgreSQL)` • `Inngest` • `Gemini API`

---

## 💼 Research & Professional Experience

- **AI/ML Research Intern — Indian Institute of Technology (IIT Patna)** *(May 2026 – July 2026)*
  - Researched Hierarchical Multi-Label Text Classification (HMTC) in **PyTorch**, implementing structure-aware pruning to maintain label hierarchy consistency across document predictions.
  - Engineered parent-child routing mechanisms and hyperbolic message passing for label representation learning; evaluated across WOS, NYTimes, and RCV1-V2 benchmarks.
  - Achieved **88.57 Micro-F1** and **82.93 Macro-F1** on the Web of Science (WOS) benchmark dataset.

- **Paper Author & Presenter — 4th ICDC 2026 Conference** *(2026)*
  - Presented research paper on multi-agent clinical coordination systems; *Springer Nature* conference proceedings publication in progress.

- **Participant — IEEE CIS Summer School 2026** *(IIT Patna)*
  - Completed intensive coursework on the foundations, theoretical challenges, and applications of Large Language Models (LLMs) and Large Vision Models (LVMs).

---

## 🎯 Current Engineering Focus

- **Distributed Systems & Concurrency**: Deepening knowledge of low-latency message streaming, consensus algorithms, and relational database indexing internals.
- **Applied LLM Evaluation**: Investigating deterministic evaluation frameworks (hallucination detection, RAG retrieval recall, and latency trade-offs) for multi-agent workflows.
- **Algorithmic Problem Solving**: Consistently solving algorithmic problems on **[LeetCode](https://leetcode.com/u/Aritra-RickC2004)** focusing on dynamic programming, graph traversal, and system-level performance.

---

## 📊 GitHub & Engineering Activity

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Aritra-rickc2004&show_icons=true&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true" alt="Aritra's GitHub Stats" height="165" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Aritra-rickc2004&layout=compact&theme=github_dark&hide_border=true" alt="Top Languages" height="165" />

</div>

---

## 📬 Connect & Collaborate

I am actively seeking **Full-Time Software Development Engineer (SDE)**, **Backend Engineering**, and **Applied AI** opportunities starting upon graduation in 2027, as well as high-impact engineering internships.

- 💼 **LinkedIn**: [linkedin.com/in/aritra-chowdhury-82201228b](https://linkedin.com/in/aritra-chowdhury-82201228b)
- 💻 **LeetCode**: [leetcode.com/u/Aritra-RickC2004](https://leetcode.com/u/Aritra-RickC2004)
- 🐙 **GitHub**: [github.com/Aritra-rickc2004](https://github.com/Aritra-rickc2004)
- ✉️ **Email**: [tchowdhury979@gmail.com](mailto:tchowdhury979@gmail.com)

