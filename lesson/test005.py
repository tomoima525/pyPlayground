#Handling files

#read file
f = open("test.txt", "r", encoding="utf_8")
lines = f.readlines()
for line in enumerate(lines):
    print(line[1], end="\n")

f.close()

with open("test.txt", "r", encoding="utf_8") as file:
    for i, line in enumerate(file):
        print("{}:{}".format(i, line))  # don't need to consider about close()

#write file
with open("out.txt", "a", encoding="utf_8") as file:
    file.write("Hello world\n")
    list = ["aaa \n", "bbb \n", "ccc \n"]
    file.writelines(list)
