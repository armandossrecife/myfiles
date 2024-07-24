from pydantic import BaseModel
import json

class ImageDTO(BaseModel):
    nome: str
    altura: str
    largura: str
    tamanho: str
    formato: str

class VideoDTO(BaseModel):
    nome: str
    altura: str
    largura: str
    tamanho: str
    duracao: str
    frame_rate: str
    formato: str

class AudioDTO(BaseModel):
    nome: str
    tamanho: str
    duracao: str
    sample_rate: str
    canais: str
    formato: str

UPLOAD_DIRECTORY = "uploads"
RESULTS_DIRECTORY = "results"
ALLOWED_EXTENSIONS = {'jpeg','jpg', 'png', 'mp4', 'mp3'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()            

def get_media_type(extension):
  media_types = {
      "jpeg": "image/jpeg",
      "jpg": "image/jpeg",
      "png": "image/png",
      "mp4": "video/mp4",
      "mp3": "audio/mp3"
  }
  return media_types.get(extension.lower())

def salva_json_em_arquivo(my_json, nome_arquivo, path_json):
    try:
        filename = f"{nome_arquivo}.json"
        file = f"{path_json}/{filename}"
        with open(file, 'w') as f:
            json.dump(my_json, f)
    except Exception as ex:
        raise ValueError(str(ex))