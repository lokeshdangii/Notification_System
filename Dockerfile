# Use a lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR .

# Copy requirements first (for caching layers)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Default command will be overridden by docker-compose
CMD ["python", "api/app.py"]
