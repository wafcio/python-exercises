class Aoc2015Day1Part1:
    def run(self, input):
        level = 0

        for char in input:
            if char == "(":
              level += 1
            elif char == ")":
              level -= 1

        return level
