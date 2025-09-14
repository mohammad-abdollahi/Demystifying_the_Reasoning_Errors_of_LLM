# ExecBench

This folder contains the benchmark datasets used in the paper  
**“Demystifying the Reasoning Errors of LLMs: An Empirical Study on Code Execution Inference.”**

## 📖 Overview
ExecBench is a curated benchmark designed to evaluate **code execution inference** of reasoning LLMs.  
It combines tasks from two widely adopted code-generation benchmarks:

* **[HumanEval+](https://huggingface.co/datasets/evalplus/humanevalplus)** – all available tasks are included.
* **[LiveCodeBench](https://huggingface.co/datasets/livecodebench/execution-v2)** – only tasks labeled as *medium* or *hard* are selected.

Each task is paired with:
* **Reference implementation** – ground-truth Python program.
* **Input sets** – regular, edge, and invalid inputs.
* **Expected execution results** – used to verify model reasoning.

---

## 📊 Dataset Statistics

| Dataset        | # Tasks | Avg. Lines of Code (LOC) | Avg. Cyclomatic Complexity (CC) | Avg. Halstead Difficulty (HM) |
|-----------------|-------:|------------------------:|---------------------------------:|------------------------------:|
| **HumanEval+**  |   164  | 8                       | 3.1                              | 2.2                           |
| **LiveCodeBench** | 263  | 12                      | 5                                | 3                              |

* **LOC** – average number of source lines per task.  
* **CC** – Cyclomatic Complexity, reflecting the number of independent execution paths.  
* **HM** – Halstead Difficulty, a measure of cognitive complexity.

These metrics confirm that **LiveCodeBench contains the more challenging programs**, while HumanEval+ consists of less complex tasks.

---

## 📁 Files

* `ExecBench.json` – combined benchmark of both datasets.  
* `HumanEval_regular_inputs.json` / `HumanEval_edge_inputs.json` / `HumanEval_invalid_inputs.json` – HumanEval+ tasks with different input types.  
* `Livecodebench_regular_inputs.json` / `Livecodebench_edge_inputs.json` / `Livecodebench_invalid_inputs.json` – LiveCodeBench tasks with different input types.

Each JSON file contains:
* The original task description and reference implementation,
* The curated input sets (regular, edge, and invalid),
* The ground-truth execution outputs.

---

## 📜 Citation
If you use ExecBench in your research, please cite:

```bibtex
@article{my-paper-2025,
  title={Demystifying the Reasoning Errors of LLMs: An Empirical Study on Code Execution Inference},
  author={Anonymous},
  journal={arXiv preprint arXiv:my-id},
  year={2025}
}
