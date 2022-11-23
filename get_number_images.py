from unet import UNet
from torch.utils.data import random_split
import torch
import torchvision
import torchvision.transforms as transforms
import pathlib
import os
 
path = pathlib.Path('Data')

data_dir = os.listdir(path)

increment = 0


for classes in data_dir:
    subfolder = os.path.join(path, classes)
    subfolder_dir = os.listdir(subfolder)
    #print(subfolder)
    for files in subfolder_dir:
        classes = os.path.join(subfolder, files)
        increment += 1

train_size = increment*0.8
test_size = increment*0.2
total_size = train_size + test_size
print(train_size)
print(test_size)
print(total_size)
