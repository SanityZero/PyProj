import pyautogui as pag
from pywinauto.keyboard import send_keys
import sys
#import cv2
#import pytesseract
directory_name = r"C:/ProgStaff/PyProj/venv/screen_parts/tl_chat/"

def im_on_scr(im_name):
    r = pag.locateOnScreen(im_name, confidence=0.90)
    if r is None:
        return False
    return True

class PagRegion:
    def __init__(self, reg_box=(0,0,0,0)):
        self.box = reg_box

    def set(self, pic_names, mod='both'):
        if mod == 'tl':
            pass
        elif mod == 'br':
            pass
        elif mod == 'both':
            pass
        else:
            pass

    def locate(self):
        return pyautogui.screenshot(region=self.box)

screen_size = pag.size()
lt_guad = [0,0,screen_size.width/2,screen_size.height/2]
rt_guad = [screen_size.width/2,0,screen_size.width/2,screen_size.height/2]
lb_guad = (0,0,screen_size.width/2,screen_size.height/2)
rb_guad = (screen_size.width/2,screen_size.height/2,screen_size.width/2,screen_size.height/2)

l_reg = (0,0,screen_size.width/2,screen_size.height)
r_reg = (screen_size.width/2,0,screen_size.width/2,screen_size.height)
t_reg = (0,0,screen_size.width,screen_size.height/2)
b_reg = (0,screen_size.height/2,screen_size.width,screen_size.height/2)

#im = pyautogui.screenshot(region=(0,0, 300, 400))

def open_tl():
    r = None
    while r is None:
        r = pag.locateOnScreen(directory_name+'bar_tl_icon.bmp', confidence=0.90)
        if r is None:
            r = pag.locateOnScreen(directory_name+'bar_tl_icon_gotm.bmp', confidence=0.90)
        if r is not None:
            pag.moveTo(r)
            pag.click()

def open_groupe():
    r = None
    while r is None:
        r = pag.locateOnScreen(directory_name+'tl_group_contacts_ua.bmp', confidence=0.90)
        if r is None:
            r = pag.locateOnScreen(directory_name+'tl_group_contacts_a.bmp', confidence=0.90)
        if r is not None:
            pag.moveTo(r)
            pag.click()

def open_dialog(dialog_name):
    search(dialog_name)

def write_mess(message_in_arr):
    r = None
    while r is None:
        r = pag.locateOnScreen(directory_name + 'tl_write_here.bmp', confidence=0.90)
        if r is not None:
            pag.moveTo(r)
            pag.move(50, -10)
            pag.click()
            pag.move(100, -100)
            for mess in message_in_arr:
                #f_mess = mess.replace('\n', '{SHIFT down}{ENTER}{SHIFT up}')
                f_mess = r'D:{SPACE}{SPACE}'+ mess.replace(' ', '{SPACE}') + '{ENTER}'
                send_keys(f_mess, pause=0.05)

def search(mess):
    f_mess = mess.replace(' ', '{SPACE}') + '{ENTER}'
    r = None
    while r is None:
        r = pag.locateOnScreen(directory_name + 'tl_search.bmp', confidence=0.90)
        if r is not None:
            pag.moveTo(r)
            pag.click()
            send_keys(f_mess, pause=0.05)

mess_arr = ['dsffs','awadaw']
open_tl()
search('Saved')
#write_mess(['''Теперь оно может писать в две строки?'''])
write_mess(mess_arr)