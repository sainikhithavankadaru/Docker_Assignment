FROM python:3.7-alpine 

WORKDIR /home

COPY . /home/data/

RUN mkdir -p /home/output/

WORKDIR /home/data

CMD ["python", "docker.py"]