FROM arm32v7/ubuntu:20.04
RUN apt-get update && apt-get install -y
WORKDIR /app 
COPY hello.py /app/
CMD ["python3", "hello.py"]
