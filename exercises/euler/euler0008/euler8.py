class Euler8:
    def run(self, n):
        big_number = self.read_big_number()
        product = 0

        for position in range(1, len(big_number) - n):
            temp_product = 1
            for i in range(position - 1, position - 1 + n):
                temp_product *= int(big_number[i])

            if temp_product > product:
                product = temp_product

        return product

    def read_big_number(self):
        lines = ""

        with open("exercises/euler/euler0008/big_number.txt") as f:
            lines = f.readlines()

        return ''.join(lines).replace("\n", "")

