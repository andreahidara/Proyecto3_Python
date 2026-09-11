# ==============================================================================
# Proyecto 3 - Katas Python
# Archivo de resolución de ejercicios
# Contiene los 40 ejercicios solicitados usando diversas estructuras y métodos.
# ==============================================================================

from functools import reduce
import math

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva
# un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencias_letras(cadena):
    cadena = cadena.replace(" ", "")
    frecuencias = {}
    for letra in cadena:
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
def doblar_valores(lista):
    return list(map(lambda x: x * 2, lista))

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def palabras_que_contienen(lista_palabras, objetivo):
    return [palabra for palabra in lista_palabras if objetivo in palabra]

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5).
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado.
# Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla (media, estado).
def evaluar_media(notas, nota_aprobado=5):
    if not notas:
        return 0, "suspenso"
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: " ".join(map(str, t)), lista_tuplas))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones.
def dividir_numeros():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
        print(f"División exitosa: {resultado}")
    except ValueError:
        print("Error: Ingresaste un valor que no es numérico.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. Usa la función filter().
def mascotas_permitidas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, mascotas))

# 10. Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass

def calcular_promedio(lista):
    try:
        if not lista:
            raise ListaVaciaError("La lista no puede estar vacía para calcular el promedio.")
        return sum(lista) / len(lista)
    except ListaVaciaError as e:
        print(f"Excepción capturada: {e}")
        return None

# 11. Escribe un programa que pida al usuario que introduzca su edad. Maneja excepciones de valor no numérico
# o fuera de rango (0-120).
def solicitar_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera del rango válido (0-120).")
        print(f"Tu edad es {edad}.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")

# 12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa map().
def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

# 13. Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas
# con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa map().
def mayus_minus(conjunto_caracteres):
    caracteres_unicos = list(set(conjunto_caracteres))
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))

# 14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa filter().
def palabras_por_letra(palabras, letra):
    return list(filter(lambda p: p.startswith(letra), palabras))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_3_a_lista = lambda lista: list(map(lambda x: x + 3, lista))

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros
# y devuelva una lista de todas las palabras que sean más largas que n. Usa filter().
def palabras_mas_largas(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda p: len(p) > n, palabras))

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Usa reduce().
def lista_a_numero(digitos):
    return reduce(lambda acc, d: acc * 10 + d, digitos)

# 18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes
# y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Pedro", "edad": 21, "calificacion": 90}
]
excelentes = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

# 19. Crea una función lambda que filtre los números impares de una lista dada.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# 20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa filter().
def solo_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
cubo = lambda x: x ** 3

# 22. Dada una lista numérica, obtén el producto total de los valores. Usa reduce().
def producto_total(lista):
    if not lista: return 0
    return reduce(lambda x, y: x * y, lista)

# 23. Concatena una lista de palabras. Usa reduce().
def concatenar_palabras(lista_palabras):
    if not lista_palabras: return ""
    return reduce(lambda a, b: a + b, lista_palabras)

# 24. Calcula la diferencia total en los valores de una lista. Usa reduce().
def diferencia_total(lista):
    if not lista: return 0
    return reduce(lambda a, b: a - b, lista)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    return len(cadena)

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
resto = lambda a, b: a % b

# 27. Crea una función que calcule el promedio de una lista de números.
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare
# todos los caracteres con el carácter '#' excepto los últimos cuatro.
def enmascarar_variable(var):
    texto = str(var)
    if len(texto) <= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]

# 30. Crea una función que determine si dos palabras son anagramas.
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.replace(" ", "").lower()) == sorted(palabra2.replace(" ", "").lower())

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar.
# Si está en la lista, imprime que fue encontrado; de lo contrario, lanza una excepción.
class NombreNoEncontradoError(Exception):
    pass

def buscar_nombre():
    entrada = input("Ingresa una lista de nombres separados por coma: ")
    nombres = [n.strip() for n in entrada.split(",")]
    objetivo = input("Ingresa el nombre a buscar: ")
    
    if objetivo in nombres:
        print(f"El nombre '{objetivo}' fue encontrado.")
    else:
        raise NombreNoEncontradoError(f"El nombre '{objetivo}' NO está en la lista.")

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre
# en la lista y devuelva el puesto del empleado.
def buscar_empleado(nombre, lista_empleados):
    for emp in lista_empleados:
        if emp.get("nombre") == nombre:
            return emp.get("puesto")
    return "La persona no trabaja aquí"

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))

# 34. Crea la clase Arbol
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
        
    def crecer_tronco(self):
        self.tronco += 1
        
    def nueva_rama(self):
        self.ramas.append(1)
        
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]
        
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
            
    def info_arbol(self):
        return f"Tronco: {self.tronco}, Ramas: {len(self.ramas)}, Longitudes ramas: {self.ramas}"

# 35. Crea la clase UsuarioBanco
class TransaccionError(Exception):
    pass

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
        
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise TransaccionError("Saldo insuficiente para retirar.")
        self.saldo -= cantidad
        
    def transferir_dinero(self, otro_usuario, cantidad):
        try:
            self.retirar_dinero(cantidad)
            otro_usuario.agregar_dinero(cantidad)
        except TransaccionError:
            raise TransaccionError("Fallo en la transferencia por saldo insuficiente.")
            
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# 36. Crea una función llamada procesar_texto
def procesar_texto(texto, opcion, *args):
    def contar_palabras(t):
        palabras = t.split()
        dicc = {}
        for p in palabras:
            dicc[p] = dicc.get(p, 0) + 1
        return dicc

    def reemplazar_palabras(t, original, nueva):
        return t.replace(original, nueva)

    def eliminar_palabra(t, palabra):
        return " ".join([p for p in t.split() if p != palabra])

    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) == 2:
            return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) == 1:
            return eliminar_palabra(texto, args[0])
    return None

# 37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora
def obtener_momento_dia(hora):
    if 6 <= hora < 13:
        return "Día"
    elif 13 <= hora < 20:
        return "Tarde"
    else:
        return "Noche"

# 38. Escribe un programa que determine qué calificación en texto tiene un alumno
def calificacion_texto(calificacion):
    if 0 <= calificacion <= 69:
        return "insuficiente"
    elif 70 <= calificacion <= 79:
        return "bien"
    elif 80 <= calificacion <= 89:
        return "muy bien"
    elif 90 <= calificacion <= 100:
        return "excelente"
    return "Nota fuera de rango"

# 39. Escribe una función que tome dos parámetros: figura y datos
def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio = datos[0]
        return math.pi * (radio ** 2)
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    return None

# 40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra
def calcular_compra():
    precio_original = float(input("Precio original del artículo: "))
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
    
    if tiene_cupon in ["sí", "si"]:
        valor_cupon = float(input("Valor del cupón de descuento: "))
        if valor_cupon > 0:
            precio_final = max(0, precio_original - valor_cupon)
            print(f"Se aplicó el descuento. Precio final: {precio_final}")
        else:
            print(f"El cupón no es válido. Precio final: {precio_original}")
    else:
        print(f"No se aplicó descuento. Precio final: {precio_original}")
