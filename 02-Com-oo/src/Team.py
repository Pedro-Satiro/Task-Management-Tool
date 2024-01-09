from .Member import Member
from .Task import Task


class Team:
    def __init__(self, team_name, gestor):
        self.team_name = team_name
        self.gestor = gestor
        self.membros = []
    
    def list_members(self):
        print("")
        print(f"Membros da equipe {self.team_name}: ")
        for member in self.membros:
            print(member)

    def add_member(self, member):
        self.membros.append(member)



