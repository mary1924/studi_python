

expr = input("Enter an expression (allowed with brackets): ")

def priority(op):
    return 1 if op in ('+', '-') else 2 if op in ('*', '/') else 0

def apply_op(a, b, op):
    return a + b if op == '+' else a - b if op == '-' else a * b if op == '*' else a / b

def calculate(expression):
    nums, ops = [], []
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch == ' ':
            i += 1
            continue
        if ch.isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            nums.append(val)
            continue
        elif ch == '(':
            ops.append(ch)
        elif ch == ')':
            while ops and ops[-1] != '(':
                b, a = nums.pop(), nums.pop()
                nums.append(apply_op(a, b, ops.pop()))
            ops.pop()
        elif ch in '+-*/':
            while ops and priority(ops[-1]) >= priority(ch):
                b, a = nums.pop(), nums.pop()
                nums.append(apply_op(a, b, ops.pop()))
            ops.append(ch)
        i += 1
    while ops:
        b, a = nums.pop(), nums.pop()
        nums.append(apply_op(a, b, ops.pop()))
    return nums[-1]

print("Result:", calculate(expr))