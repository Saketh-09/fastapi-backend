from sqlalchemy.orm import Session

import models
import schemas


def create_connect(db: Session, connect: schemas.ConnectCreate):
    db_connect = models.Connect(email=connect.email, first_name=connect.first_name,
                                last_name=connect.last_name, comment = connect.comment)
    db.add(db_connect)
    db.commit()
    db.refresh(db_connect)
    return db_connect
