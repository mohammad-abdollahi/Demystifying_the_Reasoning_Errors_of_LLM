# Demystifying the Reasoning Errors of LLMs: An Empirical Study on Code Execution Inference

## 📖 Overview

This repository accompanies the paper:

**Title:** *Demystifying the Reasoning Errors of LLMs: An Empirical Study on Code Execution Inference*  
**Authors:** Anonymous
**Year:** 2025  

Understanding a program’s runtime reasoning behavior, how intermediate states and control flows lead to final execution results, is crucial for reliable code generation, debugging, and automated reasoning. While LLMs have shown impressive output capabilities, prior studies often treat reasoning as a black box. Our work investigates the reasoning traces of state-of-the-art LLMs on code execution tasks, highlighting persistent errors and proposing a taxonomy of reasoning failure types.

## 📂 Repository Structure

.
├── Reasoning Collection
│ ├── HumanEval.ipynb # Run LLM inference and collect reasoning on HumanEval+
│ └── LiveCodeBench.ipynb # Run LLM inference and collect reasoning on LiveCodeBench
│
├── ExecBench
│ ├── ExecBench.json # Combined benchmark dataset
│ ├── HumanEval_regular_inputs.json # HumanEval+ regular inputs with ground-truth outputs
│ ├── HumanEval_edge_inputs.json # HumanEval+ edge inputs
│ ├── HumanEval_invalid_inputs.json # HumanEval+ invalid inputs
│ ├── Livecodebench_regular_inputs.json # LiveCodeBench regular inputs
│ ├── Livecodebench_edge_inputs.json # LiveCodeBench edge inputs
│ └── Livecodebench_invalid_inputs.json # LiveCodeBench invalid inputs
│
└── Annotated Reasoning Errors
├── HumanEval_Regular_Inputs_ReasoningErrors.csv # Trace- and statement-level error annotations (HumanEval+ regular)
├── HumanEval_Edge_Inputs_ReasoningErrors.csv # Error annotations (HumanEval+ edge)
├── LiveCodeBench_Regular_Inputs_ReasoningErrors.csv # Error annotations (LiveCodeBench regular)
├── LiveCodeBench_Edge_Inputs_ReasoningErrors.csv # Error annotations (LiveCodeBench edge)
└── LLM_Thinking_Errors_Analysis.xlsx # analysis of all reasoning errors saved in excel format


### Folder Highlights
* **Reasoning Collection** – Notebooks and prompts to run LLM inference and collect reasoning traces.  
* **ExecBench** – The curated benchmark datasets with regular, edge, and invalid inputs for HumanEval+ and LiveCodeBench.  
* **Annotated Reasoning Errors** – Complete results of the reasoning error analysis, including both trace-level and statement-level annotations.  


## ⚙️ Installation

### Prerequisites

* Python 3.8+
* API keys for data collection (optional)

### Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

**Core Dependencies:**

* `openai` – OpenAI API integration
* `tqdm` – Progress bars
* `python-dotenv` – Environment variable management

### Environment Setup

Create a `.env` file with your API keys:

```bash
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
CLAUDE_API_KEY=your_claude_key_here
FIREWORKS_API_KEY=your_fireworks_key_here
```

## 📊 Dataset and Benchmark

We curated a benchmark from two widely used datasets:

* **HumanEval+**
* **LiveCodeBench**

**Dataset Statistics:**

* 427 code snippets
* Each snippet evaluated with 12 input values
* Input types: Regular, Edge, Invalid
* Ground-truth execution outcomes provided

**Reasoning LLMs Evaluated:**

* DeepSeek-R1
* OpenAI o4-mini
* Gemini 2.5 Flash
* Claude 4 Sonnet

**Key Findings:**

* Accuracy on regular inputs: 95%
* Accuracy on edge-case inputs: 89%
* Accuracy on invalid inputs: 91%
* Performance drops sharply on complex snippets (nested logic, recursion, or implicit state changes)

## 🧩 Error Taxonomy

We analyzed reasoning errors made by LLMs and developed a **comprehensive error taxonomy**. The taxonomy comprises nine high-level categories, each with specific subcategories.

<img width="1260" height="720" alt="taxonomy" src="https://github.com/user-attachments/assets/7dd90d2b-467f-41e3-bc3e-1ec7517efe76" />

1. **Computation Errors**

   * Mathematical Operations Error
   * Conversion Error
   * Bitwise Errors
   * Counting / Length Errors
   * Numerical Value Representation Error
   * Special Values Arithmetic Error

2. **Indexing Errors**

   * Iteration Window Miscalculation
   * Loop Direction Mix-up

3. **Control Flow Errors**

   * Predicate Mischeck (if statement)
   * Predicate Mischeck (loop statement)

4. **Skipping Statements**

5. **Misreporting Final Output**

6. **Input Misread**

7. **Native API Misevaluation**

8. **Hallucination**

   * Numerical Value Hallucination
   * Hallucinated Runtime Error

9. **Lack of Fact Verification / Logic Following**

This taxonomy provides a structured framework to systematically classify reasoning failures in LLMs for code execution inference.


**Citation:**
```bibtex
@article{my-paper-2024,
  title={Demystifying the Reasoning Errors of LLMs: An Empirical Study on Code Execution Inference},
  author={Anonymous},
  journal={arXiv preprint arXiv:my-id},
  year={2025}
}
```

## 🤝 Contributing

We welcome contributions! Please:

1. 🍴 Fork the repository
2. 🌟 Create a feature branch
3. 📝 Make your changes
4. 🧪 Add tests
5. 📬 Submit a pull request

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
