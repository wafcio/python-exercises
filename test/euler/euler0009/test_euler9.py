from exercises.euler.euler0009.euler9 import Euler9
import unittest

class TestEuler9(unittest.TestCase):
    def test_with_input_12(self):
        result = Euler9().run(12)
        assert(result == 60)

    def test_with_input_1_000(self):
        result = Euler9().run(1_000)
        assert(result == 31_875_000)
