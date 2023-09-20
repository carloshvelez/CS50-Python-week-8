from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 32)
        self.cell(80)
        self.cell(32, 40, "CS50 Shirtificate", align="C")
        self.ln(20)




def main():

    generar_shirtificate(input("Name: "))



def generar_shirtificate(nombre):
    pdf = PDF()
    pdf.set_auto_page_break(False)
    pdf.add_page()
    pdf.image("shirtificate.png", x=0, y=60)
    pdf.set_xy(x=8, y=120)
    pdf.set_font("helvetica", size=25)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, txt=f"{nombre} took CS50", align="C")
    pdf.output("shirtificate.pdf")










if __name__ == "__main__":
    main()