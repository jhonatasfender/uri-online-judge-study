import unittest

class Basico():

    def sum(self, a, b):
        return "X = " + str(int(a) + int(b))

class TestBasico(unittest.TestCase):

    def test_upper(self):
        basico = Basico()
        print(basico.sum(input(), input()))
        self.assertEqual('X = 19', basico.sum(10, 9))
        self.assertEqual('X = -6', basico.sum(-10, 4))
        self.assertEqual('X = 8', basico.sum(15, -7))

if __name__ == '__main__':
    unittest.main()
