## Jogo da Forca;

## Criação das Variaveis;
resposta = [] ## Palavra Respostas
tentativas = [] ## Mostrar as letras Usadas
acertos = [] ## Mostrar a Respostas
vida = 6
laço = True

## Entrada e Formatação dos Dados;
palavra = input("Digite a palavra do jogo: ") 
dick = input("Digite uma dica para sua palavra: ")
palavra = palavra.upper().strip()
dick = dick.strip().capitalize()

## Espaço vaziu
print("\n \n \n \n \n \n \n \n \n")
print("\n \n \n \n \n \n \n \n \n")
print("\n \n \n \n \n \n \n \n \n")
print("\n \n \n \n \n \n \n \n \n")

## Soletrar a lista.
for i in palavra:
    resposta += i

## Loop para Adicionar a quantidade de letras no ACERTOS.
for i in resposta:
    acertos.append("_")

## Inicio do Jogo;
print("####################### Python Da Forca #########################################")
print(" ")

## Exibindo Quantidade de letras na resposta
print(f"A palavra secreta é: {acertos}")  

## Dica da palavra Secreta
print(" ")
print(f"Segue a DICA da palvra secreta abaixo:")
print(dick)
print("\n \n \n \n")

## Loop do Jogo.
while laço:
    num = 0
    letra = input("Digite a Letra: ")
    letra = letra.upper().strip()
    confirmação = False
    tentativas.append(letra)
    print(" ")  

    ## Loop para adicionar letras corretas;
    for i in resposta:
        if(letra == i):
            acertos[num] = letra
            num +=1
            confirmação = True
        else:
            num += 1
            pass   

    ## Exibindo Acertos e Tentativas
    print(f"A palavra é: {acertos}")  
    print(" ")
    print(f"Você utilizou essas letras até agora: {tentativas}")

    ## Perdendo Vidas e mensagem de Pontuação;
    if not confirmação:
        vida -= 1
        print(" ")
        print("Você Errou!!")
        print(f"VIdas: {vida}")
    else:
        print(" ")
        print("Você Acertou!!")  
        print(f"VIdas: {vida}") 

    ## Desenhos;
    if(vida == 6):
         print("  _______   ")
         print("  |     |   ")
         print("  |         ")
         print("  |         ")
         print("  |         ")
         print("  |         ")
         print("  |         ")
         print("=====       ")

    elif(vida == 5):
         print("  _______   ")
         print("  |     |   ")
         print("  |     0   ")
         print("  |         ")
         print("  |         ")
         print("  |         ")
         print("  |         ")
         print("=====       ")

    elif(vida == 4):
         print("  _______   ")
         print("  |     |   ")
         print("  |     0   ")
         print("  |     |   ")
         print("  |     |   ")
         print("  |         ")
         print("  |         ")
         print("=====       ")

    elif(vida == 3):
         print("  _______   ")
         print("  |     |   ")
         print("  |     0   ")
         print("  |    /|   ")
         print("  |     |   ")
         print("  |         ")
         print("  |         ")
         print("=====       ")

    elif(vida == 2):
         print("  _______   ")
         print("  |     |   ")
         print("  |     0   ")
         print("  |    /|\  ")
         print("  |     |   ")
         print("  |         ")
         print("  |         ")
         print("=====       ")

    elif(vida == 1):
         print("  _______   ")
         print("  |     |   ")
         print("  |     0   ")
         print("  |    /|\  ")
         print("  |     |   ")
         print("  |      \  ")
         print("  |         ")
         print("=====       ")

    elif(vida == 0):
         print("  _______   ")
         print("  |     |   ")
         print("  |     0   ")
         print("  |    /|\  ")
         print("  |     |   ")
         print("  |    / \  ")
         print("  |         ")
         print("=====       ")

    ## Ganhou ou Perdeu;
    if(vida == 0):
         print("Ixxxii, o feudo te Enforcou!! ") 
         print("\n \n \n \n") 
         laço =  False
    elif(acertos == resposta):
