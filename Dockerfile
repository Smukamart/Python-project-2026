FROM python:3.14

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 80
COPY . .
CMD [ "fastapi", "run", "./main.py", "--port", "80" ]
