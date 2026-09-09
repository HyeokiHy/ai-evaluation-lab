from regression_detector import detect_status, compare_results



def test_detect_regression():
    previous_passed = True
    current_passed = False

    status = detect_status(previous_passed, current_passed)

    assert status == "regression"

def test_detect_recovered():
    previous_passed = False
    current_passed = True

    status = detect_status(previous_passed, current_passed)

    assert status == "recovered"

def test_detect_unchanged_passed():
    previous_passed = True
    current_passed = True

    status = detect_status(previous_passed, current_passed)

    assert status == "unchanged"

def test_detect_unchanged_fail():
    previous_passed = False
    current_passed = False

    status = detect_status(previous_passed, current_passed)

    assert status == "unchanged"

def test_compare_results():
    previous_results = [
        {
            "id": "INTENT-001",
            "passed": True,
        },
        {
            "id": "INTENT-002",
            "passed": False,
        },
    ]

    current_results = [
        {
            "id": "INTENT-001",
            "passed": False,
        },
        {
            "id": "INTENT-002",
            "passed": True,
        },
    ]

    result = compare_results(previous_results, current_results)

    assert result == [
        {
            "id": "INTENT-001",
            "status": "regression",
        },
        {
            "id": "INTENT-002",
            "status": "recovered",
        },
    ]

def test_compare_results_new_case():
    previous_results = [
        {
            "id": "INTENT-001",
            "passed": True,
        },
    ]

    current_results = [
        {
            "id": "INTENT-001",
            "passed": True,
        },
        {
            "id": "INTENT-002",
            "passed": True,
        },
    ]

    result = compare_results(previous_results, current_results)

    assert result == [
        {
            "id": "INTENT-001",
            "status": "unchanged",
        },
        {
            "id": "INTENT-002",
            "status": "new",
        },
    ]

def test_compare_results_removed_case():
    previous_results = [
        {
            "id": "INTENT-001",
            "passed": True,
        },
        {
            "id": "INTENT-002",
            "passed": True,
        },
    ]

    current_results = [
        {
            "id": "INTENT-001",
            "passed": True,
        },
    ]

    result = compare_results(previous_results, current_results)

    assert result == [
        {
            "id": "INTENT-001",
            "status": "unchanged",
        },
        {
            "id": "INTENT-002",
            "status": "removed",
        },
    ]