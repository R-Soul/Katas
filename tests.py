import unittest
from fizzbuzzKata import fizzbuzz
from primeFactorsKata import primeFactors
from romansKata import toRoman
from gatoKata import GetTablero, JuegoContinua, IntentarTirada, IniciaJuego

class TestKatas(unittest.TestCase):
    
    def setUp(self):
        self.fizzBuzzSeq = {1: "1", 2:"2", 3:"fizz",
                            4: "4", 5: "buzz", 6: "fizz",
                            10: "buzz", 15: "fizzbuzz"}
        self.primeFactorSeq = {1: [], 2: [2], 3: [3],
                            4: [2,2], 5: [5], 6: [2,3],
                            7: [7], 8: [2,2,2], 9: [3,3]}
        self.romanSeq = {1: "I", 2: "II", 3: "III",
                            4: "IV", 5: "V", 6: "VI",
                            7: "VII", 8: "VIII", 9: "IX", 100: "C",
                            56: "LVI", 143: "CXLIII", 678: "DCLXXVIII",
                            999: "CMXCIX", 1583: "MDLXXXIII", 3982: "MMMCMLXXXII"}
        self.tableroVacio = " 1 │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "
        self.errFueraRango = "La tirada debe de estar entre 1 y 9"
        self.errOcupada = "La casilla ya esta ocupada"
        self.xGana = "Felicidades X as ganado. weeee"
        self.oGana = "Felicidades O as ganado. weeee"
        self.empate = "Juego empatado. :("
        
        self.tableroXuno = " X │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "
        self.tableroXdos = " X │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n O │ 8 │ 9 "
        self.tableroXtres = " X │ 2 │ 3 \n───┼───┼───\n 4 │ X │ 6 \n───┼───┼───\n O │ 8 │ 9 "
        self.tableroXcuatro = " X │ 2 │ 3 \n───┼───┼───\n O │ X │ 6 \n───┼───┼───\n O │ 8 │ 9 "
        self.tableroXcinco = " X │ 2 │ 3 \n───┼───┼───\n O │ X │ 6 \n───┼───┼───\n O │ 8 │ X "
        
        self.tableroOuno = " X │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "
        self.tableroOdos = " X │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n O │ 8 │ 9 "
        self.tableroOtes = " X │ 2 │ 3 \n───┼───┼───\n X │ 5 │ 6 \n───┼───┼───\n O │ 8 │ 9 "
        self.tableroOcuatro = " X │ 2 │ 3 \n───┼───┼───\n X │ O │ 6 \n───┼───┼───\n O │ 8 │ 9 "
        self.tableroOcinco = " X │ X │ 3 \n───┼───┼───\n X │ O │ 6 \n───┼───┼───\n O │ 8 │ 9 "
        self.tableroOseis = " X │ X │ O \n───┼───┼───\n X │ O │ 6 \n───┼───┼───\n O │ 8 │ 9 "
        
        self.tableroEmpateUno = " X │ 2 │ 3 \n───┼───┼───\n 4 │ O │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "
        self.tableroEmpateDos = " X │ 2 │ 3 \n───┼───┼───\n 4 │ O │ 6 \n───┼───┼───\n X │ 8 │ 9 "
        self.tableroEmpateTres = " X │ 2 │ 3 \n───┼───┼───\n O │ O │ 6 \n───┼───┼───\n X │ 8 │ 9 "
        self.tableroEmpateCuatro = " X │ 2 │ 3 \n───┼───┼───\n O │ O │ X \n───┼───┼───\n X │ 8 │ 9 "
        self.tableroEmpateCinco = " X │ O │ 3 \n───┼───┼───\n O │ O │ X \n───┼───┼───\n X │ 8 │ 9 "
        self.tableroEmpateSeis = " X │ O │ 3 \n───┼───┼───\n O │ O │ X \n───┼───┼───\n X │ X │ 9 "
        self.tableroEmpateSiete = " X │ O │ 3 \n───┼───┼───\n O │ O │ X \n───┼───┼───\n X │ X │ O "
        self.tableroEmpateOcho = " X │ O │ X \n───┼───┼───\n O │ O │ X \n───┼───┼───\n X │ X │ O "
      
    def test_fizzbuzz(self):
        for x in self.fizzBuzzSeq.items():
            self.assertEqual(fizzbuzz(x[0]), x[1])
            
    def test_primerFactors(self):
        for x in self.primeFactorSeq.items():
            self.assertEqual(primeFactors(x[0]), x[1])
    
    def test_toRoman(self):
        for k,v in self.romanSeq.items():
            self.assertEqual(toRoman(k),v)

    def test_gatoXGana(self):
        IniciaJuego()
        self.assertEqual(GetTablero(), self.tableroVacio)
        self.assertTrue(JuegoContinua())
        self.assertEqual(IntentarTirada(30), self.errFueraRango)
        self.assertEqual(IntentarTirada(1), "")
        self.assertEqual(GetTablero(), self.tableroXuno)
        self.assertEqual(IntentarTirada(1), self.errOcupada)
        self.assertEqual(IntentarTirada(7), "")
        self.assertEqual(GetTablero(), self.tableroXdos)
        self.assertEqual(IntentarTirada(5), "")
        self.assertEqual(GetTablero(), self.tableroXtres)
        self.assertEqual(IntentarTirada(4), "")
        self.assertEqual(GetTablero(), self.tableroXcuatro)
        self.assertEqual(IntentarTirada(9), self.xGana)
        self.assertEqual(GetTablero(), self.tableroXcinco)
        
    def test_gatoOGana(self):
        IniciaJuego()
        self.assertEqual(GetTablero(), self.tableroVacio)
        self.assertTrue(JuegoContinua())
        self.assertEqual(IntentarTirada(30), self.errFueraRango)
        self.assertEqual(IntentarTirada(1), "")
        self.assertEqual(GetTablero(), self.tableroOuno)
        self.assertEqual(IntentarTirada(1), self.errOcupada)
        self.assertEqual(IntentarTirada(7), "")
        self.assertEqual(GetTablero(), self.tableroOdos)
        self.assertEqual(IntentarTirada(4), "")
        self.assertEqual(GetTablero(), self.tableroOtes)
        self.assertEqual(IntentarTirada(5), "")
        self.assertEqual(GetTablero(), self.tableroOcuatro)
        self.assertEqual(IntentarTirada(2), "")
        self.assertEqual(GetTablero(), self.tableroOcinco)
        self.assertEqual(IntentarTirada(3), self.oGana)
        self.assertEqual(GetTablero(), self.tableroOseis)

    def test_gatoEmpate(self):
        IniciaJuego()
        self.assertEqual(GetTablero(), self.tableroVacio)
        self.assertTrue(JuegoContinua())
        self.assertEqual(IntentarTirada(30), self.errFueraRango)
        self.assertEqual(IntentarTirada(1), "")
        self.assertEqual(GetTablero(), self.tableroXuno)
        self.assertEqual(IntentarTirada(1), self.errOcupada)
        self.assertEqual(IntentarTirada(5), "")
        self.assertEqual(GetTablero(), self.tableroEmpateUno)
        self.assertEqual(IntentarTirada(7), "")
        self.assertEqual(GetTablero(), self.tableroEmpateDos)
        self.assertEqual(IntentarTirada(4), "")
        self.assertEqual(GetTablero(), self.tableroEmpateTres)
        self.assertEqual(IntentarTirada(6), "")
        self.assertEqual(GetTablero(), self.tableroEmpateCuatro)
        self.assertEqual(IntentarTirada(2), "")
        self.assertEqual(GetTablero(), self.tableroEmpateCinco)
        self.assertEqual(IntentarTirada(8), "")
        self.assertEqual(GetTablero(), self.tableroEmpateSeis)
        self.assertEqual(IntentarTirada(9), "")
        self.assertEqual(GetTablero(), self.tableroEmpateSiete)
        self.assertEqual(IntentarTirada(3), self.empate)
        self.assertEqual(GetTablero(), self.tableroEmpateOcho)
        
if __name__ == '__main__':
    unittest.main()

    
