FROM arm32v7/ubuntu
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y python3 python3-pip
RUN pip install requests
WORKDIR /app 
COPY HTTPS_CRUD.py /app/
CMD ["python3", "HTTPS_CRUD.py"]
