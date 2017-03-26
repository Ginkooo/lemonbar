import subprocess
import os
import json

CONFIG_FILE = os.getenv('NOTIFY_CONFIG')

config = {
        'HOST': 'localhost',
        'PORT': '8751'
        }

if not CONFIG_FILE:
    exit()

with open(CONFIG_FILE, 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        if line.startswith('#'):
            continue
        line = line.rstrip()
        rec = line.split('=')
        config[rec[0]] = rec[1]
idx = 0

def get_notification():
    global idx
    echo = subprocess.Popen(['echo', 'GET'], stdout = subprocess.PIPE)
    try:
        notifications = subprocess.check_output(['nc', config['HOST'], config['PORT']], stdin=echo.stdout).decode('utf-8').splitlines()
    except Exception as e:
        return 'No connection'
    if not notifications:
        return 'No notification'
    if not idx < len(notifications):
        idx = 0
    ret = notifications[idx]
    idx += 1
    return ret.replace('\n', '').replace('\r', '') + ' | '
