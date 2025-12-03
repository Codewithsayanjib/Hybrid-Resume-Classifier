# rules.py
import re

# Define patterns for each label
RULES = {
    "Education": [
        r"\bb\.?tech\b",
        r"\bm\.?e\b",
        r"\bmaster\b",
        r"\bbachelor\b",
        r"\buniversity\b",
        r"\bdegree\b"
    ],
    "Skills": [
        r"\bskills?\b",
        r"\bpython\b",
        r"\bsql\b",
        r"\bpower bi\b",
        r"\bmachine learning\b",
        r"\bdata analysis\b"
    ],
    "Experience": [
        r"\bintern\b",
        r"\bexperience\b",
        r"\bworked on\b",
        r"\bsoftware engineer\b",
        r"\bengineer\b",
        r"\bcompany\b"
    ],
    "Projects": [
        r"\bproject\b",
        r"\bbuilt\b",
        r"\bdeveloped\b",
        r"\bimplemented\b",
        r"\bflask\b",
        r"\bweb app\b"
    ]
}

def rule_classify(text: str):
    """
    Try to classify the text based purely on keyword/regex rules.
    Returns the label string if matched, otherwise None.
    """
    lowered = text.lower()
    for label, patterns in RULES.items():
        for pattern in patterns:
            if re.search(pattern, lowered):
                return label
    return None