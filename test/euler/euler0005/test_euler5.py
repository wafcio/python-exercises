# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0005.euler5 import Euler5

class TestEuler5(unittest.TestCase):
    def test_with_input_10(self):
        result = Euler5().run(10)
        assert result == 2_520

    def test_with_input_20(self):
        result = Euler5().run(20)
        assert result == 232_792_560
