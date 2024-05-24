
# MF90 - Script

Script simple untuk mengendalikan modem MF90 dari terminal


## Bisa Digunakan Untuk

- Linux Based Image OS
- Windows
- Android Based Image OS with Termux or another Terminal Emulator


## Kegunaan

- Mematikan WLAN Wifi
- Menyalakan WLAN Wifi
- Menyalakan Data
- Mematikan Data
- Merestart Modem

## Dibutuhkan

- Python3
- pip
- Password MIFI harus "admin"

## Installation

Install Script menggunakan wget

```bash
  wget --no-check-certificate https://raw.githubusercontent.com/Nuginity/mf90-script/main/requirements.txt && pip install -r requirements.txt && rm -r requirements.txt
```
```bash
  wget [https://raw.githubusercontent.com/Nuginity/mf90-script/script/script.py](https://raw.githubusercontent.com/Nuginity/mf90-script/main/script/script.py) && mv script.py mf90 && mv mf90 /usr/bin && chmod +x /usr/bin/mf90

```
    
## Usage/Examples
 
ketik di terminal :

```bash
mf90
```

## TODO
- Auto Wifi off
- Ubah Band
