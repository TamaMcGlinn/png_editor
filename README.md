# Prerequisites

[Install docker](https://docs.docker.com/get-docker/).

# Clone

Clone this repository and update the submodules:

```
git clone git@github.com:TamaMcGlinn/png_editor.git
cd png_editor
git submodule update --init --recursive
```

# Build

`make` will build the docker image.

# Use

There is one example png already in the repository, so you can try it out with:

```
cd work_dir
../png_edit.py example.png example_out.png`
```

This outputs some stuff about pixel values and generates a cyanized example_out.png for your viewing pleasure.

If you add the directory of png_edit.py to your PATH, you can run it from anywhere. Note that you cannot pass in images above the current directory; this is because your working directory is mounted in docker for read/write access prior to running the C++ program:

```
png_edit.py ../something.png ../something_out.png   <-- you can't do this
```
