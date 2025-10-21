FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./


RUN apt-get update 
RUN pip install --no-cache-dir -r requirements.txt


RUN mkdir /templates

COPY main.py /app/
COPY ./templates/ /app/templates/

EXPOSE 5000

CMD ["flask", "--app", "main.py", "run", "--host=0.0.0.0", "--port=5000"]

# CMD [ "python", "main.py" ]