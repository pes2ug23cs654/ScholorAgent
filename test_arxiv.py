from src.utils.context_evaluator import evaluate_context

query = "What is self attention?"

context = """
Self-attention is a mechanism in Transformers...
"""
print(evaluate_context(query, context))