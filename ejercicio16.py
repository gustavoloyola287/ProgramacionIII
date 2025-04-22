
#16. 3Suma más cercana
#Medio
#Temas
#Empresas
#Dada una matriz de números enteros numsde longitud ny un número entero target, encuentre tres números enteros en numstales que la suma sea la más cercana a target.

#Devuelve la suma de los tres números enteros .

#Se puede suponer que cada entrada tendría exactamente una solución.

 

#Ejemplo 1:

#Entrada: nums = [-1,2,1,-4], objetivo = 1
# Salida: 2
# Explicación: La suma que está más cerca del objetivo es 2. (-1 + 2 + 1 = 2).
#Ejemplo 2:

#Entrada: nums = [0,0,0], objetivo = 1
# Salida: 0
# Explicación: La suma que está más cerca del objetivo es 0. (0 + 0 + 0 = 0).

numeros = [5,8,3,2,10]
for numero in numeros:
    print(numero)
    
for i in range(len(numeros)):
    for j in range(i+1, len(numeros)):
        suma = numeros[i]+numeros[j]
        print(f"{numeros[i]} + {numeros[j]} = {suma}")
    
        
for i in range(len(numeros)):
    for j in range(i+1, len(numeros)):
        for k in range(j+1, len(numeros)):
            suma = numeros[i]+numeros[j]+numeros[k]
            print(f"{numeros[i]} + {numeros[j]} + {numeros[k]} = {suma}")