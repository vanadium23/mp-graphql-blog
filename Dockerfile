FROM python:3.6

MAINTAINER chernoffivan@gmail.com
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

COPY app /app
WORKDIR /app

RUN ./manage.py migrate && ./manage.py loaddata blog

