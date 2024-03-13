import json
from .Team import Team
from .Data_base import team_base, member_base
from .Task import Task
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
from .singleton_base import SingletonBase

class Login(metaclass=SingletonBase):

    @staticmethod
    def busca_membro():
        membro_valido = 0
        while not membro_valido:
            membro = simpledialog.askstring(
                "Make Login", "Enter the member name or -1 to return:"
            )
            if membro == "-1":
                break
            for i in member_base:
                if membro == i.name:
                    membro = i
                    membro_valido = 1
                    break
            if not membro_valido:
                messagebox.showerror("Invalid User", "Usuário não existe")

        return membro, membro_valido

    @staticmethod
    def create_task():
        title = simpledialog.askstring("Create Task", "Enter the task title:")
        description = simpledialog.askstring(
            "Create Task", "Enter the task description:"
        )

        members_info = ""
        for idx, user in enumerate(member_base):
            members_info += f"#{idx} nome: {user.name}\n"
        messagebox.showinfo("Members Info", members_info)

        membro, membro_valido = Login.busca_membro()

        dono = membro
        if not membro_valido:
            messagebox.showerror("Invalid User", "Usuário não informado")
            return
        prazo = simpledialog.askstring(
            "Create Task", "Digite o prazo da tarefa:\nModelo de data - 25/12/2020"
        )
        prioridade = simpledialog.askstring(
            "Create Task", "Digite a prioridade da tarefa:\nBaixo\nMedio\nUrgente"
        )

        new_task = Task(title, description, dono, prazo, prioridade)

        dono.add_task(new_task)

    @staticmethod
    def view_tasks():
        membro, membro_valido = Login.busca_membro()
        if not membro_valido:
            messagebox.showerror("Invalid User", "Usuário não informado")
            return
        usuario = membro
        tasks = [str(i) for i in usuario.tasks]
        task_options = "\n".join(tasks)
        messagebox.showinfo("User Tasks", task_options)

    @staticmethod
    def update_task():
        membro, membro_valido = Login.busca_membro()
        if not membro_valido:
            messagebox.showerror("Invalid User", "Usuário não informado")
            return
        usuario = membro
        tasks = [str(i) for i in usuario.tasks]
        task_options = "\n".join(tasks)
        selected_task_index = simpledialog.askinteger(
            "Update Task", f"Choose the task number:\n{task_options}"
        )
        if selected_task_index is None:
            return
        selected_task = usuario.tasks[selected_task_index]
        status_options = "Em Andamento, Atrasado, Concluido"
        new_status = simpledialog.askstring(
            "Update Task",
            "Choose the new status:" + status_options,
            initialvalue=selected_task.status
        )
        if new_status is None:
            return
        comentario = simpledialog.askstring(
            "Update Task", "Enter a comment for the task:"
        )
        if comentario is None:
            return
        selected_task.update_task(new_status, comentario)

    def create_team(self):
        name_team = simpledialog.askstring("Create Team", "Enter the name of the team:")
        gestor = self.member
        new_team = Team(name_team, gestor)
        team_base.append(new_team)

    @staticmethod
    def add_member_to_team():
        team_options = [team.team_name for team in team_base]
        selected_team = simpledialog.askstring(
            "Add Member to Team", "Select the team: \n" + "\n".join(team_options) + "\n"
        )
        if selected_team is None:
            return
        time = team_base[team_options.index(selected_team)]

        member_options = [user.name for user in member_base]
        selected_member = simpledialog.askstring(
            "Add Member to Team",
            "Select the member: \n" + "\n".join(member_options) + "\n",
        )
        if selected_member is None:
            return
        membro = member_base[member_options.index(selected_member)]

        time.add_member(membro)
        membro.add_team(time)

    @staticmethod
    def generate_team_report():
        team_options = [team.team_name for team in team_base]
        selected_team = simpledialog.askstring(
            "Generate Team Report", "Select the team: \n" + "\n".join(team_options) + "\n",
        )
        if selected_team is None:
            return
        time = team_base[team_options.index(selected_team)]

        relatorio = {}
        relatorio["total"] = 0
        relatorio["total_andamento"] = 0
        relatorio["total_atrasadas"] = 0
        relatorio["total_concluidas"] = 0

        for membro in time.membros:
            relatorio["total"] += len(membro.tasks)
            for i in membro.tasks:
                if i.status.lower() == "em andamento":
                    relatorio["total_andamento"] += 1
                if i.status.lower() == "atrasado":
                    relatorio["total_atrasadas"] += 1
                if i.status.lower() == "concluido":
                    relatorio["total_concluidas"] += 1

        report_text = ""
        for key in list(relatorio.keys()):
            report_text += f"{key}: {relatorio[key]}\n"

        messagebox.showinfo("Team Report", report_text)

        with open("Relatorio de produtividade.json", "w") as arquivo_json:
            json.dump(relatorio, arquivo_json)

    @staticmethod
    def view_team_members():
        team_options = [team.team_name for team in team_base]
        selected_team = simpledialog.askstring(
            "View Team Members", "Select the team: \n" + "\n".join(team_options) + "\n",
        )
        if selected_team is None:
            return
        time = team_base[team_options.index(selected_team)]

        time.list_members()

    def update_password(self):
        senha = simpledialog.askstring("Update Password", "Enter the new password:")
        self.member.alterar_senha(senha)

    def on_button_click(self, option):
        if option == 0:
            self.root.destroy()
        elif option == 1:
            Login.create_task()
        elif option == 2:
            Login.view_tasks()
        elif option == 3:
            Login.update_task()
        elif option == 4 and self.member.access_level == 1:
            self.create_team()
        elif option == 5 and self.member.access_level == 1:
            Login.add_member_to_team()
        elif option == 6 and self.member.access_level == 1:
            Login.generate_team_report()
        elif option == 7 and self.member.access_level == 1:
            Login.view_team_members()
        elif option == 8:
            self.update_password()
        else:
            messagebox.showerror("Invalid Option", "Please choose a valid option.")
    
    def make_login(self, member):
        self.root = tk.Tk()
        self.member = member
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ("Back", 0),
            ("Create Task", 1),
            ("View Tasks", 2),
            ("Update Task", 3),
            ("Create Team", 4),
            ("Add Member to Team", 5),
            ("Generate Team Report", 6),
            ("View Team Members", 7),
            ("Update Password", 8)
        ]

        for text, option in buttons:
            button = tk.Button(button_frame, text=text, command=lambda option=option: self.on_button_click(option))
            button.pack(pady=5, padx=10, fill=tk.X)

        self.root.mainloop()
