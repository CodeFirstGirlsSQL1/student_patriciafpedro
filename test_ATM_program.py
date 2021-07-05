import unittest
from unittest import mock

from ATM_program import verify_pin, log_in, run_atm


class TestPinFunction(unittest.TestCase):
    def test_pin_success(self):
        expected = True
        result = verify_pin('1234')
        self.assertEqual(expected, result)

    def test_pin_failure(self):
        expected = False
        result = verify_pin('0000')
        self.assertEqual(expected, result)

class TestLogInFunction(unittest.TestCase):
    @mock.patch('ATM_program.get_input')
    def test_log_in_success(self, mock_get_input):
        mock_get_input.return_value = '1234'
        expected = True
        result = log_in()
        self.assertEqual(expected, result)

    @mock.patch('ATM_program.get_input')
    def test_log_in_failure(self, mock_get_input):
        mock_get_input.return_value = '9586'
        expected = False
        result = log_in()
        self.assertEqual(expected, result)

class TestWithdrawalFunction(unittest.TestCase):
    @mock.patch('ATM_program.log_in')
    def test_withdrawal_success(self, mock_log_in):
        mock_log_in.return_value = True
        expected = 70
        result = run_atm(30)
        self.assertEqual(expected, result)

    @mock.patch('ATM_program.log_in')
    def test_withdrawal_exception(self, mock_log_in):
        mock_log_in.return_value = True
        self.assertRaises(ValueError, run_atm, 110)

if __name__ == '__main__':
    unittest.main()
