# Use an official Python image as base
FROM python:3.9-slim

# Install FFmpeg
RUN apt-get update && \
    # apt-get install -y ffmpeg && \
    apt-get install -y --no-install-recommends ffmpeg libavcodec-extra && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Copy requirements and install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point
CMD ["python", "main.py"]