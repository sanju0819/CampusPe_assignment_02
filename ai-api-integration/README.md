<div align="center">

# 🤖 CampusPE Generative AI Assignment

### AI API Integration using Python — Sanjan Gowda N J

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python\&logoColor=white)
![AI APIs](https://img.shields.io/badge/APIs-Generative%20AI-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Providers](https://img.shields.io/badge/AI%20Providers-Multiple-purple?style=for-the-badge)

</div>

---

## 📌 About The Project

This repository contains the implementation of the **CampusPE Generative AI Assignment – AI API Integration**.

The objective of this assignment is to demonstrate how Python programs can interact with **multiple Generative AI providers using APIs**.

Each program connects to a different AI platform, sends user prompts, and retrieves AI-generated responses.

The project focuses on learning:

* AI API integration using Python
* Secure management of API keys
* Sending prompts and processing responses
* Error handling in API-based applications
* Building a unified **multi-provider AI query system**

---

## 🧠 AI Providers Integrated

The project integrates the following AI platforms:

| Provider         | Purpose                                       |
| ---------------- | --------------------------------------------- |
| **Groq**         | Ultra-fast inference using Llama models       |
| **Hugging Face** | Access to open-source generative AI models    |
| **Cohere**       | Text generation using advanced command models |
| **Ollama**       | Running AI models locally on the system       |

Each API demonstrates a different approach to interacting with **large language models (LLMs)**.

---

## 📂 Project Structure

```
ai-api-integration/
│
├── groq_example.py
├── huggingface_example.py
├── cohere_example.py
├── ollama_example.py
├── multi_api_query.py
│
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── groq_output.png
    ├── huggingface_output.png
    ├── cohere_output.png
    ├── ollama_output.png
    └── multi_api_output.png
```

---

## 📋 Programs Overview

| # | File                     | Provider       | Description                                       |
| - | ------------------------ | -------------- | ------------------------------------------------- |
| 1 | `groq_example.py`        | Groq           | Generates AI responses using Llama models         |
| 2 | `huggingface_example.py` | Hugging Face   | Queries open-source AI models                     |
| 3 | `cohere_example.py`      | Cohere         | Generates text responses using Cohere models      |
| 4 | `ollama_example.py`      | Ollama         | Runs a local AI model on the system               |
| 5 | `multi_api_query.py`     | Multi Provider | Allows users to select an AI provider dynamically |

---

## 📊 Assignment Summary

| Feature                  | Description |
| ------------------------ | ----------- |
| AI Providers Integrated  | 4           |
| Python Programs          | 5           |
| API-based Programs       | 3           |
| Local AI Model Execution | 1           |
| Unified Query System     | 1           |

---

## ⚙️ Requirements

* **Python 3.x** — [Download here](https://www.python.org/downloads/)
* Internet connection for API-based providers
* Optional: **Ollama installed** for running local AI models

Required libraries:

```
pip install openai groq cohere requests python-dotenv
```

---

## 🔑 API Configuration

Create a `.env` file in the project root directory.

Example:

```
GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
COHERE_API_KEY=your_cohere_api_key
```

⚠️ **Important:** Never upload your `.env` file to GitHub.

---

## 🚀 Running the Programs

Run each AI integration script individually.

### Run Groq API

```
python groq_example.py
```

### Run HuggingFace API

```
python huggingface_example.py
```

### Run Cohere API

```
python cohere_example.py
```

### Run Ollama Local Model

```
python ollama_example.py
```

---

## 🔄 Multi API Query System

The **multi_api_query.py** program allows the user to select an AI provider and generate responses dynamically.

Run the program:

```
python multi_api_query.py
```

Example interface:

```
Choose AI Provider

1. Groq
2. HuggingFace
3. Cohere
4. Ollama
```

The selected provider processes the prompt and returns the AI-generated output.

---

## 📸 Execution Screenshots

Screenshots demonstrating successful execution of each API program are included in the **screenshots** folder.

| Program         | Screenshot                         |
| --------------- | ---------------------------------- |
| Groq API        | screenshots/groq_output.png        |
| HuggingFace API | screenshots/huggingface_output.png |
| Cohere API      | screenshots/cohere_output.png      |
| Ollama API      | screenshots/ollama_output.png      |
| Multi API Query | screenshots/multi_api_output.png   |

---

## 📝 Notes

* All programs are written in **Python 3**
* Each API was tested using multiple prompts
* Programs include **error handling and structured responses**
* Environment variables are used for **secure API key management**
* The project demonstrates both **cloud-based AI APIs and local AI models**

---

## 👤 Author

<div align="center">

### Sanjan Gowda N J

[![Email](https://img.shields.io/badge/Email-gowdasanjannj%40gmail.com-red?style=for-the-badge\&logo=gmail)](mailto:gowdasanjannj@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sanjan%20Gowda-blue?style=for-the-badge\&logo=linkedin)](https://www.linkedin.com/in/sanjan-gowda-67ba942a3)
[![GitHub](https://img.shields.io/badge/GitHub-sanju0819-black?style=for-the-badge\&logo=github)](https://github.com/sanju0819)

</div>

---

## 🎓 Course

**CampusPE – Generative AI**

Assignment: **AI API Integration**
