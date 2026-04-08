FROM python:latest

LABEL Maintaner="David.Franco"

WORKDIR /usr/app/src

COPY main.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]

