from .Data_base import team_base

class Member:
    def __init__(self, name, access_level, senha) :
        self.name = name
        self.access_level = access_level
        self.senha = senha
        self.tasks = []

    def add_team(self, team):
        self.team = team

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Nome: {self.name}\nNivel de acesso: {self.access_level}\n"

