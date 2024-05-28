def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[0]
    
    menores = []
    mayores = []
    
    # Iterar sobre todos los elementos de la lista excepto el pivote
    for x in lista[1:]:
        if x <= pivote:
            menores.append(x)
        else:
            mayores.append(x)
    
    # Llamar recursivamente a quicksort en las sublistas menores y mayores
    return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo
lista_desordenada = [33, 10, 55, 71, 29, 3, 45, 12, 15, 22, 4]
lista_ordenada = quicksort(lista_desordenada)
print(lista_ordenada)

assert quicksort([]) == []
assert quicksort([1]) == [1]
assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
assert quicksort([5,4, 6, 8, 9, 1, 3, 10, -2, -4]) == [-4, -2, 1, 3, 4, 5, 6, 8, 9, 10]
assert quicksort([5, 3, 3, 2, 4, 1, 1]) == [1, 1, 2, 3, 3, 4, 5]
assert quicksort([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]) == [-9, -6, -5, -5, -5, -4, -3, -3, -2, -1, -1]
assert quicksort([1000000, 999999, -1000000, -999999, 0]) == [-1000000, -999999, 0, 999999, 1000000]
assert quicksort([92, 27, 33, 48, 12, 55, 34, 91, 5, 87, 72, 58, 19, 47, 3, 50, 23, 62, 82, 41, 20, 38, 15, 31, 81, 16, 10, 13, 70, 45, 79, 64, 85, 2, 89, 77, 43, 69, 88, 26, 30, 35, 78, 63, 74, 73, 68, 1, 17, 46, 22, 21, 65, 25, 52, 39, 37, 60, 76, 32, 6, 42, 29, 4, 40, 83, 53, 54, 59, 71, 14, 66, 84, 67, 24, 51, 56, 36, 11, 86, 44, 28, 9, 75, 8, 7, 18, 49, 61, 57, 90, 80, 99, 100, 98, 97, 95, 96, 93, 94]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

print("Prueba superada")