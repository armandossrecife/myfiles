import os
import uuid
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import uvicorn
import utilidades
import json

app = FastAPI()

utilidades.cria_pasta(path_folder=utilidades.UPLOAD_DIRECTORY)

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
    else:
        raise HTTPException(status_code=404, detail="Erro: Tipo de arquivo não permitido")
    return {"filename": file.filename}

@app.get("/files")
def list_files():
    files = os.listdir(utilidades.UPLOAD_DIRECTORY)
    return {"files": files}

@app.get("/download/{file_name}")
def download_file(file_name: str):
    file_path = f"{utilidades.UPLOAD_DIRECTORY}/{file_name}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

@app.get("/mytime")
def show_graph_time():
    data = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
        dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
        dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]
    json_data = json.dumps(data)
    return json_data

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)