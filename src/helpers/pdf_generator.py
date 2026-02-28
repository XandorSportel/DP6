from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
import os
import re

def strip_ansi(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def genereer_recept_pdf(recept, bestandsnaam=None):
    export_map = "exports"
    os.makedirs(export_map, exist_ok=True)

    if not bestandsnaam:
        bestandsnaam = f"{recept.get_naam().replace(' ', '_')}.pdf"

    pad = os.path.join(export_map, bestandsnaam)

    document = SimpleDocTemplate(pad, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    normal_style = styles["Normal"]

    # Title
    elements.append(Paragraph(recept.get_naam(), title_style))
    elements.append(Spacer(1, 0.3 * inch))

    # Description
    elements.append(Paragraph(
        f"<b>Omschrijving:</b> {recept.get_omschrijving()}",
        normal_style
    ))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(
        f"<b>Aantal personen:</b> {recept.get_aantal_personen()}",
        normal_style
    ))
    elements.append(Spacer(1, 0.3 * inch))

    # Ingredients
    elements.append(Paragraph("<b>Ingrediënten:</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    ingredienten = [
        Paragraph(
            str(ingredient.get_ingredient(recept.is_plantaardig())),
            normal_style
        )
        for ingredient in recept.get_ingredienten()
    ]

    elements.append(ListFlowable(
        [ListItem(i) for i in ingredienten],
        bulletType='bullet'
    ))

    elements.append(Spacer(1, 0.3 * inch))

    # Steps
    elements.append(Paragraph("<b>Stappen:</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    stappen = [
        Paragraph(strip_ansi(str(stap)), normal_style)
        for stap in recept.get_stappen()
    ]

    elements.append(ListFlowable(
        [ListItem(s) for s in stappen],
        bulletType='1'
    ))

    document.build(elements)

    return bestandsnaam