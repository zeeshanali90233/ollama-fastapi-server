# 🚀 Ollama FastAPI Server

A simple and efficient FastAPI server that provides a REST API interface for interacting with local Ollama language models. This project makes it easy to deploy and use Ollama models through a web API with Docker containerization.

## ✨ Features

- **Fast & Lightweight**: Built with FastAPI for high-performance API endpoints
- **Docker Containerized**: Easy deployment with Docker Compose
- **Ollama Integration**: Seamless integration with Ollama local language models
- **LangChain Support**: Utilizes LangChain for advanced language model interactions
- **Environment Configurable**: Flexible configuration through environment variables
- **Production Ready**: Designed for both development and production environments

## 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────────┐
│                 │────▶│                 │
│   FastAPI App   │     │  Ollama Server  │
│   (Port 8000)   │     │  (Port 11434)   │
│                 │◀────│                 │
└─────────────────┘     └─────────────────┘
```

## 📋 Prerequisites

- **Docker** and **Docker Compose** installed on your system
- At least 4GB of available RAM for model loading
- Internet connection for initial model downloads

## 🚀 Quick Start

### Method 1: Using Docker Compose (Recommended)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ollama-fastapi-server
   ```

2. **Start the services**:
   ```bash
   docker-compose up -d
   ```

3. **Wait for services to initialize** (approximately 30 seconds)

4. **Update the model in main.py** if needed:
   ```python
   llm = OllamaLLM(
       model="gemma:2b",  # Change to your downloaded model
       temperature=0,
       max_retries=2,
       base_url=ollama_base_url,
   )
   ```
    ```yml
        command:
        - |
            ollama serve &
            sleep 10
            echo "Pulling gemma3:270m model..." # Change to your downloaded model 
            ollama pull gemma3:270m
            echo "Model pull complete!"
            wait
    ```


5. **Test the API**:
   ```bash
   curl "http://localhost:8000/ask?prompt=Hello, how are you?"
   ```

### Method 2: Custom Docker Image

1. **Build your own FastAPI image**:
   ```bash
   docker build . -t your-username/fastapi-ollama-server
   ```

2. **Push to Docker Hub** (optional):
   ```bash
   docker push your-username/fastapi-ollama-server
   ```

3. **Update docker-compose.yml** to use your custom image:
   ```yaml
   fastapi-server:
     image: your-username/fastapi-ollama-server
     # Remove the 'build: .' line
   ```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_BASE_URL` | `http://ollama:11434` | Ollama server URL |
| `OLLAMA_HOST` | `0.0.0.0` | Ollama binding host |

### Available Models

You can use any model supported by Ollama. Popular choices include:

- **gemma:2b** - Small, fast model (2GB)
- **llama3.2:latest** - Latest LLaMA model
- **llama3.2:1b** - Very small model (1GB)
- **phi3:mini** - Microsoft's Phi-3 model
- **mistral:latest** - Mistral AI model

To download a model:
```bash
docker exec ollama-server ollama pull <model-name>
```

## 📚 API Documentation

### Endpoints

#### `GET /`
**Description**: Health check endpoint  
**Response**:
```json
{
  "Hello": "World"
}
```

#### `GET /ask`
**Description**: Send a prompt to the language model  
**Parameters**:
- `prompt` (query parameter, required): The text prompt to send to the model

**Example Request**:
```bash
curl "http://localhost:8000/ask?prompt=Explain quantum computing in simple terms"
```

**Example Response**:
```json
{
  "response": "Quantum computing is a type of computing that uses quantum mechanics..."
}
```

### Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🛠️ Development

### Local Development Setup

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally** (requires local Ollama installation):
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Project Structure

```
ollama-fastapi-server/
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile            # FastAPI container definition
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── .dockerignore       # Docker ignore rules
└── README.md          # This file
```

## 🔍 Troubleshooting

### Common Issues

1. **"Model not found" error**:
   - Solution: Download the model using `docker exec ollama-server ollama pull <model-name>`

2. **Connection refused to Ollama**:
   - Check if ollama container is running: `docker ps`
   - Restart services: `docker-compose restart`

3. **Out of memory errors**:
   - Try a smaller model like `gemma:2b` or `llama3.2:1b`
   - Increase Docker memory limits

4. **Slow response times**:
   - Ensure sufficient RAM is allocated to Docker
   - Use GPU acceleration if available (uncomment GPU config in docker-compose.yml)

### Viewing Logs

```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs ollama
docker-compose logs fastapi-server

# Follow logs in real-time
docker-compose logs -f
```

## ⚡ Performance Tips

- **Use GPU acceleration** for faster inference (uncomment GPU config in docker-compose.yml)
- **Choose smaller models** for better response times
- **Adjust model parameters** (temperature, max_retries) based on your use case
- **Monitor resource usage** with `docker stats`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Ollama](https://ollama.com/) - For providing excellent local LLM capabilities
- [FastAPI](https://fastapi.tiangolo.com/) - For the amazing web framework
- [LangChain](https://langchain.readthedocs.io/) - For LLM integration tools

---

**Happy Coding! 🎉**