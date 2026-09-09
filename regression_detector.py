def detect_status(previous_passed: bool, current_passed: bool) -> str:
    if previous_passed and not current_passed:
        return "regression"

    if not previous_passed and current_passed:
        return "recovered"

    return "unchanged"

def compare_results(previous_results, current_results):
    comparison = []

    previous_map = {
        result["id"]: result
        for result in previous_results
    }

    current_map = {
        result["id"]: result
        for result in current_results
    }

    for current in current_results:
        current_id = current["id"]

        if current_id not in previous_map:
            comparison.append(
                {
                    "id": current_id,
                    "status": "new",
                }
            )
            continue

        previous = previous_map[current_id]

        status = detect_status(
                previous["passed"],
                current["passed"],
        )

        comparison.append(
            {
                "id": current_id,
                "status": status,
            }
        )

    for previous_id in previous_results:
        previous_id = previous_id["id"]

        if previous_id not in current_map:
            comparison.append(
                {
                    "id": previous_id,
                    "status": "removed",
                }
            )

    return comparison