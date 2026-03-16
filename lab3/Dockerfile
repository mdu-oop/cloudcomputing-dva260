FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN echo "print('this is my first container!')" > foo.py
CMD ["python3" , "foo.py"]
