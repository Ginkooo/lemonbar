import datetime

def show_time():
    final_output = ''
    final_output += datetime.datetime.now().strftime("%d.%m.%Y  %H:%M:%S")
    return final_output
