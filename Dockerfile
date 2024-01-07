FROM ubuntu
COPY pyproject.toml /app/
RUN pip3 install poetry
WORKDIR /app 
COPY HTTPS_CRUD.py /app/
CMD ["python3", "HTTPS_CRUD.py"]
