# WiFi Password Extractor

This Python script extracts WiFi SSIDs and their corresponding passwords from Windows using the `netsh` command. It scans XML files in the current directory, typically containing WiFi profiles, extracts SSIDs and passwords, and saves them to a file named `passwords.txt`.

## Prerequisites

- Python 3.x
- Windows operating system

## Usage

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script by executing the following command:

```
python3 wifi_password_extractor.py
```

## Description

The script performs the following steps:

1. Creates a file named `passwords.txt` to store the extracted passwords.
2. Executes the `netsh wlan export profile key=clear` command to obtain WiFi profiles with clear text passwords.
3. Iterates through XML files in the current directory, searching for files starting with "Wi-Fi" and ending with ".xml".
4. Extracts SSIDs and passwords from the XML files.
5. Writes the SSIDs and passwords to the `passwords.txt` file.

**Note:** The script may require administrative privileges to execute the `netsh` command.

## Output

The extracted WiFi SSIDs and passwords are saved in the `passwords.txt` file in the following format:

```
Passwords Found Below!

SSID: <WiFi SSID>
Password: <WiFi Password>

...
```

## Disclaimer

This script is intended for educational and research purposes only. Use it responsibly and ensure you have proper authorization before extracting passwords from any system.
