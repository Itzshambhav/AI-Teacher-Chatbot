# AI-Chatbot-Teacher

An intelligent **AI Teacher** built with **Streamlit** and **Hugging Face's LLaMA 3.1 8B Instruct** model.  
This chatbot can answer questions in **all languages**, making it perfect for global learning environments.


## Features
- **Interactive Chat Interface** – Ask questions and get instant answers.
- **Multilingual Support** – Ask questions in any language and get accurate responses.
- **Conversation History** – Keeps track of all previous messages.
- **Built with LangChain** – Uses AI-powered text generation.
- **Streamlit UI** – Simple, user-friendly web interface.

## Installation
### Clone the Repository
git clone https://github.com/sahil22011/teachers-ai.git
cd teachers-ai
### Install Dependencies
pip install -r requirements.txt
### Set Up Hugging Face API Key
Create a .env file and add:
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key_here
### Run the Streamlit app:
streamlit run teachers.py
# AI Teacher Chatbot 🤖📚

An intelligent AI-powered Teacher Chatbot built using **Python, Streamlit, Hugging Face, and LangChain**.
This chatbot helps students ask questions and receive AI-generated educational responses in an interactive interface.

---

# 🚀 Features

* AI-powered question answering
* Interactive chatbot interface using Streamlit
* Hugging Face model integration
* Clean and simple UI
* Real-time responses
* Environment variable support using `.env`
* Beginner-friendly project structure

---

# 🛠️ Technologies Used

* Python 3.11
* Streamlit
* Hugging Face API
* LangChain
* Transformers
* PyTorch

---

# 📂 Project Structure

```bash
AI Teacher Chatbot/
│
├── teachers.py
├── requirements.txt
├── .env
├── README.md
└── venv311/
```

---

# ⚡ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-Teacher-Chatbot.git
cd AI-Teacher-Chatbot
```

---

## 2️⃣ Create Virtual Environment

```bash
py -3.11 -m venv venv311
```

Activate virtual environment:

### Windows

```bash
.\venv311\Scripts\Activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Install additional packages:

```bash
pip install langchain==0.1.0
pip install langchain-huggingface
pip install torch torchvision torchaudio
```

---

## 4️⃣ Create `.env` File

Create a `.env` file in the project directory and add:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

---

## 5️⃣ Run the Application

```bash
streamlit run teachers.py
```

The application will open at:

```bash
http://localhost:8501
```

---

# 🧠 Challenges Faced During Development

While building this project, several real-world development challenges were encountered and solved:

* Python 3.14 compatibility issues with AI libraries
* Pillow and NumPy installation failures
* LangChain version incompatibility
* Streamlit dependency conflicts
* Hugging Face API token setup
* Virtual environment configuration
* PyTorch installation and configuration

These issues were resolved by:

* Switching to Python 3.11
* Managing dependencies carefully
* Using compatible LangChain versions
* Setting up isolated virtual environments

This project helped in learning practical software engineering and debugging skills used in real AI development workflows.

---

# 📸 Output

The chatbot provides AI-generated educational responses through an interactive web interface built with Streamlit.

---

# 🎯 Future Improvements

* Add voice assistant support
* Add multiple AI models
* Save chat history
* Add authentication system
* Deploy online using Streamlit Cloud or Render
* Add PDF/document question answering

---

# 👨‍💻 Author

Shambhav Kumar

---

# ⭐ Conclusion

This project demonstrates practical implementation of:

* AI integration
* NLP applications
* API handling
* Frontend + backend integration
* Real-world debugging and dependency management

It was built as a learning project to explore modern AI application development.


