#!/usr/bin/env python3

import sys, os, subprocess
import xml.etree.ElementTree as ET

# Creating a file
with open("passwords.txt", "w") as password_file:
    password_file.write("Passwords Found Below! \n\n")


# Lists
wifi_files, wifi_name, wifi_password = []

# Executing Windows Command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

# Get current directory
path = os.getcwd()


for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)

        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    #wifi SSID
                    if "name" in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)

                    #SSID PASSWORD
                    if "keyMaterial" in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)

                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open("passwords.txt", "a")
                            print("SSID: " + x, " Password: " + y, sep="\n")
                            sys.stdout.close()