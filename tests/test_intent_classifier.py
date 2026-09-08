import json
from pathlib import Path

import pytest

from intent_classifier import classify_intent

def load_cases():
    dataset_path = (
        Path(__file__).resolve().parents[1]
        /"datasets"
        /"intent_cases.json"
    )

    with open(dataset_path, encoding="utf-8") as file:
        return json.load(file)

@pytest.mark.parametrize(
    "case",
    load_cases(),
    ids=lambda case: case["id"],
)
def test_classify_intent(case):
    actual = classify_intent(case["input"])

    assert actual == case["expected"]