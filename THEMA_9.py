s=""
while 1>0:
	x=input('Dose to path tou arxeiou : ')
	try:
		f=open(x,"r")
		s=f.read()
		f.close()
		break
	except Exception:
		print('Invalid input . File not found or encoding of file is not UTF-8')
		continue

lst=[]
for i in range(len(s)):
	if s[i] not in lst[0:i]:
		lst.append(s[i])

lst2=[]
for i in range(len(lst)):
	if ord(lst[i])%2==1:
		lst2.append(lst[i])

lst3=[]
for i in range(len(lst2)):
	lst3.append(s.count(lst2[i]))

import math
for i in range(len(lst2)):
	print(lst2[i],(str)((lst3[i]/len(s))*100)+"%",round((lst3[i]/len(s))*100)*"*")
