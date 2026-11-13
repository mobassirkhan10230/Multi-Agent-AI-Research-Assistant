
import os
import json


#for tavily-client
from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_core.tools import tool


#for pdf uploader 
from pathlib import Path
import pymupdf
from langchain_core.documents import Document


# Load environment variables from .env
load_dotenv()



@tool
def web_search_tool(query: str) -> str:
    """
        Search the internet for relevant and up-to-date information
        related to the user's research query.

        Uses the Tavily Search API to retrieve up to five relevant
        web results, including titles, URLs, content snippets,
        and available metadata.

        Returns:
            str: Search results formatted as JSON.
    """

    # Read Tavily API key
    api_key = os.getenv("TAVILY_API_KEY")

    tavily_client = TavilyClient(api_key = api_key)

    
    # Perform web search
    response = tavily_client.search(
        query=query,
        search_depth="basic",
        max_results=5
    )

    # Extract useful search results
    results = response.get("results", [])

    # Return results in readable JSON format
    return json.dumps(results, indent=2)




def load_pdf(path:str)->list[Document]:
    """
        Load a PDF document and extract text page by page.

        Args:
            path: Path to the PDF file.

        Returns:
            A list of LangChain Document objects.
    """
    # Convert the provided path into a Path object
    pdf_path = Path(path)

    documents = []

    # Open the PDF document
    with pymupdf.open(pdf_path) as pdf:

        # Iterate through every page
        for page_number, page in enumerate(pdf, start=1):

            # Extract text from the current page
            page_text = page.get_text("text").strip()

            # Skip pages without extractable text
            if not page_text:
                continue

            # Create a LangChain Document object
            document = Document(
                page_content=page_text,
                metadata={
                    "source": str(pdf_path),
                    "page": page_number
                }
            )

            # Store the document in our list
            documents.append(document)

    return documents



from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):
    """
    Split extracted PDF documents into smaller chunks.
    """

    # Create the text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )

    # Split documents into smaller chunks
    chunks = text_splitter.split_documents(documents)

    return chunks



# print(chunk_documents(load_pdf("app/docs.pdf")))

# print(web_search_tool("what is AI agent and agentic AI"))
    