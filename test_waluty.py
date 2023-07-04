from exchangerates import CountRate

def test_CountRate():
    results = (4.5014, "s")
    amount = 100
    expected_result = 450.14
    actual_result = CountRate(results, amount)

    assert expected_result == actual_result


