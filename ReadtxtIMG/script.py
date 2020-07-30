import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
data = pytesseract.image_to_string(r'gest.jpg')
data = data.replace(" ","").replace(",","").replace(".","").replace("-","").replace("\n","")
print(data)
number_of_characters = len(data)
print(f"This text contains: {number_of_characters} characters")

