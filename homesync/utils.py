# homesync/utils.py

import os, shutil, time
from pathlib import Path

# TODO: allow user to decide the following from config file
BACKUP_DIR = Path("homesync/backups")
MAX_NUM_BACKUPS = 3

def backup_local_file(file_path, conflict=False):
	# TODO
	return

def clean_old_backups():
	# TODO
	return
