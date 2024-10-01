# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable
ENV NAME World

# Make port 8080 available to the world outside this container
EXPOSE 8080





RUN apt-get update && apt-get install -y curl vim
RUN pip install --upgrade pip
RUN apt install firefox-esr -y
RUN apt-get update && apt-get install -y curl vim
RUN chmod +x ./*
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.33.0-linux64.tar.gz
RUN chmod +x geckodriver
RUN export PATH=$PATH:/app/.
RUN cp -p geckodriver /usr/local/bin/


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entrypoint script into the container
COPY sub.sh /app/ 

# Make the entrypoint script executable
RUN chmod +x /app/sub.sh

# Use the entrypoint script as the entry point for the container
CMD ["./sub.sh"]
