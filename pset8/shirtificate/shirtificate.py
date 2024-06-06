from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.cell(w=0, h=50, txt="CS50 Shirtificate", align="C", new_x="LEFT", new_y="BMARGIN")

name = input("Name: ")
pdf=PDF()
pdf.set_auto_page_break(False)
pdf.set_font(family="helvetica", style="B", size=60)
pdf.set_margin(10)
pdf.add_page()
pdf.image("shirtificate.png", x='C', y=70, w=pdf.epw)
pdf.set_text_color(255,255,255)
pdf.set_font(size=24)
pdf.cell(w=0, txt=f"{name} took CS50", h=-300, align="C")
pdf.output("shirtificate.pdf")