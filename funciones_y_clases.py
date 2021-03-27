global1 = 34

def cambiar_global(valor_global):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1 
    global1 = valor_global


def anio_bisiesto(anio):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    if(anio % 4 == 0):
        if(anio % 100 == 0 and not anio % 400 == 0):
            return False
        return True
    return False 

def contar_valles(lista):
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    contadorValles = 0
    entradaValle = False

    for paso in lista:
        if paso == -1:
            entradaValle = True
        elif paso == 1:
            if(entradaValle):
                contadorValles+=1
                entradaValle= False
    return contadorValles    
        

def saltando_rocas(lista):
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    saltos = 0
    ultimo = len(lista) -1
    actual = 0
    
    def paso_valido(actual, posiciones):
        salto = actual + posiciones
        return salto > ultimo or not lista[salto] == 1           
    for index, paso in enumerate(lista):
        if actual >= ultimo:
            break
        elif(index != actual):
            continue
        elif paso_valido(actual,2):
            actual += 2
            saltos += 1
        elif paso_valido(actual,1):
            actual += 1
            saltos += 1 
    return saltos

def pares_medias(lista):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    
    Las medias que no tengan pares no deberían ser incluídas en el diccionario.
    '''
    colores = set(lista)
    pares = dict.fromkeys(colores,0)

    for media in lista:
        pares[media] += 1
    for color in list(pares):
        if pares[color] == 1:
            pares.pop(color)
            continue
        elif pares[color] % 2 != 0:
            pares[color] -= 1
        pares[color] = int(pares[color]/2)
    return pares

# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'

class ListaComa:
 
    def __init__(self,lista):
        self.lista = lista

    def __str__(self):
        return str(self.lista).strip("[]").replace(" ","")

# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'

class Persona:
 
    def __init__(self,nombres,apellidos):
        
        self.nombres = []
        self.apellidos = []

        for nombre in nombres:
            self.agregar_a_lista(nombre,self.nombres)
        for apellido in apellidos:
            self.agregar_a_lista(apellido,self.apellidos)

    def nombre_completo(self):
        nom_com = self.nombres + self.apellidos
        return ' '.join(nom_com).strip()

    def agregar_a_lista(self,valor,lista):
        if isinstance(valor,str):
            lista.append(valor.lower().capitalize())

# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.
from datetime import date

class Persona1(Persona):

  def __init__(self,nombres,apellidos,fecha_nacimiento):
      super().__init__(nombres,apellidos)
      self.fecha_nacimiento = fecha_nacimiento

  def edad(self):
      fecha_actual = date.today() - self.fecha_nacimiento
      return int(fecha_actual.days/365.25)