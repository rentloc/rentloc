import unittest
from scrapping import Scrap


class TestScrapping(unittest.TestCase):

    def test_run(self):
        self.assertEqual(Scrap.run(), None)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
