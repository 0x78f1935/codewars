FROM python:3.8-rc-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install gcc -y && apt-get install libbluetooth-dev -y

RUN pip install codewars
ADD docker_test.py /docker_test.py
RUN python /docker_test.py