#!/usr/bin/env python3
# sim
# Command for running the simulator.

######################
# Imports & Globals
######################

import argparse
import subprocess
import os
from vxcli import IPopen

# Global variables
HELP = "VxWorks simulator"


######################
# Init Parser
######################

def init_parser(subparser):
    # Used options
    subparser.add_argument("-d", "-device",
        metavar = "<boot device>",
        dest = "device",
        help = "Type of device to boot from (default: simnet_nat, supported: passDev, simnet, simnet_nat)",
        type = str,
        choices = ["passDev", "simnet", "simnet_nat"],
        default = "simnet_nat",
    )

    subparser.add_argument("-f", "-file",
        metavar = "<file name>",
        dest = "file",
        help = "VxWorks 7 core file to load (default: vxWorks or os.environ[\"KERNEL_IMAGE\"] if set)",
        type = str,
        default = os.environ.get("KERNEL_IMAGE", "vxWorks"),
    )


######################
# run
######################

def run(device, file, other_args):
    _ip = IPopen.IPopen()

    _ip.run([
            os.environ["WIND_HOME"] + "/vxworks/" + os.environ["WIND_RELEASE_ID"] + "/host/" + os.environ["WIND_HOST_TYPE"] + "/bin/vxsim-64",
        ]
        + ["-f", file]
        + ["-d", device]
        + other_args
    )
