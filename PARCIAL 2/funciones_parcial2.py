#Funciones del parcial

#Funcion para validar entrada de datos
def vali_adn(adn):
    
    if len(adn)== 6 :
        for cadena in adn:
            for letra in cadena:
                if letra not in ["A","C","G","T"]:
                    valida=False
                else:
                    valida=True
                    #print(f"ERROR - letra {letra} incorrecta en la fila {cadena}")
        return valida 
    else:
        print("ERROR - las filas no tiene 6 carácteres")
        return valida==False           
    #         if aux == ("A" or "T" or "C" or "G"):
    #             print(j)
    #         #     print(f"DENTRO DEL i{i} j{j} fila {adn[i]} caracter {aux[j]}")
    #             hay_error=True
    #         else:
    #             hay_error=False
    # return hay_error    
        
#Funcion que analiza y ordena los datos
# def is_mutant(adn):
#     for i in range(6):
        
           