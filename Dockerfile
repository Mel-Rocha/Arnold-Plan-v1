FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    libdbus-1-dev \
    libcups2-dev \
    libgirepository1.0-dev \
    libgtk-3-dev \
    libffi-dev \
    pkg-config \
    gobject-introspection \
    libsystemd-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# running migrations
RUN python manage.py migrate

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "config.wsgi"]
