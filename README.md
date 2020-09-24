# Prerequisites

[Install docker](https://docs.docker.com/get-docker/).

# Build

`make` will build the docker image.

# Use

Put the images you wish to transform into work_dir; this directory is mounted in docker so the application can access it. There is one example png already in the repository, so you can try it out with:

`./png_edit.py example.png example_out.png`

This outputs some stuff about pixel values and generates a cyanized example_out.png for your viewing pleasure.

