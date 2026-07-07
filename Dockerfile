FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

ENV PORT=8080
EXPOSE 8080

CMD exec gunicorn core.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 60
