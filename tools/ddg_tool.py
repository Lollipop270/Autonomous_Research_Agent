from duckduckgo_search import DDGS
from tools.base import SearchResult
from ddgs import DDGS

class DuckDuckGoTool:

    def search(self, query: str, max_results: int = 8):

        results = []

        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(
                    SearchResult(
                        title=r.get("title", ""),
                        url=r.get("href", ""),
                        source="duckduckgo",
                        content=r.get("body", "")
                    )
                )

        return results