import json
import datetime

from .Member import Member
from .Team import Team
from .Data_base import team_base, member_base
from .Task import Task

def atualizar():
    for member in member_base:
        for task in member.tasks:
            data_atual = datetime.date.today()
            dia_seguinte = datetime.datetime.now() + datetime.timedelta (1)
            if task.prazo < data_atual:
                task.status = "Atrasado"
                print(f"A tarefa {task.title} do usuario {member.name} esta Atrasada")
            if task.prazo == dia_seguinte:
                print(f"A tarefa {task.title} do usuario {member.name} tem o limite ate amanha")


def busca_membro():
    membro_valido = 0
    while not membro_valido:
        membro = input("Digite o nome do usuário ou -1 para retornar: ")
        if membro == '-1':
            break
        for i in member_base:
            if membro == i.name:
                membro = i
                membro_valido = 1
                break
        if not membro_valido:
            print("Usuário não existe")

    return membro, membro_valido
    
def make_login(member: Member):
    while True:
        #try:
            print("\nEscolha uma das opçoes: ")
            print("0 - Voltar")
            print("9 - alterar senha")
            print("1 - Criar tarefas")
            print("2 - Consultar tarefas")
            print("3 - Alterar tarefas")
            if member.access_level == 1:
                print("4 - Criar um novo time")
                print("5 - Adicionar Membro a um time")
                print("6 - Gerar relatorio da equipe")
                print("7 - vizualizar membros da equipe")
            opcao = int(input())

            atualizar()

            if opcao == 0:
                return
            
            elif opcao == 9:
                senha = input('Digite a nova senha: ')
                member.alterar_senha(senha)

            elif  opcao == 1:
                title = input("Digite o nome da tarefa: ")
                description = input("Digite a descrição da tarefa: ")

                for idx, user in enumerate(member_base):
                    print(f'#{idx} nome: {user.name}\n')
                
                membro, membro_valido = busca_membro()

                dono = membro
                if not membro_valido:
                    print("Usuário não informado")
                    continue
                print("Modelo de data - 25/12/2020 ")
                prazo = input("Digite o prazo da tarefa: ")
                print("Baixo\nMedio\nUrgente")
                prioridade = input("Digite a prioridade da tarefa: ")
                
                new_task = Task(title, description, dono, prazo, prioridade )

                dono.add_task(new_task)
                
            elif opcao == 2:
                membro, membro_valido = busca_membro()
                if not membro_valido:
                    print("Usuário não informado")
                    continue
                usuario = membro
                for i in usuario.tasks:
                    print(str(i))

            elif opcao == 3:
                membro, membro_valido = busca_membro()
                if not membro_valido:
                    print("Usuário não informado")
                    continue
                usuario = membro
                for idx, i in enumerate (usuario.tasks):
                    print(f"{idx} {str(i)}")
                opcao = int(input("Digite o numero tarefa que deseja alterar: "))
                selected_task = usuario.tasks[opcao]
                print("Selecione um dos estados possiveis: ")
                print("Em Andamento\nAtrasado\nConcluido")
                new_status = input("Digite o status da tarefa atual: ")

                comentario = input("Digite um comentario na tarefa para sua equipe: ")
                selected_task.update_task(new_status, comentario)
    
            elif opcao == 4 and member.access_level == 1:
                name_team = input("Digite o nome do time: ")
                gestor = member
                new_team = Team(name_team,gestor)
                team_base.append(new_team)

            elif opcao == 5 and member.access_level == 1:
                for idx, team in enumerate (team_base):
                    print(f"{idx} {team.team_name}")
                
                opcao = int(input("Digite o numero time: "))
                time = team_base[opcao]
                
                for idx, user in enumerate(member_base):
                    print(f'#{idx} nome: {user.name}\n')

                membro, membro_valido = busca_membro()
                if not membro_valido:
                    print("Usuário não informado")
                    continue
                
                time.add_member(membro)
                membro.add_team(time)

            elif opcao == 6 and member.access_level == 1:
                for idx, team in enumerate (team_base):
                    print(f"{idx} {team.team_name}")
                opcao = int(input("Digite o numero time: "))
                time = team_base[opcao]

                relatorio = {}
                relatorio["total"] = 0
                relatorio["total_andamento"] = 0
                relatorio["total_atrasadas"] = 0
                relatorio["total_concluidas"] = 0

                for membro in time.membros:
                    relatorio["total"] += len(membro.tasks)
                    for i in membro.tasks:
                        if i.status.lower() == "Em Andamento".lower():
                            relatorio["total_andamento"] += 1
                        if i.status.lower() == "Atrasado".lower():
                            relatorio["total_atrasadas"] += 1
                        if i.status.lower() == "Concluido".lower():
                            relatorio["total_concluidas"] += 1
                
                for key in list(relatorio.keys()):
                    print(f'{key}:{relatorio[key]}')

                with open("Relatorio de produtividade.json", 'w') as arquivo_json:
                    json.dump(relatorio, arquivo_json)

            elif opcao == 7 and member.access_level == 1:
                for idx, team in enumerate (team_base):
                    print(f"{idx} {team.team_name}")

                opcao = int(input("Digite o numero time: "))
                time = team_base[opcao]

                time.list_members()
                
            else:
                print("Opção invalida")
                
        #except:
         #   print("Informação digitada incorreta")