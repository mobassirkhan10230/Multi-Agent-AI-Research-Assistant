
from llm import create_llm


def summarization_agent(
    research_results: str,
    analysis_results: str,
    verification_results: str,
    query: str
):

    # 1. Initialize the LLM
    llm = create_llm()

    # 2. Construct the summarization prompt
    prompt = f"""
    You are an expert research summarization assistant.

    Your task is to create a comprehensive and clear
    research summary using the information provided below.

    Research Question:
    {query}

    Original Research Findings:
    {research_results}

    Analysis Results:
    {analysis_results}

    Verification Results:
    {verification_results}

    Summarization Instructions:

    1. Include important supported findings.
    2. Incorporate useful insights from the analysis.
    3. Respect the verification results.
    4. Do not present contradicted claims as facts.
    5. Clearly mention partially supported or unsupported claims.
    6. Highlight important missing information.
    7. Preserve source references where available.
    8. Do not invent facts or references.

    Output Structure:

    1. Research Overview
    2. Key Findings
    3. Technical Insights
    4. Contradictions and Limitations
    5. Information Gaps
    6. Conclusion
    """

    # 3. Generate the summary
    response = llm.invoke(prompt)

    return response.content
