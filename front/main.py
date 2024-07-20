from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FASTAPI_URL = "http://localhost:8000"
url_servico_upload = f'{FASTAPI_URL}/upload'
url_servico_files = f'{FASTAPI_URL}/files'
url_servico_analises = f'{FASTAPI_URL}/analysis'
url_servico_resultados = f'{FASTAPI_URL}/results'
url_servico_download = f"{FASTAPI_URL}/download"
url_servico_result = f"{FASTAPI_URL}/results"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(f"file.filename: {file.filename}")
        print(f"file.content_type: {file.content_type}")
        files = {'file': (file.filename, file.read(), file.content_type)}
        response = requests.post(url_servico_upload, files=files)
        if response.status_code == 200:
            return 'File uploaded successfully'
        else:
            return 'Error uploading file'
    return render_template('upload.html')

@app.route('/arquivos')
def list_files():
    response = requests.get(url_servico_files)
    if response.status_code == 200:
        files = response.json()['files']
        return render_template('list_files.html', files=files)
    else:
        return 'Error listing files'

@app.route('/resultados')
def list_files_results():
    response = requests.get(url_servico_analises)
    if response.status_code == 200:
        files = response.json()['files']
        return render_template('list_results.html', files=files, servico=url_servico_resultados)
    else:
        return 'Error listing results of files'

@app.route('/download/<filename>')
def download_file(filename):
    url_servico_download_file = url_servico_download + '/'+ filename
    response = requests.get(url_servico_download_file, stream=True)
    if response.status_code == 200:
        return render_template('view_image.html', filename=filename, url_file=url_servico_download_file)
    else:
        return 'Error downloading file'

@app.route('/resultados/<filename>')
def results_file(filename):
    
    url_servico_result_file = url_servico_result  + '/' + filename
    response = requests.get(f'{url_servico_result_file}', stream=True)
    if response.status_code == 200:
        my_json = response.text
        return render_template('view_json.html', filename=filename, url_file=url_servico_result_file, json_data=my_json)
    else:
        return 'Error to show results of file'

if __name__ == '__main__':
    app.run(debug=True)