FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/rishat

COPY ./requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

COPY . /opt/rishat

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]