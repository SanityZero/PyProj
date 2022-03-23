# This is a sample Python script.
import cv2
import pyautogui as pag
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageGrab
import requests
import json
# print("GeeksForGeeks")
# print("Your OpenCV version is: " + cv2.__version__)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

directory_name = "C:/ProgStaff/img/demon/"


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    r = None
    while r is None:
        r = pag.locateOnScreen(directory_name+'chat_invitation.bmp', confidence=0.99)
        if r is not None:
            pag.moveTo(r)
            pag.move(12, -3)
            pag.click()
            pag.write("Hello Master.\nM:", interval=0.05)
            pag.move(100, 0)


def readCommand():
    r = None
    while r is None:
        r = pag.locateOnScreen(directory_name + 'master_talk.bmp', confidence=0.99)
        if r is not None:
            pag.moveTo(r)
            pag.move(12, -3)
            pag.click()
            pag.write("Hello Master.\nM:", interval=0.05)
            pag.move(100, 0)


def saveScreenShot():
    while True:
        image_number = 0
        im = ImageGrab.grabclipboard()
        if im is not None:
            im.save(str(image_number)+'.png', 'PNG')
            image_number += 1


def vk_get_friends(id):
    r = vk_post('friends.get?user_id='+str(id)+'&').json()
    print(r['response']['items'])
    #r = vk_post('users.getFollowers?user_id=280114732&counters').json()
    friend_list = r['response']['items']
    for friend_id in friend_list:
        print(vk_post('users.get?user_ids='+str(friend_id)+'&').json())


# pag.screenshot("screen.png")
# image = cv2.imread("screen.png")
# plt.imshow(image)
# string = pytesseract.image_to_string(image)
# печатаем
# print(string)
# https://oauth.vk.com/authorize?client_id=8006328&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=offline&response_type=token&v=5.52
# https://oauth.vk.com/blank.html#access_token=8c92724a9d731b8dc8d399ce62ed18216893093f1daada904ab4485f140f3cfe289d935f9601840b725d6&expires_in=0&user_id=567355115
lamer_token = '8c92724a9d731b8dc8d399ce62ed18216893093f1daada904ab4485f140f3cfe289d935f9601840b725d6'


def vk_post(text, access_token='access_token=5204427a5204427a5204427a18527e68c2552045204427a339e47283e16e525c67d066d', vk_api_version='&v=5.131'):
    http = requests.Session()
    return http.post('https://api.vk.com/method/'+text+access_token+vk_api_version)
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    r = vk_post('messages.getHistory?&', access_token=lamer_token).json()
    print(r)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
