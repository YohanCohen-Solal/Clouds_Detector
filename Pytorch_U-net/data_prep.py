import os
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg


def getPathToImage(image):
    imagePath = os.path.join("./clouds_Detector/Data/", image)
    return imagePath

def countImagesOfType(image):
    path_dir = getPathToImage(image)
    lst = os.listdir(path_dir) # your directory path
    number_files = len(lst)
    return number_files

def convertSvgToPng(image):
    for images in os.listdir(getPathToImage(image)):
        if images.endswith(".svg"):
            img = svg2rlg(os.path.join(getPathToImage(image), images))
            renderPM.drawToFile(img, os.path.join(getPathToImage(image), images + ".png"), fmt='PNG')
    return print("Images from {} converted",format(image))

def cleaningData(image):
    for images in os.listdir(getPathToImage(image)):
        if images.endswith(".svg"):
            os.remove(os.path.join(getPathToImage(image), images))
    return print("Images from {} cleaned", format(image))

