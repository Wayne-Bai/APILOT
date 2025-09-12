import ast
import json
import os
import shutil
import yaml
import pkg_resources
from importlib.metadata import version
from distutils.version import StrictVersion, LooseVersion
from utils.ast import ast_to_dict, extract_functions_and_attributes_with_parents
import csv
import re
from utils.code_process import extract_blacklist, post_process
import copy
# import sagemaker
# import boto3
# from sagemaker.huggingface import HuggingFaceModel
from transformers import pipeline


# text = 'Here is a """sample string""" enclosed in triple quotes.' 
# matches = re.findall(pattern, text) 
# print(matches)

template_string = """from importlib.metadata import version
from distutils.version import StrictVersion, LooseVersion

package_name = '{package_name}'  # Replace
module = __import__(package_name)
package_version = version(package_name)

# StrictVersion requires versions to be in the format X.Y.Z
v1 = StrictVersion(str(package_version))
v2 = {version_list}

if v1 in v2:
{regenerate_code}
else:
{original_code}

"""

###### GENERATE SOLUTION ######
def generate_solution(client, prompt_path, model, all_recommendations, package, row, BANNED_FUNCTIONS_LIST, instruction, gen_time):

    notice = """Act as a coding expert. Generate Python code based on the user instructions below. Only output the code solution within code blocks (```). Avoid using any functions listed in {BANNED_FUNCTIONS_LIST} as they are outdated APIs. Instead, provide alternative solutions."""
    notice =  notice.format(BANNED_FUNCTIONS_LIST = BANNED_FUNCTIONS_LIST)

    messages = [
        {"role": "system", "content": notice}
    ]
    with open(prompt_path, 'r', encoding='utf-8') as f:
        prompt = f.read()

    user_input = prompt.format(PACKAGE = package, DESCRIPTION = instruction)
    messages.append({"role": "user", "content": user_input})

    recommendations = ""
    functions = {}
    temp = os.getenv('TEMP_VALUE')
    temp = float(temp)

    for i in range(gen_time):
        try:
            # response = client.chat.completions.create(
            #     model=model,
            #     messages=messages,
            #     max_tokens=4096,
            #     temperature=temp
            # )

            # recommendations = response.choices[0].message.content

            # try:
            #     role = sagemaker.get_execution_role()
            #     print(role)
            # except ValueError:
            #     iam = boto3.client('iam')
            #     role = iam.get_role(RoleName='AWS-APILOT')['Role']['Arn']

            # # Hub Model configuration. https://huggingface.co/models
            # hub = {
            #     'HF_MODEL_ID':'ibm-granite/granite-3.0-8b-instruct',
            #     'HF_TASK':'text-generation'
            # }

            # # create Hugging Face Model Class
            # huggingface_model = HuggingFaceModel(
            #     transformers_version='4.37.0',
            #     pytorch_version='2.1.0',
            #     py_version='py310',
            #     env=hub,
            #     role=role, 
            # )

            # # deploy model to SageMaker Inference
            # predictor = huggingface_model.deploy(
            #     initial_instance_count=1, # number of instances
            #     instance_type='ml.m5.xlarge' # ec2 instance type
            # )

            # instruct_input = f"<|start_of_role|>system<|end_of_role|>{notice}<|end_of_text|>" +\
            #                  f"<|start_of_role|>user<|end_of_role|>{user_input}<|end_of_text|>" +\
            #                  "<|start_of_role|>assistant<|end_of_role|>"
            # print(instruct_input)

            # response = predictor.predict({
            #             "inputs": instruct_input,
            #         })
            # print(response)

            pipe = pipeline("text-generation", model="ibm-granite/granite-3.0-2b-instruct")
            response = pipe(messages)
            print(response)

            exit()
            recommendations = post_process(recommendations)

            parsed_ast = ast.parse(recommendations)
            ast_dict = ast_to_dict(parsed_ast)

            called_functions, _ = extract_functions_and_attributes_with_parents(ast_dict, package=package.lower())
       
            key = f'Solution{i+1}'

            if parsed_ast:
                functions[key] = {
                    'code': recommendations,
                    'functions': called_functions
                }
            else:
                print("The generated code can't be parsed.")

        except Exception as e:
            print(e)
            recommendations = "Error"

    solution = {
        "Package": package,
        "Instruction": instruction,
        "Function Name": row['Function Name'],
        "Function Description": row['Function Description'],
        "Solutions": functions
    }

    all_recommendations.append(solution)
    return solution


