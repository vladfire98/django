FROM python:3.10-slim

WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "Site.wsgi:application"]
