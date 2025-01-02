# # # Use an official Python runtime as a parent image
# # FROM python:3.12-slim

# # # Set environment variables
# # ENV PYTHONDONTWRITEBYTECODE 1
# # ENV PYTHONUNBUFFERED 1

# # # Install system dependencies
# # RUN apt-get update && apt-get install -y \
# #     gcc \
# #     python3-dev \
# #     && rm -rf /var/lib/apt/lists/*

# # # Set work directory
# # WORKDIR /app

# # # Install Python dependencies
# # COPY requirements.txt .
# # RUN pip install --no-cache-dir -r requirements.txt


# # # Install solc
# # RUN python -c "from solcx import install_solc; install_solc('0.8.0')"

# # # Copy project
# # COPY . .

# # WORKDIR /app/blockblock/blockblock


# # CMD ["python", "/appblockblock/manage.py", "runserver", "0.0.0.0:8000"]

# # Use an official Python runtime as a parent image
# # Use an official Python runtime as a parent image
# FROM python:3.12-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     gcc \
#     python3-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Set work directory
# WORKDIR /app

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Install solc
# RUN python -c "from solcx import install_solc; install_solc('0.8.0')"

# # Copy project into container
# COPY blockblock /app

# # Set the correct working directory (blockblock folder)
# WORKDIR /app

# # Run the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install solc
RUN python -c "from solcx import install_solc; install_solc('0.8.0')"

# Copy project into container
COPY . .

# Set the correct working directory
WORKDIR /app/blockblock

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
