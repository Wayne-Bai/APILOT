#!/usr/bin/env bash
set -euo pipefail

# === Tunables (edit these) =====================================================
# Similarity threshold(s). You can list multiple to sweep.
THRESHOLDS=(0.85)

# Generation/iteration budgets for the new pipeline.
GEN_TIME=1        # how many prompt variants to try per row
ITER_TIME=3       # how many filter/regenerate rounds per row

# Instructioning: in main.py, --instr uses action=store_false
#   => default = TRUE; passing --instr DISABLES instructioning.
# Set INSTR=1 to keep instructioning ON (default behavior).
# Set INSTR=0 to pass --instr and turn it OFF.
INSTR=1

# Path to your script (adjust if needed)
SCRIPT="main.py"
TEMP = "temp_1"
# ==============================================================================

# Models (same as before; add/remove as you like)
models=(
  'gpt-3.5-turbo-0125', 
  'gpt-4-turbo-2024-04-09', 
  'gpt-4o-mini-2024-07-18', 
  'gpt-4o-2024-08-06',
  'granite-8b-code-instruct-128k', 
  'granite-20b-code-instruct-8k', 
  'granite-3.0-2b-instruct', 
  'granite-3.0-8b-instruct', 
  'codellama-34b-instruct', 
  'codellama-7b-instruct',
  'ministral-3b-latest', 
  'ministral-8b-latest', 
  'codestral-latest', 
  'open-codestral-mamba',
  'Llama-3.1-70B-Instruct', 
  'Llama-3.1-8B-Instruct',
  'deepseek-coder'
)

# Packages and their corresponding CSVs (kept 1:1 with your original)
packages=("CVE" "Jinja2" "pandas" "scipy" "tensorflow" "nltk" "seaborn" "Flask" "networkx" "scikit-learn" "urllib3" "numpy" "werkzeug" "cryptography" "tornado" "Pillow" "torch")
data_files=("CaseStudy_CVE.csv" "CaseStudy_Jinja2.csv" "CaseStudy_pandas.csv" "CaseStudy_scipy.csv" "CaseStudy_tensorflow.csv" "CaseStudy_nltk.csv" "CaseStudy_seaborn.csv" "CaseStudy_Flask.csv" "CaseStudy_networkx.csv" "CaseStudy_scikit-learn.csv" "CaseStudy_urllib3.csv" "CaseStudy_numpy.csv" "CaseStudy_werkzeug.csv" "CaseStudy_cryptography.csv" "CaseStudy_tornado.csv" "CaseStudy_Pillow.csv" "CaseStudy_torch.csv")

# Build the instructioning flag for main.py
instr_flag=()
if [[ "${INSTR}" -eq 0 ]]; then
  # Passing --instr disables instructioning in main.py
  instr_flag+=(--instr)
fi

for model in "${models[@]}"; do
  for idx in "${!packages[@]}"; do
    package="${packages[$idx]}"
    data_name="${data_files[$idx]}"

    for thresh in "${THRESHOLDS[@]}"; do
      echo "Running: python ${SCRIPT} --package \"${package}\" --data_name \"${data_name}\" --model \"${model}\" ${instr_flag[*]:-} --thresh \"${thresh}\" --gen_time \"${GEN_TIME}\" --iter_time \"${ITER_TIME}\""
      python "${SCRIPT}" \
        --package "${package}" \
        --data_name "${data_name}" \
        --csv_name "${TEMP}" \
        --model "${model}" \
        "${instr_flag[@]}" \
        --thresh "${thresh}" \
        --gen_time "${GEN_TIME}" \
        --iter_time "${ITER_TIME}" \
        --instr
    done
  done
done