def detector(issue_function, func_solution, issue_rate_info):
    ISSUED_FUNCTION = issue_function[func_solution['Package']]
    rate_dep = 0
    
    if func_solution['Solutions'] != {}:

        index = []
        issued_function = []

        for solutions, called_functions in func_solution['Solutions'].items():

            called_functions_list = [pair for pair in called_functions['functions'] if pair[0] is not None]
            callname = set([pair[0] for pair in called_functions_list])

            #### CVE CASE ####
            if isinstance(ISSUED_FUNCTION, dict):
                overlap1 = set(ISSUED_FUNCTION.keys()) & set(callname)

            #### GENERAL CASE ####
            elif isinstance(ISSUED_FUNCTION,list):
                overlap1 = set(ISSUED_FUNCTION) & set(callname)
            
            if overlap1:
                rate_dep += 1
                index.append(solutions)
                issued_function.extend(list(overlap1))

        issue_rate = {
            "Function Name": func_solution['Function Name'],
            "Issue Index": index,
            "Issue Rate Dep": rate_dep / len(func_solution['Solutions']),
            "Issued Functions": list(set(issued_function))
        }

        # issue_rate_info.append(issue_rate)   
        return issue_rate, rate_dep, len(func_solution['Solutions'])
    else:
        issue_rate = {
            "Function Name": func_solution['Function Name'],
            "Issue Index": None,
            "Issue Rate Dep": 0.0,
            "Issued Functions": []
        }

        # issue_rate_info.append(issue_rate)   
        return issue_rate, 0, 0

def detector_CVE(issue_function, func_solution, issue_rate_info):
    ISSUED_FUNCTION = issue_function['CVE']
    rate_dep = 0
    
    if func_solution['Solutions'] != {}:

        index = []
        issued_function = []

        for solutions, called_functions in func_solution['Solutions'].items():

            called_functions_list = [pair for pair in called_functions['functions'] if pair[0] is not None]
            callname = set([pair[0] for pair in called_functions_list])

            #### CVE CASE ####
            if isinstance(ISSUED_FUNCTION, dict):
                overlap1 = set(ISSUED_FUNCTION.keys()) & set(callname)

            #### GENERAL CASE ####
            elif isinstance(ISSUED_FUNCTION,list):
                overlap1 = set(ISSUED_FUNCTION) & set(callname)
            
            if overlap1:
                rate_dep += 1
                index.append(solutions)
                issued_function.extend(list(overlap1))

        issue_rate = {
            "Function Name": func_solution['Function Name'],
            "Issue Index": index,
            "Issue Rate Dep": rate_dep / len(func_solution['Solutions']),
            "Issued Functions": list(set(issued_function))
        }

        # issue_rate_info.append(issue_rate)   
        return issue_rate, rate_dep, len(func_solution['Solutions'])
    else:
        issue_rate = {
            "Function Name": func_solution['Function Name'],
            "Issue Index": None,
            "Issue Rate Dep": 0.0,
            "Issued Functions": []
        }

        # issue_rate_info.append(issue_rate)   
        return issue_rate, 0, 0

