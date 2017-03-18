import subprocess

def show_title():
    final_output = ''
    final_output += subprocess.check_output(['xtitle']).decode('utf-8').replace('\n', '')
    return final_output


