from unet import UNet
import pathlib

import os
 
path = pathlib.Path('Data')

data_dir = os.listdir(path)

def create_tataset():
    
