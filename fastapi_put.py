from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    age: int


class UserUpdate(BaseModel):
    name: str
    age: int = Field(gt=0)


users = [
    User(id=1, name="Алексей", age=25),
    User(id=2, name="Мария", age=30),
    User(id=3, name="Иван", age=22),
    User(id=4, name="Елена", age=28),
    User(id=5, name="Дмитрий", age=35)
]


@app.put("/users/{user_id}")
def update_user(user_id: int, payload: UserUpdate) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            updated_user = User(id=user_id, name=payload.name, age=payload.age)
            users[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")
