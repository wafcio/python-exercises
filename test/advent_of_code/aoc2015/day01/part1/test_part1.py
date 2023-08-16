# pylint: disable=no-self-use

import unittest

from exercises.advent_of_code.aoc2015.day01.part1.part1 import Aoc2015Day1Part1

class TestAoc2015Day1Part1(unittest.TestCase):
    def test_first_example(self):
        result = Aoc2015Day1Part1().run("(())")
        assert result == 0

    def test_second_example(self):
        result = Aoc2015Day1Part1().run("()()")
        assert result == 0

    def test_third_example(self):
        result = Aoc2015Day1Part1().run("(((")
        assert result == 3

    def test_fourth_example(self):
        result = Aoc2015Day1Part1().run("(()(()(")
        assert result == 3

    def test_fifth_example(self):
        result = Aoc2015Day1Part1().run("))(((((")
        assert result == 3

    def test_sixth_example(self):
        result = Aoc2015Day1Part1().run("())")
        assert result == -1

    def test_seventh_example(self):
        result = Aoc2015Day1Part1().run("))(")
        assert result == -1

    def test_eighth_example(self):
        result = Aoc2015Day1Part1().run(")))")
        assert result == -3

    def test_ninth_example(self):
        result = Aoc2015Day1Part1().run(")())())")
        assert result == -3

    def test_tenth_example(self):
        input_data = ""
        with open("test/support/advent_of_code/aoc2015/day01/input.txt") as file:
            lines = file.readlines()
        input_data = lines[0]

        result = Aoc2015Day1Part1().run(input_data)
        assert result == 74
