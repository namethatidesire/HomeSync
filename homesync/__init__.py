# homesync/__init__.py

"""
HomeSync Package

Client-side logic for file syncing with a home server (e.g. homelab or personal NAS).
"""

__version__ = "0.1.0"
__author__ = "namethatidesire"

from . import cli
from . import config
from . import metadata
from . import network_check
from . import sync
from . import utils

def run():
    cli.main()
