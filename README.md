# 🛒 E-Commerce Product Assistant

An **AI-powered E-commerce Product Assistant** built with **FastAPI, Streamlit, MCP Servers, and Vector Databases**.  
This project helps in product search, recommendation, and AI agent workflows using modern tools like **DataStax**, **VectorDBs**, and **Docker** for deployment.  

---

## 🚀 Features
- Product search using **MCP servers**  
- **Agentic workflow** for intelligent product discovery  
- API built with **FastAPI**  
- **Streamlit UI** for interactive user experience  
- Vector database integration with **DataStax**  
- **Dockerized deployment**  
- Package installation using **`uv`** and `pyproject.toml`  


---

## ⚙️ Setup Instructions

### 1️⃣ Check Python Installation
```bash
python --version
```
If you don’t have Python installed, please install **Python 3.10, 3.11, or 3.12**.

### 2️⃣ Install `uv` (Universal Virtualenv Manager)
```bash
uv --version
```
If not installed:
```bash
pip install uv
```
Verify:
```python
import shutil
print(shutil.which("uv"))
```

### 3️⃣ Initialize Project
```bash
uv init <my-project-name>
uv pip list
uv python list
```

### 4️⃣ Create Virtual Environment
```bash
uv venv env --python cpython-3.10.18-windows-x86_64-none
uv venv <your-env-name> --python <your-python-version>
```

Activate environment:

- **Command Prompt (Windows)**  
  ```bash
  .\<your-env-name>\Scripts\activate.bat
  ```

- **Git Bash / WSL / MacOS / Linux**  
  ```bash
  source <your-env-name>/Scripts/activate
  ```

---

## 📦 Install Dependencies

Install packages individually:
```bash
uv add <package_name>
```

Install from requirements:
```bash
uv add -r requirements.txt
```

Or using `pyproject.toml`:
```bash
uv pip install -e .
```

---

## ▶️ Running the Application

### 1️⃣ Run MCP Server
```bash
python prod_assistant/mcp_servers/product_search_server.py
```

### 2️⃣ Test Application
Two ways to test:
- Using `client.py`  
- Using **Agentic Workflow**:  
  ```bash
  python prod_assistant/workflow/agentic_workflow_with_mcp_websearch.py
  ```

### 3️⃣ Run FastAPI App
```bash
uvicorn prod_assistant.router.main:app --reload --port 8000
```
App will run at:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 4️⃣ Run Streamlit UI
```bash
streamlit run <your_file_name.py>
```

---

## 🗄️ DataStax Integration
- Login: [DataStax Console](https://accounts.datastax.com/session-service/v1/login)  
- Use the **Astra DB API** credentials in your `.env` file:  

```env
ASTRA_DB_API_ENDPOINT=<your_endpoint>
ASTRA_DB_APPLICATION_TOKEN=<your_token>
ASTRA_DB_KEYSPACE=<your_keyspace>
```

---

## 🐳 Docker Setup

### Check Containers & Images
```bash
docker ps            # running containers
docker stop <id>     # stop container
docker rm <id>       # remove container
docker images        # list images
docker rmi <id>      # remove image
```

### Build Image
```bash
docker build -t prod-assistant .
```

### Run Container
```bash
docker run -d -p 8000:8000 --name product-assistant prod-assistant
```

---

## ☁️ Deployment Secrets (GitHub Actions / AWS)
Make sure to configure secrets in your GitHub repo:

```yaml
${{ secrets.AWS_ACCESS_KEY_ID }}
${{ secrets.AWS_SECRET_ACCESS_KEY }}
${{ secrets.AWS_REGION }}
${{ secrets.ECR_REGISTRY }}
${{ secrets.ECR_REPOSITORY }}
${{ secrets.EKS_CLUSTER_NAME }}
${{ secrets.GROQ_API_KEY }}
${{ secrets.GOOGLE_API_KEY }}
${{ secrets.ASTRA_DB_API_ENDPOINT }}
${{ secrets.ASTRA_DB_APPLICATION_TOKEN }}
${{ secrets.ASTRA_DB_KEYSPACE }}
```

---

## 🧪 Testing
- Run via API endpoints  
- Test UI with **Streamlit**  
- Use workflows for end-to-end validation  

---

## 📊 Vector DB Comparison
Check: [Superlinked Vector DB Comparison](https://superlinked.com/vector-db-comparison)  

---

## 💻 Tech Stack
- **Python 3.10+**  
- **FastAPI**  
- **Streamlit**  
- **MCP Servers**  
- **DataStax Astra DB**  
- **Docker**  
- **AWS ECR/EKS**  

---

## 👨‍💻 My teacher
**Sunny Savita**  
🔗 [GitHub](https://github.com/sunnysavita10)
