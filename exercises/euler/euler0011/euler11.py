class Euler11:
    big_number = None
    product = 0

    def run(self):
        self.big_number = Euler11.read_big_number()

        self.check_horizontally_and_vertically()
        self.check_diagonally()

        return self.product

    @staticmethod
    def read_big_number():
        lines = ""

        with open("exercises/euler/euler0011/grid.txt") as file:
            lines = file.readlines()

        for position in range(0, 20):
            lines[position] = lines[position].replace("\n", "").split()

        return lines

    def check_horizontally_and_vertically(self):
        for num1 in range(0, 20):
            for num2 in range(0, 17):
                new_product = 1
                for index in range(0, 4):
                    new_product *= int(self.big_number[num1][num2 + index])
                self.memoize_greater(new_product)

                new_product = 1
                for index in range(0, 4):
                    new_product *= int(self.big_number[num2 + index][num1])
                self.memoize_greater(new_product)

    def check_diagonally(self):
        for num1 in range(0, 17):
            for num2 in range(0, 17):
                new_product = 1
                for index in range(0, 4):
                    new_product *= int(self.big_number[num1 + index][num2 + index])
                self.memoize_greater(new_product)

                new_product = 1
                for index in range(0, 4):
                    new_product *= int(self.big_number[num1 + 3 - index][num2 + index])
                self.memoize_greater(new_product)

    def memoize_greater(self, new_product):
        if new_product > self.product:
            self.product = new_product
