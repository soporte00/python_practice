import os

while True:

	os.system("clear")

	print("****************************")
	print("*Comprueba si es numero par*")
	print("****************************\n")
	
	
	number = int(input("Ingresa el número a comprobar: "))
	
	
	if number % 2 == 0:
	
		print("\nEl número es par")
	else:
		print("\nEl número es impar")


	action = input("\n'Enter' > repetir | 'q' > salir: ")

	if action == 'q':
		break
