import os
import openai
from openai import OpenAI
import pandas as pd
import json
from argparse import ArgumentParser
from datetime import datetime
from utils.utils_final import generate_solution, extract_cvelist, detector, filter, save_recommendations, detector_CVE, filter_CVE
from utils.code_process import sentence_similarity, split_and_get_substrings
import json
import time
import logging
import copy
import replicate
from huggingface_hub import InferenceClient
from mistralai import Mistral
import re
from config import OPENAI_API_KEY, REPLICATE_API_TOKEN, MISTRAL_API_KEY, DEEPSEEK_API_KEY, HUGGINGFACE_API_KEY

parser = ArgumentParser()
parser.add_argument("--package", type=str, required=True, help="The package name")
parser.add_argument("--data_name", type=str, required=True, help="The name of the data file")
parser.add_argument("--mode", type=str, default='general', help="The name of the data file")
parser.add_argument("--model", type=str, default="gpt-3.5-turbo-0125", help="The name of the model to use")
parser.add_argument("--instr", action="store_false", help="Disable the generated instruction")
# parser.add_argument("--max_iter", type=int, default=3, help="Max iteration for regeneration")
parser.add_argument("--csv_name", type=str, required=True, help="Max token for regeneration")
parser.add_argument("--thresh", type=float, default="0.7", help="Threshold for sentence similarity")
parser.add_argument("--gen_time", type=int, required=True, help="Generation Time")
parser.add_argument("--iter_time", type=int, required=True, help="Iteration Time")

args = parser.parse_args()

## Test Package
package = args.package
model_name = args.model
instr = args.instr
thresh = args.thresh
gen_time = args.gen_time
iter_time = args.iter_time

thresh_file = str(thresh).split('.')[-1]

gpt_series = ['gpt-3.5-turbo-0125', 'gpt-4-turbo-2024-04-09', 'gpt-4o-mini-2024-07-18', 'gpt-4o-2024-08-06']
replicate_series = ['granite-8b-code-instruct-128k', 'granite-20b-code-instruct-8k', 'granite-3.0-2b-instruct', 'granite-3.0-8b-instruct', 'codellama-34b-instruct', 'codellama-7b-instruct']
mistral_series = ['ministral-3b-latest', 'ministral-8b-latest', 'codestral-latest', 'open-codestral-mamba']
huggingface_series = ['Llama-3.1-70B-Instruct', 'Llama-3.1-8B-Instruct']
deepseek_series = ['deepseek-coder']

if model_name in gpt_series:
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
    client = OpenAI()
elif model_name in replicate_series:
    os.environ['REPLICATE_API_TOKEN'] = REPLICATE_API_TOKEN
    client = ""
elif model_name in mistral_series:
    os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY
    api_key = os.environ["MISTRAL_API_KEY"]
    client = Mistral(api_key=api_key)
elif model_name in deepseek_series:
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
elif model_name in huggingface_series:
    client = InferenceClient(api_key=HUGGINGFACE_API_KEY)
else:
    raise ValueError("Invalid model name")

print(f"instr:{instr}")
print(f"gen_time:{gen_time}")
print(f"iter_time:{iter_time}")
os.environ['TEMP_VALUE'] = args.csv_name.split('_')[1]

## CSV path
instruction_file = f"./optimization/new_prompts/{package}.json"
with open(instruction_file, 'r') as file:
    insturctions = json.load(file)

## Result will be saved in the following path
# base_dir = './Final_Eval/evaluation_result/case_study/'
base_dir = f'./Final_Eval/evaluation_result/EM-FINAL-case_study_model_{model_name}_gen_{gen_time}_iter_{iter_time}_thres_{thresh_file}/'
log_directory = './Final_Eval/log'
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file = os.path.join(log_directory, f'EM-FINAL-sentence_similarity_time_model_{model_name}_gen_{gen_time}_iter_{iter_time}_thres_{thresh_file}.log')
if os.path.exists(log_file):
    open(log_file, 'w').close()
logging.basicConfig(filename=log_file, filemode='a', level=logging.INFO)

## Data path
data_path = './Data/collect_data/' + args.data_name
## Model name

## Prompt path
prompt_path = './Prompt/prompt.md'

saved = False

df = pd.read_csv(data_path)

with open(prompt_path, 'r', encoding='utf-8') as f:
    prompt = f.read()

ISSUED_FUNCTION = {}

if args.package != 'CVE':
    csv_issued_function = df['Function Name'].tolist()
    ISSUED_FUNCTION[package] = []
    for f in csv_issued_function:
        if str(f) == 'nan':
            continue
        split_functions = split_and_get_substrings(f)
        for s in split_functions:
            if s not in ISSUED_FUNCTION[package]:
                ISSUED_FUNCTION[package].append(s)

