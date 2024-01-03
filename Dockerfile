FROM arm32v7/python:3
COPY helloworld.py /app/
WORKDIR /app
CMD ["python", "helloworld.py"]
