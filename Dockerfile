FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip --no-cache-dir install -r requirements.txt

CMD ["python3", "src/main.py"]