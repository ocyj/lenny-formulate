import unittest
import board


class TestLine(unittest.TestCase):

    io_pairs = (
    # INPUT    EXPECTED OUTPUT
    # All zeroes:
        ([0, 0, 0, 0], [0, 0, 0, 0]),
    # One distinct tile, three zeroes
        ([0, 0, 0, 1], [0, 0, 0, 1]),
        ([0, 0, 1, 0], [0, 0, 0, 1]),
        ([0, 1, 0, 0], [0, 0, 0, 1]),
        ([1, 0, 0, 0], [0, 0, 0, 1]),
        ([0, 0, 0, 2], [0, 0, 0, 2]),
        ([0, 0, 2, 0], [0, 0, 0, 2]),
        ([0, 2, 0, 0], [0, 0, 0, 2]),
        ([2, 0, 0, 0], [0, 0, 0, 2])
    )

    def test_swipe(self):
        for i, o in self.io_pairs:
            self.assertEqual(self, board.swipe(i), o)

if __name__ == '__main__':
    unittest.main()
