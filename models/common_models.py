from pydantic import BaseModel


class SearchResult(BaseModel):
    title: str
    url: str
    source: str
    content: str