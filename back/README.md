# MyBackend

Backend exemplo de Protótipo de Aplicação Web (Prova de Conceito) de upload de arquivos

[Quadro de Atividades do Projeto Backend](TBD)

# A. Ambiente de Desenvolvimento

Existe uma estrutura base que vamos seguir para a construção de nossas aplicações em [FastAPI](https://fastapi.tiangolo.com/): 

## 1. Virtual Environment

Vamos usar o esquema de [virtual environment](https://docs.python.org/3/library/venv.html)

```bash
python3 -m venv venv
```

Mais detalhes em [python venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

### 1.1 Para ativar o venv (Linux e MacOS)

```bash
source venv/bin/activate
```

### 1.2 Para desativar o venv 

```bash
deactivate
```

## 2. Uma vez criado e ativado o venv precisamos instalar os módulos, pacotes e bibliotecas usadas pela aplicação

```bash
pip3 install -r requirements.txt
```

## 3. Para executar a aplicação principal

```bash
uvicorn main:app --reload
```
ou 
```bash
./exec.sh
```

Abra o browser: http://localhost:8000/docs

## 4. Overview da aplicação

TBD

## 5. Execução dos testes automáticos

TBD

# B. Descrição da estrutura da aplicação

Segue uma breve descrição dos diretórios e arquivos:

**back/main.py**: O ponto de entrada da aplicação FastAPI, onde você cria a instância do aplicativo e registra as rotas da aplicação backend.

**back/exec.sh**: Script que inicia a aplicação backend.

**back/README.md**: Um arquivo de documentação contendo informações sobre a aplicação backend.

**back/requirements.txt**: Um arquivo que lista as dependências do projeto.

# C. Mais detalhes

Principais componentes da aplicação principal (main.py)

**Componentes:**

* **Envio e validação de arquivo:**
    * Usa `UploadFile` do FastAPI para upload de arquivos.
    * As funções `utilidades.get_file_extension` e `utilidades.allowed_file` lidam com a validação da extensão do arquivo.
    * Os uploads são salvos com um nome de arquivo exclusivo gerado usando `uuid.uuid4`.
* **Detecção de tipo de mídia:**
    * A função `utilidades.get_media_type` determina o tipo de mídia (imagem, vídeo, áudio) a partir da extensão.
* **Processamento de arquivo:**
    * Com base no tipo de mídia, chama a função de processamento apropriada do módulo `analyzer`. Essas funções lidam com a extração de dados básicos dos arquivos carregados.
        * `images.processa_imagem` para imagens.
        * `videos.processa_video` para vídeos.
        * `audios.processa_audio` para áudio.
* **Armazenamento de Dados:**
    * Os dados processados são salvos no `utilidades.RESULTS_DIRECTORY`.
* **Endereços adicionais:**
    * `/files` lista os arquivos carregados.
    * `/analysis` lista os resultados da análise (arquivos de dados processados).
    * `/download/{file_name}` permite baixar arquivos carregados.
    * `/results/{file_name}` permite baixar resultados da análise (arquivos de dados processados).
