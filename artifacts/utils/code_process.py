import requests
import re
import json

API_URL = "https://j570qhf9j9ecadi9.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept" : "application/json",
    "Authorization": "YOUR HUGGINGFACE API KEY",
    "Content-Type": "application/json" 
}

def split_and_get_substrings(s):
    # Split the string by '.'
    parts = s.split('.')
    
    # Create a list of progressively smaller parts
    result = ['.'.join(parts[i:]) for i in range(len(parts))]
    
    return result

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def sentence_similarity(user_input:str, prefix_prompt:list, thereshold:float):
    output = query({
            "inputs": {
                "source_sentence": user_input,
                "sentences": prefix_prompt
            }
        })
    print(output)
    prefix_prompt_similar = []
      # print(output)
    for i in range(len(output['similarities'])):
        if output['similarities'][i] >= thereshold:
            prefix_prompt_similar.append(prefix_prompt[i])

    return prefix_prompt_similar


##### Blacklist Extractor #####
def extract_blacklist(blacklist_path, new_blacklist_path):
    ISSUED_FUNCTION = []
    try:
        with open(blacklist_path, 'r') as file:
            black_list = json.load(file)
    except FileNotFoundError:
        print("Blacklist file not found.")

    try:
        with open(new_blacklist_path, 'r') as file2:
            new_blacklist = json.load(file2)
    except FileNotFoundError:
        print("Original Blacklist file not found.")

    ### GET BLACKLIST ###
    for type, lists in black_list.items():
        if type != 'Added:':
            blacknames = [entry['func_name'] for entry in lists]
            ISSUED_FUNCTION += blacknames

    for f, lists in new_blacklist.items():
        for type, item in lists.items():
            if type != 'Added':
                for _, funct_info in item.items():
                    if f == 'Function':
                        if '.tests.' in funct_info['Call Chain'] :
                            pass
                        else:
                            function_name = funct_info['Function']
                            ISSUED_FUNCTION.append(function_name)
                    elif f == 'Class':
                        if funct_info['Method'].startswith('__'):
                            pass
                        if '.tests.' in funct_info['Class Chain'] :
                            pass
                        else:
                            function_name = funct_info['Method'] 

                            ISSUED_FUNCTION.append(function_name)

    return list(set(ISSUED_FUNCTION))

def post_process(recommendations):
    recommendations = recommendations.strip()
    if recommendations.count('```') == 1:
        pattern = r"```(.*?)"
        match = re.search(pattern, recommendations, re.DOTALL)
        if match:
            recommendations = match.group(1)
    elif recommendations.count('```') == 0 and (recommendations.startswith('import') or recommendations.startswith('\nimport') or recommendations.startswith('from') or recommendations.startswith('\nfrom')):
        if recommendations.endswith('<|endoftext|>'):
            recommendations = recommendations.strip('<|endoftext|>')
        else:   
            recommendations = recommendations 
    elif recommendations.startswith('```\n```python'):
        pattern4 = r"```\n```python\n(.*?)\n```"
        match = re.search(pattern4, recommendations, re.DOTALL)
        if match:
            recommendations = match.group(1)
        else:
            recommendations = recommendations.strip('```\n```python')
    elif recommendations.startswith('```python`'):
        pattern = r"```python`(.*?)```"
        match = re.search(pattern, recommendations, re.DOTALL)
        if match:
            recommendations = match.group(1)
    elif recommendations.startswith('```python```'):
        pattern = r"```python```(.*?)```"
        match = re.search(pattern, recommendations, re.DOTALL)
        if match:
            recommendations = match.group(1)
    elif recommendations.startswith('````'):
        pattern = r"````(.*?)```"
        match = re.search(pattern, recommendations, re.DOTALL)
        if match:
            recommendations = match.group(1)
    else:
        pattern1 = r"```(.*?)```"
        pattern2 = r"```python\n(.*?)```"
        pattern3 = r"```(.*?)```<|endoftext|>"
        pattern4 = r"````(.*?)```"
   
        if '```python' in recommendations:
            match = re.search(pattern2, recommendations, re.DOTALL)
        elif '```<|endoftext|>' in recommendations:
            match = re.search(pattern3, recommendations, re.DOTALL)
        else:
            if '````' in recommendations:
                match = re.search(pattern4, recommendations, re.DOTALL)
            else:
                match = re.search(pattern1, recommendations, re.DOTALL)

        if match:
            recommendations = match.group(1)
        else:
            pass
         
    return recommendations