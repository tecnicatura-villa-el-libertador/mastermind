#!/usr/bin/env python3

"""
Este es módulo de nuestro jueguito Mastermind

"""
import random 
    

# agregar tu funcion acà
def ingresar_numero():
    pass


def crear_numero():
    digitos = ("0","1","2","3","4","5","6","7","8","9") 
    codigo = "" 
    for i in range(4):
        candidato = random.choice(digitos)
        while candidato in codigo:
            candidato = random.choice(digitos) 
        codigo = codigo + candidato
    return codigo


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
