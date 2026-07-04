import os
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Exporter:

    # -----------------------
    # MARKDOWN EXPORT
    # -----------------------
    def to_markdown(self, data: dict) -> str:

        summary = data.get("structured_summary", {})
        report = data.get("final_report", "")

        md = f"""# Research Report

## Query
{data.get('query')}

## Results Count
{data.get('results_count')}

---

## Structured Summary

### Key Points
"""

        for k in summary.get("key_points", []):
            md += f"- {k}\n"

        md += "\n### Findings\n"
        for f in summary.get("findings", []):
            md += f"- {f}\n\n"

        md += "\n### Insights\n"
        for i in summary.get("insights", []):
            md += f"- {i}\n"

        md += "\n### References\n"
        for r in summary.get("references", []):
            md += f"- {r}\n"

        md += "\n---\n\n## Final Report\n"
        md += report

        return md

    # -----------------------
    # SAVE MARKDOWN FILE
    # -----------------------
    def save_markdown(self, content: str, filename: str = None):

        os.makedirs("exports", exist_ok=True)

        if not filename:
            filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        path = os.path.join("exports", filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return path

    # -----------------------
    # PDF EXPORT
    # -----------------------
    def save_pdf(self, content: str, filename: str = None):

        os.makedirs("exports", exist_ok=True)

        if not filename:
            filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

        path = os.path.join("exports", filename)

        c = canvas.Canvas(path, pagesize=letter)
        width, height = letter

        y = height - 40

        for line in content.split("\n"):
            if y < 40:
                c.showPage()
                y = height - 40

            c.drawString(40, y, line[:100])  # prevent overflow
            y -= 15

        c.save()

        return path