#PARCIAL 2
import funciones_parcial2


#MENÚ
print("BIENVENIDO")
print("---MENÚ PRINCIPAL---")
print("(1) ANALIZAR ADN")
print("(2) CONSULTAR ADN REGISTRADOS")
print("(3) SALIR")
print("--------------------")

option=int(input())
adn=[]
#registros=[("Giovanna Suarez","HUMANA")]
while True:
    if option==1:
        print("INGRESE LA SECUENCIA DE ADN")
        print("Ingrese fila por fila")
        print("Recuerde ingresar unicamente letras A T C G")
        for i in range(6):
            comb_adn=input(f"Ingrese la {i+1}° fila de combinacion de genomas?").upper()
            adn.append(comb_adn)
        
        #funcion para validar
        if funciones_parcial2.vali_adn(adn) == True:
            print("hola")
            #llamar a funcion que analiza adn
            break    
        else:
            print("---ERROR - DATOS INGRESADOS INCORRECTAMENTE---")
            print("---Intente nuevamente por favor---")
            print()
            continue
                
    elif option==2:
        print("registros")
    elif option==3:
        print()
    else:
        print("---ERROR - OPCIÓN INGRESADA INCORRECTA---")   
        print("Intente nuevamente por favor: ")     
        continue    