# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
nome = 'Otávio'
print(nome[2])
print(nome[-4])

# print ('á' in nome) #percorre otavio e ve se tem á
# print ('s' in nome) #percorre otavio e ve se tem á
# print (10 * "-") # fazer um traço grande
# print ('á' not in nome) # inverte o valor do in
# print ('s' not in nome) #inverte o valor do in

nome = input("Digite seu nome: ")
encontrar = input("Digite oque vc quer encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")








