# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0004.euler4 import Euler4

class TestEuler4(unittest.TestCase):
    def test_with_input_2(self):
        result = Euler4().run(2)
        assert result == 9_009

    def test_with_input_3(self):
        result = Euler4().run(3)
        assert result == 906_609
