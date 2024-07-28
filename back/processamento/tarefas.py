from datetime import datetime, timedelta

class Tarefa:
    def __init__(self, descricao, data_expiracao, prioridade):
        self.descricao = descricao
        self.data_expiracao = data_expiracao
        self.prioridade = prioridade
        self.concluida = False
        self.data_conclusao = None

    def get_data_expiracao(self):
      return self.data_expiracao.strftime("%d/%m/%Y")

    def get_data_conclusao(self):
      return self.data_conclusao.strftime("%d/%m/%Y")

    def __str__(self):
      return f"Descrição: {self.descricao} - Data de Expiração: {self.get_data_expiracao()} - Prioridade: {self.prioridade}"

class TarefaDTO:
    def __init__(self, descricao, data_expiracao, prioridade, data_conclusao, concluida=0):
        self.descricao = descricao
        self.data_expiracao = data_expiracao
        self.prioridade = prioridade
        self.data_conclusao = data_conclusao
        self.concluida = concluida

class RegistrosTarefaDTO:
    def __init__(self, lista_tarefas_dto):
        self.colunas = list(vars(lista_tarefas_dto[0]).keys())
        self.registros = self.cria_registros(lista_tarefas_dto)

    def cria_registros(self, lista_tarefas):
        registros = []
        for tarefa in lista_tarefas:
            registro = {coluna: getattr(tarefa, coluna) for coluna in self.colunas}
            registros.append(registro)
        return registros

def add_days(date:datetime, days):
    new_date = date + timedelta(days=days)
    return new_date