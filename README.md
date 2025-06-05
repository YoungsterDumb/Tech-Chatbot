# 🚀 Tech-Chatbot

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/github/license/YoungsterDumb/Tech-Chatbot)](LICENSE)
[![Issues](https://img.shields.io/github/issues/YoungsterDumb/Tech-Chatbot)](https://github.com/YoungsterDumb/Tech-Chatbot/issues)

---

> **Tech-Chatbot** is an AI-powered chatbot for technology Q&A, leveraging large language models (LLMs) and a custom knowledge base. Ask questions about technology and get accurate, document-based answers instantly!

---

## ✨ Features

- 🖥️ **Modern Web Interface**: Built with Flask, HTML, CSS, and JavaScript
- 🤖 **LLM Integration**: Supports HuggingFace, Mistral, and more
- 🔍 **Vector Search**: Fast, relevant answers using FAISS
- 🌐 **Multilingual**: Vietnamese and English support
- 📄 **Document-based**: Answers are grounded in your own PDF knowledge base

---

## 📦 Installation

### 1. Clone the project
```bash
git clone https://github.com/YoungsterDumb/Tech-Chatbot.git
cd Tech-Chatbot
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/MacOS
.venv\Scripts\activate   # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```env
HF_TOKEN=your_huggingface_token
```

### 5. Prepare your data
- Place your PDF documents in the `data/` folder.
- Run the vectorization script if needed to generate the FAISS database.

### 6. Run the application
```bash
python main.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 💡 Usage

- Type your technology-related question in the chat box and click **Send**.
- The bot will answer based on the content of your uploaded documents.
- Use the **🗑️ Clear chat history** button to reset the conversation.

---

## 🤝 Contributing

Pull requests and issues are welcome! If you have ideas, bug reports, or want to add features, feel free to contribute.

- Fork this repo
- Create a new branch
- Make your changes
- Submit a pull request

---

## 📬 Contact

- GitHub: [YoungsterDumb](https://github.com/YoungsterDumb)

---

## ⚠️ Security Note

> **Never commit your `.env` file or API tokens to git.**
> Your HuggingFace token should always be kept private.
