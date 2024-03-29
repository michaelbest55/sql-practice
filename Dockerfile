FROM python:3.8.8

WORKDIR /app
COPY requirements.txt /app

RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY /app /app
CMD sleep 5; alembic upgrade head; python app/connect.py