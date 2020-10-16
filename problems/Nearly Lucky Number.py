n = int(input())
res = [int(x) for x in str(n)]
lucky_nums_cout = 0
for i in res:
    if i == 7 or i == 4:
        lucky_nums_cout += 1
if "7" in str(lucky_nums_cout) or "4" in str(lucky_nums_cout):
    print("YES")
else:
    print("NO")
