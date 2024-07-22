
palavra_secreta = "abacate"
palavra_correta= ''


while True:
    letra = input('Digite uma letra: ')


    if letra in palavra_secreta:
        palavra_correta += letra

    for letra_secreta in palavra_secreta:
        if letra_secreta in palavra_correta:
            print(letra_secreta)
        else:
            print('*')
        
        