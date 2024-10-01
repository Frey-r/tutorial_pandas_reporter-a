import tipos_de_datos

def saludar():
    print("Hola, mundo!")

def saludar_a(nombre):
    print(f"Hola, {nombre}!")

def sumar(a, b):
    print(f"Sumando...\n {a} + {b} = {a+b}")
    return a + b

def sumar_todos(*args):
    a=''
    for arg in args:
        a += f'{arg} + '
    print(f"Sumando...\n {a} = {sum(args)}")
    return sum(args)

def mostrar_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
