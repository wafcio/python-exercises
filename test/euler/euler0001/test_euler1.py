from exercises.euler.euler0001.euler1 import Euler1
import unittest

class TestEuler1(unittest.TestCase):
    def test_with_input_10(self):
        result = Euler1().run(10)
        assert(result == 23)

    def test_with_input_1_000(self):
        result = Euler1().run(1_000)
        assert(result == 233_168)
