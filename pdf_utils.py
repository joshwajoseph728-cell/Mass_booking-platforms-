"""PDF generation: booking receipt + priest prayer list."""
import io
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

def generate_receipt(booking: dict) -> bytes:
    buf = io.BytesIO()

    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "OUR LADY OF DOLOURS",
            styles["Heading1"],
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            f"Booked By: {booking.get('full_name','-')}",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            f"Mass Date: {booking.get('mass_date','-')}",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            f"Mass Time: {booking.get('mass_time','-')}",
            styles["Normal"],
        )
    )

    doc.build(story)

    return buf.getvalue()


def generate_prayer_list(
    date_label: str,
    bookings: list[dict],
) -> bytes:

    buf = io.BytesIO()

    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            f"Prayer List - {date_label}",
            styles["Heading1"],
        )
    )

    story.append(
        Spacer(1, 20)
    )

    for booking in bookings:

        story.append(
            Paragraph(
                booking.get(
                    "full_name",
                    "-"
                ),
                styles["Normal"],
            )
        )

    doc.build(story)

    return buf.getvalue()