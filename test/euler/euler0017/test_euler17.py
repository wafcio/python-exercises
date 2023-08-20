# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0017.euler17 import Euler17

class TestEuler17(unittest.TestCase):
    def test_with_input_5(self):
        result = Euler17().run(5)
        assert result == 19

    def test_with_input_1_000(self):
        result = Euler17().run(1_000)
        assert result == 21_124
