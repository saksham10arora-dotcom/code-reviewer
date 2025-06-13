import os
import sys
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

def review_code(file_path):
    """Reviews the content of a single file using Google Generative AI."""
    if not API_KEY:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        return

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro')

    try:
        with open(file_path, 'r') as f:
            code = f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return

    prompt = f"""
    You are an expert senior software engineer and code reviewer. 
    Please review the following code for:
    1. Potential bugs or logical errors.
    2. Performance optimizations.
    3. Readability and adherence to best practices.
    4. Security vulnerabilities.

    Provide a structured response with clear headings.

    Code to review ({file_path}):
    ```python
    {code}
    ```
    """

    print(f"--- Reviewing {file_path} ---")
    response = model.generate_content(prompt)
    print(response.text)
    print("-" * 30)

def main():
    parser = argparse.ArgumentParser(description="AI Code Review Agent")
    parser.add_argument("path", help="Path to the file or directory to review")
    args = parser.parse_args()

    if os.path.isfile(args.path):
        review_code(args.path)
    elif os.path.isdir(args.path):
        for root, dirs, files in os.walk(args.path):
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.go', '.cpp', '.h')):
                    full_path = os.path.join(root, file)
                    review_code(full_path)
    else:
        print(f"Error: Path {args.path} does not exist.")

if __name__ == "__main__":
    main()
