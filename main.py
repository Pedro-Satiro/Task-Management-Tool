def atualizar_tarefa():
    print("consultando")




def consulta():
    print("consultando")



def criar_equipe():
   equipe = {}

   equipe['nome' ] = input("Digite o nome da equipe: ")

   qnt_integrantes = int(input("Qual o tamanho da equipe: "))
   equipe['integrantes'] = []

   for i in range(qnt_integrantes):
      integrante = {}
      integrante['nome'] = input(f"Digite o nome do membro {i+1}: ")
      #print("Defina o nivel de acesso desse membro:\n1-acessa apenas sua atividade\n2-acessa todas atividades abaixo da sua\n3- acesso total")
      #integrante['acesso'] = input(f"Digite a acesso do membro {i+1}: ")
     
      equipe['integrantes'].append(integrante)  
      print()

   return equipe

    



def login():
    print("fazendo login")



def nova_tarefa():
    print ("qual o nome da tarefa?")
    '''
    tarefa = input("")
    print ("Qual o dia maximo da tarefa? formato modelo: 29112023")
    dia_maximo = input("")

    print("Quem é o dono da tarefa?")
    dono_tarefa = input("")
    '''





def verificacao_choices(opcao_choices):
    if opcao_choices == 3:
        exit() 
        #finalizar
    elif opcao_choices == 2:  
        #Atualizar tarefa
        atualizar_tarefa()
    elif opcao_choices == 1:
        #Criar nova tarefa
        nova_tarefa()
    elif opcao_choices == 0:
        #Consultar tarefas atuais
        consulta()



def verificacao_iniciar(opcao_iniciar):
    if opcao_iniciar == 2:
        exit() 
        #finalizar
    elif opcao_iniciar == 1:
        login()
    elif opcao_iniciar == 0:  
        criar_equipe()
        






def interface_choices():
    while True:
        print("\nSelecione uma das opções a seguir:\n")
        print("[0] Consultar tarefas atuais")
        print("[1] Criar nova tarefa")
        print("[2] Atualizar tarefa")
        print("[3] Finalizar\n")

        opcao_choices = int(input(""))
        if opcao_choices <0 or opcao_choices >= 4 :
            print("Selecione um valor valido")
            print("=========================================")            
        else:
             break
        
    verificacao_choices(opcao_choices)



def interface_iniciar():
    while True:
        print("\nBem-vindo ao Gerenciador de tarefas do IC")
        print("Selecione uma das opções a seguir:\n")
        print("[0] Criar uma equipe")
        print("[1] Realizar o login")
        print("[2] Finalizar\n")

        opcao_iniciar = int(input(""))

        if opcao_iniciar < 0 or opcao_iniciar >= 3:
                print("Selecione um valor válido.")
                print("=========================================")
        else:
            break

    verificacao_iniciar(opcao_iniciar)
    #interface_choices()


def main():
    interface_iniciar()

main()