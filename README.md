# Code Review Agent

An AI-powered CLI tool to review your code for bugs, performance, and security.

## Features
- Reviews individual files or entire directories.
- Powered by Google Gemini.
- Identifies logical errors and security flaws.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your API key in a `.env` file:
   ```env
   GOOGLE_API_KEY=your_key_here
   ```

## Usage
To review a file:
```bash
python reviewer.py path/to/your/code.py
```

To review a directory:
```bash
python reviewer.py src/
```

