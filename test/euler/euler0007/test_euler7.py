from exercises.euler.euler0007.euler7 import Euler7
import unittest

class TestEuler7(unittest.TestCase):
    def test_with_input_6(self):
        result = Euler7().run(6)
        assert(result == 13)

    def test_with_input_10_001(self):
        result = Euler7().run(10_001)
        assert(result == 104_743)
