#!/bin/bash

# Enable echoing of commands
set -x

# Define the video URL variable
VIDEO_URL="https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Stop and remove existing container only if it exists
if docker compose ps -q; then
  docker compose down -v
fi

# Remove the old image if it exists
docker rmi youtube-audio-downloader || true

# Build a new image
docker build -t youtube-audio-downloader .

# Start the container
docker compose build --no-cache
docker compose up -d

# # Run the container with the video URL as an environment variable
# docker run -e VIDEO_URL="$VIDEO_URL" youtube-audio-downloader

# Tail logs
docker logs -f youtube-audio-downloader
