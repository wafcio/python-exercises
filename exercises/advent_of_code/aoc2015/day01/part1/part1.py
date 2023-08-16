class Aoc2015Day1Part1:
    level = 0

    def run(self, input_data):
        for char in input_data:
            if char == "(":
                self.level += 1
            elif char == ")":
                self.level -= 1

        return self.level
