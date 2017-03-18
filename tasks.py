def show_tasks():
    tasks = [
            'Nauczyć się na poniedziałek',
            'Poprawić taskbar',
            'Zrobić notyfikacje',
            'Napisać dwa posty do środy',
            'Serwer notyfikacji!',
            ]
    global curr_task
    final_output = color(randomize_color(), "F")
    if curr_task == '':
        num = 0
    else:
        num = tasks.index(curr_task)
        num += 1
        if  not num < len(tasks):
            num = 0
    final_output += tasks[num]
    curr_task = tasks[num]
    return final_output


