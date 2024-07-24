from PIL import Image
import os
import utilidades
from fastapi.encoders import jsonable_encoder

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

def analisa_imagem(nome_arquivo, path_arquivo):
    try: 
        if os.path.isfile(path_arquivo):
            my_image = Imagem(nome_arquivo, path_arquivo)
            altura, largura = my_image.dimensoes()
            altura = str(altura)
            largura = str(largura)
            tamanho = str(my_image.tamanho())
            formato = my_image.formato()
            formato = formato.lower()
            my_image_dto = utilidades.ImageDTO(nome=nome_arquivo, altura=altura, largura=largura, tamanho=tamanho, formato=formato)
        return jsonable_encoder(my_image_dto)
    except Exception as ex:
        raise ValueError(str(ex))

def processa_imagem(nome_arquivo, path_arquivo, path_results):
    json_image_anlysed = analisa_imagem(nome_arquivo, path_arquivo)
    utilidades.salva_json_em_arquivo(my_json=json_image_anlysed, nome_arquivo=nome_arquivo, path_json=path_results)