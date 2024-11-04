s=input("Enter the string: ")
kposition=int(input("Enter the k position: "))
ar=[]
for char in s:
    ar.append(char)
res=['']*len(s)
for i in range(len(ar)):
    x=i+kposition
    if x >= len(ar):
        x=x-len(ar)
    res[i]=ar[x]
result=""
for char in res:
    result+=char
print(result)
