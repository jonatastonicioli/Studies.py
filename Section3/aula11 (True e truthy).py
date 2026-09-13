teste = "1"
# print(type(teste))

print(bool(teste))


if teste: #if teste == True nn vai pois a string nn vazia é considerada truty e não true
    print("olá")




#sao considerados como falsy o 0 0.0 ''
#o python para de compilar se achar uma condição False com o operador and,
#isso e chamado da avaliação de curto circuito.

print(True and True and True) #true
print(True and False and True) #false
print(True and 0 and True) #retorna 0
print(True and 0.0 and True) #retorna 0.0
print(True and "" and True) #retorna a string vazia




