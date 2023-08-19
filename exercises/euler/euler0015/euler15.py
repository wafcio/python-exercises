class Euler15:
    grid = None

    def run(self, size):
        self.grid = Euler15.prepare_grid(size)

        for i in range(1, size + 1):
            for j in range(1, size + 1):
                self.grid[i][j] = self.grid[i - 1][j] + self.grid[i][j - 1]

        return self.grid[size][size]

    @staticmethod
    def prepare_grid(size):
        grid = [[0] * (size + 1)] * (size + 1)

        for position in range(0, size + 1):
            grid[position][0] = 1
            grid[0][position] = 1

        return grid
