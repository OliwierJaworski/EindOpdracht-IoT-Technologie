FROM ubuntu
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y python3 python3-pip
RUN pip install requests
WORKDIR /app 
COPY hello.py /app/
CMD ["python3", "hello.py"]
