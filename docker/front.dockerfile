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

RUN pip install --no-cache-dir -r /root/myfiles/front/requirements.txt

# Expose the port the frontend app will run on
EXPOSE 5000

# Vai para o diretorio /root/myfiles/back
WORKDIR /root/myfiles/front

# Command to run the frontend application
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--port=5000"]