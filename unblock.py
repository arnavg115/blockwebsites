import sys
filepath = '/etc/hosts'
u = sys.argv[1]
with open(filepath) as fp:
   file = fp.read()
   lst = file.split("\n")

   j = lst
   k = []
   for index, entry in enumerate(lst):
   		if u in entry:
   			k.append(entry)
if len(k)== 0:
	raise Exception("That website was not blocked there may have been a type")
for md in k:
	j.remove(md)

def listToString(s):  

    str1 = ""  

    for ele in s:  
        str1 = str1 +ele +"\n" 

    return str1  
with open("/etc/hosts","w") as myfile:
	myfile.write(listToString(j))
	myfile.close()

