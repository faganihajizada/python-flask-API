# Use the Python3.7.2 image
FROM python:3.8.5-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start flask instance
ENTRYPOINT ["python3"]
CMD ["main.py"]
