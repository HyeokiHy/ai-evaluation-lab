from evaluator import evaluate_exact_match, evaluate_contains

def test_exact_match_pass():
    actual = "delivery"
    expected = "delivery"

    result = evaluate_exact_match(actual, expected)

    assert result is True

def test_exact_match_fail():
    actual = "refund"
    expected = "delivery"

    result = evaluate_exact_match(actual, expected)

    assert result is False

def test_contains_pass():
    actual = "현재 intent는 delivery 입니다"
    expected = "delivery"

    result = evaluate_contains(actual, expected)

    assert result is True

def test_contains_fail():
    actual = "현재 intent는 refund 입니다"
    expected = "delivery"

    result = evaluate_contains(actual, expected)

    assert result is False