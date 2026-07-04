from tools.base import SearchResult
import re
from collections import Counter


class Summarizer:

    # -----------------------
    # MAIN SUMMARIZATION
    # -----------------------
    def summarize(self, query: str, results: list[SearchResult]):

        if not results:
            return {
                "query": query,
                "key_points": [],
                "findings": [],
                "insights": [],
                "references": []
            }

        top_results = results[:10]

        # -----------------------
        # KEY POINTS
        # -----------------------
        key_points = [r.title for r in top_results if r.title]

        # -----------------------
        # FINDINGS
        # -----------------------
        findings = []

        for r in top_results:
            content = r.content or ""

            snippet = self.smart_snippet(content, 250)

            if snippet:
                cleaned = self.to_answer_style(snippet)

                keywords = self.extract_keywords(cleaned)

                highlighted = self.highlight_keywords(cleaned, keywords)

                findings.append(highlighted)

        # -----------------------
        # INSIGHTS
        # -----------------------
        insights = self._generate_simple_insights(top_results)

        # -----------------------
        # REFERENCES
        # -----------------------
        references = list({r.url for r in top_results if r.url})

        return {
            "query": query,
            "key_points": key_points,
            "findings": findings,
            "insights": insights,
            "references": references
        }

    # -----------------------
    # FINDINGS HELPERS
    # -----------------------

    def smart_snippet(self, text: str, max_len: int = 250):

        if not text:
            return ""

        sentences = re.split(r'(?<=[.!?])\s+', text)

        snippet = ""

        for sentence in sentences:
            if len(snippet) + len(sentence) <= max_len:
                snippet += sentence + " "
            else:
                break

        return snippet.strip()

    def to_answer_style(self, text: str) -> str:

        if not text:
            return ""

        text = text.strip()

        text = re.sub(r"\[\d+\]", "", text)
        text = re.sub(r"\(.*?source.*?\)", "", text, flags=re.IGNORECASE)

        sentences = re.split(r'(?<=[.!?])\s+', text)

        return sentences[0].strip() if sentences else text

    # -----------------------
    # KEYWORD EXTRACTION (NEW)
    # -----------------------
    def extract_keywords(self, text: str, top_k: int = 3):

        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())

        stopwords = {
            "this", "that", "with", "from", "have", "they", "will",
            "their", "what", "when", "which", "there", "about",
            "into", "these", "those", "such", "being", "than"
        }

        words = [w for w in words if w not in stopwords]

        freq = Counter(words)

        scored = {
            w: freq[w] * len(w) * 0.1
            for w in freq
        }

        top_words = sorted(scored, key=scored.get, reverse=True)[:top_k]

        return top_words

    # -----------------------
    # HIGHLIGHT KEYWORDS
    # -----------------------
    def highlight_keywords(self, text: str, keywords: list) -> str:

        for kw in keywords:
            pattern = re.compile(rf'\b{re.escape(kw)}\b', re.IGNORECASE)
            text = pattern.sub(f"**{kw.upper()}**", text)

        return text

    # -----------------------
    # INSIGHTS GENERATION (IMPROVED)
    # -----------------------
    def _generate_simple_insights(self, results: list[SearchResult]):

        word_freq = {}

        for r in results:
            text = f"{r.title} {r.content}".lower()

            words = re.findall(r'\b[a-zA-Z]{4,}\b', text)

            for w in words:
                word_freq[w] = word_freq.get(w, 0) + 1

        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

        insights = [
            f"Key concept: {word}"
            for word, _ in sorted_words[:8]
        ]

        return insights