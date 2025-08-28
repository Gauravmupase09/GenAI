# 🤖 Integrating a Chatbot with FastAPI  

This project demonstrates how to build and integrate a **chatbot backend with FastAPI** and a **frontend using Streamlit**.  
The chatbot uses **Groq API** (`llama-3.1-8b-instant` model) for real-time streaming responses.  

---

## 📂 Project Structure  

├── app.py # FastAPI backend (API endpoint for chatbot streaming)
├── chatbot.py # Chatbot logic (connects to Groq API)
├── frontend.py # Streamlit frontend interface
├── requirements.txt # Dependencies
├── .env # API keys and environment variables
├── .gitignore # Ignore venv, cache, and env files

---

## ⚙️ Setup Instructions  

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/fastapi-chatbot.git
cd fastapi-chatbot

2. Create and activate virtual environment
bash
python -m venv .venv

On Windows
bash
.venv\Scripts\activate

On Mac/Linux
bash
source .venv/bin/activate

3. Install dependencies
bash
pip install -r requirements.txt

4. Configure environment variables
Create a .env file in the project root and add your Groq API key:
GROQ_API_KEY=your_api_key_here
(Included in .gitignore so it won’t be pushed to GitHub)

5. Run FastAPI backend
bash
uvicorn app:app --reload
Backend will start at:
👉 http://127.0.0.1:8000/chat/stream

6. Run Streamlit frontend
In a new terminal (with venv activated):
bash
streamlit run frontend.py
Frontend will open in your browser at:
👉 http://localhost:8501

🛠 How It Works
chatbot.py → Connects to Groq API and streams responses token-by-token.

app.py → Provides a FastAPI endpoint (/chat/stream) that streams chatbot replies.

frontend.py → A Streamlit-based UI where users can chat with the bot in real-time.

📦 Dependencies
Listed in requirements.txt:

fastapi + uvicorn → Backend API

streamlit → Frontend UI

requests → Streaming response handling in frontend

groq → Groq API client

python-dotenv → Load environment variables

🚀 Demo Workflow
User enters a message in Streamlit chat UI.

The message is sent to the FastAPI backend.

FastAPI streams the Groq model’s response back to frontend.

Streamlit displays the response incrementally in real-time.

🔒 Security
.env file is ignored via .gitignore to keep API keys safe.

Never expose your GROQ_API_KEY in public repositories.

📜 License
This project is open-source and available under the MIT License.
