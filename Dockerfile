# Use an official Python image as base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt update && apt install -y ffmpeg

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# # Copy the Python script
# COPY main.py .

# Install moviepy manually (if needed)
RUN pip install moviepy

# Copy the application code
COPY . .

# Set the entry point
CMD ["python", "main.py"]