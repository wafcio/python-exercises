# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0014.euler14 import Euler14

class TestEuler14(unittest.TestCase):
    def test_with_big_number(self):
        result = Euler14().run()
        assert result == 837_799
