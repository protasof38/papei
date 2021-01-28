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

lst=s.split()
from string import punctuation

for i in range(len(lst)):
	lst[i]=lst[i].strip(punctuation)
		

lst2=[]
for i in range(0,len(lst),3):
	if(i+2)<=(len(lst)-1):
		lst2.append([lst[i],lst[i+1],lst[i+2]])
	else:
		break

from random import randint
x=randint(0,len(lst2)-1)

lst3=[]
lst3.append([lst2[x][1],lst2[x][2]])
lst2.remove(lst2[x])


for i in range(100):
	if(i-len(lst3))!=1:
		print('cannot find 200 words !!')
		break
	else:
		indx=0
		temp=lst2
		for j in range(len(temp)):
			if(lst3[i][0]==temp[j][0] and lst3[i][1]==temp[j][1])or(lst3[i][0]==temp[j][1] and lst3[i][1]==temp[j][0]):
				indx=j
				lst3.append([temp[j][1],temp[j][2]])
				lst2.remove(lst2[indx])
				break
