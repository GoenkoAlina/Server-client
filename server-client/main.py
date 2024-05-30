import unittest


class UnitTests(unittest.TestCase):
    def test_name(self):
        self.assertEqual(1, 1)


def main():
    unittest.main()
    

if __name__ == "__main__":
    main()
