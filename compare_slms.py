# compare_models.py
from evaluate import evaluate_model

MODELS = [
    "qwen2.5:1.5b",
    "llama3.2:1b",
    "gemma2:2b",
    "phi3:mini"
]

def main():
    results = []

    for model_name in MODELS:
        print(f"\nRunning evaluation for model: {model_name}")
        metrics = evaluate_model(model_name, verbose=False)
        results.append(metrics)

    print("\n================= COMPARISON SUMMARY =================")
    print(f"{'Model':20} {'Overall':>8} {'RuleAcc':>8} {'SLMAcc':>8} {'SLMUsed':>8}")
    for m in results:
        print(
            f"{m['model'][:20]:20} "
            f"{m['overall_acc']:.2f}    "
            f"{m['rule_acc']:.2f}    "
            f"{m['slm_acc']:.2f}    "
            f"{m['slm_used']:8d}"
        )

if __name__ == "__main__":
    main()