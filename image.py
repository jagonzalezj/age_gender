from PIL import Image, ImageOps
import numpy as np
import cv2
import sys, os


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




def resize_image(image, desire_size=48):
    '''
    convert an numerical input image to the desired
    size in pixels 
    '''
    out_image = cv2.resize(img, dsize=(desire_size, desire_size), interpolation=cv2.INTER_CUBIC)

    pass out_image
 


def face_detection(image):
    '''
    anter a numerical format of a image (array)
    and return the numerical format of the face
    '''

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))

    print("[INFO] Found {0} Faces.".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0),1)
        out_image = image[y:y + h, x:x + w]

    return out_image



def image_to_bw(image):
    '''
    conver a numerical input of an image to a plain 
    black and withe image
    '''
    out_image = np.mean(image, axis=2)

    return out_image


def get_image(path):
    '''
    read image in the path
    path should be string
    '''

    image_out = cv2.imread(path)

    return image_out
    