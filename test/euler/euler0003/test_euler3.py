# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0003.euler3 import Euler3

class TestEuler3(unittest.TestCase):
    def test_with_input_13_195(self):
        result = Euler3().run(13_195)
        assert result == 29

    def test_with_input_600_851_475_143(self):
        result = Euler3().run(600_851_475_143)
        assert result == 6857
