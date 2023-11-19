from sqlalchemy.orm import Session
from . import models, schemas

# ユーザー一覧取得
def get_users(db: Session, skip: int=0, limit: int=100):
    return db.query(models.User).offset(skip).limit(limit).all()

# 会議室一覧取得
def get_rooms(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Room).offset(skip).limit(limit).all()

# 予約一覧取得
def get_bookings(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Booking).offset(skip).limit(limit).all()

# ユーザー登録
def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)