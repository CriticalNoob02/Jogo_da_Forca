"""

tarefa1 = []
concluir = True

while concluir:
    atv = input("Descreva a atividade: ")

    tarefa1.append(atv)

    print(f"Sua próxima atividade é: {tarefa1[-1]}")
    finalizar = int(input("Voce deseja finalizar as atividades? (S=1 / N=2) "))
    if(finalizar == 1):
        concluir = False
    else:
        pass    

print(f"Parabens, você conclui suas tarefas.")
for i in tarefa1:
    print(i)

"""

"""

## Tabuada Personalizada

num1 = int(input("Digite o numero que deseja multiplicar: "))
qtd = int(input("Digite a Quantidade de vezes que deseja multiplicar: ")) 
inicio = int(input("Digite o númwero que deseja iniciar a multiplicação: ")) 
inicio1 = ""
soma = inicio+qtd
tabuada = []
confirmação = True



while confirmação:
    
    if(inicio1 == ""):
        inicio1 = inicio
        tabuada.append(inicio1)

    elif( inicio1 == soma):
        confirmação = False

    else:
        inicio1 += 1
        tabuada.append(inicio1)

for i in tabuada:
    print(f"{num1} X {i} = {num1*i}")

print(tabuada)    

"""

## Jogo da Forca;

resposta = []
tentativas = []
acertos = []
palavra = input("Digite a palavra do jogo: ")
palavra = palavra.upper().strip()
vida = 6
laço = True

for i in palavra:
    print(i)
    resposta += i

print(resposta)
while laço:
    print(acertos)
    letra = input("Digite a Letra: ")
    letra = letra.upper().strip()
    confirmação = False
    tentativas.append(letra)
    print(tentativas)
    print(" ")

    for i in resposta:
        if(letra == i):
            print("Acertou")
            acertos.append(letra)
            confirmação = True
        else:
            acertos.append("_")
            
    if not confirmação:
        vida -= 1
        print("Errou")
        print(vida)

    if(vida == 0):
         print("Ixxxii, você acabou de se enforcar!! ")  
         laço =  False
