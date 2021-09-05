import os

while True:

	os.system("clear")

	print("********************************")
	print("*Comprueba cual número es mayor*")
	print("********************************\n")
	


	a = int(input("Ingresa el primer número: "))
	b = int(input("Ingresa el segundo número: "))
	c = int(input("Ingresa el tercer número: "))



	if a > b and a > c:
		print("\nEl número mas grande es "+ str(a))

	elif b > a and b > c:
		print("\nEl número mas grande es "+ str(b))

	elif c > b and c > a:
		print("\nEl número mas grande es "+ str(c))





	action = input("\n'Enter' > repetir | 'q' > salir: ")

	if action == 'q':
		break