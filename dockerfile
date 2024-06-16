# Use the official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create a directory for the app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install cron and ensure python3 is linked to python
RUN apt-get update && apt-get install -y cron \
    && apt-get clean

# Copy the startup script to the container
COPY startup.sh /app/startup.sh
RUN chmod +x /app/startup.sh

# Run the command on container startup
CMD /app/startup.sh && cron && tail -f /var/log/cron.log
