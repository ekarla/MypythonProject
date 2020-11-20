import unittest


from main.calculadoraPython import Calculator
class TestSimplesCalc(unittest.TestCase):
    def test_simpleadd(self):

        self.calc = Calculator(5, 4)
        self.assertEqual(9, self.calc.add())

    def test_simplesub(self):

        self.calc = Calculator(5, 4)
        self.assertEqual(1, self.calc.sub())

    def test_simpleaddFail(self):

        self.calc = Calculator(5, 4)
        self.assertEqual(6, self.calc.add())


if __name__ == '__main__':
    unittest.main()
