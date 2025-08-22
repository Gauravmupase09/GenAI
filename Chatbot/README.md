# 🤖 Groq Chatbot

A simple and interactive chatbot using **Groq API** with **LLaMA-3.1**, built in **Python** and **Streamlit**.  
The bot streams responses live, creating a smooth “typing effect” for realistic interaction.

---

## 🚀 Features

- Real-time chat using **streaming responses** from Groq.
- Easy configuration via `.env` for **API key security**.
- Interactive UI built with **Streamlit**.
- Supports long responses with adjustable parameters like `temperature`, `max_completion_tokens`, and `top_p`.
- Fully local: no database required.

---

## 🛠 Project Structure

Chatbot/
│── .env # Stores GROQ_API_KEY
│── app.py # Main Streamlit chatbot code
│── requirements.txt # Project dependencies
│── .gitignore # Ignore sensitive and temporary files

---

## ⚡ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/groq-chatbot.git
cd groq-chatbot

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt

Add your Groq API key in .env:
GROQ_API_KEY=gsk_your_api_key_here

💻 Run the Chatbot
streamlit run app.py
Open the link shown in the terminal (default: http://localhost:8501)
Start chatting with the bot!

⚙️ Customization
You can tune the bot’s responses by changing:

Parameter	Description	Example
temperature -->	Creativity/randomness of the response	--> 0.7
max_completion_tokens	--> Maximum length of response (in tokens)	--> 512
top_p	--> Focus/diversity of vocabulary	--> 0.95
stream --> Enable live incremental responses	--> True

🧹 .gitignore Highlights
.env → Hides your Groq API key
__pycache__/ → Ignore Python cache files
venv/ → Ignore virtual environment

📌 Notes
Currently implemented in Streamlit.
FastAPI or LangChain integration can be added later for more advanced functionality.
Streaming mode shows the bot’s response token by token, creating a “typing effect.”

📜 License
This project is open-source and available under the MIT License.

✨ Author
Gaurav Upase
AI & Data Science Student
