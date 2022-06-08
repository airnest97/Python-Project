import unittest


class PlaygroundTest(unittest.TestCase):
    def setUp(self) -> None:
        print('I run before')
        self.assertEqual(True, False)  # add assertion here

    def tearDown(self) -> None:
        print("I run after")


if __name__ == '__main__':
    unittest.main()
