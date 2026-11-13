
from llm import create_llm


def analysis_agent(research_results: str, query: str):

    # 1. Initialize the LLM
    llm = create_llm()

    # 2. Prepare the analysis prompt
    prompt = f"""
    You are an expert research analyst.

    Analyze the research findings provided below.

    Your responsibilities:

    1. Identify the main findings.
    2. Group related information into key themes.
    3. Explain relationships between the findings.
    4. Identify contradictions between sources, if any.
    5. Identify missing information and unanswered questions.
    6. Do not introduce facts that are not supported
       by the research findings.

    Research Question:
    {query}

    Research Findings:
    {research_results}

    Provide your analysis using the following structure:

    1. Key Findings
    2. Major Themes
    3. Relationships and Insights
    4. Contradictions
    5. Missing Information
    """

    # 3. Generate analysis
    response = llm.invoke(prompt)

    return response.content
