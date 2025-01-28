# Remote Screenshot Monitoring System from Vohala.

A client-server system for periodic screenshot monitoring of client machines. Server collects and organizes screenshots from connected clients every 30 seconds.

## Features

- 📁 Automatic folder creation by hostname
- ⏱️ Configurable screenshot interval (default: 30s)
- 📸 PNG format screenshots with timestamp
- 🌐 Cross-platform compatibility (Windows/macOS/Linux)
- 🔌 Automatic client reconnect functionality
- 📈 Graceful error handling and network recovery

## Requirements

- Python 3.6+
- Pillow library (`pip install pillow`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vohala/Screenshot.git
cd Screenshot

pip install -r requirements.txt
