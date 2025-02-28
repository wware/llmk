# LLM Hack for Jupyter notebook

This is a dumb hack for Jupyter notebook that allows you
to chat about your code with an LLM.

## Running the LLM in a raw container

```bash
docker run -it --rm \
  -e LANGUAGE_MODEL=qwen2.5-coder:1.5b \
  -p 11434:11434 \
  -v "$(pwd)/ollama_data:/root/.ollama" \
  -v "${OLLAMA_MODELS:-./models}:/models" \
  ai-tinkerers-ollama bash
```

## Running the LLM in a docker compose

```bash
docker compose up -d
```

## Usage

```python
def dumb_factorial(n):
    if n == 0:
        return 1
    return n * dumb_factorial(n - 1)

from better import llm_chat
llm_chat("What does this code do?")
```
