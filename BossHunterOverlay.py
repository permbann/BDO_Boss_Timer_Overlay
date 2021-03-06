# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Black Desert Onine Worldboss timer using Tkinter to display a transparent window
with the next upcoming boss/es and a countdown.
"""

__authors__ = ["Lukas Schult"]
__contact__ = "glukasschult@gmail.com"
__credits__ = ["Lukas Schult"]
__date__ = "2021/06/03"
__deprecated__ = False
__email__ = "glukasschult@gmail.com"
__maintainer__ = "Lukas Schult"
__status__ = "Released"
__version__ = "0.1"

from datetime import datetime, timedelta
import pytz
from tkinter import *
import tkinter.font as tkFont
from configparser import ConfigParser
from appdirs import AppDirs
from pathlib import Path

UTC = pytz.utc

BOSS_TIMES_EU = {0: {datetime(1900, 1, 1, 0, 0): 'Karanda',
                     datetime(1900, 1, 1, 3, 0): 'Kzarka',
                     datetime(1900, 1, 1, 7, 0): 'Kzarka',
                     datetime(1900, 1, 1, 10, 0): 'Offin',
                     datetime(1900, 1, 1, 14, 0): 'Kutum',
                     datetime(1900, 1, 1, 17, 0): 'Nouver',
                     datetime(1900, 1, 1, 20, 15): 'Kzarka',
                     datetime(1900, 1, 1, 21, 15): None,
                     datetime(1900, 1, 1, 22, 15): 'Karanda'},
                 1: {datetime(1900, 1, 1, 0, 0): 'Kutum',
                     datetime(1900, 1, 1, 3, 0): 'Kzarka',
                     datetime(1900, 1, 1, 7, 0): 'Nouver',
                     datetime(1900, 1, 1, 10, 0): 'Kutum',
                     datetime(1900, 1, 1, 14, 0): 'Nouver',
                     datetime(1900, 1, 1, 17, 0): 'Karanda',
                     datetime(1900, 1, 1, 20, 15): 'Garmoth',
                     datetime(1900, 1, 1, 21, 15): None,
                     datetime(1900, 1, 1, 22, 15): 'Kutum_Kzarka'},
                 2: {datetime(1900, 1, 1, 0, 0): 'Karanda',
                     datetime(1900, 1, 1, 3, 0): 'Kzarka',
                     datetime(1900, 1, 1, 7, 0): 'Karanda',
                     datetime(1900, 1, 1, 10, 0): None,
                     datetime(1900, 1, 1, 14, 0): 'Kutum_Offin',
                     datetime(1900, 1, 1, 17, 0): 'Vell',
                     datetime(1900, 1, 1, 20, 15): 'Karanda_Kzarka',
                     datetime(1900, 1, 1, 21, 15): 'Quint_Muraka',
                     datetime(1900, 1, 1, 22, 15): 'Nouver'},
                 3: {datetime(1900, 1, 1, 0, 0): 'Kutum',
                     datetime(1900, 1, 1, 3, 0): 'Nouver',
                     datetime(1900, 1, 1, 7, 0): 'Kutum',
                     datetime(1900, 1, 1, 10, 0): 'Nouver',
                     datetime(1900, 1, 1, 14, 0): 'Kzarka',
                     datetime(1900, 1, 1, 17, 0): 'Kutum',
                     datetime(1900, 1, 1, 20, 15): 'Garmoth',
                     datetime(1900, 1, 1, 21, 15): None,
                     datetime(1900, 1, 1, 22, 15): 'Kzarka_Karanda'},
                 4: {datetime(1900, 1, 1, 0, 0): 'Nouver',
                     datetime(1900, 1, 1, 3, 0): 'Karanda',
                     datetime(1900, 1, 1, 7, 0): 'Kutum',
                     datetime(1900, 1, 1, 10, 0): 'Karanda',
                     datetime(1900, 1, 1, 14, 0): 'Nouver',
                     datetime(1900, 1, 1, 17, 0): 'Kzarka',
                     datetime(1900, 1, 1, 20, 15): 'Kutum_Kzarka',
                     datetime(1900, 1, 1, 21, 15): None,
                     datetime(1900, 1, 1, 22, 15): 'Karanda'},
                 5: {datetime(1900, 1, 1, 0, 0): 'Offin',
                     datetime(1900, 1, 1, 3, 0): 'Nouver',
                     datetime(1900, 1, 1, 7, 0): 'Kutum',
                     datetime(1900, 1, 1, 10, 0): 'Nouver',
                     datetime(1900, 1, 1, 14, 0): 'Quint_Muraka',
                     datetime(1900, 1, 1, 17, 0): 'Karanda_Kzarka',
                     datetime(1900, 1, 1, 20, 15): None,
                     datetime(1900, 1, 1, 21, 15): None,
                     datetime(1900, 1, 1, 22, 15): 'Nouver_Kutum'},
                 6: {datetime(1900, 1, 1, 0, 0): 'Kzarka',
                     datetime(1900, 1, 1, 3, 0): 'Kutum',
                     datetime(1900, 1, 1, 7, 0): 'Nouver',
                     datetime(1900, 1, 1, 10, 0): 'Kzarka',
                     datetime(1900, 1, 1, 14, 0): 'Vell',
                     datetime(1900, 1, 1, 17, 0): 'Garmoth',
                     datetime(1900, 1, 1, 20, 15): 'Kzarka_Nouver',
                     datetime(1900, 1, 1, 21, 15): None,
                     datetime(1900, 1, 1, 22, 15): 'Kutum_Karanda'}}

# BOSS_TIMES_SEA = {0: {datetime(1900, 1, 1, 3, 0): 'Kzarka_Nouver',
#                       datetime(1900, 1, 1, 7, 0): 'Nouver_Kutum',
#                       datetime(1900, 1, 1, 8, 0): None,
#                       datetime(1900, 1, 1, 12, 0): 'Kzarka_Karanda',
#                       datetime(1900, 1, 1, 16, 0): 'Offin',
#                       datetime(1900, 1, 1, 17, 30): 'Nouver'},
#                   1: {datetime(1900, 1, 1, 3, 0): 'Kutum_Karanda',
#                       datetime(1900, 1, 1, 7, 0): 'Kutum_Kzarka',
#                       datetime(1900, 1, 1, 8, 0): None,
#                       datetime(1900, 1, 1, 12, 0): 'Quint_Muraka',
#                       datetime(1900, 1, 1, 16, 0): 'Garmoth',
#                       datetime(1900, 1, 1, 17, 30): 'Kzarka_Offin'},
#                   2: {datetime(1900, 1, 1, 3, 0): 'Nouver_Kutum',
#                       datetime(1900, 1, 1, 7, 0): 'Karanda_Kzarka',
#                       datetime(1900, 1, 1, 8, 0): None,
#                       datetime(1900, 1, 1, 12, 0): 'Kutum_Nouver',
#                       datetime(1900, 1, 1, 16, 0): 'Vell',
#                       datetime(1900, 1, 1, 17, 30): 'Kutum'},
#                   3: {datetime(1900, 1, 1, 3, 0): 'Kzarka_Karanda',
#                       datetime(1900, 1, 1, 7, 0): 'Kutum_Nouver',
#                       datetime(1900, 1, 1, 8, 0): None,
#                       datetime(1900, 1, 1, 12, 0): 'Karanda_Nouver',
#                       datetime(1900, 1, 1, 16, 0): 'Garmoth',
#                       datetime(1900, 1, 1, 17, 30): 'Nouver'},
#                   4: {datetime(1900, 1, 1, 3, 0): 'Kutum_Kzarka',
#                       datetime(1900, 1, 1, 7, 0): 'Kzarka_Karanda',
#                       datetime(1900, 1, 1, 8, 0): None,
#                       datetime(1900, 1, 1, 12, 0): 'Nouver_Kutum',
#                       datetime(1900, 1, 1, 16, 0): 'Offin',
#                       datetime(1900, 1, 1, 17, 30): 'Karanda'},
#                   5: {datetime(1900, 1, 1, 3, 0): 'Kutum_Kzarka',
#                       datetime(1900, 1, 1, 7, 0): 'Karanda_Nouver',
#                       datetime(1900, 1, 1, 8, 0): 'Garmoth',
#                       datetime(1900, 1, 1, 12, 0): 'Quint_Muraka',
#                       datetime(1900, 1, 1, 16, 0): None,
#                       datetime(1900, 1, 1, 17, 30): 'Kzarka'},
#                   6: {datetime(1900, 1, 1, 3, 0): 'Nouver_Karanda',
#                       datetime(1900, 1, 1, 7, 0): 'Kutum_Karanda',
#                       datetime(1900, 1, 1, 8, 0): 'Vell',
#                       datetime(1900, 1, 1, 12, 0): 'Kzarka_Karanda',
#                       datetime(1900, 1, 1, 16, 0): 'Kutum_Nouver',
#                       datetime(1900, 1, 1, 17, 30): None}}


def get_next_spawn():
    """
    Checks for the upcoming boss based on the current time and day.
    :return: Boss names string and time until spawn as datetime.timedelta.
    """
    today_bosses = BOSS_TIMES_EU[datetime.now(UTC).weekday()]
    tomorrow_bosses = BOSS_TIMES_EU[(datetime.now(UTC).weekday() + 1) % 7]
    current_time = datetime.now(UTC).time()
    for spawn in today_bosses.keys():
        spawn_time = spawn.time()
        if spawn_time > current_time and today_bosses[spawn] is not None:
            return today_bosses[spawn], timedelta(hours=spawn_time.hour - current_time.hour,
                                                  minutes=spawn_time.minute - current_time.minute,
                                                  seconds=spawn_time.second - current_time.second)
    spawn = list(tomorrow_bosses.keys())[0]
    spawn_time = spawn.time()
    return tomorrow_bosses[list(tomorrow_bosses.keys())[0]], timedelta(hours=spawn_time.hour + 24 - current_time.hour,
                                                                       minutes=spawn_time.minute - current_time.minute,
                                                                       seconds=spawn_time.second - current_time.second)


def get_display_values():
    """
    Splits names string into a dict of names.
    :return: Names dict and countdown time as string.
    """
    names = dict()
    name, countdown = get_next_spawn()
    if "_" in name:
        sep = name.split("_")
        names[0] = sep[0]
        names[1] = sep[1]
    else:
        names[0] = name
    return names, str(countdown)


def read_create_settings():
    config_object = ConfigParser()

    if not Path(f"{AppDirs('BossHunterOverlay').user_data_dir}/config.ini").is_file():
        Path(AppDirs('BossHunterOverlay').user_data_dir).mkdir(parents=True, exist_ok=True)
        config_object["settings"] = {
            "size": "21",
            "x": "800",
            "y": "100"
        }
    else:
        config_object.read(f"{AppDirs('BossHunterOverlay').user_data_dir}/config.ini")
    return config_object


def write_settings():
    global config, size, root
    config["settings"] = {
        "size": f"{size}",
        "x": f"{root.winfo_x()}",
        "y": f"{root.winfo_y()}"
    }
    with open(f"{AppDirs('BossHunterOverlay').user_data_dir}/config.ini", 'w') as conf:
        config.write(conf)


# --------------UI
def update_overlay():
    """
    Updated the overlay with countdown and upcoming boss names.
    """
    names, countdown = get_display_values()
    timer_label.configure(text=countdown)
    name1_label.configure(text=names.get(0, ""))
    name2_label.configure(text=names.get(1, ""))
    root.after(1000, update_overlay)


def start_drag(event):
    root.x = event.x
    root.y = event.y


def stop_drag(event):
    root.x = None
    root.y = None


def on_motion(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry("+%s+%s" % (x, y))


def close(_):
    write_settings()
    root.destroy()


def get_resized_font(amount):
    global size, size_max, size_min
    size += amount
    size = size if size < size_max else size_max
    size = size if size > size_min else size_min
    return tkFont.Font(family="Lucida Grande", size=size, weight="bold")


def size_up(_):
    font = get_resized_font(2)
    timer_label.configure(font=font)
    name1_label.configure(font=font)
    name2_label.configure(font=font)


def size_down(_):
    font = get_resized_font(-2)
    timer_label.configure(font=font)
    name1_label.configure(font=font)
    name2_label.configure(font=font)


# read_create_config
config = read_create_settings()

# Tk window configs
root = Tk()
root.wm_attributes('-transparentcolor', 'black')
root.geometry(f"300x300+{config['settings']['x']}+{config['settings']['y']}")
root.overrideredirect(1)
root.call('wm', 'attributes', '.', '-topmost', True)

# Text settings
size = int(config["settings"]["size"])
size_max = 50
size_min = 10
fontcolor = "#9ca4ab"

# Frames
frame = Frame(root, bg="black")
frame.pack(expand=True, fill="both")

nav_frame = Frame(frame, bg="black")
nav_frame.pack(expand=True, fill="x", side=TOP, anchor=N)

content_frame = Frame(frame, bg="black")
content_frame.place(relx=.5, rely=.1, anchor=N)

# Navigation/Control
closer = Label(nav_frame, text="X                ", bg="black", fg=fontcolor,
               font=tkFont.Font(family="Lucida Grande", size=14, weight="bold"))
closer.pack(side="right")
closer.bind("<ButtonRelease-1>", close)

bigger = Label(nav_frame, text="+ ", bg="black", fg=fontcolor,
               font=tkFont.Font(family="Lucida Grande", size=20, weight="bold"))
bigger.pack(side="right")
bigger.bind("<ButtonRelease-1>", size_up)

grip = Label(nav_frame, text="                ???", bg="black", fg=fontcolor,
             font=tkFont.Font(family="Lucida Grande", size=14, weight="bold"))
grip.pack(side="left")
grip.bind("<ButtonPress-1>", start_drag)
grip.bind("<ButtonRelease-1>", stop_drag)
grip.bind("<B1-Motion>", on_motion)

smaller = Label(nav_frame, text=" ???", bg="black", fg=fontcolor,
                font=tkFont.Font(family="Lucida Grande", size=25, weight="bold"))
smaller.pack(side="left")
smaller.bind("<ButtonRelease-1>", size_down)

# Info Labels
timer_label = Label(content_frame, text="xxx", bg="black", fg=fontcolor,
                    font=tkFont.Font(family="Lucida Grande", size=size, weight="bold"))
timer_label.pack(side=TOP, anchor=N)

name1_label = Label(content_frame, text="xxx", bg="black", fg=fontcolor,
                    font=tkFont.Font(family="Lucida Grande", size=size, weight="bold"))
name1_label.pack(side=TOP, anchor=N)
name2_label = Label(content_frame, text="xxx", bg="black", fg=fontcolor,
                    font=tkFont.Font(family="Lucida Grande", size=size, weight="bold"))
name2_label.pack(side=TOP, anchor=N)

# Looping calls
update_overlay()
root.mainloop()
