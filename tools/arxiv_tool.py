import arxiv
from tools.base import SearchResult


class ArxivTool:

    def search(self, query: str, max_results: int = 5):

        results = []

        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        client = arxiv.Client()

        # ✅ SAFE + COMPATIBLE across versions
        for result in client.results(search):

            results.append(
                SearchResult(
                    title=result.title,
                    url=result.entry_id,
                    source="arxiv",
                    content=result.summary
                )
            )

        return results