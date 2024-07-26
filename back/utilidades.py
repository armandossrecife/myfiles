import json
import os

UPLOAD_DIRECTORY = "uploads"

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

def cria_pasta(path_folder):
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)