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


def main():
    while True:
        exp = input()
        if exp:
            if exp[0] == '/':
                command = exp[1:]
                if command == 'exit':
                    print('Bye')
                    return
                elif command == 'help':
                    print('The program calculates the result of given expressions')
                else:
                    print('Unknown command')
            else:
                exp = process_expression(exp)
                sub_exps = exp.split()
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
                else:
                    print('Invalid expression')


main()
