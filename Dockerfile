FROM arm32v7/python:3.7-slim-buster
COPY helloworld.py /app/
WORKDIR /app
CMD ["python3", "helloworld.py"]
