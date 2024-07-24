import os
import uuid
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import uvicorn
import utilidades
from analyzer import images
from analyzer import videos
from analyzer import audios

app = FastAPI()

if not os.path.exists(utilidades.UPLOAD_DIRECTORY):
    os.makedirs(utilidades.UPLOAD_DIRECTORY)

if not os.path.exists(utilidades.RESULTS_DIRECTORY):
    os.makedirs(utilidades.RESULTS_DIRECTORY)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    extensao = utilidades.get_file_extension(file.filename)
    filename_uuid = str(uuid.uuid4())
    uploaded_file = filename_uuid + "." + extensao
    if utilidades.allowed_file(uploaded_file):
        file_location = f"{utilidades.UPLOAD_DIRECTORY}/{uploaded_file}"
        extensao = utilidades.get_file_extension(uploaded_file)
        file_type = utilidades.get_media_type(extensao)
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
        # Para imagem
        if file_type == "image/jpeg" or file_type == "image/jpg" or file_type=="image/png":
            images.processa_imagem(nome_arquivo=filename_uuid, path_arquivo=file_location, path_results=utilidades.RESULTS_DIRECTORY)
        # Para video
        if file_type == "video/mp4":
            videos.processa_video(nome_arquivo=filename_uuid, path_arquivo=file_location, path_results=utilidades.RESULTS_DIRECTORY)
        # Para audio
        if file_type == "audio/mp3":
            audios.processa_audio(nome_arquivo=filename_uuid, path_arquivo=file_location, path_results=utilidades.RESULTS_DIRECTORY)
    else:
        raise HTTPException(status_code=404, detail="Erro: Tipo de arquivo não permitido")
    return {"filename": file.filename}

@app.get("/files")
def list_files():
    files = os.listdir(utilidades.UPLOAD_DIRECTORY)
    return {"files": files}

@app.get("/analysis")
def list_alysis_results():
    files = os.listdir(utilidades.RESULTS_DIRECTORY)
    return {"files": files}

@app.get("/download/{file_name}")
def download_file(file_name: str):
    file_path = f"{utilidades.UPLOAD_DIRECTORY}/{file_name}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

@app.get("/results/{file_name}")
def results_file(file_name: str):
    file_path = f"{utilidades.RESULTS_DIRECTORY}/{file_name}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)