#!/usr/bin/env python3
# compile
# Command for compiling the source code.

######################
# Imports & Globals
######################

import argparse
import subprocess
import os
from vxcli import IPopen

# Global variables
HELP = "wr-cc compiler"


######################
# Init Parser
######################

def init_parser(subparser):
    subparser.description = """
wr-cc compiler for VxWorks.

For DKM use:
$ vxcli compile -g -dkm <source files> -o <outfile>

For RTP use:
$ vxcli compile -g -rtp <source files> -static -o <outfile>
"""

    subparser.add_argument("--vsb",
        metavar = "<path to vsb>",
        dest = "vsb",
        help = "Path to the VxWorks Source Build used for the compiation (default: vsb_vxsim_linux or os.environ[\"WIND_CC_SYSROOT\"] if set)",
        type = str,
        default = os.environ.get("WIND_CC_SYSROOT", os.environ.get("WIND_BASE") + "/samples/prebuilt_projects/vsb_vxsim_linux"),
    )


######################
# run
######################

def run(vsb, other_args):
    os.environ["WIND_CC_SYSROOT"] = vsb

    _ip = IPopen.IPopen()

    _ip.run([
            os.environ["WIND_BASE"] + "/host/x86_64-linux/bin/wr-cc",
        ]
        + [ "--help" if "-help" else arg for arg in other_args ] # Their help is broken.
    )
