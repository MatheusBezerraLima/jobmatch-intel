from pydantic import BaseModel

class Job(BaseModel):
    title: str
    company: str
    description: str
    required_skills: list[str]
    experience_level: str
    location: str
    work_model: str
