# Use a Python base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files
COPY ip_both.py ip_v4.py ip_v6.py ./

# Expose ports
EXPOSE 5000 5001 5002

# Command to run the Flask apps
CMD ["/bin/bash", "-c", "python ip_both.py & python ip_v4.py & python ip_v6.py"]