##### Solution Filter in General Case #####
def filter(issue_rate, origin_func_rec, issue_function, prompt_path, client, model_name, ban_functions, instruction, gen_time, regeneration=[], time=0, max_time=3):
    print(f"Max Time: {max_time}")
    
    func_rec = copy.deepcopy(origin_func_rec)
    BANNED = issue_function[func_rec['Package']]
    banned_functions = list(set(issue_rate['Issued Functions'] + ban_functions))
    print(f"Banned Functions: {banned_functions}")
    func_rec['banned_functions'] = banned_functions

    # Base case: return func_rec and the latest counts if max_time is reached
    if time >= max_time:
        return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration

    # Recursive case: if issue_rate['Issue Rate Dep'] == 1, check for issues and regenerate
    if issue_rate['Issue Rate Dep'] == 1:

        #### GENERATE NEW SOLUTIONS 
        latest_num_issue = 0
        latest_num_sol = 0

        re_func_rec = generate_solution(client, prompt_path, model_name, [], func_rec['Package'], func_rec, banned_functions, instruction, gen_time)
        issue_rate, latest_num_issue, latest_num_sol = detector(issue_function, re_func_rec, [])

        if latest_num_sol == 0:
            latest_num_sol = 1
        
        if latest_num_issue/latest_num_sol == 1:
            ISSUE = True
        else:
            ISSUE = False
            
        regeneration.append({"num_issue": latest_num_issue, "num_sol": latest_num_sol})

        # If issues are found, increment time and recursively call filter again
        if ISSUE and time < max_time - 1:  # Recursively call unless max_time is reached
            return filter(issue_rate, func_rec, issue_function, prompt_path, client, model_name, banned_functions, instruction, gen_time, regeneration, time + 1, max_time)
        else:
            return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time+1, regeneration

    elif issue_rate['Issue Rate Dep'] == 0:
        latest_num_sol = len(func_rec['Solutions'])
        # No action is needed, simply return the original function record
        # return func_rec, latest_num_issue, latest_num_sol, time, regeneration
        regeneration.append({"num_issue": 0, "num_sol": latest_num_sol})
        return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration
        
    else:
        # Remove solutions based on the issue index
        for key in list(func_rec['Solutions'].keys()):
            if key in issue_rate['Issue Index']:
                func_rec['Solutions'].pop(key)

        latest_num_issue = 0
        latest_num_sol = len(func_rec['Solutions'])

        regeneration.append({"num_issue": latest_num_issue, "num_sol": latest_num_sol})

        # Return the final func_rec along with the latest num_issue and num_sol
        # return func_rec, latest_num_issue, latest_num_sol, time, regeneration
        return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration

def filter_CVE(issue_rate, origin_func_rec, issue_function, prompt_path, client, model_name, ban_functions, instruction, gen_time, regeneration=[], time=0, max_time=3):
    print(f"Max Time: {max_time}")
    
    func_rec = copy.deepcopy(origin_func_rec)
    BANNED = issue_function['CVE']
    banned_functions = list(set(issue_rate['Issued Functions'] + ban_functions))
    print(f"Banned Functions: {banned_functions}")
    func_rec['banned_functions'] = banned_functions

    # Base case: return func_rec and the latest counts if max_time is reached
    if time >= max_time:
        return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration

    # Recursive case: if issue_rate['Issue Rate Dep'] == 1, check for issues and regenerate
    if issue_rate['Issue Rate Dep'] == 1:

        #### GENERATE NEW SOLUTIONS 
        latest_num_issue = 0
        latest_num_sol = 0

        re_func_rec = generate_solution(client, prompt_path, model_name, [], func_rec['Package'], func_rec, banned_functions, instruction, gen_time)
        issue_rate, latest_num_issue, latest_num_sol = detector_CVE(issue_function, re_func_rec, [])

        if latest_num_sol == 0:
            latest_num_sol = 1
        
        if latest_num_issue/latest_num_sol == 1:
            ISSUE = True
        else:
            ISSUE = False
        
        regeneration.append({"num_issue": latest_num_issue, "num_sol": latest_num_sol})

        # If issues are found, increment time and recursively call filter again
        if ISSUE and time < max_time - 1:  # Recursively call unless max_time is reached
            return filter_CVE(issue_rate, re_func_rec, issue_function, prompt_path, client, model_name, banned_functions, instruction, gen_time, regeneration, time + 1, max_time)
        else:
            return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time+1, regeneration

    elif issue_rate['Issue Rate Dep'] == 0:
        latest_num_sol = len(func_rec['Solutions'])
        # No action is needed, simply return the original function record
        # return func_rec, latest_num_issue, latest_num_sol, time, regeneration
        regeneration.append({"num_issue": 0, "num_sol": latest_num_sol})
        return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration
        
    else:
        # Remove solutions based on the issue index
        for key in list(func_rec['Solutions'].keys()):
            if key in issue_rate['Issue Index']:
                func_rec['Solutions'].pop(key)

        latest_num_issue = 0
        latest_num_sol = len(func_rec['Solutions'])

        regeneration.append({"num_issue": latest_num_issue, "num_sol": latest_num_sol})

        # Return the final func_rec along with the latest num_issue and num_sol
        # return func_rec, latest_num_issue, latest_num_sol, time, regeneration
        return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration


