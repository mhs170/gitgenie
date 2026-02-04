import ollama

def generate_text(prompt):
    try:
        response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}],
        #stream=True,
        )
        return response['message']['content']
    except Exception as e:
        return None