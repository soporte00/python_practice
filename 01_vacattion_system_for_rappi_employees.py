import os



'''

	sections

		key		section

		1		A. clientes
		2 		Logística
		3 		Gerencia

	employees

		key		time(years)		vacations(days)
		
		1		1				6
		1		2-6				14
		1		7				20

		2		1				7
		2		2-6				15
		2		7				22

		3		1				10
		3		2-6				20
		3		7				30

'''




repeat = True


while(repeat):
	
	os.system("clear")

	print("**********************************************")
	print("* Sistema vacacional para empleados de rappi *")
	print("********************************************** \n")


	name = input("Ingresa el nombre del empleado: ")
	
	print("\n1)A. clientes 2)Logística 3)Gerencia ")
	
	employeeKey = int( input("\nIngresa el número correspondiente a su departamento: ") )
	
	employeeYears = int( input("\nIngresa la antiguedad en años: ") )
	
	print("\nLos datos ingresados son: \n","\n Nombre: "+ name,"\n Departamento: "+ str(employeeKey),"\n antiguedad: "+ str(employeeYears) +" años" )
	
	agree = input("\n¿Los datos son correctos? escribe si o no: ")

	if agree == 'si':
		
		print("\n==================================\n")

		if employeeKey == 1:

			if employeeYears == 1:
				print(name+" tiene 6 dias de vacaciones")
			elif employeeYears >= 2 and employeeYears <=6:
				print(name+" tiene 14 dias de vacaciones")
			elif employeeYears >= 7:
				print(name+" tiene 20 dias de vacaciones")
			else:
				print("La antiguedad es incorrecta")

		elif employeeKey == 2:

			if employeeYears == 1:
				print(name+" tiene 7 dias de vacaciones")
			elif employeeYears >= 2 and employeeYears <=6:
				print(name+" tiene 15 dias de vacaciones")
			elif employeeYears >= 7:
				print(name+" tiene 22 dias de vacaciones")
			else:
				print("La antiguedad es incorrecta")

		elif employeeKey == 3:

			if employeeYears == 1:
				print(name+" tiene 10 dias de vacaciones")
			elif employeeYears >= 2 and employeeYears <=6:
				print(name+" tiene 20 dias de vacaciones")
			elif employeeYears >= 7:
				print(name+" tiene 30 dias de vacaciones")
			else:
				print("La antiguedad es incorrecta")


		else:
			print("\nEl departamento elegido no es correcto")


	action = input('\n ** Para repetir el programa presiona Enter o "q" para salir: ')

	if action == 'q':
		repeat = False