##### CVE Detector #####
def cve_filter(issue_rate, origin_func_rec, issue_function, prompt_path, client, model_name, ban_functions, instruction, gen_time, regeneration=[], time=0, max_time=3):
    print(f"Max Time: {max_time}")
    
    func_rec = copy.deepcopy(origin_func_rec)
    package_version = StrictVersion(str(version(func_rec['Package'])))

    # Handle special cases like numpy
    if func_rec['Package'] == 'numpy':
        package_version = StrictVersion('0.25.0')
    
    BANNED = issue_function[func_rec['Package']]
    banned_functions = list(set(issue_rate['Issued Functions'] + ban_functions))
    print(f"Banned Functions: {banned_functions}")
    func_rec['banned_functions'] = banned_functions

    # Base case: return func_rec and the latest counts if max_time is reached
    if time >= max_time:
        return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration

    # Recursive case: if issue_rate['Issue Rate Dep'] == 1, check for issues and regenerate
    if issue_rate['Issue Rate Dep'] == 1:
        #### GENERATE NEW SOLUTIONS 
        latest_num_issue = 0
        latest_num_sol = 0

        re_func_rec = generate_solution(client, prompt_path, model_name, [], func_rec['Package'], func_rec, banned_functions, instruction, gen_time)
   
        ISSUE = False
        count = 0
        
        for key, called_functions in re_func_rec['Solutions'].items():
            called_functions = [pair[0] for pair in called_functions['functions']]

            # CVE case: detect overlaps with banned functions
            if isinstance(BANNED, dict):
                issue = set(BANNED.keys()) & set(called_functions)
            elif isinstance(BANNED, list):
                issue = set(BANNED) & set(called_functions)

            if issue:
                ISSUE = True
                count += 1
                banned_functions.extend(issue)
                func_rec['banned_functions'] = list(set(banned_functions))

        latest_num_issue = count
        latest_num_sol = len(re_func_rec["Solutions"])
        if latest_num_sol == 0:
            latest_num_sol = 1
        else:
            issue_rate['Issue Rate Dep'] = latest_num_issue / latest_num_sol
        
        # Append to regeneration log
        regeneration.append({"num_issue": latest_num_issue, "num_sol": latest_num_sol})

        # If issues are found, increment time and recursively call cve_filter again
        if ISSUE and time < max_time - 1:  # Recursively call unless max_time is reached
            return cve_filter(issue_rate, func_rec, issue_function, prompt_path, client, model_name, banned_functions, instruction, gen_time, regeneration, time + 1, max_time)
        else:
            return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration

    elif issue_rate['Issue Rate Dep'] == 0:
        latest_num_sol = len(func_rec['Solutions'])
        # No action is needed, simply return the original function record
        regeneration.append({"num_issue": 0, "num_sol": latest_num_sol})
        return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration
        
    else:
        # Remove solutions based on the issue index
        for key in list(func_rec['Solutions'].keys()):
            if key in issue_rate['Issue Index']:
                func_rec['Solutions'].pop(key)

        latest_num_issue = 0
        latest_num_sol = len(func_rec['Solutions'])

        regeneration.append({"num_issue": latest_num_issue, "num_sol": latest_num_sol})

    # Return the final func_rec along with the latest num_issue and num_sol
    return func_rec, regeneration[-1]['num_issue'], regeneration[-1]['num_sol'], time, regeneration


def process_code_snippets(original_code):
    # Extract all code snippets
    code_snippets = [solution['code'] for solution in original_code.values()]

    # Prepare the final code string
    final_code_list = []

    # Indent and add the first code snippet
    if code_snippets:
        indented_first_code = "\n".join(['\t' + line for line in code_snippets[0].splitlines()])
        final_code_list.append(indented_first_code)

    # Comment and indent the remaining code snippets
    for snippet in code_snippets[1:]:
        commented_and_indented_snippet = '\n'.join(['# \t' + line for line in snippet.splitlines()])
        final_code_list.append(commented_and_indented_snippet)

    # Join all snippets into a single string
    final_code_string = '\n\n'.join(final_code_list)

    return final_code_string


