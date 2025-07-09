FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Install Python dependencies with pip
RUN pip install --no-cache-dir -r requirements.txt

# Make sure uvicorn is properly installed and in PATH
RUN pip install --no-cache-dir uvicorn==0.23.2 && \
    which uvicorn

# Copy only what's needed for the app
COPY app/ ./app/
COPY templates/ ./templates/
COPY app/static/css/styles.css ./app/static/css/
COPY app/static/js/script.js ./app/static/js/
COPY garbage_resnet50_final_model.pth .

# Create necessary directories
RUN mkdir -p uploads

# Set environment variables
ENV PYTHONPATH=/app
ENV PATH="/usr/local/bin:${PATH}"

# Expose the port
EXPOSE 8000

# Command to run the application with full path
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]