from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    id: Optional[int] = None