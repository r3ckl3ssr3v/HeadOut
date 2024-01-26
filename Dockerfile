# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask (and any other dependencies if needed)
RUN pip install --no-cache-dir Flask

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable for data directory
ENV DATA_DIR /tmp/data/

# Command to run the application
CMD ["python", "app.py"]
