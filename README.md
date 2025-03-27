![image](https://github.com/user-attachments/assets/bb667ca7-49dd-4c0a-a1da-cd2e8d87db30)# AI Powered Calculator
This is an AI-powered LaTeX calculator built with React and FastAPI. Users can input math equations using a virtual math field, which are then sent to the backend for step-by-step solving internally and extracts the final answer for display using AI agents. The app displays the solution in beautifully rendered LaTeX, with loading animations for a smooth user experience.

## Feature
- Python
  - FastAPI
  - CrewAI
    - OpenAI API
- Javascript
    - React
      - Mathlive


## Environment Setup and Run scripts

```sh
cd ./frontend
npm install
npm run dev
```

```sh
cd ./backend
uv pip install -r pyproject.toml
OR
poetry install
OR
pip install .
uvicorn main:app
```

## Estimated Hours
#### Requirements Analysis & Design
Frontend Structure Design - 2 Hours
Backend Structure Design - 4 Hours
#### Development
Frontend - 56 Hours
- Learning React - 6 Hours
- Frontend Implement - 24 Hours
- Learning RESTFul - 24 Hours
- RESTFul Implement - 2 Hours
Backend - 72 Hours
- Learning AI - 48 Hours
- AI Implement - 24 Hours
- Learning Fast API - 24 Hours
- Fast API Implement - 4 Hours
#### Testing
4 Hour

## Actual Work Hours - 58 Hours In Total, finished in 3.5 weeks 
#### Requirements Analysis & Design - 3 Hours In Total
Frontend Structure Design - 1 Hours
Backend Structure Design - 2 Hours

#### Development - 48 Hours In Total
Frontend (React) Setup - 2 Hours
Frontend Page Setup and Development - 4 Hours

Backend Setup - 2 Hours
Learning OpenAI API - 8 Hours
Testing OpenAI API Output - Failed (Incorrect Output Answers)
Pivot to AI Agent (Learn For Final Project at the same time)
Learning CrewAI API - 12 Hours
Testing CrewAI API and Implement - Success - 4 Hours
Learning RESTful - 12 Hours
Learning FastAPI - 2 Hours
FastAPI Setup - 2 Hours

Frontend REST Implement - 2 Hours
Frontend Loading Bar Implement - 1 Hour

#### Testing - 7 Hours In Total
Testing Frontend - 1 Hour
Testing Rest API - 2 Hours
Testing OpenAI - 2 Hours
Testing CrewAI - 2 Hours

Average worked 18 Hours a week. I spent most of my time learning and testing AI, but I was not able to figure out how to let openai output a single answer without getting it wrong. Seems OpenAI needs the process of "Reasoning" and failed to make that a stable output. Learning Restful API also took me a long time, as I had never had experience with those before. But the front-end build-up was easy and fine since I have little experience with Vue. I use Mathlive, Latex Input and Render in this app and it has a native support with react and documentation, and I have a long time haven't code with vue. So I picked React and learned a bit, but it wasn't suffering.

## Screenshots
![](https://github.com/kennethtl0522/CS4800-Assignment-1-Calculator/blob/main/Screenshot%202025-03-27%20083136.png)
[Answer is Correct According to Symbolab](https://www.symbolab.com/solver/step-by-step/%5Cfrac%7B%5Cleft(3%20%2B%205%5Cright)%20%5Ccdot%20%5Cleft(2%5E%7B3%7D%20-%20%5Clog_%7B10%7D%5Cleft(100%5Cright)%5Cright)%7D%7B4%7D%20%2B%20%5Csin%5Cleft(%5Cfrac%7B%5Cpi%7D%7B6%7D%5Cright)%20-%20e%5E%7B2%7D?or=input)
