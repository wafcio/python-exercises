# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0015.euler15 import Euler15

class TestEuler15(unittest.TestCase):
    def test_with_input_2(self):
        result = Euler15().run(2)
        assert result == 6

    def test_with_input_20(self):
        result = Euler15().run(20)
        assert result == 137_846_528_820
