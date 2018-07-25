from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coping from %s to %s" %(from_file,to_file)

in_file = open(from_file)
file_data = in_file.read()

print "Input file is %s bytes long." %len(file_data)
print "Does files exists ?"
if exists(to_file):
	print "Do you want to copy the file ?"
	print "Yes,  \"%s\"  does exists." %to_file

	out_file = open(to_file,'w')
	out_file.write(file_data)

	print "Copied."
	out_file.close()
	in_file.close()	
else:
	print "No, \"%s\"  doesn't exists." %to_file
