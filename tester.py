import unittest
from pension import *

class pruebaa(unittest.TestCase):

    # CASO 1: Fecha supera los 140 anos de edad
    def test1(self):
        self.assertEqual(CalcularEdad(datetime.date(1794,12,13)), False)

    # CASO 2: fecha invalida
    def test2(self):
        self.assertEqual(CalcularEdad(datetime.date(3000,122,13)), False)

    # CASO 3: La fecha es correcta
    def test3(self):
        self.assertEqual(CalcularEdad(datetime.date(1994,12,13)), True)

    # CASO 4: Pensionado falla porque no cumple la edad minima
    def test4(self):
        self.assertEqual(pensionado("h",50,340,50), False)

if __name__ == '__main__':
    unittest.main()