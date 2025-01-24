FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code (added dynamically via volumes in development)
COPY . /app

# Expose the default Django port
EXPOSE 8000
