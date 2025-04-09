# 🚀 FastAPI Boilerplate

A minimal, production-ready FastAPI project template — structured for clarity, testing, and Docker deployment.

---

## 📁 Project Structure

```
fastapi_boilerplate/
├── app/
│   ├── main.py              # Entry point
│   ├── api/
│   │   └── health.py        # Health check route
├── tests/
│   └── test_health.py       # Basic test
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker build instructions
├── Makefile                 # Useful commands
└── .dockerignore            # Docker build exclusions
```

---

## ▶️ Quick Start (Local)

### 1. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
make run
```

Visit: http://localhost:8000

---

## 🧪 Run Tests

```bash
make test
```

---

## 🐳 Run with Docker

### 1. Build the Docker image

```bash
make docker-build
```

### 2. Run the container

```bash
make docker-run
```

---

## 🔧 Makefile Commands

| Command           | Description                         |
|------------------|-------------------------------------|
| `make run`        | Run app locally via Uvicorn         |
| `make test`       | Run tests with Pytest               |
| `make docker-build` | Build the Docker image           |
| `make docker-run`   | Run app inside Docker container   |
| `make docker-shell` | Drop into shell inside container  |

---

## 🔍 Health Check

```
GET /health → 200 OK
```

---

## ✅ Requirements

- Python 3.10+
- Docker (optional)
