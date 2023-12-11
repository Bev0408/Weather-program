# Base image for the application. Python 3.10.6 with Alpine Linux image
FROM python:3.10.6-alpine
#This sets the working directory in the container
WORKDIR /app
#Coppies the current directory contents into the container at /app
COPY . /app
#Installs all the dependancies needed to run the applictaion. All of these are included in the requirements.txt file)
RUN pip install -r requirements.txt 
#Defines the env variables for the API key
ENV api_key $api_key
#These are the commands that will be used to run the application
CMD ["python", "weatherapp.py"]


