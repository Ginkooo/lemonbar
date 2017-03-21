import subprocess

def get_song_stuff():
    try:
        song_name = subprocess.check_output(['mpc', '-p', '6001', 'current'], stderr=subprocess.PIPE).decode('utf-8')
    except Exception as e:
        return 'mpd is off... | '
    song_details = subprocess.check_output(['mpc', '-p', '6001', '-f', 'current']).decode('utf-8').splitlines()
    vol_line = song_details[-1]
    duration_line = song_details[-2]
    vol_line = vol_line[vol_line.find(':') + 1:vol_line.find('%')].strip()
    duration_line = duration_line[:duration_line.rfind(' ')]
    time = duration_line[duration_line.rfind(' ') + 1:]
    final_output = song_name + ' | ' + vol_line + '%' + ' | ' + time + ' | '
    final_output = final_output.replace('\n', '')
    return final_output

