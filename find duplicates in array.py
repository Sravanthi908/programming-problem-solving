n = int(input())
arr = list(map(int, input().split()))

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1

for k in freq:
    if freq[k] > 1:
        print(k, end=" ")