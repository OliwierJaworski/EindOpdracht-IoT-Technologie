FROM arm32v7/ubuntu
COPY helloworld.py /app/
WORKDIR /app
CMD ["python", "helloworld.py"]
