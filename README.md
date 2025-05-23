# Summarizer
# 🧠 Chat & PDF Summarizer

This is a full-stack web application that summarizes either user-inputted text (chat) or uploaded PDF documents using Natural Language Processing.

Built with:
- 🧰 **Flask** (Python) for the backend API
- ⚛️ **React** for the frontend interface
- 📄 **PDF parsing** and text summarization tools

---

## 🚀 Features

- 🔤 Paste raw text or upload a `.pdf` file
- ⚡ Generates a concise summary in seconds
- 🔒 Automatically cleans up uploaded files after processing
- 🌐 CORS-enabled for local frontend-backend communication

---

## 📦 Tech Stack

| Layer    | Tech                           |
|----------|--------------------------------|
| Frontend | React, Axios                   |
| Backend  | Flask, Flask-CORS              |
| NLP      | Custom summarization logic     |
| Parsing  | `PyMuPDF`, `pdfminer`, etc.    |

---

## 📁 Project Structure
```
chat-summarizer/
├── backend/
│   ├── Dockerfile            # Flask Dockerfile
│   ├── endpoints.py
│   ├── parse.py
│   ├── summarize.py
│   ├── uploads/
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile            # React Dockerfile
│   ├── src/
│   │   ├── App.js
│   │   └── App.css
│   ├── package.json
│   ├── package-lock.json
│   └── build/                # Generated by the build step
├── docker-compose.yml        # Docker Compose file
├── README.md
```


---

## 🛠️ Setup Instructions
## Without docker
### 1. Backend (Flask)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python endpoints.py
```
### 2. Frontend (React.js)
cd frontend
npm install
npm start


### 3. Ollama (llm-backend)
```
curl https://ollama.ai/install.sh | sh
```
```
ollama pull mistral
ollama run mistral
```
## With Docker 
```docker-compose up```






