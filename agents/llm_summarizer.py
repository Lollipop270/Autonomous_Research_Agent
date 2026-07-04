class OfflineReportGenerator:

    def generate(self, query: str, summary: dict):

        return f"""
# Research Report: {query}

## Executive Summary
{summary.get('key_points', [])[:3]}

## Key Findings
{"".join("- " + f + "\n" for f in summary.get('findings', []))}

## Insights
{"".join("- " + i + "\n" for i in summary.get('insights', []))}

## Sources
{"".join("- " + r for r in summary.get('references', []))}
"""