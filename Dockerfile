FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]