# Torrent Downloader CLI

## Installation (Linux)
```bash

# Install system dependencies
sudo apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    libboost-python-dev \
    libssl-dev \
    python3-libtorrent

# Clone repository
git clone https://github.com/Rajarshi122/CLI-Torrent-Downloader.git
cd Torrent-Downloader

# Install Python requirements
pip3 install -r requirements.txt
```

## Usage
```bash
python3 torrent_downloader.py "magnet:?xt=urn:btih:..." ~/Downloads
```

## Legal Note
Only use this tool to download content you have legal rights to access.
