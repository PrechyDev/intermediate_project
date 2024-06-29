# Use an official Python 3.10 runtime as a parent image
FROM python:3-slim

# Set the working directory
WORKDIR /analytics

# Install dependencies to allow downloading and unzipping DuckDB CLI
RUN apt-get update && apt-get install -y wget unzip

# Download and unzip DuckDB binary, then clean up
RUN wget https://github.com/duckdb/duckdb/releases/download/v1.0.0/duckdb_cli-linux-amd64.zip \
    && unzip duckdb_cli-linux-amd64.zip \
    && rm duckdb_cli-linux-amd64.zip 

# Copy the requirements file into the container at /app
COPY requirements.txt /analytics/

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /analytics

# Run data ingestion script
CMD ["python", "data_ingestion.py"]
