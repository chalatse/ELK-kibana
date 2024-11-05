FROM python:3.9-slim

COPY requirements.txt .

RUN mdir /src/
COPY . /src

WORKDIR /src

EXPOSE 8888

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888" ]

