# python replaceinsub.py file_format old new

import sys,os,glob,re

if len(sys.argv)!=4:
	exit()

currdir = os.getcwd()
l = os.listdir(currdir)

def replace_in_folder(folder, old, new):
	xmlfile = open(glob.glob(folder+"/*."+sys.argv[1])[0].replace('\\','/'),"r+")
	xmlcontents = xmlfile.read()
	old = old.replace("\'","\"")
	xmlcontents = re.sub(r""+re.escape(old),new,xmlcontents)
	xmlfile.seek(0)
	xmlfile.write(xmlcontents)
	xmlfile.truncate()
	

for f in l:
	if os.path.isdir(f):
		replace_in_folder(f ,sys.argv[2] ,sys.argv[3])

