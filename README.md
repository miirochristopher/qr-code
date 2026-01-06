# QR-CODE GENERATOR

A clean, lightweight **Streamlit application** for generating high-quality **325×325 pixel QR codes** from any URL, with instant PNG download support.

# 1️⃣ Run locally (python environments)

---

## Requirements

- Python **3.8+**
- pip
- A modern web browser

---

## Install Python

### Debian / Ubuntu / PopOS / Mint

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

### Fedora

```bash
sudo dnf install python3 python3-venv python3-pip
```

### Windows

Download from:
https://www.python.org/downloads/

✔ Ensure Add Python to PATH is checked.

#### Clone Repository

```bash
git clone https://github.com/miirochristopher/qr-code.git
cd qr-code
```

#### Create Virtual Environment

```bash
python3 -m venv .venv
```

#### Activate Environment

Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows (PowerShell)

```bash
.venv\Scripts\Activate.ps1
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Run the Application

```bash
streamlit run qr_ui.py
```

Open the displayed URL (usually http://localhost:8501).

### Features

```bash
URL → QR Code

Fixed output size: 325 × 325 px

High error correction

Browser-based UI

One-click PNG download

Cross-platform

Docker Support

See Docker Setup section below.

Desktop App

This app can be packaged as a desktop executable using PyInstaller (see below).
```

### Deactivate Environment

```bash
deactivate
```

---

# 2️⃣ Docker Setup (Dockerize Steps)

## `requirements.txt`

```txt
streamlit
qrcode[pil]
pillow
```

## Build Docker Image

```bash
docker build -t intuvance/qr-code .
```

## Run Container

```bash
docker run -p 8501:8501 intuvance/qr-code
```

## Open:

http://localhost:8501

# Optional: docker compose

```bash
docker compose -p qr-code up --build -d
```

## Cleanup

```bash
docker compose -p qr-code down -v
```

# 3️⃣ Desktop App Wrapper

This creates a single executable that launches the Streamlit app like a desktop application.

#### Build Desktop App

```bash
pyinstaller \
  --onefile \
  --windowed \
  --name QR-Code \
  desktop_launcher.py
```

#### Output

```bash
dist/
└── QR-Code
```

`Double-click to launch, browser opens automatically no terminal window`
