import random
import hashlib
import os
from openai import OpenAI

# ✅ Initialize OpenAI client (uses environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ------------------ Question Generator ------------------

class QuestionGenerator:

    def generate_questions(self, candidate_id, domain, difficulty, count):

        prompt = f"""
        Generate {count} unique interview questions for the domain {domain}.
        Difficulty level: {difficulty}.
        Questions should be technical and suitable for job interviews.
        Return only the questions as a numbered list.
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You generate technical interview questions."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )

            text = response.choices[0].message.content

            questions = []
            for line in text.split("\n"):
                line = line.strip()
                if line and any(char.isalnum() for char in line):
                    questions.append(line)

            return questions

        except Exception as e:
            print("API Error:", e)
            return [f"Error generating {difficulty} questions"]


# ------------------ Randomization Engine ------------------

class RandomizationEngine:

    def __init__(self, structure):
        self.structure = structure

    def generate_seed(self, candidate_id, domain):
        seed_str = f"{candidate_id}_{domain}"
        return int(hashlib.sha256(seed_str.encode()).hexdigest(), 16) % (10**8)

    def randomize_questions(self, candidate_id, domain, question_bank):

        random.seed(self.generate_seed(candidate_id, domain))

        selected_questions = []

        for difficulty, count in self.structure.items():
            pool = question_bank[difficulty]

            if len(pool) >= count:
                chosen = random.sample(pool, count)
            else:
                chosen = pool  # fallback if not enough questions

            selected_questions.extend(chosen)

        random.shuffle(selected_questions)

        return selected_questions


# ------------------ Difficulty Structure ------------------

STRUCTURE = {
    "easy": 3,
    "medium": 3,
    "hard": 3
}


# ------------------ Integration ------------------

generator = QuestionGenerator()
randomizer = RandomizationEngine(STRUCTURE)


# ------------------ Candidate Input ------------------

candidate_id = input("Enter Candidate ID: ")

print("\nAvailable Domains:")
print("Python")
print("Java")
print("Artificial Intelligence")
print("Data Science")

domain = input("\nChoose Domain: ")


# ------------------ Generate Question Pool ------------------

question_pool = {}

for difficulty, count in STRUCTURE.items():

    generated_questions = generator.generate_questions(
        candidate_id,
        domain,
        difficulty,
        count + 3   # extra buffer
    )

    question_pool[difficulty] = generated_questions


# ------------------ Randomization ------------------

domain_questions = randomizer.randomize_questions(
    candidate_id,
    domain,
    question_pool
)


# ------------------ Final Question Set ------------------

final_questions = []

# Fixed intro question
final_questions.append("Tell me about yourself")

# Add randomized questions
final_questions.extend(domain_questions)


# ------------------ Output ------------------

print("\nGenerated Question Set")
print("Candidate:", candidate_id)
print("Domain:", domain)

print("\nQuestions:\n")

for i, q in enumerate(final_questions, 1):
    print(f"{i}. {q}")