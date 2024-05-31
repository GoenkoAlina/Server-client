import unittest
from hamming import encode, decode, do_error


class UnitTests(unittest.TestCase):
    def test_no_error(self):
        self.assertEqual('Hello!', decode(encode('Hello!')))

    def test_errors(self):
        self.assertEqual('Hello!', decode(do_error(encode('Hello!'))))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
