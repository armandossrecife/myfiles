# My Files

Breve descrição de como os aplicativos backend e frontend trabalham juntos para analisar imagens, áudio e vídeos:

**Aplicativo Backend (FastAPI):**

* **Objetivo:** Gerencia uploads de arquivos, processamento e armazenamento de dados.
* **Processamento:**
    1. **Upload de arquivo:** Recebe arquivos enviados do frontend por meio de solicitações de API.
    2. **Validação de arquivo:** Verifica se o arquivo enviado é de um tipo suportado (por exemplo, JPG, PNG, MP3, MP4) e se o tamanho do arquivo está dentro dos limites.
    3. **Processamento de arquivo:** Com base no tipo de arquivo, chama a função de processamento apropriada (por exemplo, `images.processa_imagem` para imagens, `videos.processa_video` para vídeos, `audios.processa_audio` para áudio).
        * Essas funções extraem dados básicos dos arquivos usando bibliotecas como Pillow (imagens), moviepy (vídeos) e mutagen (áudio).
    4. **Armazenamento de dados:** Salva os dados extraídos (por exemplo, dimensões para imagens, duração para áudio/vídeo) no diretório `utilidades.RESULTS_DIRECTORY`.
    5. **Resposta:** Envia uma resposta JSON ao frontend indicando o sucesso ou falha da operação e, se bem-sucedida, os dados extraídos.

**Aplicativo Frontend (Flask):**

* **Objetivo:** Fornece uma interface de usuário para upload de arquivos, visualização de listas de arquivos e resultados de análise e download de arquivos.
* **Processamento:**
    1. **Interface do usuário:** Apresenta páginas HTML (usando templates Jinja2) para:
        * Upload de arquivos (formulário com campo de entrada de arquivo).
        * Listagem de arquivos enviados.
        * Listagem de resultados da análise.
        * Visualização de imagens, vídeos ou áudio baixados.
        * Visualização dos resultados da análise em formato JSON.
    2. **Interação do usuário:** Gerencia ações do usuário como:
        * Enviar o formulário de upload para enviar o arquivo para o backend.
        * Clicar em nomes de arquivo para baixar arquivos ou visualizar resultados.
    3. **Comunicação com API:** Usa a biblioteca `requests` para fazer chamadas de API ao backend para:
        * Upload de arquivos (POST para `/upload`).
        * Recuperar listas de arquivos (GET para `/files`).
        * Recuperar resultados de análise (GET para `/analysis`).
        * Download de arquivos (GET para `/download/{filename}`).
        * Recuperar resultados de análise para um arquivo (GET para `/results/{filename}`).
    4. **Exibição de dados:** Atualiza dinamicamente as páginas HTML com base nas respostas recebidas da API do backend, mostrando listas de arquivos, resultados de análise ou arquivos baixados.

**Fluxo geral de trabalho:**

1. O usuário carrega um arquivo através da interface do frontend.
2. O frontend envia o arquivo para o backend por meio de uma solicitação de API.
3. O backend valida, processa e armazena os dados do arquivo.
4. O backend envia uma resposta com os dados extraídos ou uma mensagem de erro.
5. O frontend atualiza a interface do usuário com base na resposta do backend:
    * Se for bem-sucedido, exibe uma mensagem e atualiza as listas de arquivos ou visualizações de resultados.
    * Se ocorrer um erro, exibe uma mensagem de erro.

Essa colaboração entre o backend e o frontend permite um aplicativo web amigável que permite aos usuários enviar vários arquivos de mídia, extrair dados básicos deles e visualizar os resultados.
