def evaluate_exact_match(actual: str, expected: str) -> bool:
    """
    실제 결과와 기대 결과가 정확히 일치하는지 평가합니다.

    Args:
        actual: 실제 반환된 값
        expected: 기대하는 값

    Returns:
        두 값이 정확히 일치하면 True, 아니면 False
    """
    return actual == expected


def evaluate_contains(actual: str, expected: str) -> bool:
    """
    실제 결과에 기대 값이 포함되어 있는지 평가합니다.

    Args:
        actual: 실제 반환된 문자열
        expected: 포함 여부를 확인할 문자열

    Returns:
        expected가 actual에 포함되어 있으면 True, 아니면 False
    """
    return expected in actual
