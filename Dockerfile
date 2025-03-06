# Use an official Python image as the base image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Install the required Python packages.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask web app code into the container.
COPY app.py .

# Expose port 5000 for the Flask web server.
EXPOSE 5000

# Command to run the Flask application.
CMD ["python", "app.py"]