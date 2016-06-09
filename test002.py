num1=[98,43, -12,5,24,43]
num2=sorted(num1)
print(num2)

num3=set(num1)
print(num3)

lst=[]

for num in range(0,21,2):
    lst.append(num**2)
print(lst)

lst2=[num**3 for num in range(0,21,2)]
print(lst2)
