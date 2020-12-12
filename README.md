# **Image-Converter**
The purpose of this script is to reformat, rotate and, resize images to the correct format, orientation and, size. This will be accomplished by using the **Python Imaging Library (PIL)** to modify and resave the images.

## <a name="head1"></a>**Contents**
* [Planning](#head2)
* [Variables](#head3)


## <a name="head2"></a>**Planning**
The script has to take the directory containing the images as a parameter and go through each image in the directory, converting them to the correct format, orientation and, size. Once converted, the images need to be saved to the directory for finished images.

Image module from the PIL library should provide the necessary functions to process the images correctly. To install the PIL library on your device, use:
```
MacOSX, WindowsOS ---> pip3 install pillow
Linux distr. ---> sudo apt install python3-pil
```

To import the Image module from the PIL library:
```python
from PIL import Image
```

To resize an image using Image:
```python
from PIL import Image
im = Image.open("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")
```

To rotate an image using Image:
```python
from PIL import Image
im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")
```

Pass parameters as a system environment variable and use sys.argv(1).split("|") to catch them, then split and save them into separate variables. The variables that are going to be used are: dir, newDir, size, rotate, extension. Make sure to import system module first.
```python
import sys
dir, newDir, size, rotate, extension = sys.argv[1].split("|")
```

Back to [Contents](#head1)

## <a name="head3"></a>**Variables**
Variables should be passed as one parameter in the shell as: **converter.py "dir|newDir|size|rotate|ext"**. There should be no spaces between "|"s and the variables to ensure they get split properly. It is also important to pass the variables in the order they appear so they get saved to the correct variables in the script.

[dir](#head31)|[newDir](#head31)|[size](#head32)|[rotate](#head33)|[ext](#head34)

Back to [Contents](#head1)

### <a name="head31"></a>dir and newDir
dir and newDir should both be directories. dir is the directory that currently has the images you wish to process. newDir is the directory you wish to save the new processed images to. Error status codes of 1, 10, 11, and 101 are linked to directory issues. Status codes of 1 and 101 can be linked to directory issues but can also be related to size issues [(see below)](#head32).

Example Directories:
```
WindowsOS ---> C:\\foo\\bar\\foobar
MacOS, Linux ---> /foo/bar/foobar
```
Back to [Contents](#head1)

### <a name="head32"></a>size
Desired size of the image should be passed as number1,number2. The number1 and number2 should represent the 'width' x 'height' of the desired size of the image. They will be split by using .split(",") and saved as a tuple. Error status codes of 1, 20, 21, and 101 are linked to size related issues. Status codes of 1 and 101 can be linked to size issues but can also be related to directory issues [(see above)](#head31).

Example size:
```
number1,number2 ---> 'width' x 'height'
640,480 ---> 640 x 480
```
Back to [Contents](#head1)

### <a name="head33"></a>rotate


Back to [Contents](#head1)

### <a name="head34"></a>ext


Back to [Contents](#head1)
