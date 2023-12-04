import random
import math
sum=0
arr=[]
rows, cols=8,6
for i in range(rows):
    col = []
    for j in range(cols):
        x=random.randint(100, 1000)
        sum+=x
        col.append(x)
    arr.append(col)
print(arr)
t=math.ceil(((sum/48)-(sum//48))*8)
if t==0:
    t=8
maxi=0
for j in range(cols):
    if arr[t-1][j]>maxi:
        maxi=arr[t-1][j]
        maxind=j
print("The Winner is : Player" , end=" ")
print(maxind+1 )
payoff=0
for j in range(rows):
    payoff+=arr[j][maxind]
payoff=payoff//8
print("The Winner has to pay an amount of : ")
print(payoff)
