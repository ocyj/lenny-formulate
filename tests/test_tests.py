import unittest


class TestTests(unittest.TestCase):
    def test_assert_with_lists(self):
        l = [1,2,3]
        self.assertEquals(l, list(l))
        self.assertEqual(7,7)
        self.assertFalse(l is list(l))

if __name__ == '__main__':
    unittest.main()