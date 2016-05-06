#!/usr/bin/env python3

"""
Este es módulo de nuestro jueguito Mastermind

"""
import random



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
    if not numero.isdigit():
        return False
    if len(numero) != 4:
        return False
    if len(set(numero)) != 4:
        return False
    return True



def reportar(numero, plenos, parciales):

    pleno_str = 'pleno' if plenos == 1 else 'plenos'
    parciales_str = 'parcial' if parciales == 1 else 'parciales'

    s = "El numero {} tiene {} {} y {} {}"
    return s.format(numero, plenos, pleno_str, parciales, parciales_str)


# agregar tu funcion acà
def principal():
    objetivo = crear_numero()
    while True:
        num = input ("ingrese 4 digitos: ")
        if verificar(num):
            pleno, parcial = evaluar(num, objetivo)
            print(reportar(num, pleno, parcial))
            if pleno == 4:
                print('Ganaste!')
                return
        else:
            print('Numero no válido!')



if __name__ == '__main__':
    principal()
