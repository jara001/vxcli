#!/usr/bin/env python3
# compile
# Command for compiling the source code.

######################
# Imports & Globals
######################

import argparse
import subprocess
import os
import sys
from vxcli import IPopen

# Global variables
HELP = "wr-cc compiler"
DKM_FLAGS = ["-dkm", "-g", "-o", "binary.out"]
RTP_FLAGS = ["-rtp", "-g", "-static", "-o", "binary.vxe"]


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

    subparser.add_argument("files",
        nargs = "+",
        help = "source files to be compiled",
        metavar = "<source file>",
    )

    subparser.add_argument("--dkm",
        dest = "dkm",
        help = "use usual flags for compiling the source files as DKM (set to: %s)" % " ".join(DKM_FLAGS),
        action = "store_true",
    )

    subparser.add_argument("--rtp",
        dest = "rtp",
        help = "use usual flags for compiling the source files as RTP (set to: %s)" % " ".join(RTP_FLAGS),
        action = "store_true",
    )


######################
# run
######################

def run(files, dkm, rtp, vsb, other_args):

    if dkm and rtp:
        print ("Unable to use two conflicting options '--dkm' and '--rtp'.", file = sys.stderr)
        exit (1)

    os.environ["WIND_CC_SYSROOT"] = vsb

    _ip = IPopen.IPopen()

    _ip.run([
            os.environ["WIND_BASE"] + "/host/x86_64-linux/bin/wr-cc",
        ]
        + (DKM_FLAGS if dkm else [])
        + (RTP_FLAGS if rtp else [])
        + files
        + [ "--help" if arg == "-help" else arg for arg in other_args ] # Their help is broken.
    )
