
from langgraph.graph import StateGraph, START, END

from state import ResearchState

from research_agent import research_agent
from analysis_agent import analysis_agent
from verification_agent import verification_agent
from summarization_agent import summarization_agent
from report_agent import report_agent


# ------------------------------------------------
# 1. Research Node
# ------------------------------------------------

def research_node(state: ResearchState, vector_store):

    results = research_agent(
        vector_store=vector_store,
        query=state["query"]
    )

    return {
        "research_results": results
    }


# ------------------------------------------------
# 2. Analysis Node
# ------------------------------------------------

def analysis_node(state: ResearchState):

    results = analysis_agent(
        research_results=state["research_results"],
        query=state["query"]
    )

    return {
        "analysis_results": results
    }


# ------------------------------------------------
# 3. Verification Node
# ------------------------------------------------

def verification_node(state: ResearchState):

    results = verification_agent(
        research_results=state["research_results"],
        analysis_results=state["analysis_results"],
        query=state["query"]
    )

    return {
        "verification_results": results
    }


# ------------------------------------------------
# 4. Summarization Node
# ------------------------------------------------

def summarization_node(state: ResearchState):

    results = summarization_agent(
        research_results=state["research_results"],
        analysis_results=state["analysis_results"],
        verification_results=state["verification_results"],
        query=state["query"]
    )

    return {
        "summary": results
    }


# ------------------------------------------------
# 5. Report Node
# ------------------------------------------------

def report_node(state: ResearchState):

    report_path = report_agent(
        query=state["query"],
        summary=state["summary"]
    )

    return {
        "report_path": report_path
    }


# ------------------------------------------------
# 6. Create LangGraph Workflow
# ------------------------------------------------

def create_research_graph(vector_store):

    # Initialize the graph with our shared state
    workflow = StateGraph(ResearchState)

    # Register all five agent nodes
    workflow.add_node(
        "research",
        lambda state: research_node(state, vector_store)
    )

    workflow.add_node("analysis", analysis_node)

    workflow.add_node("verification", verification_node)

    workflow.add_node("summarization", summarization_node)

    workflow.add_node("report", report_node)

    # Connect the nodes sequentially
    workflow.add_edge(START, "research")

    workflow.add_edge("research", "analysis")

    workflow.add_edge("analysis", "verification")

    workflow.add_edge("verification", "summarization")

    workflow.add_edge("summarization", "report")

    workflow.add_edge("report", END)

    # Compile the graph
    app = workflow.compile()

    return app
