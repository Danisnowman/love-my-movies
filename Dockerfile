FROM python:3-alpine

ENV DEV_PROGRA="Daniel Hernández - 20180077"

WORKDIR /love-my-movies

COPY . /love-my-movies

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]