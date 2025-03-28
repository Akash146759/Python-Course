try:
    eval("print(1 + )")  # Syntax error: missing operand
except SyntaxError as ex:
    print(f"Syntax error detected: {ex}")