FROM ubuntu
RUN apt-get update && apt-get install -y build-essential
COPY main.c /app/
WORKDIR /app
ADD ./main.c .(/usr/bin)
RUN gcc -o main.exe main.c
CMD ["C:\Users\Gebruiker\Documents\TWEEDE_JAAR\OIT\Nieuwepoging/hello.exe"]
