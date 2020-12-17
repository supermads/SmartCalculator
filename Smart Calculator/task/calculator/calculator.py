# write your code here
def add(nums):
    if nums:
        acc = 0
        for n in nums:
            acc += int(n)
        print(acc)


def main():
    while True:
        nums = input().split()
        if nums == ['/exit']:
            print('Bye')
            return
        elif nums == ['/help']:
            print('The program calculates the sum of numbers')
        else:
            add(nums)


main()
