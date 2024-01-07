FROM arm32v7/python:3.7-slim-buster
WORKDIR /app 
COPY pyproject.toml /app/ #copy poetry related file to the app dir
RUN pip3 install poetry
RUN poetry config virtualenvs.create false #makes it not run in a virtual env
COPY HTTPS_CRUD.py /app/  #copy python script to app dir
CMD ["python3", "HTTPS_CRUD.py"]
