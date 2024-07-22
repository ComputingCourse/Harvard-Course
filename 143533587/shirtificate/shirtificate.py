from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 50)
#pdf.cell(60)
pdf.cell(0, 30, 'CS50 Shirtificate', align='C')
pdf.image("shirtificate.png", 5, 40, 200)
pdf.set_text_color(255,255,255)
pdf.set_font("helvetica", "B", 40)
pdf.cell(-200, 200, f'{name} took CS50', align='C')
pdf.output("shirtificate.pdf")