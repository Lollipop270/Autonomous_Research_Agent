from pydantic import BaseModel
from typing import List


class ResearchPlan(BaseModel):
    original_query: str
    query_type: str
    topics: List[str]
    sources: List[str]
    search_queries: List[str]