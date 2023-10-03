#!/usr/bin/env python3
# upload
# Command for uploading a binary to a target device.

######################
# Imports & Globals
######################

import argparse
import subprocess
import os
import sys
from vxcli import IPopen

# Global variables
HELP = "Binary uploader"


######################
# Init Parser
######################

def init_parser(subparser):
    # Used options
    subparser.add_argument("filename",
        metavar = "<file name>",
        help = "binary file to upload",
        type = str,
    )

    subparser.add_argument("--host",
        metavar = "<hostname>",
        dest = "host",
        help = "IP address or hostname of the target device (default: localhost or os.environ[\"TARGET_HOST\"] is set)",
        type = str,
        default = os.environ.get("TARGET_HOST", "localhost"),
    )

    subparser.add_argument("--port",
        metavar = "<port>",
        dest = "port",
        help = "port used for communication with the device (default: 1534 or os.environ[\"TARGET_PORT\"] is set)",
        type = int,
        default = os.environ.get("TARGET_PORT", 1534),
    )

    subparser.add_argument("--kernel",
        metavar = "<file name>",
        dest = "kernel",
        help = "VxWorks 7 core file to load (default: vxWorks or os.environ[\"KERNEL_IMAGE\"] if set)",
        type = str,
        default = os.environ.get("KERNEL_IMAGE", "vxWorks"),
    )


######################
# run
######################

def run(host, port, kernel, filename, other_args):
    _ip = IPopen.IPopen()

    if port == 1534:
        sys.stderr.write("WARNING: Using default port '1534'. This won't work for the simulator as you have to specify the remapped port.\n")

    _ip.run([
            os.environ["WIND_WB_HOSTTOOLS"] + "/bin/wrpython",
            "-u",
            os.environ["WIND_WB_HOSTTOOLS"] + "/lib/python/windriver/shells/WrDbg.py"
        ]
        + [
            "--eval-command", "target connect vxworks7:%s:%d -kernel %s" % (host, port, kernel),
            "--eval-command", "module load %s" % filename,
            "--eval-command", "quit",
        ]
        + other_args
    )
