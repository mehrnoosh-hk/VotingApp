from typing import Optional, List
from pydantic import BaseModel


class BasePool(BaseModel):
    question: str
    description: Optional[str]
    options: List[str]
