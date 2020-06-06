FROM python:3.7-slim

# enable only
# RUN apt-get update && apt-get install -y procp 

WORKDIR /usr/src/app
COPY ./requirements/ /usr/src/app/requirements/
RUN pip install -r /usr/src/app/requirements/dev.txt
COPY . /usr/src/app

CMD [ "python", "manage.py", "run"]
