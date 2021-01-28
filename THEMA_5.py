lines=0
cols=0
lst=''
while 1>0:
	check=True
	x=input('Dose 2 akeraious megalyterous tou 2 , xorismenoi me komma : ')
	if len(x)==0:
		continue
	for i in range(len(x)):
		if x[i]==',':
			lst=x.split(',')
			break
	if len(lst)==2:
		for i in range(len(lst[0])):
			if(lst[i]>='0' and lst[i]<='9'):
				continue
			else:
				check=False
				break
		for i in range(len(lst[1])):
			if(lst[i]>='0' and lst[i]<='9'):
				continue
			else:
				check=False
				break
	else:
		lst=''
		continue
		

	if check==False:
		print('invalid input')
		lst=''
		continue
	else:
		lines=eval(lst[0])
		cols=eval(lst[1])
		if lines<=2 or cols<=2:
			print('invalid input')
			lines=0
			cols=0
			lst=''
			continue
		else:
			break


counter=0
for k in range(100):
	A=[['O' for j in range(cols)] for i in range(lines)]
	invA=[['O' for j in range(lines)] for i in range(cols)]
	count=(lines*cols)/2
	from random import randint
	while count>0.0:
		i=randint(0,lines-1)
		j=randint(0,cols-1)
		if A[i][j]=='O':
			A[i][j]='S'
			invA[j][i]='S'
			count-=1
	three=0
	for i in range(lines):
		for j in range(cols):
			if len(A[i][j:len(A[i])])>=3:
				wrd1=A[i][j]+A[i][j+1]+A[i][j+2]
				if wrd1=='SOS':
					three+=1
			else:
				break
	for i in range(cols):
		for j in range(lines):
			if len(invA[i][j:len(invA[i])])>=3:
				wrd2=invA[i][j]+invA[i][j+1]+invA[i][j+2]
				if wrd2=='SOS':
					three+=1
			else:
				break
	for i in range(lines):
		for j in range(cols):
			if lines-i>=3 and cols-j>=3:
				wrd3=A[i][j]+A[i+1][j+1]+A[i+2][j+2]
				if wrd3=='SOS':
					three+=1
				wrd4=A[i][j+2]+A[i+1][j+1]+A[i+2][j]
				if wrd4=='SOS':
					three+=1
	print('counter = ' , counter)	
	counter+=three
				


print('M.O. triadon : ' , (counter/100))