"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

nome = "jonatas tonicioli das neves"

print(f"{nome[2:]}") #omitir o restante = pega o restante da string 
print(f"{nome[2:len(nome):1]}") #faz a msm coisa da linha de cima

print(f"{nome[2:5]}") #final nao é incluido
print(f"{nome[8::2]}") #passo 2

print(f"{nome[::-1]}") #passo -1 inverte a string

print(len(nome))