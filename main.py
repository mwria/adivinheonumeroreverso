import random
comeco = 1
fim = 100
maior = fim
menor = comeco
jogar = 'Y'
contador = 0

while jogar == 'Y':
    maior = fim
    menor = comeco
    tentativa = random.randint(menor,maior)
    print(tentativa)
    direcao = 'N'
    while direcao != "C":
        direcao = input("Esse numero é Maior(M), Menor(N), ou correto?(C)")
        if direcao == "N":
            if tentativa > menor:
                menor = tentativa + 1
            tentativa = random.randint(menor,maior)
            print(tentativa)
        if direcao == "M":
            if tentativa < maior:
                maior = tentativa - 1
            tentativa= random.randint(menor,maior)
            print(tentativa)
        contador += 1
    print("Acertei! Depois de " + str(contador) + " tentativas.")
    jogar = input("continuar a jogar? Y/N")
