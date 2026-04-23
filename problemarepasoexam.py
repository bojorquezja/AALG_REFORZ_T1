"""
Cree un proyecto Python para almacenar y administrar el código de los 
productos de una zapatería. Describa un zapato con los siguientes 
atributos: modelo (string), talla (int), y precio (double). 
Crear un arreglo de clases
•	1 – Agregar(): Registrar un nuevo zapato, para lo cual buscará 
        linealmente tal que debe validar que no haya otro zapato 
        con los mismos 3 atributos e insertará el nuevo zapato en 
        la primera posición disponible. 
•	2 – Listar(): mostrará todos las zapatos creados sin ordenar
•	3 – BorraTalla(): Pedirá una talla, luego ordenará por método de 
        selección usando la talla para ordenar de mas a menos y mediante 
        búsqueda lineal buscará los zapato cuya talla coincida y los 
        eliminará del arreglo.
•	4 – BuscaTalla(): Ordenará el arreglo por la talla usando método 
        de inserción de menos a más. Luego preguntará una talla, y 
        usando la búsqueda binaria encontrará todos los zapatos esa 
        talla. Recuerde que como esta ordenado si hubieran varios 
        zapatos con la misma talla van a estar justo antes o después. 
        Use la menor cantidad de pasos para mostrar todos los zapatos 
        de la talla buscada
•	5 – ListaRecomendada(): Preguntará cuánto dinero tiene el cliente 
        y recomendará los zapatos a partir del más caro tal que la 
        suma no exceda el dinero del cliente. Use el algoritmo de 
        cambio de moneda. Ordene la lista de Zapatos con el método de 
        burbuja según el precio.
Tras terminar el código agregue 6 zapatos con los datos que considere 
y ejecute cada función creada
"""

class Zapato:
    def __init__(self, modelo = "", talla = 0, precio = 0):
        self.modelo = modelo 
        self.talla = talla 
        self.precio = precio
    
    def __str__(self):
        return f"{self.modelo} - {self.talla} (S/{self.precio})"
    
    def __repr__(self):
        return f"{self.modelo} [{self.talla}] S/{self.precio}"

def buscaZapato(lst, zapa) -> bool:
    for z in lst:
        if z.modelo == zapa.modelo and z.talla == zapa.talla and z.precio == zapa.precio:
            return True
    return False

def ordSeleccion(lst):
    n = len(lst)
    for mano in range(n-1):
        posMayor = mano
        for ver in range(mano + 1, n):
            if lst[ver].talla > lst[posMayor].talla:
                posMayor = ver
        lst[mano], lst[posMayor] = lst[posMayor], lst[mano]


lista = []        
while True:
    opc = int(input("1-Agregar, 2-Listar, 3-BorraTalla, 9-Salir"))
    if opc == 1:
        #crear nuevo
        modelo = input("Ingrese modelo:")
        talla = int(input("Ingrese talla:"))
        precio = float(input("Ingrese precio:"))
        nuevo = Zapato(modelo, talla, precio)
        #validar que no existe
        if not buscaZapato(lista, nuevo):
            print(nuevo)
            lista.append(Zapato(modelo, talla, precio))
            print(len(lista))
    elif opc == 2:
        print(lista)
    elif opc == 3:
        #ordenar seleccion
        ordSeleccion(lista)
        elitalla = int(input("ingrese talla a eliminar"))
        #elimina lineal
        for idx, q in enumerate(lista):
            if q.talla == elitalla:
                del lista[idx]
        
        
        
        