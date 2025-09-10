import unittest
from s14l import shorten_name

class TestShortenName(unittest.TestCase):
    def test_andreessen_horowitz(self):
        self.assertEqual(shorten_name("Andreessen Horowitz"), "a16z")

    def test_dean_cirielli(self):
        self.assertEqual(shorten_name("Dean Cirielli"), "d10i")

if __name__ == '__main__':
    unittest.main()
