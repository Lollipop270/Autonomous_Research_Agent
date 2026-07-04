from pydantic import BaseModel
from typing import List


class SummaryResponse(BaseModel):
    query: str
    key_points: List[str]
    findings: List[str]
    actionable_insights: List[str]
    references: List[str]