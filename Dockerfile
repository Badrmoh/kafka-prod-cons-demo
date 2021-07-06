FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=0
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "python3", "/app/app.py"]
