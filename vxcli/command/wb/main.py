#!/usr/bin/env python3
# wb
# Command for running the WindRiver Workbench.

######################
# Imports & Globals
######################

import argparse
import subprocess
import os
from vxcli import IPopen

# Global variables
HELP = "WindRiver Workbench"


######################
# Init Parser
######################

def init_parser(subparser):
    pass


######################
# run
######################

def run(other_args):
    _ip = IPopen.IPopen()

    _ip.run([
            os.environ["WIND_WRWB_PATH"] + "/wrwb",
        ]
        + other_args
    )
