# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /backend

# Copy the current directory contents into the container at /app
COPY requirements.txt /backend/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend files to the container
COPY . /backend
# Set environment variables for Flask
ENV FLASK_APP=endpoints.py
# Expose the Flask port
EXPOSE BACKEND_DOCKER_PORT

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
