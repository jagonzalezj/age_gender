from PIL import Image, ImageOps
import numpy as np

def pixel_mirroring(pixel):
    '''Mirroring a pixel from the prepared dataset'''

    #Turn the pixel list into an array 48,48
    array=np.uint8(pixel.reshape((48,48)))

    #Turn the array into an image object and mirror it
    img=Image.fromarray(array, 'L')
    img=ImageOps.mirror(img)

    #Turn the image back into a pixel list
    img=img.getdata()
    pixel_mirror=np.array(img, dtype=np.float32)

    return pixel_mirror
