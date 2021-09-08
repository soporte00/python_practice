def division():

    while True:
    
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print("El resultado de la división es: "+ str(num1/num2))
            break

        except ValueError:
            print("Los datos ingresados son erroneos. Vuelve a intentarlo")
        except ZeroDivisionError:
            print("No puedes hacer una división entre 0!. Vuelve a intentarlo")




print("********************")
print("*Divisor de números*")
print("********************\n")

division()