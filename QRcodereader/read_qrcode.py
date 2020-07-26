import cv2 
import sys


filename = sys,argv[1]

#read the QRCODE length
img = cv2.imread(filename)

#initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()