# hybrid_classifier.py
from rules import rule_classify
from ollama_client import slm_classify

def hybrid_classify(text: str, model_name: str):
    """
    First try rule-based classification.
    If that fails, call the SLM via Ollama.

    Returns (predicted_label, source) where:
      - source is 'rule' if rule-based classified it
      - source is 'llm' if SLM was used
    """
    rule_label = rule_classify(text)
    if rule_label is not None:
        return rule_label, "rule"

    slm_label = slm_classify(text, model_name=model_name)
    return slm_label, "slm"