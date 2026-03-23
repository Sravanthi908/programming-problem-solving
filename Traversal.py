bits = list(map(int, input().split()))

n = len(bits)

i = 0

while i < n - 1:
    if bits[i] == 1:
        i = i + 2
    else:
        i = i + 1

if i == n - 1:
    print(True)
else:
    print(False)