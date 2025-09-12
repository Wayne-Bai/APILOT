import os
import pandas as pd

# Parameters
GEN_TIME = 1
ITER_TIME = 1
THRES = 7

gpt_series = ['gpt-3.5-turbo-0125', 'gpt-4-turbo-2024-04-09', 'gpt-4o-mini-2024-07-18', 'gpt-4o-2024-08-06']
replicate_series = ['granite-8b-code-instruct-128k', 'granite-20b-code-instruct-8k',
                    'granite-3.0-2b-instruct', 'granite-3.0-8b-instruct',
                    'codellama-34b-instruct', 'codellama-7b-instruct']
mistral_series = ['ministral-3b-latest', 'ministral-8b-latest', 'codestral-latest', 'open-codestral-mamba']
huggingface_series = ['Llama-3.1-70B-Instruct', 'Llama-3.1-8B-Instruct']
deepseek_series = ['deepseek-coder']
model_list = gpt_series + replicate_series + mistral_series + huggingface_series + deepseek_series

def list_csvs(directory):
    instr, no_instr = [], []
    for root, _, files in os.walk(directory):
        for f in files:
            if not f.endswith('.csv'):
                continue
            p = os.path.join(root, f)
            if f.endswith('_no_instr.csv'):
                no_instr.append(p)
            else:
                instr.append(p)
    return instr, no_instr

def safe_sum(series):
    return float(series.fillna(0).sum())

def metric_from_df(df):
    # Uses ALL rows; no filtering by Iteration_Time
    if 'NUM_ISSUE (O)' not in df.columns or 'NUM_ISSUE (F)' not in df.columns:
        return None
    o = safe_sum(df['NUM_ISSUE (O)'])
    f = safe_sum(df['NUM_ISSUE (F)'])
    return None if o == 0 else (o - f) / o

def read_csv(path):
    try:
        return pd.read_csv(path)
    except Exception:
        return None

def base_without_no_instr(path):
    # Remove trailing "_no_instr.csv" -> ".csv" counterpart
    if path.endswith('_no_instr.csv'):
        return path[:-len('_no_instr.csv')] + '.csv'
    return path

results_instr = {}
results_no_instr = {}

for model in model_list:
    directory = f'../artifacts/Final_Eval/EM-FINAL-result_model_{model}_gen_{GEN_TIME}_iter_{ITER_TIME}_thres_{THRES}'
    if not os.path.exists(directory):
        print(f'[Skip] {directory} not found')
        continue

    instr_files, no_instr_files = list_csvs(directory)

    # Sum over ALL instr files
    instr_o_sum = instr_f_sum = 0.0
    for p in instr_files:
        df = read_csv(p)
        if df is None or 'NUM_ISSUE (O)' not in df.columns or 'NUM_ISSUE (F)' not in df.columns:
            continue
        instr_o_sum += safe_sum(df['NUM_ISSUE (O)'])
        instr_f_sum += safe_sum(df['NUM_ISSUE (F)'])
    results_instr[model] = None if instr_o_sum == 0 else (instr_o_sum - instr_f_sum) / instr_o_sum

    # Sum over ALL no-instr files
    no_o_sum = no_f_sum = 0.0
    for p in no_instr_files:
        df = read_csv(p)
        if df is None or 'NUM_ISSUE (O)' not in df.columns or 'NUM_ISSUE (F)' not in df.columns:
            continue
        no_o_sum += safe_sum(df['NUM_ISSUE (O)'])
        no_f_sum += safe_sum(df['NUM_ISSUE (F)'])
    results_no_instr[model] = None if no_o_sum == 0 else (no_o_sum - no_f_sum) / no_o_sum

# ---- Output ----
def pretty(v): return 'NA' if v is None else f'{v:.5f}'

print('Model\tinstr_metric\tno_instr_metric')
for m in model_list:
    if m in results_instr or m in results_no_instr:
        print(f'{m}\t{pretty(results_instr.get(m))}\t{pretty(results_no_instr.get(m))}')

# Ranks (descending) for instr and no-instr (ignoring NA)
rank_instr = sorted([(m, v) for m, v in results_instr.items() if v is not None], key=lambda x: x[1], reverse=True)
rank_no = sorted([(m, v) for m, v in results_no_instr.items() if v is not None], key=lambda x: x[1], reverse=True)

print('\nRanking (instr):')
for i, (m, v) in enumerate(rank_instr, 1):
    print(f'Rank {i}: {m} -> {v:.5f}')

print('\nRanking (no_instr):')
for i, (m, v) in enumerate(rank_no, 1):
    print(f'Rank {i}: {m} -> {v:.5f}')
