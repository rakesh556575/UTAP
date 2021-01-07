FROM python:3
FROM django

ADD . /UTAP

WORKDIR /UTAP

RUN pip install -r requirements.txt
RUN ls -la
CMD ["python","manage.py", "runserver", "0.0.0.0:8080"]