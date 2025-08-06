# Use a newer base image to avoid buster repo issues
FROM nikolaik/python-nodejs:python3.10-nodejs17-bullseye

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
WORKDIR /app
COPY . /app

# Set permissions
RUN chmod -R 755 /app

# Upgrade pip and install requirements
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Start the bot
CMD ["python3", "main.py"]
