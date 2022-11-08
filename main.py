import cv2 as cv
import numpy as np
import pyautogui
import keyboard as kb
import shutil
import time


def reload():
    main()

def main():
    scr_size = tuple(pyautogui.size())
    enc = cv.VideoWriter_fourcc(*'MJPG')
    filename = 'video_buffer'
    enc_ext = '.avi'

    fps = 25
    lenght = 5 #min
    named_tuple = time.localtime()
    current_time = int(time.strftime("%H%M"))
    out = cv.VideoWriter(filename + enc_ext, enc, fps, (scr_size))
    cap = pyautogui.screenshot()

    end_time = current_time + lenght
    #print('cur time: ' + str(current_time))
    #print('end time: ' + str(end_time))
    while current_time <= end_time:
        frame = np.array(cap)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        out.write(frame)
        
        if kb.is_pressed('f8'):
            out.release()
            shutil.copyfile(str(filename + enc_ext), str('replay_' + str(time.strftime("%Y-%m-%d_%H%M%S", named_tuple)) + enc_ext))
            return reload()
        if kb.is_pressed('f9'): #panic key
            exit()
    return reload()
main()
