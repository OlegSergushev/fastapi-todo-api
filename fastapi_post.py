from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

users = []


class User(BaseModel):
    id: int
    name: str
    age: int = Field(ge=18)


class UserCreate(BaseModel):
    name: str
    age: int = Field(ge=18)


@app.post("/users", status_code=201, response_model=User)
def create_user(payload: UserCreate) -> User:
    new_id = len(users) + 1
    user = User(id=new_id, name=payload.name, age=payload.age)
    users.append(user)
    return user
