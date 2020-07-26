import qrcode
import sys

# from command line arguments
data = sys.argv[1]
filename = sys.argv[2]

# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)

# import qrcode
# # example data
# data = "https://www.thepythoncode.com"
# # output file name
# filename = "site.png"
# # generate qr code
# img = qrcode.make(data)
# # save img to a file
# img.save(filename)