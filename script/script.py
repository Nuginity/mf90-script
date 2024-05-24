#! /usr/bin/env python3
import os
import requests
import time
from requests.exceptions import ConnectionError
from sys import exit

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_request(ip, payload):
    url = f'http://{ip}/goform/goform_set_cmd_process'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': f'http://{ip}',
        'Referer': f'http://{ip}/index.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }
    requests.post(url, data=payload, headers=headers)

def login(ip):
    payload = {'isTest': 'false', 'goformId': 'LOGIN', 'password': 'YWRtaW4%3D'}
    send_request(ip, payload)

def wifioff(ip):
    payload = {'goformId': 'SET_WIFI_INFO', 'isTest': 'false', 'm_ssid_enable': '0', 'wifiEnabled': '0'}
    send_request(ip, payload)

def wifion(ip):
    payload = {'goformId': 'SET_WIFI_INFO', 'isTest': 'false', 'm_ssid_enable': '0', 'wifiEnabled': '1'}
    send_request(ip, payload)

def reboot(ip):
    payload = {'isTest': 'false', 'goformId': 'REBOOT_DEVICE'}
    send_request(ip, payload)

def dataon(ip):
    payload = {'isTest': 'false', 'notCallback': 'true', 'goformId': 'CONNECT_NETWORK'}
    send_request(ip, payload)

def dataoff(ip):
    payload = {'isTest': 'false', 'notCallback': 'true', 'goformId': 'DISCONNECT_NETWORK'}
    send_request(ip, payload)

def printlist(data_list):
    max_length = max(len(str(item)) for item in data_list)
    border_width = max_length + 4
    border = "+" + "-" * (border_width - 2) + "+"
    print(border)
    for item in data_list:
        print(f"| {str(item).ljust(max_length)} |")
    print(border)

clear()

print('Pastikan Password MIFI mu adalah admin')
while True:
    ip = input("Masukan Alamat IP Modem, contoh 192.168.8.1: ")
    try:
        requests.get(f'http://{ip}', timeout=1)
        break
    except ConnectionError:
        print("IP Salah. Pastikan sesuai dengan WEBUI")

clear()
login(ip)
time.sleep(2)

while True:
    clear()
    pilihan = ["1. Matikan WIFI", "2. Nyalakan WIFI", "3. Nyalakan Data", "4. Matikan Data", "5. Reboot MIFI", "6. Exit"]
    print("MF90 SCRIPT BY NUGINITY")
    printlist(pilihan)
    p1 = input('Pilihan : ')

    if p1 == '1':
        print("Tunggu....")
        wifioff(ip)
        print("Wifi Berhasil Dimatikan")
    elif p1 == '2':
        print("Tunggu....")
        wifion(ip)
        print("Wifi Berhasil Dinyalakan")
    elif p1 == '3':
        print("Tunggu....")
        dataon(ip)
        print("Data Berhasil Dinyalakan")
    elif p1 == '4':
        print("Tunggu....")
        dataoff(ip)
        print("Data Berhasil Dimatikan")
    elif p1 == '5':
        print("Tunggu....")
        reboot(ip)
        print("Modem Berhasil di reboot")
        print("Mulai Script lagi jika sudah di terkonek kembali!")
        exit()
    elif p1 == '6':
        print("Exiting!")
        exit()
    time.sleep(1.5)
