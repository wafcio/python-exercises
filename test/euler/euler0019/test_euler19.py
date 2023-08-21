# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0019.euler19 import Euler19

class TestEuler19(unittest.TestCase):
    def test(self):
        result = Euler19().run()
        assert result == 171
