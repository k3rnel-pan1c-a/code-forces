n = input()
n2 = input()
if n.lower() == n2.lower():
    print(0)
elif n.lower() < n2.lower():
    print(-1)
elif n.lower() > n2.lower():
    print(1)