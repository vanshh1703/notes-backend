from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()

@app.post("/notes")
def add_note(content: str, db: Session = Depends(get_db)):
    note = models.Note(content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note
