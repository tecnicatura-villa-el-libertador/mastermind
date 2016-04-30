#!/usr/bin/env python3

"""
Este es módulo de nuestro jueguito Mastermind

"""
import random 
    

# agregar tu funcion acà
def ingresar_numero():
    while True:
        num = input ("ingrese 4 digitos: ")
        if verificar(num):
            print("tu numero es",num)
            return num


def crear_numero():
    """
    Selecciona digitos al azar(sin repetir)formando e 
    imprimiendo aleatoriamente numeros de x cifras    
    """

    digitos = [str(i) for i in range(10)]
 
    codigo = "" 
    for i in range(4):
        candidato = random.choice(digitos)
        while candidato in codigo:
            candidato = random.choice(digitos) 
        codigo = codigo + candidato
    return codigo


def evaluar(numero, numero_objetivo):
    """
    Función de Evaluación:
    Nuestro código recibe dos números de cuatro cifras y los compara. Devuelve aciertos Plenos y Parciales.
    Si los aciertos son Plenos significa que coincide el dígito y la posición.
    Si los aciertos son Parciales significa que coincide el dígito pero no la posición.
    """
    plenos = 0
    parciales = 0
    intentos = 0
    cant_digitos = 4

    for i in range(cant_digitos):
        if numero[i] == numero_objetivo [i]:
            plenos = plenos + 1
        elif numero[i] in numero_objetivo:
            parciales = parciales + 1
    return (plenos, parciales)




def verificar(numero):
    pass


def reportar(numero, plenos, parciales):
    pass


def principal():
    pass


if __name__ == '__main__':
    principal()
