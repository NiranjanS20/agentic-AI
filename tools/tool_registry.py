from tools.calculator import calculate

def detect_tool(user_input: str) -> str:
    if user_input.startswith("calc:"):
        expr = user_input.replace("calc:", "").strip()
        return calculate(expr)
    return None