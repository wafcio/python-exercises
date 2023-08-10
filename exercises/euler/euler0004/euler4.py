class Euler4:
    def run(self, n):
        a = int("1" + ("0" * (n - 1)))
        b = 0
        largest_palindrom = 0

        while a <= int("9" * n):
            b = a

            while b <= int("9" * n):
                result = a * b

                if str(result) == str(result)[::-1] and result > largest_palindrom:
                    largest_palindrom = result

                b += 1

            a += 1

        return largest_palindrom
