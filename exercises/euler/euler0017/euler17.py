class Euler17:
    WORDS = [
        None,
        "one ",
        "two ",
        "three ",
        "four ",
        "five ",
        "six ",
        "seven ",
        "eight ",
        "nine ",
        "ten ",
        "eleven ",
        "twelve ",
        "thirteen ",
        "fourteen ",
        "fifteen ",
        "sixteen ",
        "seventeen ",
        "eighteen ",
        "nineteen "
    ]

    DECIMAL_WORDS = [
        None,
        None,
        "twenty ",
        "thirty ",
        "forty ",
        "fifty ",
        "sixty ",
        "seventy ",
        "eighty ",
        "ninety "
    ]

    total = 0

    def run(self, maximum):
        for number in range(1, maximum + 1):
            words = Euler17.in_words(number)
            words = words.replace(" ", "")
            self.total += len(words)

        return self.total

    @staticmethod
    def in_words(number):
        print(number)
        if number >= 1_000:
            return Euler17.big_number_in_words(number)

        if number >= 100:
            return Euler17.houndreds_in_word(number)

        if number >= 20:
            return (Euler17.DECIMAL_WORDS[int(number / 10)] + ' ' +
                    Euler17.in_words(int(number % 10)))

        if number >= 1:
            return Euler17.WORDS[number]

        return  ""

    @staticmethod
    def big_number_in_words(number):
        if number >= 1_000_000_000:
            return (Euler17.in_words(int(number / 1_000_000_000)) + "billion " +
                    Euler17.in_words(int(number % 1_000_000_000)))

        if number >= 1_000_000:
            return (Euler17.in_words(int(number / 1_000_000)) + "million " +
                    Euler17.in_words(int(number % 1_000_000)))

        return (Euler17.in_words(int(number / 1_000)) + "thousand " +
                Euler17.in_words(int(number % 1_000)))

    @staticmethod
    def houndreds_in_word(number):
        if number >= 100 and number % 100 == 0:
            return Euler17.in_words(int(number/ 100)) + "hundred "

        return (Euler17.in_words(int(number / 100)) + "hundred and " +
                Euler17.in_words(int(number % 100)))
