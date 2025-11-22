# homesync/cli.py

import argparse
from . import network_check, sync, metadata

def main():
    # supported arguments to be parsed
    parser = argparse.ArgumentParser(description="HomeSync – Sync files and directories with your home server.")
    parser.add_argument("--sync", action="store_true", help="Run startup/manual sync")
    parser.add_argument("--status", action="store_true", help="Show last sync status")
    parser.add_argument("--help", action="store_true", help="Display a list of available commands")
    
    args = parser.parse_args()

    # ensure server is accessible
    if not network_check.server_accessible():
        print("ERROR ⚠️: Cannot reach server. Check if the server is on and that SSH or mapped network drive is configured correctly.")
        return

    # --status
    if args.status:
        metadata.show_status()
        return

    # --sync
    if args.sync:
        print("Syncing files...")
        # TODO: error checking (e.g. server inaccesible during sync)
        sync.sync_files()
        print("Sync complete. ✅")
        return
    
    # --help
    if args.help:
        # TODO: implement help script
        return

    parser.print_help()

if __name__ == "__main__":
    main()
