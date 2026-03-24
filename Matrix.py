MOD = 12345

n = int(input())
m = int(input())

grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

ans = []
for i in range(n):
    ans.append([0] * m)

pref = 1

for i in range(n):
    for j in range(m):
        ans[i][j] = pref
        pref = (pref * (grid[i][j] % MOD)) % MOD

suf = 1

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        ans[i][j] = (ans[i][j] * suf) % MOD
        suf = (suf * (grid[i][j] % MOD)) % MOD

for row in ans:
    print(*row)