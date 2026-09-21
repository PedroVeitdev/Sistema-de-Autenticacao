# Sistema de Autenticação

Um sistema interativo desenvolvido em **Python** para simular um fluxo de cadastro de usuários e controle de acesso com regras de segurança, validação de caracteres, limpeza de tela e limite de tentativas.

# Objetivo
Desenvolvi este projeto para aplicar conceitos fundamentais de lógica de programação utilizando estruturas condicionais (if, elif, else), funções nativas de manipulação de texto e variáveis de controle (flags). A aplicação conta com dois fluxos principais:
- **Validação de Cadastro com Segunda Chance:** Exige requisitos mínimos de segurança (verificados com len()) e oferece uma segunda oportunidade de correção antes de cancelar a operação.
- **Autenticação e Controle de Acesso:** Simula o login na plataforma, limpa os dados anteriores da tela (com a biblioteca os) para manter a privacidade visual e concede até 3 tentativas antes do bloqueio definitivo da conta.

# Funcionalidades e Validações
- **Tamanho Mínimo (len()):** O login e a senha devem possuir no mínimo 5 caracteres cada, validação feita calculando o comprimento das strings via len(login_usuario) e len(senha_usuario).
- **Regra de Diferenciação:** O login e a senha não podem ser iguais.
- **Lógica de Segunda Chance:** Se o usuário errar alguma regra no cadastro, o sistema concede mais 1 tentativa para corrigir os dados.
- **Privacidade Visual (import os):** Uso do comando nativo os.system('cls') (Windows) para limpar o histórico do terminal logo após o cadastro, ocultando os dados digitados.
- **Controle de Tentativas no Login:** Permite até 3 tentativas incorretas na tela de entrada antes de bloquear o acesso.

# Tecnologias e Recursos Utilizados
- **Linguagem:** Python 3.14.7
- **Módulo Nativo os:** Utilizado para executar comandos do sistema operacional e limpar a tela do terminal (os.system('cls')).
- **Função Nativa len():** Utilizada para contagem de caracteres e validação do tamanho mínimo das entradas.
- **Editor:** Visual Studio Code (VS Code)

# Evoluções Futuras
Desenvolvi este código aplicando o que aprendi até o momento sobre lógica e estruturas de decisão. Conforme eu for avançando nos meus estudos de Python, pretendo retornar a este projeto para melhorar a sua estrutura. Algumas ideias futuras são:
- **Melhorar o fluxo de tentativas:** Descobrir formas mais eficientes de permitir que o usuário tente se cadastrar novamente sem precisar repetir blocos no código.
- **Deixar a leitura do código mais limpa:** Aprender a organizar melhor o programa para evitar repetição de instruções.
- **Tornar as mensagens mais específicas:** Informar ao usuário exatamente qual regra ele errou na segunda tentativa.
- **Explorar novos recursos do Python:** Pesquisar outras ferramentas e bibliotecas nativas que ajudem a tornar a entrada de dados ainda mais segura.
