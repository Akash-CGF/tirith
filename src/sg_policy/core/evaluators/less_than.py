from base_evaluator import BaseEvaluator

# Checks if :attr:`value` is less then :attr:`other`. Automatically casts values to the same type if possible.

# Args:
#     value (mixed): Value to compare.
#     other (mixed): Other value to compare.

# Returns:
#     bool: Whether :attr:`value` is less then :attr:`other`.

# Example:

#     >>> l(None, None)
#     False
#     >>> l(2, 3)
#     True
#     >>> l('a', 'a')
#     False

# .. versionadded:: 1.0.0


class LessThan(BaseEvaluator):
    def evaluate(self, evaluator_input, evaluator_data):
        evaluation_result = {"result": False, "message": "LessThan evaluator failed"}
        try:
            value1 = evaluator_input
            value2 = evaluator_data
            evaluation_result["result"] = value1 < value2
            return evaluation_result
        except Exception as e:
            evaluation_result["message"] = str(e)
            return evaluation_result