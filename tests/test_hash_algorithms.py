import unittest
from src.hash_algorithms import sha256_hash

class TestHashAlgorithms(unittest.TestCase):
    def test_sha256_hash(self):
        self.assertEqual(sha256_hash(b"Hello, world!"), "315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3")

if __name__ == "__main__":
    unittest.main()

