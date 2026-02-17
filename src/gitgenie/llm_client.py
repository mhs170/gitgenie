import ollama

def generate_text(prompt):
    try:
        stream = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}],
            stream=True
        )
        result = ""
        for chunk in stream:
            content = chunk['message']['content']
            print(content, end='', flush=True)
            result += content
        print() 
        return result
    except Exception as e:
        return None
    
if __name__ == '__main__':
    print("Testing generate_text()...")
    
    result = generate_text("Say 'Hello' in one word")
    if result:
        print(f"Success: {result}")
    else:
        print("Error: Ollama might not be running")