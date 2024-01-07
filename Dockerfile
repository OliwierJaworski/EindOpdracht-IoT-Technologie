FROM ubuntu
RUN pip install requests
WORKDIR /app 
COPY HTTPS_CRUD.py /app/
CMD ["python3", "HTTPS_CRUD.py"]
