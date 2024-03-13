from .login import Login
from .Member import Member, Gestor
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
from .singleton_base import SingletonBase
from .Data_base import member_base

class Interface(metaclass=SingletonBase):

    def add_new_member(self):
        nome = simpledialog.askstring("Add new member", "Digite o nome:")
        senha = simpledialog.askstring("Add new member", "Digite a senha:")
        access_level = simpledialog.askinteger(
            "Add new member",
            "Digite o seu nivel de acesso:\n1 - para gestor da equipe\n0 - para membro:",
        )

        if access_level == 1:
            departamento = simpledialog.askstring(
                "Add new member", "Insira o seu departamento:"
            )
            new_member = Gestor(nome, access_level, senha, departamento)
            member_base.append(new_member)
        else:
            new_member = Member(nome, access_level, senha)
            member_base.append(new_member)

        messagebox.showinfo("Add new member", "Membro adicionado com sucesso!")

    def login(self):
        usuario = simpledialog.askstring("Login", "Digite seu usuario:")
        senha = simpledialog.askstring("Login", "Digite sua senha:")
        log_in = 0
        for member in member_base:
            if member.name == usuario and member.get_senha() == senha:
                login = Login()
                login.make_login(member)
                log_in = 1
                del login
                break
        if not log_in:
            messagebox.showerror("Login", "Login inválido")

    def exit_program(self, root):
        messagebox.showinfo("Exit", "Saindo do programa...")
        root.destroy()

    def run_interface(self):
        root = tk.Tk()

        frame = tk.Frame(root)
        frame.pack()

        button = tk.Button(
            frame,
            text="Add new member",
            fg="red",
            command=self.add_new_member,
            font=("Arial", 12),
            padx=10,
            pady=5,
        )
        button.pack(side=tk.LEFT)

        button = tk.Button(
            frame,
            text="Login",
            fg="green",
            command=self.login,
            font=("Arial", 12),
            padx=10,
            pady=5,
        )
        button.pack(side=tk.LEFT)

        button = tk.Button(
            frame,
            text="Exit",
            fg="blue",
            command=lambda: self.exit_program(root),
            font=("Arial", 12),
            padx=10,
            pady=5,
        )
        button.pack(side=tk.LEFT)

        root.mainloop()
