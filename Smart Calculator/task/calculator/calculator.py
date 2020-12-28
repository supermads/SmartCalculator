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


def check_expression(sub_exps):
    op_list = ['+', '-']
    if len(sub_exps) == 1:
        if sub_exps[0].isnumeric() or (sub_exps[0][0] in op_list and sub_exps[0][1:].isnumeric()):
            return True
        else:
            return False
    ops = 0
    nums = 0
    for c in sub_exps:
        if c in op_list:
            ops += 1
        elif c.isnumeric():
            nums += 1
    if ops + 1 == nums:
        return True
    return False


def add(nums):
    a, b = map(int, nums)
    return a + b


def subtract(nums):
    a, b = map(int, nums)
    return a - b


def do_calculations(variables, exp):
    exp = process_expression(exp)
    sub_exps = exp.split()
    for i in range(len(sub_exps)):
        if sub_exps[i] in variables:
            sub_exps[i] = variables.get(sub_exps[i])
    is_valid = check_expression(sub_exps)
    if is_valid:
        acc = sub_exps[0]
        while len(sub_exps) > 1:
            if sub_exps[1] == '+':
                acc = add([sub_exps[0], sub_exps[2]])
            elif sub_exps[1] == '-':
                acc = subtract([sub_exps[0], sub_exps[2]])
            del sub_exps[0:2]
            sub_exps[0] = acc
        print(str(acc).strip('+'))
    elif len(sub_exps) == 1 and sub_exps[0].isalpha():
        if sub_exps[0] in variables:
            print(variables.get(sub_exps[0]))
        else:
            print('Unknown variable')
    else:
        print('Invalid expression')


def main():
    variables = {}
    while True:
        exp = input()
        if exp:
            # Process Commands
            if exp[0] == '/':
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
            # Perform Calculations
            else:
                do_calculations(variables, exp)


main()
