from pydantic import BaseModel
from typing import Optional

class JoobleJob(BaseModel):
    title: str
    company: str
    location: str
    description: str
    link: str
    salary: Optional[str] = None
    updated: Optional[str] = None