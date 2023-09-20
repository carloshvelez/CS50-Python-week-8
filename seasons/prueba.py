from datetime import date
from datetime import datetime
import inflect
import re
import sys

p = inflect.engine()
formato = "%Y-%m-%d"

def main():

    fecha = input("Date of birth: ")

    print(validar(fecha))



def validar(cadena):

    return datetime.strptime(cadena, formato).date()
        #validacion = re.search(r"^(\d{4})-(\d{1,2})-(\d{1,2}$)", fecha)
        #año, mes, dia = validacion.groups()

main()





#fecha = "1986-28-08"



#print(validacion.groups())


"""print((date.today() - date(2022, 2, 20)).days)

print((date.today() - date(2022, 2, 20)).days)

print(p.number_to_words((date.today() - date(2022, 2, 20)).days * 24 * 60, andword = ""), "minutes")"""


