# Wuxiaworld-2-eBook
This Python script will download chapters from novels availaible on wuxiaworld.com and saves them into the .epub format.

## Getting Started

To run this script you'll need to have Python 3.6.x installed which you can find [here](https://www.python.org/downloads/ "Python Download Link").

### Features

- Download and save you favorite Novels from wuxiaworld.com into a .epub file
- Automatically adds some metadata like author, title and cover

### Prerequisites

As mentioned before this script was written for Python version 3.6.x. It may work with other versions too but none are tested.
Additionally the Python image library (Pillow) and Beautifulsoup4 are required.
To install all dependencies just use the console to navigate into the project folder and write

```
pip install -r requirements.txt
```

### Usage

Download the script and navigate to the folder using the console then write

```
python wuxiaworld2ebook.py
```

or just use the start.bat file. If you didn't add Python to the PATH variable during the installation or afterwards the write

```
path/where/you/installed/python.exe wuxiaworld2ebook.py
```

After that just select the novel you want to read, enter the chapter range you want to include to the eBook, enter the book number of the novel you want to read (if applicable) and hit the "Generate" Button. Keep it mind that it will take some time for the script to finish, so don't close the window or the console if the program doesn't respond.

## Keep in mind!

If you have troube with missing text in some Novels use [the legacy console application](https://github.com/MrHaCkEr/Wuxiaworld-2-eBook/tree/legacy-console-application). This script scrapes differently and could resolve problems.

If you come across bug's or suggestion's for future updates don't hesitate to open up a "new Issue" in the issue tab or write me a e-mail at bloodvioletssword@gmail.com.

Novels that are not included and won't be included in the near future:

- Charm of Soul Pets
- Demon Hunter
- Heavenly Jewel Change
- I Reincarnated for Nothing
- Red Storm
- Terror Infinity
- Unrivaled Tang Sect


### Planned feature's and updates

- Improved Cover Editing

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone on stackexchange who helped me in my most dire times

## Want to support a poor student?

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=U7KDYY9UB9PMY)
