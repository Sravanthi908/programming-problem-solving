nums = list(map(int, input().split()))
k = int(input())

total = sum(nums)
rem = total % k

if rem == 0:
    print(0)
else:
    print(k - rem)