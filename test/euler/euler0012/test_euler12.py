# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0012.euler12 import Euler12

class TestEuler12(unittest.TestCase):
    def test_with_input_5(self):
        result = Euler12().run(5)
        assert result == 28

    def test_with_input_100(self):
        result = Euler12().run(100)
        assert result == 73_920

    def test_with_input_500(self):
        result = Euler12().run(500)
        assert result == 76_576_500
