#!/usr/bin/env python3
from re import T
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api as winapi
import win32con as wincon
import cv2
from PIL import ImageGrab

def click(x, y):
    winapi.SetCursorPos((x,y))
    winapi.mouse_event(wincon.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    winapi.mouse_event(wincon.MOUSEEVENTF_LEFTUP, 0, 0)

def pause():
    pause_location = pyautogui.locateOnScreen('pause.png', grayscale=True, confidence=0.9)
    if(pause_location is not None):
        pause_location = pyautogui.center(pause_location)
        click(pause_location[0], pause_location[1])
        while(keyboard.is_pressed('p')) == False:
            continue
        
        winapi.SetCursorPos((0,0))
        time.sleep(1)

        resume_location = pyautogui.locateOnScreen('resume.png', grayscale=True, confidence=0.9)
        if(resume_location is not None):
            resume_location = pyautogui.center(resume_location)
            click(resume_location[0], resume_location[1])
        else:
            return False
        
    return True



def main():
    bar_location = pyautogui.locateOnScreen('bar.png', grayscale=True, confidence=0.9)
    if(bar_location is None):
        bar_location = (0,0)

    while(keyboard.is_pressed('q')) == False:
        if(keyboard.is_pressed('p')):
            if(pause() == False):
                print("Unable to resume")
                exit()      

        ball_location = pyautogui.locateOnScreen('ball.png', grayscale=True, confidence=0.7)
        if(ball_location is not None):
            ball_location = pyautogui.center(ball_location)
            if(bar_location == (0, 0)):
                winapi.SetCursorPos(ball_location)
            else:
                winapi.SetCursorPos((ball_location[0], bar_location[1]))

        time.sleep(0.01)



if __name__ == "__main__":
    print("Press q to start/end the program")
    while(keyboard.is_pressed('q')) == False:
        continue

    print("Program starting\nPress \'p\' for pausing the bot or \'q\' to end it")
    time.sleep(2)
    main()

print("Program ended")