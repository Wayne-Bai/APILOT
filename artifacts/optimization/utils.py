import openai

client = openai.Client(api_key="YOUR OWN OPENAI API KEY HERE")

def LLM(function_description, temperature=1):

    notice = """You are an expert in prompt generation. The prompt you generated should in ```  ```. Importantly, remember to only output the prompt."""

    messages = [
        {"role": "system", "content": notice}
    ]

    prompt = "Imagine you are a developer, and you want to utilize LLM-assisted code tools (like GitHub Copilot) to generate code for {function_descrption}. Please write the prompt."

    user_input = prompt.format(function_descrption=function_description)

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=messages,
        max_tokens = 4096,
        temperature = temperature,
    )

    return response.choices[0].message.content