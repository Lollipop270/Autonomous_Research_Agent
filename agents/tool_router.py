class ToolRouter:

    def decide(self, query: str):

        q = query.lower()
        tools = set()

        # Always include web search (important fix)
        tools.add("duckduckgo")

        # Wikipedia triggers
        if any(w in q for w in ["what is", "who is", "define"]):
            tools.add("wikipedia")

        # Research / technical queries
        if any(w in q for w in ["machine learning", "ai", "model", "algorithm", "data"]):
            tools.add("arxiv")

        # News queries
        if any(w in q for w in ["latest", "news", "update"]):
            tools.add("rss")

        # Comparison queries
        if any(w in q for w in ["vs", "versus", "compare"]):
            tools.add("duckduckgo")
            tools.add("wikipedia")

        return list(tools)