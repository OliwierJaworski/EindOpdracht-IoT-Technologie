FROM arm32v7/ubuntu
RUN apt-get update && \
    apt-get install -y python3
COPY helloworld.py /app/
WORKDIR /app
CMD ["python", "helloworld.py"]
