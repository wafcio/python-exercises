class Aoc2015Day1Part2:
    def run(self, input):
        level = 0
        position = 0

        for char in input:
            position += 1
            if char == "(":
                level += 1
            elif char == ")":
                level -= 1

            if level == -1:
                return position
