#Comprehenshion


# FORMULA for VARIABLE in ITERATABLE_OBJECT if CONDITION

lst=[1,2,3]

for num in lst:
    print(num**2)
#Comprehension
lst1=[num**2 for num in lst]
print(lst1)

#Extract with Comprehension
urls = ["https://www.google.com", "http://www.yahoo.com", "https://twitter.com"]
host_name = [url[8:] for url in urls if url.startswith("https")]
print(host_name)  # ['www.google.com', 'twitter.com']

#Taple inside array
names = [("John Doe", "M"),("Mary Jane", "W"),("Mark Co", "M"), ]

men = [name[0] for name in names if name[1] == "M"]
print(men) #['John Doe', 'Mark Co']


#Dictionay
e_numbers= ["one", "two", "three"]
numbers= [1,2,3]
dic = {n:e for (e,n) in zip(e_numbers, numbers)}
print(dic)
