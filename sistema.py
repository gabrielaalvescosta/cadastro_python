'''
Implementação em Python de um menu listando todas as funcionalidade do sistema. 
Observe que ao escolher uma opção, o programa deverá mostrar na tela a opção selecionada e exibir novamente o menu com todas as funcionalidades do sistema. 
Entregável: Arquivo py (Implementação em Python)

'''

# Texto de bem vindo
welcome_text = """
-------------------------- IBMatch --------------------------
Seja bem vindo(a)! Escolha uma das opções abaixo para iniciar:
(1) Cadastro de recrutador
(2) Cadastro de candidato
(3) Verificar cadastro
(4) Deletar cadastro
(5) Sair
"""

# Area de atuacao CANDIDATO
atuacao_can = """
Qual é a sua área de atuação? Digite o número correspondente a área:
(1) Tecnologia
(2) Humanas 
(3) Engenharia
(4) Economia e negócios
(5) Outra área
"""

# Area de atuacao RECRUITER
atuacao_rec = """
Qual é sua área de recrutamento? Digite o número correspondente a área:
(1) Tecnologia
(2) Humanas 
(3) Engenharia
(4) Economia e negócios
(5) Outra área
"""

# Tupla de recruiters e candidatos
recruiters = []
candidatos = []

# Funcao para pressionar qualquer tecla para confirmar
def confirma():
    input("Aperte ENTER para confirmar.")

# Funcao de cadastro do recrutador
def cad_recruiter():
    print(str("Bem-vindo, recrutador!"))
    id_rec = int(input("Id: "))
    name_rec = str(input("Digite o seu nome completo: "))
    email_rec = str(input("Digite o seu email: "))
    print(str(atuacao_rec))
    area_rec = str(input("Qual a área: "))

    if name_rec is not None and email_rec is not None and area_rec is not None:
        print("\nSEUS DADOS: \n Id: " + str(id_rec) + "\nnNome: " + name_rec + "\nEmail: " + email_rec + "\nÁrea: " + str(area_rec))
        print(str("\nDigite: \n(1) Confirmar \n(2) Corrigir\n"))
        conf_corr = int(input("RESPONDA -> "))
        if conf_corr == 1:
            recruiters.append((id_rec, name_rec, email_rec, area_rec))
            print("Recrutador cadastrado com sucesso.")
            welcome_system()
        elif conf_corr == 2:
            print(str("Corrija o seu cadastro:"))
            cad_recruiter()
    else:
        print(str("Cadastro não realizado. Todas as opções são obrigatórias"))
        cad_recruiter()
    
# Funcao de cadastro do candidato
def cad_candidato():
    print(str("Bem-vindo, candidato!"))
    id_can = int(input("Id: "))
    name_can = str(input("Digite o seu nome completo: "))
    email_can = str(input("Digite o seu email: "))
    print(str(atuacao_can))
    area_can = int(input("Qual a sua área: "))
    
    if name_can is not None and email_can is not None and area_can is not None:
        print("\nSEUS DADOS: \n Id: " + str(id_can) + "\nnNome: " + name_can + "\nEmail: " + email_can + "\nÁrea: " + str(area_can))
        print(str("\nDigite: \n(1) Confirmar \n(2) Corrigir\n"))
        conf_corr = int(input("RESPONDA -> "))
        if conf_corr == 1:
            recruiters.append((id_can, name_can, email_can, area_can))
            print("Usuário cadastrado com sucesso.")
            welcome_system()
        elif conf_corr == 2:
            print(str("Corrija o seu cadastro:"))
            cad_candidato()
    else:
        print(str("Cadastro não realizado. Todas as opções são obrigatórias"))
        cad_candidato()


def lista_cadastro():
    listar = int(input("Voce é \n(1) Recrutador \n(2) Candidato"))
    if listar == 1:
        print("CADASTRO de Recrutadores")
    else:
        print("CADASTRO de Usuários")


# Enquanto o usuário nao escolher a opcao 5, ele nao saira do sistema
def choose_number():
    option = int(input("Digite o número: "))
    if option == 1:
        cad_recruiter()
    elif option == 2:
        cad_candidato()
    elif option == 3:
        lista_cadastro()


# Mostra as opcoes na tela e chama funcao de escolher o numero
def welcome_system():
    print(str(welcome_text))
    choose_number()
    


welcome_system()