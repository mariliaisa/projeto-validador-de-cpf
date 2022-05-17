import emoji
cor = {
    'limpa': '\033[0m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azulclaro': '\033[1;34m',
    'lilás': '\033[1;35m',
    'azulpiscina': '\033[1;36m',
    'preto': '\033[1;37m',
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'negrito_sublinhado': '\033[1;4',
    'inverter': '\033[7m'}

#Função para continuar programa:
def quer_continuar():
    while True:
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Opção inválida. Tente novamente.')
    if continuar in 'S':
        escolha = True
    else:
        escolha = False
    return escolha

#FUNÇÃO PARA IMPRIMIR UM CABEÇALHO
def cabecalho(texto):
    print()
    print('=-'*20)
    print(emoji.emojize(':sparkles:{}{:^40}{}:sparkles:'.format(cor['amarelo'],texto, cor['limpa'], language = 'alias')))
    print('=-'*20)
    print()

#FUNÇÃO PARA RODAPÉ
def rodape():
    print()
    print('=-'*20)
    print('{:^40}'.format('FIM'))
    print('=-'*20)
    print()

#FUNÇÃO SEXO
def qualsexo():
    while True:
        sexo = str(input('Qual o seu sexo?(F/M) ')).strip().upper()
        if sexo in 'FM':
            break
        else:
            print('Opção inválida.')
    return sexo
