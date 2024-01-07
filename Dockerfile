FROM arm32v7/ubuntu:20.04
RUN apt-get update && apt-get install -y
WORKDIR /app 
COPY pyproject.toml /app/
RUN apt install python3 -y
RUN apt-get install python-pip
RUN pip install poetry -y
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY hello.py /app/
CMD ["python3", "hello.py"]
