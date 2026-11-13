
import os
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)


def generate_pdf_report(
    query: str,
    summary: str,
    output_path: str = "reports/research_report.pdf"
):

    # 1. Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    # 2. Create the PDF document
    pdf = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch
    )

    # 3. Load default styles
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        textColor=colors.HexColor("#17365D"),
        spaceAfter=18
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        textColor=colors.HexColor("#1F4E79"),
        spaceBefore=12,
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        "ReportBody",
        parent=styles["BodyText"],
        leading=15,
        spaceAfter=8
    )

    # 4. Create a list to hold PDF elements
    story = []

    # 5. Add the report title
    story.append(
        Paragraph("AI Research Assistant Report", title_style)
    )

    story.append(
        Paragraph(
            f"<b>Research Question:</b> {escape(query)}",
            body_style
        )
    )

    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", thickness=1))
    story.append(Spacer(1, 12))

    # 6. Add summary content to the PDF
    for line in summary.splitlines():

        line = line.strip()

        if not line:
            story.append(Spacer(1, 5))
            continue

        # Treat numbered headings and Markdown headings as sections
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
            story.append(
                Paragraph(escape(heading), heading_style)
            )

        elif (
            len(line) > 2
            and line[0].isdigit()
            and line[1] in ".)"
        ):
            story.append(
                Paragraph(escape(line), heading_style)
            )

        elif line.startswith(("- ", "* ")):
            bullet_text = escape(line[2:])
            story.append(
                Paragraph(
                    f"&bull; {bullet_text}",
                    body_style
                )
            )

        else:
            story.append(
                Paragraph(escape(line), body_style)
            )

    # 7. Generate and save the PDF
    pdf.build(story)

    return output_path


def report_agent(
    query: str,
    summary: str,
    output_path: str = "reports/research_report.pdf"
):

    # Generate the final research report
    report_path = generate_pdf_report(
        query=query,
        summary=summary,
        output_path=output_path
    )

    return report_path