def extract_cvelist(cve_path):
    modified_functions_list = {}

    with open(cve_path, 'r') as file:
        try:
            data = yaml.safe_load(file)

            for cve in data:
                package_name = cve['Package'].split('-')[0]

                if package_name == 'pytorch':
                    package_name = 'torch'
                if package_name == 'jinja2':
                    package_name = 'Jinja2'
                if package_name == 'yaml':
                    package_name = 'pyyaml'

                modified_functions = [func.split('.')[-1] for func in cve['modified_functions']]

                if package_name not in modified_functions_list:
                    modified_functions_list[package_name] = {}

                for func in modified_functions:
                    if func in modified_functions_list[package_name]:
                        # Add non-overlapping affected versions
                        for version in cve['affected_versions']:
                            if version not in modified_functions_list[package_name][func]['affected_versions']:
                                modified_functions_list[package_name][func]['affected_versions'].append(version)
                    else:
                        modified_functions_list[package_name][func] = {
                            'affected_versions': cve['affected_versions']
                        }
         
            return modified_functions_list
        
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")
            return None
        
def save_solution_py_cve(Function_Name, solution, path):
    ## If directory exists, remove it
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)

    api_path = os.path.join(path, f"{Function_Name}.py")
    with open(api_path, 'w') as file:
            file.write(solution)


def save_solution_py(recommendation_result, path):
    ## If directory exists, remove it
    if os.path.exists(path):
        shutil.rmtree(path)
    
    os.makedirs(path)
    for rec in recommendation_result:
        api_path = os.path.join(path, rec['Function Name'])
        if os.path.exists(api_path):
            shutil.rmtree(api_path)

        os.makedirs(api_path)
        for key, solution in rec['Solutions'].items():
           
            file_name = f"{key}.py"
            full_path = os.path.join(api_path, file_name)

            with open(full_path, 'w') as file:
                file.write(solution['code'])

    
def save_recommendations(data, path):
    if not os.path.isfile(path):
        with open(path, 'w') as file:
            file.write('') 

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)



def generate_solution_old(client, prompt_path, model, all_recommendations, package, row, BANNED_FUNCTIONS_LIST):

    notice = """Act as a coding expert. Please generate Python code based on the following user instructions.  Do not output other words except code solution. Code should be in ```  ```.  You should never call any function from {BANNED_FUNCTIONS_LIST} for your any solutions."""
    notice =  notice.format(BANNED_FUNCTIONS_LIST = BANNED_FUNCTIONS_LIST)

    messages = [
        {"role": "system", "content": notice}
    ]
    with open(prompt_path, 'r', encoding='utf-8') as f:
        prompt = f.read()

    user_input = prompt.format(PACKAGE = package, DESCRIPTION = row['Function Description'])
    messages.append({"role": "user", "content": user_input})

    recommendations = ""
    functions = {}
    temp = os.getenv('TEMP_VALUE')
    temp = float(temp)

    for i in range(10):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=4096,
                temperature=temp
            )

            recommendations = response.choices[0].message.content
            recommendations = post_process(recommendations)

            parsed_ast = ast.parse(recommendations)
            ast_dict = ast_to_dict(parsed_ast)

            called_functions, _ = extract_functions_and_attributes_with_parents(ast_dict, package=package.lower())
       
            key = f'Solution{i+1}'

            if parsed_ast:
                functions[key] = {
                    'code': recommendations,
                    'functions': called_functions
                }
            else:
                print("The generated code can't be parsed.")

        except Exception as e:
            print(e)
            recommendations = "Error"

    all_recommendations.append({
        "Package": package,
        "Function Name": row['Function Name'],
        "Function Description": row['Function Description'],
        "Solutions": functions
    })

    return user_input

