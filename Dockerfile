FROM arm32v7/ubuntu:20.04
RUN apt-get update && apt-get install -y
WORKDIR /app 
COPY pyproject.toml /app/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY hello.py /app/
CMD ["python3", "hello.py"]
