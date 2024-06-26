FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/project

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]