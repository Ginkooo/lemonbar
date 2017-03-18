def show_music_info():
    ret = ''
    if process.stdin.writable():
        process.stdin.write('currentsong'.encode('utf-8'))
    if process.stdout.readable():
        ret += process.stdout.readline().decode('utf-8')
    return ret


