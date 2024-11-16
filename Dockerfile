FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt/ .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=main.py

# Run app.py when the container launches
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]


