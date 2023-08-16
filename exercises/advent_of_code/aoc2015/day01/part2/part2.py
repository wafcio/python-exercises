class Aoc2015Day1Part2:
    level = 0
    position = 0

    def run(self, input_data):
        for char in input_data:
            self.position += 1
            if char == "(":
                self.level += 1
            elif char == ")":
                self.level -= 1

            if self.level == -1:
                break

        return self.position
