# MyFrontend

Frontend exemplo de Protótipo de Aplicação Web (Prova de Conceito) de upload de arquivos

[Quadro de Atividades do Projeto Frontend](TBD)

# A. Ambiente de Desenvolvimento

Existe uma estrutura base que vamos seguir para a construção de nossas aplicações em [Flask](https://flask.palletsprojects.com): 

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

## 3. É preciso configurar as variáveis de ambiente da aplicação

```bash
export MY_SECRET_KEY=?????????
export BACKEND_IP=?.?.?.?
export BACKEND_PORT=?
```

## 4. Para executar a aplicação principal

```bash
flask --app main run --host=0.0.0.0 --port=5000
```

ou 

```bash
.\exec.sh
```

Abra o browser: http://localhost:5000

## Flask frontend review

[Telas](https://github.com/armandossrecife/myfiles/blob/main/front/telas.md)

# B. Descrição da estrutura da aplicação 

Segue uma breve descrição dos diretórios e arquivos:

**front/static**: diretório que contem os arquivos e recursos estáticos da aplicação frontend.

**front/templates**: O diretório que contém os templates HTML usados para renderizar as páginas da aplicação frontend.

**front/main.py**: O ponto de entrada da aplicação Flask, onde você cria a instância do aplicativo frontend e registra os blueprints (routes).

**front/exec.sh**: Script para inicializar a aplicação frontend.

**front/README.md**: Um arquivo de documentação contendo informações sobre o projeto.

**front/requirements.txt**: Um arquivo que lista as dependências do projeto.

# C. Mais detalhes 

Principais componentes da aplicação principal (main.py)

**Componentes:**

* **Rotas:**
  * `/`: Página inicial da aplicação. Exibe o conteúdo do arquivo `index.html`.
  * `/upload`: Carrega um arquivo.
     * No método GET, exibe o formulário de upload de arquivo (`upload.html`).
     * No método POST, recebe o arquivo enviado pelo formulário, envia para o backend através de uma requisição POST para a URL `/upload` e exibe uma mensagem de sucesso ou erro.
  * `/arquivos`: Lista os arquivos carregados.
     * Envia uma requisição GET para a URL `/files` do backend e exibe a lista de arquivos obtida na resposta (utilizando o template `list_files.html`).
  * `/resultados`:  Lista os resultados das análises.
     * Envia uma requisição GET para a URL `/analysis` do backend e exibe a lista de resultados obtida na resposta (utilizando o template `list_results.html`).
  * `/download/<filename>`: Permite baixar um arquivo carregado.
     * Recebe o nome do arquivo (`filename`) como argumento da rota.
     * Constrói a URL de download completa para o arquivo no backend (`/download/<filename>`) e envia uma requisição GET para essa URL.
     * Exibe a visualização do arquivo baixado de acordo com seu tipo de mídia (imagem, vídeo ou áudio) utilizando templates específicos (`view_image.html`, `view_video.html`, `view_audio.html`).
  * `/resultados/<filename>`: Permite visualizar os resultados de um arquivo.
     * Recebe o nome do arquivo (`filename`) como argumento da rota.
     * Constrói a URL completa para recuperar os resultados do arquivo no backend (`/results/<filename>`) e envia uma requisição GET para essa URL.
     * Exibe os resultados recebidos no formato JSON utilizando o template `view_json.html`.

**Integração com o Backend:**

* O código utiliza a biblioteca `requests` para fazer requisições HTTP para o backend FastAPI.
* As URLs do backend são armazenadas em variáveis de ambiente (`BACKEND_IP` e `BACKEND_PORT`) ou definidas em uma URL base (`FASTAPI_URL`).
* O código constrói URLs completas para cada endpoint do backend FastAPI utilizado.

**Templates:**

* O código utiliza o Jinja2 para renderizar templates HTML dinamicamente.
* Os templates (`index.html`, `upload.html`, `list_files.html`, `list_results.html`, `view_image.html`, `view_video.html`, `view_audio.html`, `view_json.html`) exibem a interface do usuário para upload de arquivos, listagem de arquivos e resultados, visualização de arquivos baixados e visualização dos resultados da análise.
