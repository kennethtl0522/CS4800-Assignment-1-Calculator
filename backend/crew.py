# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel

class SolutionFormat(BaseModel):
    solution: str

@CrewBase
class Calculator():

  @agent
  def calculator(self) -> Agent:
    return Agent(
      config=self.agents_config['calculator'],
      verbose=True,
    )

  @agent
  def reporting_analyst(self) -> Agent:
    return Agent(
      config=self.agents_config['reporting_analyst'],
      verbose=True
    )

  @task
  def calculating_task(self) -> Task:
    return Task(
      config=self.tasks_config['calculating_task'],
    )

  @task
  def reporting_task(self) -> Task:
    return Task(
      config=self.tasks_config['reporting_task'],
    )

  @crew
  def crew(self) -> Crew:
    return Crew(
      agents=self.agents,
      tasks=self.tasks,
      process=Process.sequential,
      verbose=True,
    )