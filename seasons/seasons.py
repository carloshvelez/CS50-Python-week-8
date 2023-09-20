from datetime import date
from datetime import datetime
import inflect
import sys

p = inflect.engine()
formato = "%Y-%m-%d"

def main():

    fecha = input("Date of birth: ")
    print(cantar(validar(fecha)))



def validar(cadena):
    try:
        return datetime.strptime(cadena, formato).date()
    except ValueError:
        sys.exit("Invalid Date")



def cantar(fecha):
    diferencia = (date.today() - fecha).days * 24 * 60
    cadena = p.number_to_words(diferencia, andword = "")
    return f"{cadena.capitalize()} minutes"




if __name__ == "__main__":
    main()














#print((date.today() - date(2022, 2, 20)).days)

#print((date.today() - date(2022, 2, 20)).days)

#print(p.number_to_words((date.today() - date(2022, 2, 20)).days * 24 * 60, andword = ""), "minutes")



