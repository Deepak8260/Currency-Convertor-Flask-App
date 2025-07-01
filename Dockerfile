# Start with official Python image
FROM python:3.9

# Set up our working directory
WORKDIR /app

# Copy everything from current directory to container
COPY . .

# Install required packages
RUN pip install -r requirements.txt

# Open port 8000
EXPOSE 8000

# Run the Flask app
CMD ["python", "app.py"]