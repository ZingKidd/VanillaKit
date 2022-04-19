VERSION = 0.001
import subprocess
import socket
from os import remove
from sys import argv
import os
from time import sleep
import webbrowser
import platform
import requests as r
from bs4 import BeautifulSoup



YES = ['y', 'Y', 'YES', 'yes', 'Yes']

NO = ['n', 'N', 'NO', 'no', 'No']

github_url = 'https://github.com/ZingKidd/Vanilla/blob/main/main.py'

DRIVES = ["A:\\", "B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\","S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]

different_extensions = ['.txt', '.docx', '.pdf', '.jpg', '.png', '.jpeg', '.mp4']

def print_os():
    print("OS in my system : ",platform.system())

def return_os():
    return platform.system()

def self_delete():
    remove(argv[0])

def find_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def search_drive_by_extension(drive, extension):
    file_paths = []
    for root, dirs, files in os.walk(drive):
        for file in files:
            file_path, file_ext = os.path.splitext(root+'\\'+file)
            if file_ext in extension:
                file_paths.append(root+'\\'+file)
    for f in file_paths:
        print(f)

def rick_roll():
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    webbrowser.open(url)

def show_alive_drives(drives = DRIVES):
    for drive in drives:
        if os.path.exists(drive):
            print(f"Drive {drive} Does exist")

def check_alive_drives(drives = DRIVES):
    for drive in drives:
        if os.path.exists(drive):
            print(f"Drive {drive} Does exist")
            #sleep(5)
            # locate_drives(drive)
        else:
            print(f"Drive {drive} does not exist")

def check_for_update(github_url):
    html_text = r.get(github_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    latest_versions_location = soup.find_all('span', {"class":"pl-c1"})
    # print(searchfor[1])
    for i in latest_versions_location[1]:
        latest_version = float(i)
        # print(latest_version)
        if VERSION < latest_version:
            print('There is an available Update')
            update()
        else:
            print('You are fine!')

def update():
    update_option = input('Would you like to Update Vanilla? [y/N] ')
    if update_option in YES:
        print('Updating . . .')
        # os.system()
    elif update_option in NO:
        return
    else:
        print('Something went wrong...')
        update()

def banner():
    pass

def rotate_screen():
    pass

def chrome_history():
    pass