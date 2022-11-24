import cv2
from pathlib import Path


img_path = Path("Clouds_Detector/Data2/whole_sky_images_test/ASC100-1006_321.jpg")
mask_path = Path("Clouds_Detector/Data2/annotation_test/ASC100-1006_321_mask.jpg")

#image = np.array(Image.open(img_path).convert("RGB"))
#mask = np.array(Image.open(mask_path).convert("L"), dtype=np.float32)
#mask[mask == 255.0] = 1.0

img = cv2.imread("Clouds_Detector/Data2/whole_sky_images_test/ASC100-1006_321.jpg", cv2.COLOR_RGB2GRAY)

cv2.imshow("cloud", img)
cv2.waitKey(0)
