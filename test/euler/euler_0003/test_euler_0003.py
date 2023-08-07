from exercises.euler.euler_0003.euler_0003 import Euler3
import unittest

class TestEuler3(unittest.TestCase):
    def test_euler3_first_example(self):
        result = Euler3().run(13195)
        assert(result == 29)

    def test_euler3_second_example(self):
        result = Euler3().run(600851475143)
        assert(result == 6857)

if __name__ == "__main__":
    unittest.main()
