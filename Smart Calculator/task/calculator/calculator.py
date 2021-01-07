def process_expression(exp):
    changes = {'++': '+', '--': '+', '+-': '-', '-+': '-'}
    before_len = len(exp)
    while True:
        for original, replacement in changes.items():
            while original in exp:
                exp = exp.replace(original, replacement)
        if len(exp) == before_len:
            break
        before_len = len(exp)
    return exp


def convert_to_postfix(variables, exp):
    exp = exp.replace('(', '( ')
    exp = exp.replace(')', ' )')
    sub_exps = process_expression(exp).split()
    stack = []
    postfix = []
    op_dict = {'-': 0, '+': 0, '/': 1, '*': 1, '^': 2, ')': 3, '(': 3}
    for i in range(len(sub_exps)):
        if sub_exps[i] in variables:
            sub_exps[i] = variables.get(sub_exps[i])
    for x in sub_exps:
        # Rule 1
        if x.isnumeric():
            postfix.append(x)
        else:
            if stack:
                top_of_stack = stack[-1]
                top_precedence = op_dict.get(top_of_stack)
            else:
                top_of_stack = 0
                top_precedence = 0
            curr_precedence = op_dict.get(x)
            # Rule 5
            if x == '(':
                stack.append(x)
            # Rule 6
            elif x == ')':
                while stack and top_of_stack != '(':
                    postfix.append(stack.pop())
                    if stack:
                        top_of_stack = stack[-1]
                if top_of_stack == '(':
                    stack.pop()
                else:
                    raise Exception
            # Rules 2 and 3
            elif not stack or top_of_stack == '(' or curr_precedence > top_precedence:
                stack.append(x)
            # Rule 4
            elif curr_precedence <= top_precedence:
                top_of_stack = stack[-1]
                top_precedence = op_dict.get(top_of_stack)
                curr_precedence = op_dict.get(x)
                while curr_precedence <= top_precedence and stack and top_of_stack != '(':
                    postfix.append(stack.pop())
                stack.append(x)
    # Check if any parentheses remaining on stack
    if '(' in stack or ')' in stack:
        raise Exception
    else:
        # rule 7
        while stack:
            postfix.append(stack.pop())
    return postfix


def do_operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '^':
        return a ** b


def do_stack_calc(postfix):
    stack = []
    ops = ['^', '*', '/', '+', '-']
    for x in postfix:
        if x.isnumeric():
            stack.append(x)
        elif x in ops:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(do_operation(a, b, x))
        else:
            print(x)
            raise Exception
    while len(stack) > 1:
        stack.pop()
    return stack[0]


def main():
    variables = {}
    while True:
        exp = input()
        if exp:
            # Check if just variable name entered. If it's a valid variable, print its value.
            if exp.strip().isalpha():
                if exp[0] in variables:
                    print(variables.get(exp[0]))
                else:
                    print('Unknown variable')
            # Process Commands
            elif exp[0] == '/':
                command = exp[1:]
                if command == 'exit':
                    print('Bye!')
                    return
                elif command == 'help':
                    print('The program calculates the result of given expressions')
                else:
                    print('Unknown command')
            # Process Variable Assignments
            elif '=' in exp:
                if exp.count('=') > 1:
                    print("Invalid assignment")
                else:
                    idx = exp.find('=')
                    left = exp[0:idx].strip()
                    if len(exp) > len(left) + 1:
                        right = exp[idx + 1:]
                    if not left.isalpha():
                        print('Invalid identifier')
                    else:
                        right = right.strip()
                        if right in variables:
                            right = variables.get(right)
                        if not right.isnumeric():
                            print('Invalid assignment')
                        else:
                            variables[left] = right
            # Convert to Postfix and Do Calculations (If Possible)
            else:
                try:
                    postfix = convert_to_postfix(variables, exp)
                    if postfix:
                        ans = do_stack_calc(postfix)
                        if ans is not None:
                            print(ans)
                except Exception:
                    print('Invalid expression')


main()

