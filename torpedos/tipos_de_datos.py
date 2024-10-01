#Tipos de Datos:
def Tipos_de_Datos_Numéricos():
    #int: Almacena números enteros.
    numero_entero = 42

    #float: Almacena números de punto flotante (decimales).
    numero_flotante = 3.14

    #complex: Almacena números complejos (tienen una parte real y una parte imaginaria).
    numero_complejo = 1 + 2j

    return numero_entero, numero_flotante, numero_complejo

def Tipo_de_Datos_Booleano():
    #bool: Almacena valores booleanos (True o False).
    es_verdadero = True
    es_falso = False
    return es_verdadero, es_falso

def Tipos_de_Datos_de_Secuencia():
    #str: Almacena cadenas de texto (secuencias de caracteres).
    texto = "Hola, mundo!"

    #lista: Almacena una secuencia ordenada de elementos (puede contener elementos de diferentes tipos).
    lista = [1, 2, 3, "cuatro", 5.0]

    #tupla: Similar a la lista, pero es inmutable (no se puede modificar después de su creación).
    tupla = (1, 2, 3, "cuatro", 5.0)

    #range: Almacena una secuencia de números generada automáticamente (utilizada en loops).
    rango = range(1, 10)

    return texto, lista, tupla, rango

def Tipo_de_Datos_de_Conjunto():
    #set: Almacena una colección no ordenada de elementos únicos.
    conjunto = {1, 2, 3, 4, 5}

    #frozenset: Similar a set, pero es inmutable.
    conjunto_inmutable = frozenset({1, 2, 3, 4, 5})

    return conjunto, conjunto_inmutable

def Tipo_de_Datos_de_Mapeo():
    #dict: Almacena una colección de pares clave-valor (similar a mapas o diccionarios en otros lenguajes).
    diccionario = {"nombre": "John", "edad": 30, "ciudad": "Nueva York"}
    return diccionario

def Tipo_de_Datos_None():
    #None: Representa la ausencia de valor o un valor nulo.
    sin_valor = None

    return sin_valor

def Tipo_de_Datos_Collections():
    #Listas anidadas: Listas dentro de listas.
    lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    #Diccionarios anidados: Diccionarios dentro de diccionarios.
    diccionario_anidado = {"persona1": {"nombre": "John", "edad": 30}, "persona2": {"nombre": "Jane", "edad": 25}}

    #Conjuntos de Tuplas: Tuplas dentro de conjuntos.
    conjunto_tuplas = {(1, 2), (3, 4), (5, 6)}

    return lista_anidada, diccionario_anidado, conjunto_tuplas
