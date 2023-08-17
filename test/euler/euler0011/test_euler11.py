# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0011.euler11 import Euler11

class TestEuler11(unittest.TestCase):
    def test_with_big_input(self):
        result = Euler11().run()
        assert result == 70_600_674
