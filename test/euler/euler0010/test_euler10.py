from exercises.euler.euler0010.euler10 import Euler10
import unittest

class TestEuler10(unittest.TestCase):
    def test_with_input_10(self):
        result = Euler10().run(10)
        assert(result == 17)

    def test_with_input_2_000_000(self):
        result = Euler10().run(2_000_000)
        assert(result == 142_913_828_922)
