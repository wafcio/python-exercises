class Euler8:
    product = 0

    def run(self, number):
        big_number = Euler8.read_big_number()

        for position in range(1, len(big_number) - number):
            temp_product = 1
            for i in range(position - 1, position - 1 + number):
                temp_product *= int(big_number[i])

            if temp_product > self.product:
                self.product = temp_product

        return self.product

    @staticmethod
    def read_big_number():
        lines = ""

        with open("exercises/euler/euler0008/big_number.txt") as file:
            lines = file.readlines()

        return ''.join(lines).replace("\n", "")
