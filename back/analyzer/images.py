from PIL import Image
import os

class Imagem: 
    def __init__(self, nome_arquivo, path_arquivo):
        self.minha_imagem = None
        self.nome_arquivo = nome_arquivo
        self.path_referencia = path_arquivo
        try:
            self.minha_imagem = Image.open(path_arquivo)
        except Exception as ex:
            mensagem_erro = f'Erro ao criar a imagem com o arquivo {nome_arquivo} na referência {path_arquivo}: {str(ex)}'
            raise ValueError(mensagem_erro)

    def dimensoes(self):
        return self.minha_imagem.size

    def tamanho(self):
        return os.path.getsize(self.path_referencia)

    def formato(self):
        return self.minha_imagem.format

    def conteudo(self):
        return self.minha_imagem

    def __str__(self):
        return f'Nome: {self.nome_arquivo}, Dimensoes:{self.dimensoes()}, Formato: {self.formato()}, Tamanho: {self.tamanho()}'