# 🌸 End-to-End Iris Classification MLOps Pipeline

> An enterprise-grade Machine Learning project showcasing an end-to-end MLOps pipeline, REST API serving, and a premium frontend interface for Iris Flower Classification.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-container-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![CI/CD](https://github.com/Shivansh-mishraji/Iris-Flower-Classification/actions/workflows/mlops.yml/badge.svg)](https://github.com/Shivansh-mishraji/Iris-Flower-Classification/actions)

## 📋 Overview

This project elevates the classic Iris Classification dataset from a simple Jupyter Notebook into a **production-ready MLOps architecture**. It is designed to demonstrate proficiency in Full-Stack Web Development, Machine Learning Engineering, and DevOps best practices.

### 🌟 Key Enhancements over standard Notebooks
- **Backend API**: High-performance REST API built with FastAPI and Pydantic for data validation.
- **Frontend UI**: A custom-designed, premium glassmorphism web interface built with vanilla HTML/CSS/JS.
- **MLOps**: Reproducible training scripts (`src/train.py`), model versioning, and rigorous testing (`pytest`).
- **Containerization**: Packaged entirely into Docker with `docker-compose` for seamless, one-click deployments.
- **CI/CD Pipeline**: GitHub Actions automatically lints and tests code upon pushing to ensure a robust `main` branch.

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[Frontend Client (HTML/CSS/JS)] -->|REST POST /predict| B(FastAPI Server)
    B --> C{Pydantic Validation}
    C -->|Valid| D[Inference Engine (src/inference.py)]
    C -->|Invalid| E[422 Error Response]
    D --> F[(Trained Model: iris_log_reg_model.pkl)]
    F -.->|Trained via| G[Training Script (src/train.py)]
    D -->|Predictions & Probabilities| B
    B -->|JSON Response| A
```

---

## 🚀 Quick Start

### Option 1: Docker (Recommended)
You can run the entire application using Docker Compose, which handles all dependencies automatically.
```bash
# Clone the repository
git clone https://github.com/Shivansh-mishraji/Iris-Flower-Classification.git
cd Iris-Flower-Classification

# Build and start the containers
docker-compose up --build
```
1. Open your browser and navigate to the frontend: Open `frontend/index.html` in any browser.
2. View the automatically generated API documentation at: `http://localhost:8000/docs`

### Option 2: Local Python Environment
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
python src/api.py
```
Open `frontend/index.html` to interact with the API.

---

## 📁 Project Structure

```text
📦 Iris-Flower-Classification
 ┣ 📂 .github/workflows     # CI/CD GitHub Actions Pipeline
 ┣ 📂 frontend              # Premium Web UI (HTML, CSS, JS)
 ┃ ┣ 📜 app.js              # Fetch API integration
 ┃ ┣ 📜 index.html          # UI Layout
 ┃ ┗ 📜 style.css           # Glassmorphism Styling
 ┣ 📂 src                   # Source Code
 ┃ ┣ 📜 api.py              # FastAPI Application
 ┃ ┣ 📜 inference.py        # Model loading & prediction logic
 ┃ ┣ 📜 schemas.py          # Pydantic data validation models
 ┃ ┗ 📜 train.py            # Reproducible model training script
 ┣ 📂 tests                 # Automated Tests (pytest)
 ┃ ┣ 📜 test_api.py         # API Endpoint tests
 ┃ ┗ 📜 test_model.py       # Inference logic tests
 ┣ 📜 docker-compose.yml    # Docker orchestration
 ┣ 📜 Dockerfile            # API Container specification
 ┣ 📜 requirements.txt      # Python dependencies
 ┣ 📜 iris_log_reg_model.pkl# Serialized Scikit-learn model
 ┗ 📜 README.md             # Project documentation
```

---

## 🧪 Testing and CI/CD

To run the automated tests locally:
```bash
pytest tests/ -v
```

Every push to the repository triggers a GitHub Action (`.github/workflows/mlops.yml`) that sets up the environment, installs dependencies, and runs the `pytest` suite to ensure no breaking changes are merged.

---

## 🎯 Interview Preparation / Knowledge Base
An in-depth document explaining architectural choices (Why FastAPI? Why Docker?), potential cross-questioning, and design rationales has been prepared. Please refer to the `interview_prep.md` artifact generated alongside this project.

## 📄 License
MIT License - See LICENSE file for details.
