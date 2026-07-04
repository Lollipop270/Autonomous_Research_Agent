from fastapi import FastAPI
from models.request_models import SearchRequest
from agents.search_agent import SearchAgent
from agents.summarizer import Summarizer
from agents.llm_summarizer import OfflineReportGenerator
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from utils.exporter import Exporter

exporter = Exporter()
last_result = None

app = FastAPI(
    title="Autonomous AI Research Agent",
    version="1.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")


search_agent = SearchAgent()
summarizer = Summarizer()
report_generator = OfflineReportGenerator()


@app.post("/research")
async def research(request: SearchRequest):

    global last_result   # ✅ must be inside function

    results = await search_agent.run(request.query)

    summary = summarizer.summarize(request.query, results)

    report = report_generator.generate(request.query, summary)

    # ✅ store BEFORE returning
    last_result = {
        "query": request.query,
        "results_count": len(results),
        "structured_summary": summary,
        "final_report": report
    }

    return last_result


@app.get("/export/markdown")
def export_markdown():

    if not last_result:
        return {"error": "No report generated yet"}

    md = exporter.to_markdown(last_result)
    path = exporter.save_markdown(md)

    return FileResponse(path, media_type="text/markdown", filename="report.md")


@app.get("/export/pdf")
def export_pdf():

    if not last_result:
        return {"error": "No report generated yet"}

    md = exporter.to_markdown(last_result)
    path = exporter.save_pdf(md)

    return FileResponse(path, media_type="application/pdf", filename="report.pdf")