# https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-c/
# can use this page to change the expected results from the second test


import unittest
from unittest.mock import patch
from exchangerates import CountRate, GetCurrency



def test_CountRate():
    results = (4.5014, "s")
    amount = 100
    expected_result = 450.14
    actual_result = CountRate(results, amount)

    assert expected_result == actual_result



class TestGetCurrency(unittest.TestCase):

    @patch('builtins.input', return_value="EUR")
    def test_once_GetCurrency(self, mock_input):
        calling = GetCurrency()
        self.assertEqual(calling, (4.3782, 4.4666))

    @patch('builtins.input', side_effect=["EUR", "USD", "GBP"])
    def test_multiple_GetCurrency(self, mock_input):
        calling1 = GetCurrency()
        calling2 = GetCurrency()
        calling3 = GetCurrency()
        self.assertTrue(calling1 == (4.3782, 4.4666) and calling2 == (3.9772, 4.0576) and calling3 == (5.1129, 5.2161))


