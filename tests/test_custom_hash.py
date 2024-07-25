import unittest
from src.custom_hash import custom_hash

class TestCustomHash(unittest.TestCase):
    def test_custom_hash(self):
        self.assertEqual(custom_hash(b"Hello, world!"), "0x8ff0cbf5")

if __name__ == "__main__":
    unittest.main()

