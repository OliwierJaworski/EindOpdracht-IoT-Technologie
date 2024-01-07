FROM python:3.7
RUN apt-get update && apt-get install -y
WORKDIR /app 
COPY hello.py /app/
CMD ["python3", "hello.py"]
