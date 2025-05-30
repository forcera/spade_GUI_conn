# Copyright (c) 2024 FORCERA, LDA
# 
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0.
# 
# SPDX-License-Identifier: EPL-2.0

FROM ubuntu:focal-20240918
SHELL ["/bin/bash", "-c"]

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app/framework
COPY . .

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Lisbon

# Install dependencies, including pinned versions, Python, and additional tools
RUN DEBIAN_FRONTEND="noninteractive" \
    apt-get update && \
    apt-get install -y \
    python3=3.8.2-0ubuntu2 \
    python3-distutils=3.8.10-0ubuntu1~20.04 \
    curl \
    libgl1=1.3.2-1~ubuntu0.20.04.2 \
    tzdata \
    python3-pip=20.0.2-5ubuntu1.11 \
    python3-dev=3.8.2-0ubuntu2 \
    build-essential=12.8ubuntu1.1 \
    cmake=3.16.3-1ubuntu1.20.04.1 \
    git \
    wget=1.20.3-1ubuntu2.1 \
    pkg-config=0.29.1-0ubuntu4 \
    libjpeg-dev=8c-2ubuntu8 \
    libpng-dev=1.6.37-2 \
    libtiff-dev=4.1.0+git191117-2ubuntu0.20.04.14 \
    libavcodec-dev=7:4.2.7-0ubuntu0.1 \
    libavformat-dev=7:4.2.7-0ubuntu0.1 \
    libswscale-dev=7:4.2.7-0ubuntu0.1 \
    libv4l-dev=1.18.0-2build1 \
    libxvidcore-dev=2:1.3.7-1 \
    libx264-dev=2:0.155.2917+git0a84d98-2 \
    libgtk2.0-dev=2.24.32-4ubuntu4.1 \
    libatlas-base-dev=3.10.3-8ubuntu7 \
    gfortran=4:9.3.0-1ubuntu2 \
    ffmpeg=7:4.2.7-0ubuntu0.1 \
    libglib2.0-0=2.64.6-1~ubuntu20.04.8 \
    redis-server=5:5.0.7-2ubuntu0.1 \
    python3-gi=3.36.0-1 \
    python3-gi-cairo=3.36.0-1 \
    gir1.2-gtk-3.0=3.24.20-0ubuntu1.2 \
    gstreamer1.0-tools \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    gstreamer1.0-gtk3 \
    gstreamer1.0-pulseaudio \
    python3-gst-1.0 \
    gir1.2-gst-rtsp-server-1.0 \
    python3-tk \
    python-pil \
    python-pil.imagetk \
    x11-xserver-utils \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    python3 <(curl https://bootstrap.pypa.io/get-pip.py) && \
    pip3 install --no-cache-dir -r ./requirements.txt  

ENTRYPOINT ["python3", "-u","connection_issue_test.py"]
