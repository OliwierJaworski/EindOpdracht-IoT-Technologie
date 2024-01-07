FROM arm32v7/python:3.7-slim-buster
WORKDIR /app 
COPY pyproject.toml /app 
COPY HTTPS_CRUD.py app/  
RUN pip3 install poetry
RUN poetry config virtualenvs.create false 
CMD ["python3", "HTTPS_CRUD.py"]
