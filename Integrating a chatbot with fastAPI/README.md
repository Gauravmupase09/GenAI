🤖 Integrating a Chatbot with FastAPI

This project demonstrates how to build and integrate a chatbot backend with FastAPI and a frontend using Streamlit. The chatbot uses Groq API (llama-3.1-8b-instant model) for real-time streaming responses.

📂 Project Structure
├── app.py             # FastAPI backend (API endpoint for chatbot streaming)
├── chatbot.py         # Chatbot logic (connects to Groq API)
├── frontend.py        # Streamlit frontend interface
├── requirements.txt   # Dependencies
├── .env               # API keys and environment variables
├── .gitignore         # Ignore venv, cache, and env files

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/fastapi-chatbot.git
cd fastapi-chatbot

2. Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Mac/Linux
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the project root and add your Groq API key:

GROQ_API_KEY=your_api_key_here

(already included in .gitignore so it won’t be pushed to GitHub)

5. Run FastAPI backend
uvicorn app:app --reload

This will start the backend at:
👉 http://127.0.0.1:8000/chat/stream

6. Run Streamlit frontend

In a new terminal (with venv activated):

streamlit run frontend.py

The frontend will open in your browser at:
👉 http://localhost:8501

🛠 How It Works

chatbot.py: Connects to Groq API and streams responses token-by-token.

app.py: Provides a FastAPI endpoint (/chat/stream) that streams chatbot replies.

frontend.py: A Streamlit-based UI where users can chat with the bot in real-time.

📦 Dependencies

All dependencies are listed in requirements.txt:

fastapi + uvicorn → Backend API

streamlit → Frontend UI

requests → Streaming response handling in frontend

groq → Groq API client

python-dotenv → Load environment variables

🚀 Demo

User enters a message in Streamlit chat UI.

The message is sent to FastAPI backend.

FastAPI streams the Groq model’s response back to frontend.

Streamlit displays the response incrementally in real-time.

🔒 Security

.env file is ignored via .gitignore to keep API keys safe.

Do not expose your GROQ_API_KEY in public repos.

📜 License

This project is open-source and available under the MIT License.
