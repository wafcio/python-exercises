from exercises.euler.euler0002.euler2 import Euler2
import unittest

class TestEuler2(unittest.TestCase):
    def test_with_input_4_000_000(self):
        result = Euler2().run(4_000_000)
        assert(result == 4_613_732)
