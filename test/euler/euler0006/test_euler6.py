from exercises.euler.euler0006.euler6 import Euler6
import unittest

class TestEuler6(unittest.TestCase):
    def test_with_input_10(self):
        result = Euler6().run(10)
        assert(result == 2_640)

    def test_with_input_100(self):
        result = Euler6().run(100)
        assert(result == 25_164_150)
