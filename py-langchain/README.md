Python Langchain Demo Project
---

## Project Setup

- Create a virtual environment: `python -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate`
- Install pipenv: `pipenv install`
- Install LangChain related packages:
    - `pipenv install langchain`
    - `pipenv install langchain-openai`
    - `pipenv install langchain-community`
    - `pipenv install langchainhub`
- Download `ollama` and setup
- Install ollama related packges: `pipenv install langchain-ollama`
- Install LLM model and run to chat with: `ollama run llama3`
- Install `mistral` LLM from ollama: `ollama pull mistral`
- Install `black` for formatting: `pipenv install black`
    - Format documents in folder: `black .`

## Develop real world Generative AI application

- Register on `https://app.scrapin.io`
- 

## Inspect AI

- Install inspect ai: `pip install inspect-ai`
- Install google gemini: `pip install google-genai`
- Configure `GOOGLE_API_KEY` to use Gemini LLM
- Run task `inspect eval theory.py --model google/gemini-2.0-flash`
- Inspect the task logs: `inspect view`


## Langsmith

- Add Langsmith for tracing
