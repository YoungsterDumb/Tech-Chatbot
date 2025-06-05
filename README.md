# Tech-Chatbot

## Overview
Tech-Chatbot is an AI-powered chatbot for technology Q&A, leveraging large language models (LLMs) and a custom knowledge base. This application allows users to ask questions about technology topics and receive accurate answers extracted from provided documents.

- Modern, user-friendly web interface (Flask + HTML/CSS/JS)
- Integrated LLM (HuggingFace, Mistral, etc.)
- Vector-based information retrieval (FAISS)

## Installation

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

### 3. Install required modules
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file and add your HuggingFace API Token
```env
HF_TOKEN=your_huggingface_token
```

### 5. Prepare your data
- Place your PDF documents in the `data/` folder.
- Run the script to generate the FAISS vector database (if needed).

### 6. Run the application
```bash
python main.py
```
Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Usage
- Enter your technology-related question in the chat box and click "Send".
- The bot will answer based on the content of the provided documents.
- You can clear the chat history using the "🗑️ Clear chat history" button.

## Contributing & Contact
- Pull requests and issues are welcome!
- Contact: [github.com/YoungsterDumb](https://github.com/YoungsterDumb)

---
**Security Note:** Never commit your `.env` file or API tokens to git. Your HuggingFace token should always be kept private.