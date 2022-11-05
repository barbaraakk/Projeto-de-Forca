arquivo = open("txt.txt",'r')
import random
palavra = random.choice(arquivo.readlines()).strip("\n").upper()
 
letras = [letra for letra in palavra]
secreto = ["-" for letra in palavra]
chance = 5
lista = []
    
print("\n--Jogo da Forca--\n".upper())
print("\nTema: Jogos\n".upper())
        
print("A palavra tem".upper(), len(secreto), "letras".upper())

while chance > 0:
    print(secreto)
    tentativa = input("Digite uma letra: ").upper()
    print ('\n')
    if tentativa in lista:
        print(f"Você já digitou essa letra.".upper())
    elif tentativa in letras:
        a = 0
        for letra in palavra:
            if tentativa == letra:
                secreto[a] = tentativa
            a += 1
        lista.append(tentativa)
    else:
        chance -= 1
        print(f"Letra errada\n".upper())
        lista.append(tentativa)
    if secreto == letras:
        break
    print(f"Te restam {chance} chances".upper())
if chance == 0:
    print("Você perdeu.")
    print(f"A palavra certa era {palavra} ".upper())
else:
    print("Você ganhou".upper())
    print(f"A palavra era {palavra} ".upper())