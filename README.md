# Hybrid Resume Section Classification using Small Language Models

This repository implements a **hybrid resume section classification system** that combines deterministic rule-based logic with **locally hosted small language models (SLMs)** as a fallback.

The objective of this project is **not to maximize accuracy**, but to understand:
- how hybrid NLP systems behave under realistic constraints,
- how much impact SLM choice actually has,
- and where model errors originate in practice.

---

## Problem Statement

Given a single line extracted from a resume, classify it into **exactly one** of the following categories:

- Education  
- Skills  
- Experience  
- Projects  
- Other  

Instead of relying entirely on a language model, the system follows a **hybrid design**:

1. Apply deterministic, human-interpretable rules for clear cases  
2. Use a small language model **only when rules fail to classify the input**

This design mirrors how lightweight NLP systems are commonly built in production.

---

## System Architecture

Resume line
│
▼
Rule-based classifier
│
(no match)
▼
Small Language Model (Ollama)
│
▼
Final classification

---

## Small Language Models Evaluated

All models are executed **locally via Ollama**, using CPU only:

- `qwen2.5:1.5b`
- `llama3.2:1b`
- `gemma2:2b`
- `phi3:mini`

Each model was evaluated using:
- the **same dataset**
- the **same prompt**
- the **same hybrid fallback logic**

This ensures a fair, controlled comparison.

---

## Dataset

- 30 manually created resume lines
- Covers multiple institutions (Jadavpur University, IIT Delhi, IISER Pune, IISc Bangalore, AIIMS Kalyani)
- Includes both structured and ambiguous entries
- Labels assigned manually

The dataset is intentionally small to allow **transparent inspection and error analysis**.

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Install Ollama and pull required models

ollama pull qwen2.5:1.5b
ollama pull llama3.2:1b
ollama pull gemma2:2b
ollama pull phi3:mini

Ensure Ollama is running locally.

⸻

3. Run evaluation for a single model

python evaluate.py

This prints per-sample predictions and a summary of rule vs SLM usage.

⸻

4. Run comparative SLM evaluation

python compare_slms.py

This evaluates all models and prints a comparison table.

⸻

Results Summary

Model                 Overall  RuleAcc   SLMAcc  SLMUsed
qwen2.5:1.5b          0.57     0.60     0.50         10
llama3.2:1b           0.53     0.60     0.40         10
gemma2:2b             0.57     0.60     0.50         10
phi3:mini             0.57     0.60     0.50         10


⸻

Interpretation of Results

1. Rule-based logic dominates system behavior
	•	Rules handled ~67% of samples
	•	They are fast, interpretable, and cheap
	•	Errors arise primarily from keyword collisions

2. SLM choice has limited impact on overall accuracy
	•	All evaluated models fall within a narrow accuracy range
	•	Increasing model size does not significantly improve performance
	•	Most fallback cases are inherently ambiguous

3. “Other” is the hardest category
	•	Abstract statements (e.g., interests, workshops) lack strong lexical cues
	•	Both rules and SLMs struggle consistently

4. Architecture matters more than model size
	•	Hybrid system design dominates performance
	•	Model upgrades alone do not resolve task-level ambiguity

⸻

Why These Results Matter

This project highlights an important practical insight:

In lightweight NLP systems, task formulation and system design often matter more than choosing a larger model.

Small language models are well-suited as fallback components, but blindly increasing model size provides diminishing returns without improving task definition or labeling clarity.

⸻

Limitations
	•	Small dataset size
	•	Single prompt per model (no prompt tuning)
	•	No confidence calibration or latency measurement

This project should be viewed as a baseline and diagnostic study, not a production-ready classifier.

⸻

Possible Extensions
	•	Per-class accuracy analysis
	•	Confidence-based fallback thresholds
	•	Latency vs accuracy tradeoff study
	•	Error-driven rule refinement

⸻

Author

Sayanjib Sur
M.E. Information Technology
Learning and exploring Language Models & Agentic AI

