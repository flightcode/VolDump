#!/usr/bin/env python3

## VolDump.py
## Volatility mass collection tool
## USAGE
### Run VolDump.py in folder with memory images.
### Output will be named per image, with child folders.
## Last Updated 2023-04-17

import os

def main():
    print("----------- VOLDUMP ------------")
    print("--- Last Updated 2023-04-17 ----")
    scanImages()

def scanImages():
    print("Scanning disk images...")
    images = [each for each in os.listdir(".") if each.endswith('.dmp')]
    print(f"Found {len(images)} image(s)")
    for image in images:
        print(f"- {image}")

if __name__ == '__main__': main()