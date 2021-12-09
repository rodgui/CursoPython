#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Compreendendo o uso de argumentos - passo 6. """
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='Validação de nota')
    parser.add_argument('aluno', help="Nome do aluno")
    parser.add_argument('nota', help="Nota do aluno")

    args = parser.parse_args()

    print('\n')
    print('--- DADOS INFORMADOS ---')
    print("Aluno = {}".format(args.aluno))
    print("Nota = {}".format(args.nota))
    print('------------------------')
    print('\n')
    aluno = args.aluno
    nota = args.nota
    r = 'Resultado: '

    # a = [10, 5, 6, 8, 10, 9]
    # b = {'Adriano': 10, 'Bruno': 8, 'Manoel': 5, 'Ana': 7}
    # i = 4  # Indice do aluno
    # j = 'Bruno'  # Nome do aluno
    # j = aluno

    # Busca por matriz de nota
    # if (a[i] >= 9):
    #     print("Aprovado")
    # elif (a[i] >= 8):
    #     print("Recuperação")
    # else:
    #     print("Reprovado")

    # Busca por nome do aluno
    #print('Aluno: ' + j + ' - Nota: ' + str(b[j]))
    # if (b[j] >= 9):
    #     print(r + " " + "Aprovado")
    # elif (b[j] >= 8):
    #     print(r + " " + "Recuperação")
    # else:
    #     print(r + " " + "Reprovado")

    # Resultado

    print('**********************')
    if (int(nota) >= 6):
        print(r + " " + "Aprovado")
    elif (int(nota) >= 4):
        print(r + "Recuperação")
    else:
        print(r + "Reprovado")
    print('**********************')

    return 0


if __name__ == '__main__':
    sys.exit(main())
