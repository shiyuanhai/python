import os

# get current directory
currdir = os.getcwd()
print(currdir)

# list files and directory
l = os.listdir(currdir)
print(l)

for f in l:
	if os.path.isdir(f):
		print(f)

import glob
print(glob.glob("1/*.xml")[0].replace('\\','/'))

def search_in_folder(folder, condition):
	xmlfile = open(glob.glob(folder+"/*.xml")[0].replace('\\','/'))
	xmlcontents = xmlfile.read()
	if condition in xmlcontents:
		print("dd")

search_in_folder("1","book")
search_in_folder("2",'type="book"')

#open("list.txt", "w").write("123\n")

import re
line = "123"
x="1"
y=""
line = re.sub(r""+re.escape(x),y,line)
print(line)

print("*" in "123")