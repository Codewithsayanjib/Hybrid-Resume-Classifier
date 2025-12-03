# evaluate.py
import json
from pathlib import Path

from hybrid_classifier import hybrid_classify

DATA_PATH = Path("data") / "resumes.json"

def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def evaluate_model(model_name: str, verbose: bool = True):
    data = load_data()

    total = len(data)
    correct = 0
    rule_correct = 0
    slm_correct = 0
    rule_used = 0
    slm_used = 0

    if verbose:
        print(f"\n=== Evaluating model: {model_name} ===")
        print(f"Loaded {total} samples.\n")

    for item in data:
        text = item["text"]
        true_label = item["label"]

        pred_label, source = hybrid_classify(text, model_name=model_name)

        is_correct = (pred_label == true_label)
        if is_correct:
            correct += 1
            if source == "rule":
                rule_correct += 1
            elif source == "slm":
                slm_correct += 1

        if source == "rule":
            rule_used += 1
        else:
            slm_used += 1

        if verbose:
            print(f"TEXT: {text}")
            print(f"  True: {true_label}")
            print(f"  Pred: {pred_label} (via {source})")
            print(f"  Correct: {is_correct}")
            print("-" * 60)

    overall_acc = correct / total if total > 0 else 0.0
    rule_acc = rule_correct / rule_used if rule_used > 0 else 0.0
    slm_acc = slm_correct / slm_used if slm_used > 0 else 0.0

    if verbose:
        print("\n=== Summary ===")
        print(f"Model: {model_name}")
        print(f"Total samples: {total}")
        print(f"Overall accuracy: {correct}/{total} = {overall_acc:.2f}")
        print(f"Rule-based used: {rule_used} times, correct: {rule_correct}, acc={rule_acc:.2f}")
        print(f"SLM fallback used: {slm_used} times, correct: {slm_correct}, acc={slm_acc:.2f}")

    # Return metrics so we can compare models from another script
    return {
        "model": model_name,
        "total": total,
        "overall_acc": overall_acc,
        "correct": correct,
        "rule_used": rule_used,
        "rule_correct": rule_correct,
        "rule_acc": rule_acc,
        "slm_used": slm_used,
        "slm_correct": slm_correct,
        "slm_acc": slm_acc,
    }

if __name__ == "__main__":
    # default single-model run for debugging
    metrics = evaluate_model("qwen2.5:1.5b", verbose=True)