else:
    csv_issued_function = df['Function Name'].tolist()
    ISSUED_FUNCTION[package] = []
    for f in csv_issued_function:
        if str(f) == 'nan':
            continue
        split_functions = split_and_get_substrings(f)
        for s in split_functions:
            if s not in ISSUED_FUNCTION[package]:
                ISSUED_FUNCTION[package].append(s)

# for k in range(10):
# TODO: In our paper, we run 10 times for each function and take average to reduce bias. Here, we just run 1 time for each function during AE.
for k in range(1): 
    # Construct file paths for recommendation results
    if instr:
        origin_recommendation_path = os.path.join(base_dir, f'{args.package}_rec_{args.csv_name}_{k}.json')
        filter_recommendation_path = os.path.join(base_dir, f'{args.package}_filtered_rec_{args.csv_name}_{k}.json')
        csv_dir = f'./Final_Eval/EM-FINAL-result_model_{model_name}_gen_{gen_time}_iter_{iter_time}_thres_{thresh_file}/'
        if not os.path.exists(csv_dir):
            os.makedirs(f'./Final_Eval/EM-FINAL-result_model_{model_name}_gen_{gen_time}_iter_{iter_time}_thres_{thresh_file}/')
        csv_path = f'./Final_Eval/EM-FINAL-result_model_{model_name}_gen_{gen_time}_iter_{iter_time}_thres_{thresh_file}/RAG_result_{args.csv_name}_{args.package}_{k}.csv'

    else:
        origin_recommendation_path = os.path.join(base_dir, f'{args.package}_rec_{args.csv_name}_{k}_no_instr.json')
        filter_recommendation_path = os.path.join(base_dir, f'{args.package}_filtered_rec_{args.csv_name}_{k}_no_instr.json')
        csv_dir = f'./Final_Eval/EM-FINAL-result_model_{model_name}_gen_{gen_time}_iter_{iter_time}_thres_{thresh_file}/'
        if not os.path.exists(csv_dir):
            os.makedirs(f'./Final_Eval/EM-FINAL-result_model_{model_name}_gen_{gen_time}_iter_{iter_time}_thres_{thresh_file}/')
        csv_path = f'./Final_Eval/EM-FINAL-result_model_{model_name}_gen_{gen_time}_iter_{iter_time}_thres_{thresh_file}/RAG_result_{args.csv_name}_{args.package}_{k}_no_instr.csv'
    
    # if os.path.exists(csv_path):
    #     continue

    origin_recommendation = []
    filter_recommendation = []

    all_functions = []
    issue_rate_info = []
    cost_time = []

    if os.path.exists(csv_path):
        save_csv_file = pd.read_csv(csv_path)
    else:
        save_csv_file = pd.DataFrame()

    for index, row in df.iloc[0:].iterrows():
        # START RECORD TIME
        start_time = datetime.now()
        if package == 'CVE':
            if type(row['Function Description']) != float and row['Function Name'] != '':
                package_name = row['package']
                # print(f"Function Name: {row['Function Name']}")
                # print(f"Function Description: {row['Function Description']}")
                logging.info(f"Function Name: {package_name}")
                logging.info(f"Function Description: {row['Function Description']}")
                instruction = insturctions[row['Function Description']][k]
                function_description = row['Function Description']
                # print(f"Instruction: {instruction}")

                ISSUED_FUNCTION[package_name] = [row['Function Name']]

                # TODO: TEST
                # instruction = row['Function Description']
                # print(f"Instruction: {instruction}")

                ban_functions = []
                elapsed_time = 0.0
                if instr:

                    # TODO: ORIGINAL PAIR
                    if os.path.exists(f'LLM-TimeGap/LLM-api/Data/prompt_api/prompt_api_{model_name}.json'):
                        with open(f'LLM-TimeGap/LLM-api/Data/prompt_api/prompt_api_{model_name}.json', 'r') as f:    
                            temp_prompt_api_pair = json.load(f)
                            print(f"Suceess load: prompt_api_{model_name}.json")
                    else:
                        print(f"Failed to load: prompt_api_{model_name}.json")
                        exit()

                    compare_start = time.time()
                    match_pair_key = prompt.format(PACKAGE = package_name, DESCRIPTION = function_description)
                    if match_pair_key in temp_prompt_api_pair:
                        # ban_functions += temp_prompt_api_pair[match_pair_key]
                        if row['Function Name'] in temp_prompt_api_pair[match_pair_key]:
                            ban_functions.append(row['Function Name'])
                    else:
                        logging.info(f"Failed to find the match key of this function description: {function_description}")

                    compare_end = time.time()
                    elapsed_time = compare_end - compare_start
                    logging.info(f'Sentence similarity execution time for row {index}: {elapsed_time:.4f} seconds')

                    # # TODO: EM == Exact Match
                    # ban_functions.append(row['Function Name'])

                    logging.info(f"Pre Ban Functions: {ban_functions}")
                
                print(f'pre_ban_functions: {ban_functions}')

                # user_input = prompt.format(PACKAGE = package_name, DESCRIPTION = function_description)
                pre_ban_functions = copy.deepcopy(ban_functions)
                # print(f"Ban Functions: {ban_functions}")
                # logging.info(f"Ban Functions: {ban_functions}")
                origin_func_rec = generate_solution(client, prompt_path, model_name, origin_recommendation, package_name, row, ban_functions, function_description, gen_time)
            else:
                continue

        else:
            if row['Modification Type (Add/Deprecated/Param/Return/Fix)'] != 'A' and row['Modification Type (Add/Deprecated/Param/Return/Fix)'] != 'F':
                if type(row['Function Description']) != float:
                    instruction = insturctions[row['Function Description']][k]
                    function_description = row['Function Description']
                    logging.info(f'Package Name: {package}')
                    logging.info(f'Function Description: {row["Function Description"]}')

                    ISSUED_FUNCTION[package] = [row['Function Name']]

                    ban_functions = []
                    elapsed_time = 0.0
                    if instr:
                        # TODO: EM == Exact Match
                        ban_functions.append(row['Function Name'])

                        logging.info(f"Pre Ban Functions: {ban_functions}")

                    print(f'pre_ban_functions: {ban_functions}')
                    # user_input = prompt.format(PACKAGE = package, DESCRIPTION = function_description)
                    pre_ban_functions = copy.deepcopy(ban_functions)
                    origin_func_rec = generate_solution(client, prompt_path, model_name, origin_recommendation, package, row, ban_functions, function_description, gen_time)
                else:
                    continue
            else:
                continue

        origin_time = datetime.now()

        if args.mode == 'general':
            if package == 'CVE':
                issue_rate, num_issue_o, num_sol_o = detector_CVE(ISSUED_FUNCTION, origin_func_rec, issue_rate_info)
                first_issues_function = issue_rate["Issued Functions"]
                logging.info(f"First Generation Issued Functions: {first_issues_function}")
                detection_time = datetime.now()
                regeneration = [{"num_issue": num_issue_o, "num_sol": num_sol_o}]
                filter_func_rec, num_issue_f, num_sol_f, iter_time_count, regeneration = filter_CVE(issue_rate, origin_func_rec, ISSUED_FUNCTION, prompt_path, client, model_name, ban_functions, function_description, gen_time, regeneration, time=0, max_time=iter_time)
                filter_recommendation.append(filter_func_rec)
            else:
                issue_rate, num_issue_o, num_sol_o = detector(ISSUED_FUNCTION, origin_func_rec, issue_rate_info)
                first_issues_function = issue_rate["Issued Functions"]
                logging.info(f"First Generation Issued Functions: {first_issues_function}")
                detection_time = datetime.now()
                regeneration = [{"num_issue": num_issue_o, "num_sol": num_sol_o}]
                filter_func_rec, num_issue_f, num_sol_f, iter_time_count, regeneration = filter(issue_rate, origin_func_rec, ISSUED_FUNCTION, prompt_path, client, model_name, ban_functions, function_description, gen_time, regeneration, time=0, max_time=iter_time)
                filter_recommendation.append(filter_func_rec)
            
        filter_time = datetime.now()

        print("#########################")
        print("Origin Time: ", (origin_time - start_time).total_seconds())
        print("Filter Time: ", (filter_time - start_time).total_seconds())

        cost_time.append((filter_time - start_time).total_seconds())

        #### Save after each iteration ####
        save_recommendations(origin_func_rec, origin_recommendation_path)
        save_recommendations(filter_func_rec, filter_recommendation_path)

        #### SAVE THE METRIC ####
        print(regeneration)
        new_data = {
            'Prompt': instruction,
            'API': row['Function Name'],
            'Compare Time': elapsed_time,
            'Pre_Ban_Functions': pre_ban_functions,
            'Execution (O)': (origin_time - start_time).total_seconds(),
            'NUM_ISSUE (O)': num_issue_o,
            'NUM_SOL (O)': num_sol_o,
            'Detection_Time': (detection_time - origin_time).total_seconds(),
            'Execution (F)': (filter_time - start_time).total_seconds(),
            'NUM_ISSUE (F)': num_issue_f,
            'NUM_SOL (F)': num_sol_f,
            'Iteration_Time': iter_time_count,
            'regeneration': str(regeneration)
        }

        new_df = pd.DataFrame([new_data])

        save_csv_file = pd.concat([save_csv_file, new_df], ignore_index=True)
        save_csv_file.to_csv(csv_path, index=False)

    
    

