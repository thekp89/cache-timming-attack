# Use the full Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script to the working directory
COPY cache_timing_attack.py /app/cache_timing_attack.py

# Install necessary libraries, including numpy
RUN apt-get update && \
    apt-get install -y libfreetype6-dev libpng-dev && \
    pip install --no-cache-dir matplotlib numpy

# Command to run the Python script
CMD ["python", "cache_timing_attack.py"]

