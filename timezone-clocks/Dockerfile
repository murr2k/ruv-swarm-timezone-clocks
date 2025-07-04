# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for GUI applications
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables for GUI display
ENV DISPLAY=:0

# Expose port (not needed for this GUI app, but good practice)
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]