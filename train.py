from unet import UNet
from torch.utils import data
from torchvision import datasets, transforms

import numpy as np
import pathlib
import os
 
path = pathlib.Path('Data')
data_dir = os.listdir(path)

#creating datasets
dataset = datasets.ImageFolder(path, transform=transforms.ToTensor())
lengths = [int(np.ceil(0.8*len(dataset))),
           int(np.floor(0.2*len(dataset)))]
train_set, test_set = data.random_split(dataset, lengths)

#create dataloaders
train_dataloader = data.DataLoader(train_set, batch_size=20)
test_dataloader = data.DataLoader(test_set, batch_size=20)

#def train():
