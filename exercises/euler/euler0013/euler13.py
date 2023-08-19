class Euler13:
    def run(self):
        big_numbers = self.read_big_numbers()
        total = 0
        for number in big_numbers:
            total += int(number)

        return str(total)[0:10:]


    @staticmethod
    def read_big_numbers():
        lines = ""

        with open("exercises/euler/euler0013/big_numbers.txt") as file:
            lines = file.readlines()

        for position, line in enumerate(lines):
            lines[position] = line.replace("\n", "")

        return lines
