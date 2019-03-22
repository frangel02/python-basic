#Listas

'''lista = [1, 2, 3]
lista2 = ["aaaa", "bbbb", "cccc"]
lista3 =[1, "c", 1.2, True]
lista[0] = 1000
print(lista)'''

lista = [1, 2, 3, 4, 5, 6]
listaB = [10, 100, 1000]
'''for elemento in lista:
    print(elemento)

lista.append(100)
print(lista)

lista[6] = 'hola'
print(lista)
lista.pop()
print(lista)'''


lista.extend(listaB)
print(lista)

#del lista[5]
lista.remove(5)
print(lista)
print(lista.count(6))
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
print(lista[-2])
