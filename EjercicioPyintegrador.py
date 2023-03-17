"""Antes que nada profe, perdon por poner # en todos los renglones"""

#1. Escribir una función que calcule el máximo común divisor entre dos números.

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


#2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def mcm(a, b):
    return (a*b)//mcd(a, b)

#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(texto):
    palabras = texto.split()
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.

def contar_palabras(texto):
    palabras = texto.split()
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

def palabra_mas_repetida(diccionario):
    palabra_max = max(diccionario, key=diccionario.get)
    return (palabra_max, diccionario[palabra_max])


#5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
#cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
#del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
#ejercicio tanto de manera iterativa como recursiva.
#iterativa
def get_int():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            return num
        except ValueError:
            print("Error: Debe ingresar un número entero.")
#recursiva
def get_int():
    try:
        num = int(input("Ingrese un número entero: "))
        return num
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return get_int()



#6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
#siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
#datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("Error: el nombre debe ser una cadena de caracteres")

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.__edad = edad
        else:
            print("Error: la edad debe ser un número entero positivo")

    def set_dni(self, dni):
        if isinstance(dni, str):
            self.__dni = dni
        else:
            print("Error: el DNI debe ser una cadena de caracteres")

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("DNI:", self.__dni)

    def es_mayor_de_edad(self):
        return self.__edad >= 18




#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
#persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Crear los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
#rojos.
class Cuenta:
    
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
        
    def set_titular(self, titular):
        self.__titular = titular
        
    def get_titular(self):
        return self.__titular
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
        
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"Titular: {self.__titular}, Cantidad: {self.__cantidad}")
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            
    def retirar(self, cantidad):
        self.__cantidad -= cantidad

#8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
#CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
#además del titular y la cantidad se debe guardar una bonificación que estará expresada en
#tanto por ciento. Crear los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
#tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
#mayor de edad pero menor de 25 años y falso en caso contrario.
# Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
#cuenta.

class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
        
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
        
    def get_bonificacion(self):
        return self.__bonificacion
    
    def es_titular_valido(self):
        # asumiendo que la fecha de nacimiento del titular se encuentra en la variable fecha_nacimiento
        edad = calcular_edad(fecha_nacimiento)
        if edad >= 18 and edad < 25:
            return True
        else:
            return False
        
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
            
    def mostrar(self):
        print(f"Cuenta Joven, Bonificación: {self.__bonificacion}%")

