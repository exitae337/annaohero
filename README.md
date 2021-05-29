# annaohero

**annaohero** - this module is a Python library for building multiple files into one file and vice versa

## Installation

Install the current version with PyPI:

```python
pip install annaohero
```

## Usage

Files into one file and and vice versa

To combine the files into a single file, use the command:

compress(r"(path to the file folder with your files)") example: compress(r'C:\Users\username\Desktop\folder')

```python
compress(r'C:\Users\username\Desktop\folder')
```
After you have entered this command, the "sop.nosh" file will be created. This is the source file with your files!

To separate the files you should use the following command:

uncompress(r'(way to folder with file "sop.nosh")') example: uncompress(r'C:\Users\username\Desktop\folder') The folder must contain the file that you created with the compress() command!

```python
uncompress(r'C:\Users\username\Desktop\folderwithsopnosh')
```

##Example

```python
from annaohero import compress, uncompress

pathtofiles = r'C:\Users\username\Desktop\folder'
compress(pathtofiles)

pathtofilewithsop = r'C:\Users\username\Desktop\folderwithsopnosh'
uncompress(pathtofilewithsop)

```

## Contributing

Bug reports and/or pull requests are welcome