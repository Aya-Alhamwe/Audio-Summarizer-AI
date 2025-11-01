 
-----

# 🤖 AI Meeting Companion

A smart application, built by **Aya Alhamwi**, that transcribes and summarizes meeting audio files. This tool uses `Gradio` for the user interface, `OpenAI's Whisper` for speech-to-text, and a locally-run `Llama 3` (via Ollama) for analysis and summarization.

The application intelligently detects the language of the audio (Arabic or English) and provides a clean, summarized output in the same language.

## ✨ Features

  * **Accurate Transcription:** Uses `openai/whisper-small` for high-quality speech-to-text.
  * **AI Summarization:** Leverages the power of `Llama 3` to analyze the transcript and extract key points and decisions.
  * **Multilingual Support:** Automatically detects Arabic or English and selects the appropriate language model chain.
  * **100% Local & Private:** All AI processing (both STT and LLM) runs entirely on your local machine using your own hardware (CPU/GPU). No API keys or cloud services are required.
  * **Clean Interface:** A simple and intuitive UI built with `Gradio`.

-----

## 🛠️ Technology Stack

  * **Frontend (UI):** `Gradio`
  * **Speech-to-Text (STT):** `OpenAI Whisper` (via `transformers`)
  * **Large Language Model (LLM):** `Meta Llama 3` (via `Ollama`)
  * **Orchestration:** `LangChain`
  * **Core:** `Python`

-----

## 📂 Project Structure

Here is the file structure of the project, designed for clarity and scalability:

```
Business-AI-Companion/
│
├── .gitignore              # Ignores files that shouldn't be on GitHub
├── requirements.txt      # Lists all required Python libraries
├── config.py             # Main configuration file (model names, prompts)
├── app.py                # The main application file (Gradio UI & orchestration)
│
└── services/
    ├── __init__.py
    ├── stt_service.py      # Handles all Speech-to-Text (Whisper) logic
    └── llm_service.py      # Handles all LLM (Ollama/Llama 3) logic
```

-----

## 🚀 Installation & Setup Guide

Follow these steps precisely to set up and run the project on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.10+:** [Download Python](https://www.python.org/downloads/)
2.  **Git:** [Download Git](https://www.google.com/search?q=https://git-scm.com/downloads)
3.  **FFmpeg:** (Required by Whisper)
      * On Windows (using PowerShell): `winget install ffmpeg`
4.  **Ollama:** (Required to run Llama 3)
      * [Download Ollama](https://ollama.com/) and install it.

### Step 1: Download Llama 3

After installing Ollama, you must pull the Llama 3 model. Open your terminal and run:

```bash
ollama run llama3
```

*(Wait for the download (4.7 GB) to complete. You can type `/exit` once it's done).*

### Step 2: Clone & Set Up the Project

1.  **Clone the Repository:**

    ```bash
    git clone [Your-GitHub-Repo-URL]
    cd Business-AI-Companion
    ```

2.  **Create and Activate Virtual Environment:**

    ```powershell
    # Create the environment
    virtualenv venv

    # Activate the environment (on Windows PowerShell)
    .\venv\Scripts\Activate.ps1
    ```

    *(You should see `(venv)` at the start of your prompt)*

### Step 3: Install Python Dependencies

This project requires a specific setup to use your NVIDIA GPU. **Run these commands in order.**

1.  **Install PyTorch (for NVIDIA GPU / CUDA):**

    ```powershell
    (venv) pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    ```

2.  **Install all other requirements:**

    ```powershell
    (venv) pip install -r requirements.txt
    ```

### Step 4: Run the Application

You are all set\! Make sure your `(venv)` is active and `Ollama` is running in the background.

```powershell
(venv) python app.py
```

Your terminal will show:
`Running on local URL: http://0.0.0.0:7861`

Open **`http://127.0.0.1:7861`** in your browser to use the application.
