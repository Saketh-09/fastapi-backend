from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/connect/", response_model=schemas.ConnectCreate)
def connect_api(contact: schemas.ConnectCreate, db: Session = Depends(get_db)):
    return crud.create_connect(db=db, connect=contact)


