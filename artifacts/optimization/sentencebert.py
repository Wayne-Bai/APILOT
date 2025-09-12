import requests
import time
import json

# API setup
# API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
API_URL = "https://j570qhf9j9ecadi9.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept" : "application/json",
	"Authorization": "YOUR HUGGINGFACE API KEY",
	"Content-Type": "application/json" 
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def save_json(filename, data):
    with open(f"{filename}.json", 'w') as f:
        json.dump(data, f, indent=4)

# Measure the time to process the request
start_time = time.time()

file = "LLM-TimeGap/optimization/new_prompts/networkx.json"
data = load_json(file)
result_dict = {}

count = 0

prefix_prompt = data.keys()
for i in data:
    regenerate_prompt = data[i]
    for j in regenerate_prompt:
        # print(j)
        if j not in result_dict:
            result_dict[j] = []

        output = query({
            "inputs": {
                "source_sentence": j,
                "sentences": list(data.keys())
            }
        })
        count += 1
        print(output)
        result_dict[j].append(output)

print(result_dict)

# save_json("LLM-TimeGap/optimization/new_prompts/networkx_sentencebery_result", result_dict)

# Measure the elapsed time
elapsed_time = time.time() - start_time

# Print the response and the performance metrics
print("Response:", output)
print(f"Time taken to process: {elapsed_time:.2f} seconds")

# # TODO: TEST THE PERFORMANCE OF THE MODEL
# # Generate 100 example sentences
# sentences = [f"This is example sentence number {i}" for i in range(1, 101)]

# # Measure the time to process the request
# start_time = time.time()

# # Send request with 100 sentences
# output = query({
#     "inputs": {
#         "source_sentence": "That is a happy person",
#         "sentences": sentences
#     }
# })

# # Measure the elapsed time
# elapsed_time = time.time() - start_time

# # Print the response and the performance metrics
# print("Response:", output)
# print(f"Time taken to process 100 sentences: {elapsed_time:.2f} seconds")
