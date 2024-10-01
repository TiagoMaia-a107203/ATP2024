import random

print("""Bem vindo ao jogo dos 21 fósforos! As regras são simples:
No início começa-se com 21 fósforos e a cada rodada tanto o jogador como o pc pode retirar entre 1 a 4 fósforos!
Os jogadores jogam alternadamente e quem tirar o último fósforo perde.
Existem ainda duas modalidades:
    1- O jogador começa primeiro e depois o computador;
    2- O computador começa em primeiro e depois o utilizador.""")
print("Que modalidade quer jogar?")
mod=input("Escreva 1 ou 2.")
i=21

while mod != "1" and mod != "2":
    print("Resposta inválida! Escreva 1 ou 2")
    mod = input("Escreva 1 ou 2!")

if mod == "1":
    while i >1:
        print("Diga um número de 1 a 4 que queira retirar")
        numj = int (input("Diga um número:"))
        while numj<1 or numj>4:
            print("Resposta inválida Tente novamente")
            numj = int (input("Diga um número:"))
        i = i - numj
        print(f"Tirei {numj} e faltam {i} fósforos na pilha")
        numc = 5 - numj
        i= i -numc
        print(f"O computador retirou {numc} de fósforos e ainda faltam {i} na pilha")
    print("Como na pilha falta 1 fósforo significa que o pc ganhou!")

if mod == "2":
    while i>1:
        if i== 1 or i ==6 or i ==11 or i ==16 or i ==21:
            numc2 = random.randint(1,4)
            i =i -numc2
            print(f"O computador retirou {numc2} de fósforos e ainda faltam {i} na pilha")
            numj2 = int(input("Diga um número:"))
            while numj2<1 or numj2>4 and numj2 >i:
                print("Resposta inválida Tente novamente")
                numj2 = int (input("Diga um número:"))
            i = i - numj2
            print(f"Tirei {numj2}. Faltam {i} fósforos na pilha")
        if i == 1:
            print("O jogador ganhou!!")
        else :
            numc2 = 0
            while i >=1:
                while i !=1 and i !=6 and i !=11 and i !=16 :
                    numc2 = numc2 +1
                    i = i - 1
                print(f"O computador retirou {numc2} de fósforos e ainda faltam {i} na pilha")
                print("Escolha um número:")
                numj2 = int(input("Diga um número:"))
                while numj2<1 or numj2>4 or numj2 >i:
                    print("Resposta inválida Tente novamente")
                    numj2 = int (input("Diga um número:"))
                i = i - numj2
                print(f"Tirei {numj2}. Faltam {i} fósforos na pilha")
                numc2 = 5 - numj2
                i =i -numc2
            print("O Pc ganhou!!")
            