##### Issued Function Dectector in General Case #####
def detector_old(issue_function, recommendation_result_path, origin):
    try:
        with open(recommendation_result_path, 'r') as file:
            recommendation = json.load(file)
    except FileNotFoundError:
        print("Used function not found.")
    
    # API LEVEL COUNT
    dep_api = 0
    fun_api = 0

    # SOLUTION LEVEL COUNT
    dep_sol = 0
    fun_sol = 0
    total_sol = 0

    # ISSUE RATE PER FUNCTION
    issue_rate_info = []
    
    for function in recommendation:
        ISSUED_FUNCTION = issue_function[function['Package']]

        issued_function = []

        if function['Solutions'] != {}:
            DEPENDENCY_ISSUE = False
            FUNCTION_ISSUE = False

            total_sol += len(function['Solutions'])
            test_function = [function['Function Name'].split('.')[-1]]
            index = []

            rate_dep = 0
            rate_fun = 0

            ###### CHECK ISSUE INCLUDING DEPENDENCIES ######
            for solutions, called_functions in function['Solutions'].items():
                DEPENDENCY = False
                FUNCTION = False

                called_functions_list = [pair for pair in called_functions['functions'] if pair[0] is not None]
                callname = set([pair[0] for pair in called_functions_list])
                callparent = set([pair[1] for pair in called_functions_list])

                callpairs = list(zip(callname, callparent))

                #### CVE CASE ####
                if type(ISSUED_FUNCTION) == dict:
                    overlap1 = set(ISSUED_FUNCTION.keys()) & set(callname)

                #### GENERAL CASE ####
                elif type(ISSUED_FUNCTION) == list:
                    overlap1 = set(ISSUED_FUNCTION) & set(callname)
                
                if overlap1:
                    DEPENDENCY_ISSUE = True
                    DEPENDENCY = True
                    issued_function.extend(list(overlap1))
                    
                    ###### CHECK ISSUE WITHOUT DEPENDENCIES ######
                    overlap2 = set(test_function) & callname
                    if overlap2:
                        FUNCTION_ISSUE = True
                        FUNCTION = True
                        issued_function.extend(list(overlap2))

                if DEPENDENCY:
                    rate_dep += 1
                    dep_sol += 1
                    index.append(solutions)

                if FUNCTION:
                    rate_fun += 1
                    fun_sol += 1  
                
            if DEPENDENCY_ISSUE:
                dep_api += 1
         
            if FUNCTION_ISSUE:
                # print("Function ", function['Function Name'], " has issue.")
                fun_api += 1

            issue_rate_info.append({
                "Function Name": function['Function Name'],
                "Issue Index": index,
                "Issue Rate Dep": rate_dep / len(function['Solutions']),
                "Issue Rate Fun": rate_fun / len(function['Solutions']),
                "Issued Functions": list(set(issued_function))
            })

        else:
            issue_rate_info.append({
                "Function Name": function['Function Name'],
                "Issue Index": None,
                "Issue Rate Dep": 0.0,
                "Issue Rate Fun": 0.0,
                "Issued Functions": []
            })

        if origin:
            prompt_path = '../Prompt/prompt.md'
            with open(prompt_path, 'r', encoding='utf-8') as f:
                prompt = f.read()
            user_input = prompt.format(PACKAGE = function["Package"], DESCRIPTION = function['Function Description'])

            json_file_path = './Data/prompt_api/prompt_api_4o.json'
            if os.path.exists(json_file_path):
                with open(json_file_path, 'r') as file:
                    data = json.load(file)
            else:
                data = {}
           
            func_desc = user_input
            print(func_desc)
            if func_desc not in data:
                issued_function = list(set(issued_function))
                data[func_desc] = issued_function

            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)

    dep_api_rate = dep_api / len(recommendation)
    func_api_rate = fun_api / len(recommendation)
    dep_sol_rate = dep_sol / total_sol
    func_sol_rate = fun_sol / total_sol

    print("API LEVEL")
    print("Recommendation Issue rate with dependency: ", dep_api_rate)
    print("Recommendation Issue rate without dependency: ", func_api_rate)

    print("SOLUTION LEVEL")
    print("Recommendation Issue rate with dependency: ", dep_sol_rate)
    print("Recommendation Issue rate without dependency: ", func_sol_rate)


    return issue_rate_info, [dep_api_rate, func_api_rate, dep_sol_rate, func_sol_rate]


def cve_detector_old(blacklist, recommendation_result_path, prompt_path, client, model_name):
    ### GET USED FUNCTION ###
    try:
        with open(recommendation_result_path, 'r') as file:
            recommendation = json.load(file)
    except FileNotFoundError:
        print("recommendation file not found.")
    
    for function in recommendation:
        
        package_version = version(function['Package'])
        v1 = StrictVersion(str(package_version))
        if function['Package'] == 'numpy':
            v1 = '0.25.0'
        

        ISSUED_FUNCTION = blacklist[function['Package']]
        ISSUE_INDEX = []

        original_code = function['Solutions']
        update_code = {}

        if function['Solutions'] != {}:
            issued_functions = []
            all_affected_versions = set()

