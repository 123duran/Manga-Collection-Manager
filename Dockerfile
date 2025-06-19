# Use an official Python runtime
FROM python:3.11

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Run app (update 'your_project.wsgi' to your actual WSGI module)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mangasV2.wsgi:application"]
