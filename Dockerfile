FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install -r /opt/rishat/requirements.txt

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]