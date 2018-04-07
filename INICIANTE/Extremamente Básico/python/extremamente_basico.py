import unittest

class Basico():

    def _print(self):
        return "teste"

class TestBasico(unittest.TestCase):

    def test_upper(self):
        basico = Basico()

        self.assertEqual('teste1', basico._print())

if __name__ == '__main__':
    unittest.main()
