import json

def load_json(file):
    with open(file, 'r') as f:
        return json.load(f)

gpt_series = ['gpt-3.5-turbo-0125', 'gpt-4-turbo-2024-04-09', 'gpt-4o-mini-2024-07-18', 'gpt-4o-2024-08-06']
replicate_series = ['granite-8b-code-instruct-128k', 'granite-20b-code-instruct-8k', 'granite-3.0-2b-instruct', 'granite-3.0-8b-instruct', 'codellama-34b-instruct', 'codellama-7b-instruct']
mistral_series = ['ministral-3b-latest', 'ministral-8b-latest', 'codestral-latest', 'open-codestral-mamba']
huggingface_series = ['Llama-3.1-70B-Instruct', 'Llama-3.1-8B-Instruct']
deepseek_series = ['deepseek-coder']

model_list = gpt_series + replicate_series + mistral_series + huggingface_series + deepseek_series

# model_list = ['gpt-3.5-turbo-0125']

result_dict = {}  

for model in model_list:
    file_path = f'./Usability-Eval/Result/usabilityUR-{model}.json'
    data = load_json(file_path)
    
    latest_origin_UR = []
    latest_filter_UR = []
    nearest_origin_UR = []
    nearest_filter_UR = []

    for key, value in data.items():
        latest_origin_UR.append(value['latest_version_rate']['origin'])
        if value['latest_version_rate']['filter'] != 0:
            latest_filter_UR.append(value['latest_version_rate']['filter'])
        
        nearest_origin_UR.append(value['nearest_version_rate']['origin'])
        if value['nearest_version_rate']['filter'] != 0:
            nearest_filter_UR.append(value['nearest_version_rate']['filter'])

    result_dict[model] = {'latest_origin_UR': sum(latest_origin_UR)/len(latest_origin_UR),
                          'latest_filter_UR': sum(latest_filter_UR)/len(latest_filter_UR),
                          'nearest_origin_UR': sum(nearest_origin_UR)/len(nearest_origin_UR),
                          'nearest_filter_UR': sum(nearest_filter_UR)/len(nearest_filter_UR)}
for key, value in result_dict.items():
    print(key)
for key, value in result_dict.items():
    # print(value['latest_origin_UR'])
    # print(value['latest_filter_UR'])
    # print(value['nearest_origin_UR'])
    print(value['nearest_filter_UR'])