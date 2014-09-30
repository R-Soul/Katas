import unittest
from fizzbuzzKata import fizzbuzz
from primeFactorsKata import primeFactors
from romansKata import toRoman

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

    def test_fizzbuzz(self):
        for x in self.fizzBuzzSeq.items():
            self.assertEqual(fizzbuzz(x[0]), x[1])
            
    def test_primerFactors(self):
        for x in self.primeFactorSeq.items():
            self.assertEqual(primeFactors(x[0]), x[1])
    
    def test_toRoman(self):
        for k,v in self.romanSeq.items():
            self.assertEqual(toRoman(k),v)

if __name__ == '__main__':
    unittest.main()
    
    
