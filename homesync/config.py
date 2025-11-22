# homesync/config.py

import json
from pathlib import Path

CONFIG_PATH = Path.home() / "homesync" / ".config.json"
CONFIG_DEFAULT = {
	"server_type": "mapped",
	"server_path": "\\\\[replace]\\[me]",
	"ssh_user": "",
	"ssh_host": "",
	"ssh_port": 22,
	"local_sync_path": str(Path.home() / "homesync" / "HomeSync_data"),
	"metadata_path": str(Path.home() / "homesync" / "metadata.json")
}
