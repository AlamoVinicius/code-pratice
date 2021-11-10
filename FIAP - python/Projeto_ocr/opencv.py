import json
import cv2
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Users\VINICIUS\AppData\Local\Programs\Tesseract-OCR\tesseract'
img = cv2.imread('try.jpg')
resultado = tess.image_to_string(img)
resultado = resultado.split('\n')
print(resultado)



with open('pontuacao.json', 'w') as arq_json:
    json.dump(resultado, arq_json)