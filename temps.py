import subprocess

def show_temps():
    final_output = ''
    output_lines = []
    temps = subprocess.check_output(["sensors"])
    temps = temps.splitlines()
    temps = temps[:5:-1]
    for line in temps:
        line = line.decode('utf-8')
        line = line.replace(' ', '')
        output_lines.append(line[6:13])
    for line in output_lines:
        final_output += line
        final_output += " | "
    return final_output


