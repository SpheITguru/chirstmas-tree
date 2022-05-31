FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3

COPY mytree.py .

COPY test .

RUN chmod 711 test

CMD ["./test"]