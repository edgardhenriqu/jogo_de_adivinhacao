def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    letras_faltando = str(letras_acertadas.count('_'))
    print( 'ainda falta acerta {} letras'.format(letras_faltando))

    enforcou = False
    acertou = False

    print(letras_acertadas)

    #enquato (True)
    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)


    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()
