n = list(map(int, input().split()))
cost = 0
for i in range(n[2] + 1):
    cost += i * n[0]
if cost <= n[1]:
    print(0)
else:
    print(cost - n[1])
