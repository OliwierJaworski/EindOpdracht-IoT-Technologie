FROM ubuntu
COPY pyproject.toml /app/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
WORKDIR /app 
COPY HTTPS_CRUD.py /app/
CMD ["python3", "HTTPS_CRUD.py"]
