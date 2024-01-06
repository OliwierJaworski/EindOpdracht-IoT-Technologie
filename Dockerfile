FROM arm32v7/python:3.7-slim-buster
COPY HTTPS_CRUD.py /app/
WORKDIR /app
CMD ["python3", "HTTPS_CRUD.py"]
