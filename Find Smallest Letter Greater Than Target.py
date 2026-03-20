letters = input().split()
target = input().strip()

res = letters[0]
flag = False

for ch in letters:
    if not flag:
        if ch > target:
            res = ch
            flag = True
    else:
        if ch > target and ch < res:
            res = ch

print(res)