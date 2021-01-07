FROM django
RUN apt-get update -y
RUN apt-get install python-pip -y
ADD . /UTAP

WORKDIR /UTAP

RUN pip install -r requirements.txt
RUN ls -la
CMD ["python","manage.py", "runserver", "0.0.0.0:8080"]