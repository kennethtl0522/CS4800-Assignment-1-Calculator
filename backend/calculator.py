from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
import uvicorn

load_dotenv()
app = FastAPI()

client = OpenAI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SolveRequest(BaseModel):
    latex: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/solve")
def solve(request: SolveRequest):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4"
    messages=[
                {"role": "system", "content": (
                    "You are a math expert. "
                    "When the user provides a LaTeX math expression work with MathLive <math-field>, "
                    "solve it step-by-step"
                    "Do not add extra explanations or text other than Math. Just return LateX format solution."
                )},
                {"role": "user", "content": request.latex}
            ]
    )  
    return completion.choices[0].message.content
        
    
if __name__ == '__calculator__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)




# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )

# print(completion.choices[0].message)


