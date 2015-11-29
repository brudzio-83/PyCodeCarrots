a=input('podaj wyraz ')
palindrom=a[::-1]
if palindrom==a:
	print('tak')
elif palindrom!=a:
	print('nie')