import feedparser
from tools.base import SearchResult


class RSSTool:

    FEEDS = [
        "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "https://feeds.bbci.co.uk/news/technology/rss.xml"
    ]

    def search(self, query: str):

        results = []

        for feed in self.FEEDS:
            data = feedparser.parse(feed)

            for entry in data.entries[:5]:

                if query.lower() in entry.title.lower():

                    results.append(
                        SearchResult(
                            title=entry.title,
                            url=entry.link,
                            source="rss",
                            content=getattr(entry, "summary", "")
                        )
                    )

        return results