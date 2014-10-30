_author_='Santiago'

def SumaDos():
    print 10 * 20

def divicion(a, b):
    result = a/b
    print result

def cast():
    i = 10
    f = 10.5

    int(10.5)
    print "funcion"

def main():
    SumaDos()
    divicion(100, 10)

from datetime import datetime

class Estudiante(object):
    """docstring for Estudiante"""
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio
    def diasDeVida(self):
        nacimiento = self.anio
        fecha = datetime.now()
        ahora = fecha.year
        vida = ahora - nacimiento
        return (vida * 365)

    def esMayor(self):
         if self.anio <=1998:
            return True
         else:
            return False

def main():
    e = Estudiante("Santiago", 1992)
    print "Hola soy %s y tengo %d dias de vida" % (e.nombre,e.diasDeVida())
    if e.esMayor():
        print "y soy mayor de edad"
    else:
        print "y soy menor de edad"

if __name__ == "__main__":
    main()
