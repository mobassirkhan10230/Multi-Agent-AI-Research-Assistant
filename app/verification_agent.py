
from llm import create_llm


def verification_agent(
    research_results: str,
    analysis_results: str,
    query: str
):

    # 1. Initialize the LLM
    llm = create_llm()

    # 2. Construct the verification prompt
    prompt = f"""
    You are an expert research verification analyst.

    Your task is to verify the claims made during research
    and analysis using only the evidence provided below.

    Research Question:
    {query}

    Original Research Findings:
    {research_results}

    Analysis Results:
    {analysis_results}

    Verification Instructions:

    1. Identify the important factual claims.
    2. Check each claim against the original research findings.
    3. Classify each claim as:
       - Supported
       - Partially Supported
       - Unsupported
       - Contradicted

    4. Explain the reason for each classification.
    5. Identify missing or insufficient evidence.
    6. Do not invent facts or sources.
    7. Do not mark a claim as verified merely because
       it appears in the analysis.

    Important:
    You only have access to the supplied research findings.
    Do not claim that you independently verified external
    websites or documents.

    Output Format:

    1. Claims Reviewed
    2. Verification Status
    3. Evidence and Explanation
    4. Contradictions or Errors
    5. Missing Evidence
    6. Overall Verification Result
    """

    # 3. Generate verification results
    response = llm.invoke(prompt)

    return response.content
