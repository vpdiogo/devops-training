#!/bin/bash

# VM startup script for Google Cloud Platform
# This script sets up Docker and runs the FastAPI application

set -e

# Update system packages
apt-get update
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Install Docker
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io

# Start Docker service
systemctl start docker
systemctl enable docker

# Configure Docker to use gcloud as credential helper
gcloud auth configure-docker --quiet

# Pull and run the application container
PROJECT_ID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")
IMAGE_NAME="gcr.io/${PROJECT_ID}/devops-app:latest"

# Pull the latest image
docker pull ${IMAGE_NAME}

# Stop any existing container
docker stop devops-app || true
docker rm devops-app || true

# Run the FastAPI application
docker run -d \
  --name devops-app \
  --restart unless-stopped \
  -p 80:8080 \
  -e ENVIRONMENT=production \
  -e DEBUG=false \
  ${IMAGE_NAME}

# Setup firewall rules (if needed)
# gcloud compute firewall-rules create allow-devops-app \
#   --allow tcp:80 \
#   --source-ranges 0.0.0.0/0 \
#   --description "Allow HTTP traffic for DevOps app"

echo "DevOps Training API deployed successfully on VM"