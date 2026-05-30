# AI Teacher Chatbot 🤖📚

An AI-powered educational chatbot built using **Python, Streamlit, Hugging Face, LangChain, and Transformers** that helps students ask questions and receive intelligent responses in real time.

This project was built to explore practical AI application development, NLP integration, and real-world debugging workflows used in modern software engineering.

---

# 🚀 Live Project

## GitHub Repository

[AI Teacher Chatbot Repository](https://github.com/Itzshambhav/AI-Teacher-Chatbot?utm_source=chatgpt.com)

## GitHub Profile

[Shambhav Kumar GitHub Profile](https://github.com/Itzshambhav?utm_source=chatgpt.com)

---

# 📌 Project Overview

The AI Teacher Chatbot acts like a virtual teaching assistant capable of answering academic questions through an interactive web interface.

The chatbot was developed using:

* Streamlit for frontend UI
* Hugging Face API for AI model integration
* LangChain for conversational workflow
* Transformers and PyTorch for NLP support

This project helped in understanding:

* AI model integration
* API handling
* Dependency management
* Virtual environments
* Python package compatibility
* Real-world debugging

---

# ✨ Features

* 💬 Interactive AI chatbot interface
* 📚 Educational question answering
* ⚡ Real-time responses
* 🌐 Streamlit web application
* 🔐 Environment variable security using `.env`
* 🤖 Hugging Face AI model integration
* 🧠 Conversational AI workflow using LangChain
* 🛠️ Modular Python project structure

---

# 🛠️ Tech Stack

| Technology   | Purpose                         |
| ------------ | ------------------------------- |
| Python 3.11  | Core programming language       |
| Streamlit    | Frontend web app                |
| Hugging Face | AI model API                    |
| LangChain    | Conversation pipeline           |
| Transformers | NLP model support               |
| PyTorch      | Deep learning backend           |
| dotenv       | Environment variable management |

---

# 📂 Project Structure

```bash
AI-Teacher-Chatbot/
│
├── teachers.py
├── requirements.txt
├── .env
├── README.md
└── venv311/
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Itzshambhav/AI-Teacher-Chatbot.git
cd AI-Teacher-Chatbot
```

---

## 2️⃣ Create Virtual Environment

```bash
py -3.11 -m venv venv311
```

Activate environment:

### Windows

```bash
.\venv311\Scripts\Activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Install additional required packages:

```bash
pip install langchain==0.1.0
pip install langchain-huggingface
pip install torch torchvision torchaudio
```

---

## 4️⃣ Create `.env` File

Create a `.env` file inside the project directory and add:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

---

## 5️⃣ Run Application

```bash
streamlit run teachers.py
```

The application will run on:

```bash
http://localhost:8501
```

---

# 🧩 Challenges Faced During Development

This project involved solving several real-world software engineering and AI development issues.

## 🔹 Python Compatibility Issues

Initially, the project was configured using Python 3.14, but several AI libraries were incompatible with the latest version.

Problems faced:

* Pillow installation failure
* NumPy build issues
* Streamlit dependency conflicts

### Solution:

Downgraded environment to Python 3.11 for stable AI library support.

---

## 🔹 LangChain Version Conflicts

The project code was written using older LangChain imports, but the latest LangChain version had breaking changes.

Error faced:

```python
ModuleNotFoundError: No module named 'langchain.chains'
```

### Solution:

Installed a compatible LangChain version:

```bash
pip install langchain==0.1.0
```

---

## 🔹 Hugging Face API Integration

The chatbot required secure API token integration.

### Solution:

* Generated Hugging Face API token
* Configured `.env` file
* Connected chatbot to AI model API securely

---

## 🔹 Virtual Environment Management

Multiple environments caused package conflicts during installation.

### Solution:

Created a dedicated Python 3.11 virtual environment for dependency isolation.

---

# 📖 What I Learned

This project helped me gain practical experience in:

* AI chatbot development
* NLP workflows
* Python environment management
* API integration
* Debugging package conflicts
* Streamlit web applications
* Dependency resolution
* Real-world software engineering practices

---

# 🎯 Future Improvements

* 🎤 Voice input support
* 🧠 Multiple AI model integration
* 💾 Chat history storage
* 🔐 User authentication
* ☁️ Cloud deployment
* 📄 PDF/document question answering
* 🌍 Multi-language support

---

# 📸 Screenshots

*Add chatbot screenshots here*

---

# 👨‍💻 Author

## Shambhav Kumar

Passionate about:

* Artificial Intelligence
* Machine Learning
* Software Development
* AI-based Educational Systems

GitHub:
[Itzshambhav GitHub](https://github.com/Itzshambhav?utm_source=chatgpt.com)

---

# ⭐ Conclusion

The AI Teacher Chatbot project was built not only to create an AI-powered educational assistant but also to gain hands-on experience with modern AI development tools and debugging workflows.

The project involved solving real dependency conflicts, environment setup issues, API integration problems, and AI framework compatibility challenges — closely reflecting practical software engineering scenarios used in industry-level development.
