import unittest
import testing.main_file as mf


class mainTest(unittest.TestCase):
    def test_add_two_numbers(self):
        # given
        num1 = 10
        num2 = 20

        # when
        actual = mf.add_two_numbers(num1, num2)

        # then
        self.assertEqual(30, actual)

    def test_asset_an_error(self):
        # given
        num1 = 23
        num2 = 0

        # when
        actual = mf.add_two_numbers(num1, num2)

        # then
        self.assertRaises(Exception)

    def test_input(self):
        # please note in the video, I had the parameters flipped it should be the "guess" parameter 1st and "answer"
        # parameter 2nd
        result = mf.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = mf.run_guess(0, )
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = mf.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = mf.run_guess('11', 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
