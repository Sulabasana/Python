# pip3 install pyzbar opencv-python
# or create file req.txt in it opencv-python pyzbar and then pip3 install -r req.txt
from pyzbar import pyzbar
import cv2
# copy images from https://github.com/x4nth055/pythoncode-tutorials/tree/master/general/barcode-reader

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image

