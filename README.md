# QR-CODE GENERATOR

Install python3

## For Debian/Ubuntu-based systems

```
sudo apt update
sudo apt install python3 python3-venv
```

## Ubuntu / Debian / PopOS / Mint

```
sudo apt update
sudo apt install python3-tk
```

## For Fedora-based systems

```
sudo dnf install python3 python3-venv
```

## Clone this repository

Create a virtual environment using the venv module. This command creates a new directory (commonly named .venv or env) that contains an isolated Python installation:

```
cd qr-code

python3 -m venv .venv
```

## Activate the virtual environment.

```
source .venv/bin/activate
```

## Install packages using pip.

The packages will be installed into your isolated environment, not the system's Python:

```
pip install qrcode[pil]

python -m pip install qrcode[pil] pillow
```

## Run the application

Windows

```
python qr_ui.py
```

Linux / macOS

```
python3 qr_ui.py
```

## Deactivate the environment when you are finished working on the project.

This returns your shell to the normal system Python environment:

```
deactivate
```
