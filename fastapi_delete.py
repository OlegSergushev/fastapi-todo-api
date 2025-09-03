from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Note(BaseModel):
    id: int
    text: str


notes = [
    Note(id=1, text="Купить хлеб"),
    Note(id=2, text="Написать отчет"),
    Note(id=3, text="Позвонить маме"),
    Note(id=4, text="Сходить в спортзал"),
    Note(id=5, text="Прочитать книгу")
]


@app.delete("/notes/{note_id}", response_model=Note)
def delete_note(note_id: int) -> Note:        
    for i, note in enumerate(notes):
        if note.id == note_id:
            return notes.pop(i)
    raise HTTPException(status_code=404, detail="Note not found")
