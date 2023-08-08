from exercises.euler.euler_0004.euler4 import Euler4
import unittest

class TestEuler4(unittest.TestCase):
    def test_euler4_first_example(self):
        result = Euler4().run(2)
        assert(result == 9009)

    def test_euler4_second_example(self):
        result = Euler4().run(3)
        assert(result == 906609)

if __name__ == "__main__":
    unittest.main()
