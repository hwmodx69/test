FROM nikolaik/python-nodejs:python3.10-nodejs23-bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
    apt-get install -y tzdata ntpdate ffmpeg busybox && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN chmod -R 755 /app

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Ensure time is synced before starting bot
CMD bash -c "ntpdate -u pool.ntp.org || busybox ntpd -q -p pool.ntp.org || true && python3 main.py"
