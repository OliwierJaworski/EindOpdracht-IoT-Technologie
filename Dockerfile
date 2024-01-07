FROM arm32v7/ubuntu:20.04
RUN apt-get update && apt-get install -y
RUN apt-get install curl -y
WORKDIR /app 
COPY pyproject.toml /app/
COPY pyproject.toml /app/
RUN apt-get install python3-pip -y
RUN apt-get install -y ca-certificates
RUN curl -sSL https://install.python-poetry.org | python3.8 -
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY HTTPS_CRUD.py /app/
CMD ["python3", "HTTPS_CRUD.py"]
