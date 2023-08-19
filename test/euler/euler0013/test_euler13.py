# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0013.euler13 import Euler13

class TestEuler13(unittest.TestCase):
    def test_with_input_from_file(self):
        result = Euler13().run()
        assert result == "5537376230"
