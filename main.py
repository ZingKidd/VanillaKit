VERSION = 0.0001
import subprocess
import socket
from os import remove
from sys import argv
import os
import re
from time import sleep
import webbrowser
import platform
import requests as r
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


YES = ['y', 'Y', 'YES', 'yes', 'Yes']

NO = ['n', 'N', 'NO', 'no', 'No']

URL = 'https://github.com/ZingKidd/VanillaKit/blob/main/main.py'

DRIVES = ["A:\\", "B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\","S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]

different_extensions = ['.txt', '.docx', '.pdf', '.jpg', '.png', '.jpeg', '.mp4']

def pop_message(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message)

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
    webbrowser.open_new_tab(url)

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

def check_for_update(github_url = URL):
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
            return

def check_for_update_V2(version = VERSION, github_url = URL):
    result = r.get(github_url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    tds = soup.find_all("td")
    for td in tds:
        if "VERSION" in td.text:
            for span in td:
                # print(span)
                for value in span:
                    latest_version = ""
                    for i in value:
                        if i.isdigit() or i == '.':
                            latest_version = latest_version + i
                    if latest_version != '':
                        latest_version = float(latest_version)
                        if version < latest_version:
                            print('There is an available Update')
                            update()
                            return

def get_latest_repo_version(version = VERSION, github_url = URL):
    result = r.get(github_url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    tds = soup.find_all("td")
    for td in tds:
        if "VERSION" in td.text:
            for span in td:
                # print(span)
                for value in span:
                    latest_version = ""
                    for i in value:
                        if i.isdigit() or i == '.':
                            latest_version = latest_version + i
                    if latest_version != '':
                        return float(latest_version)

def update():
    update_option = input('Would you like to Update Vanilla? [y/N] ')
    if update_option in YES:
        print('Updating . . .')
        # Does not work . . .
        os.chdir('..')
        subprocess.run(['rd', '-r', 'VanillaKit'], shell=True)
        subprocess.run(['git', 'clone', 'https://github.com/ZingKidd/VanillaKit.git'], shell=True)
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

check_for_update()



