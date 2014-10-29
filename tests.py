import unittest
from fizzbuzzKata import fizzbuzz
from primeFactorsKata import primeFactors
from romansKata import toRoman
from gatoKata import GetTablero, JuegoContinua, IntentarTirada, IniciaJuego
from gameOfLifeKata import GetUniverse, NextOfspring
from texasHoldEmKata import GetRankedGame

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
        
        self.u1 = "48............*......**..........."
        self.u1Ofspring1 = "........\n....*...\n...**...\n........\n"
        self.u1Ofspring2 = "........\n...**...\n...**...\n........\n"
        self.u1Ofspring3 = "........\n...**...\n...**...\n........\n"
        
        self.u2 = "99....*.*....**...*.....*....**....*......**...*......*.***.***....****..*..*..*..*"
        self.u2Ofspring1 = "....*.*..\n..**...*.\n....*....\n**....*..\n....**...\n*......*.\n***.***..\n..****..*\n..*..*..*\n"
        self.u2Ofspring2 = "...*.....\n...***...\n.***.....\n....*....\n**...**..\n*..*.....\n*.*...**.\n.......*.\n..*..*...\n"
        self.u2Ofspring3 = "...*.....\n.........\n..*..*...\n*..***...\n**..**...\n*.*..*.*.\n.*....**.\n.*.....*.\n.........\n"
        self.u2Ofspring4 = ".........\n.........\n...*.*...\n*.**..*..\n*.*......\n*.*.**.*.\n***....**\n......**.\n.........\n"
        self.u2Ofspring5 = ".........\n.........\n..***....\n..***....\n*.*.***..\n*.*...***\n*.**.*..*\n.*....***\n.........\n"
        self.u2Ofspring6 = ".........\n...*.....\n..*.*....\n.........\n..*.*.*..\n*.*.....*\n*.**.*...\n.**...***\n.......*.\n"
        self.u2Ofspring7 = ".........\n...*.....\n...*.....\n.....*...\n.*.*.....\n..*.**...\n*..*..*.*\n.***..***\n......***\n"
        self.u2Ofspring8 = ".........\n.........\n....*....\n..*.*....\n..**.*...\n.**.**...\n......*.*\n.***.*...\n..*...*.*\n"
        self.u2Ofspring9 = ".........\n.........\n...*.....\n..*.**...\n.....*...\n.**.***..\n......*..\n.***.**..\n.***.....\n"
        self.u2Ofspring10 = ".........\n.........\n...**....\n...***...\n.**......\n....*.*..\n.......*.\n.*.****..\n.*.**....\n"
        self.u2Ofspring11 = ".........\n.........\n...*.*...\n.....*...\n..*......\n.........\n...*...*.\n...*.**..\n...*.....\n"
        self.u2Ofspring12 = ".........\n.........\n....*....\n....*....\n.........\n.........\n....*.*..\n..**..*..\n....*....\n"
        self.u2Ofspring13 = ".........\n.........\n.........\n.........\n.........\n.........\n...*.*...\n...**....\n...*.....\n"
        self.u2Ofspring14 = ".........\n.........\n.........\n.........\n.........\n.........\n...*.....\n..**.....\n...**....\n"
        self.u2Ofspring15 = ".........\n.........\n.........\n.........\n.........\n.........\n..**.....\n..*......\n..***....\n"
        self.u2Ofspring16 = ".........\n.........\n.........\n.........\n.........\n.........\n..**.....\n.*..*....\n..**.....\n"
        
        self.texas1 = "Kc 9s Ks Kd 9d 3c 6d\n9c Ah Ks Kd 9d 3c 6d\nAc Qc Ks Kd 9d 3c\n9h 5s\n4d 2d Ks Kd 9d 3c 6d\n7s Ts Ks Kd 9d"
        self.texas1Result = "Kc 9s Ks Kd 9d 3c 6d Full House (winner)\n9c Ah Ks Kd 9d 3c 6d Two Pair\nAc Qc Ks Kd 9d 3c One Pair\n9h 5s\n4d 2d Ks Kd 9d 3c 6d Flush\n7s Ts Ks Kd 9d One Pair"
        self.texas2 = "9h 5s\n9c Ah 3c Kd 9d 3d 6d\nAc Qc Ks Kd 9d Ks\nKc 9s Ks Kd Kh 3c 6d\n4d 2d Ks Kd 9d 3c 6d\n7s Ts Ks Kd 9d"
        self.texas2Result = "9h 5s\n9c Ah 3c Kd 9d 3d 6d Two Pair\nAc Qc Ks Kd 9d Ks Three of a kind\nKc 9s Ks Kd Kh 3c 6d Poker (winner)\n4d 2d Ks Kd 9d 3c 6d Flush\n7s Ts Ks Kd 9d One Pair"
        
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
        
    def test_gameOfLife(self):
        self.assertEqual(GetUniverse(self.u1), self.u1Ofspring1)
        u = NextOfspring(self.u1)
        self.assertEqual(GetUniverse(u), self.u1Ofspring2)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u1Ofspring3)
        
        self.assertEqual(GetUniverse(self.u2), self.u2Ofspring1)
        u = NextOfspring(self.u2)
        self.assertEqual(GetUniverse(u), self.u2Ofspring2)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring3)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring4)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring5)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring6)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring7)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring8)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring9)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring10)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring11)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring12)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring13)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring14)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring15)
        u = NextOfspring(u)
        self.assertEqual(GetUniverse(u), self.u2Ofspring16)
        
    def test_texasHoldEmKata(self):
        self.assertEqual(GetRankedGame(self.texas1), self.texas1Result)
        self.assertEqual(GetRankedGame(self.texas2), self.texas2Result)

if __name__ == '__main__':
    unittest.main()
    
    
