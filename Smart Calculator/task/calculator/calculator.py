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


def add(nums):
    if nums:
        acc = 0
        for n in nums:
            acc += int(n)
        return acc


def subtract(nums):
    a, b = map(int, nums)
    return a - b


def main():
    while True:
        exp = input()
        if exp == '/exit':
            print('Bye')
            return
        elif exp == '/help':
            print('The program calculates the result of given expressions')
        elif exp:
            exp = process_expression(exp)
            sub_exps = exp.split()
            acc = sub_exps[0]
            while len(sub_exps) > 1:
                if sub_exps[1] == '+':
                    acc = add([sub_exps[0], sub_exps[2]])
                elif sub_exps[1] == '-':
                    acc = subtract([sub_exps[0], sub_exps[2]])
                del sub_exps[0:2]
                sub_exps[0] = acc
            print(acc)


main()
