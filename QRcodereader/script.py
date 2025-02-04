import qrcode

# example data
data = "https://www.thepythoncode.com"

# output file name
filename = "site.png"

# generate qr code
img = qrcode.make(data)

# save img to a file
img.save(filename)

import cv2

# read the QRCODE image
img = cv2.imread("site.png")

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
        