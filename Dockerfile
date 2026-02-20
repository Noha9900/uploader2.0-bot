# ==============================
# Base Image
# ==============================
FROM python:3.11-slim

# ==============================
# Environment Settings
# ==============================
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ==============================
# System Dependencies
# ==============================
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    gcc \
    libffi-dev \
    build-essential \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ==============================
# Set Work Directory
# ==============================
WORKDIR /app

# ==============================
# Install Python Dependencies
# ==============================
COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# ==============================
# Copy Application Code
# ==============================
COPY . .

# ==============================
# Create Runtime Folders
# ==============================
RUN mkdir -p /app/downloads \
    && mkdir -p /app/thumbnails

# ==============================
# Start Application
# ==============================
CMD ["python", "main.py"]
