# Wuxiaworld-2-eBook
This Python script will download chapters from novels availaible on wuxiaworld.com saves then into the .epub format.
Also read the Keep in mind part!

## Getting Started

To run this script you'll need to have Python 3.6.1 install which you can find [here](https://www.python.org/downloads/ "Python Download Link").
Or you can just donwload the standalone executable which you can find [here](https://drive.google.com/file/d/0B_b6PybP95z1Vm9samQtX3hGMG8/view?usp=sharing "Google Drive Standalone Link").

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

The table of contents generation doesn't work properly at the moment.
If you want to have a woking table of contents you will need to have calibre installed.
You need to add the file to calibre, then right click on the book and select "edit book" in the drop down menu.
Afterwards you should see a somewhat blue icon in the top taskbar where you can edit the table of contents.
There just select "Generate Table of Contends out of file names".
Then close the window and click save. Afterwards you should have a working table of contend.

### ToDo list

- Fix table of contends
- Add missing Novels

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone on stackexchange who helped me in my most dire times
