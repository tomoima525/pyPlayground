#handle list, set
num1=[98,43, -12,5,24,43]
num2=sorted(num1)
print(num2)

num3=set(num1)

print("num3: " + repr(num3)) # repr convert object into String

num4 = {"test1", "test2"}
num5 = {-12}
print("combine " + repr(num3 | num4))
print("common " + repr(num3 & num5))

lst=[]

for num in range(0,21,2):
    lst.append(num**2)
print(lst)

lst2=[num**3 for num in range(0,21,2)]
print(lst2)


list1 = [1,2,3]
list2 = [4,5,6]
for a,b in zip(list1,list2):
    print(a+b)
    
