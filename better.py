import os
import json
import time
import requests
from IPython.display import display, Javascript, Markdown

def llm_chat(query):
    """Save notebook, read contents, and process with LLM"""
    
    # 1. Force notebook save and get contents
    display(Javascript(
        "document.body.dispatchEvent("
        "new KeyboardEvent('keydown', {key:'s', keyCode: 83, ctrlKey: true}"
        "))"
    ))
    
    notebook_name = os.environ.get("JPY_SESSION_NAME")
    with open(notebook_name) as f:
        notebook = json.load(f)

    code_cells = []
    for cell in notebook['cells']:
        source = ''.join(cell['source'])
        if cell['cell_type'] == 'code':
            code_cells.append("```")
            code_cells.append(source)
            code_cells.append("```")
        else:
            code_cells.append(source)

    query += "\n\n\nContext:\n\n" + "\n".join(code_cells)
    
    full_query = query + "\n\nContext:\n\n" + "\n".join(code_cells)
    
    ollama_host = os.environ.get("OLLAMA_HOST")
    model = os.environ.get("LANGUAGE_MODEL")
    
    chat_request = {
        "model": model,
        "messages": [
            {
                "role": "user", 
                "content": full_query
            }
        ],
        "stream": False  # Get complete response at once
    }

    try:
        display(Markdown("Just a moment, thinking..."))
        time.sleep(0.1)
        # Make request to Ollama API
        response = requests.post(
            f"http://{ollama_host}:11434/api/chat",
            json=chat_request,
            timeout=600
        )
        response.raise_for_status()
        
        # Extract and display the response
        result = response.json()
        if "message" in result and "content" in result["message"]:
            display(Markdown(result["message"]["content"]))
        else:
            display(Markdown("Error: Unexpected response format from LLM"))
            
    except requests.exceptions.RequestException as e:
        display(Markdown(f"Error communicating with LLM service: {str(e)}"))
    except Exception as e:
        display(Markdown(f"Unexpected error: {str(e)}"))
