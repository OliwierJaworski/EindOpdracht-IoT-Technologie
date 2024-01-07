FROM arm32v7/python:3.7-slim-buster
WORKDIR /app 
COPY HTTPS_CRUD.py app/
CMD ["python3", "HTTPS_CRUD.py"]
