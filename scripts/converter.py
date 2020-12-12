#!/usr/bin/env python3

from PIL import Image
import os, sys

def oneByOne():
    cont = "n"
    while cont.lower().strip() != "y":
        cont = input("Would you like to continue to the next file? ['y'/'n'] ... ")

def convert(dir, newDir, size, rotate, extension):
    images = os.listdir(dir)

    for image in images:
        # Check for any files not wanting to be processed
        if image.startswith(".") or image.endswith(extension):
            continue
        # get old extension of images at ext
        fn, ext = image.split(".")
        # get new file name with extension
        newFn = fn + extension
        # Get full path to unprocessed image
        unPath = os.path.join(dir, image)
        # Get full path to processed image
        prPath = os.path.join(newDir, newFn)
        # create instance of image at path called im
        im = Image.open(unPath)
        im.rotate(rotate).resize(size).save(prPath)

        # Unhash to go through images one by one
        #oneByOne()

def main():
    dir, newDir, size, rotate, extension = sys.argv[1].split("|")

    try:
        os.path.isdir(dir)
        os.path.isdir(newDir)

        num1, num2 = size.split(",")
        size = (int(num1), int(num2))

        rotate = int(rotate)
    except TypeError:
        print("Please pass a directory to get started.")
        print("Invocation: converter.py dir|newDir|size|rotate|ext")
        sys.exit(1)
    except Exception as e:
        print("Please fix error in parameter format: {}".format(e))
        sys.exit(101)

    # Check to make sure dir and newDir exist
    if os.path.isdir(dir) != True:
        print("{} is not a vaid directory\nPlease pass a valid directory to get started".format(dir))
        sys.exit(10)
    if os.path.isdir(newDir) != True:
        print("{} is not a vaid directory\nPlease pass a valid directory to get started".format(newDir))
        sys.exit(11)

    # Check to ensure size is a tuple and that it is not empty
    if len(size) != 2 or type(size) != tuple:
        if type(size) != tuple:
            print("{} is not acceptable format\nPlease format size: |num1,num2|".format(size))
            sys.exit(20)
        print("size has length: {}\nPlease ensure size is a tuple formatted as: |num1,num2|".format(size))
        sys.exit(21)

    # Check to ensure rotate is an integer less than 360 or above 0
    if type(rotate) != int or rotate >= 360 or rotate <= 0:
        if type(rotate) != int:
            print("{} is not an integer\nPlease input an integer for rotation".format(rotate))
            sys.exit(30)
        print("{} is above 360 or below 0\nPlease input a rotation less than 360 or above 0".format(rotate))
        sys.exit(31)

    # Check to ensure extension is a string that begins with (.)
    if not extension.startswith(".") or type(extension) != str:
        if type(extension) != str:
            print("extension was type: {}\nPlease pass an extension of type str".format(extension))
            sys.exit(40)
        print("{} extension does not start with (.)\nPlease entr extension begining with (.)".format(extension))
        sys.exit(41)

    #convert(dir, newDir, size, rotate, extension)
    try:
        convert(dir, newDir, size, rotate, extension)
        sys.exit(0)
    except Exception as e:
        print("Error in convert(): {}".format(e))
        sys.exit(101)

if __name__ == "__main__":
    main()
