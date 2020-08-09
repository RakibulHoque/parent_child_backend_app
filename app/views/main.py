from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils import models, schemas, crud
from app.utils.db import SessionLocal, engine

from typing import List

models.Base.metadata.create_all(bind=engine)

# app = FastAPI()
from app import app


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/parents/", response_model=schemas.Parent)
def create_parent(parent: schemas.ParentCreate, db: Session = Depends(get_db)):
    db_parent = crud.get_parent_by_email(db, email=parent.email)
    if db_parent:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_parent(db=db, parent=parent)


@app.get("/parents/", response_model=List[schemas.Parent])
def read_parents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    parents = crud.get_parents(db, skip=skip, limit=limit)
    return parents


@app.get("/parents/{parent_id}", response_model=schemas.Parent)
def read_parent(parent_id: int, db: Session = Depends(get_db)):
    db_parent = crud.get_parent(db, parent_id=parent_id)
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return db_parent


@app.put("/parents/{parent_id}", response_model=schemas.Parent)
def update_parent(parent_id: int, parent: schemas.ParentCreate, db: Session = Depends(get_db)):
    db_parent = crud.get_parent(db, parent_id=parent_id)
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return crud.update_parent(db=db, parent_id=parent_id, parent=parent)


@app.delete("/parents/{parent_id}", response_model=schemas.Parent)
def delete_parent(parent_id: int, db: Session = Depends(get_db)):
    db_parent = crud.get_parent(db, parent_id=parent_id)
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return crud.delete_parent(db=db, parent_id=parent_id)


@app.get("/children/", response_model=List[schemas.Child])
def read_children(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    children = crud.get_children(db, skip=skip, limit=limit)
    return children


@app.post("/parents/{parent_id}/children/", response_model=schemas.Child)
def create_child_for_parent(
        parent_id: int, child: schemas.ChildCreate, db: Session = Depends(get_db)
):
    db_parent = crud.get_parent(db, parent_id=parent_id)
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return crud.create_parent_child(db=db, child=child, parent_id=parent_id)


@app.get("/children/{child_id}", response_model=schemas.Child)
def read_child(child_id: int, db: Session = Depends(get_db)):
    db_child = crud.get_child(db, child_id=child_id)
    if db_child is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return db_child


@app.put("/children/{child_id}", response_model=schemas.Child)
def update_child(child_id: int, child: schemas.ChildCreate, db: Session = Depends(get_db)):
    db_child = crud.get_child(db, child_id=child_id)
    if db_child is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return crud.update_child(db=db, child_id=child_id, child=child)


@app.delete("/children/{child_id}", response_model=schemas.Child)
def delete_child(child_id: int, db: Session = Depends(get_db)):
    db_child = crud.get_child(db, child_id=child_id)
    if db_child is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return crud.delete_child(db=db, child_id=child_id)