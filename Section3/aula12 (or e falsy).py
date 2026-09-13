# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: #colocar parenteses para organizar as condicoes
#     print('Entrar')
# else:
#     print('Sair')

#na avaliacao de curto circuito do operador or, o python parar a avalicao se achar um valor True

print(True or False)
print(0 or False or 0.0 or "abc") #retorna abc pois é truthy (nn esta na lista dos falsy 0 0.0 '')


