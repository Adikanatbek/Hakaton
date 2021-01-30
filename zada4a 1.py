
prodoljit = 'y'
while prodoljit == 'y':
	f_num = int(input("Введите число: "))
	oper = input("Введите операцию: ")
	s_num = int(input("Введите второе число:"))
	if oper == '+':
		print (f_num + s_num)
	elif oper == '-':
		print (f_num - s_num)
	elif oper== '*' :
		print(f_num * s_num)
	elif oper =='/': 
		print (f_num / s_num)
	else :
		print ('Error')
	prodoljit = input("Введите 'y', чтобы продолжить, или любую клавищу, чтобы заверщить>>")
