import unittest
from contador import contador

class TestContador(unittest.TestCase):
    def test_simple(self):
        result = contador('hola')
        self.assertEqual(result, {'hola': 1})

    def test_complex(self):
        result = contador('Hola como estas hola')
        self.assertEqual(
            result,
            {
                'hola': 2,
                'como': 1,
                'estas': 1,
            },
        )

if __name__ == '__main__':
    unittest.main()