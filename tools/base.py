from dataclasses import dataclass
from typing import List
from ddgs import DDGS

@dataclass
class SearchResult:
    title: str
    url: str
    source: str
    content: str