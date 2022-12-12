import torch
import torchvision
import numpy as np
import albumentations as A
import torchvision.transforms as transforms

from unet_model import UNet
from PIL import Image
# Model class must be defined somewhere

model = UNet(n_channels=3, n_classes=1)

model.load_state_dict(torch.load('my_checkpoint.pth.h5')['state_dict'])
model.eval()
img_path = "IA/Data/stratus/stratocumulus.jpeg"
pil_image = Image.open(img_path)

to_tensor = transforms.ToTensor()
tensor_image = to_tensor(pil_image)
tensor_image = tensor_image.unsqueeze(0)
preds = torch.sigmoid(model(tensor_image))

torchvision.utils.save_image(preds, "pred_.png")
