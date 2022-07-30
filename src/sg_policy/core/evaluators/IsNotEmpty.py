import BaseEvaluator

# Checks if input is not empty

# Args:
#     value (mixed): Value to check.

# Returns:
#     bool: Whether :attr:`value` is not empty

# Example:

#     >>> e('')
#     False
#     >>> e("abc")
#     True
#     >>> l([])
#     False

# .. versionadded:: 1.0.0


class IsNotEmpty(BaseEvaluator):
    def evaluate(self, input):
        evaluation_result = {"result": False, "reason": "IsNotEmpty evaluator failed"}
        try:
            if (isinstance(input, str) or isinstance(input, list) or isinstance(input, dict)) and input:
                evaluation_result["result"] = True
            return evaluation_result
        except Exception as e:
            evaluation_result["reason"] = str(e)
            return evaluation_result
