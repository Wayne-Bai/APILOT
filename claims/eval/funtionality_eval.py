from argparse import ArgumentParser
import os
import json
import openai
import pandas as pd
import numpy as np

def read_csv(file_path):
    data = pd.read_csv(file_path)
    return data

# Specify the directory you want to traverse
# directory_path = '/data/Weiheng/LLM-TimeGap/LLM-TimeGap/LLM-api/result'

result_dict = {}

gpt_series = ['gpt-3.5-turbo-0125', 'gpt-4-turbo-2024-04-09', 'gpt-4o-mini-2024-07-18', 'gpt-4o-2024-08-06']
replicate_series = ['granite-8b-code-instruct-128k', 'granite-20b-code-instruct-8k', 'granite-3.0-2b-instruct', 'granite-3.0-8b-instruct', 'codellama-34b-instruct', 'codellama-7b-instruct']
mistral_series = ['ministral-3b-latest', 'ministral-8b-latest', 'codestral-latest', 'open-codestral-mamba']
huggingface_series = ['Llama-3.1-70B-Instruct', 'Llama-3.1-8B-Instruct']
deepseek_series = ['deepseek-coder']

model_list = gpt_series + replicate_series + mistral_series + huggingface_series + deepseek_series

result_dict = {}

for model in model_list:

    file_path = f"Functionality-Eval/FR-{model}_instr.csv"
    data = read_csv(file_path)

    filter_score_list = data[data['Category'] == 'Filter']['Score'].tolist()
    origin_score_list = data[data['Category'] == 'Origin']['Score'].tolist()

    filter_score = np.mean(filter_score_list)
    origin_score = np.mean(origin_score_list)

    result_dict[model] = {
        "Filter": filter_score,
        "Origin": origin_score
    }
    
    print(result_dict)

for key, item in result_dict.items():
    print(key)
for key, item in result_dict.items():
    print(item['Filter'])
    # print(item['Origin'])