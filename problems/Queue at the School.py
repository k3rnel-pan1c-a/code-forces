n = list(map(int,input().split()))
n2 = list(input())
final = ""
while (n[1]>0):
    i =0
    while i < (len(n2)-1):
        if n2[i] == "B":
            if n2[i+1] == "G":
                n2[i],n2[i+1] = n2[i+1],n2[i]
                i+=1
            else:
                pass
        i += 1
    n[1] -= 1
# while (n[1]>0):
# 	i=0
# 	while i<(len(n2)-1):
# 		#to check if 'G' is standing behind 'B',If yes thn swap their positions
# 		if (n2[i]=='B' and n2[i+1]=='G'):
# 			n2[i],n2[i+1]=n2[i+1],n2[i]
# 			#as i and i+1 as swapped so it vl be 'B' therefore there is a need to increment
# 			i+=1
# 		i+=1
# 	n[1]-=1
for i in n2:
    final += i
print(final)