def funcion_suma(numero1 = 0, numero2 = 0):
    print(numero1 + numero2)


#opcion = int(input("Digite numero"))
#if opcion > 5:
#    funcion_suma(5, 3)   

#funcion_suma(5,)
# 
def cuenta_hacia_tras(numero):
    numero -= 1 # numero = numero - 1 
    if(numero > 0):
        print("vamos en el numero:", numero)
        cuenta_hacia_tras(numero)
    else:
        print("Terminamos")    


#numero_ingresado = int(input("Digite numero:"))
#cuenta_hacia_tras(numero_ingresado)       
def factorial(numero):
    if(numero > 1):
        numero = numero * factorial(numero - 1)

    return numero    

print(factorial(6))