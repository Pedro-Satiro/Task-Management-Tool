from tkinter import messagebox

class Team:
    def __init__(self, team_name, gestor):
        self.team_name = team_name
        self.gestor = gestor
        self.membros = []
    
    def list_members(self):
        report_text = f"Membros da equipe {self.team_name}: \n" + "\n".join([member.name for member in self.membros])
        messagebox.showinfo("Team Report", report_text)

    def add_member(self, member):
        self.membros.append(member)
