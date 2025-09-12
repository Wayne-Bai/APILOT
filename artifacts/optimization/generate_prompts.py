import pandas as pd
import utils
import re
import json
import os

def extract_backtick_content(text):
    # Regular expression to match content inside triple backticks
    pattern = r'```(.*?)```'
    # Find all matches in the text
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

def load_csv(filename):
    data = pd.read_csv(filename)
    return data

def save_json(filename, data):
    directory = "LLM-TimeGap/optimization/new_prompts/"
    with open("{}/{}.json".format(directory, filename), 'w') as f:
        json.dump(data, f, indent=4)

def get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
            # Add the full file path to the list
                file_list.append(os.path.join(root, file))
    return file_list

directory = "LLM-TimeGap/optimization/collect_data/"
files = get_all_files(directory)

for file in files:

    package = file.split("/")[-1].split(".")[0].split("_")[-1]
    print("File: ", file)
    print("Package: ", package)
    

    data = load_csv(file)
    # print(data['Function Description'])

    prompt_dict = {}

    # TODO: 10 test cases
    # for i in range(10):
    #     function_description = data.iloc[i]['Function Description']
    #     prompt_dict[function_description] = []
    #     for j in range(10):
    #         prompt = utils.LLM(function_description)
    #         prompt_dict[function_description].append(extract_backtick_content(prompt)[0])

    print("Data shape: ", data.shape[0])
    print('-'*50)

    for i in range(data.shape[0]):
        function_description = data.iloc[i]['Function Description']
        if pd.isna(function_description):
            print("Function description is missing in row: ", i)
            continue

        prompt_dict[function_description] = []
        for j in range(10):
            prompt = utils.LLM(function_description)
            prompt_dict[function_description].append(extract_backtick_content(prompt)[0])

    save_json(package, prompt_dict)

