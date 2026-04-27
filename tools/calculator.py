def calculate(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Calculation Error: {str(e)}"