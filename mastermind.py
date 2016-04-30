#!/usr/bin/env python3

"""
Este es módulo de nuestro jueguito Mastermind

"""


# agregar tu funcion acà
def ingresar_numero():
    while True:
        num = input ("ingrese 4 digitos: ")
        if verificar(num):
            print("tu numero es",num)
            return num


def crear_numero():
    pass


def evaluar(numero, numero_objetivo):
    pass


def verificar(numero):
    pass


def reportar(numero, plenos, parciales):
    pass


def principal():
    pass


if __name__ == '__main__':
    principal()
