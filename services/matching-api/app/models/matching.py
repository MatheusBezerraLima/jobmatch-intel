from pydantic import BaseModel
from app.models.job import Job

class MatchingRequest(BaseModel):
    job: Job
    resume: str

class MatchingResponse(BaseModel):
    score: int
    justification: str
    gaps: list[str]
    recommendations: list[str]