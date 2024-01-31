from .Team import Team
from .login import make_login
from .Member import Member, Gestor
from .Data_base import member_base, team_base

def interface():
    while True:
        print("\nEscolha uma das seguintes opçoes: ")
        print("1 - Criar usuario novo")
        print("2 - Login")
        print("3 - Finalizar")

        choice = input("Digite sua escolha: ")
        if choice == "1":
            nome = input("Digite o nome: ")
            senha = input("Digite a senha: ")
            print("DIgite o seu nivel de acesso")
            access_level = int(input("1 - para gestor da equipe\n0 - para membro: "))
            
            if access_level == 1:
                departamento = input('Insira o seu departamento: ')
                new_member = Gestor(nome, access_level, senha, departamento)
                member_base.append(new_member)
            else:
                new_member = Member(nome,access_level,senha)
                member_base.append(new_member)
        elif choice == "2":
            usuario = input("Digite seu usuario: ")
            senha = input("Digite sua senha: ")
            log_in = 0
            for member in member_base:
                if member.name == usuario and member.get_senha() == senha:
                    make_login(member)
                    log_in = 1
                    break
            if not log_in:
                print("Login invalido")

        elif choice == "3":
            print("Saindo do programa...")
            break
        else: 
            print("Escolha errada. Selecione entre 1, 2, or 3.")