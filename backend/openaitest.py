from openai import OpenAI
import dotenv

dotenv.load_dotenv()
client = OpenAI()

user_input = r"Solve: \int x^2 dx"

completion = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4"
    messages=[
        {"role": "system", "content": (
            "You are a math expert. "
            "When the user provides a LaTeX math expression, "
            "solve it step-by-step, and present the final solution in LaTeX format. "
            "Do not add extra explanations or text—just return the math solution."
        )},
        {"role": "user", "content": user_input}
    ]
)

print(completion.choices[0].message.content)

