
from typing import TypedDict


class ResearchState(TypedDict, total=False):

    # Original research question
    query: str

    # Research Agent output
    research_results: str

    # Analysis Agent output
    analysis_results: str

    # Verification Agent output
    verification_results: str

    # Summarization Agent output
    summary: str

    # Generated PDF report location
    report_path: str

    # New fields for feedback loop
    research_attempts: int
    needs_more_research: bool
    research_feedback: str
