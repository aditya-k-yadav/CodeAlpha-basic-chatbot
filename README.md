# 🤖 Chatbot 

A smart offline chatbot built using Python that simulates human-like conversation using rule-based logic, intent detection, and a built-in knowledge base. It runs entirely in the terminal and does not require any external APIs or internet connection.

---

## 🚀 Features

- 💬 Handles daily conversation (hello, how are you, etc.)
- 🧠 Intent detection using keyword mapping
- 📚 Built-in knowledge base (Python, tech, general knowledge)
- 📝 Remembers user name using JSON file (memory system)
- ⏰ Tells current time
- 😂 Tells random jokes
- 🔍 Smart fallback using similarity matching
- ⚡ Fully offline (no API, no internet required)

---

## 🧠 Example Capabilities

### 💡 General Chat
- "hello" → Hi there!
- "how are you" → I'm doing great!

### 🐍 Python Knowledge
- "what is python" → Explanation of Python
- "what is loop" → Explanation of loops
- "what is function" → Explanation of functions

### 🌍 General Knowledge
- "earth" → Information about Earth
- "india" → Information about India

### 😂 Fun Features
- "tell me a joke" → Random programming joke

### 🧠 Memory Feature
- "my name is xyz" → Stores name
- "what is my name" → Recalls name

---

## 🛠️ Concepts Used

- Object-Oriented Programming (OOP)
- Dictionaries for knowledge base
- String processing
- File handling (JSON for memory)
- Intent detection using keyword matching
- Fuzzy matching using difflib
- Loops and conditionals

---

## ▶️ How to Run (Anaconda + VS Code)

### 1. Install Anaconda
Download from: https://www.anaconda.com/download

### 2. Create project folder
Place `chatbot.py` inside a folder.

### 3. (Optional) Create virtual environment
Open Anaconda Prompt:
```bash
conda create -n chatbot python=3.11
conda activate chatbot

### Run the Chatbot
 
 python chatbot.py


💡 How to Use
Run the program

1. Type messages like: hello, what is python, tell me a joke, my name is xyz
2. Type bye to exit


## 📜 License

MIT

---

## ⭐ Support

If you found this project useful:

* Give it a ⭐ on GitHub

