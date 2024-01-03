FROM arm32v7/ubuntu
RUN apt-get update && \
    apt-get install -y python
COPY helloworld.py /app/
WORKDIR /app
CMD ["python", "helloworld.py"]
