# pylint: disable=no-self-use

import unittest

from exercises.euler.euler0018.euler18 import Euler18

class TestEuler18(unittest.TestCase):
    def test_with_small_tree(self):
        lines = ""
        with open("test/support/euler/euler0018/small_tree.txt") as file:
            lines = file.readlines()

        result = Euler18().run(lines)
        assert result == 23

    def test_with_big_tree(self):
        lines = ""
        with open("test/support/euler/euler0018/big_tree.txt") as file:
            lines = file.readlines()

        result = Euler18().run(lines)
        assert result == 1_074
