# APILOT: Official Implementation

Official code and evaluation framework for the paper: **[APILOT: Improving the Security and Usability of LLM Code Suggestions via Outdated API Mitigation](https://arxiv.org/pdf/2409.16526)**.
Weiheng Bai, Keyang Xuan, Pengxiang Huang, Qiushi Wu, Jianing Wen, Jingjing Wu, Kangjie Lu
*Annual Computer Security Applications Conference (ACSAC), 2025.* DOI: 10.1109/ACSAC67867.2025.00094
Preprint: arXiv:2409.16526 (September 2024)

## About

Large language models are trained on static snapshots of code and therefore keep
recommending APIs that have since been deprecated, patched for security reasons, or
changed in behavior. APILOT is a generation-time defense: it maintains a continuously
updated dataset of outdated APIs, predicts which requests are at risk, screens and
re-ranks candidate outputs, and re-queries the model when the screened result is
unsatisfactory.

**Results (ACSAC 2025).** Evaluated across seventeen open-source and commercial
language models, APILOT reduces outdated-API recommendations by 75% on average and
by up to 100% for some models, while improving the usability of the generated code
by 37% on average and without degrading functionality.

## Repository Structure

*   `artifacts/`: Contains the core implementation and evaluation framework for the APILOT system. The main experiment script is `experiment.sh`.
    *   TIPS: It may cause several thousand dollars to reproduce the experiment. To provie the Reproducibility and Functionality, please try the demo script as belw.
*   `artifacts/main.py`: Contains the main script to run the experiment. To run the demo experiment, use the following code. 
    *   ```--package``` to denote which package you want to inverstigate into.
    *   ```--csv_name``` to denote the temperature of the model.
    *   ```--data_name``` to denote the outdated APIs。
    *   ```--model``` to denote the model you want to investigate.
    *   ```--gen_time``` to denote the potential candidates we let LLM generate per run.
    *   ```--iter_time``` to denote the iteration time of regenerating with ban list.
    *   ```--thres``` to denote the similarity threshold for predicting related outdated API before input the user's prompt to LLM.
    *   ```--instr``` to decide whether we use prediction for related outdated API based on user input. The default value is ```True```, if you use this parameter, it means that we do not use prediction.

    ```
    cd artifacts
    python3.10 main.py --package "networkx" --csv_name "temp_1" --data_name "CaseStudy_networkx.csv" --model "gpt-4o-mini-2024-07-18" --gen_time 1 --iter_time 1 --thres 7 --instr
    ```
    * Result will be saved in ```Final_Eval``` Folder.
*   `artifacts/optimization/new_prompts`: Includes the prompts that mimics user input.
*   ```claims/analyze_result```: Perform the statical analysis on the output result by ```artifacts/main.py```.
*   ```claims/eval```: Includes the evaluation scripts for Functionality (`functionality_eval.py`) and Usability (`usability_calculated.py`). 

## Dependencies

This project requires Python 3.10 or higher. You can install the necessary packages using pip:

```bash
pip install pandas openai replicate mistralai huggingface_hub h5py
```

## Setup

Before running any experiments, you need to download the necessary data and configure your API keys.

1.  **Configure API Keys:** Navigate to `LLM-api/config.py` and replace the placeholder values with your actual API keys.

## Reproducing the Experiments

The main script to run the full suite of experiments and evaluate the APILOT system is `artifacts/experiment.sh`. This script will iterate through a predefined list of models and packages.
