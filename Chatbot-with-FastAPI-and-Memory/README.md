# 🤖 Chatbot with FastAPI & Memory  

A simple yet powerful chatbot application built with **FastAPI (backend)** and **Streamlit (frontend)**.  
It uses **session memory** to store conversation history, making interactions more natural and context-aware.  

---

```
## 📂 Project Structure  

Chatbot-with-FastAPI-and-Memory/
│
├── Backend/
│ ├── app.py → Main FastAPI app (entry point for backend server)
│ ├── chatbot.py → Handles chatbot logic (calls LLM API, processes response)
│ ├── memory.py → Stores conversation history (session memory)
│ └── models.py → Defines request/response data structures (Pydantic models)
│
├── Frontend/
│ └── frontend.py → Simple frontend (Streamlit) to chat with backend
│
├── .env → Stores API keys & secrets (not shared publicly)
├── .gitignore → Ignore files like .env, venv/, __pycache__/
├── README.md → Project documentation
└── requirements.txt → Python dependencies

---

## 🚀 Features  

- ⚡ **FastAPI Backend** → Handles chatbot API requests efficiently.  
- 💬 **Session Memory** → Remembers previous messages in the conversation.  
- 🎨 **Frontend (Streamlit)** → Clean UI to interact with the chatbot.  
- 🔒 **Environment Variables** → Securely store API keys in `.env`.  
- 📦 **Modular Code** → Separate files for models, memory, chatbot logic.  

---

## 🛠️ Installation  
1️⃣ Clone the Repository  
bash
git clone https://github.com/your-username/Chatbot-with-FastAPI-and-Memory.git
cd Chatbot-with-FastAPI-and-Memory

2️⃣ Create Virtual Environment
bash
Copy code
python -m venv .venv

Activate it:
Windows (PowerShell):
bash
Copy code
.venv\Scripts\activate

Linux/Mac:
bash
Copy code
source .venv/bin/activate

3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt

4️⃣ Setup Environment Variables
Create a .env file in the project root:
ini
Copy code
API_KEY=your_api_key_here

---

▶️ Running the Project
Start Backend (FastAPI)
bash
Copy code
cd Backend
uvicorn app:app --reload
Backend will run at → http://127.0.0.1:8000

Start Frontend (Streamlit)
bash
Copy code
cd Frontend
streamlit run frontend.py
Frontend will run at → http://localhost:8501

---

📡 API Endpoints
1. Chat Endpoint
POST /chat

Request Body:
json
Copy code
{
  "session_id": "123",
  "message": "Hello!"
}

Response:
json
Copy code
{
  "response": "Hi! How can I help you today?",
  "history": [
    {"user": "Hello!", "bot": "Hi! How can I help you today?"}
  ]
}

2. Health Check
GET /health
Response:
json
Copy code
{"status": "ok"}

---

🧠 Memory Management
Each user has a session_id that keeps track of conversation history.
The memory.py file stores messages in a dictionary:

python
Copy code
{
  "123": [
    {"user": "Hello", "bot": "Hi there!"},
    {"user": "Tell me a joke", "bot": "Why don’t skeletons fight? They don’t have guts."}
  ]
}
This makes the chatbot context-aware.

---

📸 Demo Preview
Backend running on FastAPI
Frontend with Streamlit simple chat UI

---

📌 Future Improvements
✅ Add database support for persistent memory (Redis/Postgres).
✅ Enhance UI (Gradio/React frontend).
✅ Multi-user memory handling with authentication.
✅ Support for multiple LLMs (OpenAI, Groq, Anthropic).

---

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

---

📜 License
This project is licensed under the MIT License.
