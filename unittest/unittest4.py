import unittest


def doblar(a): return a*2
def sumar(a, b): return a+b
def es_par(a): return 1 if a % 2 == 0 else 0


class PruebasFunciones(unittest.TestCase):

    def test_doblar(self):
        self.assertEqual(doblar(10), 20)
        self.assertEqual(doblar('Ab'), 'AbAb')

    def test_sumar(self):
        self.assertEqual(sumar(-15, 15), 0)
        self.assertEqual(sumar('Ab', 'cd'), 'Abcd')

    def test_es_par(self):
        self.assertEqual(es_par(11), False)
        self.assertEqual(es_par(68), True)


if __name__ == '__main__':
    unittest.main()
