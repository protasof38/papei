n=0
while 1>0:
	check=True
	x=input('Dose akeraio megalytero tou 3 : ')
	if len(x)==0:
		continue
	else:
		for i in range(len(x)):
			if(x[i]>='0' and x[i]<='9'):
				continue
			else:
				check=False
				break
	if check==False:
		print('invalid input')
		continue
	else:
		n=eval(x)
		if n<=3:
			print('invalid input')
			n=0
			continue
		else:
			break
counter=0
for k in range(100):
	A=[[0 for i in range(n)] for j in range(n)]
	invA=A
	count=(n**2)/2
	from random import randint
	while count>0.0:
		i=randint(0,n-1)
		j=randint(0,n-1)
		if A[i][j]==0:
			A[i][j]=1
			invA[j][i]=1
			count-=1
	four=0
	for i in range(n):
		for j in range(n):
			if len(A[i][j:len(A[i])])>=4:
				sum1=A[i][j]+A[i][j+1]+A[i][j+2]+A[i][j+3]
				if sum1==4:
					four+=1
				sum2=invA[i][j]+invA[i][j+1]+invA[i][j+2]+invA[i][j+3]
				if sum2==4:
					four+=1
			else:
				break
	for i in range(n):
		for j in range(n):
			if n-i>=4 and n-j>=4:
				sum3=A[i][j]+A[i+1][j+1]+A[i+2][j+2]+A[i+3][j+3]
				if sum3==4:
					four+=1
				sum4=A[i][j+3]+A[i+1][j+2]+A[i+2][j+1]+A[i+3][j]
				if sum4==4:
					four+=1
	#print('counter = ' , counter)	
	counter+=four

print('M.O. tetradon : ' , (counter/100))