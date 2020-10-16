import itertools
n= int(input("Enter number of threads : "))
n1 = [1,2,3,4]
n2 = [5,6,7]
#
# for i,j in zip(n1,n2):
#     print(i,j)
for i,j in itertools.zip_longest(n1,range(n)):
    print(i)