def classify_intent(text: str) -> str:
    intent_keywords = {
        "refund": ["환불"],
        "delivery": ["배송", "택배"],
        "account": ["비밀번호"],
    }
    matched_intents = []

    for intent, keywords in intent_keywords.items():
        if any(keyword in text for keyword in keywords):
            matched_intents.append(intent)

    if len(matched_intents) >= 2:
        return "ambiguous"

    if len(matched_intents) == 1:
        return matched_intents[0]

    return "unknown"

