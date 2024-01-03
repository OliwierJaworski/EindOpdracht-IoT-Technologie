FROM python:3
COPY helloworld.py /app/
WORKDIR /app
CMD ["python", "helloworld.py"]
