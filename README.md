# HomeSync
A basic and lightweight tool for syncing files between Windows devices via a home server/NAS.

This tool is intended to be used on your personal home network as a solution to syncing game saves and other files from handheld/portable devices and your main computer(s) (e.g. ROG Ally to Gaming Desktop).

This app only supports Windows.

## Requirements
- Python (3.10+ recommended; developed on 3.14.0)
- Access to the destination path on your personal server:
	1. Mapped network drive - ensure that the shared folder is mapped on your device.
	2. SSH/SFTP - the server has SSH enabled and you have the necessary credentials.

## Usage
There are two ways you can sync your files to a server on your home network:

1. Using a mapped network drive.
- See how to map a network drive in Windows.

2. Using ssh.