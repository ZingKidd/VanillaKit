import socket
from os import remove
from sys import argv
import os
import webbrowser
import platform

#import rotatescreen
# def rotate_screen():
#     rotate_screen  = rotatescreen.get_primary_display()
#     rotate_screen.set_landscape_flipped()

VERSION = 0.01

drives = ["A:\\", "B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\","S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]

different_extensions = ['.txt', '.docx', '.pdf', '.jpg', '.png', '.jpeg', '.mp4']

def print_os():
    print("OS in my system : ",platform.system())

def return_os():
    return platform.system()

def self_delete():
    remove(argv[0])

def find_ip(hostname):
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

def show_alive_drives(drives):
    for drive in drives:
        if os.path.exists(drive):
            print(f"Drive {drive} Does exist")

def check_alive_drives(drives):
    for drive in drives:
        if os.path.exists(drive):
            print(f"Drive {drive} Does exist")
            #sleep(5)
            # locate_drives(drive)
        else:
            print(f"Drive {drive} does not exist")

def chrome_history():
    pass

def update():
    pass