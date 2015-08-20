# python searchinsub.py file_format conditions
# conditions : a='b', space seperated

import sys,os,glob

if len(sys.argv)<=2:
	exit()

currdir = os.getcwd()
l = os.listdir(currdir)

def search_in_folder(folder, conditions):
	xmlfile = open(glob.glob(folder+"/*."+sys.argv[1])[0].replace('\\','/'))
	xmlcontents = xmlfile.read()
	matched = [1,1]
	for c in conditions:
		c = c.replace("\'","\"")
		if c in xmlcontents:
			matched.append(1)
	return len(matched)==len(conditions)

listfile = open("list.txt", "w")

for f in l:
	if os.path.isdir(f):
		if search_in_folder(f,sys.argv):
			listfile.write(f+"\n")

listfile.close()


