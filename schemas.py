from pydantic import BaseModel
from typing import Union


class ConnectBase(BaseModel):
    first_name: str
    last_name: Union[str,None] = None
    comment: Union[str,None] = None
    email: Union[str,None] = None

class ConnectCreate(ConnectBase):
    pass


class Connect(ConnectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True