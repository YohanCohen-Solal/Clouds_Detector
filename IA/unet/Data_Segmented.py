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
img_path = "IA/Data/cumulus/Small_puffy_cumulus_clouds.jpg"
pil_image = Image.open(img_path)
width, height = pil_image.size

# Définissez les nouvelles dimensions de l'image
new_width = 240
new_height = 240

# Redimensionnez l'image
pil_image = pil_image.resize((new_width, new_height), Image.ANTIALIAS)


to_tensor = transforms.ToTensor()
tensor_image = to_tensor(pil_image)
tensor_image = tensor_image.unsqueeze(0)
preds = torch.sigmoid(model(tensor_image))

torchvision.utils.save_image(preds, "pred_1.png")
