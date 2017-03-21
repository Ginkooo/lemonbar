#! /bin/python
import sys
import os
from utils import color, align, rand_color
import temps
import window_title
import clock
import master_volume
import song
import notifier

while True:
    parts = [
        color(rand_color(), 'F', temps.show_temps()),
        color(rand_color(), 'F', master_volume.get_master_volume()),
        color(rand_color(), 'F', song.get_song_stuff()),
        color(rand_color(), 'F', notifier.get_notification()),
        align('r', color('#FF00FF', 'F', clock.show_time())),
    ]


    output = ''
    for part in parts:
        output += part

    print(output)
    sys.stdout.flush()
    os.system('sleep 1')
