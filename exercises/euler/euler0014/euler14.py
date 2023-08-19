class Euler14:
    maximum = 0
    start = 0

    def run(self):
        for number in range(1_000_001):
            count = Euler14.count_terms(number)
            if count > self.maximum:
                self.maximum = count
                self.start = number

        return self.start

    @staticmethod
    def count_terms(number):
        if number <= 0:
            return 0

        count = 1
        while number > 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = (3 * number) + 1
            count += 1

        return count
