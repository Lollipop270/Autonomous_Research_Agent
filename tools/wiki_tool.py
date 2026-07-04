import wikipedia
from tools.base import SearchResult


class WikipediaTool:

    def search(self, query: str):

        try:
            page = wikipedia.page(query)

            return [
                SearchResult(
                    title=page.title,
                    url=page.url,
                    source="wikipedia",
                    content=page.summary
                )
            ]

        except Exception:
            return []