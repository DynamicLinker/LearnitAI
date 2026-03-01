# 🎓 LearnitAI: Your Personal AI Study Buddy

**LearnitAI** is an AI-powered educational platform designed to bridge the gap between complex lecture content and clear, actionable study notes. Developed as a capstone project for the **AICTE Virtual Internship**, this application leverages Large Language Models (LLMs) and Speech-to-Text technology to provide a seamless, multi-modal learning experience for students.



---

## 🚀 Key Features

* **📄 PDF Notes Simplifier:** Instantly process textbook chapters or lecture slides to generate concise summaries, simplified "Plain English" explanations, or interactive quizzes.
* **🎙️ Audio Lecture Summarizer:** Transcribe recorded lectures (MP3, WAV, AAC, M4a) into text using OpenAI's **Whisper** and convert them into structured bullet points.
* **💬 Interactive AI Tutor:** A dedicated "WhatsApp-style" chat interface for real-time doubt clearing, powered by **Qwen 2.5** and persistent session memory.
* **💻 Hardware Optimized:** Custom logic to force audio processing on the CPU, ensuring the application remains portable and functional on standard laptop hardware.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Web Framework)
* **LLM Engine:** [Hugging Face Inference API](https://huggingface.co/) (Model: `Qwen/Qwen2.5-7B-Instruct`)
* **Speech-to-Text:** [OpenAI Whisper](https://github.com/openai/whisper) (Base Model)
* **PDF Parsing:** [PyPDF2](https://pypi.org/project/PyPDF2/)
* **Environment Management:** `python-dotenv`

---

## ⚙️ Installation & Setup

To run LearnitAI locally, follow these steps:

### 1. Clone the Repository
```sh
git clone [https://github.com/YOUR_USERNAME/LearnitAI.git](https://github.com/YOUR_USERNAME/LearnitAI.git)
cd LearnitAI
```

### 2. Install Required Libraries

    Ensure you have FFmpeg installed on your system, then run:

```sh
pip install -r requirements.txt
```

### 3. Configure Your Environment

Create a .env file in the root directory and add your Hugging Face Access Token:
Plaintext
```sh
HF_TOKEN=hf_your_actual_token_here
```

### 4. Launch the App
```sh
streamlit run app.py
```

### 📁 Project Structure
```
LearnitAI/
├── .env                # Secret API Keys (Excluded via .gitignore)
├── .gitignore          # Prevents sensitive data from being pushed to GitHub
├── app.py              # Main Streamlit UI & Multi-tab Logic
├── ai_engine.py        # LLM integration & Prompt Engineering
├── audio_processor.py  # Audio-to-Text processing via Whisper
├── requirements.txt    # List of project dependencies
└── README.md           # Project documentation
```

### 🛡️ Security & Deployment

* Secrets Management: The project uses a .env file and .gitignore to prevent API key exposure.
* Cloud Ready: When deployed to Streamlit Community Cloud, API tokens are managed via the secure "Secrets" dashboard.
* Session State: Utilizes Streamlit's st.session_state to maintain a persistent chat history, providing a modern conversational experience.


#### Developed by: Ajitesh Chaurasia
