import os
from glob import glob
from time import sleep

format_files = []
delete_files = []
with open(".gitignore") as file:
    for i in file.read().split("\n"):
        if "*" in i:
            format_files.append(i[2:])
        elif "." in i:
            delete_files.append(i)

rpycs = []
notDeleteds = []

for i in format_files:
    for j in range(0, 100):
        rpycs += glob(f"{'**/'*j}**.{i}")


for i in rpycs:
    print("")
    print(f"Try delete {i}")

    try:
        os.remove(i)
        print(f"File {i} deleted succesful")

    except Exception as e:
        notDeleteds.append((i, e))
        print(f"File {i} not deleted")
        rpycs.remove(i)

for i in delete_files:
    try:
        os.remove(i)
        print(f"File {i} deleted succesful")
    except Exception as e:
        notDeleteds.append((i, e))
        print(f"File {i} not deleted")
        delete_files.remove(i)
    

print("")

os.system('cls' if os.name == 'nt' else 'clear')

print("Deleted:")

for a in rpycs:
    print(f"- {a}")

if len(rpycs) == 0:
    print("No")

print("")

print("Not deleted: ")

for d in notDeleteds:
    print(f"- {d[0]}")

if len(notDeleteds) == 0:
    print("No")

print("")

print(f"Errors: {len(notDeleteds)}")

for k in notDeleteds:
    print(k[1])

if len(rpycs) == 0:
    print("No")
