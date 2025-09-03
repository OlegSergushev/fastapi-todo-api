from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    completed: bool


tasks = [
    Task(id=1, title="Купить молоко", completed=False),
    Task(id=2, title="Позвонить другу", completed=True),
    Task(id=3, title="Сделать домашку", completed=False),
    Task(id=4, title="Погулять с собакой", completed=True),
    Task(id=5, title="Записаться на тренировку", completed=False)
]

      
@app.get('/tasks', response_model=List[Task])
async def read_tasks() -> List[Task]:
    return tasks
