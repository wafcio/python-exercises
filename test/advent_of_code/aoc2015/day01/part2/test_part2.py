from exercises.advent_of_code.aoc2015.day_01.part2.part2 import Aoc2015Day1Part2
import unittest

class TestAoc2015Day1Part2(unittest.TestCase):
    def test_first_example(self):
        result = Aoc2015Day1Part2().run(")")
        assert(result == 1)

    def test_second_example(self):
        result = Aoc2015Day1Part2().run("()())")
        assert(result == 5)

    def test_third_example(self):
        input_data = ""
        with open("test/support/advent_of_code/aoc2015/day01/input.txt") as f:
            lines = f.readlines()
        input_data = lines[0]

        result = Aoc2015Day1Part2().run(input_data)
        assert(result == 1795)

if __name__ == "__main__":
    unittest.main()
