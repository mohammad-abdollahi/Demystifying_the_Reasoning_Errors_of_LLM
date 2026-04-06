# ExecBench

This folder contains the benchmark datasets used in the paper  
**“Demystifying the Reasoning Errors of LLMs: An Empirical Study on Code Execution Inference.”**

## 📖 Overview
ExecBench is a curated benchmark designed to evaluate **code execution inference** of reasoning LLMs.  
It combines tasks from three widely adopted benchmarks:

* **[HumanEval+](https://huggingface.co/datasets/evalplus/humanevalplus)** – all available tasks are included.
* **[LiveCodeBench](https://huggingface.co/datasets/livecodebench/execution-v2)** – only tasks labeled as *medium* or *hard* are selected.
* **[RepoExec](https://repoexec.github.io/)** – a repository-level executable benchmark; we selected the **50 hardest samples** for our analysis.

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
| **RepoExec (50 hardest)** | 50 | 152                     | 8.6                              | 16                            |

* **LOC** – average number of source lines per task.  
* **CC** – Cyclomatic Complexity, reflecting the number of independent execution paths.  
* **HM** – Halstead Difficulty, a measure of cognitive complexity.

These metrics confirm that **RepoExec is the most challenging benchmark in our study**, with substantially higher code size and complexity than LiveCodeBench and HumanEval+.

---

## 📁 Files

* `ExecBench.json` – combined benchmark of both datasets.  
* `HumanEval_regular_inputs.json` / `HumanEval_edge_inputs.json` / `HumanEval_invalid_inputs.json` – HumanEval+ tasks with different input types.  
* `Livecodebench_regular_inputs.json` / `Livecodebench_edge_inputs.json` / `Livecodebench_invalid_inputs.json` – LiveCodeBench tasks with different input types.
* `RepoExec_regular_inputs.json` / `RepoExec_edge_inputs.json` / `RepoExec_invalid_inputs.json` – RepoExec tasks with different input types.

Each JSON file contains:
* The original task description and reference implementation,
* The curated input sets (regular, edge, and invalid),
* The ground-truth execution outputs.

---

## 📜 Citation
If you use ExecBench in your research, please cite:

```bibtex
@article{abdollahi2025demystifyingerrorsllmreasoning,
      title={Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation}, 
      author={Mohammad Abdollahi and Khandaker Rifah Tasnia and Soumit Kanti Saha and Jinqiu Yang and Song Wang and Hadi Hemmati},
      year={2025},
      eprint={2512.00215},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2512.00215}, 
}
