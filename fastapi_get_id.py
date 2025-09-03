from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str


users = [
    User(id=1, name="Алексей", email="alexey@example.com"),
    User(id=2, name="Мария", email="maria@example.com"),
    User(id=3, name="Иван", email="ivan@example.com"),
    User(id=4, name="Елена", email="elena@example.com"),
    User(id=5, name="Дмитрий", email="dmitry@example.com")
]


@app.get("/users/{user_id}", response_model = User)
def get_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
