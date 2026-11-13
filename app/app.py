
import streamlit as st
from pathlib import Path

from embeddings import create_embeddings
from vector_store import load_vector_store
from graph import create_research_graph


st.set_page_config(
    page_title="Deep Research Assistant",
    page_icon="🔍",
    layout="wide",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        html, body, [data-testid="stAppViewContainer"] {
            background: #f2f2f4;
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: #f2f2f4;
        }

        .block-container {
            max-width: 1440px;
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        .app-header {
            background: linear-gradient(90deg, #4f7fd8 0%, #7a5ec8 100%);
            border-radius: 0;
            padding: 1.4rem 0 1.2rem 0;
            margin: 0 -1.2rem 1.5rem -1.2rem;
            box-shadow: inset 0 -1px rgba(255,255,255,0.08);
            text-align: center;
        }

        .app-header h1 {
            color: #f2f5fb;
            font-size: 3.1rem;
            font-weight: 800;
            line-height: 1.1;
            margin: 0;
            letter-spacing: -0.06em;
        }

        .ui-panel {
            background: #f4f4f6;
            border-radius: 0.7rem;
            padding: 1rem 1.1rem 0.7rem 1.1rem;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(18, 28, 45, 0.08);
        }

        .section-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: #1d1d1f;
            letter-spacing: -0.05em;
            margin: 0 0 1rem 0;
        }

        .report-title {
            font-size: 2.6rem;
            font-weight: 800;
            color: #1d1d1f;
            letter-spacing: -0.05em;
            margin: 0 0 0.9rem 0;
        }

        div[data-testid="stForm"] {
            border: 1px solid rgba(17, 24, 39, 0.08);
            background: #f4f4f6;
            padding: 0 0 0.2rem 0;
            border-radius: 0.7rem;
            overflow: hidden;
        }

        .control-label {
            color: #1d1d1f;
            font-size: 1.05rem;
            font-weight: 500;
            margin: 0.25rem 0 0.35rem 0;
        }

        div[data-baseweb="select"] > div {
            background: rgba(233, 234, 238, 0.9);
            border: none;
            border-radius: 0.45rem;
            min-height: 2.8rem;
            box-shadow: none;
        }

        div[data-baseweb="select"] span {
            color: #1d1d1f;
        }

        .stTextArea textarea,
        .stTextInput input {
            background: rgba(233, 234, 238, 0.9);
            border: none;
            border-radius: 0.45rem;
            color: #1d1d1f;
            padding: 1rem 0.9rem;
            font-size: 1.05rem;
        }

        .stTextArea textarea::placeholder,
        .stTextInput input::placeholder {
            color: rgba(29, 29, 31, 0.6);
        }

        .stButton > button {
            width: 100%;
            background: linear-gradient(180deg, #f14b48 0%, #ea3a3a 100%);
            color: white;
            border: none;
            border-radius: 0.45rem;
            font-size: 1.05rem;
            font-weight: 700;
            padding: 0.9rem 1rem;
            box-shadow: none;
        }

        .stButton > button:hover {
            background: linear-gradient(180deg, #ea3d3d 0%, #de2a2a 100%);
            color: white;
        }

        .topic-box {
            background: rgba(233, 234, 238, 0.9);
            border-radius: 0.45rem;
            border: 1px solid rgba(17, 24, 39, 0.08);
            padding: 0.8rem 0.9rem;
            color: #1d1d1f;
            font-size: 1.15rem;
            line-height: 1.5;
            margin-top: 0.5rem;
        }

        .result-body {
            background: #f4f4f6;
            border-radius: 0.7rem;
            padding: 0.2rem 0;
        }

        .result-body p,
        .result-body li,
        .result-body strong {
            color: #1d1d1f;
            font-size: 1.08rem;
            line-height: 1.7;
        }

        .result-body h3 {
            color: #1d1d1f;
            font-size: 1.45rem;
            margin-top: 1.1rem;
        }

        .report-topic {
            font-size: 1.15rem;
            font-weight: 500;
            color: #1d1d1f;
            margin: 0 0 1rem 0;
            line-height: 1.5;
        }

        .pdf-button {
            margin-top: 1.2rem;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: transparent;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource
def initialize_research_system():
    embedding_model = create_embeddings()
    vector_store = load_vector_store(embedding_model=embedding_model)
    app = create_research_graph(vector_store)
    return app


st.markdown('<div class="app-header"><h1>Deep Research Assistant</h1></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Research Configuration</div>', unsafe_allow_html=True)

with st.form("research_form"):
    st.markdown('<div class="control-label">Research Topic</div>', unsafe_allow_html=True)
    topic = st.text_area(
        label="",
        value=(
            "Impact of artificial intelligence on healthcare efficiency and patient outcomes"
        ),
        height=112,
        label_visibility="collapsed",
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="control-label">Research Depth</div>', unsafe_allow_html=True)
        research_depth = st.selectbox(
            "",
            ["Surface (5-8 sources)", "Detailed (10-15 sources)", "Expert (20+ sources)"],
            index=0,
            label_visibility="collapsed",
        )
    with col2:
        st.markdown('<div class="control-label">Time Frame</div>', unsafe_allow_html=True)
        time_frame = st.selectbox(
            "",
            ["Current (≤6 months)", "Past year", "Past 3 years", "All available"],
            index=0,
            label_visibility="collapsed",
        )

    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="control-label">Focus Area</div>', unsafe_allow_html=True)
        focus_area = st.selectbox(
            "",
            ["General", "Clinical outcomes", "Economic impact", "Policy and ethics"],
            index=0,
            label_visibility="collapsed",
        )
    with col4:
        st.markdown('<div class="control-label">Report Format</div>', unsafe_allow_html=True)
        report_format = st.selectbox(
            "",
            ["Detailed Analysis", "Executive Summary", "Brief Notes", "Annotated Bibliography"],
            index=0,
            label_visibility="collapsed",
        )

    submitted = st.form_submit_button("Start Deep Research", use_container_width=True)

if submitted:
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        try:
            with st.spinner("AI agents are researching your topic..."):
                research_app = initialize_research_system()
                final_state = research_app.invoke({"query": topic.strip()})
                st.session_state["research_result"] = final_state
            st.success("Research completed successfully!")
        except Exception as error:
            st.error(f"An error occurred: {error}")


if "research_result" in st.session_state:
    result = st.session_state["research_result"]
    st.markdown('<div class="report-title">Research Report</div>', unsafe_allow_html=True)

    topic_text = topic.strip() if topic.strip() else "Research Topic"
    st.markdown(f'<div class="report-topic">Topic: {topic_text}</div>', unsafe_allow_html=True)

    st.markdown('<div class="result-body">', unsafe_allow_html=True)
    summary = result.get("summary", "No summary available.")
    if summary:
        st.markdown(summary)
    else:
        st.write("No summary available.")
    st.markdown('</div>', unsafe_allow_html=True)

    report_path = result.get("report_path")
    if report_path and Path(report_path).is_file():
        with open(report_path, "rb") as pdf_file:
            st.download_button(
                label="Download Research Report",
                data=pdf_file.read(),
                file_name="research_report.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="download_report",
            )
    else:
        st.warning("The PDF report could not be found.")
