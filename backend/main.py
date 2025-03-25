from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
from crew import Calculator, SolutionFormat
import uvicorn

load_dotenv()
app = FastAPI()

def run(latex: str):
    inputs = {
        'latex': latex
    }
    return Calculator().crew().kickoff(inputs=inputs)
    

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
    response = run(request.latex)
    print(response.raw)
    return response.raw
        
    
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
