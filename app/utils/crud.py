from sqlalchemy.orm import Session

from app.utils import models, schemas


def get_parent(db: Session, parent_id: int):
    return db.query(models.Parent).filter(models.Parent.id == parent_id).first()


def get_parent_by_email(db: Session, email: str):
    return db.query(models.Parent).filter(models.Parent.email == email).first()


def get_parents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parent).offset(skip).limit(limit).all()


def create_parent(db: Session, parent: schemas.ParentCreate):
    db_parent = models.Parent(**parent.dict(), full_name=" ".join([parent.first_name, parent.last_name]))
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return db_parent


def update_parent(db: Session, parent: schemas.ParentCreate, parent_id: int):
    db_parent = db.query(models.Parent).filter(models.Parent.id == parent_id).first()
    db_parent.first_name = parent.first_name
    db_parent.last_name = parent.last_name
    db_parent.age = parent.age
    db_parent.email = parent.email
    db_parent.address = parent.address
    db_parent.full_name = " ".join([parent.first_name, parent.last_name])
    db.commit()
    db.refresh(db_parent)
    return db_parent


def delete_parent(db: Session, parent_id: int):
    db_parent = db.query(models.Parent).filter(models.Parent.id == parent_id).first()
    db.delete(db_parent)
    db.commit()
    return db_parent


def get_child(db: Session, child_id: int):
    return db.query(models.Child).filter(models.Child.id == child_id).first()


def get_children(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Child).offset(skip).limit(limit).all()


def create_parent_child(db: Session, child: schemas.ChildCreate, parent_id: int):
    db_child = models.Child(**child.dict(), parent_id=parent_id,
                            full_name=" ".join([child.first_name, child.last_name]))
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child


def update_child(db: Session, child: schemas.ChildCreate, child_id: int):
    db_child = db.query(models.Child).filter(models.Child.id == child_id).first()
    db_child.first_name = child.first_name
    db_child.last_name = child.last_name
    db_child.age = child.age
    db_child.full_name = " ".join([child.first_name, child.last_name])
    db.commit()
    db.refresh(db_child)
    return db_child


def delete_child(db: Session, child_id: int):
    db_child = db.query(models.Child).filter(models.Child.id == child_id).first()
    db.delete(db_child)
    db.commit()
    return db_child