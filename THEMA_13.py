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

lst=s.split()#len(lst)=47785
lst2=[]
from string import punctuation
for i in range(len(lst)):
	lst[i]=lst[i].strip(punctuation)
for i in range(len(lst)):
	if lst[i] not in lst[0:i]:
		lst2.append(lst[i])#len(lst2)=885
	
couples=[]
for i in range(0,len(lst2)-1):
	for j in range(i+1,len(lst2)):
		if(len(lst2[i])+len(lst2[j]))>=20:
			couples.append([lst2[i],lst2[j]])

#len(couples)=40969
while len(couples)>0:
	num=len(couples[0][0])+len(couples[0][1])
	print('('+couples[0][0]+'|'+couples[0][1]+')'+' = '+(str)(num)+ ' characters')
	couples.remove(couples[0])

