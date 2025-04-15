
#67. Sumar binario
#Fácil
#Temas
#Empresas
#Dadas dos cadenas binarias a y b, devuelve su suma como una cadena binaria .

 

#Ejemplo 1:

#Entrada: a = "11", b = "1"
# Salida: "100"
#Ejemplo 2:

#Entrada: a = "1010", b = "1011"
# Salida: "10101"
 

#Restricciones:

#1 <= a.length, b.length <= 104
#a y b constan únicamente de caracteres '0'o .'1'
#Cada cadena no contiene ceros iniciales, excepto el cero mismo.

num1 = "1011" # 11 en decimal
num2 = "1101" # 13 en decimal
suma = bin(int(num1,2) + int(num2,2))[2:]

print(f"La suma de los numeros binarios {num1} y {num2} es: {suma}")

def sumar_numeros():
    print("¿Qué tipo de números vas a ingresar?")
    print("1. Decimal")
    print("2. Binario")
    
    opcion=input("Eleguí una opción ")
    
    if opcion == "1":
        num3 = int(input("Ingresa el primer número decimal: "))
        num4 = int(input("Ingresa el segundo número decimal: "))
    
    elif opcion == "2":
        bin1 = input("Ingresa el primer número binario: ")    
        bin2 = input("Ingresa el segundo número binario: ") 
        
        num3 = int(bin1,2)   
        num4 = int(bin2,2)   
    
    else:
        print("Opción no valida")   
        return 

    suma1 = num3 + num4
    print("\nResultado: ")
    print(f"En decimal: {suma1}")
    print(f"En binario: {bin(suma1)[2:]}")
    
    
sumar_numeros()


