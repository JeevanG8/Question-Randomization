🎯 Interview Question Generation & Randomization System
📌 Overview

This project is a Python-based interview system that generates domain-specific questions using the OpenAI API and applies a deterministic randomization algorithm to ensure each candidate receives a unique yet structured question set.

🚀 Features

AI-generated technical interview questions

Unique question set per candidate (based on Candidate ID + Domain)

Fixed first question: "Tell me about yourself"

Balanced difficulty distribution:

Easy (3)

Medium (3)

Hard (3)

Deterministic randomization using SHA-256 seed

Dynamic question pool generation with buffer

🛠️ Technologies Used

Python 3

OpenAI API (gpt-4o-mini)

Built-in libraries:

random

hashlib

os

📂 Project Structure
├── Question randomization.py   # Main script
├── README.md                  # Project documentation
⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install Dependencies
pip install openai
3. Configure API Key

Set your OpenAI API key as an environment variable:

Linux / Mac:

export OPENAI_API_KEY="your_api_key_here"

Windows:

set OPENAI_API_KEY=your_api_key_here
▶️ Usage

Run the script:

python "Question randomization.py"
Input:

Candidate ID

Domain (Python, Java, AI, Data Science)

Output:

10 questions:

1 fixed introduction question

9 randomized technical questions

🧠 System Workflow

Question Generation

Generates questions per difficulty level using OpenAI API

Adds extra buffer questions to ensure sufficient pool

Seed Generation

Uses SHA-256 hash of:

candidate_id + domain

Ensures reproducible randomness

Randomization Engine

Selects questions per difficulty

Shuffles final question set

Final Output

Prepends fixed question

Displays structured interview set

🔑 Key Design Principle

Same Candidate ID + Domain → Same Questions

Different Candidate ID → Different Questions

Ensures fairness + uniqueness in assessments

📊 Example Output
Generated Question Set
Candidate: 101
Domain: Python

1. Tell me about yourself
2. What is a Python list?
3. Explain decorators
...
⚠️ Notes

Requires a valid OpenAI API key

Internet connection is required for question generation

Model used: gpt-4o-mini

🤝 Contributing

Contributions are welcome! Feel free to fork and enhance the system.

📜 License

This project is licensed under the MIT License.
