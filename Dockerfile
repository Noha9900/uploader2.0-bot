# Use lightweight Python image
FROM python:3.11-slim

# Prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (IMPORTANT for ffmpeg + build)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    libffi-dev \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Upgrade pip & install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create download directory
RUN mkdir -p downloads

# Expose nothing (Telegram bot does not need port)
# EXPOSE 8080  (not required)

# Start bot
CMD ["python", "main.py"]
