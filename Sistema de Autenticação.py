import os

cadastro_valido = True

print('\nSistema de Autenticação')    
print('Lembre-se: o login e a senha precisam ter pelo menos 5 caracteres cada e devem ser diferentes.\n')

login_usuario = input('Digite um nome de login: ')
senha_usuario = input('Digite sua senha: ')

# 1. TESTA A PRIMEIRA TENTATIVA
if len(login_usuario) < 5 or len(senha_usuario) < 5:
    print('\nErro: O login e a senha precisam ter pelo menos 5 caracteres.')
    print('Você tem mais UMA tentativa para se cadastrar.\n')

    # Segunda chance (1ª tentativa falhou por tamanho)
    login_usuario = input('Digite um nome de login: ')
    senha_usuario = input('Digite sua senha: ')

    # Valida tudo da segunda chance (tamanho OU igualdade)
    if len(login_usuario) < 5 or len(senha_usuario) < 5 or login_usuario == senha_usuario:
        print('\nCadastro cancelado por dados inválidos.')
        cadastro_valido = False 
    
elif login_usuario == senha_usuario:
    print("\nErro: O login e a senha não podem ser iguais.")
    print('Você tem mais UMA tentativa para se cadastrar.\n')

    # Segunda chance (1ª tentativa falhou por igualdade)
    login_usuario = input('Digite um nome de login: ')
    senha_usuario = input('Digite sua senha: ')
    
    # Valida TUDO da segunda chance (tamanho OU igualdade)
    if len(login_usuario) < 5 or len(senha_usuario) < 5 or login_usuario == senha_usuario:
        print('\nCadastro cancelado por dados inválidos.')
        cadastro_valido = False

# --- ETAPA DE LOGIN (Só executa se o cadastro terminou VÁLIDO) ---
if cadastro_valido:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Cadastro realizado com sucesso!')
    print('Entre na plataforma \n')
    login_plataforma = input('Digite seu login: ')
    senha_plataforma = input('Digite sua senha: ')

    if login_usuario == login_plataforma and senha_usuario == senha_plataforma:
        print('\nAcesso permitido com sucesso')
    else: 
        # 2ª tentativa de login
        print('\nAcesso negado, verifique os campos de login e senha')
        print('Você só tem mais duas tentativas \n')
        
        login_plataforma = input('Digite seu login: ')
        senha_plataforma = input('Digite sua senha: ')

        if login_usuario == login_plataforma and senha_usuario == senha_plataforma:
            print('\nAcesso permitido com sucesso')
        else: 
            # 3ª e última tentativa de login
            print('\nAcesso negado, verifique os campos de login e senha')
            print('Você só tem mais uma tentativa\n')
            
            login_plataforma = input('Digite seu login: ')
            senha_plataforma = input('Digite sua senha: ')

            if login_usuario == login_plataforma and senha_usuario == senha_plataforma:
                print('\nAcesso permitido com sucesso')
            else: 
                print('\nAcesso bloqueado. Entre em contato por meio dos canais da empresa.')