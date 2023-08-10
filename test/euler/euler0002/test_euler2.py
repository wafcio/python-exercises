from exercises.euler.euler0002.euler2 import Euler2
import unittest

class TestEuler2(unittest.TestCase):
    def test_euler2(self):
        result = Euler2().run()
        assert(result == 4_613_732)
