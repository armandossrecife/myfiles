import os
import utilidades
from fastapi.encoders import jsonable_encoder
import subprocess
import json
import soundfile

def extract_audio_info(audio_path):
  try:
    # Use ffprobe for metadata extraction
    command = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", audio_path]
    output = subprocess.check_output(command).decode()
    probe_data = json.loads(output)

    # Extract data information using soundfile
    info = soundfile.info(audio_path)

    data_info = {
      "filename": os.path.basename(audio_path),
      "size": os.path.getsize(audio_path),
      "format": info.format,
      "length": probe_data['format']['duration'],  # In seconds (float) from ffprobe
      "channels": info.channels,
      "sample_rate": info.samplerate,
    }

    # Extract metadata (tags) from ffprobe data
    metadata = {stream.get('tags', {}).get(key) for stream in probe_data['streams'] for key in stream.get('tags', {}).keys()}

  except subprocess.CalledProcessError as e:
    raise ValueError(f"Error processing audio: {audio_path} - {e}")
  return info, data_info, metadata

def processa_audio(nome_arquivo, path_arquivo, path_results):
    audio_info, audio_data, audio_metada = extract_audio_info(path_arquivo)
    
    tamanho = str(audio_data['size'])
    duracao = str(audio_data['length']) 
    sample_rate = str(audio_data['sample_rate'])
    canais = str(audio_data['channels'])
    formato=str(audio_data['format'])

    my_audio_dto = utilidades.AudioDTO(nome=nome_arquivo, tamanho=tamanho, duracao=duracao, sample_rate=sample_rate, canais=canais, formato=formato)
    
    json_audio_anlysed = jsonable_encoder(my_audio_dto)
    utilidades.salva_json_em_arquivo(my_json=json_audio_anlysed, nome_arquivo=nome_arquivo, path_json=path_results)