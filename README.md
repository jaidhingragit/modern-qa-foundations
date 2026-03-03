# 🛠️ Modern QA Foundations

![AI QA Status](https://github.com/jaidhingraQA/modern-qa-foundations/actions/workflows/python-tests.yml/badge.svg)

This repository serves as my technical laboratory for **AI Quality Engineering**. It contains automated frameworks designed to validate the reliability of non-deterministic systems (LLMs).

## 🚀 Featured Project: Hallucination Checker
A Python-based evaluation utility that quantifies the accuracy of AI responses against a "Golden Dataset" (Ground Truth) using string similarity metrics.

### Key Features:
- **Jaccard Similarity Logic:** Calculates overlap between expected and actual AI outputs.
- **Data-Driven Testing:** Uses `test_cases.json` to manage various test scenarios.
- **CI/CD Integrated:** Automated testing via GitHub Actions on every push.

---

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Automation:** GitHub Actions
- **Format:** JSON-based data-driven architecture

## 🧪 How to Run
1. Clone the repo: `git clone https://github.com/jaidhingraQA/modern-qa-foundations.git`
2. Run the evaluator: `python hallucination_check.py`