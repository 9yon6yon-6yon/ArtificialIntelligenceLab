n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

i = 1
for i in range(n):
    for j in range(i+1,n):
        print (arr[i]," ",arr[j])
    i+=1    

