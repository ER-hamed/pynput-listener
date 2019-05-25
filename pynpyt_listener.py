#! /usr/bin/python3.6

from pynput import mouse
from pynput import keyboard
from _thread import start_new_thread


def on_move(x, y):
    print('on_move     ' + '   x: ' + str(x) + '   y: ' + str(y), flush=True)


def on_click(x, y, button, pressed):
    print('on_click     ' + '   x: ' + str(x) + '   y: ' + str(y) + '   button: ' + str(button) + '   state: ' + str(pressed), flush=True)


def on_scroll(x, y, dx, dy):
    print('on_scroll     ' + '   x: ' + str(x) + '   y: ' + str(y) + '   scroll[x]: ' + str(dx) + '   scroll[y]: ' + str(dy), flush=True)


def on_press(key):
    print('on_press     ' + str(key), flush=True)


def on_release(key):
    print('on_release     ' + str(key), flush=True)


def mouse_listener():
    with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
    listener = mouse.Listener()
    listener.start()


def keyboard_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()


start_new_thread(mouse_Listener, ())
keyboard_Listener()
