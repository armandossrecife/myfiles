# Use a lightweight Python base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /root

# install git, pip, vim
RUN apt-get update && apt-get install -y git python3-pip vim

# Faz o clone de repositorio mycluster
RUN git clone https://github.com/armandossrecife/myfiles.git

# Vai para o diretorio /root/myfiles
WORKDIR /root/myfiles

RUN pip install --no-cache-dir -r /root/myfiles/back/requirements.txt

# Expose the port the backend app will run on
EXPOSE 8000

# Vai para o diretorio /root/myfiles/back
WORKDIR /root/myfiles/back

# Command to run the backend application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]