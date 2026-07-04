from collections import Counter
import re
from tools.base import SearchResult


class Processor:

    STOPWORDS = {
        "the", "is", "a", "an", "and", "or", "of", "to", "in",
        "for", "on", "with", "as", "by", "at", "from", "that",
        "this", "it", "are", "was", "be", "has", "have", "had",
        "i", "you", "we", "they", "them", "he", "she", "it"
    }

    # -----------------------
    # CLEANING
    # -----------------------
    def clean_text(self, text: str) -> str:
        if not text:
            return ""

        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    # -----------------------
    # DEDUPLICATION
    # -----------------------
    def deduplicate(self, results: list[SearchResult]) -> list[SearchResult]:

        seen = set()
        unique_results = []

        for r in results:
            key = self.clean_text(r.title + " " + r.content)

            if key not in seen:
                seen.add(key)
                unique_results.append(r)

        return unique_results

    # -----------------------
    # RANKING
    # -----------------------
    def rank(self, query: str, results: list[SearchResult]) -> list[SearchResult]:

        query_terms = set(self.clean_text(query).split())
        scored = []

        for r in results:
            content = self.clean_text(r.title + " " + r.content)

            # base relevance score
            score = sum(1 for word in query_terms if word in content)

            # boost trusted sources
            if r.source in ["wikipedia", "arxiv"]:
                score += 2

            # slight boost for longer, richer content
            score += min(len(content.split()) / 50, 2)

            scored.append((score, r))

        scored.sort(key=lambda x: x[0], reverse=True)

        return [r for _, r in scored]

    # -----------------------
    # INSIGHTS EXTRACTION
    # -----------------------
    def extract_insights(self, results: list[SearchResult]) -> list[str]:

        words = []

        for r in results:
            text = (r.title + " " + r.content).lower()
            text = re.sub(r"[^\w\s]", "", text)
            words.extend(text.split())

        filtered = [
            w for w in words
            if w not in self.STOPWORDS and len(w) > 3
        ]

        common = Counter(filtered).most_common(8)

        return [f"Key concept: {word}" for word, _ in common]