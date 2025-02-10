
#Parcial 2 Programación

#Ejercicio 1
#Desarrollar un programa que determine si en una lista no existen elementos repetidos

lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    if lista.count(i) > 1:
        print(f"El numero {i} se repite")
        break
else:
        print("No se repite ningún elemento de la lista")

#Ejercicio 2
#Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla
#y si no existe debe imprimir "No existe". 

lista = ("Jaaaa", "Ettgt", "Safff", "Gutrrz")
vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
for i in vocales:
    if i in lista:
        print(i)
        break
else:
    print("No existe")
      
#Ejercicio 3
#Desarrollar un ejercicio que dadas dos listas determine qué elementos tiene la primera lista que no tenga la segunda lista 

lista1 = [1,2,3,4,11]
lista2 = [5,6,7,8,9]
for i in lista1:
    if i in lista2:
        print(f"El elemento {i} se encuentra en ambas listas")
        break
else: 
    print("No hay elementos repetidos")
 
#Ejercicio 4
#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales 

Lista = [1.5,2,3,4,5.8,6,7,8.333,9,10.999]

suma = sum(Lista)
promedio = suma / len(Lista)
print(f"El promedio de la lista es {promedio}")

#Ejercicio 5
#Desarrollar un algoritmo que determine la mediana de un arreglo de enteros. La mediana es el número que queda en la mitad del arreglo después de ser ordenado.

Lista = [9,7,1,5,3,2,6,8,11,7,12]

lista_ordenada = Lista.sort()
mediana = len(Lista) // 2
print(f"La mediana de la lista es {mediana}")




