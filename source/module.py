import requests

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