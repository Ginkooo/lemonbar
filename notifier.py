import subprocess
import os

CONFIG_FILE = os.getenv('NOTIFY_CONFIG')

if not CONFIG_FILE:
    print('There is no NOTIFY_CONFIG env variable')
    exit()

with open(CONFIG_FILE, 'r') as f:
    for line in f.readlines():
        line = line.strip()
        rec = line.split('=')
        if rec[0] == 'PORT':
            PORT = rec[1]
        if rec[0] == 'HOST':
            HOST = rec[1]

idx = 0

def get_notification():
    global idx
    echo = subprocess.Popen(['echo', 'GET'], stdout = subprocess.PIPE)
    try:
        notifications = subprocess.check_output(['nc', HOST, PORT], stdin=echo.stdout).decode('utf-8').splitlines()
    except:
        return 'No connection'
    if not notifications:
        return 'No notification'
    if not idx < len(notifications):
        idx = 0
    ret = notifications[idx]
    idx += 1
    return ret.replace('\n', '').replace('\r', '') + ' | '
