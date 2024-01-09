import datetime

class Task:
    def __init__(self, title, description, dono, prazo, prioridade, status = "Em Andamento") :
        """
        31/10/2023
        """
        self.title = title
        self.description = description
        self.prioridade = prioridade
        self.status = status
        self.dono = dono 
        self.prazo = datetime.date(int(prazo[6:]), int(prazo[3:5]), int(prazo[0:2]))
        self.comentario = ""

    def update_task(self, new_status, comentario,):
        self.status = new_status
        self.comentario = comentario


    def __str__(self):
        return f"Titulo: {self.title} \nDescrição da tarefa: {self.description} \nStatus: {self.status}\nComentario da equipe: {self.comentario}\nPrioridade {self.prioridade}\nPrazo {str(self.prazo)}"
     
