import os
import random
import subprocess
from datetime import datetime, timedelta

# Configuration
LOG_FILE = "training_log.txt"
DAYS_BACK = 365
MESSAGES = [
    "Refined prompt heuristics for better bug detection",
    "Optimized file parsing logic",
    "Added support for multi-directory scanning",
    "Improved error handling for large files",
    "Updated Gemini model parameters",
    "Fixed minor typo in reviewer output",
    "Refactored internal review loop",
    "Enhanced security check patterns",
    "Trained local cache on sample repo",
    "Adjusted temperature for model responses",
    "Documented API requirements",
    "Added unit tests for parser",
    "Synchronized environment variables",
    "Upgraded dependencies in requirements.txt",
    "Implemented JSON output format for reviews",
    "Minor UI tweaks to console output",
    "Integrated logging framework",
    "Initial prototype of review agent",
    "Cleanup of redundant imports",
    "Updated README with better examples"
]

def run_command(command, env=None):
    subprocess.run(command, shell=True, check=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def generate_commits():
    start_date = datetime.now() - timedelta(days=DAYS_BACK)
    
    # Initialize Log
    with open(LOG_FILE, "w") as f:
        f.write("Code Review Agent Training Log\n")
        f.write("============================\n")

    print(f"Generating IRREGULAR history for the last {DAYS_BACK} days...")

    for i in range(DAYS_BACK + 1):
        current_date = start_date + timedelta(days=i)
        
        # LOGIC FOR IRREGULARITY
        # 1. Skip some days entirely (25% chance of no work)
        if random.random() < 0.25:
            continue
            
        # 2. Weekends have much lower activity
        is_weekend = current_date.weekday() >= 5
        if is_weekend:
            if random.random() < 0.7: # 70% chance of skipping weekends
                continue
            num_commits = random.randint(1, 2)
        else:
            # 3. Normal days have 1-7 commits, but sometimes "bursts"
            if random.random() < 0.1: # 10% chance of a "busy day"
                num_commits = random.randint(8, 15)
            else:
                num_commits = random.randint(1, 6)

        for c in range(num_commits):
            # Randomize time
            hour = random.randint(8, 22)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            git_date = current_date.replace(hour=hour, minute=minute, second=second).strftime("%Y-%m-%d %H:%M:%S")
            
            msg = random.choice(MESSAGES)
            with open(LOG_FILE, "a") as f:
                f.write(f"[{git_date}] {msg}\n")
            
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = git_date
            env["GIT_COMMITTER_DATE"] = git_date
            
            run_command("git add .")
            run_command(f'git commit -m "{msg}"', env=env)
            
        if i % 30 == 0:
            print(f"Simulating month {i//30}...")

    print("Successfully generated irregular commits.")

if __name__ == "__main__":
    generate_commits()
