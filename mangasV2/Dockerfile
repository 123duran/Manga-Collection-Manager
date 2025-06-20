# Use an official Python runtime
FROM python:3.11

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /mangasV2

# Install dependencies
COPY requirements.txt /mangasV2/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /mangasV2/

# Copy and set entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
