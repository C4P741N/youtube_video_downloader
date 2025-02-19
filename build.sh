#!/bin/bash

# Enable echoing of commands
set -x

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

# Tail logs
docker logs -f youtube-audio-downloader
