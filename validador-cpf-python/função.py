from suporte import *
from time import sleep

def digitacfp():
    """Função para validar a entrada dos dados, verificando o tipo de caractere e a quantidade correta."""
    cabecalho('Validação de CPF')
    while True:
        sleep(0.4)
        print()
        numCPF = str(input('Digite um CPF para saber se é válido: ')).strip().replace('.','').replace('-','')
        mesmoNumero = set(numCPF)
        if numCPF.isnumeric():
            if len(numCPF) != 11:
                sleep(0.4)
                print(f'{cor["vermelho"]}Erro! Digite a quantidade correta de caracteres!{cor["limpa"]}')
            elif len(mesmoNumero) == 1:
                sleep(0.4)
                print(f'{cor["vermelho"]}Erro! O CPF digitado só possui dígitos iguais.{cor["limpa"]}')
            else:
                return numCPF
        else:
            sleep(0.4)
            print(f'{cor["vermelho"]}Digite apenas números!{cor["limpa"]}')


def validaCPF(str):
    listaCPF = list(map(int, str))
    contador = 10
    soma = 0
    for i in listaCPF[0:9]:
        soma += i * contador
        contador -=1
    primeiroDigito = (soma * 10) % 11
    if primeiroDigito == 10 or primeiroDigito == 11:
        primeiroDigito = 0
    if primeiroDigito == listaCPF[9]:
        contador = 11
        soma = 0
        for i in listaCPF[0:10]:
            soma += i * contador
            contador -=1
        segundoDigito = (soma * 10) % 11
        if segundoDigito == 10 or segundoDigito == 11:
            segundoDigito = 0
        if segundoDigito == listaCPF[-1]:
            sleep(0.4)
            print(f'{cor["verde"]}O CPF é válido!{cor["limpa"]}')
        else:
            sleep(0.4)
            print(f'{cor["vermelho"]}O CPF não é válido!{cor["limpa"]}')
    else:
        sleep(0.4)
        print(f'{cor["vermelho"]}O CPF não é válido!{cor["limpa"]}')
    sleep(0.4)
    rodape()