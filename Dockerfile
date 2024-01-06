FROM ubuntu
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y python3 python3-pip
RUN pip3 install poetry
WORKDIR /app
COPY main.c /app/
ADD ./main.c .(/usr/bin)
RUN gcc -o main.exe main.c
COPY py_app/ .
RUN poetry install
CMD ["./main.exe", "python3", "app.py"]
