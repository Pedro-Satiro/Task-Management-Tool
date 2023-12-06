class Task:
    def __init__(self, title, description, dono, status = "Pendente", ) :
        self.title = title
        self.description = description
        self.status = status
        self.dono = dono 
        self.access_level = dono.access_level

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Title: {self.title} \nDescription: {self.description} \nStatus: {self.status}\n"
     

class Member:
    def __init__(self, name, access_level) :
        self.name = name
        self.access_level = access_level

    def __str__(self):
        return f"Name: {self.name}\nAccess level: {self.access_level}\n"


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.members = []

    def add_member(self, name, access_level):    
        member = Member(name, access_level)
        self.members.append(member)

    def make_team(self, new_team_name, qnt_members):
        print(f"Now some information from the team members {new_team_name}: \n")
        for i in range (qnt_members):
            name = input(f"Enter member name {i+1}: ")
            print("The access levels are: 3 Full access; 2 Access only the tasks under you and your own tasks; 1 Only your tasks")
            access_level = input(f"Enter the access level of member {i+1}: ")
            self.add_member(name, access_level)
    
    def list_members(self):
        print(f"Member of the team {self.team_name}: ")
        for member in self.members:
            print(member)


def make_task ():
    new_titulo = input("Enter the task name: ")
    new_descricao = input("Enter tesk description: ")
    
    new_task = Task(new_titulo, new_descricao)
    return new_task

def new_team ():
    new_team_name = input("Enter team name: ")
    qnt_members = int(input("Enter the number of members: "))
    
    team = Team(new_team_name)
    team.make_team(new_team_name, qnt_members)
    team.list_members()

def main():
    while True:
        print("\nChoose one of the options: ")
        print("1 - Create a new team")
        print("2 - Create a new task")
        print("3 - Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            new_team()

        elif choice == "2":
            make_task()

        elif choice == "3":
            print("Exiting the program...")
            break
        else: 
            print("Invalid choice. Please enter 1, 2, or 3.")



main()