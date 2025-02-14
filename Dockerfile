# Use Python as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY fetch_commits.py .

# Install dependencies
RUN pip install requests

# Run the script
CMD ["python", "fetch_commits.py"]
