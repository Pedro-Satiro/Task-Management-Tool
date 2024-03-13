from .Data_base import team_base

class Member:
    def __init__(self, name, access_level, senha) :
        self.name = name
        self.access_level = access_level
        self._senha = senha
        self.tasks = []

    def add_team(self, team):
        self.team = team

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Nome: {self.name}\nNivel de acesso: {self.access_level}\n"
    
    def get_senha(self):
        return self._senha
    
    def alterar_senha(self, new_senha):
        self._senha = new_senha


class Gestor(Member):
    def __init__(self, name, access_level, senha, departamento):
        super().__init__(name, access_level, senha)
        self.departamento = departamento

    def add_task(self, task):
        self.tasks.append(task)
        self.tasks[-1].dono = self.name

