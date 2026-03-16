FROM ubuntu
COPY fileserver.py /fileserver.py
RUN apt-get update
RUN apt-get install python3 python3-flask -y
CMD ["python3", "/fileserver.py"]
