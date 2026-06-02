from abc import ABC, abstractmethod
from app.models.job import Job
from app.models.matching import MatchingResponse

class BaseAIProvider(ABC):

    @abstractmethod
    def match(self, job: Job, resume: str) -> MatchingResponse:
        pass