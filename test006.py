import os, sys, random;

if len(sys.argv) !=2:
    print("Select one file")
    sys.exit()

path = sys.argv[1]
if os.path.exists(path):
    if input("Overwrite? (y/n): ") != "y":
        sys.exit()
values = ["1","2","3"]
with open(path, "w", encoding="utf_8") as f:
    f.write(values[random.randrange(len(values))] + "\n")
