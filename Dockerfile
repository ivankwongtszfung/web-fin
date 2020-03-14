FROM python:3.7-slim

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install -r /usr/src/app/requirements/common.txt

CMD [ "python", "manage.py", "run"]