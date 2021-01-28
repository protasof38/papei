n=0
while 1>0:
	check=True
	x=input('Dose akeraio megalytero tou 2 : ')
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
		if n<=2:
			print('invalid input')
			n=0
			continue
		else:
			break
	
fib1=1
fib2=1
p=0
for i in range(2,n):
	p=fib1+fib2
	fib1=fib2
	fib2=p

from random import randint
first=True
for i in range(20):
	a=randint(-1000,p+1000)
	y=a**p
	z=y-a
	if z>0:
		if z%p==0 or z%p==z:
			continue
		else:
			first=False
			break
	else:
		if z%p==0 or z%p<p:
			continue
		else:
			first=False
			break

if first==False:
	print('Oros akolouthias Fibo : ', n , ' me timh ' , p , 'den einai protos')
else:
	print('Oros akolouthias Fibo : ', n , ' me timh ' , p , ' einai protos')


print('End of program .')