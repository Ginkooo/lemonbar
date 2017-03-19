import subprocess

def show_temps():
    final_output = ''
    output_lines = []
    sensors = subprocess.check_output(["sensors"]).decode('utf-8')
    sensors = sensors.splitlines()
    temps = []
    for line in sensors:
        if line.startswith('Core'):
            temps.append(line)
    for line in temps:
        line = line
        line = line.replace(' ', '')
        output_lines.append(line[6:13])
    for line in output_lines:
        final_output += line
        final_output += " | "
    return final_output


