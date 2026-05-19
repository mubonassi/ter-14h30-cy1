print("| SISTEMA DE CADASTRO E LOGIN |")
print("-"*30)

usuarioCadastro = input("Digite aqui o usuário para cadastrar: ")
senhaCadastro = input("Digite aqui a senha para cadastrar: ")
print("| CADASTRO REALIZADO COM SUCESSO |")
print("-"*30)
print("| Agora faça o Login! |")

usuarioLogin = input("Usuario: ")
senhaLogin = input("Senha: ")

if usuarioCadastro == usuarioLogin and senhaCadastro == senhaLogin:
    print(">> Login realizado com sucesso!")
else:
    print(">> Usuário ou Senha Incorretos!")