# 🚀 Daily Content Generator (AI-Powered)

A modular Python automation tool that generates high-quality, SEO-optimized technical blog posts in bulk using Google's Gemini API. It reads topics from a CSV file and outputs formatted Markdown files ready for publication.

## ✨ Features

- **Bulk Processing:** Generates unlimited blog posts from a single CSV queue.
- **Modular Architecture:** Clean separation between logic, API services, and file handling.
- **Professional Formatting:** Outputs articles with H1-H3 tags, tables, and code blocks.
- **Smart Context:** Configurable tone, audience, and word count for every topic.
- **Security First:** Uses .env files to keep API keys safe.

---

## 🛠️ Prerequisites

Before running the project, ensure you have:

- Python 3.8+ installed.
- A Google Gemini API Key (Get it free from Google AI Studio).

---

## ⚙️ Installation & Setup

Follow these steps to set up your local environment.

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd daily-content-generator
```

### 2. Create a Virtual Environment

This isolates your project dependencies from your system Python.

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Mac / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required libraries (Google GenAI, Pandas, Dotenv).

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

### 1. Set up Environment Variables

Create a file named `.env` in the root directory.

Paste your API key inside:

```
GEMINI_API_KEY=your_actual_api_key_here
```

> ⚠️ IMPORTANT: Never commit `.env` to GitHub. It is added to `.gitignore` by default.

### 2. Prepare the Topic Queue

Create a `topics.csv` file in the root directory. It must have the following headers:

```
Topic,Tone,Target Audience,Word Limit
Python Decorators,Educational,Junior Developers,800
Docker vs Kubernetes,Technical,DevOps Engineers,1500
React Hooks Guide,Tutorial,Frontend Devs,1000
```

Example `topics.csv` content:

```
Topic,Tone,Target Audience,Word Limit
Python Decorators,Educational,Junior Developers,800
Docker vs Kubernetes,Technical,DevOps Engineers,1500
React Hooks Guide,Tutorial,Frontend Devs,1000
```

---

## 🚀 Usage

Run the main script to start the generation process:

```bash
python main.py
```

**The Workflow:**

1. The script validates your API key.
2. It loads the `topics.csv` queue.
3. It generates a blog post for each row using Gemini.
4. Files are saved to the `/generated_blogs` folder with timestamped filenames.

---

## 📂 Project Structure

```
daily-content-generator/
├── .env                 # Secrets (API Key) - DO NOT COMMIT
├── .venv/               # Virtual Environment folder
├── config.py            # Configuration loader
├── file_manager.py      # CSV reading & Markdown saving
├── main.py              # Entry point (The Orchestrator)
├── prompt_builder.py    # Prompt engineering logic
├── services.py          # Google Gemini API interaction
├── topics.csv           # Input data
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🐛 Troubleshooting

**Error:** `ModuleNotFoundError: No module named 'google'`  
**Fix:** You likely forgot to activate your virtual environment or install requirements.  
Run: `pip install -r requirements.txt`

**Error:** `ValueError: GEMINI_API_KEY not found`  
**Fix:** Ensure your `.env` file exists in the root folder and uses the exact variable name `GEMINI_API_KEY`.

**Error:** `429 Resource Exhausted`  
**Fix:** You are hitting the API rate limit. Increase `SLEEP_BETWEEN_CALLS` in `config.py`.

