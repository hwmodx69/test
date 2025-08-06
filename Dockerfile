FROM nikolaik/python-nodejs:python3.10-nodejs23-bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y tzdata ntpdate ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN chmod -R 755 /app

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Sync time before starting Python bot
CMD bash -c "ntpdate -u pool.ntp.org || true && python3 main.py"
