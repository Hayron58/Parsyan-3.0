from fpdf import FPDF
def generate_pdf(data, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for entry in data:
        pdf.cell(200, 10, txt=f"{entry['name']} — {entry['site_status']}", ln=True)
    pdf.output(filename)
    return filename
