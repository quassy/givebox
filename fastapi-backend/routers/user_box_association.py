from fastapi import APIRouter
from fastapi import Depends

import models
from database import SessionLocal
from utils import get_db

router = APIRouter()


@router.post("/add_maintainer/{box_id}/{user_id}")
def add_maintainer(box_id: int, user_id: int, db: SessionLocal = Depends(get_db)) -> int:
    db_box: models.GiveBox = db.query(models.GiveBox).filter(models.GiveBox.id == box_id).first()
    db_user: models.User = db.query(models.User).filter(models.User.id == user_id).first()

    assert db_box is not None
    assert db_user is not None

    if db_box.maintainers:
        db_box.maintainers.append(db_user)
    else:
        db_box.maintainers = [db_user]

    db.commit()
    return 200
