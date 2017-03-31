#! /bin/python
import sys
import time
import os
from utils import color, align, rand_color
import temps
import window_title
import clock
import master_volume
import song
import notifier
import window_title
from threading import Event
from multiprocessing import Process, Manager, Event
from ctypes import c_char


def get_output(dic, event):
    while True:
        event.wait()
        parts = [
            color(rand_color(), 'F', temps.show_temps()),
            color(rand_color(), 'F', master_volume.get_master_volume()),
            color(rand_color(), 'F', song.get_song_stuff()),
            color('#ffffff', 'F', window_title.show_title()),
            color(rand_color(), 'F', notifier.get_notification()),
            align('r', color('#FF00FF', 'F', clock.show_time())),
        ]


        output = ''
        for part in parts:
            output += part
        dic['output'] = output

event = Event()
manager = Manager()
dic = manager.dict()
dic['output'] = 'No input...'
t = Process(target=get_output, args=(dic,event), daemon=True)
t.start()

while True:
    time.sleep(1)
    print(dic['output'])
    event.set()
    sys.stdout.flush()
