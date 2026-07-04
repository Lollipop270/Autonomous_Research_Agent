import asyncio

from tools.ddg_tool import DuckDuckGoTool
from tools.wiki_tool import WikipediaTool
from tools.arxiv_tool import ArxivTool
from tools.rss_tool import RSSTool
from agents.tool_router import ToolRouter
from agents.processor import Processor


class SearchAgent:

    def __init__(self):
        self.router = ToolRouter()
        self.processor = Processor()

        self.ddg = DuckDuckGoTool()
        self.wiki = WikipediaTool()
        self.arxiv = ArxivTool()
        self.rss = RSSTool()

    async def run(self, query: str):

        tools = self.router.decide(query)

        results = []

        # IMPORTANT: use to_thread ONLY on sync functions
        tasks = []

        if "duckduckgo" in tools:
            tasks.append(asyncio.to_thread(self.ddg.search, query))

        if "wikipedia" in tools:
            tasks.append(asyncio.to_thread(self.wiki.search, query))

        if "arxiv" in tools:
            tasks.append(asyncio.to_thread(self.arxiv.search, query))

        if "rss" in tools:
            tasks.append(asyncio.to_thread(self.rss.search, query))

        if tasks:
            outputs = await asyncio.gather(*tasks)
            results = [item for sublist in outputs for item in sublist]

        # STEP 1: deduplicate
        results = self.processor.deduplicate(results)

        # STEP 2: rank
        results = self.processor.rank(query, results)

        return results