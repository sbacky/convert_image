# **Image-Converter**
The purpose of this script is to be able to reformat, rotate or resize images to the correct format, orientation and, size. And, id desired, have the newly processed images be saved to a directory passed as a parameter. This will be accomplished by using the **Python Imaging Library (PIL)** to modify and resave the images.

## <a name="head1"></a>**Contents**
* [Planning](#head2)
* [Variables](#head3)


## <a name="head2"></a>**Planning**
The script has to take the directory containing the images as a parameter and go through each image in the directory, converting them to the correct format, orientation and, size. Once converted, the images need to be saved to the same directory they were in or to a new directory that would be passed as a parameter as well.

Image module from the PIL library should provide the necessary functions to process the images correctly. In order to use this script, you will have to install the PIL library. To install the PIL library on your device, use:
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
Variables should be passed as one parameter in the shell as: **converter.py "dir|newDir|size|rotate|ext"**. There should be no spaces between "|"s and the variables being passed to ensure they get split properly. It is also important to pass the variables in the order they appear so they get saved to the correct variables in the script. If you do not want to change a parameter on the image in question, then leave it blank when entering the parameters.

For example, if you want to keep the same size and format of an image but, want to rotate and save the rotated image to a different directory then the one it is currently in, enter the parameters like so:
```
converter.py "/path/to/images|/path/to/rotatedImages||90|"
```

Or if you want to keep the image size, orientation and within the same directory, and only change the image format to 'jpg', enter the parameters like so:
```
converter.py "/path/to/images||||jpg"
```

[dir](#head31)|[newDir](#head31)|[size](#head32)|[rotate](#head33)|[extension](#head34)

Back to [Contents](#head1)

### <a name="head31"></a>dir and newDir
dir and newDir should both be valid directories. The variable dir is the directory that currently has the images you wish to process. This is the only mandatory parameter to run the script. The variable newDir, if passed, is the directory you wish to save the new processed images to. If a new directory is not passed then the script will save the processed images to the directory passed as dir. Error status codes of 1, 10, 11, and 101 are linked to directory issues.

Example Directories:
```
WindowsOS ---> C:\\foo\\bar\\foobar
MacOS, Linux ---> /foo/bar/foobar
```

Back to [Variables](#head3)

### <a name="head32"></a>size
The size parameter, if passed, resizes the image to the dimensions passed. Desired size of the image should be passed as number1,number2. The number1 and number2 should represent the 'width' x 'height' of the desired size of the image. Both the values number1 and number2 have to be integers. They will be split by using .split(",") and saved as a tuple. Error status codes of 20, 21, 22, and 23 are linked to size related issues.

Example size 640 x 480:
```
number1,number2 ---> 'width' x 'height'
640,480 ---> 640 x 480
```

Back to [Variables](#head3)

### <a name="head33"></a>rotate
The rotate parameter, if passed, rotates the image by the given number of degrees **counter clockwise** around its center. The value for rotate has to be an integer greater than or equal to zero and less than three-hundred and sixty. If the rotate parameter is not passed, rotate defaults to zero degrees, thus not rotating the image. Error status codes of 30 and 31 are linked to rotate parameter related issues.

Example rotate 90 degrees clockwise:
```
rotate ---> degrees
270 ---> 270 degrees
```

Back to [Variables](#head3)

### <a name="head34"></a>extension
The extension parameter, if passed, formats the image to the value of the extension. The value for extension has to be a string and cannot contain a period (.). If the extension parameter is not passed, the extension value defaults to the current format of the image. Error status codes of 40 and 41 are linked to extension related issues.

Example extension png:
```
extension ---> format
png ---> .PNG
```

Back to [Variables](#head3)

Back to [Contents](#head1)
