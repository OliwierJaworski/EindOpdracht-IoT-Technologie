FROM arm32v7/ubuntu:20.04
RUN apt-get update && apt-get install -y
WORKDIR /app 
COPY pyproject.toml /app/
RUN apt-get install python3-pip -y
RUN pip3 install requests
COPY HTTPS_CRUD.py /app/
CMD ["python3", "HTTPS_CRUD.py"]
