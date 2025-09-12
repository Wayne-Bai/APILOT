
from PIL import Image
import numpy as np

def getbbox(img_path):
    """Calculate the bounding box of the non-zero regions in the image."""
    img = Image.open(img_path)
    img_arr = np.array(img)
    rows = np.any(img_arr, axis=1)
    cols = np.any(img_arr, axis=0)
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    return rmin, rmax, cmin, cmax
