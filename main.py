import os
from fastapi import FastAPI
from langchain_ollama import OllamaLLM

app = FastAPI()

# Get Ollama base URL from environment variable, default to localhost
ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

llm = OllamaLLM(
    model="gemma3:270m",
    temperature=0,
    max_retries=2,
    base_url=ollama_base_url,
)

@app.get("/ask")
async def ask_llm(prompt: str):
    response = llm.invoke(prompt)
    return {"response": response}

@app.get("/")
def read_root():
    return {"Hello": "World"}
