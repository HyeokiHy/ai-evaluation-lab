import json
from pathlib import Path

from intent_classifier import classify_intent
from evaluator import evaluate_exact_match, evaluate_contains
from datetime import datetime

EVALUATORS = {
    "contains": evaluate_contains,
    "exact_match": evaluate_exact_match,
}

def load_cases():
    dataset_path = Path("datasets") / "intent_cases.json"

    with open(dataset_path, encoding="utf-8") as file:
        return json.load(file)

def save_results(summary, results):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    result_path = (
            Path("results")
            / f"evaluation_result_{timestamp}.json")

    result_path.parent.mkdir(exist_ok=True)

    report = {
        "summary": summary,
        "results": results,
    }

    with open(result_path, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            ensure_ascii=False,
            indent=2,
        )

    return result_path

def run_evaluation():
    cases = load_cases()

    passed = 0
    failed = 0
    results = []

    for case in cases:
        actual = classify_intent(case["input"])
        expected = case["expected"]
        evaluator_type = case["evaluator"]

        if evaluator_type not in EVALUATORS:
            raise ValueError(f"Invalid evaluator type: {evaluator_type}")

        evaluator = EVALUATORS[evaluator_type]
        is_passed = evaluator(actual, expected)

        results.append(
            {
                "id": case["id"],
                "input": case["input"],
                "expected": expected,
                "actual": actual,
                "evaluator": evaluator_type,
                "passed": is_passed,
            }
        )

        if is_passed:
            passed += 1
        else:
            failed += 1

            print("\n[FAILED]")
            print(f"ID: {case['id']}")
            print(f"Input: {case['input']}")
            print(f"Expected: {expected}")
            print(f"Actual: {actual}")

    total = len(cases)
    accuracy = passed / total

    summary = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "accuracy": accuracy,
    }

    result_path = save_results(summary, results)

    print("\n=== Evaluation Summary ===")
    print(f"Total : {total}")
    print(f"Passed : {passed}")
    print(f"Failed : {failed}")
    print(f"Accuracy : {accuracy:.2%}")
    print(f"Result : {result_path}")

    return results

if __name__ == "__main__":
    run_evaluation()