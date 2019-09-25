from os import walk
import os


path = "/home/lmezard/ft_fun/"
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

files = []
for file_ in f:
	with open(path + file_, "r") as fd:
		number = fd.read().split("//file")[1]
		files.append({'key' : int(number), 'name' : file_})
files.sort()
print("All files are sorted !")

code = ""
for fil in files:
	with open(path + fil['name']) as f:
		data = f.read().split("//file")
		code += data[0] + "//" + fil['name'] + "\n"
print("Code recovered !")

with open("main.c", "w") as main:
	main.write(code)
print("'main.c' file was created !")

os.system("gcc main.c && ./a.out")
print("\n")
