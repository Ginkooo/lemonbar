import subprocess

def get_master_volume():
    output = subprocess.check_output(['amixer', 'sget', 'Master']).decode('utf-8').splitlines()
    output = [line.strip() for line in output]
    output = [line for line in output if line.startswith('Front')]
    output = output[0]
    final_output = output[:output.rfind('%')]
    final_output = final_output[final_output.rfind('[') + 1:]
    return final_output + '%' + ' | '
