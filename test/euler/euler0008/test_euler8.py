# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0008.euler8 import Euler8

class TestEuler8(unittest.TestCase):
    def test_with_input_4(self):
        result = Euler8().run(4)
        assert result == 5_832

    def test_with_input_13(self):
        result = Euler8().run(13)
        assert result == 23_514_624_000
