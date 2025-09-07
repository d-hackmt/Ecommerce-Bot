import importlib.metadata
packages = [
    "langchain",
    "python-dotenv",
    "langchain_core",
    "streamlit",
    "fastapi",
    "html5lib",
    "jinja2",
    "langchain-astradb",
    "langchain-google-genai",
    "langchain-groq",
    "lxml",
    "python-multipart",
    "selenium",
    "undetected-chromedriver",
    "uvicorn",
    "structlog"
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")