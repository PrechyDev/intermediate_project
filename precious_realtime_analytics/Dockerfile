# Use an official Python 3.10 runtime as a parent image
FROM python:3-slim

# Set the working directory
WORKDIR /analytics

# Copy the DuckDB binary into the container
COPY duckdb /analytics

# Copy the requirements file into the container at /app
COPY requirements.txt /analytics/

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /analytics

# Run python command
CMD ["python", "data_ingestion.py"]