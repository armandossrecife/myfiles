import os
import uuid
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import uvicorn
import utilidades
from analyzer import images
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import json

app = FastAPI()

UPLOAD_DIRECTORY = "uploads"
RESULTS_DIRECTORY = "results"

class ImageDTO(BaseModel):
    nome: str
    altura: str
    largura: str
    tamanho: str
    formato: str

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

if not os.path.exists(RESULTS_DIRECTORY):
    os.makedirs(RESULTS_DIRECTORY)

def analisa_imagem(nome_arquivo, path_arquivo):
    try: 
        if os.path.isfile(path_arquivo):
            my_image = images.Imagem(nome_arquivo, path_arquivo)
            altura, largura = my_image.dimensoes()
            altura = str(altura)
            largura = str(largura)
            tamanho = str(my_image.tamanho())
            formato = my_image.formato()
            formato = formato.lower()
            my_image_dto = ImageDTO(nome=nome_arquivo, altura=altura, largura=largura, tamanho=tamanho, formato=formato)
        return jsonable_encoder(my_image_dto)
    except Exception as ex:
        raise ValueError(str(ex))

def salva_json_em_arquivo(my_json, nome_arquivo, path_json):
    try:
        filename = f"{nome_arquivo}.json"
        file = f"{path_json}/{filename}"
        with open(file, 'w') as f:
            json.dump(my_json, f)
    except Exception as ex:
        raise ValueError(str(ex))

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    extensao = utilidades.get_file_extension(file.filename)
    filename_uuid = str(uuid.uuid4())
    uploaded_file = filename_uuid + "." + extensao
    file_location = f"{UPLOAD_DIRECTORY}/{uploaded_file}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())
    json_image_anlysed = analisa_imagem(nome_arquivo=filename_uuid, path_arquivo=file_location)
    salva_json_em_arquivo(my_json=json_image_anlysed, nome_arquivo=filename_uuid, path_json=RESULTS_DIRECTORY)
    return {"filename": file.filename}

@app.get("/files")
def list_files():
    files = os.listdir(UPLOAD_DIRECTORY)
    return {"files": files}

@app.get("/analysis")
def list_alysis_results():
    files = os.listdir(RESULTS_DIRECTORY)
    return {"files": files}

@app.get("/download/{file_name}")
def download_file(file_name: str):
    file_path = f"{UPLOAD_DIRECTORY}/{file_name}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

@app.get("/results/{file_name}")
def results_file(file_name: str):
    file_path = f"{RESULTS_DIRECTORY}/{file_name}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)