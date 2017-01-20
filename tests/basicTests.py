import unittest
import junit


class TestBasicStuff(unittest.TestCase):

    def testNothing(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
