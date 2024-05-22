from os import system, name
import requests
from requests.exceptions import ConnectionError
import time
from sys import exit

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def send_request(ip, payload):
    url = 'http://' +  ip + '/goform/goform_set_cmd_process'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': str(len(payload)),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Host': ip,
        'Origin': 'http://' + ip,
        'Referer': 'http://' + ip + '/index.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.post(url, data=payload, headers=headers)

def login(ip):
    payload = {
        'isTest': 'false',
        'goformId': 'LOGIN',
        'password': 'YWRtaW4%3D'
    }
    send_request(ip, payload)

def wifioff(ip):
    payload = {
        'goformId': 'SET_WIFI_INFO',
        'isTest': 'false',
        'm_ssid_enable': '0',
        'wifiEnabled': '0'
    }
    send_request(ip, payload)

def wifion(ip):
    payload = {
        'goformId': 'SET_WIFI_INFO',
        'isTest': 'false',
        'm_ssid_enable': '0',
        'wifiEnabled': '1'
    }
    send_request(ip, payload)

def reboot(ip):
    payload = {
        'isTest': 'false',
        'goformId' : 'REBOOT_DEVICE'
    }
    send_request(ip, payload)

def dataon(ip):
    payload = {
        'isTest': 'false',
        'notCallback' : 'true',
        'goformId' : 'CONNECT_NETWORK'
    }
    send_request(ip, payload)

def dataoff(ip):
    payload = {
        'isTest': 'false',
        'notCallback' : 'true',
        'goformId' : 'DISCONNECT_NETWORK'
    }
    send_request(ip, payload)

def printlist(data_list):
        max_length = max(len(str(item)) for item in data_list)
        border_width = max_length + 4
        top_border = "+" + "-" * (border_width - 2) + "+"
        bottom_border = top_border
    
        print(top_border)
    
        for item in data_list:
            item_str = str(item).ljust(max_length)
            print(f"| {item_str} |")
        print(bottom_border)

clear()

print('Pastikan Password MIFI mu adalah admin')
while True:
    ip = input("Masukan Alamat IP Modem, contoh 192.168.8.1: ")
    try:
        requests.get('http://' + ip, timeout=1)
        break
    except ConnectionError as e:
        print("IP Salah. Pastikan sesuai dengan WEBUI")

while True:

    clear()

    login(ip)
    time.sleep(2)

    clear()
    

    pilihan = ["1. Matikan WIFI", "2. Nyalakan WIFI", "3. Nyalakan Data", "4. Matikan Data", "5. Reboot MIFI", "6. Exit"]
    print("MF90 SCRIPT BY NUGINITY")
    printlist(pilihan)
    p1 = input('Pilihan : ')

    if p1 == '1':
        print("Tunggu....")
        wifioff(ip)
        print("Wifi Berhasil Dimatikan")
        time.sleep(1.5)
    elif p1 == '2':
        print("Tunggu....")
        wifion(ip)
        print("Wifi Berhasil Dinyalakan")
        time.sleep(1.5)
    elif p1 == '3':
        print("Tunggu....")
        dataon(ip)
        print("Data Berhasil Dinyalakan")
        time.sleep(1.5)
    elif p1 == '4':
        print("Tunggu....")
        dataoff(ip)
        print("Data Berhasil Dimatikan")
        time.sleep(1.5)
    elif p1 == '5':
        print("Tunggu....")
        reboot(ip)
        print("Modem Berhasil di reboot")
        print("Mulai Script lagi jika sudah di terkonek kembali!")
        exit()
    elif p1 == '6':
        print("Exiting!")
        exit()