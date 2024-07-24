import os
import utilidades
from fastapi.encoders import jsonable_encoder
import subprocess
import json

def extract_video_info(video_path):
  try:
    if os.path.isfile(video_path):
        # Use ffmpeg command-line tool for probing
        command = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", video_path]
        output = subprocess.check_output(command).decode()
        probe = json.loads(output)

        # Extract information (adjust based on your needs)
        video_stream = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
        info = {
        "filename": os.path.basename(video_path),
        "size": os.path.getsize(video_path),
        "format": probe['format']['format_name'],
        "duration": video_stream['duration'],  # In seconds (float)
        "width": video_stream['width'],
        "height": video_stream['height'],
        "frame_rate": video_stream['avg_frame_rate'],  # Format: fps (string)
        }
  except subprocess.CalledProcessError as e:
    raise ValueError(f"Error processing video: {video_path} - {e}")
  return info

def processa_video(nome_arquivo, path_arquivo, path_results):
    video_info = extract_video_info(path_arquivo)
    
    altura=str(video_info['height'])
    largura=str(video_info['width'])
    tamanho=str(video_info['size'])
    duracao=str(video_info['duration']) 
    frame_rate=str(video_info['frame_rate'])
    formato=str(video_info['format'])

    my_video_dto = utilidades.VideoDTO(nome=nome_arquivo, altura=altura, largura=largura, 
        tamanho=tamanho, duracao=duracao, frame_rate=frame_rate, formato=formato)
        
    json_video_anlysed = jsonable_encoder(my_video_dto)
    utilidades.salva_json_em_arquivo(my_json=json_video_anlysed, nome_arquivo=nome_arquivo, path_json=path_results)