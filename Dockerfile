FROM python:3.12.2-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN pip install --upgrade setuptools

EXPOSE 8008

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8008
