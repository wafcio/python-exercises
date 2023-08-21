# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0020.euler20 import Euler20

class TestEuler20(unittest.TestCase):
    def test_with_input_10(self):
        result = Euler20().run(10)
        assert result == 27

    def test_with_input_100(self):
        result = Euler20().run(100)
        assert result == 648
