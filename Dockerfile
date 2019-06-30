FROM python:3.8-rc-slim

# Install codewars dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install git -y
RUN apt-get install gcc -y && apt-get install libbluetooth-dev -y
RUN apt-get install libxml2-dev libxslt1-dev zlib1g-dev -y && apt-get install python3-lxml -y

# RUN pip install codewars # LIVE ENV
RUN pip install git+https://github.com/0x78f1935/codewars@master # DEBUG ENV
ADD docker_test.py /docker_test.py
CMD python /docker_test.py
