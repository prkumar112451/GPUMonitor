# Dockerfile
FROM python:3.9-slim

# Copy the requirements.txt file into the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r /app/requirements.txt

# Copy the GPU monitoring script into the container
COPY gpu_monitor.py /app/gpu_monitor.py

# Set the working directory
WORKDIR /app

# Command to run the GPU monitoring script
CMD ["python", "gpu_monitor.py"]
