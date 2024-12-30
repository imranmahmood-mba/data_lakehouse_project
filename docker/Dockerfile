FROM python:3.8-slim

# Install Delta Lake dependencies
RUN pip install pyspark delta-spark pytest

# Copy project files into the container
COPY . /app
WORKDIR /app

# Entry point for running tests or scripts
CMD ["bash"]

