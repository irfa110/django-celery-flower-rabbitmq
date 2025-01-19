
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY ./requirements.txt /app/

# Install PostgreSQL client and other dependencies
RUN apt-get update \
    && apt-get install -y postgresql-client \
    && pip install --no-cache-dir --default-timeout=300 --upgrade pip \
    && pip install --no-cache-dir --default-timeout=300 -r requirements.txt \
    && apt-get clean

# Copy the application files into the container
COPY . /app/

# Set proper ownership of the application files
RUN chown -R root:root /app

# Switch to the root user (if necessary, though consider using a non-root user in production)
USER root

# Optionally, you can specify the entrypoint for the container
ENTRYPOINT ["python"]