#### Check issue rate
            ISSUE_RATE = 0
            for solutions, called_functions in function['Solutions'].items():
            
                called_functions_list = [pair for pair in called_functions['functions'] if pair[0] is not None]
                callname = set([pair[0] for pair in called_functions_list])
                overlap = set(ISSUED_FUNCTION.keys()) & set(callname)

                if overlap:
                    vulnerable_functions = []
                    for name in overlap:
                        
                        if str(v1) in ISSUED_FUNCTION[name]['affected_versions']:
                            vulnerable_functions.append(name)
                            all_affected_versions.update(ISSUED_FUNCTION[name]['affected_versions'])

                    if vulnerable_functions:
                        ISSUE_INDEX.append(solutions)
                        ISSUE_RATE += 1
                        issued_functions.extend(vulnerable_functions)
            
###### IF ISSUE RATE IS FULL, REGENERATE SOLUTIONS ######
            if ISSUE_RATE == len(function['Solutions']):
                time = 0
                while time < 3:
                    notice = """Act as a coding expert. Please generate Python code based on the following user instructions.  Do not output other words except code solution. Code should be in ```  ```.  You should never call any function from {BANNED_FUNCTIONS_LIST} for your any solutions."""
                    notice = notice.format(BANNED_FUNCTIONS_LIST = issued_functions)

                    messages = [{"role": "system", "content": notice}]
                    with open(prompt_path, 'r', encoding='utf-8') as f:
                        prompt = f.read()
                   

                    user_input = prompt.format(PACKAGE = function['Package'], DESCRIPTION = function['Function Description'])
                    messages.append({"role": "user", "content": user_input})

                    recommendations = ""
                    temp = os.getenv('TEMP_VALUE')
                    temp = float(temp)

                    for i in range(10):
                        try:
                            response = client.chat.completions.create(
                                model=model_name,
                                messages=messages,
                                max_tokens=4096,
                                temperature=temp
                            )

                            recommendations = response.choices[0].message.content
                            recommendations = post_process(recommendations)

                            parsed_ast = ast.parse(recommendations)
                            ast_dict = ast_to_dict(parsed_ast)

                            key = f'Solution{i+1}'
                            # Extract functions called from 'nx' package
                            called_info, _ = extract_functions_and_attributes_with_parents(ast_dict, package=function['Package'].lower())
                            called_info = list(set(called_info))  

                            called_functions = [pair[0] for pair in called_info]

                            overlap = set(ISSUED_FUNCTION.keys()) & set(called_functions)

                            if overlap:
                                vulnerable_functions = []
                                for name in overlap:
                                    if str(v1) in ISSUED_FUNCTION[name]['affected_versions']:
                                        vulnerable_functions.append(name)
                                        all_affected_versions.update(ISSUED_FUNCTION[name]['affected_versions'])
                                
                                if vulnerable_functions:
                                    if time != 2:
                                        issued_functions.extend(vulnerable_functions)
                                    else:
                                        if parsed_ast:
                                            update_code[key] = {
                                                'code': recommendations,
                                                'functions': called_info,
                                                'issue explanation': 'Function still calls CVE functions.'
                                            }
                                        else:
                                            print("The regenerated code can't be parsed.")
                                else:
                                    if parsed_ast:
                                        update_code[key] = {
                                            'code': recommendations,
                                            'functions': called_info,
                                        }
                                    else:
                                        print("The regenerated code can't be parsed.")
                            else:
                                if parsed_ast:
                                    update_code[key] = {
                                        'code': recommendations,
                                        'functions': called_info,
                                    }
                                else:
                                    print("The regenerated code can't be parsed.")

                            if update_code == {}:
                                issued_functions = list(set(issued_functions))
                                time += 1
                            else:
                                break

                        except Exception as e:
                            print(e)
                            recommendations = "Error"
                
                original_code = process_code_snippets(original_code)
                update_code = process_code_snippets(update_code)
                final_code = template_string.format(package_name = function['Package'], version_list = list(all_affected_versions), regenerate_code = update_code, original_code = original_code)

            elif ISSUE_RATE == 0:
                original_code = process_code_snippets(original_code)
                case1 = '\t' + 'pass'
                final_code = template_string.format(package_name = function['Package'], version_list = list(all_affected_versions), regenerate_code = '\t' + 'pass', original_code = original_code)


            else:
                for key in list(function['Solutions'].keys()):
                    if key in ISSUE_INDEX:
                        update_code[key] = function['Solutions'][key]
                        function['Solutions'].pop(key)

                update_code = process_code_snippets(update_code)
                final_code = template_string.format(package_name = function['Package'], version_list = list(all_affected_versions), regenerate_code = update_code, original_code = original_code)

            save_solution_py_cve(function['Function Name'], final_code, f'./CVE')
