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