# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0016.euler16 import Euler16

class TestEuler16(unittest.TestCase):
    def test_with_input_15(self):
        result = Euler16().run(15)
        assert result == 26

    def test_with_input_1_000(self):
        result = Euler16().run(1_000)
        assert result == 1_366
