class Euler4:
    number_a = 0
    number_b = 0
    max_value = 0
    largest_palindrom = 0

    def run(self, number):
        self.number_a = int("1" + ("0" * (number - 1)))
        self.max_value = int("9" * number)

        while self.number_a <= self.max_value:
            self.number_b = self.number_a

            while self.number_b <= self.max_value:
                result = self.number_a * self.number_b

                if str(result) == str(result)[::-1] and result > self.largest_palindrom:
                    self.largest_palindrom = result

                self.number_b += 1

            self.number_a += 1

        return self.largest_palindrom
