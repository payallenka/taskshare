# Use official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /code

# Copy requirements.txt first to optimize Docker caching
COPY requirements.txt /code/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /code/

# Expose port 8000 for the app to be accessed
EXPOSE 8000

# Set environment variable to tell Django not to prompt for input during migrations
ENV PYTHONUNBUFFERED 1

# Command to run the Django app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "taskshare.wsgi:application"]
