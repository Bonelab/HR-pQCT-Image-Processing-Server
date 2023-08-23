"""
constants.py
Author: Ian Smith
Module to hold needed constants for this program
"""

# Important Directories
DEST = 'destination'
BATCHES = 'batches'
DEL = 'del'
FAILED = 'failed'
DONE = 'processed'
REC = 'rec'
TMP = 'tmp'
DIRS = [BATCHES, DEL, DEST, FAILED, DONE, REC, TMP]
JOB_DIRS = [BATCHES, DEST, DONE, FAILED]


# Time before a file gets deleted in days
TIME_TO_DELETE = 7


# Important Values from COM file
DATE = "DATE"
F_NAME = "EVAL_FNAME"
TARGET_IMAGE = "TARGET_FILE"
EXT = "FEXT"


# Socket details for communicating from CLI to daemon
ip_addr = "127.0.0.1"
port = 4000
ADDR = (ip_addr, port)


# Log Locations
DEBUG = "/home/bonelab/bls/logs/debug.log"
ERROR = "/home/bonelab/bls/logs/error.log"

# Model setup parameters
RAD_TIB_PATH_TO_ENV = "/home/bonelab/.conda/envs/bl_torch/bin/python"
RAD_TIB_PATH_TO_START = "/home/bonelab/repos/Bonelab/HR-pQCT-Segmentation/segment.py"
RAD_TIB_TRAINED_MODELS = "radius_tibia_final"

