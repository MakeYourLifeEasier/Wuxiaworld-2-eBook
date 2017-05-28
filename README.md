# Wuxiaworld-2-eBook
This Python script will download chapters from novels availaible on wuxiaworld.com and saves them into the .epub format.

## Getting Started

To run this script you'll need to have Python 3.6.1 install which you can find [here](https://www.python.org/downloads/ "Python Download Link").
Or you can just donwload the standalone executable which you can find [here](https://github.com/MrHaCkEr/Wuxiaworld-2-eBook/releases "GitHub releases 1.2").

### Features

- Download and save you favorite Novels from wuxiaworld.com into a .epub file
- Automatically adds some metadata like author, title and series names

### Prerequisites

As mentioned before this script was written for Python version 3.6.1. It may work with other versions too but none are tested.
There are no dependencies required to run this script.

### Usage

If you downloaded the executable just start it.
Else download the script and navigate to the folder using the console then write

```
python wuxiaworld2ebook.py
```

if you didn't add Python to the PATH variable during the installation or afterwards the write

```
path/where/you/installed/python.exe wuxiaworld2ebook.py
```

then you shoud see all the available Novels thet are supported (which are almost all). Then just enter the number which is assigned to the novel you want to read.
Afterwards the program will ask for the starting chapter and the end chapter. Just enter the chapters you want and hit enter.
Now it should download the chapters you wanted and will save them into an .epub file that is located in the folder the script or executable is located in.

## Keep in mind!

This script could be buggy since the core of the code was never build for a public release. Although the code works as far as I know there a a lot of small bugs that I have yet to fix. If you come across some of them feel free to let me know so I have a general idea what is still necesarry to fix.

### ToDo list

- Fix table of contents
- Add missing Novels

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone on stackexchange who helped me in my most dire times

## Want to support a poor student?

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=U7KDYY9UB9PMY)
