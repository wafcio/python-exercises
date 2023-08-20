class Euler18:
    triangle = None

    def run(self, input_data):
        self.triangle = Euler18.parse_data(input_data)
        return self.calculate_max_sum()

    def calculate_max_sum(self, point_x=0, point_y=0):
        if point_y == len(self.triangle) - 1:
            return self.triangle[point_y][point_x]

        values = [
            self.calculate_max_sum(point_x, point_y + 1),
            self.calculate_max_sum(point_x + 1, point_y + 1)
        ]
        values.sort()
        return values[-1] + self.triangle[point_y][point_x]

    @staticmethod
    def parse_data(lines):
        for position, line in enumerate(lines):
            lines[position] = line.replace("\n", "").split()
            for position2, number in enumerate(lines[position]):
                lines[position][position2] = int(number)

        return lines
