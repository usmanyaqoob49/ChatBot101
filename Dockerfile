#our base image will be linux image
#python:3.8-alpine is a base image and we are trying to pull it from Docker Hub
FROM python:3.8-alpine

#now we will copy all the files present in this base image
#so source is current working directory (.) and destination is app foler in base image
COPY . /app

#now our working directory will become app
WORKDIR /app

#installing all the dependancies
RUN pip install -r requirements.txt

#and command we will run
CMD python chat_gpt_app.py