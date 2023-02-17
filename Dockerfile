FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/rishat

COPY ./requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

COPY . /opt/rishat

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]