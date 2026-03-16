FROM ubuntu
COPY task2.py /task2.py
COPY task2.db /task2.db
RUN apt-get update
RUN apt-get install python3 python3-flask -y
CMD ["python3", "/task2.py"]
