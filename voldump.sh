#!/bin/bash

## VolDump
## Volatility mass collection tool
## USAGE
### Run VolDump.sh in folder with memory images.
### Output will be named per image, with child folders.
## Last Updated 2023-04-17

function main () {
    echo "----------- VOLDUMP ------------"
    echo "--- Last Updated 2023-04-17 ----"
    scanImages
}

function scanImages () {
    echo "Scanning disk images..."
    shopt -s nullglob
	images=(*.dmp)
    echo "Found ${#images[@]} image(s)"
	for img in "${images[@]}"; do
		echo "- $img"
	done
}

main