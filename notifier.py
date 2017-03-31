import subprocess
import sys
import os
import socket
import fcntl
import json
from socket import socket, AF_INET, SOCK_STREAM

CONFIG_FILE = os.getenv('NOTIFY_CONFIG')

def log(msg):
    print(msg)
    sys.stdout.flush()

config = {
        'HOST': 'localhost',
        'PORT': 8755
        }

if not CONFIG_FILE:
    print('No NOTIFY_CONFIG system variable set')
    exit()

with open(CONFIG_FILE, 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        if line.startswith('#'):
            continue
        line = line.rstrip()
        rec = line.split('=')
        if rec[0] == 'PORT':
            rec[1] = int(rec[1])
        config[rec[0]] = rec[1]
idx = 0


def connect(s: socket) -> None:
    '''Reconects to server'''

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((config['HOST'], config['PORT']))


def get_from_server() -> str:
    '''Sends GET to sever and returns response'''
    global s
    s.sendall(b'GET')
    data = s.recv(1024)
    if not data:
        connect(s)
    else:
        data = data.decode('utf-8').strip().splitlines()
        return data


def get_notification():
    global idx
    global s
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((config['HOST'], config['PORT']))
        notifications = get_from_server()
    except socket.error as e:
        sys.stderr.write(e.__traceback__)
        sys.stderr.flush()
        return 'No connection'
    if not notifications:
        return 'No notification'
    if not idx < len(notifications):
        idx = 0
    ret = notifications[idx]
    idx += 1
    return ret.rstrip() + ' | '
