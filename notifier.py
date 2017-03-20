import subprocess

idx = 0

def get_notification():
    global idx
    echo = subprocess.Popen(['echo', 'GET'], stdout = subprocess.PIPE)
    notifications = subprocess.check_output(['nc', 'localhost', '8755'], stdin=echo.stdout).decode('utf-8').splitlines()
    if not notifications:
        return 'No notification'
    if not idx < len(notifications):
        idx = 0
    ret = notifications[idx]
    idx += 1
    return ret.replace('\n', '').replace('\r', '')
