FROM python:3.10-slim

WORKDIR /code

COPY . . 

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]