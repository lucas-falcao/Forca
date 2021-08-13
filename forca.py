import random
words = []
with open('forca.txt')as j:
    for line in j:
        line = line.rstrip()
        words.append(line)

palavra = random.choice(words)
chances = 6
acerto=True
acertando=[]
erros=0

oculta=[]
letras_acertadas=[]
for o in range(len(palavra)):
    oculta.insert(o,'_')
    letras_acertadas.insert(o,'-')
for s in palavra:
    acertando.append(s)

while True:
    if acertando == letras_acertadas:
        print(palavra.upper())
        print('Parabéns! Você ganhou o jogo \o/')
        break

    print('Você tem', chances, 'chances')
    print('A palavra é: ',','.join(oculta).replace(',',' '))
    letra = input('Digite uma letra: ')
    if letra == '':
        print('Por favor, você deve digitar uma letra -_-'.upper())
    elif letra in palavra:

        if letra in letras_acertadas:
            print('Perdeu uma chance: Você já digitou essa letra!')
            chances-=1
        else:
            print('Acertou :)')
        for n in range(len(palavra)):
            if palavra[n] == letra:
                letras_acertadas[n] = letra
                acertando[n]=letra
                oculta[n] = letra
    else:
        if chances > 0:
            erros=erros+1
            print('Errou pela',erros,'vez. Tente de novo!')
            chances -= 1
    if chances == 0:
        print('---PERDEU--- Que pena :( ')
        print('A palavra era:',palavra)
        break
    # print('*'*(len(oculta)*2))

'''
UFRPE
Lucas Alves Falcão
Prof.ª Camila Ascendina
Laboratório de Programação 1 / 2019.1
'''










