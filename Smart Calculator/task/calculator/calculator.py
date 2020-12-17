# write your code here
def add(nums):
    if nums:
        sum = 0
        for n in nums:
            sum += int(n)
        print(sum)


def main():
    while True:
        nums = input().split()
        if nums == ['/exit']:
            print('Bye')
            return
        else:
            add(nums)


main()
