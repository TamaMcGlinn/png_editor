#!/usr/bin/env python3
import sys

MIN_PYTHON = (3, 7)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='convert a png')
parser.add_argument('input_image', type=str, help='the input image')
parser.add_argument('output_image', type=str, help='the output image')
args = parser.parse_args()

PWD = os.getcwd()
subprocess.run(['docker', 'run', '--rm', '-v', f'{PWD}:/opt/application/work_dir', 'png_edit', '../test-libpng', args.input_image, args.output_image])

