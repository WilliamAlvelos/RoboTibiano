import pyautogui as pg 
import time
import threading
from thread import Thread, ThreadGroup
import constants
import actions
from pynput.keyboard import Listener
from pynput import keyboard

def run():
    flags = [(1, 5), (2, 10), (3, 8), (4, 10), (5, 8), (6, 8), (7, 20)]    
    while True:
        for (flag, timer) in flags:
            actions.go_to_flag(flag, timer);
            while not actions.kill_monsters():
                pass
            


def key_code(key, th_group):
    if key == keyboard.Key.esc:
        event_th.set()
        th_group.stop()
        return False
    if key == keyboard.Key.delete:
        th_group.start()
        th_run.start()

global event_th

event_th = threading.Event()
th_run = threading.Thread(target=run)

th_check_potions = Thread(actions.check_potions)
th_check_healing = Thread(actions.check_healing)

group_thread = ThreadGroup([th_check_potions, th_check_healing])

with Listener(on_press=lambda key: key_code(key, group_thread)) as listener:
    listener.join()