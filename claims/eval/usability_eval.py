import os
import subprocess
import sys
import json
import logging
from importlib.metadata import version
from find_version import get_versions
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_script(script_path, attemp=0, timeout=5):
    """Execute a Python script and log the outcome, with a timeout."""
    try:
        # Added a timeout directly to subprocess.run()
        result = subprocess.run(['timeout', '1s', 'python3.8', script_path], capture_output=True, text=True, check=True, timeout=timeout)
        logging.info(f"SUCCESS: {script_path} ran successfully.")
        return 1
    except subprocess.TimeoutExpired:
        logging.error(f"TIMEOUT: {script_path} did not complete within {timeout} seconds.")
        return 0
    except subprocess.CalledProcessError as e:
        if 'ModuleNotFoundError' in e.stderr:
            attemp += 1
            missing_module = e.stderr.split("'")[-2]  # Assumes the error message format is consistent
            logging.warning(f"Attempting to install missing module: {missing_module}")
            try:
                install_support_package(missing_module)
            except:
                return 0
            if attemp < 3:
                return run_script(script_path, attemp, timeout)  # Retry running the script after installation
            else:
                return 0
        else:
            logging.error(f"FAILURE: {script_path} encountered an error: {e.stderr}")
            return 0

def install_support_package(package_name):
    """Install a package using pip."""
    try:
        subprocess.run(['python3.8', '-m', 'pip', 'install', package_name], check=True)
        logging.info(f"Successfully installed {package_name}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install {package_name}: {str(e)}")
        raise RuntimeError(f"Failed to install {package_name}: {str(e)}")

def install_package(package_name, version):
    """Install a specific version of a package using pip."""
    install_version = f"{package_name}=={version}"
    try:
        subprocess.run(['python3.8', '-m', 'pip', 'install', install_version], check=True)
        logging.info(f"Installed {install_version} successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install {install_version}: {str(e)}")

# def find_all_files(directory):
#     """Generate a list of all files in a directory."""
#     file_paths = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             full_path = os.path.join(root, file)
#             file_paths.append(full_path)
#     return file_paths
def find_all_files(directory):
    """Generate a list of all files in a directory."""
    return [str(file) for file in Path(directory).rglob('*') if file.is_file()]

def main(path1, path2):
    files_1 = find_all_files(path1)
    files_2 = find_all_files(path2)
    all_files = files_1 + files_2
    python_version = '3.8'  # The Python version you're interested in
    gpt_date = '2021-09-01'

    packages = {}
    files_dict = {}

    for file in all_files:
        try:
            print(file)
            package = file.split('/')[-3]
            package = package.lower()

            if package not in packages and package != 'cve':
                packages[package] = process_package(package, python_version, gpt_date)

            if package not in files_dict:
                files_dict[package] = []
            files_dict[package].append(file)
        except:
            pass
    assess_packages(packages, files_dict)
    save_to_json(packages, path1)  # Save package data to JSON

def process_package(package, python_version, gpt_date):
    """Retrieve version information and prepare package data structure."""
    latest_version, nearest_version, old_version = get_versions(package, python_version, gpt_date)
    logging.info(f"{package} - Latest: {latest_version}, Nearest: {nearest_version}, Old: {old_version}")
    return {
        'latest_version': latest_version,
        'latest_version_rate': {'origin': 0, 'filter': 0},
        'nearest_version': nearest_version,
        'nearest_version_rate': {'origin': 0, 'filter': 0},
        'old_version': old_version,
        'old_version_rate': {'origin': 0, 'filter': 0}
    }

def assess_packages(packages, files_dict):
    """Assess packages based on the latest, nearest, and old versions."""
    for package, data in packages.items():
        
        version_checks = [('latest_version', data['latest_version']),
                        ('nearest_version', data['nearest_version']),
                        ('old_version', data['old_version'])]

        for version_type, version_num in version_checks:
            if version_type == 'old_version':
                pass
            else:
                install_package(package, version_num)
                # print(package)
                try:
                    if package == 'pillow':
                        __import__('PIL')
                    elif package == 'scikit-learn':
                        __import__('sklearn')
                    else:
                        __import__(package)
                except:
                    logging.error(f"Failed to import {package} version {version_num}")
                    print(f'Failed to import {package} version {version_num}')
                
                try:
                    # installed_version = version(package)
                    # if installed_version != version_num:
                    #     logging.error(f"Failed to install {package} version {version_num}")
                    #     print(f'Failed to install {package} version {version_num}')
                    # else:
                    evaluate_package_version(package, version_num, files_dict[package], data[version_type + '_rate'])
                except:
                    logging.error(f"Failed to install {package} and check version {version_num}")
                    print(f"Failed to install {package} and check version {version_num}")
                
def evaluate_package_version(package, version_num, files, rate_dict):
    """Evaluate a specific version of a package by running associated scripts."""
    count_origin = count_filter = total_origin = total_filter = 0
    for file in files:
        file_type = file.split('/')[-4]  # 'filter' or 'origin'
        result = run_script(file)
        if file_type == 'filter':
            count_filter += result
            total_filter += 1
        elif file_type == 'origin':
            count_origin += result
            total_origin += 1

    if total_filter > 0:
        rate_dict['filter'] = count_filter / total_filter
    if total_origin > 0:
        rate_dict['origin'] = count_origin / total_origin
    logging.info(f"{package} version {version_num} - Filter rate: {rate_dict.get('filter', 0)}, Original rate: {rate_dict.get('origin', 0)}")

def save_to_json(data, path):
    target = path.split('/')[-2]
    """Save data to JSON file."""
    with open('./Usability-Eval/Result/usability'+target+'.json', 'a') as json_file:
        json.dump(data, json_file, indent=4)
        logging.info("Package data saved to JSON.")

def find_subdirectories_with_suffix(directory, suffix=''):
    """Find all subdirectories ending with a specific suffix in the given directory."""
    subdirs = []
    for root, dirs, files in os.walk(directory):
        # Filter and add directories that end with the suffix
        for d in dirs:
            # if d.endswith(suffix):
            #     subdirs.append(os.path.join(root, d))
            subdirs.append(os.path.join(root, d))
    
    return subdirs

if __name__ == "__main__":
    # path = '/data/Weiheng/TimeGap-Eval/result/temp_0_result'
    # main(path)

    # gpt_series = ['gpt-3.5-turbo-0125', 'gpt-4-turbo-2024-04-09', 'gpt-4o-mini-2024-07-18', 'gpt-4o-2024-08-06']
    gpt_series = ['gpt-4-turbo-2024-04-09', 'gpt-4o-mini-2024-07-18', 'gpt-4o-2024-08-06']
    replicate_series = ['granite-8b-code-instruct-128k', 'granite-20b-code-instruct-8k', 'granite-3.0-2b-instruct', 'granite-3.0-8b-instruct', 'codellama-34b-instruct', 'codellama-7b-instruct']
    mistral_series = ['ministral-3b-latest', 'ministral-8b-latest', 'codestral-latest', 'open-codestral-mamba']
    huggingface_series = ['Llama-3.1-70B-Instruct', 'Llama-3.1-8B-Instruct']
    deepseek_series = ['deepseek-coder']

    model_list = gpt_series + replicate_series + mistral_series + huggingface_series + deepseek_series

    for model in model_list:
        print(f'Processing model: {model}')
        directory = f'.//Usability-Eval/instr/UR-{model}'
        # subdirs = find_subdirectories_with_suffix(directory)
        subdirs = [f'{directory}/origin', f'{directory}/filter']
        main(subdirs[0], subdirs[1])